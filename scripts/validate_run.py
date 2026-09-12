#!/usr/bin/env python3
"""Validate one explicitly selected run's records, never judge image contents.

No recursive scan, historical migration, mutation, image rendering or generation.
Exit 0: record links are consistent (the image may honestly remain needs_revision).
Exit 1: invalid/inconsistent records. Exit 2: invalid command-line usage.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

CHECK_IDS = tuple([f'C{i:02}' for i in range(1, 5)] +
                  [f'L{i:02}' for i in range(1, 8)] +
                  [f'S{i:02}' for i in range(1, 5)] +
                  [f'W{i:02}' for i in range(1, 6)] +
                  [f'R{i:02}' for i in range(1, 4)])
DIMENSIONS = ('structure', 'large_form', 'facade_depth', 'surface',
              'light_material', 'world', 'request')
ROLES = ('geometry', 'art', 'world', 'surface', 'architecture_form')
STATUSES = {'PASS', 'FAIL', 'UNCERTAIN', 'NOT_REVIEWED', 'NOT_APPLICABLE'}
MODES = {'new_location', 'independent_variant', 'edit_existing', 'own_correction'}
CONDITIONAL_CHECKS = {'L06', 'L07', 'W04', 'W05', 'R02', 'R03'}
SHA = re.compile(r'^[0-9a-f]{64}$')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def aggregate(statuses):
    """All mandatory observations must pass, including noncritical uncertainty."""
    for status, overall in [('FAIL', 'needs_revision'), ('UNCERTAIN', 'uncertain'),
                            ('NOT_REVIEWED', 'not_reviewed')]:
        if status in statuses:
            return overall
    return 'candidate_pass'


class Validator:
    def __init__(self, root, run, stage):
        self.root = Path(root).resolve()
        raw = Path(run)
        self.run = (raw if raw.is_absolute() else self.root / raw).resolve()
        self.stage = stage
        self.errors = []
        self.image_status = 'not_reviewed'

    def need(self, condition, message):
        if not condition:
            self.errors.append(message)
        return bool(condition)

    def nonempty(self, value):
        return isinstance(value, str) and bool(value.strip())

    def path(self, value, base, label, exists=True):
        if not self.need(self.nonempty(value), f'{label}: missing path'):
            return None
        raw = Path(value)
        if not self.need(not raw.is_absolute() and '..' not in raw.parts and '\\' not in value,
                         f'{label}: use a relative path without traversal'):
            return None
        path = (base / raw).resolve()
        if not self.need(path.is_relative_to(base.resolve()), f'{label}: path escapes its root'):
            return None
        if exists and not self.need(path.is_file(), f'{label}: missing file {value}'):
            return None
        return path

    def read(self, value, base, label):
        path = self.path(value, base, label)
        if path is None:
            return {}
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(data, dict):
                raise ValueError('JSON object required')
            return data
        except (OSError, ValueError) as exc:
            self.errors.append(f'{label}: {exc}')
            return {}

    def hashed(self, value, sha, base, label):
        path = self.path(value, base, label)
        self.need(isinstance(sha, str) and bool(SHA.fullmatch(sha)), f'{label}: sha256 required')
        if path is not None:
            self.need(path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'}, f'{label}: expected preserved raster image')
            self.need(sha == digest(path), f'{label}: sha256 mismatch')
        return path

    def objects(self, value, label):
        if not self.need(isinstance(value, list), f'{label}: array required'):
            return []
        for item in value:
            self.need(isinstance(item, dict), f'{label}: object entries required')
        return [item for item in value if isinstance(item, dict)]

    def observation(self, obs, label, applicable=True):
        if not self.need(isinstance(obs, dict), f'{label}: observation object required'):
            return 'NOT_REVIEWED'
        status = obs.get('status')
        self.need(status in STATUSES, f'{label}: invalid status')
        if not applicable:
            self.need(status == 'NOT_APPLICABLE', f'{label}: nonapplicable must be NOT_APPLICABLE')
            return status
        self.need(status != 'NOT_APPLICABLE', f'{label}: applicable observation cannot be N/A')
        if self.stage == 'preflight':
            self.need(status == 'NOT_REVIEWED', f'{label}: preflight cannot claim an observed output judgment')
        if self.stage != 'preflight' and status != 'NOT_REVIEWED':
            self.need(obs.get('basis') == 'actual_image', f'{label}: judgment needs actual_image basis')
            for key in ('evidence', 'positive_evidence', 'forbidden_evidence'):
                self.need(self.nonempty(obs.get(key)), f'{label}: missing {key}')
            regions = obs.get('regions')
            self.need(isinstance(regions, list) and bool(regions) and
                      all(self.nonempty(r) for r in regions), f'{label}: observed regions required')
        return status

    def validate_references(self, data, args, prompt):
        refs = self.read(data.get('references_path'), self.run, 'references')
        self.need(refs.get('run_id') == data.get('run_id'), 'references: run_id mismatch')
        self.need(refs.get('masters_version') == '2.8' and refs.get('execution_rules_version') == '1.9',
                  'references: version mismatch')
        mechanism = refs.get('delivery_mechanism')
        inspected = self.objects(refs.get('inspected_for_planning'), 'inspected_for_planning')
        submitted = self.objects(refs.get('submitted_to_generation'), 'submitted_to_generation')
        inspected_by_id = {}
        catalog = self.read('refs/manifest.json', self.root, 'reference catalog')
        catalog_by_id = {r.get('id'): r for r in self.objects(catalog.get('references'), 'catalog references')}
        catalog_by_hash = {r.get('sha256'): r for r in catalog_by_id.values()}
        for entry in inspected:
            rid = entry.get('id')
            self.need(self.nonempty(rid) and rid not in inspected_by_id, 'inspected: missing/duplicate id')
            inspected_by_id[rid] = entry
            if entry.get('path') is not None:
                self.hashed(entry.get('path'), entry.get('sha256'), self.root, f'reference {rid}')
            else:
                self.need(mechanism == 'num_last_images_to_include' and
                          self.nonempty(entry.get('conversation_image_evidence')),
                          f'reference {rid}: no local file; recent conversation-image evidence required')
                self.need(entry.get('sha256') is None, f'reference {rid}: cannot verify hash without local source')
            self.need(entry.get('inspected') is True, f'reference {rid}: not actually inspected')
            self.need(entry.get('role') in ROLES + ('edit_target', 'comparison'), f'reference {rid}: invalid role')
            self.need(self.nonempty(entry.get('scope')) and self.nonempty(entry.get('exclusions')),
                      f'reference {rid}: specific scope and exclusions required')
        self.inspected_references = inspected_by_id
        submitted_ids = []
        submitted_paths = []
        for index, entry in enumerate(submitted, 1):
            rid = entry.get('id')
            self.need(rid not in submitted_ids, 'submitted: duplicate reference id')
            submitted_ids.append(rid)
            prior = inspected_by_id.get(rid, {})
            self.need(bool(prior), f'submitted {rid}: not in inspected list')
            for key in ('path', 'sha256', 'role', 'scope', 'exclusions', 'conversation_image_evidence'):
                self.need(entry.get(key) == prior.get(key), f'submitted {rid}: {key} mismatch')
            self.need(entry.get('input_index') == index, f'submitted {rid}: input_index mismatch')
            path = self.path(entry.get('path'), self.root, f'submitted {rid}') if entry.get('path') is not None else None
            if path:
                submitted_paths.append(str(path))
            canonical = catalog_by_id.get(rid) or catalog_by_hash.get(entry.get('sha256'))
            explicit = (entry.get('authorization_kind') == 'explicit_current_request' and
                        all(self.nonempty(entry.get(k)) for k in ('authorization_evidence', 'authorization_source', 'authorization_quote')))
            explicit_edit = explicit and entry.get('role') == 'edit_target' and data.get('request_mode') in {'edit_existing', 'own_correction'}
            if entry.get('authorization_kind') == 'explicit_current_request':
                self.need(explicit, f'submitted {rid}: explicit request source, quote and evidence required')
            if entry.get('role') == 'edit_target':
                self.need(data.get('request_mode') in {'edit_existing', 'own_correction'}, f'submitted {rid}: edit target requires edit/correction mode')
                self.need(explicit_edit or entry.get('authorization_kind') == 'own_correction_target',
                          f'submitted {rid}: edit target needs current explicit request or own correction provenance')
            if canonical:
                self.need(path is None or entry.get('sha256') == canonical.get('sha256'), f'submitted {rid}: catalog hash mismatch')
                approved_roles = {'master01': {'geometry'}, 'master02': {'geometry'},
                                  'master03': {'art', 'surface', 'architecture_form'}, 'master04': {'world'},
                                  'style_support': {'surface'}, 'architecture_form': {'architecture_form'},
                                  'architecture_example': {'architecture_form', 'edit_target'}}
                if canonical.get('group') in approved_roles:
                    self.need(explicit_edit or entry.get('role') in approved_roles[canonical['group']],
                              f'submitted {rid}: role exceeds approved catalog scope')
                allowed = canonical.get('generation_input_allowed') is True
                self.need(allowed or explicit, f'submitted {rid}: comparison/review-only source needs explicit current request')
                if not allowed:
                    self.need(entry.get('role') != 'geometry', f'submitted {rid}: failed geometry is not a positive geometry source')
            else:
                self.need(entry.get('authorization_kind') in {'scene_structure_guide', 'explicit_current_request', 'own_correction_target'},
                          f'submitted {rid}: unregistered input lacks scoped authorization')
                self.need(self.nonempty(entry.get('authorization_evidence')), f'submitted {rid}: missing authorization evidence')
                if entry.get('authorization_kind') == 'scene_structure_guide':
                    self.need(entry.get('role') == 'geometry' and path and path.is_relative_to(self.run),
                              f'submitted {rid}: scene guide must be current run geometry')
                if entry.get('authorization_kind') == 'own_correction_target':
                    self.need(data.get('request_mode') in {'edit_existing', 'own_correction'} and entry.get('role') == 'edit_target',
                              f'submitted {rid}: correction target used outside own edit')
            self.need(entry.get('role') != 'comparison', f'submitted {rid}: comparison role cannot be an input')
        self.need(len(set(submitted_paths)) == len(submitted_paths), 'submitted: duplicate image paths')
        contract = refs.get('tool_contract', {})
        self.need(isinstance(contract, dict), 'tool_contract: object required')
        if not isinstance(contract, dict):
            contract = {}
        self.need(self.nonempty(contract.get('contract_source')), 'tool_contract: current source required')
        mechanism = refs.get('delivery_mechanism')
        paths = args.get('referenced_image_paths')
        recent = args.get('num_last_images_to_include')
        self.need(not (paths is not None and recent is not None), 'tool arguments: two image mechanisms supplied')
        if paths is not None:
            self.need(isinstance(paths, list) and all(isinstance(p, str) for p in paths), 'tool arguments: paths must be string array')
            self.need(paths == submitted_paths, 'tool arguments: exact submitted image paths/order mismatch')
            self.need(mechanism == 'referenced_image_paths', 'references: delivery mechanism mismatch')
        elif recent is not None:
            self.need(type(recent) is int and 1 <= recent <= 5, 'tool arguments: recent image count must be 1..5')
            self.need(recent == len(submitted), 'tool arguments: recent selected count mismatch')
            self.need(mechanism == 'num_last_images_to_include', 'references: delivery mechanism mismatch')
            for entry in submitted:
                self.need(self.nonempty(entry.get('conversation_image_evidence')), 'recent image: conversation mapping required')
        else:
            self.need(not submitted and mechanism == 'none', 'references: input records without image arguments')
        self.need(type(refs.get('actual_submitted_image_count')) is int and
                  refs.get('actual_submitted_image_count') == len(submitted), 'references: actual image count mismatch')
        expected_delivery = 'planned' if self.stage == 'preflight' else 'submitted'
        self.need(refs.get('delivery_status') == expected_delivery, f'references: expected {expected_delivery} delivery status')
        for key in ('referenced_image_paths', 'num_last_images_to_include'):
            limits = contract.get('parameter_specific_limits', {})
            limit = limits.get(key + '_max_count', {}) if isinstance(limits, dict) else {}
            if isinstance(limit, dict) and limit.get('status') == 'confirmed':
                self.need(type(limit.get('value')) is int and limit['value'] >= 0 and self.nonempty(limit.get('evidence')),
                          f'contract {key}: confirmed limit requires value and evidence')
                if mechanism == key and type(limit.get('value')) is int:
                    self.need(len(submitted) <= limit['value'], f'contract {key}: selected count exceeds confirmed limit')
        metadata = refs.get('submitted_prompt', {})
        self.need(isinstance(metadata, dict), 'submitted_prompt: object required')
        if isinstance(metadata, dict):
            self.need(metadata.get('path') == data.get('prompt_path'), 'submitted_prompt: path mismatch')
            for key, actual in [('character_count', len(prompt)), ('utf8_byte_count', len(prompt.encode('utf-8'))),
                                ('whitespace_word_count', len(prompt.split()))]:
                if metadata.get(key) is not None:
                    self.need(type(metadata[key]) is int and metadata[key] == actual, f'submitted_prompt: {key} mismatch')
            self.need(metadata.get('sha256') == hashlib.sha256(prompt.encode('utf-8')).hexdigest(), 'submitted_prompt: sha256 mismatch')
            returned_evidence = metadata.get('returned_metadata_evidence', {})
            for key in ('returned_token_usage', 'returned_model_info', 'returned_revised_prompt'):
                if metadata.get(key) is None:
                    continue
                proof = returned_evidence.get(key, {}) if isinstance(returned_evidence, dict) else {}
                if not self.need(isinstance(proof, dict) and self.nonempty(proof.get('response_path')) and
                                 self.nonempty(proof.get('json_pointer')), f'{key}: actual returned metadata evidence required'):
                    continue
                value = self.read(proof['response_path'], self.run, f'{key} response')
                pointer = proof['json_pointer']
                self.need(pointer.startswith('/'), f'{key}: JSON pointer must begin with /')
                try:
                    for part in pointer.lstrip('/').split('/'):
                        part = part.replace('~1', '/').replace('~0', '~')
                        value = value[int(part)] if isinstance(value, list) else value[part]
                    self.need(value == metadata[key], f'{key}: does not match actual returned value')
                except (KeyError, IndexError, TypeError, ValueError):
                    self.errors.append(f'{key}: returned JSON pointer not found')
        role_review = self.objects(refs.get('role_preservation_review'), 'role_preservation_review')
        self.need({r.get('role') for r in role_review} == set(ROLES), 'reference roles: all five roles must be reviewed')
        for row in role_review:
            ids = row.get('current_input_ids')
            self.need(isinstance(ids, list) and all(rid in submitted_ids for rid in ids), 'role review: invalid input ids')
            self.need(self.nonempty(row.get('coverage_evidence')), 'role review: visual/text coverage evidence required')
            if not ids:
                self.need(self.nonempty(row.get('text_only_reason')), f'role review {row.get("role")}: omission reason required')
            if data.get('request_mode') in {'edit_existing', 'own_correction'}:
                self.need(self.nonempty(row.get('change_reason')) and self.nonempty(row.get('preservation_evidence')),
                          'role review: correction needs reference change and preservation evidence')
        return set(submitted_ids)

    def validate_comparison(self, data, requirement_ids):
        comp = data.get('comparison', {})
        if not self.need(isinstance(comp, dict), 'comparison: object required'):
            return []
        applies = data.get('request_mode') in {'edit_existing', 'own_correction'}
        self.need(comp.get('applicable') is applies, 'comparison: applicability must match edit/correction mode')
        if not applies:
            self.need(self.nonempty(comp.get('na_reason')), 'comparison: N/A reason required')
            return []
        baseline = comp.get('baseline', {})
        if not self.need(isinstance(baseline, dict), 'comparison: baseline object required'):
            return []
        baseline_path = None
        if baseline.get('image_path') is not None:
            baseline_path = self.hashed(baseline.get('image_path'), baseline.get('sha256'), self.root, 'comparison baseline')
        else:
            source = getattr(self, 'inspected_references', {}).get(baseline.get('reference_id'), {})
            self.need(source.get('role') == 'edit_target' and source.get('path') is None and
                      self.nonempty(baseline.get('conversation_image_evidence')) and
                      baseline.get('conversation_image_evidence') == source.get('conversation_image_evidence') and
                      baseline.get('sha256') is None, 'comparison: conversation-only baseline must link the inspected edit target')
        candidate_path = (self.run / data.get('candidate', {}).get('image_path', '')).resolve()
        self.need(baseline_path != candidate_path, 'comparison: baseline cannot be the current candidate itself')
        if self.stage == 'preflight':
            self.need(self.nonempty(comp.get('preservation_plan')), 'comparison: preflight preservation plan required')
            return []
        self.need(baseline.get('actually_opened') is True, 'comparison: baseline not actually opened')
        rows = self.objects(comp.get('dimensions'), 'comparison dimensions')
        self.need(len(rows) == len(DIMENSIONS) and {r.get('dimension') for r in rows} == set(DIMENSIONS),
                  'comparison: all seven dimensions required exactly once')
        regressions = []
        for row in rows:
            for key in ('before', 'after', 'evidence'):
                self.need(self.nonempty(row.get(key)), f'comparison {row.get("dimension")}: missing {key}')
            self.need(row.get('change') in {'improved', 'preserved', 'regressed', 'uncertain', 'not_reviewed', 'not_applicable'}, 'comparison: invalid change')
            ids = row.get('requirement_ids')
            self.need(isinstance(ids, list) and bool(ids) and all(rid in requirement_ids for rid in ids),
                      'comparison: linked requirement ids required')
            if row.get('change') == 'regressed':
                regressions.extend(ids or [])
        self.need(sorted(set(comp.get('unresolved_regressions', []))) == sorted(set(regressions)), 'comparison: unresolved regression list mismatch')
        if any(row.get('change') == 'not_reviewed' for row in rows) and not regressions:
            r03 = next((c for c in data.get('checks', []) if c.get('id') == 'R03'), {})
            self.need(r03.get('status') in {'NOT_REVIEWED', 'FAIL', 'UNCERTAIN'}, 'R03: unreviewed comparison cannot be PASS')
        if any(row.get('change') == 'uncertain' for row in rows) and not regressions:
            r03 = next((c for c in data.get('checks', []) if c.get('id') == 'R03'), {})
            self.need(r03.get('status') in {'UNCERTAIN', 'FAIL'}, 'R03: uncertain comparison cannot be PASS')
        return regressions

    def validate_selection(self, data):
        selection = data.get('selection', {})
        if not self.need(isinstance(selection, dict), 'selection: object required'):
            return
        self.need(selection.get('selected') is True, 'selection stage requires an explicitly selected deliverable')
        self.need(selection.get('qa_status') == self.image_status, 'selection: QA status mismatch')
        self.need(self.nonempty(selection.get('reason')), 'selection: missing selection reason')
        self.need(selection.get('claims_overall_pass') is (self.image_status == 'candidate_pass'), 'selection: false overall-pass promotion')
        if self.image_status != 'candidate_pass':
            self.need(self.nonempty(selection.get('unresolved_limitations')) and self.nonempty(selection.get('stop_reason')),
                      'selection: honest incomplete delivery needs limitations and stop reason')
        candidates = self.objects(selection.get('considered_candidates'), 'considered_candidates')
        self.need(bool(candidates), 'selection: considered candidates required')
        current = str((self.run / data.get('candidate', {}).get('image_path', '')).relative_to(self.root))
        self.need(sum(c.get('image_path') == current for c in candidates) == 1, 'selection: selected candidate must occur once')
        if data.get('comparison', {}).get('applicable'):
            baseline = data['comparison'].get('baseline', {})
            self.need(any((c.get('image_path') == baseline.get('image_path') if baseline.get('image_path') is not None else
                           c.get('reference_id') == baseline.get('reference_id') and
                           c.get('conversation_image_evidence') == baseline.get('conversation_image_evidence')) for c in candidates),
                      'selection: known correction baseline missing from considered candidates')
        seen = set()
        for item in candidates:
            label = 'candidate comparison'
            if item.get('image_path') is not None:
                identity = self.hashed(item.get('image_path'), item.get('sha256'), self.root, label)
            else:
                baseline = data.get('comparison', {}).get('baseline', {})
                self.need(data.get('comparison', {}).get('applicable') and baseline.get('image_path') is None and
                          self.nonempty(item.get('reference_id')) and item.get('reference_id') == baseline.get('reference_id') and
                          self.nonempty(item.get('conversation_image_evidence')) and
                          item.get('conversation_image_evidence') == baseline.get('conversation_image_evidence') and
                          item.get('sha256') is None, 'selection: local-file-free candidate must be the linked conversation baseline')
                identity = ('conversation', item.get('reference_id'))
            self.need(identity not in seen, 'selection: duplicate considered candidate')
            seen.add(identity)
            self.need(type(item.get('actually_opened')) is bool, 'selection: candidate opened flag required')
            if item.get('qa_status') != 'not_reviewed':
                self.need(item.get('actually_opened') is True, 'selection: judged candidate not actually opened')
            self.need(item.get('qa_status') in {'candidate_pass', 'needs_revision', 'uncertain', 'not_reviewed'}, 'selection: invalid candidate QA status')
            dims = item.get('dimensions', {})
            self.need(isinstance(dims, dict) and set(dims) == set(DIMENSIONS) and
                      all(self.nonempty(v) for v in dims.values()), 'selection: seven-dimension evidence required for every candidate')
            if item.get('image_path') == current:
                self.need(item.get('qa_status') == self.image_status, 'selection: selected comparison QA mismatch')
                self.need(item.get('actually_opened') is data['candidate'].get('actually_opened'),
                          'selection: selected candidate opened flag mismatch')
        manifest = self.read(selection.get('manifest_path'), self.root, 'final manifest')
        entries = self.objects(manifest.get('images'), 'final manifest images')
        matches = [e for e in entries if e.get('source') == current]
        self.need(len(matches) == 1, 'selection: exactly one matching final manifest entry required')
        if len(matches) == 1:
            entry = matches[0]
            for key, expected in [('qa_status', self.image_status), ('selection_reason', selection.get('reason')),
                                  ('sha256', data.get('candidate', {}).get('sha256'))]:
                self.need(entry.get(key) == expected, f'final manifest: {key} mismatch')
            name = entry.get('filename')
            self.need(self.nonempty(name) and Path(name).name == name and '\\' not in name, 'final manifest: invalid filename')

    def validate(self):
        if not self.need(self.run.is_relative_to(self.root / 'outputs') and self.run != self.root / 'outputs' and
                         not self.run.is_relative_to(self.root / 'outputs/final'), 'run must be a single outputs run directory'):
            return self.report()
        data = self.read('requirements.json', self.run, 'requirements ledger')
        if not data:
            return self.report()
        self.need(data.get('schema_version') == 1, 'ledger: unsupported schema version')
        self.need(data.get('run_id') == self.run.name, 'ledger: run_id must match directory name')
        self.need(data.get('masters_version') == '2.8' and data.get('execution_rules_version') == '1.9', 'ledger: version mismatch')
        self.need(data.get('request_mode') in MODES, 'ledger: invalid request_mode')
        self.need(type(data.get('requested_final_count')) is int and data['requested_final_count'] > 0,
                  'ledger: positive requested_final_count required')
        self.need(self.nonempty(data.get('request_original')), 'ledger: current original request required')
        prompt_file = self.path(data.get('prompt_path'), self.run, 'prompt')
        prompt = prompt_file.read_text(encoding='utf-8') if prompt_file else ''
        args = self.read(data.get('tool_arguments_path'), self.run, 'tool arguments')
        self.need(args.get('prompt') == prompt, 'tool arguments: exact prompt differs from saved prompt')
        self.need(set(args) <= {'prompt', 'referenced_image_paths', 'num_last_images_to_include'}, 'tool arguments: unsupported native imagegen metadata/parameter')
        self.need(not re.search(r'\{\{|\}\}|<TODO>|\bTODO\b', prompt), 'prompt: unresolved placeholder')
        refs = self.validate_references(data, args, prompt)
        rows = self.objects(data.get('requirements'), 'requirements')
        by_id = {}
        statuses = []
        by_check = {cid: [] for cid in CHECK_IDS}
        for row in rows:
            rid = row.get('id')
            self.need(self.nonempty(rid) and rid not in by_id, 'requirements: missing/duplicate id')
            by_id[rid] = row
            applies = row.get('applicable')
            self.need(type(applies) is bool and type(row.get('critical')) is bool, f'{rid}: applicability/critical booleans required')
            for key in ('source', 'positive_visual', 'forbidden_visual'):
                self.need(self.nonempty(row.get(key)), f'{rid}: missing {key}')
            ids = row.get('check_ids')
            self.need(isinstance(ids, list) and bool(ids) and all(cid in CHECK_IDS for cid in ids), f'{rid}: valid check_ids required')
            for cid in ids or []:
                if cid in by_check:
                    by_check[cid].append(row)
            if applies:
                clauses = row.get('prompt_clauses')
                self.need(isinstance(clauses, list) and bool(clauses), f'{rid}: exact prompt clauses required')
                for clause in clauses or []:
                    self.need(self.nonempty(clause) and clause in prompt and clause.strip().strip('# ').upper() not in
                              {'ART', 'STRUCTURE', 'CURRENT SCENE', 'STRUCTURE MUST KEEP', 'ART / REFERENCE ROLES'},
                              f'{rid}: clause missing from exact prompt or merely a section title')
                linked = row.get('reference_ids')
                self.need(isinstance(linked, list) and all(ref in refs for ref in linked), f'{rid}: invalid submitted reference ids')
                if not linked:
                    self.need(self.nonempty(row.get('text_only_reason')), f'{rid}: text-only reason required')
                self.need(self.nonempty(row.get('planned_evidence')), f'{rid}: planned evidence required')
            else:
                self.need(self.nonempty(row.get('na_reason')), f'{rid}: N/A reason required')
            status = self.observation(row.get('observation'), str(rid), bool(applies))
            if self.stage != 'preflight':
                statuses.append(status)
        checks = self.objects(data.get('checks'), 'checks')
        self.need(len(checks) == len(CHECK_IDS) and {c.get('id') for c in checks} == set(CHECK_IDS), 'checks: every required ID exactly once')
        check_lookup = {c.get('id'): c for c in checks}
        for check in checks:
            cid = check.get('id')
            linked = by_check.get(cid, [])
            self.need(bool(linked), f'{cid}: missing requirement mapping')
            applicable = any(r.get('applicable') is True for r in linked)
            self.need(check.get('applicable') is applicable, f'{cid}: applicability disagrees with ledger')
            if not applicable:
                self.need(self.nonempty(check.get('na_reason')), f'{cid}: N/A reason required')
                if cid not in CONDITIONAL_CHECKS:
                    exception = check.get('exception', {})
                    self.need(isinstance(exception, dict) and self.nonempty(exception.get('source')) and
                              self.nonempty(exception.get('quote')), f'{cid}: mandatory-check N/A needs current user exception source and quote')
            if cid == 'R02':
                self.need(applicable is (data.get('request_mode') in {'new_location', 'independent_variant'}), 'R02: only new locations/independent variants')
            if cid == 'R03':
                self.need(applicable is (data.get('request_mode') in {'edit_existing', 'own_correction'}), 'R03: required for same-scene edits/corrections')
            status = self.observation(check, str(cid), applicable)
            if self.stage != 'preflight':
                expected = aggregate([r.get('observation', {}).get('status') for r in linked])
                mapped = {'candidate_pass': 'PASS' if applicable else 'NOT_APPLICABLE', 'needs_revision': 'FAIL',
                          'uncertain': 'UNCERTAIN', 'not_reviewed': 'NOT_REVIEWED'}[expected]
                self.need(status == mapped, f'{cid}: status contradicts linked requirement observations')
                statuses.append(status)
        if self.stage != 'preflight':
            c04, s04 = check_lookup.get('C04', {}), check_lookup.get('S04', {})
            if c04.get('status') == s04.get('status') == 'FAIL':
                self.need(c04.get('evidence') != s04.get('evidence'),
                          'S04: geometry FAIL evidence copied verbatim; independent visual-form observation required')
        if self.stage == 'preflight':
            self.validate_comparison(data, set(by_id))
            return self.report()
        candidate = data.get('candidate', {})
        self.need(isinstance(candidate, dict), 'candidate: object required')
        if not isinstance(candidate, dict):
            candidate = {}
        self.hashed(candidate.get('image_path'), candidate.get('sha256'), self.run, 'actual candidate')
        judged = any(s in {'PASS', 'FAIL', 'UNCERTAIN'} for s in statuses)
        if judged:
            self.need(candidate.get('actually_opened') is True and candidate.get('observation_basis') == 'actual_image' and
                      self.nonempty(candidate.get('reviewed_at')), 'candidate: unseen/planned image cannot receive observed judgments')
        if not judged and candidate.get('actually_opened') is False:
            self.need(candidate.get('observation_basis') == 'not_reviewed', 'candidate: unopened output must retain not_reviewed basis')
        regressions = self.validate_comparison(data, set(by_id))
        if regressions:
            self.need(check_lookup.get('R03', {}).get('status') == 'FAIL', 'R03: unresolved regression requires FAIL')
        self.image_status = aggregate(statuses + (['FAIL'] if regressions else []))
        self.need(candidate.get('overall_status') == self.image_status, 'candidate: overall status contradicts required checks')
        result = self.read(candidate.get('result_path'), self.run, 'result')
        self.need(result.get('status') == self.image_status, 'result: overall status mismatch')
        self.need(result.get('image_path') == candidate.get('image_path') and result.get('sha256') == candidate.get('sha256'),
                  'result: image/hash mismatch')
        if self.stage == 'selection':
            self.validate_selection(data)
        return self.report()

    def report(self):
        return {'record_status': 'FAIL' if self.errors else 'PASS', 'stage': self.stage,
                'run': str(self.run), 'image_qa_status': self.image_status,
                'image_contents_automatically_judged': False, 'errors': self.errors}


def validate_run(root, run, stage):
    checker = Validator(root, run, stage)
    try:
        return checker.validate()
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        checker.errors.append(f'Malformed or unreadable record: {type(exc).__name__}: {exc}')
        return checker.report()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', required=True, help='One outputs run; old runs are never scanned automatically')
    parser.add_argument('--stage', required=True, choices=('preflight', 'review', 'selection'))
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    report = validate_run(args.root, args.run, args.stage)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"RECORD {report['record_status']}: {report['stage']}; image QA={report['image_qa_status']}; no automated image judgment")
        for error in report['errors']:
            print('- ' + error)
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())

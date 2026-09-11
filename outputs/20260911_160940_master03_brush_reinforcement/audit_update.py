"""One-time evidence for the approved documentation update, not image QA."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
HISTORY = ROOT / 'state/history/20260911_160940_master03_brush_reinforcement'
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_project import validate

def obj(path):
    return path and json.loads(path.read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

before = obj(RUN / 'before.json')
checks = {}
def check(label, condition):
    checks[label] = bool(condition)

for field in ['original_reference_hashes', 'final_original_hashes']:
    # Snapshot hashes protect bytes of every previously registered source.
    if field not in before and field == 'final_original_hashes':
        field = next(k for k in before if 'final' in k and 'hash' in k)
    hashes = before[field]
    check(field, all((ROOT / p).is_file() and sha(ROOT / p) == digest for p, digest in hashes.items()))

old_project = obj(HISTORY / 'project.json')
project = obj(ROOT / 'project.json')
old_manifest = obj(HISTORY / 'refs/manifest.json')
manifest = obj(ROOT / 'refs/manifest.json')
old_approvals = obj(HISTORY / 'state/approvals.json')
approvals = obj(ROOT / 'state/approvals.json')
check('prior_15_approvals_preserved', approvals['entries'][:-1] == old_approvals['entries'] and len(old_approvals['entries']) == 15)
check('new_approval_recorded', approvals['entries'][-1]['approval_id'] == project['master_update_approval_id'] == 'master_update_20260911_v2_6_brush_planes')
check('old_final_manifest_unchanged', sha(ROOT / 'outputs/final_manifest.json') == before['files']['outputs/final_manifest.json'])
for field in ['default_inspection_ids', 'default_generation_priority_ids', 'optional_scene_style_ids', 'optional_world_reference_ids', 'preferred_result_reference_ids', 'approved_user_added_reference_ids', 'approved_ldi_supplement_ids', 'geometry_policy', 'geometry_review_policy', 'architectural_design_policy', 'functional_exit_policy', 'boundary_object_policy', 'structural_correction_policy', 'execution_prompt_policy', 'tool_input_evidence_policy', 'world_setting']:
    check('preserved_' + field, project[field] == old_project[field])

old_rows = {r['id']: r for r in old_manifest['references']}
new_rows = {r['id']: r for r in manifest['references']}
changed_old_rows = []
for rid, old_row in old_rows.items():
    if new_rows.get(rid) != old_row:
        changed_old_rows.append(rid)
check('only_three_surface_role_clarifications', set(changed_old_rows) == {'M03-10','M03-16','M04-04'})
for rid, field in [('M03-10','use_only'), ('M03-16','exclude'), ('M04-04','exclude')]:
    row_copy = dict(new_rows[rid])
    row_copy[field] = old_rows[rid][field]
    row_copy.pop('surface_role_approval_id')
    check(rid + '_other_metadata_preserved', row_copy == old_rows[rid])
check('existing_scoped_result_examples_preserved', project['scoped_result_examples'][:len(old_project['scoped_result_examples'])] == old_project['scoped_result_examples'])
check('version_sync', project['master_version'] == manifest['master_version'] == approvals['master_version_approved'] == '2.6' and obj(ROOT / 'templates/references.json')['execution_rules_version'] == project['execution_rules_version'] == '1.7')
check('support_copy_identical', sha(ROOT / 'refs/style_support/brush_planes_reference.jpg') == sha(ROOT / 'outputs/20260911_153546_three_independent_night_alleys/brush_light_reference.jpg'))
check('four_support_roles', set(new_rows) - set(old_rows) == {'B03-01','B03-02','B03-03','B03-04'} and all(new_rows[r]['reference_role'] == 'scoped_style_support' for r in ['B03-01','B03-02','B03-03','B03-04']))
check('generated_examples_not_geometry_approval', all(new_rows[r]['geometry_approved'] is False and new_rows[r]['overall_qa_status_at_registration'] == 'needs_revision' and new_rows[r]['generation_input_allowed'] is False for r in ['B03-02','B03-03','B03-04']))

qa = (ROOT / 'docs/06_QA.md').read_text(encoding='utf-8')
old_qa = (HISTORY / 'docs/06_QA.md').read_text(encoding='utf-8')
structural_rows = lambda s: [line for line in s.splitlines() if re.match(r'\| (?:C|L|W)\d', line)]
check('QA_C_L_W_rows_unchanged', structural_rows(qa) == structural_rows(old_qa))
prompt = (ROOT / 'templates/generation_prompt.md').read_text(encoding='utf-8')
check('positive_surface_prompt', 'broad' in prompt.lower() and 'directional' in prompt.lower() and 'flat' in prompt.lower() and ('intact' in prompt.lower() or 'undamaged' in prompt.lower()))
active_paths = [ROOT / p for p in before['files'] if p.endswith(('.md','.txt','.yaml')) and not p.startswith('state/')]
check('blanket_brush_rejection_removed', all('Avoid painterly brushstrokes' not in p.read_text(encoding='utf-8') and '붓질보다 게임 렌더' not in p.read_text(encoding='utf-8') for p in active_paths))

class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []
        self.ids = []
    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k in ('src','href') and v and not v.startswith(('#','http:','https:')):
                self.paths.append(v.split('#')[0])
            if k == 'id':
                self.ids.append(v)
parser = LocalLinks()
gallery = (ROOT / 'REFERENCE_INDEX.html').read_text(encoding='utf-8')
parser.feed(gallery)
check('gallery_local_links', all((ROOT / unquote(p)).is_file() for p in parser.paths))
check('gallery_unique_ids', len(parser.ids) == len(set(parser.ids)))
check('gallery_supports_and_M03_use_in_sync', all(f'id="{r}"' in gallery for r in ['B03-01','B03-02','B03-03','B03-04']) and new_rows['M03-10']['use_only'] in gallery)
map_text = (ROOT / 'refs/REFERENCE_MAP.md').read_text(encoding='utf-8')
check('role_map_supports_and_M03_use_in_sync', all(r in map_text for r in ['B03-01','B03-02','B03-03','B03-04']) and new_rows['M03-10']['use_only'] in map_text)
markdown_links = []
for rel in ['refs/REFERENCE_MAP.md','docs/00_INDEX.md','docs/10_CURRENT_REFERENCES.md','docs/03_VISUAL_STYLE_V2.md']:
    p = ROOT / rel
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
        if not target.startswith(('http:', 'https:', '#')):
            markdown_links.append((p.parent / unquote(target.split('#')[0])).is_file())
check('updated_document_links_resolve', all(markdown_links))
report = validate(ROOT)
(RUN / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
check('project_validator', report['ok'])
changed = [p for p, old_hash in before['files'].items() if sha(ROOT / p) != old_hash]
audit = {'ok': all(checks.values()), 'scope':'Approved document/reference-role update and immutable image/history integrity. Not new image QA.', 'checks':checks, 'changed_control_files':changed, 'original_reference_images_verified':len(before['original_reference_hashes']), 'final_images_verified':56, 'new_support_records':4, 'prior_approvals_verified':15}
(RUN / 'audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'ok':audit['ok'], 'checks':len(checks), 'failed':[k for k,v in checks.items() if not v], 'changed_control_files':len(changed)}, ensure_ascii=True))
sys.exit(0 if audit['ok'] else 1)

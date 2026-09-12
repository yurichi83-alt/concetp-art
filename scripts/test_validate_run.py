#!/usr/bin/env python3
"""Regression tests for record integrity, with synthetic images in temp directories.

These fixtures are fabricated records for testing, not real visual QA evidence.
"""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from validate_run import CHECK_IDS, DIMENSIONS, ROLES, validate_run


def sha(data):
    return hashlib.sha256(data).hexdigest()


class RunValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.run = self.root / 'outputs/current'
        self.run.mkdir(parents=True)
        (self.root / 'refs').mkdir()
        self.image = b'Synthetic image bytes: validator never interprets pixels.'
        self.ref = b'Synthetic reference bytes.'
        (self.run / 'image.png').write_bytes(self.image)
        (self.root / 'refs/source.png').write_bytes(self.ref)
        self.write('refs/manifest.json', {'references': [{'id': 'M01-01', 'path': 'refs/source.png',
                   'sha256': sha(self.ref), 'group': 'master01', 'generation_input_allowed': True}]})
        self.data = self.fixture()
        self.save()

    def write(self, rel, data):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')

    @staticmethod
    def obs(status='PASS'):
        return {'status': status, 'basis': 'actual_image', 'regions': ['synthetic test region'],
                'evidence': 'Fabricated unit-test observation.', 'positive_evidence': 'Synthetic positive observation.',
                'forbidden_evidence': 'Synthetic prohibited-feature observation.'}

    def fixture(self):
        requirements=[]
        checks=[]
        clauses=[]
        for cid in CHECK_IDS:
            applies=cid!='R03'
            clause=f'The scene-specific visual requirement for {cid} is explicitly stated.'
            clauses.append(clause)
            requirements.append({'id':cid+'-01','source':'synthetic current requirement','check_ids':[cid],
                'applicable':applies,'critical':True,'na_reason':'' if applies else 'First scene has no edit baseline.',
                'positive_visual':'Synthetic positive condition.','forbidden_visual':'Synthetic prohibited condition.',
                'prompt_clauses':[clause],'reference_ids':['M01-01'],'text_only_reason':'',
                'planned_evidence':'Synthetic planning evidence.', 'observation':self.obs() if applies else self.obs('NOT_APPLICABLE')})
            checks.append({'id':cid,'applicable':applies,'na_reason':requirements[-1]['na_reason'],
                           **(self.obs() if applies else self.obs('NOT_APPLICABLE'))})
        prompt='\n'.join(clauses)
        (self.run / 'generation_prompt.md').write_text(prompt, encoding='utf-8')
        self.args={'prompt':prompt,'referenced_image_paths':[str(self.root / 'refs/source.png')]}
        entry={'id':'M01-01','path':'refs/source.png','sha256':sha(self.ref),'role':'geometry',
               'scope':'Base and framing.','exclusions':'No copied camera or text.','inspected':True}
        self.refs={'run_id':'current','masters_version':'2.8','execution_rules_version':'1.9',
              'inspected_for_planning':[entry], 'submitted_to_generation':[{**entry,'input_index':1}],
              'delivery_mechanism':'referenced_image_paths','delivery_status':'submitted','actual_submitted_image_count':1,
              'tool_contract':{'contract_source':'Synthetic native contract fixture.','parameter_specific_limits':{}},
              'submitted_prompt':{'path':'generation_prompt.md','sha256':sha(prompt.encode()),'character_count':len(prompt)},
              'role_preservation_review':[{'role':r,'current_input_ids':['M01-01'] if r=='geometry' else [],
                'coverage_evidence':'Synthetic role coverage.','text_only_reason':'Synthetic justified text planning.',
                'change_reason':'No input change.','preservation_evidence':'Synthetic maintained role evidence.'} for r in ROLES]}
        return {'schema_version':1,'masters_version':'2.8','execution_rules_version':'1.9','run_id':'current',
            'request_mode':'new_location','request_original':'Synthetic current request.','requested_final_count':1,
            'prompt_path':'generation_prompt.md','tool_arguments_path':'tool_arguments.json','references_path':'references.json',
            'requirements':requirements,'checks':checks,
            'candidate':{'image_path':'image.png','sha256':sha(self.image),'actually_opened':True,
                         'observation_basis':'actual_image','reviewed_at':'2026-09-12T00:00:00Z',
                         'overall_status':'candidate_pass','result_path':'result.json'},
            'comparison':{'applicable':False,'na_reason':'First synthetic scene, no edit baseline.'},
            'selection':{'selected':True,'qa_status':'candidate_pass','claims_overall_pass':True,'reason':'Synthetic choice.',
                'manifest_path':'outputs/final_manifest.json','unresolved_limitations':'','stop_reason':'',
                'considered_candidates':[{'image_path':'outputs/current/image.png','sha256':sha(self.image),
                  'actually_opened':True,'qa_status':'candidate_pass','dimensions':{d:'Synthetic observed '+d for d in DIMENSIONS}}]}}

    def save(self):
        self.write('outputs/current/requirements.json', self.data)
        self.write('outputs/current/references.json', self.refs)
        self.write('outputs/current/tool_arguments.json', self.args)
        c=self.data['candidate']
        self.write('outputs/current/result.json', {'status':c['overall_status'],'image_path':c['image_path'],'sha256':c['sha256']})
        self.write('outputs/final_manifest.json', {'images':[{'filename':'current__image.png','source':'outputs/current/image.png',
            'sha256':sha(self.image),'qa_status':self.data['selection']['qa_status'],'selection_reason':self.data['selection']['reason']}]})

    def validate(self, stage='review'):
        self.save()
        return validate_run(self.root, 'outputs/current', stage)

    def assert_valid(self, stage='review'):
        report=self.validate(stage)
        self.assertEqual(report['errors'], [], report)
        self.assertFalse(report['image_contents_automatically_judged'])
        return report

    def assert_error(self, needle, stage='review'):
        report=self.validate(stage)
        self.assertEqual(report['record_status'], 'FAIL', report)
        self.assertTrue(any(needle in e for e in report['errors']), report['errors'])

    def set_check(self, cid, status):
        for row in self.data['requirements']:
            if cid in row['check_ids']:
                row['observation']['status']=status
        for check in self.data['checks']:
            if check['id']==cid:
                check['status']=status

    def make_edit(self):
        self.data['request_mode']='own_correction'
        for cid, applies in [('R02',False),('R03',True)]:
            for row in self.data['requirements']:
                if cid in row['check_ids']:
                    row['applicable']=applies; row['na_reason']='Same scene edit.' if not applies else ''
            for check in self.data['checks']:
                if check['id']==cid:
                    check['applicable']=applies; check['na_reason']='Same scene edit.' if not applies else ''
            self.set_check(cid,'PASS' if applies else 'NOT_APPLICABLE')
        (self.root / 'outputs/baseline.png').write_bytes(b'Synthetic baseline')
        self.data['comparison']={'applicable':True,'baseline':{'image_path':'outputs/baseline.png',
             'sha256':sha(b'Synthetic baseline'),'actually_opened':True},'preservation_plan':'Keep defined volumes.',
             'dimensions':[{'dimension':d,'before':'Synthetic earlier appearance.','after':'Synthetic current appearance.',
              'change':'preserved','evidence':'Synthetic comparison.','requirement_ids':['R03-01']} for d in DIMENSIONS],
             'unresolved_regressions':[]}
        self.data['selection']['considered_candidates'].append({'image_path':'outputs/baseline.png',
            'sha256':sha(b'Synthetic baseline'),'actually_opened':True,'qa_status':'candidate_pass',
            'dimensions':{d:'Synthetic baseline '+d for d in DIMENSIONS}})

    def test_valid_review_and_selection_records(self):
        self.assert_valid()
        self.assert_valid('selection')

    def test_valid_preflight_without_claiming_output_qa(self):
        self.refs['delivery_status']='planned'
        for row in self.data['requirements']:
            if row['applicable']:
                row['observation']=self.obs('NOT_REVIEWED'); row['observation']['basis']='planned'
        for check in self.data['checks']:
            if check['applicable']:
                check.update(self.obs('NOT_REVIEWED')); check['basis']='planned'
        self.assert_valid('preflight')

    def test_exact_clause_missing_from_actual_prompt(self):
        self.data['requirements'][0]['prompt_clauses']=['Stale text copied from another run.']
        self.assert_error('clause missing')

    def test_section_title_is_not_a_visual_clause(self):
        self.data['requirements'][0]['prompt_clauses']=['ART / REFERENCE ROLES']
        self.assert_error('merely a section title')

    def test_saved_and_actual_prompt_must_be_identical(self):
        self.args['prompt'] += '\nUnrecorded edit.'
        self.assert_error('exact prompt differs')

    def test_preflight_cannot_preapprove_unseen_output(self):
        self.refs['delivery_status']='planned'
        self.assert_error('preflight cannot claim', 'preflight')

    def test_style_input_cannot_be_relabelled_geometry(self):
        self.write('refs/manifest.json', {'references':[{'id':'M01-01','sha256':sha(self.ref),'group':'master03','generation_input_allowed':True}]})
        self.assert_error('role exceeds approved catalog scope')

    def test_returned_model_cannot_be_invented(self):
        self.refs['submitted_prompt']['returned_model_info']='unverified-model'
        self.assert_error('actual returned metadata evidence required')

    def test_actual_returned_metadata_is_linked_to_saved_response(self):
        self.refs['submitted_prompt']['returned_model_info']='synthetic-model'
        self.refs['submitted_prompt']['returned_metadata_evidence']={'returned_model_info':{'response_path':'tool_response.json','json_pointer':'/model'}}
        self.write('outputs/current/tool_response.json',{'model':'synthetic-model'})
        self.assert_valid()

    def test_s04_cannot_copy_c04_failure_evidence(self):
        self.set_check('C04','FAIL'); self.set_check('S04','FAIL')
        self.assert_error('geometry FAIL evidence copied')

    def test_uncertain_comparison_cannot_pass_r03(self):
        self.make_edit(); self.data['comparison']['dimensions'][1]['change']='uncertain'
        self.assert_error('uncertain comparison cannot be PASS')

    def test_correction_baseline_cannot_be_omitted_from_selection(self):
        self.make_edit()
        self.data['selection']['considered_candidates'].pop()
        self.assert_error('baseline missing from considered candidates','selection')

    def test_current_candidate_cannot_be_its_own_baseline(self):
        self.make_edit()
        self.data['comparison']['baseline'].update(image_path='outputs/current/image.png',sha256=sha(self.image))
        self.assert_error('baseline cannot be the current candidate')

    def test_mandatory_projection_cannot_be_na_without_user_exception(self):
        for row in self.data['requirements']:
            if 'C04' in row['check_ids']:
                row.update(applicable=False,na_reason='Convenient omission.')
        for check in self.data['checks']:
            if check['id']=='C04':
                check.update(applicable=False,na_reason='Convenient omission.')
        self.set_check('C04','NOT_APPLICABLE')
        self.assert_error('mandatory-check N/A needs current user exception')
        for check in self.data['checks']:
            if check['id']=='C04':
                check['exception']={'source':'synthetic current user request','quote':'For this fixture allow a perspective camera.'}
        self.assert_valid()

    def test_honest_unreviewed_delivery_is_permitted(self):
        for row in self.data['requirements']:
            if row['applicable']:
                row['observation']=self.obs('NOT_REVIEWED'); row['observation']['basis']='not_reviewed'
        for check in self.data['checks']:
            if check['applicable']:
                check.update(self.obs('NOT_REVIEWED')); check['basis']='not_reviewed'
        self.data['candidate'].update(actually_opened=False,observation_basis='not_reviewed',reviewed_at=None,overall_status='not_reviewed')
        self.data['selection'].update(qa_status='not_reviewed',claims_overall_pass=False,
            unresolved_limitations='Image could not be opened; all visual requirements unreviewed.',stop_reason='Tool host ended inspection.')
        self.data['selection']['considered_candidates'][0].update(actually_opened=False,qa_status='not_reviewed',
            dimensions={d:'Not reviewed; no image observation for '+d for d in DIMENSIONS})
        self.assertEqual(self.assert_valid('selection')['image_qa_status'],'not_reviewed')

    def test_recent_conversation_input_without_local_path_is_supported(self):
        self.refs['delivery_mechanism']='num_last_images_to_include'
        for entry in self.refs['inspected_for_planning']+self.refs['submitted_to_generation']:
            entry.update(path=None,sha256=None,conversation_image_evidence='Synthetic current conversation image, only selected target; actually inspected inline.')
        self.args.pop('referenced_image_paths'); self.args['num_last_images_to_include']=1
        self.assert_valid()

    def test_explicit_catalog_image_edit_is_scoped_not_master_promotion(self):
        self.make_edit()
        self.write('refs/manifest.json', {'references':[{'id':'M01-01','sha256':sha(self.ref),
                   'group':'architecture_example','generation_input_allowed':False}]})
        for entry in self.refs['inspected_for_planning']+self.refs['submitted_to_generation']:
            entry.update(role='edit_target',authorization_kind='explicit_current_request',
                         authorization_source='synthetic current user request',authorization_quote='Edit this particular example.',
                         authorization_evidence='Produce a separate edited output; preserve source bytes.')
        self.assert_valid('selection')
        self.assertEqual((self.root/'refs/source.png').read_bytes(),self.ref)

    def test_recent_only_edit_baseline_has_honest_conversation_evidence(self):
        self.make_edit()
        self.refs['delivery_mechanism']='num_last_images_to_include'
        evidence='Synthetic current conversation edit target, inspected inline.'
        for entry in self.refs['inspected_for_planning']+self.refs['submitted_to_generation']:
            entry.update(path=None,sha256=None,role='edit_target',conversation_image_evidence=evidence,
                authorization_kind='explicit_current_request',authorization_source='synthetic user request',
                authorization_quote='Edit this attached image.',authorization_evidence='Separate requested edit; source retained.')
        self.args.pop('referenced_image_paths'); self.args['num_last_images_to_include']=1
        self.data['comparison']['baseline'].update(image_path=None,sha256=None,reference_id='M01-01',conversation_image_evidence=evidence)
        self.data['selection']['considered_candidates'][1].update(image_path=None,sha256=None,reference_id='M01-01',conversation_image_evidence=evidence)
        self.assert_valid('selection')
        self.data['comparison']['baseline']['conversation_image_evidence']='A different unrecorded image.'
        self.assert_error('baseline must link the inspected edit target')

    def test_actual_reference_count_mismatch(self):
        self.refs['actual_submitted_image_count']=5
        self.assert_error('actual image count mismatch')

    def test_reference_hash_mismatch(self):
        self.refs['inspected_for_planning'][0]['sha256']='0'*64
        self.assert_error('sha256 mismatch')

    def test_uninspected_input_cannot_be_submitted(self):
        self.refs['inspected_for_planning'][0]['inspected']=False
        self.assert_error('not actually inspected')

    def test_planned_observation_cannot_be_pass(self):
        self.data['requirements'][0]['observation']['basis']='planned'
        self.assert_error('actual_image basis')

    def test_unopened_image_cannot_pass(self):
        self.data['candidate']['actually_opened']=False
        self.assert_error('unseen/planned image')

    def test_positive_and_forbidden_surface_evidence_both_required(self):
        for check in self.data['checks']:
            if check['id']=='S03': check['positive_evidence']=''
        self.assert_error('S03: missing positive_evidence')

    def test_missing_check_cannot_pass(self):
        self.data['checks'].pop(0)
        self.assert_error('every required ID')

    def test_observed_art_failure_cannot_have_overall_pass(self):
        self.set_check('S03','FAIL')
        self.assert_error('overall status contradicts')

    def test_check_cannot_override_failed_requirement(self):
        self.data['requirements'][0]['observation']['status']='FAIL'
        self.assert_error('contradicts linked requirement')

    def test_uncertainty_cannot_be_hidden_by_noncritical_flag(self):
        self.data['requirements'][0]['critical']=False
        self.set_check('C01','UNCERTAIN')
        self.assert_error('overall status contradicts')

    def test_same_scene_requires_r03_not_r02(self):
        self.data['request_mode']='own_correction'
        self.assert_error('R03: required')

    def test_valid_same_scene_comparison(self):
        self.make_edit()
        self.assert_valid('selection')

    def test_remaining_regression_cannot_be_promoted(self):
        self.make_edit()
        self.data['comparison']['dimensions'][1]['change']='regressed'
        self.data['comparison']['unresolved_regressions']=['R03-01']
        self.assert_error('unresolved regression requires FAIL','selection')

    def test_regression_list_cannot_omit_observed_regression(self):
        self.make_edit()
        self.data['comparison']['dimensions'][1]['change']='regressed'
        self.assert_error('unresolved regression list mismatch')

    def test_honest_incomplete_delivery_is_valid_record_not_image_pass(self):
        self.set_check('S03','FAIL')
        self.data['candidate']['overall_status']='needs_revision'
        s=self.data['selection']; s.update(qa_status='needs_revision',claims_overall_pass=False,
            unresolved_limitations='S03 still lacks the intended surface expression.',stop_reason='Tool failed during authorized correction.')
        s['considered_candidates'][0]['qa_status']='needs_revision'
        report=self.assert_valid('selection')
        self.assertEqual(report['image_qa_status'],'needs_revision')

    def test_selection_needs_all_seven_candidate_dimensions(self):
        del self.data['selection']['considered_candidates'][0]['dimensions']['surface']
        self.assert_error('seven-dimension evidence','selection')

    def test_final_manifest_cannot_silently_change_status(self):
        self.save()
        self.write('outputs/final_manifest.json', {'images':[{'source':'outputs/current/image.png','qa_status':'needs_revision'}]})
        report=validate_run(self.root,'outputs/current','selection')
        self.assertTrue(any('final manifest: qa_status mismatch' in e for e in report['errors']),report)

    def test_comparison_only_reference_cannot_be_laundered_by_renaming(self):
        self.write('refs/manifest.json', {'references':[{'id':'F-08','sha256':sha(self.ref),'generation_input_allowed':False}]})
        self.assert_error('comparison/review-only source needs explicit')

    def test_unknown_reference_needs_authorization(self):
        self.write('refs/manifest.json',{'references':[]})
        self.assert_error('unregistered input lacks scoped authorization')

    def test_native_arguments_reject_invented_seed_model_parameters(self):
        self.args['seed']=123
        self.assert_error('unsupported native imagegen')

    def test_both_image_input_mechanisms_are_rejected(self):
        self.args['num_last_images_to_include']=1
        self.assert_error('two image mechanisms')

    def test_no_five_path_limit_inferred_from_recent_image_limit(self):
        self.refs['tool_contract']['parameter_specific_limits']={
          'num_last_images_to_include_max_count':{'status':'confirmed','value':5,'evidence':'Synthetic current recent-image contract.'}}
        for i in range(2,7):
            p=f'refs/source{i}.png'; raw=f'Synthetic image {i}'.encode(); (self.root/p).write_bytes(raw)
            entry={**self.refs['inspected_for_planning'][0], 'id':f'USER-{i}','path':p,'sha256':sha(raw),
                   'authorization_kind':'explicit_current_request','authorization_evidence':'Synthetic user specified this reference.',
                   'authorization_source':'current synthetic request','authorization_quote':'Use this test reference.'}
            self.refs['inspected_for_planning'].append(entry)
            self.refs['submitted_to_generation'].append({**entry,'input_index':i})
            self.args['referenced_image_paths'].append(str(self.root/p))
        self.refs['actual_submitted_image_count']=6
        self.assert_valid()

    def test_relative_traversal_is_rejected(self):
        self.data['prompt_path']='../outside.md'
        self.assert_error('without traversal')

    def test_symlink_escape_is_rejected(self):
        outside=self.root/'outside.png'; outside.write_bytes(self.image)
        (self.run/'escape.png').symlink_to(outside)
        self.data['candidate']['image_path']='escape.png'
        self.assert_error('path escapes its root')

    def test_arbitrary_absolute_argument_cannot_replace_recorded_input(self):
        self.args['referenced_image_paths']=['/tmp/unrecorded.png']
        self.assert_error('exact submitted image paths/order mismatch')

    def test_malformed_input_is_reported_not_a_traceback(self):
        self.data['requirements']='not an array'
        self.assert_error('requirements: array required')

    def test_historical_run_is_never_scanned_or_modified(self):
        old=self.root/'outputs/old'; old.mkdir(); (old/'result.json').write_text('{"status":"candidate_pass"}')
        before=(old/'result.json').read_bytes()
        self.assert_valid()
        self.assertEqual((old/'result.json').read_bytes(),before)
        self.assertFalse((old/'requirements.json').exists())


if __name__=='__main__':
    unittest.main()

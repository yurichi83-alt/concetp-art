"""One-time approved local registration; no image generation, network or Git writes."""
from pathlib import Path
import hashlib
import importlib.util
import json
import shutil

ROOT = Path(__file__).resolve().parents[2]
APPROVAL = 'master_update_20260912_v2_7_architecture_forms'
CATALOG = '2026-09-12-architecture-form-01'
SNAPSHOT = 'state/history/20260912_master_v2_7_architecture_forms'
RECORD = 'outputs/20260912_master_v2_7_update'
PROPOSAL = 'outputs/20260912_master_architecture_update_proposal/proposal_ko.md'

def read(rel):
    return json.loads((ROOT / rel).read_text())

def write(rel, data):
    (ROOT / rel).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

spec = importlib.util.spec_from_file_location('validation', ROOT / 'scripts/validate_project.py')
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)
manifest = read('refs/manifest.json')
project = read('project.json')
approvals = read('state/approvals.json')
assert project['master_version'] == '2.6', 'This one-time update has already run or baseline differs.'
assert not any(r['id'].startswith('F-') for r in manifest['references'])

roles = [
 ('stacked_wings', '다른 폭·높이의 날개와 외부 계단', '다른 폭/높이의 날개, 외부 계단, 돌출 창·발코니와 지붕 단차', ['unequal_wings', 'exterior_stairs', 'projecting_bays', 'roof_steps']),
 ('rounded_housings', '둥근 대형 하우징과 잘록한 중간부', '건물 규모의 둥근 하우징, 잘록한 중간부, 상하 비대칭', ['building_scale_rounded_housings', 'recessed_waist', 'asymmetric_volumes']),
 ('projecting_modules', '돌출 상층·후퇴 중간층과 기계 외장', '상층 돌출·중간층 후퇴·큰 기계 외장과 지지', ['projecting_upper_modules', 'recessed_middle', 'large_cladding_supports']),
 ('work_decks', '작업 데크·대형 설비와 구조 프레임', '넓은 작업 데크, 외부 대형 설비, 프레임/지지와 건축 결합', ['work_decks', 'external_plant_volumes', 'functional_structural_frames']),
 ('living_extensions', '덧붙인 생활 공간과 지붕 변화', '덧붙인 생활 공간, 층별 다른 재료, 외부 계단·차양·지붕 변화', ['living_extensions', 'layered_building_materials', 'stairs_awnings_roof_profiles']),
 ('service_channels', '깊은 서비스 홈과 큰 외장 띠', '깊은 서비스 홈, 큰 외장 띠와 패널 겹침, 건물 규모 설비 경로', ['deep_service_channels', 'large_cladding_bands', 'layered_panels']),
 ('street_rhythm', '거리의 건물 비례·돌출 리듬', '건물 폭/높이/돌출의 리듬과 거리 단위 연결 관계', ['varied_building_proportions', 'projection_rhythm', 'street_relationships']),
]
attachments = read('outputs/20260912_024611_architecture_direction_analysis/analysis_metadata.json')['attachments']
external_exclude = '원본 카메라·원근·배치 복제·초고층 높이·수상 베이스·미세 질감·실사 밀도·네온·상호/인물 제외. 큰 형태·외벽 깊이만 참고하며 최종 정사영·공통 베이스·LDI 표면 표현·Salvage Cyberpunk 해석을 유지'
new_refs = []
for n, (attachment, role) in enumerate(zip(attachments, roles), 1):
    stem, title, scope, aspects = role
    source = ROOT / attachment['copy']
    data = source.read_bytes()
    assert hashlib.sha256(data).hexdigest() == attachment['sha256']
    fmt, (w, h) = validation.image_dimensions(data)
    target = f'refs/architecture_form/form_{n:02d}_{stem}.png'
    (ROOT / target).parent.mkdir(parents=True, exist_ok=True)
    assert not (ROOT / target).exists()
    shutil.copy2(source, ROOT / target)
    new_refs.append(dict(
        id=f'F-{n:02d}', path=target, group='architecture_form', title=title,
        use_only=scope, exclude=external_exclude, positive_reference=True,
        reference_role='scoped_architecture_form', source_kind='user_supplied_architecture_form_reference',
        width=w, height=h, format=fmt, sha256=hashlib.sha256(data).hexdigest(),
        approved_aspects=aspects, approval_id=APPROVAL, registration_date='2026-09-12',
        default_generation_input=False, generation_input_allowed=True, geometry_approved=False,
        reference_catalog_revision=CATALOG, archived_source_path=attachment['copy'],
        original_source_path=attachment['source'], original_filename=Path(attachment['source']).name,
        provenance='사용자 첨부 외부 건축 이미지. 작가·작품·제작 방식·출처 미확인; Little Devil Inside 자료로 분류하지 않음.',
        prior_inspection_record='outputs/20260912_024611_architecture_direction_analysis/analysis_metadata.json',
        selection_scope='Optional architecture-form input when relevant; select only needed images, preserve 01/02 geometry and 03/04 roles and unchanged default priorities. Not a whole-image or camera reference.',
    ))

examples = [
 ('20260912_030800__slum_curved_architecture_01.png', '20260912_030800_slum_curved_architecture_01_rebuild', '곡면 슬럼 1', '둥근 지상 외장, 외부 계단/후퇴 주택, 반원 지붕과 옆 기계', ['rounded_ground_cladding', 'stairs_recessed_home', 'barrel_roof_adjacent_machine'], '실제 투영·통로 가림·정량 비율'),
 ('20260912_031500__slum_curved_architecture_02.png', '20260912_031500_slum_curved_architecture_02_exit_clearance', '곡면 슬럼 2', '돌출 상층·곡면 외피·기계 경계·톱니 지붕', ['projecting_upper_volume', 'curved_shell', 'machine_boundary', 'sawtooth_roof'], 'B의 낮은 시점처럼 보이는 수평 투영·가려진 경계'),
 ('20260912_033801__city_day_l_building_01.png', '20260912_033801_city_day_l_building_01_geometry_rebuild', '낮 시가지 1', '연결된 ㄱ자 건물·대형 하우징이 차지하는 기계층', ['connected_l_building', 'large_horizontal_mechanical_storey'], '상층/바닥 축 불일치·고정 배치'),
 ('20260912_033801__city_day_l_building_02.png', '20260912_033801_city_day_l_building_02_geometry_rebuild', '낮 시가지 2', '높이가 다른 ㄱ자 날개·수직형 기계층', ['unequal_height_l_wings', 'vertical_mechanical_storey'], '정사영 오차·빈 콘크리트 단면·고정 낮 팔레트'),
]
for n, (filename, run, title, scope, aspects, exclude) in enumerate(examples, 8):
    path = f'outputs/final/{filename}'
    data = (ROOT / path).read_bytes()
    source = f'outputs/{run}/image.png'
    review = f'outputs/{run}/review.md'
    assert (ROOT / source).read_bytes() == data
    assert (ROOT / review).is_file()
    result = read(f'outputs/{run}/result.json')
    assert 'needs_revision' in json.dumps(result), 'Inspect source QA before registration'
    fmt, (w, h) = validation.image_dimensions(data)
    new_refs.append(dict(
        id=f'F-{n:02d}', path=path, group='architecture_example', title=f'形態比較 — {title}'.replace('形態比較','형태 비교'),
        use_only=scope, exclude=exclude + '; 카메라·고정 배치·표면 스타일·장면 팔레트/소품/기계 비율·기하 오류는 승인 범위 밖',
        positive_reference=True, reference_role='scoped_architecture_example',
        source_kind='generated_result_scoped_form_approval', width=w, height=h, format=fmt,
        sha256=hashlib.sha256(data).hexdigest(), approved_aspects=aspects,
        approval_id=APPROVAL, registration_date='2026-09-12', default_generation_input=False,
        generation_input_allowed=False, reference_catalog_revision=CATALOG,
        source_output_path=source, review_path=review, result_path=f'outputs/{run}/result.json',
        overall_qa_status_at_registration='needs_revision', geometry_approved=False,
        selection_scope='Form comparison only. No automatic generation input, camera/layout reuse or whole-image approval. Later explicit user edit/reference requests are separately scoped; preserve existing QA.',
    ))

manifest['references'].extend(new_refs)
manifest.update(master_version='2.7', reference_catalog_revision=CATALOG,
                reference_catalog_approval_id=APPROVAL, architecture_form_approval_id=APPROVAL,
                architecture_form_reference_count=7, architecture_form_example_count=4)
manifest['scoped_positive_reference_semantics'] = 'Scoped positive references approve only their approved_aspects, never whole-image geometry. Separately count 27 masters, 4 surface supports, 7 architecture-form references and 4 architecture-form comparison examples. Respect generation_input_allowed and keep default priorities unchanged.'
m17 = next(r for r in manifest['references'] if r['id']=='M03-17')
m17['exclude'] = '원본 카메라·원근·초고층 적층·과밀 배치·해안 도시 세계관·물/배/인물/식생 자동 삽입 제외. 지상 곡면 건축은 v2.7의 공통 투영·접지·명료한 보행 경계에 맞게 해석하며 임의 사선 회전은 복사하지 않음. 지붕 비움·높이·동선·구조 불일치의 근거로 사용하지 않음'
m17['role_scope_update_approval_id'] = APPROVAL

project.update(package_version='1.7.0', master_version='2.7', execution_rules_version='1.8',
               updated_date='2026-09-12', master_update_approval_id=APPROVAL,
               reference_catalog_revision=CATALOG, reference_catalog_approval_id=APPROVAL,
               architectural_design_revision='2026-09-12-architecture-forms',
               optional_architecture_form_ids=[f'F-{n:02d}' for n in range(1,8)],
               approved_architecture_example_ids=[f'F-{n:02d}' for n in range(8,12)])
project['generation_reference_selection'] = project['generation_reference_selection'].replace('v2.6','v2.7').replace('building ground footprints are orthogonal and roof planes are validated separately.', 'main straight building structure follows common XY axes; grounded curved walls are allowed with clear visual boundaries; roof surfaces and curve tangents are inspected separately.') + ' F-01~07 are optional large-form/facade-depth references, not camera or rendering references; do not submit all seven by default. F-08~11 are form comparison examples only, not automatic generation inputs; preserve their needs_revision QA and do not promote their geometry.'
g = project['geometry_policy']
g['architecture_form_approval_id'] = APPROVAL
g['building_footprints'] = 'Main arrangement and straight structural segments follow common XY axes. Rounded ground corners, curved facades and rounded machine-like buildings are allowed with readable grounding and walking/blocking boundaries. No arbitrary oblique building rotation, ambiguous wedge gaps or implausible joints. Curve tangents are distinct from level axis lines; do not wrap every curved building in a rectangular plinth or impose curve counts/radii.'
g['workflow'][0] = 'Record mandatory single orthographic camera; shared-coordinate large forms, facade depth, straight/curved ground boundaries and separate roof/support plan'
g['workflow'][1] = 'Check common axes for straight structure, coherent curves, unchanged square base corners, grounding and visually continuous routes; plan visible evidence'
g['current_concept_collision_validation_required'] = False
g['numeric_clearance_requires_3d_validation'] = True
g['collision_scope'] = 'Actual collider/mesh/UV construction and validation belong to a separately requested later 3D task. Their absence does not fail or hold current concept art; inspect visible grounding, support, boundary clarity and walking continuity.'
project['architectural_design_policy']['form_approval_id'] = APPROVAL
project['architectural_design_policy']['design_order'] = ['large_masses_and_silhouettes','facade_depth_and_functional_spaces','surface_depiction']
project['architectural_design_policy']['form_options'] = 'Choose purpose-driven L/T/U wings, unequal widths/heights, setbacks/projections, deep openings, stairs, balconies, decks, supported curved housings and roof profiles. Use only suitable choices; no mandatory feature bundle or fixed number of variants.'
project['architectural_design_policy']['mechanical_storey'] = 'When requested or functionally appropriate, machinery may form a cladding shell, frame, plant annex or an entire nonhabitable storey. A mechanical second storey is that storey itself, not a residential second storey plus rooftop props. Ground-level human access remains building-specific.'
project['architectural_design_policy']['rooftop']['mechanical_storey_application'] = 'Keep per-building functional roof composition at 40–80%, distinct from requested facade/storey machinery proportions. Choose supported useful elements; do not add redundant machinery above a machinery storey merely to satisfy coverage, or repeat the same tanks/panels.'
project['functional_exit_policy']['form_approval_id'] = APPROVAL
project['functional_exit_policy']['forms'].append('passage_between_or_below_equipment')
project['functional_exit_policy']['accidental_obstruction'] = 'Do not retroactively label a fence/stock blocking a planned open route as an intended locked exit.'
project['boundary_object_policy']['form_approval_id'] = APPROVAL
project['boundary_object_policy']['requirements'] += '; use legible connected blocking masses, not tiny low props; buildings are optional boundary carriers. Maintain central combat space with scene-appropriate street widths, not the same oversized empty courtyard everywhere.'
project['geometry_review_policy']['form_approval_id'] = APPROVAL
project['geometry_review_policy']['parallel_projection'] += ' Also compare footings, floor edges, shutter horizontal lines, terrace beams and upper walls against matching ground-axis lines; internally coherent building lines can still contradict the scene camera.'
project['geometry_review_policy']['exclude_false_matches'] = 'Distinguish true horizontal straight structural edges from roof slopes, awnings, shadows, rotated props and curved-building tangent lines. Partial occlusion alone does not prove building rotation or wall tilt.'
project['geometry_review_policy']['collision_mesh_uv_validation_required'] = False
project['geometry_review_policy']['collision_mesh_uv_scope'] = g['collision_scope']
project['structural_correction_policy']['form_approval_id'] = APPROVAL
project['structural_correction_policy']['global_geometry_fault_strategy'] += ' Retain the intended large-form design (curves, projections, L wings and mechanical storeys) while rebuilding its common projection; do not flatten every design into boxes.'
project['scene_interpretation'] += ' Interpret city, alley, market by distinct building purposes, silhouettes/depth and street relationships. L shape, second-storey machinery, 40%/20%, half-size upper home, building counts, poles/cars, lighting/palette are current-request values only. Two outputs require independently designed visible forms and layout, not just mirrors or recoloring; no fixed variation count.'
project['architecture_form_policy'] = dict(
    approval_id=APPROVAL, reference='docs/10_CURRENT_REFERENCES.md',
    optional_inputs=project['optional_architecture_form_ids'],
    comparison_only_examples=project['approved_architecture_example_ids'],
    approved_scope='large building forms, facade depth, purposeful reuse and structural machinery; preserve 01/02 geometry and 03/04 art/world roles',
    existing_master_count=27, geometry_approval_from_examples=False,
    default_reference_priorities_changed=False, new_fixed_curve_counts_radii_or_scene_values=False,
)

approvals.update(master_version_approved='2.7', reference_catalog_revision=CATALOG,
                 reference_catalog_approval_id=APPROVAL,
                 note='Current master2.7 / execution1.8. Architecture-form update approved; 27 core masters, 4 surface supports, 7 optional form references and 4 form-comparison examples are separate. Ground building curves allowed; actual collision validation excluded from current image acceptance. Orthographic geometry, LDI expression, Salvage Cyberpunk and prior QA remain. Earlier entries and pre-update root metadata preserved in snapshot.')
approvals['entries'].append(dict(
    approval_id=APPROVAL,date='2026-09-12',status='approved',
    user_request='좋아 결과는 만족 스러워. 그럼 마스터 레퍼런스에 갱신할 내용을 정리해줘',
    user_confirmation='좋아 메인 레퍼런스에 갱신해줘', proposal_path=PROPOSAL,
    scope='Approved architecture diversity, grounded curved building boundaries, machinery as architecture, varied blocking objects/exits, and image-only geometry review scope; register seven form references and four scoped form-comparison examples.',
    approved_aspects=['large_form_and_facade_depth_diversity','ground_level_curved_building_walls','functional_structural_mechanical_storeys','nonbuilding_boundaries_and_varied_exits','visual_grounding_and_common_projection_without_actual_collider_validation'],
    not_approved_aspects=['whole_image_or_geometry_promotion','test_image_qa_override','fixed_scene_numbers_props_ratios_palette','reference_camera_microtexture_neon_or_world_copy','base_curvature','arbitrary_oblique_building_rotation'],
    reference_ids=[r['id'] for r in new_refs], master_image_count_before=27,master_image_count_after=27,
    architecture_form_reference_count=7,architecture_form_example_count=4,scoped_style_support_count=4,
    master_version='2.7',execution_rules_version='1.8',package_version_after='1.7.0',reference_catalog_revision=CATALOG,
    historical_qa_preserved=True,existing_original_reference_bytes_preserved=True,
    snapshot_path=SNAPSHOT,update_record_path=RECORD,
))
write('refs/manifest.json',manifest)
write('project.json',project)
write('state/approvals.json',approvals)
write(RECORD+'/registered_references.json',{'approval_id':APPROVAL,'references':new_refs,'source_inspection':'Prior analysis and generation review records; registration verifies bytes, dimensions and scoped roles, does not regrade images.'})
print('Registered 7 optional form references and 4 comparison-only examples; core27/defaults/previous approvals preserved.')

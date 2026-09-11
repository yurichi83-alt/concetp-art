from pathlib import Path
from datetime import datetime
import hashlib
import json

RUN = Path(__file__).resolve().parent
ROOT = RUN.parents[1]
run_id = RUN.name
prompt = (RUN / 'generation_prompt.md').read_text(encoding='utf-8')
roles = [
    ('scene_guide', (RUN/'structure_guide.png').relative_to(ROOT).as_posix(), 'orthographic common axes, square base, building masses and two reserved exits; no final palette/materials'),
    ('M01-01','refs/master01/composition_cutaway.png','full standalone base and two cutaway faces; exclude perspective, neon, buildings/signs/props'),
    ('M02-01','refs/master02/layout_two_exits.png','two adjacent blocking directions and two connected exits; exclude labels/colors/icons and fixed gate positions'),
    ('M03-10','refs/master03/ldi_10_storefront_style_anchor.png','simplified architecture/materials and clean broad color planes; exclude camera/world/people/storefront identity'),
    ('M04-02','refs/master04/world_02_heavy_mechanical_arms.png','recovered technology/repair/functional joins translated into buildings; exclude human/armor/camera/photoreal density'),
    ('user_retro_machine',(RUN/'user_retro_machine_reference.png').relative_to(ROOT).as_posix(),'retro casing/instrument/control shapes only; exclude dense rust/lettering/branding/UI/photoreal finish'),
    ('B03-01','refs/style_support/brush_planes_reference.jpg','broad clean color planes plus sparse large flat neighboring-tone strokes; exclude fantasy architecture/harbor/people/day/palette/camera'),
]
inputs = []
for i,(rid,path,role) in enumerate(roles,1):
    data = (ROOT/path).read_bytes()
    inputs.append(dict(id=rid, input_index=i, path=path, absolute_path=str((ROOT/path).resolve()),
                       role=role, sha256=hashlib.sha256(data).hexdigest(), inspected=True, delivery_status='prepared_not_submitted'))
refs = json.loads((ROOT/'templates/references.json').read_text(encoding='utf-8'))
refs.update(run_id=run_id, request_group_id=run_id, scene_id='retro_alley', inspected_for_planning=inputs,
            submitted_to_generation=[], delivery_status='prepared_not_submitted', delivery_mechanism='referenced_image_paths',
            planned_inputs=inputs, actual_submitted_image_count=None, prior_generated_images_used=False)
refs['reference_role_mapping'].update(geometry_projection_inputs=['scene_guide','M01-01','M02-01'], art_expression_inputs=['M03-10'],
    world_design_inputs=['M04-02','user_retro_machine'], surface_style_support_inputs=['B03-01'],
    role_balance_and_selection_reason='Current machine attachment guides design while M03-10/B03-01 guide finish. Original 01/02/04 roles retained. No previous generated examples are inputs.')
refs['tool_contract'].update(checked_at=datetime.now().isoformat(), tool_name='image_gen.imagegen', selected_image_parameter='referenced_image_paths',
    contract_source='Current callable tool schema/developer instructions', confirmed_contract_facts_with_evidence=['prompt and referenced_image_paths are available; num_last_images_to_include cannot be combined with paths', 'num_last_images_to_include has max5; referenced_image_paths maximum is not exposed'])
refs['tool_contract']['parameter_specific_limits']['num_last_images_to_include_max_count']={'status':'confirmed_current_contract','value':5,'evidence':'tool description limits recent conversation selection to5'}
refs['submitted_prompt'].update(path='generation_prompt.md',saved_text_matches_actual_argument='prepared_not_submitted',
    character_count=len(prompt),character_count_method='Python len of exact UTF-8-decoded saved text',
    utf8_byte_count=len(prompt.encode('utf-8')),utf8_byte_count_method='len(text.encode(utf-8))',
    whitespace_word_count=len(prompt.split()),word_count_method='Python whitespace split; not token count')
refs['structure_guide'].update(path=roles[0][1],coordinate_camera_source_path=(RUN/'structure_plan.json').relative_to(ROOT).as_posix(),
    projection_mode='orthographic_parallel',selected_camera='See structure_plan.json; single mathematical orthographic projector',
    inspected=True,submitted=False,building_orthogonal_footprints_checked=True,roof_planes_and_supports_checked=True,
    upper_lower_correspondence_checked=True,polygon_roof_checks_separate_from_AABB=True,
    functional_exit_roles_locations_states_recorded=True)
(RUN/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
protected = ['project.json','refs/manifest.json','state/approvals.json','docs/03_VISUAL_STYLE_V2.md']
(RUN/'protected_before.json').write_text(json.dumps({p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in protected},indent=2)+'\n',encoding='utf-8')
(RUN/'brief.md').write_text('''# 생성 브리프

사용자: 골목 / 밤 / 쓰레기통, 고철, 판자, 건물 중 하나의 기계비율40% / 한 장. 기계는 현재 첨부 레트로 퓨처리즘 이미지 참고.
신규 독립 장면1장. 마스터2.6 / 실행1.7 / Master03본문2.2. 기존 출력은 입력하지 않는다. 마스터 변경 요청은 아니다.

## 요구사항 대응

| 요구 | 프롬프트 구역/계획 | 검수 |
|---|---|---|
| 완전 정사영·정사각베이스·두전면단면·전체프레이밍 | STRUCTURE / structure_plan의 단일투영·일정깊이 | C01~C04 |
| 두후방차단 방향·두기능출구·보행부피·직교건물 | guide의 두개방골목; 중앙→11시, 중앙→두건물사이1시 | L01~L07 |
| 골목·밤 | CURRENT SCENE; 낮은 창고와2층서비스주택, 어두운청보라주변광·국소램프 | K01/S01~S04 |
| 쓰레기통·고철·판자 | 벽가서로다른작업/보관포켓, 통로밖 | K01/L03 |
| 한건물기계40% | A하부 서비스설비영역+부착구조; 외관상 약40%, 정밀면적검증아님 | W03/K02 |
| 첨부레트로기계 | 입력6 둥근케이스·아날로그계기·주황창·물리버튼; 크기/실루엣변화 | W01/K03 |
| 녹색CRT제외 | CURRENT SCENE 명시 | K03 |
| 각건물 사람입구·지붕40~80% | 문/셔터, 지지된roof설비계획각약49%; 기계40%와별개 | W04/W05 |
| 넓은깨끗한색면·큰성긴방향성평면붓터치 | ART, 온전한면에도적용; 표면색변화와손상분리 | S01~S04 |
| 물결유리·모자이크·부조·과밀잡티방지 | ART; 메마른도로·큰색패치 | S01~S04 |
| 회수·수리기술·선택적노후 | ART/WORLD; 기능적수리결합과반복기계복제방지 | W01~W03 |

이번엔 팔레트/분위기를 장면에 맞춰 선택했다. 이전 편집의 물웅덩이·손상절반·건물수3개·전봇대는 자동상속하지 않는다.
실내는 노출하지 않아 내부동선L06은 N/A 예정. 최종이미지에서 노출되면 새로 검수한다. 보행폭·높이와기계/옥상비율은 설계값과2D관찰추정을 구분한다.
''',encoding='utf-8')
(RUN/'preflight.md').write_text('''# 생성 전 확인

- 사용자 요청은 새 한 장이며 내장 image_gen으로 처리. API 키·별도설치 없음.
- 현재 사용자 기계 자료, 원본01/02/03/04 및 B03-01을 실제 확인. 각 역할/제외를 전달 프롬프트에 명시.
- 생성용 독립 구조 가이드에 공통정사영·직교발판·동선·문·지붕/설비 지지/점유를 계획. 가이드는 강제 기하제어가 아니며 최종 PASS 근거도 아님.
- 브리프 대응표의 구조/장면/아트 요구를 세 구역 실제프롬프트에 기록. 이전 생성이미지 입력 없음.
- 전체 보행보호공간과 설비/소품은 계획에서 분리. PNG 가이드 실제 확인 후 호출.
- 계획 입력7장은 실제 사용 계획일 뿐 도구상한이 아님. 아직 호출 전이므로 전달상태 prepared_not_submitted.
- 생성후 원본을보존하고 최종이미지의 실측선군/단면대응/기단/두출구/재질을 다시 검수한다.
''',encoding='utf-8')
print(json.dumps({'run':run_id,'input_count':len(inputs),'prompt_characters':len(prompt)},ensure_ascii=True))

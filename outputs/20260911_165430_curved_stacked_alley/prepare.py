from pathlib import Path
import hashlib
import json
from datetime import datetime

RUN=Path(__file__).resolve().parent
ROOT=RUN.parents[1]
def dump(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
protected=[ROOT/'AGENTS.md',ROOT/'project.json',ROOT/'refs/manifest.json',ROOT/'state/approvals.json',ROOT/'state/CHANGELOG.md',*sorted((ROOT/'docs').glob('*.md')),ROOT/'.agents/skills/game-env-art/SKILL.md']
dump(RUN/'master_hashes_before.json',{p.relative_to(ROOT).as_posix():digest(p) for p in protected})
specs=[
 ('scene_guide',RUN/'structure_guide.png','new mathematical orthographic massing and square base/two exits; contains allowed curved buildings and varied stack, no collision debug overlay'),
 ('user_future_home',RUN/'future_home_reference.jpg','architectural massing: curved habitable modules/projections/recessed connecting bands; exclude original camera/height/world/scene/people/text/detail density'),
 ('user_stacked_house',RUN/'stacked_house_reference.png','architectural massing: mixed-size/material rooms, external stairs, terraces and multiple roof levels; exclude original camera/height/world/text/detail density'),
 ('B03-01',ROOT/'refs/style_support/brush_planes_reference.jpg','only broad calm painted planes and sparse flat directional nearby-tone strokes; exclude source architecture/camera/palette/harbor/day/people'),
 ('user_retro_machine',RUN/'retro_machine_reference.png','retro machine casing/instrument/control design; exclude portrait composition/text/logos/UI/dense rust'),
]
inputs=[]
for i,(rid,p,role) in enumerate(specs,1):
 assert p.is_file(),p
 inputs.append(dict(id=rid,input_index=i,path=p.relative_to(ROOT).as_posix(),absolute_path=str(p.resolve()),role=role,sha256=digest(p),inspected=True,delivery_status='prepared_not_submitted'))
prompt=(RUN/'generation_prompt.md').read_text(encoding='utf-8')
tpl=json.loads((ROOT/'templates/references.json').read_text(encoding='utf-8'))
tpl.update(run_id=RUN.name,request_group_id=RUN.name,scene_id='curved_stacked_alley',
 inspected_for_planning=inputs,planned_inputs=inputs,submitted_to_generation=[],delivery_status='prepared_not_submitted',delivery_mechanism='referenced_image_paths',
 prior_generated_scene_inputs=False,master_files_modified=False,
 scene_only_exception={'user_instruction':'상층 방 자체의 둥근 외장도 허용 지상 건물도 곡선 묘사도 허용. 직각 컬리전으로 막을 수 있으면 됨. 아직 마스터에는 반영하지 않음.',
 'allowed':['curved ground-floor architectural facades','rounded upper habitable rooms','different floor widths/depths and projections/setbacks'],
 'collision_intent':'common X/Y axis-aligned boxes or orthogonal unions, no obligatory20/70degree collision boundaries; conceptual plan only, no engine implementation',
 'unchanged':['flat square constant-depth base','one orthographic camera','exactly two clear functional rear exits','supported volumes','Master03 approved surface finish','Salvage Cyberpunk'],
 'qa_override':'L07 visual ground-footprint orthogonality restriction superseded for this request. Assess simple orthogonal collision-envelope plan and free traversal; intended curved building shapes are not FAIL. C02/C03 square base and C04 coherent projection still apply.'})
tpl['reference_role_mapping'].update(geometry_projection_inputs=['scene_guide'],art_expression_inputs=['user_future_home','user_stacked_house'],world_design_inputs=['user_retro_machine'],surface_style_support_inputs=['B03-01'],
 role_balance_and_selection_reason='User current massing clarification is tested via two complementary architecture references and a newly varied guide. B03-01 preserves approved brush finish, and current retro machinery continues. Under runtime5-image cap, M01/M02/M03/M04 original pictures omitted; their applicable approved rules remain explicit in guide/prompt.')
tpl['omitted_references_and_reasons']=[{'ids':['M01-01','M02-01','M03-10','M04-02'],'reason':'Runtime max5 paths confirmed by previous same-tool error. Geometry implemented in new scene guide; Master03/04 rules retained in text. No hidden submission claims.'},{'ids':['other4of6userarchitectureimages'],'reason':'Two complementary examples selected for curved modules and stepped mixed-material additions; other analyzed pictures remain available but are not submitted.'}]
tpl['tool_contract'].update(checked_at=datetime.now().isoformat(),tool_name='image_gen.imagegen',contract_source='Current tool schema plus actual prior runtime validation in this thread',selected_image_parameter='referenced_image_paths')
tpl['tool_contract']['parameter_specific_limits']['referenced_image_paths_max_count']={'status':'observed_same_tool_runtime','value':5,'evidence':'Previous request rejected7 paths with referenced_image_paths must contain at most5 paths; outputs/20260911_162630_retro_machine_alley/tool_limit_resolution.md'}
tpl['submitted_prompt'].update(path='generation_prompt.md',saved_text_matches_actual_argument='prepared_not_submitted',character_count=len(prompt),character_count_method='Python len decoded UTF-8',utf8_byte_count=len(prompt.encode('utf-8')),utf8_byte_count_method='len UTF-8 encoded bytes',whitespace_word_count=len(prompt.split()),word_count_method='whitespace split, not tokens')
tpl['structure_guide'].update(path=inputs[0]['path'],coordinate_camera_source_path=(RUN/'structure_plan.json').relative_to(ROOT).as_posix(),projection_mode='orthographic_parallel',selected_camera='See scene structure_plan.json',inspected=True,submitted=False,building_orthogonal_footprints_checked=False,roof_planes_and_supports_checked=True,upper_lower_correspondence_checked=True,functional_exit_roles_locations_states_recorded=True,
 override_note='Visual building facades may curve per current explicit user exception. Check axis-aligned collision envelopes instead; no completed engine collision claim.')
dump(RUN/'references.json',tpl)
(RUN/'brief.md').write_text('''# 이번 테스트 브리프

골목 / 밤 / 쓰레기통, 고철, 판자 / 한건물 기계비율40% / 최종1장. 새 형태로 생성하며 이전 생성물을 입력하지 않는다.
사용자 이번만예외: 상층방 둥근외장과지상건물곡선 모두허용. 실제컬리전은직각박스/직교결합으로단순화가능한형태가목표.20도/70도기울어진컬리전요구하지않음. 마스터영구수정금지.

## 대응표

| 요구 | 설계/지시 | 최종확인 |
|---|---|---|
| 실루엣·쌓임 | A둥근지상+캡슐상층+좁은연결부/빈테라스, B폭깊이다른증축+계단+단차지붕 | 작은장식없이도본체실루엣다양 |
| 곡선지상/상층 허용 | CURRENT EXCEPTION이구문서지상직교묘사제약보다우선 | 곡선건물자체를L07FAIL로취급금지 |
| 직각컬리전 | structure_plan의별도visualvolume/collision_envelope/clear_route | 직교결합기획타당성,실제엔진검증아님 |
| 단일정사영·정사각베이스·두단면 | guide카메라/일정깊이대응, 구조지시 | C01~C04실제선군/상하점대조 |
| 출구2개/중앙부터동선 |11시/1시벽틈개방, 보호부피내장식금지 | L01~L06 |
| 기계40% | A옆실/세로서비스/연결부/구조통합,하층띠만으로고정금지 | 외관상목표,정밀비율미검증 |
| 쓰레기통/고철/판자/밤 | 벽가보관포켓,청보라주변광·국소온색 | R01 |
| 레트로기계/녹색CRT제외 | 사용자이전기계참조와조작부/케이스다양성 | W01~W03 |
| 건물입구/옥상40~80% | 사람문/셔터와지지된기능설비/여백,기계40%와분리 | W04/W05 |
| 합격붓터치 | 넓은색면,온전한면에도큰성긴방향성평면터치 | S01~S04,유리물결/모자이크/부조금지 |

첨부건축의높이/원근/초과밀텍스처는복사하지않는다. 형상과표면참조역할을분리한다. 현재높이기준안에서적층원리를옮긴다.
새실루엣도식을먼저만든뒤정사영으로검증하며,이전상자2개외형을보존하라는지시는사용하지않는다.
''',encoding='utf-8')
(RUN/'preflight.md').write_text('''# 생성 전 확인

- 현재사용자예외를장면기록에만저장. 마스터/승인/스킬은수정하지않음.
- 새가이드의곡면실·돌출/후퇴·테라스·계단·다른지붕높이를실제확인후입력.
- 시각건물곡면과직각충돌기획을구분. 지면베이스곡률은계속금지.
- 입력5장계획, 이전출력입력없음. 원본마스터사진생략과텍스트역할유지이유기록.
- 단일정사영·베이스상하일정깊이·두후방출구와중앙접근부피·각입구/옥상기획을보존.
- 계획검증은최종PASS가아님. 실제PNG검수,기하FAIL/불확실을보고하고관찰된오류는기존승인범위로보정.
''',encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'prompt_characters':len(prompt),'master_update':False},ensure_ascii=True))

from pathlib import Path
import json, hashlib, importlib.util
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
HIST=ROOT/'state/history/20260910_113645_architecture_rules'
AID='architecture_entrances_roofs_20260910'
def digest(b): return hashlib.sha256(b).hexdigest()
files=['AGENTS.md','docs/00_INDEX.md','docs/02_LAYOUT.md','docs/04_WORLD_DESIGN_V2.md','docs/05_GENERATION_RULES.md','docs/06_QA.md','docs/10_CURRENT_REFERENCES.md','templates/brief.md','templates/preflight.md','templates/review.md','project.json','state/approvals.json','state/CHANGELOG.md']
assert not HIST.exists(),'Do not overwrite previous snapshot'
HIST.mkdir(parents=True)
original={f:(ROOT/f).read_bytes() for f in files}
for f,b in original.items():
 p=HIST/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def read(f): return original[f].decode('utf-8').replace('\r\n','\n')
def write(f,s):
 newline='\r\n' if b'\r\n' in original[f] else '\n'
 (ROOT/f).write_bytes(s.replace('\r\n','\n').replace('\n',newline).encode('utf-8'))
def append(f,s):write(f,read(f).rstrip()+'\n\n'+s.strip()+'\n')
entrance='각 건물에는 사람이 출입할 수 있다고 납득되는 문·셔터·출입구 중 최소 하나를 외관에서 식별 가능하게 설계한다. 실제 게임플레이 진입, 열린 문, 내부 구현을 의무화하지 않으며 닫힌 문이나 내려진 셔터도 가능하다. 사람 크기의 비례, 문틀·문턱·손잡이/셔터 구조 및 바닥과의 연결로 출입 용도가 읽혀야 한다. 작은 점검 패널, 환기구, 창문을 출입구 대신 세지 않는다.'
roof='건물 윗면이 넓고 밋밋하게 남지 않도록 각 건물의 옥상/지붕 윗면 40~80%를 설득력 있는 설비·기계·소품 또는 기능적 건축 요소로 구성한다. 건물마다 용도에 맞는 전력·환기·물 저장·통신·보관·차양 등에서 선택하고, 받침/고정·공급 연결·필요한 유지 접근이 납득되게 배치한다. 모든 지붕에 같은 장비를 반복하거나 면적을 채우려고 미세 부품을 흩뿌리지 않는다.'
coverage='40~80%는 전체 장면 평균이나 전체 기계 비율이 아니라 건물별 윗면 구성 범위다. 계획에서는 지붕 위 요소의 중복되지 않는 평면 점유 영역을 기준으로 잡고, 단순 그림자·오염·도색·기존 평판 지붕 자체는 채움으로 세지 않는다. 최종 이미지에서는 기능적 덩어리와 남은 여백을 보고 범위 적합을 추정하되 정확한 픽셀/3D 면적을 검증했다고 주장하지 않는다. 가려진 부분은 불확실로 기록한다. 40~80%를 건물 전체의 기계화율로 해석하지 않는다.'
compat='출입구 디자인은 기존의 외부 이동 출구 두 개와 구분한다. 건물 문/셔터는 실내로 이어지는 표현이며 제3의 외부 통로를 만들지 않는다. 옥상 요소는 공통 투영·납득되는 지지·기존 높이/전체 프레이밍과 두 출구/중앙 시야를 유지해야 한다. 넓은 색면과 선택적 디테일이라는 마스터03 표현도 유지한다.'
append('docs/04_WORLD_DESIGN_V2.md',f'## 건축 외관 보완 — 2026-09-10\n\n사용자 직접 추가 지시: {AID}. 마스터 세트 v2.2에 보완 기록.\n\n### 건물별 출입구 표현\n{entrance}\n\n### 건물별 윗면 40~80% 구성\n{roof}\n\n{coverage}\n\n{compat}\n\n기존의 전체 기계 비중 비정량 원칙은 유지하되, 이번에 명시된 건물별 윗면 구성 40~80%는 별도 요구로 적용한다. 기계만으로 채울 의무는 없다.')
# Bring the now-amended Master04 document's own title to current suite version.
s=(ROOT/'docs/04_WORLD_DESIGN_V2.md').read_text(encoding='utf-8').replace('# Master 04 v2.1 —','# Master 04 v2.2 —',1)
write('docs/04_WORLD_DESIGN_V2.md',s)
append('docs/02_LAYOUT.md','## 건물 문/셔터와 외부 출구의 구분 — 2026-09-10\n\n'+entrance+'\n\n외관 설득력을 위한 요구이며 모든 건물의 게임플레이 진입이나 내부 모델링을 요구하지 않는다. 닫힌 문/셔터는 허용한다. 기존의 두 외부 이동 출구 수를 늘리지 않는다. 실내가 실제 보이는 경우 H07의 방 깊이/동선 규칙은 계속 적용한다. 건물별 윗면 40~80% 설계는 마스터04를 따른다.')
append('AGENTS.md','## 건축 외관 추가 기준 — 2026-09-10\n- 각 건물에 사람용 문/셔터 등 출입구 표현 필수. 닫혀 있어도 가능하며 실제 게임플레이 진입 의무 아님. 점검판/환기구는 대체 불가. 두 외부 출구와 구분.\n- 각 건물 윗면 40~80%에 용도·지지·연결이 납득되는 기계/소품/기능적 건축 요소 배치. 전체 장면 평균/기계화율이 아님. 넓은 색면·구도·높이·통로 보존. 상세04, 검수W04/W05.\n')
append('docs/00_INDEX.md','## 건축 외관 추가 — 2026-09-10\n\n마스터 세트 v2.2 / 실행 v1.3 안에서 '+AID+' 보완을 적용한다. 마스터04 본문에 건물별 출입구 표현과 윗면40~80% 구성을 추가하고 02·05·06·템플릿에 연결했다. 기존 기하 기준과 원본24장은 유지한다. 03 본문은 v2.1 표현을 유지하고 04는 이번 보완으로 v2.2 표기를 적용한다.')
s=(ROOT/'docs/00_INDEX.md').read_text(encoding='utf-8').replace('03·04 아트/세계관 본문은 v2.1에서 유지하고,','03의 아트 본문은 v2.1에서 유지하고 04의 건축 외관은 아래 2026-09-10 추가를 적용하며,')
write('docs/00_INDEX.md',s)
append('docs/05_GENERATION_RULES.md','## 건축 외관 계획·검수 보완 — 2026-09-10\n\n생성 전 건물별 문/셔터 위치와 출입 크기·접지 근거를 기록한다. 닫힌 출입구도 외관 요구를 충족하며 실제 게임 진입 의무는 없다. 외부 두 출구 수와 구분한다.\n건물별 옥상/지붕 윗면40~80% 구성 영역과 설비 용도·지지/연결을 구조안/브리프에 포함한다. 상세04의 범위 해석과 03의 넓은 색면을 적용한다.\n결과에서 W04(건물별 출입구 표현), W05(건물별 윗면 구성)를 별도 검수한다. 명백한 누락은 전체 needs_revision, 핵심 관찰 불가는 uncertain으로 기록한다. 2D에서 정확한 면적을 검증했다고 하지 않는다.\n이번 외관 기준 추가는 기존 C01~C04/L01~L06의 구조 자동 보정 범위를 임의로 확대하지 않는다. 새 외관 규칙을 위반한 결과를 합격으로 취급하지 않되, 분석/검토/마스터 갱신 요청에서 자동 이미지를 생성하지 않는다.')
append('docs/06_QA.md','## 건축 외관 검사 — 2026-09-10\n\n| ID | 확인 항목 | 실패 예시 |\n|---|---|---|\n| W04 | 각 건물에 사람용 문/셔터 등 식별 가능한 출입구 표현. 닫힘 가능, 비게임플레이 목적 | 창·환기구·점검판만 있고 사람이 출입할 만한 요소가 없음 |\n| W05 | 각 건물 윗면40~80%의 기능적 구성, 용도·지지·연결·여백 | 넓게 빈 평판 지붕, 장비 몇 개를 구석에 둔 것으로 충족 처리, 무의미한 미세 소품 도배 |\n\n건물별로 근거를 기록하며 전체 평균으로 처리하지 않는다. W05 면적은 마스터04의 평면 점유 기준으로 계획하고 최종2D는 관찰 추정/불확실을 구분한다. 전체 기계화율이 아니며 그림자/때/평판 표면은 채움에 포함하지 않는다.\nW04/W05는 외관 디자인 검사다. 닫힌 문은 허용되며 실제 입장 기능은 검증 대상이 아니다. 외부 두 출구를 늘리지 않는다. 명백한 FAIL은 전체 needs_revision, 핵심 불확실은 uncertain. 기존 결과의 과거 검수는 새 규칙으로 소급 덮어쓰지 말고 새 검토 기록을 남긴다. 기존 구조 자동 보정 권한을 확대하지 않는다.')
append('docs/10_CURRENT_REFERENCES.md','## 최신 건축 외관 추가 — 2026-09-10\n\n사용자가 메인 레퍼런스 추가 내용으로 직접 지정한 '+AID+'를 마스터v2.2에 반영했다.\n\n1. '+entrance+'\n2. '+roof+'\n\n'+coverage+'\n\n'+compat+'\n\n이번 추가 범위는 출입구 표현과 윗면 구성이다. 카세트 퓨처리즘은 현재 이미지에서 부분 적용/약한 가독성으로 검토했으며, 이 확인 요청을 별도의 영구 스타일 승격 승인으로 처리하지 않았다. 기존 대화의 카세트 퓨처리즘/CRT 제외 지시는 다음 장면에도 유효하다.\n이전 파일: state/history/20260910_113645_architecture_rules/. 검토와 갱신 기록: '+str(RUN.relative_to(ROOT))+'/')
append('templates/brief.md','## Building exterior design (2026-09-10)\n- each_building_human_entry_door_or_shutter_visible_closed_allowed:\n- entry_scale_grounding_and_separation_from_two_external_exits:\n- each_roof_40_to_80_percent_footprint_plan:\n- rooftop_items_function_support_connections_and_remaining_space:\n- final_roof_coverage_visual_estimate_or_uncertain_not_metric_certification:')
append('templates/preflight.md','## Building exterior preflight\n\n| Item | Status | Evidence |\n|---|---|---|\n| Each building has a human-scale door/shutter design; actual gameplay entry not required | UNKNOWN | |\n| Each roof 40~80% functional composition plan with support/connections and remaining space | UNKNOWN | |\n| Rooftop volumes preserve framing, projection, height and route visibility | UNKNOWN | |')
s=read('templates/review.md').replace('| W03 | NOT_REVIEWED | |','| W03 | NOT_REVIEWED | |\n| W04 | NOT_REVIEWED | Per-building human entry design, closed door/shutter allowed, not gameplay requirement. |\n| W05 | NOT_REVIEWED | Per-roof 40~80% functional composition, visible basis/uncertainty, not exact 2D area certification. |')
write('templates/review.md',s+'\nW04/W05 are exterior-design checks; do not silently expand the standing structural auto-correction scope. Any clear exterior FAIL remains needs_revision; critical uncertainty remains uncertain.\n')
project=json.loads(read('project.json'))
oldchecks=project['structural_correction_policy']['checks'][:]
project['architectural_design_policy']={'approval_id':AID,'building_entry':{'required_per_building':True,'closed_door_or_shutter_allowed':True,'actual_gameplay_entry_required':False,'human_scale_and_grounding_required':True,'inspection_panel_or_vent_is_not_entry':True,'distinct_from_two_external_exits':True},'rooftop':{'coverage_min':0.4,'coverage_max':0.8,'scope':'each_building_roof_not_scene_average_or_mechanical_ratio','planned_measure':'union_of_functional_element_footprints_on_roof_plane','allowed':'purposeful equipment, props or functional architectural elements with credible support and connections','exclude_from_coverage':['shadows','grime','paint','plain_roof_surface'],'final_image_measure':'visual_estimate_or_uncertain_not_exact_metric_validation'},'qa_ids':['W04','W05'],'structural_auto_correction_scope_changed':False}
project['architectural_design_revision']='2026-09-10-entrances-roofs'
write('project.json',json.dumps(project,ensure_ascii=False,indent=2)+'\n')
approvals=json.loads(read('state/approvals.json')); previous_entries=approvals['entries'][:]
approvals['entries'].append({'id':AID,'date':'2026-09-10','type':'direct_user_master_addition','status':'active','evidence':'추가로 메인 레퍼런스에 추가할 내용도 알려줄게. 건물 같은경우 들어갈 수 있는 입구가 있어야해. 실제 게임플레이에서 들어갈 수 있는 구조는 아니고 외관상 설득력 있는 디자인을 위해서 건물에는 문이던 아니면 셔터던 어떤 형태로든 들어 갈 수 있는 디자인적인 요소가 있어야해. 그리고 건물의 옥상이 밋밋한 형태는 피해줘. salvage cyberpunk 의 기계적 요소던 아니면 다른 디자인 요소로 풀어내든 건물의 윗면은 40%~80% 는 설득력 있는 소품이나 기계등을 배치해야해.','scope':'건물별 외관상 출입구와 건물별 옥상/지붕40~80% 기능적 구성; master2.2 additive revision','not_authorized_by_this_entry':['new_image_generation','generated_image_master_promotion','cassette_futurism_permanent_style_promotion','expanded_structural_auto_correction_scope','git_commit_push'],'history_path':str(HIST.relative_to(ROOT)),'update_record_path':str(RUN.relative_to(ROOT))})
write('state/approvals.json',json.dumps(approvals,ensure_ascii=False,indent=2)+'\n')
append('state/CHANGELOG.md','## 2026-09-10 — 건물 출입구·윗면 구성 추가\n\n- 사용자 직접 메인 추가 지시 '+AID+'. 마스터세트2.2/실행1.3 유지, 건축보완 기록.\n- 각 건물의 식별 가능한 사람용 문/셔터(닫힘 허용, 게임 진입 의무 없음), 건물별 윗면40~80% 기능적 구성 반영.\n- 마스터04 및 02/05/06, 템플릿, 프로젝트·승인 기록 동기화. W04/W05 외관 검수 추가, 기존 구조 자동보정 범위 유지.\n- 카세트 퓨처리즘 현 이미지 적용은 약함/부분적이라는 별도 검토. 이미지 생성·승격·영구 카세트 스타일 변경 없음.\n- 이전13파일 '+str(HIST.relative_to(ROOT))+'에 보존.')
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
for ref in manifest['references']: assert digest((ROOT/ref['path']).read_bytes())==ref['sha256']
assert json.loads((ROOT/'state/approvals.json').read_text(encoding='utf-8'))['entries'][:-1]==previous_entries
assert json.loads((ROOT/'project.json').read_text(encoding='utf-8'))['structural_correction_policy']['checks']==oldchecks
for f,b in original.items(): assert (HIST/f).read_bytes()==b
(HIST/'snapshot_manifest.json').write_text(json.dumps({'approval_id':AID,'files':{f:digest(b) for f,b in original.items()}},ensure_ascii=False,indent=2),encoding='utf-8')
spec=importlib.util.spec_from_file_location('validator',ROOT/'scripts/validate_project.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
validation=mod.validate(ROOT)
assert validation['ok'],validation
(RUN/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
(RUN/'update_result.json').write_text(json.dumps({'status':'complete','approval_id':AID,'changed_files':files,'master_version':'2.2','additive_revision':'entrances_roofs_20260910','previous_files_preserved':len(files),'all_reference_hashes_preserved':len(manifest['references']),'existing_approval_entries_preserved':True,'structural_auto_correction_scope_unchanged':True,'image_generation_performed':False},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'ok':validation['ok'],'changed_files':len(files),'reference_hashes_verified':len(manifest['references']),'history':str(HIST)},ensure_ascii=False))


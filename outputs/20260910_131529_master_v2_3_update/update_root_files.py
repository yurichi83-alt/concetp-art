from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
AID='master_update_20260910_v2_3'
changed=[]
def read(p):return (ROOT/p).read_text(encoding='utf-8-sig')
def write(p,s):
 if read(p)!=s:
  (ROOT/p).write_text(s,encoding='utf-8');changed.append(p)
def rep(s,a,b):
 assert a in s,('missing replacement',a)
 return s.replace(a,b)
def dump(p,o):write(p,json.dumps(o,ensure_ascii=False,indent=2)+'\n')
# Root-owned current-version banners only. Historical sections retain their old versions.
own=['AGENTS.md','docs/00_INDEX.md','docs/01_COMPOSITION.md','docs/03_VISUAL_STYLE_V2.md','docs/10_CURRENT_REFERENCES.md','README_KO.md','START_HERE_KO.md','FIRST_MESSAGE.txt','.agents/skills/game-env-art/SKILL.md']
for p in own:
 s=read(p).replace('마스터 01~04 v2.2','마스터 01~04 v2.3')
 if p=='README_KO.md':s=s.replace('생성 실행 규칙 v1.3','생성 실행 규칙 v1.4')
 write(p,s)
p='docs/01_COMPOSITION.md';s=read(p).replace('# Master 01 v2.2','# Master 01 v2.3')
s=rep(s,'단면을 지하 보행 통로나 추가 출구로 만들지 않는다.','전면 절개 단면을 지하 보행 통로나 제3의 출구로 만들지 않는다. 뒤쪽 지정된 두 기능 출구 중 하나를 지하 주차장 램프/계단으로 설계하는 것은 가능하다.')
s=rep(s,'의도적으로 회전한 물체는 다른 방향의 소실점을 가질 수 있으나 같은 카메라와 지평선에 종속되어야 한다.','회전한 소품·차량·비건물 구조물은 다른 방향의 소실점을 가질 수 있으나 같은 카메라와 지평선에 종속되어야 한다. 건물의 지상 평면과 플레이어 접촉 외벽은 공통 X/Y축에 맞는 직교 형태로 제한한다. 화면상 사선과 실제 수평 평면의 사선을 혼동하지 않는다.')
s+='''\n## v2.3 직교 건축과 지붕의 면 정합
승인: master_update_20260910_v2_3. 건물 바닥 외곽선과 플레이어 이동에 접하는 고정 외벽은 X/Y축에 평행한 선분으로 연결한다. 사선으로 깎은 모서리·회전된 건물·쐐기형 틈·곡선 보행 경계를 사용하지 않는다. L/T/U형, 직각 후퇴·돌출과 높이가 다른 날개·상층으로 다양화한다.
지붕은 경사·박공·톱니형·배럴형 등으로 달라질 수 있으며 아래 건물의 보행 경계는 직교 형태를 유지한다. 지붕 면/곡면의 경사 시작·끝, 용마루·골·처마, 벽 상단 및 받침을 일관되게 연결한다. 장비 지지 없이 경사면에 떠 있거나 비틀린 면을 의도적 디자인으로 정당화하지 않는다. 면 정합이 불명확하면 UNCERTAIN, 명백한 모순은 FAIL이며 최종 통과로 보고하지 않는다.
직교 제한은 탱크·자동차·트럭·소품의 원래 곡면/회전에 적용하지 않는다. 비건물도 공통 투영·접지와 기능 출구 접근 공간은 지킨다. 두 후방 경계는 방향과 연결 관계이며 동일한 벽 두 줄이나 정해진 문틀 좌표를 복제하는 규칙이 아니다.
'''
write(p,s)
summary='''\n## 승인된 v2.3 보강 — 2026-09-10
승인 ID: master_update_20260910_v2_3. 사용자 “좋아 내용 반영해줘.”에 따라 건물 직교 평면, 지붕 면 정합, 두 기능 출구의 가변 위치·형태·개폐 상태, 건물 입구 겸용, 비건물 경계와 적용 대상을 명확히 했다.
건물은 공통 X/Y축의 L/T/U형·직각 후퇴·높이/지붕 변화로 다양화한다. 탱크·차량·소품의 곡면과 회전은 허용하되 동선·접지를 보존한다. 약11시/1시 두 방향에 출구 기능 하나씩을 두고 각 면의 중앙/중간/끝 모두 가능하다. 문틀에 한정하지 않으며 건물 진입·골목·개폐 철문·계단·지하 주차장도 가능하다. 닫힘/개방 상태와 클리어 후 연결을 구분한다.
건물 입구는 장식 또는 지정 출구 겸용으로 기록한다. 건물용 입구·옥상40~80% 규칙은 탱크/차량에 전용하지 않는다. C01~C04/L01~L07 중 적용 항목 모두 통과해야 하며 L07은 건물 직교 외곽선 검사다. C04/L05의 지붕 면 정합과 지지 검수도 강화했다. 분석/갱신 요청에서는 자동 이미지를 만들지 않는다.
원본24장·선호2장·검토3장과 기존 아트/세계관을 보존한다. 카세트 퓨처리즘 참조/생성물의 메인 승격은 이번 승인에 포함하지 않는다. 변경 전 문서: state/history/20260910_131529_master_v2_3/. 갱신/검증: outputs/20260910_131529_master_v2_3_update/.
'''
p='docs/00_INDEX.md';s=read(p)
s=rep(s,'패키지 1.2 / 마스터 세트 v2.2 / 생성 실행 규칙 v1.3','패키지 1.3 / 마스터 세트 v2.3 / 생성 실행 규칙 v1.4')
s=s.replace('01·02 및 실행·검수에는 v2.2 보강을 적용한다.','01·02 및 실행·검수에는 v2.2 기하 기준에 이어 아래 v2.3 보강을 적용한다.')
write(p,s+summary)
p='docs/10_CURRENT_REFERENCES.md';s=read(p).replace('# 현재 마스터와 참조 사용 범위 — v2.2','# 현재 마스터와 참조 사용 범위 — v2.3')
s=rep(s,'최신 기하·동선 보강 승인: “보강안 내용은 적절해보여. 승인할게 메인 래퍼런스 갱신해줘” (master_update_20260910_v2_2).','최신 기하·게임 동선 보강 승인: “좋아 내용 반영해줘.” (master_update_20260910_v2_3). 직전 기하 보강 승인: “보강안 내용은 적절해보여. 승인할게 메인 래퍼런스 갱신해줘” (master_update_20260910_v2_2).')
s=rep(s,'- 02 / M02-01: 같은 기본 바닥 위의 두 직교 경계, 각 출구 하나, 중앙부터 출구 너머까지의 연속 보행 공간. 특정 건물 두 줄·문틀·동일 평면 배치를 복사하는 규칙이 아니다.','- 02 / M02-01: 같은 기본 바닥 위의 상단 좌·우 직교 경계 방향과 기능 출구 하나씩. 각 면의 중앙/중간/끝 위치와 문·건물 입구·골목·계단·램프 형태는 자유다. 클리어 전 닫힘/이후 개방과 연결 동선을 기록한다. 특정 건물 두 줄·문틀·고정 좌표를 복사하지 않는다.')
s=rep(s,'출입구 디자인은 기존의 외부 이동 출구 두 개와 구분한다. 건물 문/셔터는 실내로 이어지는 표현이며 제3의 외부 통로를 만들지 않는다.','출입구 디자인과 기능 출구는 역할로 구분하며 물리적 분리 의무가 아니다. 건물 문/셔터를 지정된 두 출구 중 하나로 겸용할 수 있다. 나머지는 장식 입구이며 문의 개수로 기능 출구 수를 늘리지 않는다.')
write(p,s+summary)
p='AGENTS.md';s=read(p).replace('L01~L06','L01~L07').replace('## v2.2 구조 적용','## v2.3 구조 적용')
s=rep(s,'- 뒤쪽 좌우 두 면은 이동 불가 경계. 각 면 하나씩 정확히 두 출구, 모두 눈에 보이고 접근 가능.','- 뒤쪽 좌우 두 방향(약11시/1시)은 이동 경계. 방향별 기능 출구 하나씩 정확히 두 개. 각 면 중앙/중간/끝 위치 모두 가능하고 문틀·게이트에 한정하지 않는다. 건물 입구 겸용과 클리어 전 잠금도 허용하며 역할·상태·개방 후 연결과 접근 여유를 기록한다.')
s=rep(s,'- 중앙부터 두 출구 너머까지 폭·높이가 있는 보행 공간을 먼저 확보한다.','- 중앙부터 두 전환 지점 및 개방 후 연결 경로까지 폭·높이가 있는 보행 공간을 먼저 확보한다. 의도된 잠금 장치와 우발적 장애물을 구분한다.')
s=rep(s,'두 외부 출구와 구분.','장식 입구/두 기능 출구 중 하나와 겸용을 역할로 구분. 물리적 분리 의무 아님.')
s+='''\n## v2.3 게임 공간 설계
- 건물 지상 평면/플레이어 접촉 외벽은 공통 X/Y축 직교. L/T/U형·직각 후퇴/돌출·높이/지붕 변화 허용, 사선 건물 모서리·쐐기형 틈 금지. 화면 사선은 투영과 구분한다.
- 탱크·자동차·트럭·프랍의 곡면/회전은 허용. 이들도 경계 역할을 할 수 있으며 두 출구와 중앙 동선·접지·공통 카메라는 보존한다. 사람용 입구·옥상40~80%는 건물에만 적용한다.
- 지붕 면·처마·벽 상단·설비 받침의 연결을 확인한다. 구조안의 AABB 무충돌만으로 통과하지 말고 건물 외곽선 직교(L07)와 최종 지붕 정합(C04/L05)을 따로 검사한다.
- 매 새 장면에서 출구 위치/형태/상태를 재선택하며 기존 끝쪽 좌표를 자동 반복하지 않는다. 무조건 위치를 교대로 바꿀 의무도 없다. 상세02·05·06과 승인 master_update_20260910_v2_3을 따른다.
'''
write(p,s)
p='.agents/skills/game-env-art/SKILL.md';s=read(p).replace('L01~L06','L01~L07').replace('## v2.2 필수 구조 규칙','## v2.3 필수 구조 규칙')
s=rep(s,'뒤쪽 두 면에 출구 하나씩 /','뒤쪽 두 방향에 기능 출구 하나씩(면 안의 위치·형태 가변, 건물 입구 겸용·클리어 전 잠금 허용) /')
s+='''\n## v2.3 실행 보완
건물 지상 외곽선/접촉 외벽은 공통 X/Y축 직교로 계획하고 L07로 검사한다. 단일 상자 대신 L/T/U형·직각 후퇴·높이와 지붕 변화로 다양화한다. 소품·원통 탱크·차량의 곡면/회전은 이 제한 밖이며 벽 역할도 가능하다. 건물용 입구·옥상40~80%를 비건물에 적용하지 않는다.
두 출구는 약11시/1시 방향에 하나씩, 각 면의 중앙/중간/끝 모두 가능하다. 문틀/열린 게이트로 고정하지 않으며 건물 진입·골목·계단·지하주차장 램프도 허용한다. 역할/위치/형태/개폐 상태/클리어 후 연결/건물 입구 겸용을 기록한다. 잠금 상태와 잔해 차단은 구분하고 개방 시 문짝 및 경로 여유를 검토한다.
도해/직전 구조안의 끝쪽 출구 좌표를 자동 복제하지 않는다. 지붕 경사·벽 상단·설비 지지의 정합은 최종 이미지에서 따로 확인하고 불확실한 면을 의도적 형태로 합격시키지 않는다. 승인 master_update_20260910_v2_3; 실행 v1.4.
'''
write(p,s)
p='.agents/skills/game-env-art/agents/openai.yaml';write(p,read(p).replace('마스터 v2.2의 공통 기하·투영·연속 통로','마스터 v2.3의 직교 건물·기능 출구·공통 기하'))
for p in ['README_KO.md','START_HERE_KO.md','FIRST_MESSAGE.txt']:
 s=read(p)
 s+='''\n현재 v2.3/실행1.4에서는 건물 지상 경계를 X/Y축 직교로 설계하고 지붕·높이·직교 매스로 다양화한다. 탱크·차량도 뒤쪽 경계 역할이 가능하다. 약11시/1시 방향의 기능 출구 두 개는 면 안 위치/형태가 자유이며 건물 입구 겸용·클리어 전 닫힘도 가능하다. 출구의 상태와 개방 후 연결을 기록하고, 이전 끝쪽 게이트 배치를 고정하지 않는다. 건물 입구·옥상40~80% 규칙은 건물에만 적용한다.\n'''
 write(p,s)
# Reference semantics, preserved IDs/files/hash/dimensions/provenance.
p='refs/manifest.json';m=json.loads(read(p));m['master_version']='2.3';m['geometry_role_clarification_approval_id']=AID
r=next(r for r in m['references'] if r['id']=='M02-01');old_use=r['use_only'];old_exclude=r['exclude']
r['use_only']='공통 바닥과 기본 입체, 상단 좌·우 직교 경계 방향과 기능 출구 하나씩, 상태에 맞는 접근 및 개방 후 연결 동선, 높이 상한. 각 면 중앙·중간·끝 위치와 출구 형태 가변; 건물 입구 겸용 가능'
r['exclude']='파란 벽·글자·아이콘·화살표·입구 표시와 도해의 문틀/좌표를 의무 복제하지 않음. 중앙 배치 금지가 아니며 중앙·편심·끝 모두 가능'
r['role_clarification_approval_id']=AID
dump(p,m)
for p in ['refs/REFERENCE_MAP.md','REFERENCE_INDEX.html']:
 s=read(p).replace(old_use,r['use_only']).replace(old_exclude,r['exclude'])
 s=s.replace('마스터 v2.2','마스터 v2.3')
 if p.endswith('.html'):
  s=s.replace('<p class="scope">v2.2: 공통 공간·단일 투영·베이스 상하 대응·직교 경계·실제 보행 공간을 강화했다. 원본24장은 보존하며 새 설명 도식/실패 출력 승격은 없다.</p>','<p class="scope">v2.3: 건물 평면은 직교하고 지붕·높이로 다양화한다. 두 기능 출구의 면 안 위치·형태·개폐 상태는 가변이며 건물 입구 겸용이 가능하다. 탱크·차량 등도 경계를 구성할 수 있다. 원본24장과 기존 아트/세계관은 보존한다.</p>')
 else:s+='\nv2.3 승인 master_update_20260910_v2_3: 중앙/끝 출구 모두 가능, 문틀은 의무가 아니며 건물 입구 겸용·상태별 연결을 허용한다. 위 도해는 경계 방향·기능 관계를 참고하며 고정 좌표를 복제하지 않는다. 원본 이미지와 이전 보강 승인 이력은 보존한다.\n'
 write(p,s)
p='templates/references.json';o=json.loads(read(p));o['structure_guide'].update({'building_orthogonal_footprints_checked':False,'roof_planes_and_supports_checked':False,'functional_exit_roles_locations_states_recorded':False,'M02_role':'two functional exits on back-left/back-right directions; locations/forms variable, no fixed gate template'})
dump(p,o)
p='project.json';pobj=json.loads(read(p));pobj.update(package_version='1.3.0',master_version='2.3',execution_rules_version='1.4',master_update_approval_id=AID,updated_date='2026-09-10')
pobj['generation_reference_selection']=pobj['generation_reference_selection'].replace('v2.2','v2.3')+' M02 supplies functional direction/connectivity, not fixed gate locations; building ground footprints are orthogonal and roof planes are validated separately.'
pol=pobj['structural_correction_policy'];pol['checks'].append('L07');pol['checks_clarification_approval_id']=AID
g=pobj['geometry_policy'];g.update(approval_id=AID,rear_boundaries='two adjacent perpendicular back-boundary directions, expressed through buildings or other blocking objects; one functional exit per direction',routes='reserve approach and post-clear/open-state passage volume to each transition; planned lock is distinct from accidental obstruction',building_footprints='common XY-axis orthogonal ground footprint and player-contact walls; L/T/U and right-angle setbacks permitted; no diagonal/chamfered/curved building traversal boundary',prop_shape_exception='tanks/vehicles/props may be curved or rotated; same camera, grounding and clear exit routes required',roof_geometry='varied roof profiles allowed; explicit plane/surface joins, wall-top alignment and supported equipment; uncertainty is not PASS')
g['workflow']=['shared-coordinate building footprints and separate roof/support plan','orthogonal polygon-edge, geometry and route-volume checks','two functional exit role/location/form/state/post-clear-connection plan','art with actual guide/reference inputs','final image structure and state-aware traversal comparison']
pobj['functional_exit_policy']={'approval_id':AID,'count':2,'directions':['back_left_approximately_11_oclock','back_right_approximately_1_oclock'],'position_per_side':'center/intermediate/end, symmetric or asymmetric; no fixed coordinates or forced alternation','forms':['door_or_gate','building_entry_or_internal_transition','alley','facility_passage','stairs','underground_parking_ramp'],'state':'record pre-clear locked or post-clear open; preserve approach, opening clearance and usable post-clear connection','building_entry_may_double_as_exit':True,'count_by':'assigned traversal function, not visible door count','front_cutaway_is_not_third_exit':True}
pobj['boundary_object_policy']={'approval_id':AID,'allowed':['building','wall','fence','container','cylindrical_tank','car','truck','industrial_equipment','debris','terrain'],'requirements':'readable blocking role along two rear directions; no unintended third route; protect center and designated exits'}
arch=pobj['architectural_design_policy'];arch['role_scope_clarification_approval_id']=AID;ent=arch['building_entry'];ent.pop('distinct_from_two_external_exits',None);ent.update(distinct_role_from_map_exit=True,may_double_as_designated_exit=True,physical_separation_required=False,applies_to='buildings only; non-building tanks/vehicles exempt')
arch['rooftop']['applies_to']='buildings only; do not impose roof occupancy on tanks/vehicles'
dump(p,pobj)
p='state/approvals.json';a=json.loads(read(p));assert not any(x.get('id')==AID for x in a['entries'])
a['master_version_approved']='2.3';a['entries'].append({'id':AID,'date':'2026-09-10','type':'orthogonal_buildings_functional_exits_boundary_diversity','status':'active','evidence':'좋아 내용 반영해줘.','proposal_path':'outputs/20260910_130219_geometry_gameplay_reference_proposal/proposal_ko.md','scope':'승인 제안 A~F: 건물 직교 지상 경계/지붕 정합, 가변 두 기능 출구와 개폐 상태·입구 겸용, 비건물 차단체, 계획/QA 일관화','master_version_before':'2.2','master_version_after':'2.3','execution_rules_version_after':'1.4','approved_aspects':['orthogonal_building_player_contact_footprints','roof_plane_and_support_clarity','variable_functional_exit_positions_forms_states','building_entry_exit_dual_role','nonbuilding_boundary_diversity','building_only_entry_and_roof_rules','L07_and_state_aware_structural_QA'],'preserved_aspects':['24_master_image_files_and_hashes','LDI_art_and_salvage_world','previous_reference_approval_history','square_base_shared_camera_two_cut_faces','structural_correction_only_during_generation_requests'],'not_approved_aspects':['new_image_generation_in_this_update','cassette_reference_permanent_promotion','generated_image_master_promotion','fixed_camera_width_coordinates_or_mechanical_ratio','external_API_installation','git_commit_push'],'history_path':'state/history/20260910_131529_master_v2_3','update_record_path':'outputs/20260910_131529_master_v2_3_update'})
a['note']='Master set v2.3 preserves all24 masters and previous art/world; approved orthogonal building geometry, functional exits and boundary diversity are synchronized across rules/config/templates. Historical approval entries remain unchanged.'
dump(p,a)
p='state/CHANGELOG.md';s=read(p)+'''\n## 2026-09-10 — 직교 건물·기능 출구·경계 다양성 / 마스터 v2.3 / 실행 v1.4 / 패키지1.3.0
- 사용자 “좋아 내용 반영해줘.”로 승인된 master_update_20260910_v2_3. 제안 outputs/20260910_130219_geometry_gameplay_reference_proposal/proposal_ko.md.
- 건물 지상 평면/접촉 외벽 직교 제한(L07), 지붕 면·벽 상단·설비 지지 검수 보강. 소품/탱크/차량 곡면·회전은 별도.
- 기능 출구 두 개의 상단 좌우 방향만 고정, 면 안 위치·형태·개폐 상태 가변. 건물 입구 겸용과 지하 주차장 연결 허용. 열린 문틀/끝쪽 좌표 반복 지시 제거.
- 탱크·차량 등 비건물 경계 허용 및 건물용 입구·옥상40~80% 규칙의 대상 명확화.
- 원본24장/선호2장/검토3장 보존. 기존 카세트 참조나 생성물은 메인 승격하지 않음. 이전 문서·출력·승인 이력 보존.
- 변경 전27파일: state/history/20260910_131529_master_v2_3/. 검증: outputs/20260910_131529_master_v2_3_update/.
- 이번 작업은 문서/설정 갱신이며 이미지 생성·설치·API·Git 커밋/푸시 없음.
'''
write(p,s)
(RUN/'root_changed_files.json').write_text(json.dumps(sorted(set(changed)),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'root_owned_files_changed':len(set(changed))}))


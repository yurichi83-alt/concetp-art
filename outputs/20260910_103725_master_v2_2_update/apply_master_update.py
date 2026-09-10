from pathlib import Path
import json, hashlib, shutil, re

ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
HREL="state/history/20260910_103725_master_v2_2"
HISTORY=ROOT/HREL
AID="master_update_20260910_v2_2"
PREL="outputs/20260910_102058_geometry_master_reinforcement_proposal/proposal_ko.md"
files=["AGENTS.md","README_KO.md","START_HERE_KO.md","FIRST_MESSAGE.txt",
"docs/00_INDEX.md","docs/01_COMPOSITION.md","docs/02_LAYOUT.md","docs/03_VISUAL_STYLE_V2.md","docs/04_WORLD_DESIGN_V2.md",
"docs/05_GENERATION_RULES.md","docs/06_QA.md","docs/10_CURRENT_REFERENCES.md",
".agents/skills/game-env-art/SKILL.md",".agents/skills/game-env-art/agents/openai.yaml",
"templates/brief.md","templates/preflight.md","templates/review.md","templates/references.json",
"project.json","refs/manifest.json","refs/REFERENCE_MAP.md","REFERENCE_INDEX.html","state/approvals.json","state/CHANGELOG.md"]
old={f:(ROOT/f).read_text(encoding="utf-8") for f in files}
new=dict(old)
proposal=(ROOT/PREL).read_text(encoding="utf-8")
section3=proposal.split("## 3.")[1].split("## 4.")[0]
clauses=re.findall(r"^> (.+)$",section3,re.M)
assert len(clauses)==7, len(clauses)
def rep(f,a,b):
    if a not in new[f]: raise RuntimeError(f"Missing expected text: {f}: {a[:80]}")
    new[f]=new[f].replace(a,b)
def add(f,s): new[f]=new[f].rstrip()+"\n\n"+s.strip()+"\n"
def js(v): return json.dumps(v,ensure_ascii=False,indent=2)+"\n"

# Active suite version; art/world content and historical supplement approvals remain v2.1.
for f in files:
    if f.endswith((".md",".txt",".yaml")) and f!="state/CHANGELOG.md":
        new[f]=new[f].replace("마스터 01~04 v2.1","마스터 01~04 v2.2")
rep("docs/01_COMPOSITION.md","# Master 01 v2.1","# Master 01 v2.2")
rep("docs/02_LAYOUT.md","# Master 02 v2.1","# Master 02 v2.2")
rep("docs/05_GENERATION_RULES.md","# Generation Execution Rules v1.2","# Generation Execution Rules v1.3")
rep("docs/00_INDEX.md","패키지 1.1 / 마스터 v2.1 / 생성 실행 규칙 v1.2 / 2026-09-09.",
"패키지 1.2 / 마스터 세트 v2.2 / 생성 실행 규칙 v1.3 / 2026-09-10.")
rep("docs/00_INDEX.md","파일명 V2는 호환성을 위해 유지하며 문서 본문은 v2.1이다.",
"파일명 V2는 호환성을 위해 유지한다. 03·04 아트/세계관 본문은 v2.1에서 유지하고, 01·02 및 실행·검수에는 v2.2 보강을 적용한다.")
rep("README_KO.md","생성 실행 규칙 v1.2","생성 실행 규칙 v1.3")
rep("README_KO.md","문서 정리 기준일: 2026-09-09.","문서 정리 기준일: 2026-09-10.")
rep(".agents/skills/game-env-art/agents/openai.yaml","마스터 v2.1과 디오라마 공간 규칙 적용","마스터 v2.2의 공통 기하·투영·연속 통로 적용")

# The seven exact approved clauses are incorporated in their owning documents.
rep("docs/01_COMPOSITION.md","**카메라와 바닥 단면만**","**공통 카메라·기본 베이스 입체·상하 대응 모서리·두 측면 단면**")
rep("docs/01_COMPOSITION.md","직사각형 계열의 독립형 디오라마 베이스 전체를 프레임 안에 담는다.",
"정사각형 기본 평면의 독립형 디오라마 베이스와 연결된 경계 전체를 프레임 안에 담는다. 기본 외형 변경은 사용자 명시 요청으로만 적용한다.")
rep("docs/01_COMPOSITION.md","새 장소에서는 건축의 용도와 매스, 공간 폭, 포장, 외곽 기반 시설을 장소에 맞게 새로 설계한다.",
"새 장소에서는 공통 공간 틀 안에서 건축 용도·매스·내부 공간 폭·포장·외곽 기반 시설을 새로 설계한다. 배치 변화가 기본 입체의 휨이나 임의 외형 변경을 허용하지 않는다.")
add("docs/01_COMPOSITION.md","\n\n".join([
"## v2.2 공통 공간 틀\n"+clauses[0],
"## v2.2 공통 카메라와 투영\n"+clauses[1]+"\n\n권장 기본은 일관된 평행투영 쿼터뷰다. 약한 투시를 선택해도 한 장면에서 하나로 고정하고 브리프에 기록한다. 카메라 수치가 미정이어도 공통 투영은 필수다.",
"## v2.2 기본 블록과 단면 정합\n"+clauses[2]+"\n\n화면의 모든 직각을 90도로 만들거나 원근 때문에 줄어드는 화면상 두께를 같게 맞추라는 뜻이 아니다. 같은 3D 입체의 투영을 검사한다. 디오라마에 붙은 잘린 벽을 배경 예외로 인정하지 않는다."]))

rep("docs/02_LAYOUT.md","**경계와 연결 관계**","**공통 바닥·기본 입체·직교 경계·두 출구와 연속 동선**")
rep("docs/02_LAYOUT.md","고정되는 것은 뒤쪽 서로 인접한 두 경계의 연결 관계다.",
"같은 베이스의 인접한 두 뒤쪽 변 위에서 만나는 직교 경계의 기본 형태와 연결 관계를 함께 고정한다.")
rep("docs/02_LAYOUT.md","- 큰 오브젝트는 외곽으로 보내고 두 출구 접근로도 확보한다.",
"- 두 출구의 보행 보호 공간을 먼저 확보하고 그 밖의 외곽에 큰 물체를 둔다. 외곽이라는 이유로 통로를 점유할 수 없다.")
rep("docs/02_LAYOUT.md","한 장면의 잘못된 평면을 보정하기 위해 사용한 단일 바닥 높이·격자 방향을 모든 장소의 영구 규칙으로 만들지 않는다.",
"바닥·기초·문턱·외벽은 01의 공통 기준면과 투영에 맞춘다. 장면의 특정 높이나 건물 방향을 모든 장소에 복제하지 않되 공통 입체/카메라는 항상 유지한다.")
add("docs/02_LAYOUT.md","\n\n".join([
"## v2.2 경계의 기하 관계\n"+clauses[3],
"## v2.2 실제 보행 보호 공간\n"+clauses[4]+"\n\n폭은 장면의 공통 사람 스케일로 계획하고 전체 구간에서 유지한다. 임의의 2m/2인 폭을 영구 수치로 고정하지 않는다. 가려진 핵심 경로는 UNCERTAIN이다.",
"## H07: 내부 이동과 방 깊이\n"+clauses[5]]))

rep("docs/05_GENERATION_RULES.md","는 생성 요청이 아니다.",
"는 생성 요청이 아니다. 분석/보강안 정리/마스터 갱신에서도 구조 오류를 발견했다는 이유로 자동 생성하지 않는다.")
rep("docs/05_GENERATION_RULES.md","M02-01 연결 관계, M01-01 구도·단면",
"M02-01 공통 바닥/직교 경계/연속 통로, M01-01 공통 투영/기본 입체/상하 대응/구도·단면")
workflow=proposal.split("## 5. 생성 절차 보강안\n")[1].split("## 6.")[0].strip()
rep("docs/05_GENERATION_RULES.md","## 4. 실제 생성 사양",
"## 3a. 구조안부터 최종 대조까지 — v1.3\n\n"+workflow+
"\n\n검토용 설명 도식은 양성 마스터로 자동 등록하지 않는다. 참고 안내 파일은 실제 도구의 지원 형식으로 준비하며 SVG 지원이나 실제 전달을 추정하지 않는다.\n\n## 4. 실제 생성 사양")
rep("docs/05_GENERATION_RULES.md","- 베이스 전체와 앞쪽 두 측면 단면이 보이는 사선 하이앵글. 크롭을 방지할 주변 여유를 둔다.",
"- 정육면체형 공통 공간/정사각형 기본 평면과 하나의 투영을 사용한다. 전체 베이스·상하 대응 모서리·두 평면 단면·연결 경계를 사선 하이앵글로 프레이밍한다.")
rep("docs/05_GENERATION_RULES.md","- 중앙에 넓고 연속된 빈 전투 바닥. 외곽 물체도 출구를 막지 않는다.",
"- 중앙부터 두 출구 너머까지 폭·높이·회전 여유를 확보한 보행 공간을 비운다. 외곽 물체도 침범하지 않는다. 내부 노출 시설은 실체적 방 깊이와 내부 동선을 확보한다.")
rep("docs/05_GENERATION_RULES.md","- 대상: 출구 수·위치·가시성, 뒤쪽 경계, 건물 배치/각도와 지면 정렬, 중앙·출구 동선, 전체 프레이밍과 바닥 단면.",
"- 대상: C01~C04, L01~L06. 프레이밍/단면·기본 입체·공통 투영·경계/출구·접지·중앙/출구 및 해당 내부 동선. 검사 구체화 승인: "+AID+".")
rep("docs/05_GENERATION_RULES.md","- 매 결과를 실제로 열어 구조를 검수한다. 구조 통과한 결과를 요청한 최종 장수로 전달하고 추가 변형을 중단한다.",
"- 매 결과를 실제로 열어 구조안과 대조한다. 해당 구조 항목 전부 PASS이고 적절한 N/A 근거가 있을 때 구조 통과로 전달한다. 구조 FAIL은 전체 needs_revision, 핵심 불확실은 uncertain이다. 통과 후 추가 변형을 중단한다.")
add("docs/05_GENERATION_RULES.md","## 구조 기록과 판정\n장면 구조안은 같은 좌표의 기본 블록·카메라·경계/출구·건물 부피·보행 보호 공간을 담아 outputs의 해당 run에 structure_plan.*로 저장한다. 지원되는 파일 형식을 사용하고 브리프에 투영과 통로의 최소 구간/회전부/문턱 전후 확인을 기록한다.\n\n"+clauses[6])

# QA changes.
rep("docs/06_QA.md","공간 → 전투 동선 → 스타일 → 세계관 → 개별 요청.",
"기본 입체 → 공통 투영 → 바닥/경계 접합 → 두 외부 통로 → 해당 내부 동선 → 스타일 → 세계관 → 개별 요청.")
replacements={
"| C01 | 단독 쿼터뷰와 베이스 전체 프레이밍 | 일반 풍경, 분할 패널, 베이스 크롭 |":
"| C01 | 단독 쿼터뷰·전체 프레이밍·독립성 | 베이스/연결 경계 크롭, 붙어 있는 잘린 벽을 배경 예외로 취급 |",
"| C02 | 앞쪽 두 측면의 두께와 내부 단면 | 평면 바닥, 막힌 검은 벽만 존재 |":
"| C02 | 양면 단면의 존재와 두께/모서리 대응 | 단면이 보여도 상하 대응·평면 접합이 틀림 |\n| C03 | 기본 블록 기하 | 기준면 비틀림, 대응 수직 모서리 불일치, 요청하지 않은 곡률/모따기/추가 꼭짓점 |\n| C04 | 공통 카메라·투영 | X/Y/Z 선군과 기초·외벽·포장·출구의 투영 불일치, 회전과 원근 오류 혼동 |",
"| L01 | 뒤쪽 좌우 이동 경계 | 경계 불명확, 통과 가능해 보이는 추가 틈 |":
"| L01 | 공통 바닥 위의 인접한 두 직교 경계 | 기본 입체와 어긋난 경계/접합, 제3의 틈 |",
"| L02 | 왼쪽 출구 하나·오른쪽 출구 하나 | 한쪽 누락, 불분명한 문, 세 번째 큰 통로 |":
"| L02 | 좌우 각 하나의 외부 출구와 전후 바닥 | 문틀만 보임, 한쪽 누락, 문턱 너머 차단/단절, 제3의 외부 통로 |",
"| L03 | 중앙과 출구 접근로 개방 | 중앙 진열대/프레스/드럼통, 차량이 출구 차단 |":
"| L03 | 중앙부터 두 출구 너머까지 연속 보행 부피 | 시작부/최소 폭/회전부/문턱 전후에 상자·잔해·난간·장치·문짝 침범, 가는 빈 선만 존재 |",
"| L05 | 지면 연결·건물 정렬 | 바닥이 비틀리거나 서로 다른 평면처럼 갈라짐, 건물 접지/방향과 포장 격자가 모순됨 |":
"| L05 | 기준면·건물 기초·외벽·문턱의 접합/지지 | 높이/축/투영의 모순, 근거 없는 바닥 비틀림/단절 |\n| L06 | 해당하는 내부 시설의 이동 공간 | 입구→통로→기능 영역 차단, 외관 대비 얕은 진열 상자. 내부 미노출/미해당은 N/A |",
"구조 오류(C01~C02, L01~L05)":"구조 오류(C01~C04, L01~L06)"
}
for a,b in replacements.items(): rep("docs/06_QA.md",a,b)
rep("docs/06_QA.md","## 상태",
"## v2.2 필수 구조 판정\n"+clauses[6]+
"\n\n- C01 프레이밍은 C03 기본 기하/C04 투영을 대신하지 않는다. C02도 흙/배관의 존재만으로 통과하지 않는다.\n- L03은 좌/우 각각 시작부·최소 폭·회전부·문턱·문턱 너머를 기록하고 물체의 부피 침범을 검사한다.\n- L06은 해당 실내를 보이는 경우 적용하고 미해당은 N/A 근거를 기록한다.\n- 모든 적용 구조 항목이 PASS여야 통과한다. 구조 FAIL 하나는 전체 needs_revision이며 핵심 불확실은 uncertain이다.\n- 정투영의 평행선과 투시의 방향별 소실점/공통 지평선을 구분한다. 계획된 회전도 같은 카메라를 따라야 한다.\n- 3D 치수/콜라이더 미검증은 눈에 보이는 차단/비틀림의 면제 사유가 아니다.\n\n## 상태")

# Top-level entry, skill and templates.
rep("AGENTS.md","- 한 이미지 = 단독 쿼터뷰 디오라마 하나. 전체 베이스를 여유 있게 프레이밍. 분할 패널/풍경 크롭 금지.",
"- 한 이미지 = 하나의 정육면체형 가상 공간에 배치한 단독 쿼터뷰 디오라마. 정사각형 기본 평면·공통 XYZ/척도·하나의 투영을 지킨다. 기본 외형 예외는 사용자 명시 요청만. 전체 베이스와 연결 경계를 프레이밍한다.")
rep("AGENTS.md","- 카메라 쪽 두 측면의 바닥 두께와 지층·배관 단면을 드러낸다.",
"- 두 전면 평면 단면을 드러내고 상하 대응 모서리/수직축을 맞춘다. 요청하지 않은 곡률·모따기·비틀림·두께 변화는 불합격이다.")
rep("AGENTS.md","- 중앙 전투 바닥과 두 출구 접근로는 비운다. 큰 물체는 외곽. 마트라고 중앙 진열대를 자동 배치하지 않는다.",
"- 중앙부터 두 출구 너머까지 폭·높이가 있는 보행 공간을 먼저 확보한다. 외곽 상자/잔해/장치도 침범 금지. 내부 시설은 방 깊이와 내부 동선을 확보한다.")
add("AGENTS.md","## v2.2 구조 적용\n구조안 → 아트 적용 → 최종 기하/동선 대조 순서로 작업한다. C01~C04·L01~L06 중 FAIL 하나라도 있으면 전체 needs_revision, 핵심 불확실은 uncertain이다. 전체 기하 오류는 실패 형태 보존을 중단하고 재구성한다. 분석/검수/마스터 갱신 요청에서는 구조 오류 발견으로 자동 생성하지 않는다.")
rep("docs/00_INDEX.md","“좁은 공간”은 베이스 폭을 줄일 수 있지만 두 출구와 연속된 싸움/이동 공간을 삭제하지 않는다.",
"“좁은 공간”은 공통 공간 틀 안의 건물/길 배치를 조정하되 두 출구와 연속 보행 공간을 삭제하지 않는다. 기본 외형 예외는 사용자 명시 요청으로 구분한다.")
add("docs/00_INDEX.md","## 승인된 v2.2 보강 — 2026-09-10\n승인 ID: "+AID+". 정육면체형 공통 공간/정사각형 평면, 단일 투영, 상하 대응 모서리/평면 단면, 직교 경계, 실제 보행 부피, 실내 동선과 구조 우선 검수를 적용한다. C03/C04/L06를 추가하고 구조 FAIL/핵심 불확실을 전체 합격으로 처리하지 않는다.\n원본24장과 03·04 아트/세계관 본문은 유지한다. 설명 SVG/실패 출력 승격과 별도로 보류 중인 스타일 항목의 메인 갱신은 포함하지 않는다.")

rep(".agents/skills/game-env-art/SKILL.md","4. templates의 형식을 참고해 outputs의 새 run 폴더에 브리프·전달 기록·사전 점검을 작성한다.",
"4. 같은 XYZ/척도와 하나의 투영으로 기본 블록·경계/출구·건물 부피·보행 보호 공간의 구조안을 먼저 만든다. templates에 따라 구조안·브리프·참조 전달·사전 점검을 outputs에 기록한다.")
rep(".agents/skills/game-env-art/SKILL.md","6. 실제 결과를 저장하고 열어 구조·아트·세계관·현재 키워드를 나누어 검수한다.",
"6. 실제 결과를 저장하고 열어 구조안과 대조한다. 기본 입체→공통 투영→접지/경계→두 외부 통로→해당 내부 동선→아트/세계관/키워드 순서로 검수한다.")
add(".agents/skills/game-env-art/SKILL.md","## v2.2 필수 구조 규칙\n정육면체형 공통 공간·정사각형 기본 평면·하나의 카메라/투영 및 상하 대응 모서리를 유지한다. 통로는 가는 빈 선이 아닌 보행 폭/높이/회전 여유로 검사한다. 외곽 잔해/상자/장치 부피도 포함한다.\nC01~C04·L01~L06에서 FAIL 하나라도 있으면 needs_revision, 핵심 불확실은 uncertain이다. 전체 입체/원근 오류는 잘못된 기하를 보존하는 편집 대신 01·02에서 재구성한다. 분석/검수/마스터 갱신만 요청된 경우 자동 생성하지 않는다. 시각적 오류를 3D 치수 미검증으로 면제하지 않는다.")

rep("templates/brief.md","- masters: v2.1","- masters: v2.2")
rep("templates/brief.md","- execution_rules: v1.2","- execution_rules: v1.3")
rep("templates/brief.md","## Scene plan",
"## Shared geometry plan before art\n- structure_plan_artifact:\n- common_XYZ_scale_and_square_footprint:\n- single_projection_mode_and_camera:\n- top_bottom_corner_correspondence_and_cut_planes:\n- protected_left_route_start_narrowest_turn_threshold_beyond:\n- protected_right_route_start_narrowest_turn_threshold_beyond:\n- building_prop_volumes_outside_routes:\n- interior_depth_and_aisle_or_NA:\n- planned_steps_rotations_and_ground_connections:\n- previous_faulty_geometry_not_to_preserve:\n- final_image_structure_comparison:\n\n## Scene plan")
rep("templates/preflight.md","| Whole base and front cutaway | UNKNOWN | |",
"| Shared cubic space / square footprint / single projection | UNKNOWN | |\n| Structure plan: corner correspondence / vertical axes / cut planes | UNKNOWN | |\n| Whole base, connected boundaries and front cutaway | UNKNOWN | |")
rep("templates/preflight.md","| Empty central floor and approaches | UNKNOWN | |",
"| Left route: start / narrowest / turn / threshold / beyond | UNKNOWN | |\n| Right route: start / narrowest / turn / threshold / beyond | UNKNOWN | |\n| Props/rubble/protrusions outside walking volume | UNKNOWN | |\n| Interior room depth / aisle or justified N/A | UNKNOWN | |")
rep("templates/review.md","- further_generation_authorized: structural_errors_only (2026-09-09 standing approval)",
"- further_generation_authorized: structural_errors_only_for_generation_requests (standing approval; checks clarified by "+AID+")\n- structure_plan_and_projection_compared:\n- structural_gate: any_FAIL_means_needs_revision; critical_uncertainty_means_uncertain")
rep("templates/review.md","| C02 | NOT_REVIEWED | |",
"| C02 | NOT_REVIEWED | Visible cuts plus thickness/corner correspondence. |\n| C03 | NOT_REVIEWED | Four-corner plane / vertical correspondence / no unintended curve or bevel. |\n| C04 | NOT_REVIEWED | Single projection across floor, buildings and boundaries. |")
rep("templates/review.md","| L03 | NOT_REVIEWED | |",
"| L03 | NOT_REVIEWED | Both routes: start, narrowest, turn, threshold, beyond; object-volume intrusion. |")
rep("templates/review.md","| L05 | NOT_REVIEWED | |",
"| L05 | NOT_REVIEWED | |\n| L06 | NOT_REVIEWED | Interior entry/aisle/functional space and depth, or justified N/A. |")
add("templates/review.md","Global block/projection faults require reconstruction without preserving failed geometry. Review/analysis/master-update-only requests do not trigger generation. All applicable structural checks must pass before overall structural pass.")
rt=json.loads(new["templates/references.json"])
rt["structure_guide"]={"path":None,"projection_mode":None,"inspected":False,"submitted":False,"input_format_verified":False,"role":"scene-specific structure guide; not automatically a positive master"}
new["templates/references.json"]=js(rt)
add("README_KO.md","## v2.2 기하·동선\n공통 정육면체형 공간과 하나의 투영에서 구조안을 먼저 만들고 아트 적용 뒤 최종 결과를 대조합니다. 기본 블록 기하(C03), 공통 투영(C04), 내부 동선(L06)과 실제 보행 부피를 검사합니다. 구조 FAIL/핵심 불확실은 전체 합격으로 처리하지 않습니다.")
for f in ["START_HERE_KO.md","FIRST_MESSAGE.txt"]:
    rep(f,"중앙 전투 공간은 비우고, 뒤쪽 두 면의 출구 두 개와 전체 디오라마·바닥 단면을 유지해줘.",
"정육면체형 공통 공간과 하나의 투영으로 구조안을 먼저 잡고, 중앙부터 두 출구 너머까지 물체가 침범하지 않는 보행 공간을 확보해줘. 베이스 상하 대응/평면 단면과 실내 이동 공간도 검사해줘.")
rep("START_HERE_KO.md","좁은 골목은 베이스를 좁게 설계하되 중앙 동선과 출구를 막지 않습니다.",
"좁은 골목은 공통 공간 틀 안의 배치를 조정하되 중앙과 출구의 보행 공간을 막지 않습니다.")

# Reference role metadata and active policy; old image records/approvals are preserved.
roles={"M01-01":"공통 쿼터뷰 카메라·투영, 기본 베이스 입체, 상하 대응 모서리·두께와 두 평면 단면",
"M02-01":"공통 바닥과 기본 입체, 인접한 두 직교 경계, 각 출구와 중앙부터 문턱 너머까지 연속 보행 공간, 높이 상한"}
manifest=json.loads(new["refs/manifest.json"])
for item in manifest["references"]:
    if item["id"] in roles:
        for f in ["refs/REFERENCE_MAP.md","REFERENCE_INDEX.html"]: rep(f,item["use_only"],roles[item["id"]])
        item["use_only"]=roles[item["id"]]
        item["role_clarification_approval_id"]=AID
manifest["master_version"]="2.2"
manifest["geometry_role_clarification_approval_id"]=AID
new["refs/manifest.json"]=js(manifest)
rep("refs/REFERENCE_MAP.md","# Reference Map — 마스터 v2.1","# Reference Map — 마스터 v2.2")
add("refs/REFERENCE_MAP.md","v2.2 승인 "+AID+"에 따라 M01/M02 역할을 보강했다. 원본24장 파일/해시와 v2.1 보강 이미지 승인 이력은 유지한다. 설명 도식/실패 출력은 새 양성 참조가 아니다.")
rep("REFERENCE_INDEX.html","<title>마스터 v2.1과 선호 결과 참조</title>","<title>마스터 v2.2와 선호 결과 참조</title>")
rep("REFERENCE_INDEX.html","<h1>마스터 v2.1 · 참조 역할과 사용 범위</h1>","<h1>마스터 v2.2 · 참조 역할과 사용 범위</h1>")
rep("REFERENCE_INDEX.html","<h2>마스터 24장 — 원본 19장 + 승인 보강 5장</h2>",
'<p class="scope">v2.2: 공통 공간·단일 투영·베이스 상하 대응·직교 경계·실제 보행 공간을 강화했다. 원본24장은 보존하며 새 설명 도식/실패 출력 승격은 없다.</p>\n<h2>마스터 24장 — 원본 19장 + 승인 보강 5장</h2>')
rep("docs/10_CURRENT_REFERENCES.md","# 현재 마스터와 참조 사용 범위 — v2.1 / 2026-09-09","# 현재 마스터와 참조 사용 범위 — v2.2 / 2026-09-10")
rep("docs/10_CURRENT_REFERENCES.md","사용자가 사전 검토 후 “좋아 문제 없으면 승인할게”라고 승인한 보완안이다.",
"최신 기하·동선 보강 승인: “보강안 내용은 적절해보여. 승인할게 메인 래퍼런스 갱신해줘” ("+AID+"). 원본 구성과 03·04 아트/세계관은 이전 v2.1 승인에서 유지한다. 이전 보강")
rep("docs/10_CURRENT_REFERENCES.md","- 01 / M01-01: 쿼터뷰 카메라, 전체 베이스, 두 전면 측면 단면.",
"- 01 / M01-01: 공통 쿼터뷰 카메라/투영, 기본 베이스 입체, 상하 대응 모서리와 두 평면 단면.")
rep("docs/10_CURRENT_REFERENCES.md","- 02 / M02-01: 뒤쪽 두 경계, 각 경계의 출구 하나, 빈 중앙과 연결 동선.",
"- 02 / M02-01: 같은 기본 바닥 위의 두 직교 경계, 각 출구 하나, 중앙부터 출구 너머까지의 연속 보행 공간.")
rep("docs/10_CURRENT_REFERENCES.md","## 이번에 보완한 공통 원칙","## v2.1에서 유지하는 공통 원칙")
add("docs/10_CURRENT_REFERENCES.md","## 승인된 v2.2 보강\n승인 ID: "+AID+". 검토 제안: ../"+PREL+".\n공통 정육면체형 공간/정사각형 평면, 단일 투영, 기본 베이스 상하 대응/평면 단면, 인접한 직교 경계, 보행 보호 부피, 내부 이동 공간과 구조 우선 합격 조건을 적용한다. 상세 문안은 01·02·05·06, 검사 대상은 C01~C04/L01~L06이다.\n원본24장의 파일/해시와 보강5장의 기존 승인 이력은 보존하고 M01/M02 역할 설명만 보강했다. 설명 SVG와 실패 출력의 양성 마스터 등록, 정확한 카메라 수치/미터 치수/고정 통로 폭, 별도 보류 중인 카세트 퓨처리즘/CRT 및 모든 건물·소품 세계관 명문화의 메인 갱신은 이번 승인에 포함하지 않는다. 해당 대화 지시를 무효화하는 뜻은 아니다.\n이전 파일: "+HREL+"/. 갱신/검증 기록: outputs/"+RUN.name+"/.")

checks=["C01","C02","C03","C04","L01","L02","L03","L04","L05","L06"]
project=json.loads(new["project.json"])
project.update(package_version="1.2.0",master_version="2.2",execution_rules_version="1.3",updated_date="2026-09-10",master_update_approval_id=AID)
project["generation_reference_selection"]=project["generation_reference_selection"].replace("v2.1","v2.2")+" M01/M02 govern basic geometry, single projection, perpendicular boundaries and continuous walking volumes. Compare final art to a scene-specific structure guide."
policy=project["structural_correction_policy"]
policy["checks"]=checks
policy["checks_clarification_approval_id"]=AID
policy["non_generation_requests_excluded"]=["analysis","review_only","master_update","file_organization"]
policy["pass_gate"]="All applicable structural checks PASS; any FAIL => needs_revision; critical uncertainty => uncertain."
policy["global_geometry_fault_strategy"]="Rebuild common structure without preserving faulty geometry; zoom-out alone is not geometry correction."
project["geometry_policy"]={
"approval_id":AID,"spatial_frame":"single cubic virtual space with shared XYZ axes and scale",
"default_base_footprint":"square; shape exceptions require explicit user request",
"default_projection_preference":"consistent parallel quarter-view",
"allowed_projection":["single parallel/orthographic projection","single coherent weak-perspective projection"],
"fixed_camera_numbers":None,"base_geometry":"four-corner plane extruded by consistent depth; corresponding vertical corners and planar front cuts",
"unrequested_base_curves_bevels_or_warping":False,
"rear_boundaries":"adjacent perpendicular rear sides of the same base; one external exit each",
"routes":"reserve width, height and turning clearance from center through each threshold and beyond before object placement",
"interior":"when applicable, room depth and entry-to-functional-space circulation",
"workflow":["shared-coordinate structure plan","geometry and route-volume check","art with actual guide/reference inputs","final structure comparison"],
"numeric_clearance_requires_3d_validation":True}
new["project.json"]=js(project)
approvals=json.loads(new["state/approvals.json"])
assert not any(e.get("id")==AID for e in approvals["entries"])
approvals["master_version_approved"]="2.2"
approvals["entries"].append({
"id":AID,"date":"2026-09-10","type":"geometry_and_traversal_master_reinforcement","status":"active",
"evidence":"보강안 내용은 적절해보여. 승인할게 메인 래퍼런스 갱신해줘","proposal_path":PREL,
"scope":"승인 제안의 7개 기하·동선 규칙, 구조안/실행·검수·템플릿 및 관련 설정·참조 역할 동기화",
"master_version_before":"2.1","master_version_after":"2.2","execution_rules_version_after":"1.3",
"approved_aspects":["cubic_shared_spatial_frame","single_projection","base_corner_and_plane_consistency","perpendicular_rear_boundaries","continuous_walkable_route_volumes","usable_interior_circulation","geometry_first_generation_and_hard_QA_gate"],
"structural_checks":checks,
"preserved_aspects":["24_reference_image_files_and_hashes","LDI_art_and_v2_1_style_content","Salvage_Cyberpunk_world_content","preferred_and_review_only_hierarchy","existing_structural_auto_correction"],
"not_approved_aspects":["generated_image_master_promotion","explanatory_SVG_positive_reference_registration","separately_deferred_cassette_CRT_and_all_props_style_master_updates","fixed_camera_numbers_or_global_passage_width","new_concept_image_generation_in_this_update","external_API_installation_global_settings","git_commit_or_push"],
"history_path":HREL,"update_record_path":"outputs/"+RUN.name})
approvals["note"]="Master set v2.2 preserves all 24 reference images and v2.1 art/world content; geometry, traversal and execution/QA strengthened by explicit approval. Historical approvals and supplement provenance remain unchanged."
new["state/approvals.json"]=js(approvals)
add("state/CHANGELOG.md","## 2026-09-10 — 승인된 기하·동선 보강 / 마스터 세트 v2.2 / 실행 v1.3 / 패키지 1.2.0\n- 승인: “보강안 내용은 적절해보여. 승인할게 메인 래퍼런스 갱신해줘”. ID: "+AID+". 제안: "+PREL+".\n- 공통 정육면체형 공간, 단일 투영, 베이스 상하 대응/평면 단면, 직교 경계, 실제 보행 부피, 내부 이동 공간과 구조 우선 검수를 반영.\n- C03/C04/L06를 QA·실행·project.json·템플릿에 연결. 구조안→아트→최종 대조. 전체 기하 오류는 실패 형태 보존 대신 재구성.\n- M01/M02 역할을 문서·manifest·참조표·갤러리에 동기화. 진입문서와 프로젝트 스킬도 갱신.\n- 원본24장, 기존 03·04 아트/세계관 본문과 승인/부분 선호 보존. 설명 SVG/실패 이미지 승격 및 별도 보류 스타일 항목 갱신 없음.\n- 이전 파일: "+HREL+"/. 검증: outputs/"+RUN.name+"/. 이번 이미지 생성·설치·API·커밋/푸시 없음.")

# Validate all intended content before making backups and changing active files.
for f in files:
    if f.endswith(".json"): json.loads(new[f])
image_records=[]
for item in json.loads(old["refs/manifest.json"])["references"]:
    actual=hashlib.sha256((ROOT/item["path"]).read_bytes()).hexdigest()
    assert actual==item["sha256"],item["id"]
    image_records.append({"id":item["id"],"path":item["path"],"sha256":actual})
if HISTORY.exists(): raise RuntimeError("History exists; refusing overwrite")
HISTORY.mkdir(parents=True)
backups=[]
for f in files:
    source,dest=ROOT/f,HISTORY/f
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(source,dest)
    h=hashlib.sha256(source.read_bytes()).hexdigest()
    assert hashlib.sha256(dest.read_bytes()).hexdigest()==h
    backups.append({"path":f,"sha256":h})
(HISTORY/"snapshot_manifest.json").write_text(js({"source_master_version":"2.1","files":backups,"reference_image_hashes":image_records}),encoding="utf-8")
changed=[]
for f in files:
    if new[f]!=old[f]:
        (ROOT/f).write_text(new[f],encoding="utf-8",newline="\n")
        changed.append(f)
result={"status":"updated_pending_validation","approval_id":AID,"master_version":"2.2","execution_rules_version":"1.3","package_version":"1.2.0",
"history_path":HREL,"changed_files":changed,"backup_file_count":len(backups),"reference_images_verified_before_update":len(image_records),
"concept_images_generated":0,"git_commit_or_push":False}
(RUN/"update_result.json").write_text(js(result),encoding="utf-8")
print(js(result))


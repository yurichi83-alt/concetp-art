# Generation brief — master v2.7 / execution v1.8

- 요청 원문: 고철상 / 낮 / 황무지 / 한 장
- mode: new_location; use_case: stylized-concept; 최종 전달1장.
- 선택: 낮고 긴 곡면 회수기계 외장 작업장, 편심 상부 사무실과 정비 데크, 대형 원통 분류설비·고철 적재 경계. 마른 흙/큰 작업 슬랩, 절제된 황무지 배경.
- 현재 장면만 적용: 건물1동+별도 비건물 분류기, 따뜻한 흙빛/차가운 하늘 그림자. 이전 시가지의 ㄱ자/층별 기계비율/자동차/전봇대/밤/안개를 상속하지 않는다.
- 세계관: Salvage Cyberpunk. 오래된 대형 기계 외장을 작업장으로 전용, 교체 패널/어댑터와 우회 공급선, 현재 쓰이는 분류 장치와 유지 접근으로 설명.
- 표현: LDI의 큰 형태·넓은 깨끗한 기본 색면·큰 명암, 일부 인접 톤의 크고 성긴 평면 붓터치. 선택적인 큰 손상/수리와 표면 붓터치를 분리. 미세 녹·자갈·파편 과밀을 피한다.
- 실제 콜리전·메시·UV 검수 범위: 제외. 현재 PNG의 접지·지지·형태·연결·동선은 검사.

## 구조와 관찰 계획

structure_plan.json / structure_guide.png에 장면별 공통 XYZ·정사영 투영·큰 형태·두 출구를 기록한다. 가이드 PNG는 참고이며3D 강제 제약이 아니다. 베이스는 정사각 평면과 일정 깊이의 전면2단면, 전체 프레이밍. 직선 구조축과 곡면 접선은 분리한다. 작업장 기단/셔터 수평·계단 착지부/상부 데크 수평보를 베이스·포장과 대조한다.

| 기능 | 위치·형태·상태 | 접근/개방 후 연결 |
|---|---|---|
| 좌측 기능 출구 | 뒤좌 방향 작업장 끝과 재사용 패널 경계 사이 열린 배송 접근로 | 중앙에서 이어지는 넓은 마른 바닥, 문짝/적재/계단 돌출 금지, 황무지 외부 연결 |
| 우측 기능 출구 | 뒤우 방향 높은 분류설비 프레임/데크 아래 열린 서비스 통로 | 지지 기둥은 길 밖, 폭·머리 여유와 뒤쪽 연결부가 보이며 펜스·호퍼·재고 차단 금지 |
| 작업장 셔터·사무실 문 | 닫힌 사람용 입구, 장식/건물 기능 | 두 맵 전환 기능에 추가하지 않음, 입구의 접지와 계단/데크 연결 확보 |

노출 실내는 없음: L06 N/A 예정(최종 결과가 실내를 노출하면 재검사). 건물별 윗면40~80%는 통합 정비 데크·환기부·보호 차양의 실제 기능 점유로 계획하고 건물 전체 기계화율과 구분. 비건물 분류기는 건물 입구/옥상 규칙을 적용하지 않는다. 자세한 면적·카메라 선택은 구조안에 기록하며 최종 PNG에서 계측 완료로 주장하지 않는다.

## 요구사항 → 실제 지시 → 검수

| 요구 | generation_prompt.md의 대응 구절/설계 | QA |
|---|---|---|
| 단독 쿼터뷰/전체/장수1 | ONE finished…complete standalone high-angle quarter-view; one diorama | C01/R01 |
| 정사각 평면/두 단면/깊이 | one square plane extruded…BOTH planar front cutaway faces; equal downward corner displacement | C02/C03 |
| 정사영 공통축/척도 | single ORTHOGRAPHIC…same-direction straight edges stay parallel…no depth-based enlargement | C04 |
| 곡면·주요직선축·기단 | Building placement and straight…X/Y; rounded…legible contact; important footing edges visible | L07/C04 |
| 지붕/지지/계단 | roof curves/slopes connect…supporting members; office visibly supported; proper landings | C04/L05 |
| 두 뒤경계/추가통로금지 | EXACTLY TWO; continuous barriers with no accidental third gap | L01/L02 |
| 출구위치형태상태 | Back-left open delivery; Back-right deeper framed underpass | L02 |
| 접근/회전/폭/높이/개방연결 | both approach/turn/transition volumes free; columns OUTSIDE walking width; visible headroom | L03 |
| 중앙/전면열림 | central combat/walking free…foreground open | L03/L04 |
| 높이계획/접지 | about6.5m human-scale; local foundations; common axes | L05 |
| 실내 | closed doors/shutter; no exposed room expected | L06 N/A if observed |
| 건물별 사람입구 | closed human door + roll-up shutter; non-transition | W04 |
| 옥상40~80·기계비중분리 | purposeful…40–80%; not facade ratio; no redundant rooftop kit | W05 |
| 큰형태/깊이/장소차이 | LONG LOW machine-casing workshop; offset office/deck; nonbuilding sorter boundary | R02/S04 |
| 단면장소기능 | weighing-floor foundation, arid layers, power/hydraulic lines tied to sorter | C02/W03/R02 |
| 수리·회수기술/쇠락 | shell repurposed…replacement panels/adapters…rerouted supply | W01/W02/W03 |
| 색면·붓터치·손상분리 | BROAD flat directional…nearby-tone…independent of rust/damage | S01/S02/S03 |
| 재질/명암/입체 | large light-shadow groups, matte concrete/dust, painted metal, restrained glass | S03/S04 |
| 현재키워드 | scrap merchant / arid wasteland / clear daytime | R01 |
| 과거조건/문자UI인물제외 | no rain/night/fog; no people…labels…UI; no unrequested cars/cranes/poles | R01/S02 |
| 참조역할/제외 | numbered1~7 geometry/art/world/form/surface roles, mandatory camera overrides all | reference audit |
| 보강7/비교4제한 | F-04 only optional form submitted; F-08~11 excluded entirely | reference audit |

실제 입력·도구 계약·글자 수는 references.json. 브리프/승인이력은 생성 프롬프트에 덤프하지 않는다. 이미지가 나온 뒤 actual PNG의 선쌍과 상하 대응표를 review.md에 기록한다. 구조 오류만 상시 승인 범위로 보정하며 취향 변형을 자동 추가하지 않는다.

실행 시 확인한 도구 제한: 7개 로컬 경로 호출은 생성 전 인자 검증에서 거절되어 실제 최대5개를 확인했다(tool_rejection.json). 실행 입력은 구조가이드/M03-10/M04-02/F-04/B03-01의5장으로 조정했다. M01/M02는 직접 열람·구조 설계에 반영했지만 재호출 이미지 입력에서는 제외한다. 도해 역할은 새 구조가이드와 명시적 구조 지시가 담당한다. 위7장 계획/번호는 최초 사전 계획의 이력이며 실제 입력은 tool_arguments.json이 기준이다.

현재 보정본 실제입력4장: scene_structure/M03-10/M04-02/B03-01. 기존7/5장 설명은 최초 계획과 도구 제한 대응의 이력이다. F-04는 보정입력에서 제외. 최종 검수와 중단근거는 review.md/result.json이 기준.

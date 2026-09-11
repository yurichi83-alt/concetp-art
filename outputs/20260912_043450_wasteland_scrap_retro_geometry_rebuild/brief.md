# 생성 브리프 — 고철상/낮/황무지, M04-08

마스터2.7/실행1.8. 독립 추가1장. 내장 imagegen 사용. 사용자 지정 M04-08은 이번 입력 선택이며 전역 마스터 갱신이 아니다. 기존 Salvage Cyberpunk 세계관/LDI 표현 유지.

형태: 둥근 모서리 작업장과 후방 단차가 있는 비거주 서비스 타워, 별도 계단형 레트로 아날로그 분류/배터리 설비. 직전 배럴 작업장·기어 드럼·상층 사무실/외부계단을 반복하지 않는다. 기존 결과 PNG 입력 없음.

좌측 열린 배송 틈과 우측 닫힌 상방 롤러 게이트가 각각 기능 출구. 중앙과 접근폭 확보, 건물문은 장식 입구. 설비는 비건물이며 입구/옥상 강제 없음. 건물 높이최대5.8m 계획, 공통16×16기단/일정깊이2.3 계획이며 실제2D미터검증이 아니다. 실제콜리전/메시/UV 작업 없음.

|요구사항|실행 프롬프트/계획|QA|
|---|---|---|
|고철상/낮/황무지/한장|CURRENT SCENE, dry daylight; single scene|R01|
|M04 레트로 참조|Reference5 M04-08 케이스/아날로그/모듈|W01~03|
|기존회수수리 세계관/LDI 유지|CURRENT SCENE repair/adapters; ART clean broad planes|S01~04,W01~03|
|사각 베이스·두단면·공통정사영|STRUCTURE, guide commonvectors|C01~04|
|지상 곡면/깊이·단차|rounded workshop, stepped tower, recessed bays|L05,L07,R02|
|뒤쪽2경계와2기능출구|left open delivery/right closed upward gate|L01~03|
|중앙·앞 시야 확보|flush pad, peripheral stock|L03~04|
|사람입구/옥상40~80 건물별|closed shutter/personnel door; canopy/tower/vent, tower cover|W04~05|
|재질큰면/평면붓터치/선택손상|ART intact nearby-tone broad flat patches|S01~03|
|단면장소변화/전체프레임|dry strata/powerconduits, no basement/rockburied corners|C01~03,R02|
|문자/사람/CRT제외|ART/CURRENT exclusions|R01|
|입력기록/출력검수/보정|tool_arguments/references/result/review|현재실행|

요구사항은5개 참조의 실제 역할과 연결됨. 가이드/계획의 합격으로 결과 합격을 대신하지 않는다.

보정 실행 실제입력3장: 새구조가이드/M03-10/M04-08. M01/M02는열람/설계반영후보정입력에서제외. 최초5장대응표와분리하며actualtool_arguments/references가최종입력기준. 최종검수uncertain,마스터변경없음.

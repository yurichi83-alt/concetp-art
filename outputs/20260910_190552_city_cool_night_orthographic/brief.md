# 생성 브리프

사용자 원문: 도심속 고층 건물 / 밤, 쿨 톤 / 최대 4층 최소 2층 건물 3개. 출구 한쪽은 지하 주차장 입구로. 너무 낙후화 되지 않은 도심. 도로 / 한 장

새 독립 시안 1장. 마스터2.4/실행1.5. 왼쪽4층·뒤2층·오른쪽3층, 우측 지하주차장 출구. 이번 2~4층 요청만 높이 기본6.5m 예외. 내장 이미지생성, 전역/마스터/승인/Git 수정 없음.

| 요구 | 프롬프트 대응 | 검수 |
|---|---|---|
| 공통 정투영·정사각 압출·두 단면·전체 프레임 | STRUCTURE1 | C01~C04 |
| 직교 접지·지붕·지지·중앙/두 보행부피 | STRUCTURE2 | L01,L03~L07 |
| 뒤 좌 도로·뒤 우 지하주차장 정확히2출구 | CURRENT exit2문단 | L02~L03 |
| 건물 정확히3동 지상2~4층 | CURRENT first paragraph | R01 |
| 건물별 사람 입구·옥상40~80% | CURRENT door/roof paragraphs | W04~W05 |
| 덜 낙후된 도심·밤쿨톤·도로 | CURRENT first/last paragraphs | R01,S04 |
| LDI 큰 형태/면/재질+Salvage 기능과수리 | CURRENT reuse, ART | S01~S04,W01~W03 |
| 독립 새설계·5원본 역할별 전달 | ART Input1~5, references.json | R02 |
| 보관·진짜파일열기·관찰기반검수·구조보정 | preflight.md/result.json | 실제 QA |


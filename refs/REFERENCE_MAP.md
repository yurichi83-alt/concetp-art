# Reference Map — 마스터 v2.1

원본 마스터 19장을 유지하고 승인된 Little Devil Inside 보강 5장을 더한 총 24장이다. A-01/A-02 선호 결과 2장과 검토 이력 3장은 별도이며 마스터를 대체하지 않는다.

M03-11~M03-15는 건축의 형태·재질 표현·조명과 색감 범위로만 사용한다. 구도 01·공간 02·Salvage Cyberpunk 세계관 04의 역할을 대체하지 않는다. 세계관·시대·서사·캐릭터·차량·UI·상호와 포스터 문자·카메라·공간 배치·자연물 묘사는 사용하지 않는다.

M03-12(두 번째 추가 이미지)는 건물 부분만 참고한다. 나무·풀·숲·자연 지면은 제외한다. 이는 해당 이미지의 참고 범위이며, 기존 자연물 자료의 역할이나 프로젝트 전체의 식생 허용 여부를 바꾸지 않는다.

실제 생성 입력 여부는 각 run의 `references.json`에 따로 기록한다. 마스터 등록이 매번 24장 모두를 이미지 도구에 전달한다는 뜻은 아니다. 아래 역할·제외 범위는 `refs/manifest.json`과 일치한다.

## 마스터 24장 — 원본 19장 + 승인 보강 5장

| ID | 파일 | 역할 (`use_only`) | 제외 (`exclude`) |
|---|---|---|---|
| M01-01 | [composition_cutaway.png](../refs/master01/composition_cutaway.png) | 카메라, 전체 베이스, 두께와 측면 단면만 참고 | 네온·상점가·일본풍·팔레트·고밀도 재질은 제외 |
| M02-01 | [layout_two_exits.png](../refs/master02/layout_two_exits.png) | 이동 경계, 각 뒤쪽 면의 출구, 높이 상한만 참고 | 파란 벽·글자·아이콘·화살표·입구 표시·정중앙 배치는 복사하지 않음 |
| M03-01 | [ldi_01_attic.png](../refs/master03/ldi_01_attic.png) | 큰 형태·목재 면·선택적 상세·국소 조명 | 세계관·장소·캐릭터·카메라·지붕 높이 제외 |
| M03-02 | [ldi_02_reading_room.png](../refs/master03/ldi_02_reading_room.png) | 넓은 벽면·정돈된 가구 형태·빛과 면의 관계 | 중앙 가구 배치·캐릭터·시대·창문 형태 의무화 제외 |
| M03-03 | [ldi_03_dark_corner.png](../refs/master03/ldi_03_dark_corner.png) | 어두운 면과 국소광의 대비 | 과도한 암부·구도·캐릭터·낙서 문구 제외 |
| M03-04 | [ldi_04_large_interior.png](../refs/master03/ldi_04_large_interior.png) | 광원의 집중과 덩어리 명암 | 캐릭터·몬스터·침대 중앙 배치·세계관 제외 |
| M03-05 | [ldi_05_fog_forest.png](../refs/master03/ldi_05_fog_forest.png) | 차분한 팔레트·단순화된 자연물·안개층 | 숲 테마·인물·몬스터·낮은 카메라·거대한 나무 높이 제외 |
| M03-06 | [ldi_06_night_path.png](../refs/master03/ldi_06_night_path.png) | 쿨톤 환경과 조명 영역·소재 절제 | 주인공·장비·구도·전력 상태 고정 제외 |
| M03-07 | [ldi_07_station.png](../refs/master03/ldi_07_station.png) | 큰 벽·지붕 면·재질의 생략과 부분 손상 | 역 건축·철도 테마·정면 구도·캐릭터 제외 |
| M03-08 | [ldi_08_pub_exterior.png](../refs/master03/ldi_08_pub_exterior.png) | 넓은 도장면·큰 포장석·형태로 읽히는 재질 | 펍·영국풍 건축·상호·캐릭터 제외 |
| M03-09 | [ldi_09_pub_interior.png](../refs/master03/ldi_09_pub_interior.png) | 면 중심의 가구·재질·국소적인 따뜻한 조명 | 술집 테마·중앙 가구·캐릭터·시대 제외 |
| M03-10 | [ldi_10_storefront_style_anchor.png](../refs/master03/ldi_10_storefront_style_anchor.png) | 큰 깨끗한 색면, 선택적 손상, 특징적 큰 윤곽, 디테일 집중과 여백의 대비 | 상점 종류·건축 양식·상호·캐릭터·카메라 제외 |
| M03-11 | [ldi_11_pub_clean_surfaces.png](../refs/master03/ldi_11_pub_clean_surfaces.png) | 넓은 벽 색면, 창틀·몰딩의 큰 형태, 큰 포장석의 재질과 명암 | 세계관·시대·서사·캐릭터·차량·UI·상호/포스터 문자·카메라·공간 배치 복사 제외. 자연물 묘사 제외. |
| M03-12 | [ldi_12_gas_station_building_only.png](../refs/master03/ldi_12_gas_station_building_only.png) | 건물 외벽·지붕의 큰 형태, 건축 재질과 건물에 맺힌 빛만 참고 | 세계관·시대·서사·캐릭터·차량·UI·상호/포스터 문자·카메라·공간 배치 복사 제외. 자연물 묘사 제외. 특히 나무·풀·숲·자연 지면은 참고하지 않고 건물 부분만 사용. |
| M03-13 | [ldi_13_kiosk_materials.png](../refs/master03/ldi_13_kiosk_materials.png) | 건축 외벽·창틀의 단순한 면, 도장·목재·유리의 구분, 건물 국소광 | 세계관·시대·서사·캐릭터·차량·UI·상호/포스터 문자·카메라·공간 배치 복사 제외. 자연물 묘사 제외. |
| M03-14 | [ldi_14_attic_structure_light.png](../refs/master03/ldi_14_attic_structure_light.png) | 큰 목재 구조와 판재 표현, 선택적 큰 파손, 건축 공간의 조명 구획 | 세계관·시대·서사·캐릭터·차량·UI·상호/포스터 문자·카메라·공간 배치 복사 제외. 자연물 묘사 제외. |
| M03-15 | [ldi_15_street_light_planes.png](../refs/master03/ldi_15_street_light_planes.png) | 건축의 큰 덩어리, 정돈된 바닥 재질 표현, 건축과 지면의 빛·그림자 대비 | 세계관·시대·서사·캐릭터·차량·UI·상호/포스터 문자·카메라·공간 배치 복사 제외. 자연물 묘사 제외. |
| M04-01 | [world_01_masked_scavenger.png](../refs/master04/world_01_masked_scavenger.png) | 강한 실루엣·기계와 천·개조 방식 | 사실적인 재질 밀도·인물 직접 삽입 제외 |
| M04-02 | [world_02_heavy_mechanical_arms.png](../refs/master04/world_02_heavy_mechanical_arms.png) | 큰 산업기계 덩어리·도장 패널·관절의 기능감 | 인물 직접 삽입·포토리얼 표면·동일 복장 복제 제외 |
| M04-03 | [world_03_helmet_and_coat.png](../refs/master04/world_03_helmet_and_coat.png) | 인간/기계 경계·천과 기계 대비·수리 흔적 | 실사 재질·네온 골목·인물 직접 삽입 제외 |
| M04-04 | [world_04_cloak_and_mechanical_arm.png](../refs/master04/world_04_cloak_and_mechanical_arm.png) | 천의 큰 면·금속 관절·제한된 포인트 색·노후 기술 | 붓질·선화·인물 직접 삽입·색상 고정 제외 |
| M04-05 | [world_05_rebuilt_robot.png](../refs/master04/world_05_rebuilt_robot.png) | 실루엣·노출 구조·우회 케이블·수리 문화 | 무기·캐릭터 직접 삽입·고밀도 표면·배경 제외 |
| M04-06 | [world_06_asymmetric_machine.png](../refs/master04/world_06_asymmetric_machine.png) | 비대칭 개조·기능적인 큰 기계 요소 | 그림체·전투 포즈·무기·캐릭터 직접 삽입 제외 |
| M04-07 | [world_07_repurposed_machine_head.png](../refs/master04/world_07_repurposed_machine_head.png) | 다른 부품 조합·남아 있는 제품 도장·첨단기술의 잔재 | 제품 문자·촘촘한 부품 묘사·캐릭터 직접 삽입 제외 |

M03-11~M03-15는 승인 `master_update_20260909_v2_1`에 따라 추가했으며 각 원본은 3024×1898이다. 기존 19장은 삭제하거나 교체하지 않았다.

## 선호 결과 예시 2장 — 마스터 아래의 보조 참조

| ID | 파일 | 역할 (`use_only`) | 제외 (`exclude`) |
|---|---|---|---|
| A-01 | [night_courtyard.png](../refs/current/night_courtyard.png) | 원본 마스터 기준으로 만든 결과 중 사용자가 원하는 아트에 가까운 예시. 분위기·표현 인상의 보조 참조. | 원본 마스터·Little Devil Inside 아트 방향·Salvage Cyberpunk를 대체하지 않음. 개별 크롭·밀도·치수를 영구 규칙으로 승격하지 않음. |
| A-02 | [day_alley.png](../refs/current/day_alley.png) | 원본 마스터 기준으로 만든 결과 중 사용자가 원하는 아트에 가까운 예시. 분위기·표현 인상의 보조 참조. | 원본 마스터·Little Devil Inside 아트 방향·Salvage Cyberpunk를 대체하지 않음. 개별 크롭·밀도·치수를 영구 규칙으로 승격하지 않음. |

## 검토 이력 3장 — 기본 생성 참조 제외

| ID | 파일 | 역할 (`use_only`) | 제외 (`exclude`) |
|---|---|---|---|
| R-01 | [dense_pump_station.png](../review_only/dense_pump_station.png) | 표면·부품·배치가 동시에 과밀해지는 실패 확인 | 생성의 양성 참조로 전달 금지; 스타일 미승인 |
| R-02 | [split_day_night_concept_only.png](../review_only/split_day_night_concept_only.png) | 사용자가 좋아한 컨셉 방향과 색감의 이력 보관 | 레이아웃·카메라·분할 패널·단면 누락은 미승인. 기본 생성 입력으로 전달 금지 |
| R-03 | [store_center_obstructed.png](../review_only/store_center_obstructed.png) | 중앙 장애물·출구 판독·미세 디테일 누락 검사 사례 | 어시스턴트 사후 검사 사례이며 사용자 승인 아님. 생성의 양성 참조로 전달 금지 |

상세 기준: [현재 참조와 승인 범위](../docs/10_CURRENT_REFERENCES.md). 전체 이미지: [참조 갤러리](../REFERENCE_INDEX.html).

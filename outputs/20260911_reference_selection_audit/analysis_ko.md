# 마스터3·4 실제 선택 이력 점검

최근 상위 run 폴더의 실제 전달 기록14개를 확인했다. 보정 포함이며14개의 독립 요청을 뜻하지 않는다. 중첩 variant 폴더와 과거 메타데이터 백업은 이 집계에서 제외했다. 검사/계획/생략 목록을 실제 입력으로 세지 않았다.

-14개 모두 M03-10과 M04-02 사용.
-그중1개만 M03-11을 보조로 추가. 마스터4의 다른 원본은 이14개에서0회.
-중첩된 오늘 ㄱ자 시안3종도 최초 입력은 같은3·4 조합. 정사영 편집2종은 기존 생성물/구조 가이드만 전달하므로 새로운3·4 선택 사례가 아니다.
-더 이른 기록에는 야간M03-06, 작은 상점M03-13, 파손 실내M03-14, 세계관M04-04/07 등의 사용이 있다. 역사 전체가 단일 조합이었다는 뜻은 아니지만 최근 대표쌍 편중은 명확하다.

## 원인과 설명 정정
-project.json의 기본 우선순위는 M03-10/M04-02이며, 마스터03 문서는 M03-10을 최우선 앵커로 지정한다. 보조 선택은 필요시로 되어 있다.
-이 설정은 자동으로 전체 이미지를 비교/선택하는 실행 코드가 아니다. 어시스턴트가 호출별 첨부 경로를 선택한다.
-실제 최근 실행에서는 기본 조합 재사용과 입력 축소가 우선되었고, 장면별 후보 비교와 선정 근거가 충분히 남아 있지 않다. 이전 답변은 문서에 정의된 선택 방식을 실제 일관되게 수행한 것처럼 과장했다.
-5장 한도는 일부 호출의 보조자료 생략 사유다. 최근 보정2회는3장만 사용하면서도 같은 대표쌍을 유지했으므로 한도만으로 반복을 설명할 수 없다. 기존기록의 avoid redundant inputs 같은 포괄적 이유는 후보 적합성 비교를 대체하지 못한다.
-동일 원본이 반복되어도 그 자체가 잘못인 것은 아니지만, 다른 장소에서도 반복 선택할 때에는 해당 장면에 가장 적합한 이유가 필요하다.

## 보완 방향 (미적용)
장면의 조명/재질/건축 형태/기계 기능별로 후보를 추리고 실제 열람한 후보와 선정 이유를 남긴다. 기본 대표라는 이유만으로 선택을 끝내지 않는다. 반복 사용은 금지/랜덤 교체할 대상이 아니라 장면 적합성으로 재평가할 대상이다. 검사만 한 자료와 실제 첨부한 자료를 구분한다.

마스터/설정/과거 기록 변경 없음. 이번에는 감사 문서만 작성.

| 전달 기록 | 입력 장수 | 실제 마스터3·4 |
|---|---:|---|
| [20260910_182329_scrapyard_warm_sunset](../20260910_182329_scrapyard_warm_sunset/references.json) | 4 | M03-10, M04-02 |
| [20260910_183000_scrapyard_spatial_rebuild](../20260910_183000_scrapyard_spatial_rebuild/references.json) | 4 | M03-10, M04-02 |
| [20260910_183400_scrapyard_exit_fix](../20260910_183400_scrapyard_exit_fix/references.json) | 5 | M03-10, M04-02 |
| [20260910_184527_city_three_buildings_night](../20260910_184527_city_three_buildings_night/references.json) | 4 | M03-10, M04-02 |
| [20260910_184900_city_square_base_fix](../20260910_184900_city_square_base_fix/references.json) | 5 | M03-10, M04-02 |
| [20260910_185100_city_full_framing](../20260910_185100_city_full_framing/references.json) | 5 | M03-10, M04-02 |
| [20260910_185824_city_night_new_arrangement](../20260910_185824_city_night_new_arrangement/references.json) | 4 | M03-10, M04-02 |
| [20260910_190552_city_cool_night_orthographic](../20260910_190552_city_cool_night_orthographic/references.json) | 5 | M03-10, M03-11, M04-02 |
| [20260910_191326_city_projection_rebuild](../20260910_191326_city_projection_rebuild/references.json) | 5 | M03-10, M04-02 |
| [20260911_090939_image2_vs_25_sunset](../20260911_090939_image2_vs_25_sunset/references.json) | 4 | M03-10, M04-02 |
| [20260911_093324_builtin_4k_sunset_test](../20260911_093324_builtin_4k_sunset_test/references.json) | 4 | M03-10, M04-02 |
| [20260911_101122_desert_cylinder_night](../20260911_101122_desert_cylinder_night/references.json) | 5 | M03-10, M04-02 |
| [20260911_101122_desert_cylinder_night_correction01](../20260911_101122_desert_cylinder_night_correction01/references.json) | 3 | M03-10, M04-02 |
| [20260911_101122_desert_cylinder_night_correction02](../20260911_101122_desert_cylinder_night_correction02/references.json) | 3 | M03-10, M04-02 |

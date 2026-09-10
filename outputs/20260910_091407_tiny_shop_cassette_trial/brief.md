# 카세트 퓨처리즘 — 이번 이미지 한정 테스트

- run_id: 20260910_091407_tiny_shop_cassette_trial
- request_mode: edit_existing_for_controlled_temporary_trial
- baseline_run: 20260910_084302_tiny_city_shop_rebuild
- masters: v2.1 (변경 없음)
- execution_rules: v1.2 (변경 없음)
- requested_count: 1 final deliverable
- route: built-in image_gen.imagegen
- api_explicitly_authorized: false
- master_update_authorized: false

## 사용자 요청 원문

메인 레퍼런스에 추가 할 수도 있는데 아직 추가는 하지 말고 다음 이미지를 제작 할 때만 우선 적용해서 결과물을 보고싶어. 결과물을 보고 괜찮으면 나중에 내가 승인할 때 메인 레퍼런스에 추가해줘. 키워드는 '카세트 퓨처리즘' 이야. 기계적 요소의 디자인에 카세트 퓨처리즘을 추가하고 싶어. 그러면 카세트 퓨처리즘을 추가한 상태에서 위에랑 같은 키워드로 테스트 이미지를 만들어보자. 키워드는 동일하게 도심 속 구멍가개 / 낮 / 큰 건물 들 사이에 끼어있는 작은 상점 / 한 장 그리고 기계의 비율을 지금보다 조금 만 높여줘. 지금의 기계 비율을 100 이라고 했을 때 130 정도로 높여주고, 작은 프랍 같은 거에도 기계적 요소를 첨부해 줬으면 좋겠어. 테스트 이미지 만들어줘

## 적용 범위

현재 최종 상점 결과를 비교 기준으로 삼아 구도·건물/상점 비례·두 출구·중앙 바닥·낮과 주요 재질을 보존하는 편집으로 진행한다. 카세트 퓨처리즘은 이번 기계 디자인과 작은 생활 프랍에만 적용한다. 메인 참조, 프로젝트 데이터, 승인 장부는 변경하지 않는다. 향후 명시적 승인 전에는 이번 결과나 키워드를 기본 참조로 자동 사용하지 않는다.

기계의 존재감은 기준 100→목표 130, 즉 시각적으로 약 30% 증가하는 방향이다. 픽셀 면적이나 개수의 정확한 1.3배를 측정·보장하는 뜻이 아니며 영구 수치 규칙으로 저장하지 않는다.

## Scene plan

기존 벽·지붕 설비를 두꺼운 사각 외장, 어두운 조작부, 작은 CRT형 표시창, 아날로그 계기·큰 버튼·카트리지 점검구 등으로 재설계한다. 일부 기존 모듈을 약간 확장해 전체 기계의 존재감을 적당히 높인다. 작은 재고/결제 단말기와 기계식 잠금·상태 계기가 달린 소형 보관함을 상점/외곽 벽에 밀착시킨다. 음식·모든 소품을 기계화하지 않는다. 중앙과 두 출구 접근로는 비우며 큰 건물과 작은 가게가 주인공으로 남는다.

기존 Salvage Cyberpunk의 회수·수리와 LDI의 넓은 색면·선택적 묘사를 유지한다. 새 기계 외장도 사용 이력과 교체부가 읽히게 하고 미세 버튼·스크래치·배선의 전면 증식을 피한다.

## 실제 전달 프롬프트

Use case: precise-object-edit / temporary mechanical-design study. Produce ONE edited image of input image 1, the existing DAYTIME tiny city shop squeezed between two larger perpendicular building wings. This is a controlled test of CASSETTE FUTURISM on mechanical elements only, with a modest increase in mechanical presence.

Input roles:
1. EDIT TARGET and comparison baseline. Preserve its camera, diamond-shaped whole base, two perpendicular rear building wings, exact two exits and steps, broad clear central court, the small corner shop, relative building/shop proportions, teal storefront, striped awning, closed door, provisions display, daylight, architectural palette, overall surface simplicity, and exposed front foundation/cutaway geometry.
2. M03-10: primary rendering style, large calm architectural color planes and selectively detailed 3D solids. Not its world, characters, store identities, camera or lettering.
3. M03-13: shop material/frame and small-object rendering support only, not its world, figures, vehicle, posters, words or layout.
4. M02-01 diagram: preserve the target's two genuinely perpendicular rear boundary planes, one visible unobstructed through-exit on each, and connected empty center. No diagram graphics.
5. M04-02: functional salvaged mechanical masses, repairs and visibly adapted connections translated into utility equipment. Do not depict people, humanoid machinery or photographic microtexture.

Apply the user's trial aesthetic specifically to MACHINERY and a few SMALL FUNCTIONAL PROPS: cassette futurism expressed through chunky squared-off housings with gently rounded corners; aged ivory/beige molded casing and charcoal control inserts; recessed monochrome green or amber CRT-style instrument displays; tactile rectangular buttons, rotary selectors and simple analog needle gauges; horizontal vent bands; latchable cartridge/tape-access bays; sturdy handles and a few substantial cable connections. Use these as practical industrial control and service-design features. It should evoke tangible analog/electromechanical future technology, not modern glass touchscreens, holograms, neon sci-fi or decorative cassette tapes scattered around.

Keep the existing worn Salvage Cyberpunk repair culture. Retain repaired foundations, selectively broken plaster and reused utility connections. Old technology is still maintained and functional. Show mismatched replacement casings and useful adapters, not uniformly pristine new electronics. The Cassette Futurism addition does NOT replace the existing architectural style or world.

Mechanical presence target: consider the ORIGINAL image's total perceived machinery presence as 100 and aim for approximately 130 for THIS IMAGE ONLY. This means a moderate roughly thirty-percent increase in visible mechanical emphasis, not 130 extra devices, not 130 percent more, and not doubling machinery. Accomplish it mostly by carefully enlarging or extending several existing wall/roof service modules and giving them legible cassette-era controls, plus a FEW compact daily-use props. Buildings remain the dominant masses, with plenty of quiet wall area. Do not turn every window, shelf item or paving tile into a machine.

Specific controlled changes:
- Redesign existing large wall-mounted service boxes into coherent cassette-futurist cooling/power units: substantial cream rectangular shells, dark recessed control strips, one small CRT readout on a focal unit, a simple analog gauge, broad pushbuttons and a protected tape/cartridge service bay. Keep functional joins to their existing pipes.
- Give selected rooftop supply units similar robust modular casings and service handles; modest added volume, avoiding a forest of antennas, wires or new roof towers. Keep all original roof silhouettes and height relationships readable.
- At the little shop, add a small portable inventory/payment terminal on a TINY wall-mounted or window-counter ledge, with a miniature monochrome display, tactile keypad and a tape/cartridge slot. Keep it small relative to the shop, leaving the provisions visible.
- Beside the storefront, tightly against an existing peripheral wall, add or adapt a small delivery/tool box with a chunky electromechanical latch, little analog status dial, and a cartridge-like battery/service module. It remains recognizably a compact everyday container, not a robot or large vending machine. It must not intrude on either exit approach or the open central floor.
- Refine one existing front-cutaway electrical junction box with the same robust control-panel and cartridge-access language while preserving the thickness and exposed infrastructure. Do not fill the cutaway with additional tiny parts.

Keep controls readable as FEW SIMPLE SHAPES at this viewing distance; broad silhouette and material changes carry the theme. A few selected panels may have small lit segments without readable slogans, logos or explanatory labels. Never add diagram text, arrows, floating UI or comparison panels.

Hard invariants: same elevated camera and entire base within the frame; roofs and all corners fully visible with margins; unchanged two perpendicular rear boundaries; exactly one open passage in each rear boundary; both thresholds and step routes clear; shop door closed; uninterrupted EMPTY central combat/pedestrian court; both front foundation cutaway sides visible and coherent; large buildings still enclose the tiny shop at the back corner. Do not reconstruct into a straight row, add a third opening, hide exits, increase building height or move the shop into the center.

Preserve neutral bright daytime lighting, pale blue-gray background, quiet large stylized color planes and selected wear. Distinguish molded housings, painted metal, glass, fabric and plaster without making the whole scene plastic. No additional gritty micro-rust, dense scratches, rubble, vines, posters, people, robots, cars, night, sunset, campfire or scrapyard. One final edited image, not a before/after sheet.

## Status

temporary_test_generated_and_reviewed — tiny_shop_cassette_trial.png 1장. 구조 candidate_pass, 기계 존재감 증가는 시각적 비교만 수행. 메인 반영 없음, 사용자 승인 대기.

# 고물상·식료품점 — 화면 없는 카세트 퓨처리즘 테스트

- run_id: 20260910_093245_junkdealer_grocer_cassette_no_crt
- user_request: 녹색 브라운관 같은 요소는 제외. 카세트 퓨처리즘은 유효. 고물상, 식료품 상점 / 낮, 웜톤 / 고물상 건물의 절반은 기계화, 쓰레기통, 굴뚝 / 한 장
- masters: v2.1 (변경 없음)
- execution_rules: v1.2
- request_mode: new_location_for_continued_temporary_test
- requested_final_count: 1
- route: built-in image_gen.imagegen
- api_explicitly_authorized: false
- master_update_authorized: false

## 장면 계획과 이번 변경

뒤쪽 좌측 고물상은 넓고 낮은 작업장으로, 한쪽은 낡고 수리한 건축, 다른 쪽은 건물의 벽·지붕 부피를 실제로 대신하는 큰 기계 모듈로 설계한다. '절반'은 고물상 건물의 시각적 덩어리 비중에 대한 목표이며 전체 장면의 50%가 아니다. 직전 테스트의 100→130 목표를 누적하지 않는다.

직교하는 뒤쪽 우측에는 낮은 식료품점, 작은 차양과 벽면 진열창을 둔다. 서로 다른 후면 경계에 출구 하나씩, 중앙과 접근로는 비운다. 쓰레기통은 외곽 벽에 붙이고 작은 구동부·페달/잠금 장치만 부여한다. 고물상 기계화 구획에 낮은 굴뚝을 연결한다. 새 단면은 고물상 장치의 기초·공급과 식료품점 냉각·배수 기능으로 구성한다.

카세트 퓨처리즘은 두꺼운 사각 외장, 물리 버튼, 회전 다이얼, 흰색 바탕 바늘 계기, 카트리지 점검구·손잡이·넓은 통풍구로 표현한다. 녹색 브라운관을 다른 색 브라운관으로 바꾸지 않고 화면/모니터 요소를 제외한다. 큰 색면과 선택적인 손상, Salvage Cyberpunk의 회수·수리는 계속 적용한다.

사용자의 새 테스트 요청으로만 제작한다. 메인 문서·참조·프로젝트 데이터·승인 장부를 갱신하지 않는다.

## 실제 도구 전달 프롬프트

Use case: stylized-concept. Create ONE new game-environment concept image: a JUNK DEALER / RECLAMATION SHOP and a GROCERY STORE sharing an open urban court, in WARM DAYLIGHT. Roughly HALF of the junk-dealer building is physically mechanized. Include trash bins and a chimney. This is a new location, not an edit or copy of the previous tiny corner grocery scene.

Temporary mechanical aesthetic: CASSETTE FUTURISM remains active, but REMOVE the green CRT/monitor motif. There must be NO CRTs, televisions, video screens, computer screens, glowing green displays or substitute amber CRT displays anywhere. Convey the analog future through thick ivory/beige square housings with softly rounded corners, dark recessed physical controls, large tactile rectangular buttons, rotary selectors, simple white-faced needle gauges, latchable cassette/cartridge access doors, broad ventilation bands and sturdy handles. All control panels are physical, not screen interfaces.

Use the supplied references according to role:
1. Spatial diagram: two genuinely PERPENDICULAR rear boundary planes forming a V in the image, one open exit in EACH, and a broad connected empty center. No diagram colors, arrows, labels or icons.
2. Little Devil Inside main architectural style: large calm color planes, simplified but solid forms, readable thickness, sparse large repair/wear patches. Exclude its world, characters, actual shops, words and camera.
3. Small storefront material support: frames, broad painted surfaces, glass/wood/metal distinction and restrained shop-scale details ONLY. Exclude its characters, vehicle, world, posters, letters, camera and natural elements.
4. Whole-base three-quarter diorama and front cutaways ONLY. Exclude its miniature-photography surface density, neon, specific buildings and street.
5. Translate substantial salvaged actuator housings, joints, adapted repair plates and functional connections into the mechanized building. No figure, limbs, humanoid robot or photoreal microtexture.

New site design:
Along the back-left boundary, put a LOW, BROAD junk-dealer workshop. Design it as a hybrid building whose visible mass is roughly one-half conventional repaired architecture and one-half integrated heavy machine. One section is worn plaster/masonry with a modest closed rolling shutter and small parts display window. The adjacent section REPLACES a substantial portion of wall and roof volume with a chunky cassette-futurist reclamation/pressing module: large stacked mechanical casing masses, a recessed material receiving chamber contained within the edge bay, thick actuator supports, a few clear joints and a broad physical control bank with analog gauges. It must read as an architectural half-building/half-machine, not a normal intact building with a few little boxes stuck on. Both sections share foundations and connect structurally. The intended half proportion is a visual design target for THIS junk building, not fifty percent of the entire scene.
A single modest chimney rises from the workshop/mechanized section, with a substantial flue connection and simple capped top. Keep the chimney and apparatus low enough that the visible blocking structures are planned within roughly 6.5m. It must not hide an exit or extend out of the frame.

Along the PERPENDICULAR back-right boundary, place a smaller grocery building with a DIFFERENT architectural mass: low simple sloping/canopy roof, restrained warm ochre/cream walls, muted fabric awning and a clear glazed provisions window with a few grouped produce baskets, jars and cartons. Keep goods tucked inside or along the wall. The grocery's own door is visibly closed. Its refrigeration/service equipment has compact cassette-futurist casings and physical controls, with absolutely no screen.

Make the two buildings enclose the back sides of the shared court and connect the rear corner without an extra walk-through gap. ONE clear open through-passage is in the outer portion of the back-left boundary, and ONE in the outer portion of the back-right boundary. Both passage thresholds and ground beyond are easy to see and connected to the empty central court. The two passages face into the court from different directions. All other ground-level openings are closed doors, glazed shop windows or a machinery chamber with a visible solid floor/back wall; none should look like a third exit. Keep workshop machines, receiving chamber, delivery supplies and grocery displays outside both exit approach routes.

Put a pair of recognizable trash bins against a peripheral wall: one robust lidded refuse bin with a small salvaged lid actuator/foot pedal and mechanical latch; one simple companion bin. Retain their everyday container purpose. No robot face, arms or legs, and no monitor. A few substantial reclaimed shells/parts can be stored in the junk-dealer edge bay, but do not turn the center into a scrap pile. Small shop props may have cassette-like battery/service compartments or mechanical latches; do not mechanize the food.

Spatial presentation: a square rectangular standalone base seen from an elevated three-quarter camera as a diamond. The two rear building directions must form an unmistakable right-angle plan, not a row of two front facades. Both camera-facing sides are open cut edges. Keep a generous connected EMPTY central pedestrian/combat/work area. Show the WHOLE base, all four corners, all roofs and chimney tip with comfortable surrounding margin. No high foreground walls.

Expose thick SIMPLE earth/foundation cross-sections on BOTH front faces. Design new location-specific infrastructure: deep support foundations and a compact power/hydraulic conduit under the mechanized junk shop; a small cold-storage supply/drain connection beneath the grocery. Use a few big legible mechanical shapes. No underground pedestrian passages or repeated decorative pipe patterns. Align ground slabs, footings, thresholds and machine supports coherently.

World and rendering: Salvage Cyberpunk as a repaired old working neighborhood, expressed with Little Devil Inside-inspired architectural/material simplification. Large repair plates, selected missing plaster and repurposed casing connections explain aging; keep broad quiet surfaces between them. Cassette futurism changes the equipment design, not the world or architectural rendering style. Distinguish aged molded casings, painted metal, masonry, cloth and wood with large planes, not all-over rust/scratch/gravel noise. No photographic miniature finish, dense micro-parts, painterly brush strokes, thick outlines or plastic toy environment.

Lighting: warm-toned DAYLIGHT, soft golden-cream sun and warm bounce on walls and ground, readable restrained cooler shadows. It is daytime, not orange sunset or night. Simple pale warm atmospheric background. All exits, central floor, mechanical integration, bins, chimney and both cutaways remain readable. No people, robots, cars, campfire barrels, overgrown vines, poster collage, fog, smoke curtain, neon, CRTs/screens, labels, arrows, logos, watermarks or split panels. Exactly ONE complete image.

## Status

needs_framing_revision — actual candidate saved; both lateral edges cropped (C01). Follow-up: 20260910_093731_junkdealer_grocer_framing_fix.

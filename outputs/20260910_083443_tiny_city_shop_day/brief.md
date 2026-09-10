# 도심 속 작은 구멍가게 / 낮

- run_id: 20260910_083443_tiny_city_shop_day
- request_original: 도심 속 구멍가개 / 낮 / 큰 건물 들 사이에 끼어있는 작은 상점 / 한 장
- interpretation: 문맥상 '구멍가게', 큰 도시 건물 사이의 작은 생활잡화 상점으로 해석
- masters: v2.1
- execution_rules: v1.2
- request_mode: new_location
- requested_count: 1 final deliverable
- route: built-in image_gen.imagegen
- api_explicitly_authorized: false
- scene_only_assumptions: 맑은 낮, 작은 생활잡화점, 주변은 상대적으로 큰 2층 규모 도시 매스. 기존 높이 계획 조건 내에서 크기 대비를 표현.

## Scene plan

큰 건물 두 매스의 안쪽 끝 사이에 작은 단층 상점이 물리적으로 끼어 있도록 뒤쪽 경계에 배치한다. 상점의 지붕과 양쪽 큰 건물의 지붕까지 프레임 내에 보인다. 두 출구는 상점과 겹치지 않는 뒤쪽 좌우 외측에 하나씩 두며, 상점의 유리문은 닫혀 있고 진열창에는 단단한 하부 구조를 두어 세 번째 통로로 읽히지 않게 한다.

중앙과 출구 접근로는 비운다. 상품은 진열창 안쪽과 벽면에 국소 배치한다. 낡은 건물을 큰 보수판과 재사용 기계 지지부로 수리하고 상점 냉각·공급 장치의 교체 외장과 연결부로 Salvage Cyberpunk 생활 기술을 표현한다. 넓고 정돈된 색면과 선택적 큰 손상에 집중한다.

새로운 단면은 큰 건물의 기초, 작은 상점으로 이어지는 공급 접속함·도관, 짧은 배수 연결로 설계한다. 밤·고철·드럼통 불·넝쿨·벽보 같은 이전 장면 키워드는 계승하지 않는다.

## Reference roles

M03-10 대표 표현 → M03-13 상점 재질·창틀 → M02-01 공간 → M01-01 전체 구도·단면 → M04-02 기능적 회수 기술. 표현 기준을 강조하기 위해 입력 순서를 조정했으며 마스터 자체의 변경은 없다.

## Compiled generation prompt

Use case: stylized-concept. Make ONE game environment concept image: a tiny neighborhood provisions shop squeezed into a narrow infill gap between much larger city buildings, in DAYLIGHT. The contrast between the tiny independent shop and the two bulky neighboring buildings is the subject. Design a new place, not a reskin of the earlier scrapyard or slum alley.

Reference roles, explicitly separated:
Image 1 is the PRIMARY style master: Little Devil Inside architectural forms, large calm painted color planes, solid readable thickness, simplified material depiction and selective large wear. Image 2 supplements the small shop's framing, broad painted surfaces, wood/glass material separation and a small window counter. These two images govern visual detail density across the ENTIRE render. Do not borrow their world, specific shop identity, characters, vehicles, writing, camera, UI or vegetation.
Image 3 governs ONLY spatial connectivity: exactly two rear boundary exits and a clear central floor. Do not reproduce diagram colors, arrows, text or symbols.
Image 4 governs ONLY elevated three-quarter view, whole rectangular isolated base and two camera-facing cutaway sides. Its photographic miniature finish, surface density, neon, Japanese shops and street design are NOT the rendering style.
Image 5 supplies ONLY the design language of large salvaged actuator housings, repair plates and functional mechanical connections, translated into architectural and shop utilities. Do not include its person, arms, armor or photographic textures.

Scene design: at the back of a compact urban pedestrian space, a VERY SMALL single-story general shop is physically wedged between the inner ends of two much broader and taller city building masses. The neighboring buildings nearly touch its side walls and rise distinctly above its modest roof, making it unmistakably an infill shop, not a freestanding market stall. Show the entire small shop clearly between them. One neighboring building has a broad restrained plaster facade and stacked window frames; the other has deeper concrete structural bays and repaired service panels. Keep them asymmetrical in width, roof shape and facade rhythm. Express their size RELATIVE to the low tiny shop: use modest two-story urban blocks within the established roughly 6.5m visible-height planning envelope. Show roof tops; do not crop tall buildings out of frame.

The little shop is nestled along the REAR perimeter, never standing in the empty central floor. Give it a short faded muted-teal painted facade, a modest patched fabric awning, a wood-framed glazed display window, and a narrow closed glass door. Behind the window, a few simple grouped cans, cartons and household supplies identify a neighborhood provisions shop. Keep the window sill/counter solid and the door visibly CLOSED so the storefront cannot be mistaken for a third through-exit. Display items stay inside or tightly against the storefront, not on center-floor racks. A small subdued sign panel may be plain or have abstract shapes; no readable brand, slogan, poster collage or giant signage.

The world is Salvage Cyberpunk: old city architecture remains in use through repair and repurposed advanced technology. Show a few large missing-finish areas repaired with differently sized material panels, and a visibly adapted mechanical support at an old building joint. Integrate a compact reclaimed cooling/power unit into the shop's side facade with a rounded replaced shell, an adapter collar, a modest control panel and two substantial connections feeding the shop. Another chunky rerouted utility line patches the neighboring building's old service path. The shop feels maintained and lived-in, while its surrounding infrastructure is aged and adapted. These devices serve the buildings; no giant display machine or humanoid robot.

Mandatory spatial structure: exactly two adjoining rear boundaries formed by the neighboring building masses and their connected walls. Provide ONE clearly visible OPEN through-passage in the rear-left boundary and ONE in the rear-right boundary, offset toward the outer portions so neither is behind the small shop. Both thresholds and ground continuing beyond them must be visible and accessible from the center. All other doors are closed and all unintended gaps are closed. Keep the central pedestrian/combat floor broad, connected and unobstructed, with both exit approaches clear. No cars, kiosk, tables, crates, large props or posts in the center.

Composition: ONE freestanding rectangular diorama, high three-quarter view, with every base corner, both front cut faces and all roof lines comfortably inside the image. Leave a calm margin around the whole silhouette. Both camera-facing sides are cut edges with no high foreground wall. Show thick, SIMPLE earth and foundation masses under large paved ground planes. Design a new shop-specific substructure: distinct footings beneath the two larger buildings and a shallow service conduit with a small power junction feeding the infill shop, plus a short drain connection on the other front cut face. Make these legible infrastructure cutaways, not underground walking tunnels or repeated ornamental pipe networks. Foundations, thresholds and ground planes must align.

Daylight: clear neutral-to-gently-warm daytime sun, broad readable shadows, soft cool skylight in the passageways, slightly warmer reflected light beneath the shop awning. Bright enough to see both exits, storefront, building grounding and subsurface forms. Not sunset, night, rain or fog. Use a restrained pale blue-gray atmospheric backdrop without additional city towers or surrounding terrain.

Style is essential: look like a sophisticated selectively detailed stylized 3D GAME environment in images 1 and 2, NOT photoreal miniature photography. Plaster, pavement and painted metal keep broad nearly uninterrupted color fields; wear is shown by selected LARGE broken areas and repair plates with quiet surfaces between them. Distinct solid silhouettes, thickness, joins and material planes are more important than granular texture. Avoid all-over mottled grunge, tiny rust dots, dense scratches, scattered rubble, stippled concrete and gritty soil. No generic toy plastic, extreme low-poly facets, painterly brush strokes or thick outlines. Do not inherit the previous scene's scrapyard equipment, scrap piles, fire barrels, vines, posters or sunset palette. No characters, UI, arrows, watermarks, split panels or labels. One finished image, roughly 4:3, whole-base framing first.

## Status

needs_structural_revision — 첫 결과를 tiny_city_shop_day_candidate.png로 보존. L01/L02 배치 수정 기록은 review.md, 후속 run은 20260910_083909_tiny_city_shop_layout_fix.

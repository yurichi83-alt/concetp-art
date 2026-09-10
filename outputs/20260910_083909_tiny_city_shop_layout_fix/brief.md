# 구조 보정 — 도심 속 작은 구멍가게

- run_id: 20260910_083909_tiny_city_shop_layout_fix
- previous_run: 20260910_083443_tiny_city_shop_day
- request_original: 도심 속 구멍가개 / 낮 / 큰 건물 들 사이에 끼어있는 작은 상점 / 한 장
- request_mode: edit_existing_with_layout_reconstruction
- masters: v2.1
- execution_rules: v1.2
- requested_final_count: 1
- authorization: structural_auto_correction_20260909
- backend: built-in image_gen.imagegen
- api_explicitly_authorized: false

## 구조 변경과 보존

뒤쪽 직교 두 경계를 이루는 L자 건축으로 재배치하고 각 면에 출구 하나씩 둔다. 작은 가게는 큰 건물 두 날개의 끝 사이 뒤쪽 코너에 끼워 넣는다. 중앙에 더 넓고 연결된 빈 바닥과 전체 베이스 주변 여백을 확보한다. 낮·가게의 크기 대비·청록색 외장·차양·진열창·닫힌 문·절제된 재질 표현은 유지한다. 구조 오류가 있는 기존 건물열은 보존하지 않는다.

## 실제 도구 전달 프롬프트

Use case: precise-object-edit / structural reconstruction. Produce ONE corrected finished image of the supplied tiny city shop scene.

Image 1 is the EDIT TARGET: preserve its daytime lighting, restrained clean stylized 3D materials, muted-teal tiny shop, striped cloth awning, glazed provisions display, closed shop door, and the relative size contrast with the two much bigger city buildings. Preserve the general architectural identity and useful repaired cooling/power devices. However, REBUILD THE SITE LAYOUT AND CAMERA. The current almost straight storefront row with two passages in that row is the structural error. Do not keep that row geometry and merely change the lighting or crop.

Image 2 is the non-negotiable spatial diagram: make the two rear boundaries genuinely PERPENDICULAR in plan, meeting at a far rear corner, with exactly one visible walk-through exit in EACH of those different boundary planes. Exclude diagram colors, text, arrows and icons.
Image 3 is a reference ONLY for a whole three-quarter diorama with the two rear sides receding toward a common far corner and two camera-facing cutaway sides. Do not copy its neon, stores, layout props or photographic surface detail.
Image 4 governs rendering: Little Devil Inside large calm architectural color planes, readable solid thickness and selected large wear. Do not copy characters, shops, lettering or its world.
Image 5 supplies functional repaired/reclaimed technology form language for the existing utility devices, not people/limbs or photoreal textures.

Required reconstruction, seen in a clear elevated three-quarter view:
- Use a roughly square rectangular base seen as a diamond in perspective, with a far BACK CORNER and a near FRONT CORNER both easy to understand.
- Place the large plaster building along the BACK-LEFT boundary, its inside-facing facade angled toward the open central floor.
- Place the other large concrete building along the BACK-RIGHT boundary, rotated roughly 90 degrees in ground plan relative to the first. Their inside facades must form an unmistakable L around the floor; they must NOT read as one straight row.
- Set the tiny single-story general shop into the narrow shared corner gap BETWEEN the inner ends of these taller buildings, at the FAR BACK CORNER of the site. Its left and right sidewalls are closely squeezed by the two larger neighbors. Its small facade may angle toward the camera across the corner so its awning and provisions window remain clearly visible. It is attached to the rear perimeter, never an island in the middle.
- Cut ONE open through-passage in the outer half of the BACK-LEFT boundary and ONE in the outer half of the BACK-RIGHT boundary. They face into the central court from visibly different angles. Both openings and thresholds are fully visible, unobstructed, and connected to the open central floor. Do not hide either behind building corners, the shop, a roof, or a machine.
- All other ground-level doors, including the shop door, are visibly closed. The small display window has a solid sill and cannot read as a third exit. Close all incidental boundary gaps.
- Leave a reasonably broad, connected CENTRAL pedestrian/combat court between the two rear wings and the two open camera-facing edges. No props or shop mass in that central clear area. Ground perspective, thresholds, foundations and stairs must be coherent.
- Keep all buildings modestly two-story relative to the very low shop, within the existing approximately 6.5m visible-height planning limit, and show their complete roof silhouettes.
- Frame the entire base and every roof with clear surrounding margin, especially BELOW the front corner. Do not crop the thick base or switch to an eye-level streetscape.
- Expose earth, foundation masses and a few chunky power/drain service connections along BOTH front-facing cutaway sides. Connect the small shop services meaningfully without repeating the exact original pipe routing. No underground walk-through entrances. No high front walls.

This remains a bright DAYTIME urban infill shop in the Salvage Cyberpunk setting. Keep large selectively repaired plaster/concrete areas, a modest reclaimed cooling/power unit with distinct replacement housing and functional connections to the shop. Keep the successful quiet surface density and soft neutral daylight from image 1; no additional all-over grime, rust speckles or micro-cracks. Maintain broad stylized material planes instead of photographic miniature detail.

No scrapyard equipment, fire barrels, scrap piles, vines, poster collage, people, robots, sunset, night, fog, UI, arrows, labels, watermarks or split panels. Deliver a SINGLE reconstructed image, roughly 4:3, with unmistakable perpendicular rear boundary wings and exactly one clear exit in each.

## Status

needs_structural_revision — 건물열이 유지되어 L01/L02 미해결. 원본과 검수 기록 보존. 다음 시도는 20260910_084302_tiny_city_shop_rebuild.

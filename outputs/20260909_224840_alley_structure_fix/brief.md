# 낮 골목 구조 보정 — 1차

## 사용자 요청

앞으로는 구조적으로 문제가 있을 때는 알아서 수정해서 재생성까지 해줘. 지금처럼 출구의 위치나 갯수가 틀리거나 이번에 생성한 건물들의 구조? 아니면 배치 각도 때문인지 지면 공간이 조금 이상하거든 우선 구초레 맞게 수정진행해줘.

## 구조 원인과 수정

- 편집 대상: ../20260909_223829_day_narrow_salvage_alley/day_narrow_salvage_alley.png
- 원인: 서로 마주보는 두 건물 사이에서 뒤 중앙 통로 하나로 이어지는 배치. 마스터 02의 인접한 뒤쪽 두 면/면마다 출구 하나 구조와 다름.
- 바닥의 실제 비평면 여부는 이미지로 확정 불가. 건물/골목 축과 베이스 축이 달라 지면이 비스듬히 쐐기처럼 읽힘.
- 변경: 두 건물을 뒤쪽 두 베이스 변에 맞춰 회전/재배치, 뒤 모서리 틈 폐쇄, 좌측/우측 뒤 경계 각각 출구 하나. 바닥/문턱/건물 발자국을 동일 평면과 두 축에 정렬.
- 유지: 낮, 좁은 도심 공간, 폐건물·쓰레기통·바닥의 종이/납작한 상자, Salvage Cyberpunk, Little Devil Inside 건축 표현, 전체 베이스와 전면 두 단면.
- 최종 목표 한 장. 실제 구조 오류가 남으면 사용자 상시 승인에 따라 추가 보정 가능.
- 실행 규칙 v1.1 승인 기록: structural_auto_correction_20260909. 아트 마스터/원본 이미지 승인과는 별개.

## 실제 생성 지시

Use case: precise-object-edit. Make ONE corrected version of input image 1.

This is a STRUCTURAL REBUILD of the same daytime abandoned inner-city Salvage Cyberpunk alley. Preserve its worn building materials, reclaimed mechanical support, patched canopies, waste bins, loose paper/cardboard, restrained daylight palette and thick foundation. CHANGE the building placement, ground alignment and exits. The existing layout in image 1 is WRONG and must not be preserved.

REFERENCE PRIORITY:
Image 2 is the mandatory new spatial layout. It shows two ADJACENT rear walls meeting in a CLOSED CORNER, with a separate open exit through each wall. Use only this topology, not its diagram colors, labels or symbols.
Image 3 guides the full standalone quarter-view base and two exposed cutaway sides only; exclude its neon, signage, shop theme and photographic miniature detail.
Images 4 and 5 guide restrained Little Devil Inside architectural rendering and quiet broad surfaces only; no characters, plants, story, text or copied storefronts.
Image 1 supplies the existing asset/design vocabulary, not spatial arrangement.

REBUILD IN THIS ORDER:
1. Use one compact rectangular ground slab in an elevated isometric/quarter-view camera. Its footprint has one rear corner at the top, a left corner, a right corner and a front corner below. Both camera-facing foundation sides are fully exposed.
2. REPOSITION AND ROTATE the buildings so their principal facades occupy the two BACK EDGES of this slab and meet at the top/rear corner at a right angle in plan. One row runs from the rear corner toward the left corner; the other from the rear corner toward the right corner. Both facades face the open foreground. They must NOT be two parallel buildings facing each other down a long alley.
3. Completely CLOSE the previous central rear gap with a solid joined building corner. No opening at that corner and no overhead pipe bridging a central exit. Use a continuous joined wall/body there.
4. Create exactly TWO clear open passageways through the rear building boundary: one in the left-facing rear facade around the middle of that wall, and one in the right-facing rear facade around the middle of that wall. Each opening has its complete lintel, two side jambs, a visible flat threshold, and daylight visible THROUGH a short passage to the outside. Both openings must be unambiguously walk-through exits seen from the camera; no doors, gates, stairs or bins obstructing them. They are separated by the SOLID REAR CORNER. All other doors/shutters are closed; raised boarded windows are not extra exits.
5. Rebuild the exposed ground as ONE level, continuous paved plane. Tile seams follow the SAME two projected axes as the rectangular base and building footprints. Every wall foot and foundation meets that plane coherently. No rotated central strip, funnel-shaped wedge, overlapping curbs, warped tiles, raised island, floating building or unexplained change of floor height. The center connects at the same floor level to both exit thresholds.
6. Keep the base compact, a small confined service-alley corner rather than a large plaza. Leave the modest central movement/combat area free of bulky objects, with clear paths to BOTH exits. Keep low scattered litter on parts of the floor, and bins/bags/large discarded pieces only against walls away from the passage openings.

Keep the existing abandoned, repaired and scavenged condition: broad broken-plaster areas, boarded windows, mismatched reused repair panels, worn advanced mechanical equipment actually supporting a canopy or serving utilities, patched cloth and old bins. Reposition or shorten these as needed to fit the CORRECT structure. Use selective large wear and broad quiet surfaces; reduce fine scattered texture noise while retaining coherent edges and material differences. Salvage Cyberpunk world, Little Devil Inside architectural rendering, neutral daytime illumination and readable soft shadows. No new shop theme, no characters, vehicles, greenery, neon or extra decorative machines.

FRAME: One complete standalone diorama centered on a neutral grey background. Pull the camera back to leave visible generous margin around every wall end, roof, passage frame, entire base and bottom corner. Expose thick earth/masonry and a few large pipes on BOTH front-facing foundation sides. Compact low roofs without towers; retain the planned roughly 6.5m visible-boundary limit. No labels, numbers, arrows, text, diagram graphics, multiple panels or cropped structures.

The final silhouette and ground organization must follow image 2: TWO joined rear boundaries, a SOLID back corner, TWO separate visible openings through different rear faces, and ONE coherent empty ground plane in front.

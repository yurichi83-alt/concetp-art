# 표면 정리 편집 브리프

- run: 20260909_215624_shopping_street_clean_surfaces
- 요청 범위: 직전 상점가 이미지 수정 1장. 자동 재생성 없음.
- 사용자 핵심: 새 5장 모두 Little Devil Inside. 2번은 건물만, 자연물 제외. 벽·바닥을 깔끔하게. 향후 3면도 및 AI 모델링에 사용할 형태/재질 가독성 고려.
- 이전 분석의 수정 제안 반영: 잔손상·균일한 얼룩·작은 반사 제거, 넓은 색면, 단순한 포장, 소수의 기능성 설비, 큰 명암 구획.
- 유지: 시가지 상점가, 차가운 밤, 쓰레기통/소량 쓰레기, 전봇대, 기존 구도/건물, 두 출구, 중앙 비움, 양면 단면, Salvage Cyberpunk.
- 이번 결과는 3면도/텍스처 맵/메시가 아닌 컨셉 이미지. 아직 3면 일치나 AI 모델링 품질 검증 없음.
- 기존 마스터: 01~04 v2 유지. 새 자료는 이 run에만 보존/사용하며 refs와 승인 마스터에 추가하지 않음.
- 실제 입력: 편집 대상 1장 + 사용자 LDI 자료 1~4번 4장. 5번은 열람한 명암/형태 지침만 텍스트로 반영. 구도는 편집 대상에 고정하므로 기존 M01/M02 도해를 중복 첨부하지 않음. 원본 마스터 역할/manifest/승인 상태 확인.
- 내장 image_gen. 별도 API/추가 설치 없음.

## 실제 도구 입력 지시

Use case: style-transfer / precise environment edit.
Output exactly ONE revised image of image 1, same single scene, landscape 3:2.

IMAGE ROLES:
Image 1 is the EDIT TARGET: the recently generated cold-night shopping street diorama. Preserve its overall geometry/layout and camera. Its dirty surface texture and wet highlights are the parts to REPLACE, not a style reference.
Images 2–5 are ALL Little Devil Inside screenshots supplied by the user as the desired ART rendering guidance, not world-setting references.
Image 2 (pink pub wall / green shop trim): strongest reference for CLEAN broad wall surfaces, large quiet paving shapes, crisp architectural trim, restrained mapped surface detail.
Image 3 (gas-station building amid forest): use ONLY the BUILDING, its painted siding and broad architectural shapes. EXCLUDE ALL TREES, GRASS, foliage, vegetation, soil detail and other nature; do not copy their photoreal density.
Image 4 (blue-green kiosk close view): use clean painted trim, coherent thickness and broad material color planes.
Image 5 (damaged attic interior): use large simple boards/beams and sparse large-shaped damage, concentrated light with clear quiet surfaces. Do not copy interior arrangement.
Use large clean building/pavement planes, readable silhouettes and organized large-scale lighting. Exclude people, signs/text, UI, setting/lore from ALL references.

PRIMARY CHANGE — MAKE THE WALLS AND PAVEMENT VISIBLY CLEAN AND TIDY LIKE THE LDI REFERENCES:
Substantially re-render the surface treatment of image 1. Broad intact painted wall areas dominate each facade. Remove the pervasive small paint chips, peeling flecks, dirt mottling, rust speckle, gritty granular texture, scratch fields and cracked-surface patterns across walls, pillars and cutaway.
Keep a small number of deliberate large patches or repaired panels, crisp joints, material boundaries, window recesses and wall thickness. Age is expressed through a few meaningful repairs and slightly irregular forms. Most wall surfaces should read as smooth, quiet base-color planes with gentle large-scale shading.
Replace the shiny distressed plaza with DRY, mostly matte paving: large simple slabs, clearly legible thin joints, very few isolated chips, subtle broad tile-color variation. REMOVE the fragmented orange/blue wet reflections and puddle pattern entirely. The center is a large clean quiet floor.
Keep sharp modeled geometry and full image clarity. No blur, denoising smear, softened edges, loss of resolution, featureless plastic, toy gloss, painterly strokes, cel outlines or aggressive low-poly facets.
Make the distinction between painted plaster, painted metal, fabric awnings, glass and pavement readable through coherent shape, base colors and restrained material response. Glass can retain limited reflection; keep the ground dry.

SECONDARY CLEANUP:
Preserve the recognizable principal roof units, but consolidate accessory clutter into a few legible equipment masses. Remove redundant little fittings and tightly repeated seam/bolt detail. Keep readable thick pipes with clear connections, repaired panels and functional utility hardware.
Keep the two existing peripheral utility poles and their main cable route. Keep rubbish bins and only a modest small cluster of tied bags/cartons beside them; remove scattered litter outside those groups.
Clean up the exposed base into broad earth/foundation masses and a few clearly formed pipes. Retain two exposed cutaway faces, no underground tunnel.

LIGHT AND COLOR:
Remain unmistakably NIGHT, in a cold desaturated blue-gray tone. Use broad cool ambient illumination that makes wall/paving planes, openings and material boundaries easy to read. Keep a few restrained warm window accents, reduce repeated hot orange wall lamps and competing bright pools. Shadows reveal geometry with clear direction; no dirty-looking excessive dark crevice outlines, crushed-black structures or photographic micro-bump highlights. Enough fill on both cutaway sides and both exits. Large muted local colors remain visible in walls and awnings.

LOCK THESE INVARIANTS:
Same single standalone quarter-view diorama, same main building arrangement and storefront positions, same broad empty center. EXACTLY TWO visible accessible rear exits, one in each rear boundary, both clear. Closed other shop doors/shutters. Same thick base footprint and BOTH front-facing ground sections. Keep all base corners, poles and roof extremities fully inside the frame, with surrounding margin. No central props or new obstructions. Salvage Cyberpunk world remains, conveyed by repaired/reused functional technology, not by blanket grime.
Purpose: a clean concept reference to support LATER orthographic three-view design and AI-assisted modeling. Prioritize unambiguous forms, consistent proportions, crisp object separation and clear surface color regions. For THIS request produce only this one quarter-view scene, no turnaround, no triptych, no texture sheet, no dimensions, no labeling or text, no people or animals.

The change must be obvious at first glance: much cleaner walls and dry quiet flooring with the same coherent setting and spatial design.

## 실행 결과
내장 도구로 편집 이미지 1장 생성, 저장 후 실제 열람 검수. 참조 6장 입력 검증 오류 1회는 생성 전에 거절됐으며 5장으로 조정. 실제 생성 1회만 수행.

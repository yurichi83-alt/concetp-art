# 폐철물점·가전제품 판매장 / 밤

- run_id: 20260910_094940_ruined_hardware_appliance_night
- user_request: 폐건물, 가전제품 판매장 / 밤 / 폐건물은 철물점이고, 벽이 뚫려있어서 안쪽이 보임. 뚫린 벽 아래에는 벽의 파편도 떨어져 있음. 가전제품 판매장의 1/3 은 기계화 해주고 폐건물 보다 1.3배 정도 높은 건물. 가전제품 판매장 옥상에는 태양광 패널과 발전기 같은 요소가 있음 / 한 장
- master_version: 2.1
- execution_rules: 1.2
- request_mode: new_location
- route: built-in image_gen.imagegen
- requested_final_count: 1
- status: completed_candidate_pass — 실제 결과 저장/검수 완료. 1회 생성으로 최종 1장. 높이비/기계 분율은 정량 미검증. 사용자/마스터 승인 없음.

## 장면 계획

폐철물점은 낮은 노후 벽돌/목재 건물로, 앞 벽의 큰 불규칙 파손부에서 선반·공구와 막힌 내부 뒷벽이 보인다. 파편은 구멍 바로 아래 외곽에 집중한다. 구멍이 추가 통과 출구로 읽히지 않게 낮은 파손 벽체와 뒷벽을 남기며, 두 정상 출구는 뒤쪽 직교 경계에 별도로 둔다.

가전제품점은 같은 지면에서 폐철물점보다 약 1.3배 높게 계획한다(예: 3.8m 대 4.9m 지붕선). 약 1/3의 건물 구획은 전력·재생정비 기계와 제품 외장을 통합하고, 나머지는 냉장고·세탁기 등이 보이는 판매장이다. 옥상 태양광 패널은 밤에 빛을 내지 않으며, 소형 발전기/배터리와 연결한다. 치수와 분수는 시각적 설계 목표이고 픽셀로 정량 검증하지 않는다.

이전 건물/단면을 재사용하지 않는다. 폐점의 낡은 기초·막힌 공급관과 판매장의 배터리/전력 모듈을 구분한다. 화면 없는 카세트 퓨처리즘은 이어지는 테스트 범위로만 적용한다. 메인 참조/승인장부 갱신 없음.

## 실제 도구 전달 프롬프트

Use case: stylized-concept.
Asset: ONE standalone game-environment concept diorama.
Scene: an ABANDONED HARDWARE STORE with a large broken exterior wall, beside an operating APPLIANCE RETAIL SHOP, at NIGHT. Entirely new building designs and infrastructure for this location. The appliance building is approximately 1.3 times the height of the ruined hardware building, and approximately ONE THIRD of the appliance building is integrated machinery. Its rooftop contains recognizable SOLAR PANELS and a compact GENERATOR.

Reference roles, in actual input order:
1: spatial diagram ONLY: two perpendicular rear boundary planes, exactly one open exit on each, broad open central floor. Do not render diagram blue, arrows, symbols or text.
2: PRIMARY Little Devil Inside architectural rendering: broad calm color planes, distinctive solid masses, selective large damage, readable thickness, restrained surface texture. Exclude its actual shops, world, people, lettering and camera.
3: supporting architectural timber structure, large selected broken shapes and localized lighting only. Exclude character, furniture, scene layout, UI, story, setting and letters.
4: full-base elevated quarter-view composition and both front cutaway sides ONLY. Exclude its buildings, neon, Japanese street, dense miniature texture and props.
5: Salvage Cyberpunk product housings repurposed as advanced mechanical systems; retained painted casings, visibly replaced parts, functional connections. Translate into architecture and domestic equipment using the calm style of input 2. Do NOT copy the humanoid head, figure, text, exact device or dense micro-parts.

Architecture and story: The LOWER building along the back-left boundary is a disused small HARDWARE STORE: weathered muted terracotta and gray plaster over thick brick, a low old timber/metal roof, closed original door, former tool inventory still inside. Its courtyard-facing wall has ONE LARGE IRREGULAR COLLAPSED BREACH with thick jagged masonry edges and exposed timber lintel. Through the breach, clearly show the room's surviving solid rear wall, heavy shelving, a few hanging hand tools (wrench/saw/hammer silhouettes), old hardware boxes and a compact abandoned workbench. The breach is a view into a shallow enclosed interior, NOT a dark tunnel or through exit: retain a jagged low masonry sill and interior shelving/back wall plainly visible. Place several large recognizable matching plaster/brick wall fragments DIRECTLY BELOW THE BREACH, partly inside and partly at its exterior foot. Localized rubble mound hugs this wall; keep central court and exit routes clear. Prefer a few big readable pieces over granular rubble carpet. Let the room be mostly unpowered, softly visible in moonlight and spill from the neighboring shop. Abandoned, no worker.

The TALLER appliance shop follows the perpendicular back-right boundary. Both share the same ground datum. For proportional planning, hardware roof height about 3.8 m and appliance parapet about 4.9 m, roughly 1.3x. The rooftop additions are compact, overall visible structures planned below about 6.5 m. Do not render dimensions or text. The height difference is moderate and clear, not a doubled tall tower. A boxy flat roof and broad faded blue-gray/ivory facade distinguish this shop from the ruined hardware store. Two thirds of its envelope is ordinary repaired retail architecture with a CLOSED glazed storefront showing a few REFRIGERATORS, FRONT-LOADING WASHING MACHINES and compact household fans, plus a closed entrance. One remaining vertical third of the building is a substantial integrated cassette-futurist power/reconditioning service bay with reusable cream product casings, one large drive/vent module, battery drawers and physical electrical controls. Machinery should replace a meaningful one-third facade/body section rather than merely adding tiny wall-mounted boxes. Keep it recognizably a domestic appliance retailer, not a scrap press factory.

On the appliance FLAT ROOF visibly separate an angled small array of dark blue SOLAR PANELS with simple clean cell grids from a boxy compact salvaged GENERATOR with vented housing, modest exhaust pipe and physical service controls. Show sturdy mounts, a few thick functional cables leading to the mechanized bay/battery system. At night panels are passive and reflect subtle cool ambient light, not glowing screens. Generator can power restrained shop lighting; avoid smoke. All rooftop parts must be clearly visible from the elevated camera.

Temporary cassette-futurism direction retained: cream/beige durable squared casings, large tactile buttons, rotary switches, white-faced needle gauges, chunky handles, cassette/cartridge service drawers and broad ventilation slats. NO green CRT elements, NO CRT monitors, NO video/computer screens or substitute glowing amber displays. Use refrigerators/washers/fans instead of television merchandise. Small practical appliances may carry physical knobs and cartridge-style service hatches. Do not make robot faces or humanoids.

LAYOUT IS CRITICAL: the buildings and rear boundary walls form an unmistakable L in plan / V in the image, with their facades facing into the shared courtyard from perpendicular directions, NOT a single flat row. They meet at the back corner without another walk-through gap. Put one open access passage in the outer back-left boundary beyond the ruined shop, and one in the outer back-right boundary beyond the appliance store. Exactly TWO visible THROUGH EXITS, their complete frames, thresholds and reachable approaches clearly readable. The broken hardware wall is visibly a room with a SOLID REAR WALL, NOT a third through-passage. Keep both proper exits separate from the breach and retail windows.

Composition: single compact rectangular square base viewed as a diamond from elevated three-quarter angle. Fit the ENTIRE diorama within the canvas with at least a calm 6% surrounding margin on all sides. All lateral base corners, doorway pillars, front soil point and the entire highest rooftop equipment must remain uncropped. No tall front walls. The courtyard center is a broad connected empty dark concrete loading/work floor with a few large inset repair slabs and one flush service cover. Perimeter rubble, inventory and equipment cannot obstruct it.

Both FRONT camera-facing sides reveal thick simplified earth/foundation CUTAWAYS: beneath the ruin, an old damaged masonry footing and a capped former utility pipe; beneath the active appliance shop, a compact battery/power conversion module in a supported recess with a few organized thick supply conduits. Different systems for the two functions, no repeated giant motors or decorative pipe carpet. Coherent ground plane, supports and thresholds.

Rendering: restrained stylized 3D architectural concept art, broad painted planes and large simple material distinctions like INPUT 2. Structural breakage is the main wear detail. Preserve quiet wall/roof/floor surfaces away from the collapsed area. No all-over fine scratches, mottled grime, granular asphalt, photoreal miniature texture, toy plastic or excessively faceted low-poly. Repaired and reclaimed does not mean every surface covered with micro-damage.
Lighting: clearly NIGHT, deep desaturated navy ambient with soft cool moonlight on roofs and solar panels, restrained warm practical lighting inside the appliance showroom and near the two exits. Enough bounced light to read the breach interior, rubble, both passages and both cutaway faces. Simple quiet dark blue background. Dry ground. No neon, green glow, fog, smoke curtain, campfire, vegetation takeover, unrelated grocery stock, trash bins or prior-scene chimney. No figures, cars, captions, labels, watermark, UI, arrows or split panels. ONE complete image.

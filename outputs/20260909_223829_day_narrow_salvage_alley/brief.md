# 낮의 도심 속 좁은 골목 — 추가 테스트 1장

## 사용자 원문

테스트용으로 한번만 더 만들어 보고 결과물이 괜찮으면 마스터 레퍼런스 규칙으로 정리하자. 이번 키워드는 도심 속 골목 / 낮 / 폐건물과 쓰레기통 / 바닥에 널린 쓰레기 / 좁은 공간 / 한 장

## 해석과 적용 범위

- 현재 요청: 테스트 이미지 1장. 결과가 괜찮다는 사용자 평가 전에는 마스터 영구 규칙으로 승격하지 않는다.
- 기존 01~04 v2와 Salvage Cyberpunk + Little Devil Inside 건축 표현 유지.
- 이번 변경: 낮, 폐건물 골목, 작은 베이스·좁은 건물 사이 간격, 쓰레기통, 바닥의 식별 가능한 종이/납작한 포장지.
- 쇠락·회수·보수: 큰 파손과 결손, 다른 규격 폐부품으로 막은 벽, 수선 차양, 구조를 지지하는 회수 구동부, 기존 고장 설비를 우회하는 전력 연결.
- 좁음은 실제 배치 간격으로 표현하며 카메라 크롭으로 만들지 않는다.
- 중앙과 두 출구 접근로는 연속 확보. 큰 쓰레기는 벽쪽, 바닥 쓰레기는 낮고 평평한 개별 물체.
- 이전 결과에서 확인한 크롭/표면 과밀 보완: 전체 외곽에 여백 확보, 넓은 무늬 없는 포장면과 벽면 유지. 프롬프트의 여백 비율은 이번 실행 가이드이며 영구 규칙이 아님.
- 전봇대/상점가/야간 조명은 이전 장면의 소재이므로 자동 이월하지 않는다.
- 3면도·모델링·텍스처 맵 산출은 이번 범위 아님.

## 실제 생성 지시

Create ONE standalone game-environment concept image: a NARROW INNER-CITY ALLEY in DAYLIGHT, with ABANDONED BUILDINGS, TRASH BINS and LITTER SCATTERED ON THE FLOOR. The world is Salvage Cyberpunk: a declining post-apocalyptic city where old advanced technology and damaged urban structures are kept usable through scavenged repairs. This is a new location, not another shopping plaza.

REFERENCE ROLES:
1 is the mandatory layout topology only: one exit in each of two rear boundaries, connected open center, two camera-facing open cutaway sides. No diagram text, symbols, arrows or blue walls.
2 is the elevated quarter-view camera and full standalone base/cutaway only. Do not borrow its neon, shops, lettering, busy props or photographic miniature finish.
3 and 5 are primary Little Devil Inside architectural RENDERING references: large shaped solids, broad quiet color planes, selective wear, readable materials and controlled light. Exclude their world, characters, plants, storefront subjects and camera.
4 is the salvage-world design language only: worn advanced metal mechanisms, replacement components and old cloth. Translate the repair logic into functional architecture and utilities. No character, decorative robot limb/head, brushwork or dense texture marks.

FRAME AND SPACE — CRITICAL:
Use a square or near-square composition, pulled back enough that EVERY outer wall end, roof corner, passage frame and base corner fits inside generous empty background margin. Keep about one tenth of the image empty around the entire object; nothing touches or crosses the canvas edge. Show the COMPLETE diorama, not a cropped slice of a larger landscape. Neutral muted grey backdrop, no detailed distant city.
The actual footprint is compact and distinctly smaller/narrower than a plaza. Low abandoned building facades form a continuous L along the rear left and rear right edges around a short modest-width alley lane. The gap feels confined through close architecture and reduced ground footprint, not through zooming the camera. Keep the full central lane empty of bulky objects and continuous for movement/combat. Two plainly visible open exit passages, ONE on each rear boundary, each with its whole frame shown and a clear approach. All other ground-level doorways are closed or boarded. Large windows are raised and cannot read as more walk-through openings. Damage must not open additional traversable boundary gaps.
Camera-facing two sides remain low and open to view. Both exposed foundation faces have convincing thickness, a few large earth/masonry sections and several thick pipes. Keep the entire bottom corner and two faces visible. Compact low buildings, planned visible barrier height no more than about 6.5m; no towering city canyon.

SCENE AND AGE:
The abandoned buildings clearly show time and failed maintenance in BIG shapes: a short missing roof/upper-cornice section, one broad area of fallen plaster, blank boarded windows, a bent shutter and an empty former sign mounting. Retain large areas of faded unbroken painted wall between these marks.
Show scavenged repairs integrated into the alley: one damaged wall bay closed with a cut-down old industrial door fitted sideways into a mismatched frame, retaining its obsolete hinge sockets; a torn small utility canopy patched with one large cloth piece and a reclaimed curved metal panel; one failing lintel supported by a stout salvaged mechanical actuator with a clear circular joint and clamp base. These are structural adaptations with readable reasons, not matching new SF decoration.
On a side wall, a dead old electrical cabinet with a capped original feed is bypassed by a compact recovered power module, a differently painted replacement cover and one thick clearly routed cable. Its tiny indicator can still function even though the buildings are abandoned. Retain a few large technological couplings and connectors to distinguish surviving advanced infrastructure from an ordinary derelict alley. Equipment stays within the perimeter.
Place two or three old bins at wall recesses: a dented steel bin and a differently colored repaired wheeled bin, with a modest bag/cardboard cluster. Scatter visible individual paper sheets, flattened cartons and wrappers over parts of the alley floor, including a few near the middle, with broad stretches of floor between them. Larger garbage remains at walls. The requested scattered litter must look like separate recognizable objects, not a painted layer of dirt. No vehicle, dumpster or rubble mound blocking the lane.

MATERIAL TREATMENT — CRITICAL:
Render like a deliberately simplified 3D game environment in the architectural style of references 3 and 5. Large flat painted forms with soft lighting gradients; shaped edges, thickness, contact and clear material regions. Keep MOST wall and ground area visually calm and undecorated. Entire paving slabs remain free of weathering marks; use one broad flush repair patch and only a few larger damaged edges. Wear appears in selected large missing sections, bends, faded color blocks and a few broad exposed-metal patches. NO blanket grain, speckling, little chips on every edge, mottled stains on every tile, tiny scratches, dense cracks or gravel dust texture. Preserve age in the shape and construction even when surface noise is removed. Distinguish plaster, metal, cloth, stone, glass and paper with controlled material response. Not blurred, not plastic, not overly faceted low-poly.

LIGHT:
Neutral daytime sky fill with gentle directional sunlight and cool soft shadows. Muted faded plaster, desaturated teal/grey repaired metal, restrained dull ochre accents. Readable building faces and both cutaway sides. Dry ground, no glossy wet look, no cinematic night blue or sunset wash. No active storefront lighting or neon.

One image, one scene. No people, no shop displays, no vehicles, no labels, readable lettering, arrows, HUD, split panels or multiple views. Prioritize complete framing, narrow but connected empty floor, two visible exits, quiet surface depiction and a legible old city being kept usable through salvage repairs.

# 야간 고철 처리장

- run_id: 20260910_082127_scrapyard_night_barrel_fire
- request_original: 고철 처리장 / 밤 / 고철, 고철 처리 기계, 판자, 잡초, 드럼통 캠프파이어 / 한 장
- masters: v2.1
- execution_rules: v1.2
- request_mode: new_location
- requested_count: 1 final deliverable
- native_generation_route: built-in image_gen.imagegen
- api_explicitly_authorized: false
- scene_only_assumptions: 건조한 콘크리트 작업장, 청회색 야간 환경광, 드럼통 불을 주된 따뜻한 강조광으로 사용. 인물 없음.

## Scene plan

- 뒤쪽 경계: 수리한 골강판·회수 기계 외장과 고철 보관 구획으로 연속 경계 구성. 좌우 뒤쪽 면에 열린 게이트 하나씩.
- 중앙/접근로: 연결된 빈 작업·전투 바닥. 기계·고철·판자·화로는 중앙과 게이트 접근로 바깥에 둠.
- 처리 기계: 우측 후면 외곽의 낮은 유압 압축/절단 장치, 투입구 안쪽으로 접힌 짧은 선별 집게, 배출부 옆 압축 고철. 램·판금·교체 외장·제어함과 굵은 연결부의 기능 관계를 보여 줌.
- 요청 소품: 외곽에 큰 고철 형태와 판자 더미, 경계 균열의 잡초, 좌측 외곽 공간의 불붙은 드럼통 하나.
- 새 장소: 주거 골목 건물과 넝쿨·벽보를 계승하지 않고 산업 야드의 낮은 경계·처리 설비·하드스탠드로 재설계.
- 단면: 압축기 하부의 큰 기초, 한쪽 전력 도관, 다른 쪽 회수 섬프/짧은 반환 배관. 두 앞면 전체 판독.
- 표현: 넓고 정돈된 기본 색면에 선택적 큰 파손·교체판. 미세 고철/녹/풀 밀도를 화면 전체에 채우지 않음.
- 조명: 청회색 야간광 아래 두 출구·중앙·단면을 읽을 수 있게 유지하고 드럼통 불의 따뜻한 국소광을 대비.

## Reference roles

M02-01 공간 / M01-01 구도·단면 / M03-10 기본 표현 / M04-02 회수 산업기계 형태 / M03-06 야간의 환경광과 국소광. 실제 전달은 references.json에 별도 기록.

## Compiled generation prompt

Use case: stylized-concept. Create ONE complete game-environment concept image: a scrapyard at night with scrap metal, functional scrap-processing machinery, wooden planks, weeds, and a campfire burning inside a steel drum. Design a distinct industrial location. Do not reuse the residential alley from earlier in the conversation.

Use the five supplied master images ONLY for their assigned roles:
1. Spatial diagram: two adjoining rear boundaries, exactly one visible through-exit in each, and a clear central floor. Exclude blue walls, writing, arrows, icons and entrance circles.
2. Diorama reference: elevated three-quarter camera, complete rectangular isolated base, thickness and exposed cross-sections on BOTH front-facing sides. Exclude its specific buildings, neon, Japanese theme and street markings.
3. Little Devil Inside architecture: the PRIMARY visual style. Broad clean color planes, characteristic solid forms, readable thickness, selective large wear, restrained material depiction and organized detail. Exclude its characters, specific shops, historical world, lettering and camera.
4. Salvaged mechanical arms: translate large reclaimed actuator shells, substantial joints, mismatched replacement plates and functional connections into yard equipment. No characters or humanoid machines; do not copy photographic surface noise.
5. Little Devil Inside night scene: cool night ambient light with localized warm illumination, restrained materials and readable volumes. Do not copy the person, forest, camera, props or dense vegetation.

Layout and place identity: a compact open industrial reclamation yard enclosed along the two rear sides by low patched corrugated steel screens, reused heavy machine casings and solid salvage partitions. Their joins are closed so there are no unintended third passages. Exactly TWO clear open through-gates, one in the rear-left boundary and one in the rear-right boundary, each leading directly from the empty central hardstand. Show the threshold and ground beyond each opening. Both must remain fully legible. No residential buildings and no repeat of the prior alley silhouettes.

Along the rear-right edge, in a dedicated recessed equipment bay away from the exit approach, show a squat hydraulic scrap baler/shear with an unmistakable open receiving hopper, thick pressing platen, large hydraulic ram, and several stacked compressed metal bales beside its discharge side. Integrate a short articulated salvage sorting claw folded INWARD over its receiving hopper, entirely inside the peripheral machinery footprint. Neither boom nor load extends across the central floor or obscures a gate. Make the machine functional and readable rather than an unidentifiable mass of tiny parts. A small patched control cabinet and thick power/hydraulic connections visibly supply the unit. Its repaired advanced actuators and repurposed industrial shells establish Salvage Cyberpunk technology. Keep the machinery and rear barriers modest in height; planned visible structures below roughly 6.5m.

Along the rear-left perimeter, cluster a limited number of legible large scrap forms: bent sheet-metal shells, short beams and compressed bales, with quiet space between groups. Place a stack of rough wooden planks in one peripheral recess. Near the left SIDE edge, in a small cleared nook outside BOTH exit approaches and the central lane, put one weathered open-topped steel barrel with visible orange flames and embers: the requested drum campfire. No tents, people or additional camping scene. Scatter small grouped weeds in boundary cracks and around the outside of the plank/scrap storage; simplified leaf and grass masses, not dense foliage or wall-climbing vines.

The center is a broad connected EMPTY combat/work hardstand with both gate approaches clear. No central machine, scrap heap, barrel, planks, vehicle or obstacle. Use large dry repaired concrete slabs, some broad scuffs and a few flat traces, not a carpet of shavings, gravel or micro-debris. Foundations, machinery feet, pavement and thresholds share believable perspective and grounding.

Whole-base presentation is mandatory: one standalone rectangular diorama, elevated three-quarter view with the WHOLE base, all corners and both front cut faces comfortably inside the image with surrounding margin. No high foreground wall. Show thick earth/foundation strata and a location-specific industrial substructure: heavy foundations beneath the baler, a simple recessed power conduit on one front cut face, and a chunky collection sump with a short return pipe on the other. These are infrastructure cross-sections, never underground pedestrian tunnels or extra exits. Keep large structural masses, not granular dirt or repeated decorative pipe patterns.

Lighting: unmistakable NIGHT. Cool desaturated blue moon/sky fill reveals the rear gates, machine silhouette, central floor and both cutaway faces. The drum campfire is the principal warm accent, lighting adjacent steel, planks and ground with a restrained orange pool. A small subdued machine task light can identify the control area. No sunset sky, wet reflective floor, large fog bank, bright neon or excessive bloom. Isolate the base against a simple dark blue-gray atmospheric backdrop.

Art direction: sophisticated stylized 3D game environment, strongly led by reference 3's architectural/material simplification. Worn painted metal, rough wood and concrete retain broad readable color planes; selected large repairs and peeling patches explain age. A repaired old world, not new factory equipment, and not photoreal hyper-detailed miniature photography. Restrained slate/charcoal/dirty ivory industrial colors with limited faded hazard-yellow/orange parts. Distinct material response without tiny uniform rust, scratches, bolts or leaf noise. No painterly strokes, thick outlines, aggressively faceted low-poly geometry or plastic toy look. No people, robots, text labels, arrows, logos, watermarks, UI or split panels. Exactly one finished image, approximately 4:3 composition; complete base and structural readability take priority.

## Status

generated_and_reviewed — 최종 1장: scrapyard_night_barrel_fire.png. 구조 candidate_pass. 표면 손상 밀도는 uncertain으로 review.md에 기록. 추가 생성과 마스터 갱신 없음.

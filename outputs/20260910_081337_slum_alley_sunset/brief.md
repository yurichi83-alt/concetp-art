# 슬럼가 골목 / 노을

- run_id: 20260910_081337_slum_alley_sunset
- request_original: 슬럼가 골목 / 노을 지는 시간 / 쓰레기, 고철, 벽보, 넝쿨 / 한 장
- masters: v2.1
- execution_rules: v1.2
- request_mode: new_location
- requested_count: 1 final deliverable
- route: built-in image_gen.imagegen, reference-guided generation
- api_explicitly_authorized: false
- scene_only_assumptions: 건조한 바닥, 낮은 황금빛 사광과 차가운 그늘, 낡은 다세대 주거 및 임시 증축 골목. 인물 없음.

## 장면 계획

뒤쪽 좌측의 낮은 2층 주거 매스와 우측의 더 낮은 판금 증축이 경계를 이룬다. 각 뒤쪽 경계에 열린 통로 하나씩, 나머지 문은 닫힌 상태로 구분한다. 중앙은 연결된 전투·이동 바닥이며 쓰레기봉투·고철·골판지는 외곽 벽 아래에 모은다. 벽보와 넝쿨은 벽면과 지붕 가장자리에 국소 배치한다.

건물 결손을 교체 외장으로 보수하고, 회수한 큰 구동부를 구조 보강과 생활 공급 설비에 통합한다. 지하는 이 골목의 배수·공급 기능을 설명하는 새 단면으로 설계한다. 기존 골목/광장의 건물, 배관, 안개, 젖은 바닥을 재사용하지 않는다.

부피·두께·접지와 넓은 색면을 먼저 읽히게 하며, 노후함은 선택적인 큰 파손·수리·바랜 면으로 표현한다. 전체 베이스와 앞쪽 양면 단면을 여유 있게 프레이밍한다. 높이/충돌 수치의 판정은 3D 검증 대상이다.

## 참조 역할

입력 예정 순서: M02-01 공간 → M01-01 구도·단면 → M03-10 대표 표현 → M04-02 회수 기술 형태 → M03-15 건축의 재질·빛과 면.

## 실제 도구에 전달할 프롬프트

Use case: stylized-concept. Produce ONE finished game-environment concept image, a new slum alley at sunset, from these role-specific master references. This is a new location, not a remake of a prior generated courtyard.

Reference roles in the supplied order:
1. Layout diagram: use ONLY the two adjoining rear boundaries, exactly one exit in each, and the open connected central floor. Do not reproduce diagram colors, labels, arrows, icons or circles.
2. Diorama: use ONLY the elevated three-quarter camera, whole rectangular isolated base and thick cutaway along BOTH camera-facing base sides. Do not copy its buildings, neon, Japanese theme, street markings or surface density.
3. Little Devil Inside storefront: main architectural rendering reference. Use broad painted color planes, distinctive solid masses, readable frame thickness, restrained material information and selective large wear. Exclude its characters, world, specific shops, lettering and camera.
4. Salvaged mechanical arms: translate the large functional reclaimed actuator housings, replacement armor plates and mechanical joints into building repairs and utility equipment. Do NOT depict people, robots, limbs or this photoreal surface detail.
5. Little Devil Inside street: supplement architectural and ground planes, strong large sunlight/shadow shapes and restrained materials ONLY. Exclude its characters, world, camera, lettering and vegetation depiction.

Scene: an intimate back alley between improvised low tenement dwellings in a worn Salvage Cyberpunk settlement. Design fresh asymmetrical architecture: a squat two-level patched plaster dwelling along the rear-left boundary, and lower stepped sheet-metal extensions with a salvaged utility installation along the rear-right boundary. Large missing plaster patches reveal a few masonry blocks; reused exterior plates repair gaps; a reclaimed industrial actuator braces an improvised roof support. A bulky recovered water/power regulator with mismatched painted shells, a clear access panel and a few thick functional connections supplies the dwellings. The technology is visibly repaired and still in use. Keep modest silhouettes, with visible blocking structures planned below roughly 6.5m.

Spatial requirements take priority. One rectangular freestanding diorama, viewed from above at a three-quarter angle, framed with generous space around EVERY corner and the full base. The two rear sides form clearly continuous non-traversable boundaries, with exactly TWO unobstructed open through-passages: one in the rear-left boundary and one in the rear-right boundary. Both openings, thresholds and routes leading from the center must be plainly visible. Other doors are visibly shut. Roofs and foliage must not hide the exits. Camera-facing two sides are open cut edges with no foreground wall. A connected, moderately narrow but usable central combat/movement strip stays clear of large props; this should read as a slum alley, not a monumental plaza.

User motifs: trash, scrap metal, pasted posters, climbing vines. Cluster tied trash bags and cardboard against peripheral walls; a readable pile of a few bent metal panels and worn machine housings in one edge recess. Keep the central floor quiet with at most a few flat paper scraps. Put small overlapping faded/torn paper posters on wall panels; abstract graphic blocks, no prominent readable slogans or copied brands. Group climbing ivy in simplified dark green masses on selected wall corners and roof edges, with sparse hanging strands that leave entrances and architecture legible. Vines are explicitly requested; do not cover the scene with fine leaf detail.

Ground: large repaired concrete/asphalt planes, restrained broad cracks, continuous believable grounding and perspective between foundations, thresholds and paving. Expose thick earth/foundation layers on both front cut faces. Design new location-specific subsurface infrastructure: a simple stormwater channel and a reclaimed supply junction connecting clearly to the surface regulator, with a few substantial pipe sections. No underground entrances or underground pedestrian passages. Avoid repeating a generic identical pipe pattern.

Lighting: sun is setting, low warm amber/apricot sunlight grazing upper facades and ivy, long coherent shadows over the alley, cool muted violet-blue fill that keeps passages and cutaways readable. Dry surfaces, no inherited night fog, no wet-floor sparkles. A restrained warm neutral atmospheric backdrop isolates the whole base, without a panoramic city or extra terrain.

Style: sophisticated stylized 3D game environment in the architectural/material/lighting language of references 3 and 5, rendered with large clean color planes and selected meaningful detail. Aged does not mean dirty microtexture everywhere; clean depiction does not mean brand-new buildings. Show solid volumes, joins, thickness, grounding and distinct metal/plaster/fabric/leaf materials. No painterly brushwork, no hyper-detailed photoreal miniature, no plastic toy look, no aggressive low-poly facets, no pervasive rust speckles, gravel, tiny cables or grunge. No characters, UI, labels, arrows, watermarks or split panels. One complete image; full base framing first, roughly 4:3 composition.

## 상태

generated_and_reviewed — 결과: slum_alley_sunset.png. 구조 관찰 candidate_pass, 최종 1장, 추가 생성 없음. 사용자 승인 아님.

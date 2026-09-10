# Preflight — masters v2.4 / execution v1.5

This is a plan and submission check, not output QA. Use PLANNED / BLOCKED / UNKNOWN or N/A with a reason. Do not mark an unseen image correct. Resolve missing required inputs, contradictory instructions, unmapped requirements and prompt variables before calling the tool.

## Tool, delivery and compilation

| Item | Status | Evidence |
|---|---|---|
| Current request is generation/edit; active changes and scene-only exceptions recorded | UNKNOWN | |
| Native tool/permissions; separate API explicit authorization if needed | UNKNOWN | |
| Actual image input mechanism, supported format and selected parameter verified | UNKNOWN | |
| Confirmed limits recorded by parameter; referenced_image_paths limit not inferred from recent-image max5 | UNKNOWN | |
| Actual input count recorded separately from contract; text/token/weight/mask/rewrite unknowns retained | UNKNOWN | |
| Original selected images inspected; unapproved outputs/review_only excluded as default positive references; explicit edit/own-correction targets separately role-labeled | UNKNOWN | |
| Geometry01/02, art03 and world04 roles sufficiently represented; redundant images avoided and omissions explained | UNKNOWN | |
| Each input index/role/exclusion mapped; art/world camera excluded without claiming enforced weights/masks | UNKNOWN | |
| LDI supplement scope / M03-12 building-only exclusion respected | UNKNOWN | |
| Requested final count / one scene per image / current aspect ratio supported | UNKNOWN | |
| Independent new scenes, when requested: separate plan/prompt/input set and no other scene's output or correction as input | UNKNOWN | |
| Own correction has own scene ID and parent run; corrections do not alter final requested count | UNKNOWN | |
| Saved generation_prompt.md has STRUCTURE MUST KEEP -> CURRENT SCENE -> ART / REFERENCE ROLES only | UNKNOWN | |
| Actual prompt omits history/examples/approval bookkeeping and duplicated rules, preserves all applicable requirements | UNKNOWN | |
| No arbitrary word/token cap or constraint deletion; any measured counts recorded only as metadata | UNKNOWN | |
| No invented token usage, model configuration, revised_prompt or claim of no truncation | UNKNOWN | |
| Saved exact prompt ready for submission; all variables resolved | UNKNOWN | |

## Requirement coverage audit

Review brief.md's requirement-to-prompt-and-check ledger against the active masters and user constraints. A group is covered only when every applicable subcondition has a prompt clause and check. Record exact ledger row/clauses rather than merely “masters read.” Execution/approval/storage requirements map to preflight and do not need image text.

| Coverage audit | Status | Ledger row / exact clause / unresolved issue |
|---|---|---|
| Every applicable01/02 structure constraint maps to prompt and planned/final check | UNKNOWN | |
| Building entry/roof and nonbuilding exceptions map to prompt and W04/W05 checks | UNKNOWN | |
| All03 art and04 world requirements map to prompt and relevant S/W checks | UNKNOWN | |
| Current user additions/exclusions/count/independence/edit preservation map to appropriate prompt or execution check | UNKNOWN | |
| Reference role exclusions map to actual input index and prompt role clause | UNKNOWN | |
| N/A decisions justified; no UNMAPPED or CONFLICT remains | UNKNOWN | |

## Structure and final-observation readiness

| Item | Status | Plan evidence and intended final check |
|---|---|---|
| Shared cubic space / square base / common XYZ and scale | UNKNOWN | |
| Exactly one selected projection, explicit camera choice; no orthographic-style ambiguity or mixed test criteria | UNKNOWN | |
| Top/bottom corner correspondence / vertical axes / constant extrusion / two planar cuts | UNKNOWN | |
| Building footprint polygons/contact walls parallel to common X/Y axes, or building-free N/A | UNKNOWN | |
| Roof planes/surfaces defined separately: slopes/ridges/valleys/eaves, wall joins and support | UNKNOWN | |
| Polygon axes, roof joins, upper/lower correspondence checked separately from AABB collision | UNKNOWN | |
| Whole base/front cuts and both connected boundaries framed; front sightline open | UNKNOWN | |
| Base upper/lower edges, building footings/wall tops/roof and paving lines visible enough for final comparison | UNKNOWN | |
| 2D guide recorded as reference, not geometry lock; coordinates/camera source separate from actual image input | UNKNOWN | |
| Two rear blocking directions approximately11/1 o'clock, one functional exit each and no unintended third gap | UNKNOWN | |
| Each exit position/form/state/post-clear connection/entrance-sharing chosen for this scene; no fixed/forced alternating positions | UNKNOWN | |
| Left and right walking volumes: approach / narrowest / height / turn / transition / open-state route / opening mechanism clearance | UNKNOWN | |
| Designed lock distinguished from accidental blockage; closed/hidden connection plan distinguished from visible evidence | UNKNOWN | |
| Exits can use buildings/alley/stairs/ramps; no mandatory separate gate or fully exposed interior | UNKNOWN | |
| Stairs/ramps follow XY and connect levels; front soil cut is not a third exit | UNKNOWN | |
| Central combat floor clear, including peripheral props/rubble/protrusions outside walking volume | UNKNOWN | |
| Nonbuilding tanks/vehicles/props retain allowed curves/rotations with common camera/grounding/routes | UNKNOWN | |
| Exposed interior room depth / entry / aisle / functional space or justified N/A | UNKNOWN | |
| Barrier height plan up to approximately6.5m; metric claims reserved for actual3D validation | UNKNOWN | |
| Each building human-scale door/shutter with credible grounding; decorative/shared-exit role, closed allowed | UNKNOWN | |
| Each building roof40~80% functional footprint plan, support/connections/remaining space; preserved height/framing/routes | UNKNOWN | |
| Building entry/roof percentage exempt for nonbuildings; final2D coverage remains estimate/uncertain | UNKNOWN | |
| Broad forms/color areas/selective damage/material differences; functional salvaged technology and place-wide repairs | UNKNOWN | |
| New architecture/paving/cutaway or explicit edit preservation; no unrelated prior scene carryover | UNKNOWN | |
| Lighting/atmosphere preserve structural evidence; no unrequested figures/text/UI | UNKNOWN | |
| Final actual-image line/footing/upper-lower/roof/route comparison planned; guide/AABB/prompt success cannot substitute | UNKNOWN | |
| Core occlusion -> UNCERTAIN; structural FAIL -> needs_revision; cannot inspect -> not_reviewed | UNKNOWN | |
| Saved3D geometry/camera needed for later precision claims; no unrequested Unity/mesh creation | UNKNOWN | |

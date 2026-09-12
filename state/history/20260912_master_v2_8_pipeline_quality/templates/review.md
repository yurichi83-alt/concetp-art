# Image review — master v2.7 / execution v1.8

- image_path_or_artifact:
- native_image_size_px:
- actually_opened: false
- status: not_reviewed
- user_approval: none
- structural_status: not_reviewed
- art_world_request_status: not_reviewed
- masters: v2.7
- execution_rules: v1.8
- further_generation_authorized: C01_to_C04_and_L01_to_L07_only_for_generation_requests (standing scope retained; final evidence strengthened by master_update_20260910_v2_4; orthographic required by master_update_20260911_v2_5)
- structure_plan_path:
- structure_plan_preflight_status: not_reviewed
- planned_projection: orthographic_parallel (mandatory for the final image)
- final_projection_evidence_status: not_reviewed
- structure_plan_and_actual_final_image_compared: false
- structural_gate: any_FAIL_means_needs_revision; otherwise_critical_uncertainty_means_uncertain; all_applicable_final_checks_PASS_and_justified_NA_required
- actual_collision_mesh_UV_validation_in_current_acceptance_scope: false
- missing_actual_collision_mesh_UV_validation_is_not_FAIL_or_UNCERTAIN: true
- previous_review_or_recheck: none
- supersedes_previous_judgment_scope: none

| ID | PASS / FAIL / UNCERTAIN / NOT_REVIEWED / NOT_APPLICABLE | Visible evidence |
|---|---|---|
| C01 | NOT_REVIEWED | |
| C02 | NOT_REVIEWED | Both cuts; upper/lower line pairs and corner correspondence vectors tested against the required orthographic projection. Cite evidence rows. |
| C03 | NOT_REVIEWED | Basic plane/corners and visible outline geometry. Separate convex impression, visible line bending, and unverified physical 3D curvature. |
| C04 | NOT_REVIEWED | Same-world-direction straight line pairs across base upper/lower edges, paving, footings, storey floors, shutter horizontals, terrace beams, upper walls and level roof edges; required orthographic projection and roof joins. Classify curve tangents/slopes separately. Cite evidence rows. |
| L01 | NOT_REVIEWED | |
| L02 | NOT_REVIEWED | Exactly two assigned functional exits toward rear-left/rear-right: position/type/shown state/post-clear connection/entrance-sharing. Count functions, not visible doors. |
| L03 | NOT_REVIEWED | Both approaches: start, narrowest, turn, transition, opening clearance and state-appropriate/post-clear connection; object-volume intrusion. |
| L04 | NOT_REVIEWED | |
| L05 | NOT_REVIEWED | Ground/foundation/walls/entrances/transition levels plus roof-wall joins and machinery support. Ambiguous roof structure is UNCERTAIN, not an intentional-shape PASS. |
| L06 | NOT_REVIEWED | Interior entry/aisle/functional space and depth, or justified N/A. |
| L07 | NOT_REVIEWED | Compare actual visible footings/main placement/straight structure with common XY and permitted ground-level curved boundary segments. Inspect grounding, boundary continuity and walk/block distinction. Curve tangents are not straight-axis lines. Occluded critical footing/boundary is UNCERTAIN; roof/awning/shadow alone cannot prove footprint rotation/wall tilt. Building-free N/A needs reason. No actual collision validation. |
| S01 | NOT_REVIEWED | Broad clean base-color areas with selected nearby-tone color variation, including intact surfaces; brushwork distinguished from rust/dirt/peeling. |
| S02 | NOT_REVIEWED | Surface-relative broad stroke size, directional variation and open space; no all-over equal small marks or fixed global density. |
| S03 | NOT_REVIEWED | Flat brushwork and coherent modeled volume coexist. Inspect raised relief, wavy/refractive-glass patterns, mosaic/fine noise, excessive stroke density or unreadable form. Brushwork itself is not a failure. |
| S04 | NOT_REVIEWED | Large light-shadow masses preserve silhouette, thickness, grounding, mechanical joins and distinct material cues despite surface strokes. |
| W01 | NOT_REVIEWED | |
| W02 | NOT_REVIEWED | |
| W03 | NOT_REVIEWED | Functional machine presence may form shell/frame/service building or a specified equipment storey; no universal machine floor. Requested storey ratio is separate from rooftop coverage. |
| W04 | NOT_REVIEWED | Each building human entrance: closed allowed, actual entry not required; decorative or shared with one assigned exit. Nonbuilding objects exempt. |
| W05 | NOT_REVIEWED | Each building roof 40~80% functional composition, visible basis/uncertainty, not exact 2D area certification or requested storey machine ratio. Avoid redundant equipment above a machine storey or mandatory repeated tank/panel kit while retaining function/support/space. Nonbuilding tanks/vehicles/props exempt. |
| R01 | NOT_REVIEWED | |
| R02 | NOT_REVIEWED | New location/independent variants: observed large forms, facade depth, place/spatial/boundary/exit relationships and cutaway differences, not only color/storey count/location/detail swaps. Plans or exclusion of previous output alone cannot prove PASS. NOT_APPLICABLE for an explicit edit. |

## Measurement caveat
Brush size, coverage and tone count have no universal numeric threshold. Judge observable surface organization and readability. B03-01~04 approve only color-plane/brushwork traits; generated B03-02~04 do not certify geometry, layout, exits or overall QA. Their night/palette/white lamps/damage quantity are not fixed checks. This surface update does not expand structural auto-correction scope.

Approximately <=6.5m height and human-scale route space are planning conditions, not exact metric certification from 2D. Actual collision creation/testing and mesh/UV validation are excluded from this image task and its acceptance criteria; their absence alone is not FAIL or UNCERTAIN. Continue checking visible grounding, thickness, support, continuous boundaries and routes.
Closed-state imagery does not visually prove a later opening animation or all hidden interior space. Distinguish visible evidence from the planned post-clear connection; do not require an exposed outside floor for every valid transition type.
For future separately requested precise modeling, use validated 3D blockout/camera geometry and treat generated 2D images as appearance/material/lighting guidance. S04 judges visible form readability, not three-view consistency or mesh/UV quality. This review does not authorize separate collision/3D production.

F-01~07 are optional scoped_architecture_form sources (generation_input_allowed=true, default_generation_input=false): selected large form/facade depth only; source camera/fine texture/photoreal density/neon/extreme height/water-base/text/people excluded, source not confirmed LDI. F-08~11 are scoped_architecture_example comparisons only (generation_input_allowed=false, default_generation_input=false, geometry_approved=false) with original needs_revision retained. Form preference does not approve projection/layout/routes/ratios or whole QA. Original27, surface4 and architecture supplements remain separate and default priorities unchanged.

## Exit function and route evidence

| Exit | Within-side position / type / shown state | Visible approach and transition | Planned post-clear connection / opening clearance | Building entrance sharing |
|---|---|---|---|---|
| Rear-left (~11 o'clock) | | | | |
| Rear-right (~1 o'clock) | | | | |

Center/intermediate/end positions are allowed and need not alternate. A designed closed gate is distinct from rubble blocking an exit; do not relabel fences/stock/rails blocking a shown-open route as intentional closure. Building entrances may double as the assigned exits, while other entrances remain decorative. For stairs/landings/ramps, verify planned XY direction and level joins; equipment-between/below passages can be valid. Boundaries may use substantial machinery, linked structures, vehicles, containers or retaining structures with visible blocking continuity; low props alone are insufficient. Front soil cuts do not supply a third exit.

## Final-image line-pair evidence
Use the actual native-resolution image, origin (0,0) at top-left, +x right, +y down. Record observed endpoints, not inferred hidden geometry. Choose representative pairs covering both ground axes, base upper/lower edges and each building's available footing/storey floor/shutter horizontal/terrace beam/upper wall/level roof relations; note missing or occluded evidence. Exact measurement of every pixel is not required.

- coordinate_selection_method_and_view_scale:
- native_coordinate_conversion_if_resized:
- optional_angle_method_and_estimated_manual_reading_error:

| Pair ID / QA IDs | Same 3D direction and basis | Line A: feature; native endpoints (x,y)→(x,y) | Line B: feature; native endpoints (x,y)→(x,y) | Expected relation under planned projection | Observed relation / optional screen angles | PASS / FAIL / UNCERTAIN and limitation |
|---|---|---|---|---|---|---|
| G01 / C02,C04 | Base X upper/lower | | | | | NOT_REVIEWED |
| G02 / C02,C04 | Base Y upper/lower | | | | | NOT_REVIEWED |
| G03 / C04 | Base ↔ axis-aligned paving; note if no usable paving line | | | | | NOT_REVIEWED |
| G04 / C04,L07 | Base/paving ↔ building footing; repeat per building/direction as needed | | | | | NOT_REVIEWED |
| G05 / C04,L05 | Footing/base ↔ level wall top/level roof edge; repeat per building/direction as needed | | | | | NOT_REVIEWED |
| G06 / C04 | Base/paving ↔ storey floors/shutter horizontals/terrace beams/upper walls; repeat across heights and buildings | | | | | NOT_REVIEWED |

Classify each line before comparing it: same-world-direction level edges, sloping roof line, ridge/eave, awning, curve tangent, shadow, or rotated nonbuilding feature. Quarter-view diagonals are normal; they must remain consistent for the same ground direction. Do not force pitched roof lines or sloping ridges/eaves into horizontal XY groups. Inspect their roof-plane/wall/support joins separately. Curve tangents need not parallel common straight axes; inspect curved shape/thickness/support/grounding and continuity separately. Internally consistent building lines may still contradict the base/paving camera; compare buildings against the ground, not just against themselves.

For the mandatory orthographic projection, compare parallelism across locations and heights and screen length of equal real lengths in the same 3D direction. Perspective convergence or depth-based scaling is FAIL even when coherent; do not relabel it as an acceptable alternative. Optional screen angles may use atan2(dy,dx), with method and reading error recorded; they are not measured 3D rotation angles. No universal angle/pixel tolerance is derived from one example.

## Upper/lower correspondence evidence
For the constant-depth orthographic base, corresponding upper/lower displacement vectors must share screen direction and length. Perspective-dependent apparent thickness is not an exemption.

| Vector ID / QA IDs | Visible corresponding corner | Upper point (native x,y) | Lower point (native x,y) | Observed vector (dx,dy), optional length | Relation to other corners / required orthographic projection | Status / occlusion / uncertainty |
|---|---|---|---|---|---|---|
| V01 / C02,C03 | | | | | | NOT_REVIEWED |
| V02 / C02,C03 | | | | | | NOT_REVIEWED |
| V03 / C02,C03 | | | | | | NOT_REVIEWED |

- Observed perspective convergence/depth-based scaling violations, or insufficient evidence (C02/C04; no alternative perspective PASS):
- Convex floor impression:
- Observed straightness/bending of long outlines:
- Projection/thickness correspondence and lighting/paving cues:
- What physical 3D shape remains unproven:

## Building geometry and visibility
| Building / QA IDs | Planned main placement/straight axes and curved boundary segments | Actual footing/walk-block boundary continuity and visibility | Floors/shutter/terrace/upper-wall/roof lines vs base; slopes/curve tangents/occlusion separated | Roof-plane/wall joins and machinery support | Final status / remaining uncertainty |
|---|---|---|---|---|---|
| / C04,L05,L07 | | | | | NOT_REVIEWED |

- Ground-level building curves: visible grounding / thickness / local support / continuous walk-block boundary; no enclosing rectangular-plinth obligation:
- Nonbuilding curved or rotated shapes: common camera / grounding / boundary role / visual route clearance:
- Differences between the structure plan and the actual final image:

A plan PASS or optional planning-volume/AABB check cannot fill missing final-image evidence; no actual collision check is required. Critical occluded footings remain L07 UNCERTAIN even if upper wall lines allow a separate C04 FAIL. Distinguish footprint rotation from height-dependent projection mismatch, roof/awning slope and curve tangents; do not invent the hidden footprint or convert a screen-angle difference to a physical rotation.

## Actual form and place comparison (R02)
- Comparison target, or explicit-edit N/A reason:
- Primary silhouette/storey volumes/wings/recesses/projections visible in final image:
- Facade/functional-space depth, selected stairs/decks/roofs or integrated mechanical body:
- Lane width/building function and adjacency/boundary/exit relationship/cutaway differences:
- Why the difference exceeds color/storey count/location/detail swaps or mirroring/recoloring:
- Repeated primary body/roof kit/exit-operation pattern still observed:
- Scene-only ratios/storeys/counts/props/weather/forms not promoted to defaults:
- Visible evidence and R02 status; no fixed change count or compulsory curves:

A different plan or an unused previous output is not perceptual evidence. Compare actual images; the central clear space may suit an alley/city without repeating a large courtyard. R02 does not expand structural auto-correction authority.

## Proposed correction
Record structural faults and preserved elements. Correct and regenerate observed structural errors under docs/05_GENERATION_RULES.md, then inspect the real output again. Stop when structure passes; do not automatically iterate on taste alone.

Global block/projection faults require reconstruction without preserving failed projection/joins. Retain the current request's or approved curves, projections, L-shaped wings, facade depth and functional character in the corrected guide/design; do not regress to generic boxes. Review/analysis/master-update-only requests do not trigger generation. All applicable structural checks must pass before overall structural pass.

## Recheck history
- Target image/run and earlier review:
- Current judgment and supporting evidence rows:
- Prior judgment superseded by this record (scope/reason):
- Original image and previous review/result retained: true

Keep historical records unchanged. A latest needs_revision supersedes an earlier candidate_pass for current use; it does not make the failed result a positive master or default generation input. Failure examples are review evidence, with text-only document links where useful.

W04/W05 are building exterior-design checks; they do not expand the C01~C04/L01~L07 structural auto-correction scope. Any clear exterior FAIL remains needs_revision; critical uncertainty remains uncertain. Review/analysis/master-update requests do not authorize automatic image generation.

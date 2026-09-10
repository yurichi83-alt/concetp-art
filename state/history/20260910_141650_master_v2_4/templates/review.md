# Image review

- image_path_or_artifact:
- actually_opened: false
- status: not_reviewed
- user_approval: none
- structural_status: not_reviewed
- art_world_request_status: not_reviewed
- masters: v2.3
- execution_rules: v1.4
- further_generation_authorized: C01_to_C04_and_L01_to_L07_only_for_generation_requests (standing approval; checks and L07 updated by master_update_20260910_v2_3)
- structure_plan_and_projection_compared:
- structural_gate: any_FAIL_means_needs_revision; critical_uncertainty_means_uncertain

| ID | PASS / FAIL / UNCERTAIN / NOT_REVIEWED / NOT_APPLICABLE | Visible evidence |
|---|---|---|
| C01 | NOT_REVIEWED | |
| C02 | NOT_REVIEWED | Visible cuts plus thickness/corner correspondence. |
| C03 | NOT_REVIEWED | Four-corner plane / vertical correspondence / no unintended curve or bevel. |
| C04 | NOT_REVIEWED | Single projection across floor/buildings/boundaries; coherent roof slopes/ridges/eaves and wall-top geometry. |
| L01 | NOT_REVIEWED | |
| L02 | NOT_REVIEWED | Exactly two assigned functional exits toward rear-left/rear-right: position/type/shown state/post-clear connection/entrance-sharing. Count functions, not visible doors. |
| L03 | NOT_REVIEWED | Both approaches: start, narrowest, turn, transition, opening clearance and state-appropriate/post-clear connection; object-volume intrusion. |
| L04 | NOT_REVIEWED | |
| L05 | NOT_REVIEWED | Ground/foundation/walls/entrances/transition levels plus roof-wall joins and machinery support. Ambiguous roof structure is UNCERTAIN, not an intentional-shape PASS. |
| L06 | NOT_REVIEWED | Interior entry/aisle/functional space and depth, or justified N/A. |
| L07 | NOT_REVIEWED | Building horizontal footprint/player-contact fixed walls follow common XY axes; compare polygon edges and actual image, not screen pixel angles or AABB alone. Props/vehicles/round tanks exempt; building-free N/A needs reason. |
| S01 | NOT_REVIEWED | |
| S02 | NOT_REVIEWED | |
| S03 | NOT_REVIEWED | |
| S04 | NOT_REVIEWED | |
| W01 | NOT_REVIEWED | |
| W02 | NOT_REVIEWED | |
| W03 | NOT_REVIEWED | |
| W04 | NOT_REVIEWED | Each building human entrance: closed allowed, actual entry not required; decorative or shared with one assigned exit. Nonbuilding objects exempt. |
| W05 | NOT_REVIEWED | Each building roof 40~80% functional composition, visible basis/uncertainty, not exact 2D area certification. Nonbuilding tanks/vehicles/props exempt. |
| R01 | NOT_REVIEWED | |
| R02 | NOT_REVIEWED | New location only; NOT_APPLICABLE for an explicit edit. |

## Measurement caveat
Height approximately <= 6.5m and collision clearance require 3D validation.
Closed-state imagery does not visually prove a later opening animation or all hidden interior space. Distinguish visible evidence from the planned post-clear connection; do not require an exposed outside floor for every valid transition type.

## Exit function and route evidence

| Exit | Within-side position / type / shown state | Visible approach and transition | Planned post-clear connection / opening clearance | Building entrance sharing |
|---|---|---|---|---|
| Rear-left (~11 o'clock) | | | | |
| Rear-right (~1 o'clock) | | | | |

Center/intermediate/end positions are allowed and need not alternate. A designed closed gate is distinct from rubble blocking an exit. Building entrances may double as the assigned exits, while other entrances remain decorative. For stairs/ramps, verify XY plan direction and level joins; front soil cuts do not supply a third exit.

## Geometry evidence
- Building footprint edge axes and actual player-contact boundaries:
- Roof plane boundaries / wall-top correspondence / machinery supports:
- Nonbuilding curved or rotated shapes: common camera / grounding / boundary role / route clearance:
- Any ambiguity or conflict with the structure plan (do not pass by intent or AABB noncollision alone):

## Proposed correction
Record structural faults and preserved elements. Correct and regenerate observed structural errors under docs/05_GENERATION_RULES.md, then inspect the real output again. Stop when structure passes; do not automatically iterate on taste alone.

Global block/projection faults require reconstruction without preserving failed geometry. Review/analysis/master-update-only requests do not trigger generation. All applicable structural checks must pass before overall structural pass.

W04/W05 are building exterior-design checks; they do not expand the C01~C04/L01~L07 structural auto-correction scope. Any clear exterior FAIL remains needs_revision; critical uncertainty remains uncertain. Review/analysis/master-update requests do not authorize automatic image generation.

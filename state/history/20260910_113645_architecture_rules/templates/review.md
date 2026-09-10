# Image review

- image_path_or_artifact:
- actually_opened: false
- status: not_reviewed
- user_approval: none
- structural_status: not_reviewed
- art_world_request_status: not_reviewed
- further_generation_authorized: structural_errors_only_for_generation_requests (standing approval; checks clarified by master_update_20260910_v2_2)
- structure_plan_and_projection_compared:
- structural_gate: any_FAIL_means_needs_revision; critical_uncertainty_means_uncertain

| ID | PASS / FAIL / UNCERTAIN / NOT_REVIEWED / NOT_APPLICABLE | Visible evidence |
|---|---|---|
| C01 | NOT_REVIEWED | |
| C02 | NOT_REVIEWED | Visible cuts plus thickness/corner correspondence. |
| C03 | NOT_REVIEWED | Four-corner plane / vertical correspondence / no unintended curve or bevel. |
| C04 | NOT_REVIEWED | Single projection across floor, buildings and boundaries. |
| L01 | NOT_REVIEWED | |
| L02 | NOT_REVIEWED | |
| L03 | NOT_REVIEWED | Both routes: start, narrowest, turn, threshold, beyond; object-volume intrusion. |
| L04 | NOT_REVIEWED | |
| L05 | NOT_REVIEWED | |
| L06 | NOT_REVIEWED | Interior entry/aisle/functional space and depth, or justified N/A. |
| S01 | NOT_REVIEWED | |
| S02 | NOT_REVIEWED | |
| S03 | NOT_REVIEWED | |
| S04 | NOT_REVIEWED | |
| W01 | NOT_REVIEWED | |
| W02 | NOT_REVIEWED | |
| W03 | NOT_REVIEWED | |
| R01 | NOT_REVIEWED | |
| R02 | NOT_REVIEWED | New location only; NOT_APPLICABLE for an explicit edit. |

## Measurement caveat
Height approximately <= 6.5m and collision clearance require 3D validation.

## Proposed correction
Record structural faults and preserved elements. Correct and regenerate observed structural errors under docs/05_GENERATION_RULES.md, then inspect the real output again. Stop when structure passes; do not automatically iterate on taste alone.

Global block/projection faults require reconstruction without preserving failed geometry. Review/analysis/master-update-only requests do not trigger generation. All applicable structural checks must pass before overall structural pass.

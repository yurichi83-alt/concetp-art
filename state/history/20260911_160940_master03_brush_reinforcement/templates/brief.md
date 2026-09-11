# Generation brief — masters v2.5 / execution v1.6

- run_id:
- request_original:
- active_user_changes_and_scene_only_exceptions:
- masters: v2.5
- execution_rules: v1.6
- request_mode: new_location / edit_existing / own_structural_correction (select one)
- edit_target_and_preserved_aspects:
- scene_location:
- time_and_palette:
- scene_only_assumptions:
- requested_final_count:
- independent_new_scenes_requested: false
- request_group_id_and_scene_id:
- own_parent_run_if_correction:
- other_independent_scene_outputs_excluded_from_inputs:
- output_aspect_ratio: choose an actually supported ratio that frames the whole base
- native_generation_route:
- api_explicitly_authorized: false

## Shared geometry plan before art
- structure_plan_artifact_and_coordinate_source:
- structure_guide_image_path:
- common_XYZ_scale_and_square_footprint:
- selected_projection_mode: orthographic_parallel (mandatory for the final image)
- selected_camera_and_scene_only_parameters:
- projection_specific_expected_line_families_and_top_bottom_correspondence:
- base_top_bottom_corner_pairs_vertical_axes_consistent_depth_and_two_planar_front_cuts:
- building_footprint_polygons_with_common_XY_axis_for_each_edge_L07_or_building_free_NA:
- roof_planes_slopes_ridges_valleys_eaves_wall_top_joins_and_equipment_support:
- building_footings_wall_top_roof_paving_lines_kept_visible_for_final_comparison:
- building_and_prop_volumes_outside_center_and_routes:
- polygon_axis_and_roof_checks_separate_from_AABB_overlap_checks:
- planned_steps_ramps_XY_direction_and_level_connections:
- nonbuilding_vehicles_tanks_props_allowed_shapes_rotations_same_camera_grounding:
- visible_barrier_height_plan_up_to_approximately_6_5m:
- exposed_interior_room_depth_entry_aisle_functional_space_or_NA:
- previous_faulty_geometry_not_to_preserve:
- actual_3D_source_if_already_available_or_future_precision_need:

Use the mandatory single orthographic camera for the final image; weak perspective is not an option and “orthographic-style” alone is insufficient. Record rotation/elevation/scale as scene choices, without fixing a universal isometric angle. The delivered 2D guide is a visual reference, not a geometry lock; saved coordinates are not automatically supplied as enforced geometry. A future need for modeling precision requires an actual 3D geometry/camera source and separate validation, not an unrequested Unity/mesh task.

## Scene and building plan
- Back-left blocking boundary composition:
- Back-right blocking boundary composition:
- Boundary gaps prevented from reading as a third transition:
- Central free combat floor / full front view:
- Peripheral large props and protected walking volumes:
- Building function / masses / place identity / differences from previous new location:
- Front cutaway layers and mechanical infrastructure tied to the current place:
- Large age / repair / functional recovered technology relationships across buildings and everyday facilities:
- Relative mechanical presence without a fixed global percentage or copied devices:
- Form / thickness / material separation / later three-view readability:
- Lighting and atmosphere without obscuring structural evidence:

| Building | Human-scale entry / grounded threshold | Role: decorative / left exit / right exit | Roof form, functional 40~80% plan, support and connections | Remaining broad surfaces / height / visibility |
|---|---|---|---|---|
| | | | | |

Each building needs a credible door/shutter; closed is allowed and actual gameplay entry is not required. A shared entry/exit needs no extra exit. Inspection panels/vents do not substitute. Roof coverage is each building's union of purposeful element footprints, excluding shadows/grime/paint/plain roof, not a scene average or mechanical ratio. Nonbuilding tanks/vehicles/props are exempt from building entry/roof percentage rules. Final 2D coverage is a visual estimate or uncertain, never exact metric certification.

## Two functional exits
One assigned transition toward back-left (approximately 11 o'clock), one toward back-right (approximately 1 o'clock). Select center/intermediate/end positions and suitable forms for this scene; no inherited fixed coordinates or forced alternation. Building/internal entries, alley gates, facility passages, stairs and underground parking ramps are valid. Count transition functions, not visible doors, and keep role labels out of the image unless requested.

| Exit | Direction / within-side position | Type | Shown pre-clear closed or post-clear open state | Approach / narrowest / turn / transition / opening clearance / post-clear connection | Shared building entrance or separate |
|---|---|---|---|---|---|---|
| Left | | | | | |
| Right | | | | | |

- Visible evidence expected for both exits and their approaches:
- Intentional closed mechanism distinguished from rubble; planned operation/connection versus what can be observed:
- Open state continuous route and external protrusion/volume check:
- Building-interior transition: credible entrance and scale; hidden connection is planned, not visually verified:
- Stairs/ramps: XY alignment, level connections; no third exit through front soil cuts:

## Reference roles and tool evidence
Use references.json for inspected versus actually submitted images, input order, scope/exclusions, omitted roles/reasons, confirmed parameter-specific contract and unknown capabilities. The mandatory orthographic rule overrides every reference camera, including M01; geometry sources govern base/framing/connectivity within it; style/world sources supply their approved aspects and exclude their camera/layout. This is an instruction, not a claimed reference-weight or mask control. M03-12 is building-only. Do not cross-input independent new scenes.

## Requirement-to-prompt-and-check coverage ledger
For every applicable visual requirement, record a short exact clause from the compiled prompt, the plan evidence and its final QA check. Expand grouped rows into individual requirements if a clause covers only part. Add every active user constraint; no row may conceal an unmapped subcondition. N/A needs a reason. Operational requirements belong to preflight rather than image text. This ledger, history and approval bookkeeping are not pasted into the generation prompt. No arbitrary length target permits deleting constraints.

| Requirement / source | Exact prompt clause and section | Plan evidence | Final QA IDs / observation | Coverage: MAPPED / UNMAPPED / CONFLICT / N/A + reason |
|---|---|---|---|---|
| 01: single scene, quarter-view, whole independent base and boundaries | | | C01 | UNMAPPED |
| 01: square base, shared XYZ/scale, mandatory orthographic projection | | | C03/C04 | UNMAPPED |
| 01: two planar cuts, top/bottom corners, constant depth, no unrequested curve/bevel/warp | | | C02/C03/C04 | UNMAPPED |
| 01/02: orthogonal building contact footprints; permitted massing and nonbuilding exceptions | | | L07/C04 | UNMAPPED |
| 01/04: roof surfaces/joins, wall tops, supports and grounding | | | C04/L05 | UNMAPPED |
| 02: two rear blocking directions, no unintended third path | | | L01/L02 | UNMAPPED |
| 02: one functional exit per direction; selected position/form/state/entrance role | | | L02 | UNMAPPED |
| 02: each approach, width/height/turn/transition/opening/post-clear volume; central combat floor | | | L03 | UNMAPPED |
| 01/02: open front and legible base/footing/line evidence | | | C01/C04/L04/L05/L07 | UNMAPPED |
| 02: planned barrier height, props outside routes, connected levels and XY stairs/ramps | | | L03/L05 + 3D height validation separate | UNMAPPED |
| 01/02: exposed room depth/entry/internal circulation or justified N/A | | | L06 | UNMAPPED |
| 04: per-building human entry, role and credible grounding; nonbuilding exception | | | W04/L05 | UNMAPPED |
| 04: per-building functional roof40~80%, support/connections/space; nonbuilding exception | | | W05/C04/L05 | UNMAPPED |
| 03: large forms/broad color fields/selective wear, material distinctions, restrained detail/reflection/light | | | S01/S02/S03/S04 | UNMAPPED |
| 03/04: age is retained; functional salvaged technology across place; relative machine presence | | | W01/W02/W03 | UNMAPPED |
| 01~04: structural versus art/world reference roles and camera/content exclusions | | | C04/S01~S04/W01~W03 | UNMAPPED |
| 03 supplement scope, M03-12 building-only if used, approved-aspect examples only | | | reference audit + S/W checks | UNMAPPED |
| User: location/time/palette/material/count, active additions/exclusions or edit preservation | | | R01 | UNMAPPED |
| 01/02/04: new place architecture/paving/cutaway, no unrelated prior-scene carryover | | | R01/R02 | UNMAPPED |
| 05: no unrequested people/monsters/text/numbers/arrows/UI; minimal needed signage | | | R01 | UNMAPPED |

## Compiled prompt and execution metadata
- actual_prompt_path: generation_prompt.md
- section_order: STRUCTURE MUST KEEP -> CURRENT SCENE -> ART / REFERENCE ROLES
- exact_saved_text_matches_submitted_prompt: not_submitted
- unresolved_variables_conflicts_or_unmapped_requirements:
- character_count_and_counting_method: not_measured
- utf8_byte_count_and_counting_method: not_measured
- whitespace_word_count_and_counting_method: not_measured
- returned_token_usage_only_if_exposed: unknown
- returned_model_info_only_if_exposed: unknown
- returned_revised_prompt_only_if_exposed: unknown
- prompt_truncation_or_internal_rewrite_evidence: unknown

The compiled file is the intended submitted text, not an unavailable hidden prompt. Counts are metadata, not a token-budget estimate, capacity percentage, or proof of no truncation/compliance.

## Final comparison plan and status
- compare_actual_base_top_bottom_footings_walls_roofs_paving_against_required_orthographic_projection:
- endpoint_or_line_annotations_if_needed_with_pixel_reading_uncertainty:
- final_roof_joins_supports_and_each_exit_state_volume_comparison:
- occluded_critical_evidence_means_UNCERTAIN_not_PASS:
- status: pending_generation

from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
source=ROOT/'outputs/20260910_115606_windows_posters_motorcycle/structure_plan.json'
plan=json.loads(source.read_text(encoding='utf-8'))
plan.update(inherited_plan=str(source.relative_to(ROOT)),edit_type='all existing machinery redesigned within its occupied envelope; architecture, camera, routes and parking invariant',mechanical_redesign_inventory=['left_roof_tank_instrumentation_pumps_power','right_roof_all_units','shop_roof_cooling_awning_motor','white_upper_vent','blue_wall_fans','all_wall_gate_control_boxes','shop_weighing_payment_devices','motorcycle_all_mechanical_modules','cutaway_junctions_and_couplings'],no_new_ground_obstacles=True)
bike=plan['motorcycle']['envelope_including_handlebars_and_stand']
hits=[key for key,a in plan['protected_routes'].items() if all(min(a[k+1],bike[k+1])>max(a[k],bike[k]) for k in (0,2,4))]
assert not hits
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
paths=[ROOT/'outputs/20260910_115606_windows_posters_motorcycle/tiny_shop_windows_posters_motorcycle.png',ROOT/'refs/master03/ldi_10_storefront_style_anchor.png']
refs={'inputs':[{'path':str(p),'role':['edit_target_spatial_invariants_but_machinery_shapes_to_replace','rendering_only'][i],'visually_inspected':True,'submitted':False,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for i,p in enumerate(paths)],'mechanism':'referenced_image_paths','omitted':'M01/M02 existing target preserves geometry; M04 character sources omitted to avoid anchoring unchanged generic industrial machinery, salvage world retained explicitly in prompt','intent':'edit_all_machine_designs'}
(RUN/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'planned_inputs':2,'route_intersections':hits}))


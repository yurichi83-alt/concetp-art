from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
source=ROOT/'outputs/20260910_114238_tiny_shop_balcony/structure_plan.json'
plan=json.loads(source.read_text(encoding='utf-8'))
bike=[11.9,12.75,4.1,6.5,0,1.45]
hits=[key for key,a in plan['protected_routes'].items() if all(min(a[k+1],bike[k+1])>max(a[k],bike[k]) for k in (0,2,4))]
assert not hits
plan.update(inherited_plan=str(source.relative_to(ROOT)),edit_type='additive; preserve existing camera/buildings/base',motorcycle={'count':1,'envelope_including_handlebars_and_stand':bike,'orientation':'parallel to side wall, wheels along Y','protected_route_intersections':hits},facade_edits={'white_building':'one window and one vent on visible second-storey wall; balcony door retained','blue_building':'torn posters and graffiti on side wall ground-floor level facing right gate path'},metric_limit='plan coordinates only, final image separately reviewed')
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
paths=[
 ROOT/'outputs/20260910_114834_balcony_shop_entry_fix/tiny_city_shop_balcony_day.png',
 ROOT/'refs/master04/world_02_heavy_mechanical_arms.png',
 ROOT/'refs/master03/ldi_10_storefront_style_anchor.png']
refs={'inputs':[{'path':str(p),'role':['edit_target','motorcycle_world_design_only','material_style_only'][i],'visually_inspected':True,'submitted':False,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for i,p in enumerate(paths)],'mechanism':'referenced_image_paths','omitted':'M01/M02 and previous schematic duplicated existing target geometry; current edit plan checked separately','master_version':'2.2'}
(RUN/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'route_intersections':hits,'planned_inputs':3}))


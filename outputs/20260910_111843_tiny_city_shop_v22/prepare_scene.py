from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
old=(ROOT/'outputs/20260910_110250_hardware_appliance_v22_test/prepare_scene.py').read_text(encoding='utf-8')
prefix=old[:old.index('base=(0,16')]
renderer=old[old.index('# Render the new 3D schematic'):old.index('routes=[')]
scene="""
box(0,16,0,16,-1.1,0,('#756f62','#605e54','#b4b2a0'))
for n in range(2,16,2):
 line([(n,0,.01),(n,16,.01)],'#969b8c')
 line([(0,n,.01),(16,n,.01)],'#969b8c')
plane(0,8,11,14,.02,'#9bb7a9')
plane(13,15.5,0,14,.02,'#9bb7a9')
for c,d in [(0,11),(14,16)]:
 box(.45,.8,c,d,0,3)
box(.45,.8,11,14,2.65,3)
for a,b in [(0,13),(15.5,16)]:
 box(a,b,.45,.8,0,3)
box(13,15.5,.45,.8,2.65,3)
# Adjacent larger city buildings, with a narrow low shop tightly infilling the gap.
box(1,5,1,9,0,6.0,('#9e9f8e','#898c7b','#c1c4ad'))
box(8,11.8,1,8.8,0,6.4,('#859ca0','#718c91','#a3b9b8'))
# Windows and enclosed service panels are not entrances.
for z in [1.3,4.1]:
 for x in [1.6,3.3]:
  box(x,x+1.1,9,9.04,z,z+1.25,('#637c7b','#52696b','#809492'))
for z in [1.2,4.2]:
 for x in [8.6,10.2]:
  box(x,x+1.0,8.8,8.84,z,z+1.3,('#728082','#576e76','#899b9e'))
box(10.9,11.8,5.5,8.5,2.9,4.0,('#8d8e7b','#757967','#b1b099'))
# Tiny shop floor and side/back walls, clear entrance rather than a closed display cabinet.
plane(5,8,5,9.2,.035,'#c4b69b')
box(5,8,5,5.2,0,2.75,('#b3a17d','#99856b','#d1bc91'))
box(5,5.2,5,9.2,0,2.75,('#b3a17d','#99856b','#d1bc91'))
box(7.8,8,5,9.2,0,2.75,('#b3a17d','#99856b','#d1bc91'))
box(5,8,5,8.2,2.55,2.75,('#b3a17d','#99856b','#d1bc91'))
box(5,8,8.2,9.65,2.65,2.8,('#a98b5d','#927449','#cba576'))
box(5.25,5.75,7,9.2,0,.9,('#a29878','#8b846b','#c6b994'))
box(5.3,7.6,5.3,5.7,0,1.5,('#889988','#70836f','#a7b69b'))
# A low wall-side prop is outside all circulation zones.
box(11.9,12.35,7.4,8.2,0,1,('#808c84','#6d7c73','#a3aca0'))
# Two different simple subsurface service forms on flat cut faces.
line([(2,16,-.55),(8,16,-.55)],'#769aa0',9)
line([(16,3,-.5),(16,9,-.5)],'#a98c64',8)
"""
exec(compile(prefix+scene+renderer,str(RUN/'prepare_scene.py'),'exec'))
routes={'left':[0,8,11,14],'right':[13,15.5,0,14],'center':[6,13,10,14]}
objects={'left_building':[1,5,1,9],'right_building':[8,11.8,1,8.8],'tiny_shop':[5,8,5,9.65],'small_prop':[11.9,12.35,7.4,8.2]}
collision=lambda a,b: min(a[1],b[1])>max(a[0],b[0]) and min(a[3],b[3])>max(a[2],b[2])
hits=[(r,o) for r,a in routes.items() for o,b in objects.items() if collision(a,b)]
assert not hits,hits
plan={'projection':'one orthographic XYZ basis; renderer preserved from tested geometric schematic, scene replaced','base':[0,16,0,16,-1.1,0],'routes':routes,'building_and_prop_footprints':objects,'heights':[6.0,6.4,2.75],'walk_volume_height':2.5,'shop_clear_aisle':[5.9,7.6,5.9,9.2],'route_collisions':hits,'frame':'single cubic virtual volume','numeric_scope':'this scene only, final raster not metric-certified','guide_role':'new current-run coordinate diagram; not master promotion'}
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
ids=['M02-01','M01-01','M03-10','M04-02']
refs=[{'id':'structure_plan','path':str(RUN/'structure_plan.png'),'role':'primary scene geometry, no diagram coloring in art','submitted':False}]
for key in ids:
 r=next(x for x in manifest['references'] if x['id']==key)
 assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
 refs.append({'id':key,'path':str(ROOT/r['path']),'role':r['use_only'],'exclude':r['exclude'],'submitted':False})
(RUN/'references.json').write_text(json.dumps({'inputs':refs,'limit':5,'mechanism':'referenced_image_paths','omitted':'extra style images and all previous generated results; fresh location design'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'route_collisions':hits,'guide':str(RUN/'structure_plan.png')}))


from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
old=(ROOT/'outputs/20260910_110250_hardware_appliance_v22_test/prepare_scene.py').read_text(encoding='utf-8')
prefix=old[:old.index('base=(0,16')]
renderer=old[old.index('# Render the new 3D schematic'):old.index('routes=[')]
scene="""
box(0,16,0,16,-1.6,0,('#78644d','#63513f','#a6a49a'))
for n in range(2,16,2):
 line([(n,0,.01),(n,16,.01)],'#898f88')
 line([(0,n,.01),(16,n,.01)],'#898f88')
for c,d in [(0,11),(14,16)]:box(.45,.8,c,d,0,2.9)
box(.45,.8,11,14,2.55,2.9)
for a,b in [(0,13),(15.5,16)]:box(a,b,.45,.8,0,2.9)
box(13,15.5,.45,.8,2.55,2.9)
# Abandoned narrow two-storey service block and a broad low derelict loading hall.
box(.9,4.5,.9,9,0,5.6,('#939586','#7d8070','#b1b49a'))
box(6,11.5,.9,6.6,0,3.5,('#947c68','#806657','#b69a7d'))
# Human entrances closed; no open shallow pseudo-interior.
box(2.8,4.0,9,9.07,0,2.3,('#5e7270','#405957','#83958a'))
box(8.2,10.1,6.6,6.67,0,2.7,('#8d9180','#717967','#b2b29a'))
for z in [.4,.9,1.4,1.9,2.4]:line([(8.25,6.69,z),(10.05,6.69,z)],'#526967',3)
for z in [1,3.7]:
 box(1.3,2.4,9,9.05,z,z+1.3,('#596b63','#40594e','#839788'))
# Side wall window band and structural repair brace.
box(4.5,4.56,3.1,6.8,3.65,4.8,('#657c78','#506965','#839a91'))
line([(4.6,7.3,.3),(4.6,7.3,5.3)],'#626d67',9)
# Bins stay beside doors, not in gate approaches.
box(1.0,2.4,9.3,10.4,0,1.1,('#75846c','#5c6c56','#9caa8e'))
box(1.0,2.4,9.3,10.4,1.1,1.25,('#7f8c78','#65745f','#a8b29a'))
box(6.2,7.35,6.85,7.95,0,1.2,('#81897d','#657163','#a7af9c'))
box(6.25,7.3,8.05,8.7,0,.35,('#746f62','#5e5c51','#938b7b'))
# Rooftop footprint assemblies, conventional industrial salvage (not cassette futurism).
for a,b,c,d,h in [(1.3,3,1.3,6.3,.65),(3.2,4.2,1.3,6.3,.5),(1.3,3.8,7,8.5,.4)]:
 box(a,b,c,d,5.6,5.6+h,('#808e83','#69796d','#a7b09d'))
for a,b,c,d,h in [(6.4,9.5,1.3,4.2,.6),(9.8,11.1,1.3,5.9,.55),(6.4,8.8,4.7,5.9,.45)]:
 box(a,b,c,d,3.5,3.5+h,('#8b9388','#718073','#adb5a0'))
# Flat litter across pavement: footprint-only marks, no tall route obstruction.
for x,y,a,b in [(5.3,9.6,.3,.45),(6.4,11.3,.6,.3),(8.1,12.4,.4,.45),(10.7,10.4,.4,.3),(11.4,14,.5,.25),(4.0,12.5,.35,.5),(2.3,13.4,.5,.2),(13.8,8.8,.4,.3),(14,4.3,.35,.5),(8.7,8.3,.4,.3),(6,6.8,.25,.35),(10,14.4,.5,.3)]:
 plane(x,x+a,y,y+b,.025,'#c5b899')
line([(16,1,-.65),(16,9,-.65)],'#a49466',10)
line([(3,16,-.9),(14,16,-.9)],'#779b9f',12)
"""
exec(compile(prefix+scene+renderer,str(RUN/'prepare_scene.py'),'exec'))
roofs={'left':{'area':3.6*8.1,'occupied':8.5+5+3.75},'right':{'area':5.5*5.7,'occupied':8.99+5.98+2.88}}
for r in roofs.values():
 r['fraction']=r['occupied']/r['area'];assert .4<=r['fraction']<=.8
routes={'left':[0,8,11,14,0,2.4],'right':[13,15.5,0,14,0,2.4],'center':[6,13,9.2,14,0,2.4]}
objects={'left_building':[.9,4.5,.9,9,0,5.6],'right_building':[6,11.5,.9,6.6,0,3.5],'left_bin':[1,2.4,9.3,10.4,0,1.25],'right_bin':[6.2,7.35,6.85,7.95,0,1.2],'bag_zone':[6.25,7.3,8.05,8.7,0,.6]}
hits=[(r,o) for r,a in routes.items() for o,b in objects.items() if all(min(a[k+1],b[k+1])>max(a[k],b[k]) for k in (0,2,4))]
assert not hits,hits
plan={'base':[0,16,0,16,-1.6,0],'projection':'one common orthographic XYZ basis','roof_coverage_plan':roofs,'protected_routes':routes,'objects':objects,'route_collisions':hits,'litter':'thin paper/flattened packaging on floor; bags and high piles confined to wall-side zones','entrances':'left closed human door, right closed full-height shutter, clear approaches','numeric_limit':'plan only; final raster separately reviewed','baseline_cassette_futurism':False}
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
refs=[{'id':'structure_guide','path':str(RUN/'structure_plan.png'),'role':'scene geometry guide only','submitted':False}]
for key in ['M02-01','M01-01','M03-10','M04-02']:
 r=next(x for x in manifest['references'] if x['id']==key)
 assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
 refs.append({'id':key,'path':str(ROOT/r['path']),'role':r['use_only'],'exclude':r['exclude'],'submitted':False})
(RUN/'references.json').write_text(json.dumps({'inputs':refs,'mechanism':'referenced_image_paths','omitted':'previous generated city-store images and optional duplicate style sources; new alley design'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'route_collisions':hits,'roof_fractions':{k:v['fraction'] for k,v in roofs.items()}}))


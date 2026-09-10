from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
old=(ROOT/'outputs/20260910_110250_hardware_appliance_v22_test/prepare_scene.py').read_text(encoding='utf-8')
prefix=old[:old.index('base=(0,16')]
renderer=old[old.index('# Render the new 3D schematic'):old.index('routes=[')]
scene="""
box(0,16,0,16,-1.6,0,('#796d59','#665a48','#aba99a'))
# Broad strata shown within both flat cuts, not exterior sealed panels.
poly([(16,0,-.25),(16,16,-.25),(16,16,-1.3),(16,0,-1.3)],'#8e7957')
poly([(0,16,-.25),(16,16,-.25),(16,16,-1.3),(0,16,-1.3)],'#77613f')
for n in range(2,16,2):
 line([(n,0,.01),(n,16,.01)],'#95978c')
 line([(0,n,.01),(16,n,.01)],'#95978c')
for c,d in [(0,11),(14,16)]: box(.45,.8,c,d,0,2.9)
box(.45,.8,11,14,2.55,2.9)
for a,b in [(0,13),(15.5,16)]: box(a,b,.45,.8,0,2.9)
box(13,15.5,.45,.8,2.55,2.9)
box(1,5,1,9,0,5.3,('#a3a191','#8c8a77','#c2c0a8'))
box(8,11.8,1,8.8,0,5.6,('#879fa1','#728a8e','#a3b9b5'))
# Each large building has a readable ground-level entrance, distinct from gates.
box(2.2,3.5,9,9.06,0,2.35,('#556b6e','#3d565d','#7d8c88'))
line([(3.2,9.08,.95),(3.2,9.08,1.2)],'#d1bc87',4)
box(9.0,10.95,8.8,8.86,0,2.5,('#928574','#796b5e','#b4a48c'))
for z in [.4,.8,1.2,1.6,2.0]: line([(9.05,8.88,z),(10.9,8.88,z)],'#495d64',3)
# Second-floor balcony on left building; door, slab, rail and support.
box(2.2,3.5,9,9.04,2.85,5.05,('#63777a','#4b636d','#829590'))
box(1.3,4.8,9,10.3,2.72,2.88,('#738689','#596e78','#98a5a5'))
for x in [1.4,2.1,2.8,3.5,4.2,4.7]:
 line([(x,10.25,2.9),(x,10.25,3.85)],'#bac0aa',4)
line([(1.35,10.25,3.85),(4.75,10.25,3.85)],'#bac0aa',5)
for x in [1.35,4.75]:
 line([(x,9,3.85),(x,10.25,3.85)],'#bac0aa',5)
 line([(x,9.03,2.1),(x,10.1,2.72)],'#647b81',8)
for x in [8.5,10.2]: box(x,x+1.15,8.8,8.84,3.5,4.8)
# Tiny grocery between both larger buildings.
plane(5,8,5,9.2,.03,'#c9b48e')
box(5,8,5,5.2,0,2.65,('#b59c72','#9c8261','#d6bb8e'))
box(5,5.2,5,9.2,0,2.65)
box(7.8,8,5,9.2,0,2.65)
box(5,8,5,9.2,2.5,2.65,('#b59c72','#9c8261','#d6bb8e'))
box(5.25,5.75,6.6,9.0,0,.85,('#a29878','#8b846b','#c6b994'))
box(5.3,7.6,5.3,5.7,0,1.4)
box(5,8,9.2,9.6,2.45,2.6,('#b9a177','#a08660','#ddc296'))
# Rooftop functional footprints: each separately 40-80%.
for a,b,c,d,h in [(1.3,3.3,1.5,5.5,.75),(3.5,4.7,1.5,5.5,.55),(1.3,3.3,6,8.5,.6)]:
 box(a,b,c,d,5.3,5.3+h,('#85988b','#6c8074','#a9b5a3'))
for a,b,c,d,h in [(8.3,11.4,1.4,4.5,.75),(8.3,10.5,5,7.8,.55)]:
 box(a,b,c,d,5.6,5.6+h,('#9a9880','#7e836c','#bcbc9d'))
for a,b,c,d,h in [(5.2,6.55,6.1,8.5,.55),(6.7,7.8,6.1,8.5,.4)]:
 box(a,b,c,d,2.65,2.65+h,('#8b9a91','#6d8079','#b0bba7'))
line([(16,2,-.8),(16,13,-.8)],'#bda265',12)
line([(2,16,-.9),(13,16,-.9)],'#7eabb0',12)
"""
exec(compile(prefix+scene+renderer,str(RUN/'prepare_scene.py'),'exec'))
roofs={
 'left':{'area':32,'footprints':[[1.3,3.3,1.5,5.5],[3.5,4.7,1.5,5.5],[1.3,3.3,6,8.5]]},
 'right':{'area':3.8*7.8,'footprints':[[8.3,11.4,1.4,4.5],[8.3,10.5,5,7.8]]},
 'shop':{'area':3*4.2,'footprints':[[5.2,6.55,6.1,8.5],[6.7,7.8,6.1,8.5]]}}
for roof in roofs.values():
 roof['fraction']=sum((b-a)*(d-c) for a,b,c,d in roof['footprints'])/roof['area']
 assert .4<=roof['fraction']<=.8
routes={'left':[0,8,11,14,0,2.4],'right':[13,15.5,0,14,0,2.4],'center':[6,13,10,14,0,2.4]}
objects={'left_building':[1,5,1,9,0,5.3],'right_building':[8,11.8,1,8.8,0,5.6],'shop':[5,8,5,9.6,0,3.2],'balcony':[1.3,4.8,9,10.3,2.1,3.85]}
hits=[(r,o) for r,a in routes.items() for o,b in objects.items() if all(min(a[k+1],b[k+1])>max(a[k],b[k]) for k in (0,2,4))]
assert not hits,hits
plan={'projection':'single orthographic XYZ basis from depth-buffer renderer','base':[0,16,0,16,-1.6,0],'roofs':roofs,'doors':{'left':'ground door x2.2..3.5 y9, second-floor balcony door','right':'ground roller shutter x9..10.95 y8.8','shop':'open front y9.2, clear aisle x5.9..7.6'},'protected_routes':routes,'objects':objects,'route_collisions':hits,'notes':'current-run geometry only; roof fractions are plan footprints, not final pixel measurement; total planned heights <=6.35'}
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
refs=[{'path':str(RUN/'structure_plan.png'),'id':'scene_structure','role':'geometry, doors, balcony, roof coverage only, schematic not art','submitted':False}]
for key in ['M02-01','M01-01','M03-10','M04-02']:
 r=next(x for x in manifest['references'] if x['id']==key)
 assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
 refs.append({'path':str(ROOT/r['path']),'id':key,'role':r['use_only'],'exclude':r['exclude'],'submitted':False})
(RUN/'references.json').write_text(json.dumps({'inputs':refs,'limit':5,'mechanism':'referenced_image_paths','omitted':'previous generated images and optional stylistic duplicates'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'roof_plan_fractions':{k:v['fraction'] for k,v in roofs.items()},'collisions':hits}))


from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
old=(ROOT/'outputs/20260910_110250_hardware_appliance_v22_test/prepare_scene.py').read_text(encoding='utf-8')
prefix=old[:old.index('base=(0,16')]
renderer=old[old.index('# Render the new 3D schematic'):old.index('routes=[')]
scene="""
box(0,16,0,16,-1.6,0,('#79644e','#67503c','#a6a293'))
for n in range(2,16,2):
 line([(n,0,.01),(n,16,.01)],'#85897f')
 line([(0,n,.01),(16,n,.01)],'#85897f')
# Planar exposed earth with concrete piers, pipes recessed inside cuts.
for a in [1,5.4,10.4,15.2]:
 poly([(a,16,-1.6),(a+.55,16,-1.6),(a+.55,16,0),(a,16,0)],'#95958a')
 poly([(16,a,-1.6),(16,a+.55,-1.6),(16,a+.55,0),(16,a,0)],'#95958a')
for a in [2,7,12]:
 poly([(a,16,-1.4),(a+1.5,16,-1.35),(a+1.2,16,-.9),(a+.3,16,-.95)],'#886d4d')
 poly([(16,a,-1.4),(16,a+1.5,-1.35),(16,a+1.2,-.9),(16,a+.3,-.95)],'#967a55')
line([(16,1,-.65),(16,15,-.65)],'#6e7774',10)
line([(1,16,-.65),(15,16,-.65)],'#927151',10)
for c,d in [(0,11),(14,16)]:box(.45,.8,c,d,0,2.9)
box(.45,.8,11,14,2.55,2.9)
for a,b in [(0,13),(15.5,16)]:box(a,b,.45,.8,0,2.9)
box(13,15.5,.45,.8,2.55,2.9)
# L-shaped stepped left building. Real setbacks, not a simple tall box.
box(1,5,1,8,0,3.2,('#977e6d','#7b6556','#b6a08a'))
box(5,6.5,1,4,0,3.2,('#977e6d','#7b6556','#b6a08a'))
box(1,4.2,1,4.4,3.2,5,('#947f6e','#796452','#bca38c'))
# Right pentagonal footprint with deliberately chamfered BUILDING corner only.
v=[(7,1),(11.8,1),(11.8,5),(10,7),(7,7)]
for i in [1,2,3]:
 a,b=v[i],v[(i+1)%5]
 poly([(a[0],a[1],0),(b[0],b[1],0),(b[0],b[1],4.1),(a[0],a[1],4.1)],'#758c87' if i!=3 else '#657e79')
poly([(x,y,4.1) for x,y in v],'#9aafa4')
# Asymmetric sloping roof on rear part, plus low front service terrace.
poly([(7,1,4.1),(11.8,1,4.1),(11.8,4.4,4.1),(7,4.4,5.1)],'#8c9d96')
poly([(7,1,4.1),(7,4.4,5.1),(7,4.4,4.1)],'#698077')
poly([(7,4.4,4.1),(11.8,4.4,4.1),(7,4.4,5.1)],'#70857e')
# Human doors and an integrated 20%-intent vertical equipment core in left building.
box(2,3.3,8,8.07,0,2.3,('#566964','#3c534c','#7e9084'))
box(7.6,8.9,7,7.07,0,2.4,('#63706c','#495b55','#87988c'))
box(4.3,5.3,4.4,7.7,0,4.25,('#b6b39c','#979580','#d3cab0'))
# Roof equipment occupancy; not literal shape requirements.
for a,b,c,d,z,h in [(1.4,3.8,1.4,3.9,5,.6),(1.4,3.7,4.9,6.5,3.2,.6),(5.2,6.2,1.4,3.6,3.2,.7),(3.8,4.6,6.8,7.6,3.2,.4)]:
 box(a,b,c,d,z,z+h,('#b4b098','#95937e','#d2cab0'))
for a,b,c,d,z,h in [(7.4,9.2,1.4,3.3,4.95,.5),(9.5,11.3,1.4,3.6,4.45,.5),(7.4,9.6,4.8,6.4,4.1,.55)]:
 box(a,b,c,d,z,z+h,('#b7b39c','#95977e','#d5cdb4'))
# Wallside bins/litter remain outside protected walkways.
box(1.1,2.7,8.35,9.5,0,1.25,('#71816d','#55674f','#9aa68b'))
box(9.2,10.2,7.35,8.4,0,1.2,('#82745b','#6b5d48','#a69a7b'))
box(2.85,3.4,8.6,9.35,0,.55,('#6e6f62','#515b4b','#92917e'))
for x,y in [(4,9),(6,9),(8,10),(9,11.4),(10.5,12.8),(3,12),(6,13.4),(12,9.5),(13.8,5.5),(5,14)]:
 plane(x,x+.45,y,y+.35,.02,'#cbbf9f')
"""
exec(compile(prefix+scene+renderer,str(RUN/'prepare_scene.py'),'exec'))
routes={'left':[0,8,11,14,0,2.4],'right':[13,15.5,0,14,0,2.4],'center':[5.6,13,9.8,14,0,2.4]}
objects={'left_main':[1,5,1,8,0,5],'left_wing':[5,6.5,1,4,0,3.2],'machine_core':[4.3,5.3,4.4,7.7,0,4.25],'right_bound':[7,11.8,1,7,0,5.1],'bin_left':[1.1,2.7,8.35,9.5,0,1.25],'bin_right':[9.2,10.2,7.35,8.4,0,1.2],'bags':[2.85,3.4,8.6,9.35,0,.55]}
hits=[(r,o) for r,a in routes.items() for o,b in objects.items() if all(min(a[k+1],b[k+1])>max(a[k],b[k]) for k in (0,2,4))]
assert not hits,hits
# Each roof has equipment plus functional sloping/raised service elements; union plan, no shadows/grime.
roofs={'left':{'roof_horizontal_area':32.5,'functional_occupied_plan':17.9},'right':{'roof_horizontal_area':27,'functional_occupied_plan':15.2}}
for v in roofs.values():
 v['fraction']=v['functional_occupied_plan']/v['roof_horizontal_area'];assert .4<=v['fraction']<=.8
plan={'base':[0,16,0,16,-1.6,0],'projection':'single orthographic XYZ','buildings':'left L footprint with stepped upper volume; right pentagon with diagonal corner and asymmetric roof','roof_coverage':roofs,'routes':routes,'objects':objects,'route_collisions':hits,'mechanical_fraction':'left body about20% visual target continuing previous request; integrated core not just roof equipment','entrances':'left y8 x2..3.3, right y7 x7.6..8.9','limits':'planning values only; final image visually checked; sloped-roof equipment must gain credible supports in final art'}
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
src=Path('C:/Users/YEONHE~1/AppData/Local/Temp/codex-clipboard-14032519-644e-411a-9b9e-89a6a8231741.png')
dst=RUN/'user_cassette_reference.png';shutil.copy2(src,dst)
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8-sig'))
refs=[{'path':str(RUN/'structure_plan.png'),'role':'new geometry guide; equipment shapes illustrative only','submitted':False},{'path':str(dst),'role':'explicit user cassette machinery design reference only, no full scene/camera copy or master promotion','submitted':False}]
for key in ['M02-01','M01-01','M03-10']:
 r=next(x for x in manifest['references'] if x['id']==key)
 assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
 refs.append({'id':key,'path':str(ROOT/r['path']),'role':r['use_only'],'exclude':r['exclude'],'submitted':False})
(RUN/'references.json').write_text(json.dumps({'inputs':refs,'mechanism':'referenced_image_paths','omitted':'M04 standalone image omitted under5 input cap; user reference supplies reclaimed advanced machine forms, M04 text rules preserved. Prior output images excluded.'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'collisions':hits,'roof_fractions':[v['fraction'] for v in roofs.values()]}))


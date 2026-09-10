from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
old=(ROOT/'outputs/20260910_110250_hardware_appliance_v22_test/prepare_scene.py').read_text(encoding='utf-8')
prefix=old[:old.index('base=(0,16')]
renderer=old[old.index('# Render the new 3D schematic'):old.index('routes=[')]
scene="""
box(0,16,0,16,-1.5,0,('#756955','#635946','#a2a193'))
for n in range(2,16,2):
 line([(n,0,.01),(n,16,.01)],'#898f88')
 line([(0,n,.01),(16,n,.01)],'#898f88')
for c,d in [(0,11),(14,16)]:box(.45,.8,c,d,0,2.9)
box(.45,.8,11,14,2.55,2.9)
for a,b in [(0,13),(15.5,16)]:box(a,b,.45,.8,0,2.9)
box(13,15.5,.45,.8,2.55,2.9)
# New low elongated workshop left, tall rear utility block right.
box(.9,5.5,.9,8,0,3.8,('#877f67','#726953','#a49a7c'))
box(6.3,10.7,.9,6.8,0,5.5,('#668381','#526e6c','#8ca29b'))
# Full-height machinery occupies the rightmost fifth of this building envelope.
box(10.7,11.8,.9,6.8,0,5.5,('#69737a','#4c5962','#8e999e'))
for z in [.5,1.7,2.9,4.1]:
 box(10.8,11.7,6.8,6.88,z,z+.8,('#7c7666','#696150','#a2997e'))
# Human entrances on front facades, separated from mechanical service panels.
box(3.5,4.9,8,8.07,0,2.45,('#727968','#535c4d','#969c87'))
box(7.1,8.4,6.8,6.87,0,2.35,('#606f77','#45525e','#809297'))
box(1.3,3,8,8.04,1.4,2.7,('#5e6963','#404e49','#869589'))
box(6.8,9.8,6.8,6.85,3.4,4.7,('#617674','#425d5a','#8a9e98'))
# Supportable roof equipment footprint envelopes only; final forms diverse.
for a,b,c,d,h in [(1.3,3.4,1.4,4.6,.8),(3.7,5.1,1.4,4.6,.6),(1.3,4.8,5.2,7.5,.45)]:
 box(a,b,c,d,3.8,3.8+h,('#7b8067','#626750','#a1a087'))
for a,b,c,d,h in [(6.7,9.2,1.3,4.0,.7),(9.5,11.3,1.3,4,.8),(8.7,11.2,4.5,6.3,.5)]:
 box(a,b,c,d,5.5,5.5+h,('#757987','#5c6372','#a1a4ab'))
# Wide compacting dumpster left; cylindrical bin final design fits right box.
box(1.15,2.95,8.3,9.65,0,1.4,('#737c64','#58664d','#979d80'))
box(9.0,10.1,7.15,8.3,0,1.3,('#8a6c56','#775942','#af8c6c'))
box(3.05,3.45,8.5,9.35,0,.6,('#6e7165','#585e52','#939587'))
box(10.15,10.8,7.2,8.3,0,.6,('#6e7165','#585e52','#939587'))
for x,y,a,b in [(4.9,9.6,.4,.45),(6.4,11.3,.6,.3),(8.1,12.4,.4,.45),(10.7,10.4,.4,.3),(11.4,14,.5,.25),(4,12.5,.35,.5),(2.3,13.4,.5,.2),(13.8,8.8,.4,.3),(14,4.3,.35,.5),(8.7,8.9,.4,.3),(6,8.8,.25,.35),(10,14.4,.5,.3)]:
 plane(x,x+a,y,y+b,.025,'#c9bd9f')
line([(16,1,-.6),(16,9,-.6)],'#879da3',11)
line([(3,16,-1.0),(14,16,-1.0)],'#9e8d67',11)
"""
exec(compile(prefix+scene+renderer,str(RUN/'prepare_scene.py'),'exec'))
roofs={'left':{'area':4.6*7.1,'occupied':2.1*3.2+1.4*3.2+3.5*2.3},'right':{'area':5.5*5.9,'occupied':2.5*2.7+1.8*2.7+2.5*1.8}}
for r in roofs.values():
 r['fraction']=r['occupied']/r['area'];assert .4<=r['fraction']<=.8
routes={'left':[0,8,11,14,0,2.4],'right':[13,15.5,0,14,0,2.4],'center':[5.6,13,9.8,14,0,2.4]}
objects={'left_building':[.9,5.5,.9,8,0,3.8],'right_building':[6.3,11.8,.9,6.8,0,5.5],'left_bin':[1.15,2.95,8.3,9.65,0,1.4],'right_bin':[9,10.1,7.15,8.3,0,1.3],'bags_left':[3.05,3.45,8.5,9.35,0,.6],'bags_right':[10.15,10.8,7.2,8.3,0,.6]}
hits=[(r,o) for r,a in routes.items() for o,b in objects.items() if all(min(a[k+1],b[k+1])>max(a[k],b[k]) for k in (0,2,4))]
assert not hits,hits
plan={'base':[0,16,0,16,-1.5,0],'projection':'common orthographic XYZ basis from deterministic renderer','roofs':roofs,'protected_routes':routes,'objects':objects,'collisions':hits,'mechanical_building':'right block rightmost full-height fifth, 1.1/5.5 width = 20% envelope volume; distinct from roof occupancy','entrances':'left x3.5..4.9 at y8, right x7.1..8.4 at y6.8, clear in front','numeric_limit':'planned envelope ratio and footprints only; final image separately visually reviewed','new_generation':True,'previous_art_inputs':False}
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8-sig'))
refs=[{'id':'structure_guide','path':str(RUN/'structure_plan.png'),'role':'new geometry guide only, boxes are not machine shape targets','submitted':False}]
for key in ['M02-01','M01-01','M03-10','M04-02']:
 r=next(x for x in manifest['references'] if x['id']==key)
 assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
 refs.append({'id':key,'path':str(ROOT/r['path']),'role':r['use_only'],'exclude':r['exclude'],'submitted':False,'sha256':r['sha256']})
(RUN/'references.json').write_text(json.dumps({'inputs':refs,'mechanism':'referenced_image_paths','omitted':'prior generated alley images excluded; fresh cassette-first design, not an edit'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'route_collisions':hits,'roof_fractions':{k:v['fraction'] for k,v in roofs.items()},'machine_body_fraction':1.1/5.5}))


from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[2]; RUN=Path(__file__).resolve().parent
renderer_source=(ROOT/'outputs/20260910_110250_hardware_appliance_v22_test/prepare_scene.py').read_text(encoding='utf-8')
prefix=renderer_source[:renderer_source.index('base=(0,16')]
renderer=renderer_source[renderer_source.index('# Render the new 3D schematic'):renderer_source.index('routes=[')]
scene="""
box(0,16,0,16,-1.6,0,('#88735d','#745a44','#b5ab90'))
for n in range(2,16,2):
 line([(n,0,.01),(n,16,.01)],'#8f9384')
 line([(0,n,.01),(16,n,.01)],'#8f9384')
# Square planar cuts: earth, foundations, power routing for recycler and grocery water service.
for a in [1,6.2,11.6,15.35]:
 poly([(a,16,-1.6),(a+.45,16,-1.6),(a+.45,16,0),(a,16,0)],'#b0a08d')
 poly([(16,a,-1.6),(16,a+.45,-1.6),(16,a+.45,0),(16,a,0)],'#b0a08d')
poly([(2,16,-1.35),(5.3,16,-1.35),(5.3,16,-.35),(2,16,-.35)],'#5f6c65')
line([(6,16,-.55),(10,16,-.55),(10,16,-1.1),(15,16,-1.1)],'#766b57',8)
line([(16,.8,-.65),(16,14.8,-.65)],'#6c8988',11)
# Back-left gate position freshly chosen; no overhead gate frame.
for c,d in [(0,10.4),(13.2,16)]:box(.25,.55,c,d,0,2.3)
box(.6,.77,9.1,10.3,0,2.2) # gate leaf stowed flush outside opening
# Back-right exit is intermediate alley between shops, NOT a duplicate frame.
for a,b in [(0,6.1),(8.7,16)]:box(a,b,.25,.55,0,2.3)
# Scrap dealer: two equal length connected sections, one full-volume recycling mechanism.
box(.7,5.8,.7,4.6,0,3.6,('#557b75','#3f645d','#7f9690'))
box(.7,5.8,4.6,8.5,0,3.6,('#a78264','#8b684c','#c1a17d'))
# Large machine chamber inset diagram: feed opening raised, not a walk-through.
poly([(5.81,1.15,1),(5.81,4.05,1),(5.81,4.05,3.1),(5.81,1.15,3.1)],'#354f4e')
# Human door of scrapyard facing open center, CLOSED decorative.
poly([(5.81,6.45,0),(5.81,7.7,0),(5.81,7.7,2.35),(5.81,6.45,2.35)],'#536054')
# Grocery L footprint: main shop and lower end storage wing.
box(9,15.6,.7,5.7,0,3.4,('#beaa76','#a39368','#d3c797'))
box(12.8,15.6,5.7,7.2,0,2.25,('#ae9b70','#908164','#c3b58c'))
# Closed glass human entry and product window facing courtyard, no extra map exit.
poly([(9.45,5.71,0),(10.75,5.71,0),(10.75,5.71,2.35),(9.45,5.71,2.35)],'#687f76')
poly([(11,5.71,.7),(12.55,5.71,.7),(12.55,5.71,2.15),(11,5.71,2.15)],'#667964')
box(11.05,12.5,5.82,6.55,0,.65,('#9a8b5b','#7c7045','#c2ae73'))
box(9.2,12.7,5.65,6.65,2.45,2.58,('#8c8663','#787655','#aaa17b'))
# Full roof envelope coverage 54 percent / 60 percent with supports.
for a,b,c,d,z,h in [(1.1,4.9,1.1,4.1,3.6,.9),(1.2,4.8,5,7.8,3.6,.65)]:
 box(a,b,c,d,z,z+h,('#74817c','#556964','#9caaa0'))
# chimney on a supported block within recycler roof envelope.
box(1.4,2.45,1.5,2.55,4.5,6.05,('#837361','#685744','#a2927d'))
box(1.2,2.65,1.3,2.75,6.05,6.2,('#736451','#61503f','#96826b'))
for a,b,c,d,z,h in [(9.4,13,1.1,4.8,3.4,.7),(13.3,15.2,1.1,4.8,3.4,.6),(13.1,15.2,5.95,6.95,2.25,.65)]:
 box(a,b,c,d,z,z+h,('#7f9182','#5d796a','#a9b49b'))
# Scrapyard stock and modified bin outside left gate corridor.
box(1,3,8.85,9.95,0,1.05,('#6e7a74','#536860','#9caaa2'))
box(3.3,5.3,8.85,10,0,1.25,('#637a57','#4b6443','#8fa176'))
# Grocery waste bin at outer wall, outside both routes.
box(14.35,15.4,7.55,8.5,0,1.05,('#9a855c','#7d6e4a','#bca774'))
"""
exec(compile(prefix+scene+renderer,str(RUN/'prepare_scene.py'),'exec'))
buildings={'scrapyard':[(.7,.7),(5.8,.7),(5.8,8.5),(.7,8.5)],'grocery':[(9,.7),(15.6,.7),(15.6,7.2),(12.8,7.2),(12.8,5.7),(9,5.7)]}
edges={n:[abs(a[0]-b[0])<1e-8 or abs(a[1]-b[1])<1e-8 for a,b in zip(p,p[1:]+p[:1])] for n,p in buildings.items()}
assert all(all(v) for v in edges.values())
routes={'left_exit':[0,9.2,10.4,13.2,0,2.4],'right_exit':[6.1,8.7,0,11.2,0,2.4],'center':[6.1,14,8.8,14.8,0,2.4],'scrap_entry_approach':[5.8,8.7,6.3,8.5,0,2.4],'grocery_entry_approach':[8.7,10.9,5.7,8.8,0,2.4]}
obstacles={'scrapyard':[.7,5.8,.7,8.5,0,3.6],'grocery_main':[9,15.6,.7,5.7,0,3.4],'grocery_wing':[12.8,15.6,5.7,7.2,0,2.25],'produce_crates':[11.05,12.5,5.82,6.55,0,.65],'grocery_awning':[9.2,12.7,5.65,6.65,2.45,2.58],'scrap_stock':[1,3,8.85,9.95,0,1.05],'scrap_bin':[3.3,5.3,8.85,10,0,1.25],'grocery_bin':[14.35,15.4,7.55,8.5,0,1.05]}
for c,d in [(0,10.4),(13.2,16)]:obstacles[f'left_boundary_{c}']=[.25,.55,c,d,0,2.3]
for a,b in [(0,6.1),(8.7,16)]:obstacles[f'right_boundary_{a}']=[a,b,.25,.55,0,2.3]
obstacles['stowed_gate']=[.6,.77,9.1,10.3,0,2.2]
intersects=lambda a,b:all(min(a[k+1],b[k+1])>max(a[k],b[k])+1e-8 for k in (0,2,4))
collisions=[(r,o) for r,a in routes.items() for o,b in obstacles.items() if intersects(a,b)]
assert not collisions,collisions
roofs={'scrapyard':{'area':5.1*7.8,'occupied':3.8*3+3.6*2.8,'support':'two coplanar supported roof sections at z3.6; chimney base on recycler equipment'},'grocery':{'area':6.6*5+2.8*1.5,'occupied':3.6*3.7+1.9*3.7+2.1*1,'support':'main flat roof z3.4 and storage flat roof z2.25'}}
for v in roofs.values():v['fraction']=v['occupied']/v['area'];assert .4<=v['fraction']<=.8
plan={'master_version':'2.3','execution_version':'1.4','base':[0,16,0,16,-1.6,0],'projection':'one orthographic XYZ','building_polygons':buildings,'orthogonal_edges':edges,'roofs':roofs,'routes':routes,'obstacles':obstacles,'collisions':collisions,'functional_exits':[{'direction':'back_left_11','position':'y10.4..13.2 nearer end','form':'open gate in scrap boundary, leaf stowed parallel outside opening','state':'open_after_clear','shared_building_entry':False,'connection':'straight empty level lane across boundary and into rear-left continuation'},{'direction':'back_right_1','position':'x6.1..8.7 intermediate','form':'open unframed alley between scrapyard and grocery','state':'open_after_clear','shared_building_entry':False,'connection':'straight level empty space between buildings to rear boundary'}],'building_entries':'closed human door on scrapyard inner facade and grocery glass front entry; both decorative, not map exits','interior':'grocery closed glass-front visible floor aisle and perimeter goods; no exposed walkthrough. Do not fill door with stock.','mechanized_fraction_scrapyard':.5,'mechanization_measure':'equal plan length and same structural height across full building width: integrated full-volume recycler half versus repair office/storage half. Final image approximate visual target, not exact volumetric measurement.','independent_new_generation':True,'cassette_futurism':False,'height_plan_max':6.2,'numeric_scope':'guide only, final visible geometry and circulation need separate inspection'}
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
m=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
refs=[{'path':str(RUN/'structure_plan.png'),'role':'new independent scrapyard/grocery structural guide only','submitted':False,'visually_inspected':False}]
for key in ['M02-01','M01-01','M03-10','M04-02']:
 r=next(v for v in m['references'] if v['id']==key);path=ROOT/r['path'];assert hashlib.sha256(path.read_bytes()).hexdigest()==r['sha256']
 refs.append({'id':key,'path':str(path),'role':r['use_only'],'exclude':r['exclude'],'sha256':r['sha256'],'submitted':False,'visually_inspected':True})
(RUN/'references.json').write_text(json.dumps({'mechanism':'referenced_image_paths','inputs':refs,'inspected_not_submitted':['M03-11','M04-04'],'omission_reason':'five input slots prioritize new geometry, M01/M02, main art and world reference','excluded':'all generated scene outputs, all paired cassette files and guide, prior user cassette reference'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'guide':str(RUN/'structure_plan.png'),'collision_count':len(collisions),'roof_fractions':[v['fraction'] for v in roofs.values()],'scrapyard_full_volume_fraction':.5},ensure_ascii=False))


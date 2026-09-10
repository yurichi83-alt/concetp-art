from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
old=(ROOT/'outputs/20260910_110250_hardware_appliance_v22_test/prepare_scene.py').read_text(encoding='utf-8')
prefix=old[:old.index('base=(0,16')]
renderer=old[old.index('# Render the new 3D schematic'):old.index('routes=[')]
scene="""
box(0,16,0,16,-1.6,0,('#796b57','#65543f','#a7a696'))
for n in range(2,16,2):
 line([(n,0,.01),(n,16,.01)],'#898f85')
 line([(0,n,.01),(16,n,.01)],'#898f85')
# Subsurface section: piers and pipe silhouettes contained on flat planes.
for a in [1,5,9.5,15.3]:
 poly([(a,16,-1.6),(a+.55,16,-1.6),(a+.55,16,0),(a,16,0)],'#95958a')
 poly([(16,a,-1.6),(16,a+.55,-1.6),(16,a+.55,0),(16,a,0)],'#95958a')
for a in [2,6.7,11.3]:
 poly([(a,16,-1.4),(a+2,16,-1.3),(a+1.7,16,-.9),(a+.3,16,-.9)],'#886d4d')
 poly([(16,a,-1.4),(16,a+2,-1.3),(16,a+1.7,-.9),(16,a+.3,-.9)],'#967a55')
line([(16,1,-.6),(16,15,-.6)],'#7b8b89',8)
line([(1,16,-.8),(15,16,-.8)],'#957957',10)
# Back-left boundary function enters through wide ground-floor building passage at y5..7.8.
for c,d in [(0,5),(7.8,16)]:box(.3,.65,c,d,0,2.45)
# Back-right functional exit is an unframed open alley between tank fence and small building.
for a,b in [(0,9.5),(12.5,16)]:box(a,b,.3,.65,0,2.35)
# One stepped abandoned through-building, orthogonal blocks. Passage truly empty.
box(.8,5.5,.8,5,0,4.8,('#7e8b89','#647b75','#a9b3a3'))
box(.8,5.5,7.8,9.5,0,3.0,('#7e8b89','#647b75','#a9b3a3'))
box(.8,5.5,5,7.8,2.65,4.8,('#7e8b89','#647b75','#a9b3a3'))
# Small standalone derelict utility hut at right; closed human door is decorative.
box(12.8,15.6,.8,6,0,3.3,('#ab916f','#947b5b','#c5af8d'))
box(13.35,14.55,6,6.05,0,2.25,('#676f67','#4c5c51','#909886'))
# Large tank is a nonbuilding boundary prop; octagonal cylinder guide.
cx,cy,r=7.6,2.6,1.5
vv=[(cx+r*math.cos(i*math.pi/4),cy+r*math.sin(i*math.pi/4)) for i in range(8)]
for i in range(8):
 a,b=vv[i],vv[(i+1)%8]
 poly([(a[0],a[1],0),(b[0],b[1],0),(b[0],b[1],3.5),(a[0],a[1],3.5)],'#8f9991')
poly([(x,y,3.5) for x,y in vv],'#b7bca7')
# Roof equipment envelopes: varied form in final art, all on flat supported surfaces.
for a,b,c,d,z,h in [(1.25,3.6,1.2,4.5,4.8,.65),(3.85,5.1,1.2,4.5,4.8,.55),(1.25,4.8,5.2,7.4,4.8,.5),(1.15,4.95,8.05,9.15,3,.55)]:
 box(a,b,c,d,z,z+h,('#738b96','#526e7b','#97adb2'))
for a,b,c,d,z,h in [(13.15,15.2,1.2,3.8,3.3,.65),(13.15,15.2,4.2,5.5,3.3,.45)]:
 box(a,b,c,d,z,z+h,('#8c8b7a','#706f60','#b1ac93'))
# Bins placed at low wing and hut, outside either exit approach.
box(1.5,3.3,9.8,10.8,0,1.2,('#64795f','#4e624a','#899a7c'))
box(14,15.25,6.35,7.45,0,1.25,('#947b60','#776048','#b49c79'))
box(3.55,4.5,9.85,10.6,0,.5,('#777568','#585c4e','#959584'))
for x,y in [(5.5,10.3),(6.2,12.4),(8.2,11.2),(10.5,12.9),(12.5,9.2),(3.6,12.5),(7.4,8.8),(9.8,6.8),(14,9),(11,14.3)]:
 plane(x,x+.5,y,y+.32,.022,'#d4c8a9')
"""
exec(compile(prefix+scene+renderer,str(RUN/'prepare_scene.py'),'exec'))
buildings={'through_block_back':[(.8,.8),(5.5,.8),(5.5,5),(.8,5)],'through_block_front':[(.8,7.8),(5.5,7.8),(5.5,9.5),(.8,9.5)],'right_hut':[(12.8,.8),(15.6,.8),(15.6,6),(12.8,6)]}
edgecheck={}
for name,v in buildings.items():
 flags=[abs(a[0]-b[0])<1e-8 or abs(a[1]-b[1])<1e-8 for a,b in zip(v,v[1:]+v[:1])]
 assert all(flags);edgecheck[name]=flags
routes={'left_passage':[0,6.4,5,7.8,0,2.4],'left_approach':[5.6,8.8,5,10,0,2.4],'right_alley':[9.5,12.5,0,10,0,2.4],'center':[5,13.5,9.3,14,0,2.4]}
obstacles={'left_back':[.8,5.5,.8,5,0,4.8],'left_front':[.8,5.5,7.8,9.5,0,3],'passage_roof':[.8,5.5,5,7.8,2.65,4.8],'hut':[12.8,15.6,.8,6,0,3.3],'tank_bound':[6.1,9.1,1.1,4.1,0,3.5],'bin_left':[1.5,3.3,9.8,10.8,0,1.2],'bin_right':[14,15.25,6.35,7.45,0,1.25],'bags':[3.55,4.5,9.85,10.6,0,.5]}
hits=[(r,o) for r,a in routes.items() for o,b in obstacles.items() if all(min(a[k+1],b[k+1])>max(a[k],b[k]) for k in (0,2,4))]
# Center starts in front of the low wing; overlap of numerical .2 strips fixed by route below.
if hits:
 routes['center']=[5.6,13.5,9.3,14,0,2.4]
 hits=[(r,o) for r,a in routes.items() for o,b in obstacles.items() if all(min(a[k+1],b[k+1])>max(a[k],b[k]) for k in (0,2,4))]
assert not hits,hits
roofs={'left_building':{'area':4.7*(7+.0)+4.7*1.7,'occupied':2.35*3.3+1.25*3.3+3.55*2.2+3.8*1.1},'right_hut':{'area':2.8*5.2,'occupied':2.05*2.6+2.05*1.3}}
for r in roofs.values():r['fraction']=r['occupied']/r['area'];assert .4<=r['fraction']<=.8
exits=[{'direction':'back_left_11','position':'mid-side y5..7.8','type':'building_ground_floor_passage','state':'open_after_clear','shared_building_entry':True,'connection':'straight level corridor to rear-left boundary; visible depth and far daylight','opening_clearance':'no leaf across route'},{'direction':'back_right_1','position':'intermediate x9.5..12.5','type':'unframed alley between tank enclosure and hut','state':'open_after_clear','shared_building_entry':False,'connection':'clear strip from center to rear-right boundary','opening_clearance':'no overhead frame or blocking leaf'}]
plan={'master_version':'2.3','execution_version':'1.4','base':[0,16,0,16,-1.6,0],'projection':'one orthographic XYZ','building_polygons':buildings,'orthogonal_edges':edgecheck,'roofs':roofs,'roof_supports':'flat roof surfaces and explicit supported lintel over passage; equipment sits on these levels','routes':routes,'obstacles':obstacles,'collisions':hits,'functional_exits':exits,'decorative_entry':'closed hut door at y6, not a third exit','independence':'fresh scene, neither pair output seen or used as input','cassette_futurism':False,'numeric_limit':'plan only; final actual image must separately pass C/L'}
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
m=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'));refs=[{'path':str(RUN/'structure_plan.png'),'role':'new baseline geometry only, not cassette variant','submitted':False}]
for key in ['M02-01','M01-01','M03-10','M04-02']:
 r=next(x for x in m['references'] if x['id']==key);assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
 refs.append({'id':key,'path':str(ROOT/r['path']),'role':r['use_only'],'exclude':r['exclude'],'submitted':False})
(RUN/'references.json').write_text(json.dumps({'mechanism':'referenced_image_paths','inputs':refs,'not_used':'other pair output, all prior generated concept images, cassette user reference'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'collisions':hits,'orthogonal_edges_pass':True,'roof_fractions':[x['fraction'] for x in roofs.values()]}))


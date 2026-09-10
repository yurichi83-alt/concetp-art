from pathlib import Path
RUN=Path(__file__).resolve().parent
exec((RUN/'renderer_prefix.py.txt').read_text(encoding='utf-8-sig'))
# New independent cassette scene. Only rendering helpers were reused, no previous scene.
base=(0,16,0,16,-2.2,0)
box(*base,colors=('#766b58','#605d54','#959a95'))
# Calm paving: same orthogonal plane and camera.
for k in range(2,16,2):
 line([(k,0,.012),(k,16,.012)],'#888f8b',1)
 line([(0,k,.012),(16,k,.012)],'#888f8b',1)
# Rear left boundary continuity; archive building includes a traversable undercroft.
wall_col=('#817f71','#716d61','#aaa791')
box(0,.45,0,4,0,3.0,wall_col)
box(0,.45,10.5,16,0,2.8,wall_col)
# Building A: rectangle x[0,3.8], y[4,10.5], roof4.2. Tunnel y[6.2,9.2].
box(0,3.8,4,6.2,0,4.2,('#9b8e7c','#81745f','#b4a38c'))
box(0,3.8,9.2,10.5,0,4.2,('#9b8e7c','#81745f','#b4a38c'))
box(0,3.8,6.2,9.2,2.8,4.2,('#9b8e7c','#81745f','#b4a38c'))
plane(0,3.8,6.2,9.2,.025,'#647773')
# Building B: orthogonal L footprint, lower front wing on one end.
box(4.8,12.5,0,3.5,0,3.4,('#738480','#637571','#a2ada2'))
box(10,12.5,3.5,5.5,0,2.5,('#738480','#637571','#a2ada2'))
# Closed decorative human door facing courtyard on B; on y=3.5 plane.
poly([(6,3.505,.06),(7.4,3.505,.06),(7.4,3.505,2.35),(6,3.505,2.35)],'#4a5552')
line([(7.15,3.52,.9),(7.15,3.52,1.2)],'#c5baa2',2)
# Back-right gap bounded by continuous panels. Open alley x[13,15.5].
box(.45,4.8,0,.45,0,3.0,wall_col)
box(12.5,13,0,.45,0,2.6,wall_col)
box(15.5,16,0,.45,0,2.6,wall_col)
plane(13,15.5,0,4.0,.025,'#647773')
# Folded open gate panel aligned along outer side so the walk lane is clear.
box(15.65,15.9,.45,2.4,0,2.35,('#66726c','#53635c','#88948b'))
# Roof A apparatus union 13.35 / 25.46 =52.44%. Varied utility silhouettes.
roof_devices=[
 ('A','air-recovery bank',(0.35,2.45,4.35,6.15,4.2,5.15)),
 ('A','broad modular converter',(0.4,3.3,6.55,8.9,4.2,5.6)),
 ('A','slim buffer duct',(0.55,3.0,9.35,10.15,4.2,4.8)),
 ('B','vent plenum',(5.15,8.25,.3,2.75,3.4,4.6)),
 ('B','flat recovery rack',(8.6,12.1,.3,2.6,3.4,4.25)),
 ('B','wing water module',(10.25,12.15,3.75,5.15,2.5,3.55)),
]
for owner,name,b in roof_devices:
 box(*b,colors=('#aaa898','#888c81','#d0cbbb'))
# Broad recesses and vents on apparatus faces; gray dots/rectangles are mechanical only.
for x1,x2,y,z1,z2 in [(5.5,7.95,2.755,3.7,4.25),(9,11.8,2.605,3.55,3.95)]:
 poly([(x1,y,z1),(x2,y,z1),(x2,y,z2),(x1,y,z2)],'#303e3e')
# Low wall-side trash and waste compactors, excluded from walking reserves.
props=[('waste_compactor',(3.9,5.25,4.15,5.75,0,1.3)),('bin',(0.55,1.8,12,13.25,0,1.15)),('bags',(0.7,2,13.4,14.45,0,.7)),('right_bin',(13.15,14.3,5.75,7.05,0,1.1))]
for name,b in props:
 box(*b,colors=('#777a67','#5c6559','#9fa390'))
# Underground services are sealed utility cut faces, not underground passages.
for x1,x2,z1,z2 in [(3,7,-1.35,-.9),(10,14.4,-1.7,-1.25)]:
 poly([(x1,16.01,z1),(x2,16.01,z1),(x2,16.01,z2),(x1,16.01,z2)],'#39464a')
poly([(16.01,4,-1.55),(16.01,9,-1.55),(16.01,9,-.9),(16.01,4,-.9)],'#465458')
exec((RUN/'renderer_depth.py.txt').read_text(encoding='utf-8-sig'))
svg.append('</svg>')
(RUN/'structure_plan.svg').write_text('\n'.join(svg),encoding='utf-8')

footprints={
 'A':[(0,4),(3.8,4),(3.8,10.5),(0,10.5)],
 'B':[(4.8,0),(12.5,0),(12.5,5.5),(10,5.5),(10,3.5),(4.8,3.5)]
}
routes=[
 {'id':'center','volume':[5.5,12.7,6.1,13.5,0,2.5]},
 {'id':'left_approach','volume':[3.8,8,6.3,9.1,0,2.5]},
 {'id':'left_transition','volume':[0,3.8,6.3,9.1,0,2.5]},
 {'id':'right_approach','volume':[12,15.4,3.6,5.5,0,2.5]},
 {'id':'right_connection','volume':[13.1,15.4,0,5.5,0,2.5]},
 {'id':'right_turn','volume':[11.3,13.8,5.5,7.7,0,2.5]},
]
# right_turn must not intersect right_bin; reserve narrowed before props at y5.75.
routes[-1]['volume']=[11.3,13.05,5.5,7.7,0,2.5]
solids=[
 ('A_left',(0,3.8,4,6.2,0,4.2)),('A_right',(0,3.8,9.2,10.5,0,4.2)),
 ('A_lintel',(0,3.8,6.2,9.2,2.8,4.2)),
 ('B_main',(4.8,12.5,0,3.5,0,3.4)),('B_wing',(10,12.5,3.5,5.5,0,2.5)),
 ('leftwall0',(0,.45,0,4,0,3)),('leftwall1',(0,.45,10.5,16,0,2.8)),
 ('backwall',(0.45,4.8,0,.45,0,3)),('gateleft',(12.5,13,0,.45,0,2.6)),('gateright',(15.5,16,0,.45,0,2.6)),('openleaf',(15.65,15.9,.45,2.4,0,2.35)),
]+props
# Approach right starts outside B wing, preserving corner clearance.
routes[3]['volume']=[12.65,15.4,3.6,5.5,0,2.5]
def overlap(a,b):
 return all(min(a[i+1],b[i+1])-max(a[i],b[i])>1e-6 for i in (0,2,4))
collisions=[(r['id'],n) for r in routes for n,b in solids if overlap(r['volume'],b)]
axis_checks={n:all((a[0]==b[0]) != (a[1]==b[1]) for a,b in zip(poly,poly[1:]+poly[:1])) for n,poly in footprints.items()}
roof_areas={'A':3.8*6.5,'B':7.7*3.5+2.5*2}
occupied={n:sum((b[1]-b[0])*(b[3]-b[2]) for o,name,b in roof_devices if o==n) for n in roof_areas}
coverage={n:occupied[n]/roof_areas[n] for n in roof_areas}
roof_planes=[{'building':'A','bounds':[0,3.8,4,10.5],'z':4.2}, {'building':'B','bounds':[4.8,12.5,0,3.5],'z':3.4},{'building':'B','bounds':[10,12.5,3.5,5.5],'z':2.5}]
support_checks=[]
for owner,name,b in roof_devices:
 fits=any(s['building']==owner and abs(s['z']-b[4])<1e-8 and b[0]>=s['bounds'][0] and b[1]<=s['bounds'][1] and b[2]>=s['bounds'][2] and b[3]<=s['bounds'][3] for s in roof_planes)
 support_checks.append({'device':name,'flat_roof_support_and_wall_top_match':fits})
plan={'mode':'independent_new_scene','master_version':'2.3','execution_version':'1.4','base':base,'camera':'single orthographic p(x,y,z) = (640+32(x-y),310+32/sqrt(3)(x+y)-64/sqrt(3)z)','building_footprints':footprints,'roof_planes':roof_planes,'roof_devices':roof_devices,'roof_coverage':coverage,'roof_support_checks':support_checks,'axis_checks':axis_checks,'walk_volumes':routes,'solid_volumes':solids,'collision_results':collisions,'exits':[
 {'id':'E_left','direction':'11 oclock, x=0 side','position':'intermediate side','form':'archive building through passage','current_state':'open','post_clear_connection':'x continues negative to the next alley, behind roof; no extra exposed destination required','opening_clearance':'already open; 2.8m planned height, 3m planned width','building_entry_role':'A human entry doubles as left functional exit'},
 {'id':'E_right','direction':'1 oclock, y=0 side','position':'near outer end x13..15.5','form':'open side-alley with gate folded to outer edge','current_state':'open','post_clear_connection':'y continues negative beyond base into next city lane','opening_clearance':'folded leaf x15.65..15.9 outside walking volume','building_entry_role':'not a building entry; B has closed decorative human door'}
],'dimension_limit':'planned max5.6m; actual image scale/colliders require 3D validation','independence':'Only renderer helper code reused. No other new requested image opened or supplied.'}
assert not collisions,collisions
assert all(axis_checks.values())
assert all(.4<=c<=.8 for c in coverage.values())
assert all(s['flat_roof_support_and_wall_top_match'] for s in support_checks)
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'axis_checks':axis_checks,'collisions':collisions,'roof_coverage':coverage,'roof_support_checks':support_checks},indent=2))

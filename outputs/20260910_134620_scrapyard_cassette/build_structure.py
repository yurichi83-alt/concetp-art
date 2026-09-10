from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, hashlib

R=Path(__file__).resolve().parent
ROOT=R.parent.parent
S={
 'master_version':'2.3','mode':'independent_new_generation',
 'camera':{'projection':'parallel orthographic','screen_x':'700+36*(x-y)','screen_y':'280+18*(x+y)-47*z'},
 'base':{'square':[0,0,16,16],'top_z':0,'bottom_z':-2,'no_bevel':True},
 'buildings':[
  {'id':'scrapyard','footprint':[[0,1.4],[4.6,1.4],[4.6,11.6],[0,11.6]],'zones':[
   {'id':'integrated_recycler','aabb':[0,1.4,0,4.6,6.5,4.7],'role':'one half of the building architecture is a thick-shell recycler/compactor with deep service cavity; not rooftop AC'},
   {'id':'workshop','aabb':[0,6.5,0,4.6,11.6,3.6],'role':'older workshop half with human-scale roller shutter internal transition'}],
   'roof_planes':[{'bounds':[0,1.4,4.6,6.5],'z':4.7},{'bounds':[0,6.5,4.6,11.6],'z':3.6}],
   'roof_equipment':[{'bounds':[0.5,1.8,4.1,4.8],'type':'heat recovery and intake deck','base_z':4.7,'height':0.7},{'bounds':[0.7,5.0,3.6,6.2],'type':'chimney duct pedestal','base_z':4.7,'height':0.55},{'bounds':[0.5,7.0,4.1,10.3],'type':'raised ventilating monitor and reclaimed solar-thermal cover','base_z':3.6,'height':0.65}],
   'human_entry':{'face':'x=4.6','y':[8.5,10.9],'width':2.4,'height':2.7,'state':'closed roller shutter','role':'left functional exit'},
   'mechanized_architecture_planned_fraction':0.5},
  {'id':'grocery','footprint':[[7.4,0],[13.2,0],[13.2,3.8],[7.4,3.8]],'zones':[{'id':'grocery_store','aabb':[7.4,0,0,13.2,3.8,3.2]}],
   'roof_planes':[{'bounds':[7.4,0,13.2,3.8],'z':3.2}],
   'roof_equipment':[{'bounds':[7.8,0.4,11.0,2.7],'type':'reclaimed bulk refrigeration exchanger','base_z':3.2,'height':0.65},{'bounds':[11.3,0.4,12.8,2.7],'type':'gravity-fed water store','base_z':3.2,'height':0.9}],
   'human_entry':{'face':'y=3.8','x':[11.4,12.5],'width':1.1,'height':2.3,'state':'closed glazed door','role':'decorative building entry'}}],
 'rear_blockers':[{'aabb':[0,0,0,4.6,1.4,2.8],'role':'closed corner infrastructure fence'},{'aabb':[0,11.6,0,1.0,16,2.8],'role':'contained scrap bays plus solid back fence'},{'aabb':[13.2,0,0,16,0.65,2.5],'role':'solid fence behind grocery water tanks'}],
 'exits':[
 {'id':'left','direction':'approximately 11 oclock','location':'intermediate left building facade','form':'workshop roller shutter/internal transition','current_state':'closed','cleared_state':'rolls up overhead; passage traverses workshop to x=0','building_entry_dual_use':True,'portal':[4.6,8.5,0,4.6,10.9,2.7],'protected_approach':[4.6,8.3,0,8.2,11.1,3.0],'protected_internal_after_open':[0,8.5,0,4.6,10.9,3.0]},
 {'id':'right','direction':'approximately 1 oclock','location':'intermediate between workshop and grocery','form':'open service passage through rear boundary','current_state':'open','cleared_state':'same open passage beyond y=0','building_entry_dual_use':False,'portal':[4.9,0,0,7.1,0,3.0],'protected_approach':[4.9,0,0,7.1,8.3,3.0]}],
 'center':[7.2,4.5,0,13.5,13.3,3.0],
 'props':[{'aabb':[1.2,12.4,0,3.0,14.8,1.3],'role':'two ordinary deep bins with reclaimed lid ram'},{'aabb':[8.0,3.8,0,10.8,4.35,0.9],'role':'grocery produce crates against facade'},{'aabb':[13.55,0.8,0,15.6,2.7,2.1],'role':'curved water tank nonbuilding'}, {'aabb':[0.8,4.9,5.25,1.7,5.8,6.25],'role':'supported short chimney'}],
 'cutaway':{'left':'large clay and foundation layers; enclosed oblong settling vessel and short pipe cross section','right':'large earth layer; separate stepped service trench with broad chilled-water loop and rectangular power conduit','no_walkable_void':True},
 'independence':'New coordinates authored from current keywords and masters. No counterpart scene/guide/prompt/output or previous generated artwork opened/read/reused. User cassette reference is the only scoped nonmaster reference.'
}
def edge_axis(poly):
 return ['Y' if a[0]==b[0] and a[1]!=b[1] else 'X' if a[1]==b[1] and a[0]!=b[0] else 'INVALID' for a,b in zip(poly,poly[1:]+poly[:1])]
def area(b): return (b[2]-b[0])*(b[3]-b[1])
for b in S['buildings']:
 b['edge_axes']=edge_axis(b['footprint'])
 assert 'INVALID' not in b['edge_axes']
 b['roof_coverage_planned']=sum(area(e['bounds']) for e in b['roof_equipment'])/sum(area(p['bounds']) for p in b['roof_planes'])
 assert .4 <= b['roof_coverage_planned'] <= .8
def intersect(a,b):return all(min(a[i+3],b[i+3])-max(a[i],b[i])>1e-6 for i in range(3))
protected=[e['protected_approach'] for e in S['exits']]+[S['center']]
obstacles=[z['aabb'] for b in S['buildings'] for z in b['zones']]+[p['aabb'] for p in S['props']]+[p['aabb'] for p in S['rear_blockers']]
assert not any(intersect(p,o) for p in protected for o in obstacles)
S['preflight_geometry']={'orthogonal_edges':'PASS','reserved_routes_no_obstacle_overlap':'PASS','roof_supports':'explicit flat planes with matching pedestal bases','planning_only':'Final image must be inspected; no 3D collider verification'}
(R/'structure_plan.json').write_text(json.dumps(S,ensure_ascii=False,indent=2),encoding='utf-8')

img=Image.new('RGB',(1400,1100),(247,245,237)); d=ImageDraw.Draw(img)
def p(x,y,z):return (round(700+36*(x-y)),round(280+18*(x+y)-47*z))
def face(v,c):d.polygon([p(*a) for a in v],fill=c,outline=(72,76,75),width=2)
def box(a,c):
 x,y,z,X,Y,Z=a
 face([(x,Y,z),(X,Y,z),(X,Y,Z),(x,Y,Z)],tuple(max(0,int(q*.79)) for q in c))
 face([(X,y,z),(X,Y,z),(X,Y,Z),(X,y,Z)],tuple(max(0,int(q*.9)) for q in c))
 face([(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)],c)
box([0,0,-2,16,16,0],(198,179,143))
face([(0,0,.01),(16,0,.01),(16,16,.01),(0,16,.01)],(220,215,199))
# Broad reserved corridors shown as floor tones only. This is a structural guide, never final art.
for a in protected:
 x,y,z,X,Y,Z=a;face([(x,y,.02),(X,y,.02),(X,Y,.02),(x,Y,.02)],(218,229,209))
items=[]
for a in S['rear_blockers']:items.append((a['aabb'],(137,143,132)))
for b in S['buildings']:
 for z in b['zones']:items.append((z['aabb'],(166,155,133) if z['id']=='workshop' else (150,161,157) if z['id']=='integrated_recycler' else (188,162,119)))
 for e in b['roof_equipment']:
  x,y,X,Y=e['bounds']; zz=e['base_z']; items.append(([x,y,zz,X,Y,zz+e['height']],(156,170,166)))
for a in S['props']:items.append((a['aabb'],(137,155,144)))
for a,c in sorted(items,key=lambda q:q[0][0]+q[0][1]+q[0][3]+q[0][4]+(36/47)*(q[0][2]+q[0][5])):box(a,c)
# Deep machine bay in mechanized front facade, and closed workshop passage.
face([(4.63,2.25,.55),(4.63,5.7,.55),(4.63,5.7,3.85),(4.63,2.25,3.85)],(53,69,67))
face([(4.65,8.5,0),(4.65,10.9,0),(4.65,10.9,2.7),(4.65,8.5,2.7)],(98,112,104))
for z in [.35,.7,1.05,1.4,1.75,2.1,2.45]:d.line([p(4.67,8.5,z),p(4.67,10.9,z)],fill=(169,174,160),width=3)
face([(11.4,3.83,0),(12.5,3.83,0),(12.5,3.83,2.3),(11.4,3.83,2.3)],(76,99,94))
face([(8,3.83,1.05),(10.8,3.83,1.05),(10.8,3.83,2.55),(8,3.83,2.55)],(98,128,113))
# Structural cut-section utility cross-sections; only shapes, no scene art.
face([(16,3.0,-1.6),(16,6.8,-1.6),(16,6.8,-.5),(16,3,-.5)],(128,148,147))
face([(4,16,-1.55),(7.4,16,-1.55),(7.4,16,-.5),(4,16,-.5)],(140,139,123))
img.save(R/'structure_guide.png')

refs=[('structure_guide.png','New independent geometry guide; preserve square slab, common camera, building faces, two assigned exits and protected space'),
 ('refs/master02/layout_two_exits.png','M02 common boundary/connectivity only; not labels or fixed exit positions'),
 ('refs/master01/composition_cutaway.png','M01 camera/base/two cut planes only; no neon or buildings copied'),
 ('refs/master03/ldi_10_storefront_style_anchor.png','M03 broad stylized 3D planes/materials/lighting; no characters/store identities'),
 ('outputs/20260910_124032_alley_reference_shapes/user_cassette_reference.png','User cassette shape vocabulary only; thick shells, deep mechanical cavities, analog meters, ducts; no layout/palette copying')]
data={'mode':'new_generation','input_count':5,'all_inputs_visually_inspected_before_call':False,'actual_transmission':'pending','inputs':[],'omitted':[{'id':'M04-02','path':'refs/master04/world_02_heavy_mechanical_arms.png','visually_inspected':True,'reason':'Five input slots prioritize own structural guide + M01/M02/M03 + explicit cassette image. M04 functional repaired high-tech masses and mismatched replacement panels preserved textually.'}],'independence':S['independence']}
for i,(q,role) in enumerate(refs,1):
 q=R/q if i==1 else ROOT/q
 data['inputs'].append({'order':i,'path':str(q),'role':role,'sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'visually_inspected':i!=1})
(R/'references.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(R/'preflight.md').write_text('# Preflight\n\nCurrent master 2.3 / execution 1.4 / approvals read. One new cassette scene under fixed Salvage Cyberpunk world. Current request: 고물상, 식료품 상점 / 낮, 웜톤 / 고물상 건물의 절반은 기계화, 쓰레기통, 굴뚝 / 한 장.\n\nSquare prism, common projection, no unrequested bevel; all building footprint edges X/Y aligned; explicit horizontal roof planes and support pedestals. Exactly two assigned functional exits with reserved continuous approach; left closed workshop shutter and right open service passage. Collision check uses planned volumes and does not substitute final visual QA.\n\nScrapyard half integrated recycler by ground plan and visible mass intent; roof occupancy scrapyard {:.1%}, grocery {:.1%}. Person-scale entry in both buildings; two genuine earth/foundation/utility cut faces. No characters, screens, CRT, neon, center obstructions or third passage.\n\nBuilt-in imagegen only; no API/install/git/global changes. Image output and QA pending.\n'.format(*[b['roof_coverage_planned'] for b in S['buildings']]),encoding='utf-8')
print(json.dumps({'run':str(R),'roof_coverage':{b['id']:b['roof_coverage_planned'] for b in S['buildings']},'structure_check':'PASS'},ensure_ascii=False))

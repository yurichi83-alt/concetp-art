from pathlib import Path
import json, math
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).parent
im=Image.new("RGB",(1440,1440),(243,242,233)); d=ImageDraw.Draw(im)
def P(x,y,z=0):return (720+35*x-35*y,300+20*x+20*y-40*z)
def poly(q,c,outline=(48,59,65),width=3):d.polygon([P(*p) for p in q],fill=c,outline=outline,width=width)
def line(q,c=(48,59,65),w=3):d.line([P(*p) for p in q],fill=c,width=w)
def box(a,b,col):
 x,y,z=a;X,Y,Z=b
 poly([(x,y,z),(X,y,z),(X,Y,z),(x,Y,z)],col)
 poly([(X,y,z),(X,Y,z),(X,Y,Z),(X,y,Z)],tuple(max(0,v-24) for v in col))
 poly([(x,Y,z),(X,Y,z),(X,Y,Z),(x,Y,Z)],tuple(max(0,v-10) for v in col))
 poly([(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)],tuple(min(255,v+20) for v in col))
def text_world(p,t,fill=(28,43,47)):
 d.text(P(*p),t,fill=fill,stroke_width=2,stroke_fill=(243,242,233))
font=None
try:font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',24)
except:pass
d.text((62,46),'STRUCTURE GUIDE / one orthographic camera / not a geometry lock',fill=(26,44,52),font=font)
# Unchanged square base, two planar front cut faces.
box((0,0,-2.5),(16,16,0),(185,170,147))
poly([(0,0,0),(16,0,0),(16,16,0),(0,16,0)],(213,207,182))
for t in [4,8,12]:
 line([(t,0,0.01),(t,16,0.01)],(193,189,171),1)
 line([(0,t,0.01),(16,t,0.01)],(193,189,171),1)
# Exactly two rear gaps: x=0,y12..14.5 and y=0,x11.8..14.3.
for a,b in [((0,0,0),(.28,12,2.65)),((0,14.5,0),(.28,16,2.65)),((0,0,0),(11.8,.28,2.8)),((14.3,0,0),(16,.28,2.8))]:box(a,b,(139,153,149))
# Cyan guide-only continuous walk surfaces.
poly([(0,12,.03),(7,12,.03),(7,14.5,.03),(0,14.5,.03)],(143,202,199))
poly([(11.8,0,.03),(14.3,0,.03),(14.3,10,.03),(11.8,10,.03)],(143,202,199))
poly([(6.2,6,.035),(14.3,6,.035),(14.3,14.5,.035),(6.2,14.5,.035)],(172,211,191))
# Non-building sorting machine; faceted broad curved casing with functional base.
box((6.3,0.3,0),(11,3.7,.65),(100,118,123))
xs=[6.3+i*4.7/18 for i in range(19)]
roof=lambda x:1.1+2.5*math.sqrt(max(0,1-((x-8.65)/2.35)**2))
poly([(x,3.7,roof(x)) for x in xs]+[(11,3.7,.65),(6.3,3.7,.65)],(151,137,102))
for i in range(len(xs)-1):
 x,X=xs[i:i+2];poly([(x,.3,roof(x)),(X,.3,roof(X)),(X,3.7,roof(X)),(x,3.7,roof(x))],(170-i*2,152-i,111),width=1)
# Exposed broad circular drum end, heavy concentric ring and toothed drive gear.
def drum_ring(cx,yy,cz,r,n=48):
 return [(cx+r*math.cos(i*2*math.pi/n),yy,cz+r*math.sin(i*2*math.pi/n)) for i in range(n)]
poly(drum_ring(8.65,3.79,2.1,1.7),(76,95,99),width=4)
poly(drum_ring(8.65,3.81,2.1,1.46),(182,162,110),width=4)
teeth=[]
for i in range(48):
 a=i*2*math.pi/48;r=1.27 if i%4 in (0,1) else 1.08
 teeth.append((8.65+r*math.cos(a),3.88,2.1+r*math.sin(a)))
poly(teeth,(83,111,116),width=3)
poly(drum_ring(8.65,3.90,2.1,.78),(139,151,133),width=3)
for a in [0,math.pi/2,math.pi,3*math.pi/2]:
 line([(8.65+.25*math.cos(a),3.92,2.1+.25*math.sin(a)),(8.65+.70*math.cos(a),3.92,2.1+.70*math.sin(a))],(57,81,89),9)
poly(drum_ring(8.65,3.94,2.1,.28),(195,166,103),width=3)
# Distinct projecting drive casing, grounded service skid and round motor hub.
box((10.2,2.8,.45),(11.4,4.3,1.38),(96,120,123))
box((10.3,3.1,1.38),(11.25,4.15,1.75),(145,143,115))
poly(drum_ring(10.8,4.32,1.12,.43),(60,90,98),width=3)
poly(drum_ring(10.8,4.34,1.12,.20),(192,162,110),width=3)
# Deep service deck spans the open exit with four outside pillars, clear z3.2 below.
for x in [11.35,14.3]:
 for y in [.35,2.05]:box((x,y,0),(x+.45,y+.45,3.55),(119,127,125))
box((11.35,.35,3.2),(14.75,2.5,3.55),(143,151,145))
# Equipment-side supported beam joins sorter to service deck without route intrusion.
box((10.65,1.15,2.0),(11.1,1.65,3.55),(111,135,136))
box((10.65,1.15,3.2),(11.8,1.65,3.55),(139,153,145))
line([(11.55,.5,3.58),(14.5,.5,3.58),(14.5,2.25,3.58)],(93,114,117),4)
# Single workshop long y silhouette, human shutter facing +X.
box((.7,2,0),(4.8,11.5,2.6),(149,130,105))
for y in [6.3,9.3]:
 poly([(4.815,y,.08),(4.815,y+1.55,.08),(4.815,y+1.55,2.18),(4.815,y,2.18)],(66,86,89))
 for z in [.4,.8,1.2,1.6,2]:line([(4.825,y,z),(4.825,y+1.55,z)],(115,135,134),2)
# Barrel roof, cylindrical axis parallel to Y.
xx=[.7+4.1*i/20 for i in range(21)]
z=lambda x:2.6+1.4*math.sqrt(max(0,1-((x-2.75)/2.05)**2))
poly([(x,11.5,z(x)) for x in xx]+[(4.8,11.5,2.6),(.7,11.5,2.6)],(143,157,151))
for i in range(20):
 x,X=xx[i:i+2];poly([(x,2,z(x)),(X,2,z(X)),(X,11.5,z(X)),(x,11.5,z(x))],(164-i*2,174-i*2,159-i),width=1)
# Supported rear roof service platform with off-center office volume.
for x,y in [(.85,2.1),(4.6,2.1),(.85,5.3),(4.6,5.3)]:box((x,y,2.6),(x+.13,y+.13,4.18),(87,110,111))
box((.7,2,4.12),(4.8,5.6,4.3),(130,139,127))
box((1.1,2.3,4.3),(3.85,4.7,5.4),(185,171,133))
box((1,2.2,5.4),(3.95,4.8,5.5),(130,151,143))
poly([(3.86,2.65,4.55),(3.86,4.3,4.55),(3.86,4.3,5.4),(3.86,2.65,5.4)],(75,104,110))
# Low functional roof cover atop office (building maximum remains 5.8).
box((1.4,2.4,5.5),(3.5,4.3,5.8),(71,114,119))
poly([(2.8,4.715,4.31),(3.5,4.715,4.31),(3.5,4.715,5.27),(2.8,4.715,5.27)],(72,95,96))
# Integrated side maintenance canopy/deck and broad duct, all supported.
box((3.5,5.6,2.6),(4.8,8.8,2.8),(129,147,139))
for y in [5.7,8.65]:box((4.55,y,0),(4.7,y+.13,2.65),(90,113,112))
box((2.25,8.8,3.95),(3.05,10.9,4.35),(125,151,146))
for y in [8.9,10.65]:box((2.3,y,3.75),(3,y+.15,4.05),(92,116,116))
# Compact exterior stair within x4.8..6,y2..5.8; no rear exit overlap.
for i in range(10):
 y=5-(i+1)*.30;box((5.4,y,i*.215),(6,y+.30,(i+1)*.215),(130,143,139))
for i in range(10):
 y=2+i*.30;box((4.8,y,2.15+i*.215),(5.4,y+.30,2.15+(i+1)*.215),(139,153,145))
box((4.8,1.7,2.05),(6,2,2.15),(128,146,142))
line([(6,5,1),(6,2,3.15),(4.8,2,3.15),(4.8,5,5.3)],(77,99,100),4)
# Front sharp edges and constant depth comparison vectors remain unobscured.
for x,y in [(16,0),(16,16),(0,16)]:line([(x,y,0),(x,y,-2.5)],(41,78,99),5)
line([(16,0,0),(16,16,0),(0,16,0)],(40,79,99),5)
line([(16,0,-2.5),(16,16,-2.5),(0,16,-2.5)],(40,79,99),5)
text_world((.1,12.15,.08),'EXIT A / OPEN')
text_world((12.0,1.3,.08),'EXIT B / OPEN')
text_world((8,9,.1),'CLEAR ACTIVITY FLOOR')
d.text((65,1120),'Blue edges: matching base axes and equal-depth vertical vectors. Cyan/green: guide-only walking zones.',fill=(34,60,68),font=font)
d.text((65,1164),'No front walls. Two rear transitions only. Roof curve tangents are not XY comparison edges.',fill=(34,60,68),font=font)
d.text((65,1208),'Labels and guide colors must not appear in the concept image.',fill=(34,60,68),font=font)
im.save(ROOT/'structure_guide.png')
plan={
 'scene':'고철상 / 낮 / 황무지 / 한 장','masters_version':'2.7','execution_rules_version':'1.8',
 'guide_role':'visual structure/form guide, not hard geometry control; labels/colors are guide-only',
 'camera':{'projection':'orthographic_parallel','canvas':[1440,1440],'origin':[720,300],'basis':{'x':[35,20],'y':[-35,20],'z':[0,-40]},'scene_choice_not_global_default':True},
 'base':{'x':[0,16],'y':[0,16],'top_z':0,'bottom_z':-2.5,'visible_front_faces':['x=16','y=16'],'sharp_square_planar':True},
 'buildings':[{'id':'workshop','footprint':{'x':[.7,4.8],'y':[2,11.5]},'wall_z':2.6,'barrel_roof':{'axis':'Y','apex_z':4.0},'upper_office':{'x':[1.1,3.85],'y':[2.3,4.7],'floor_z':4.3,'top_z':5.8,'support':'service platform and four visible wall-supported posts'},'entries':[{'face':'x+','y':[6.3,7.85],'state':'closed human shutter','role':'decorative building entry, not map exit'},{'face':'x+','y':[9.3,10.85],'state':'closed human shutter','role':'decorative service entry'}],'external_stairs':{'x':[4.8,6],'y':[1.7,5],'top_z':4.3,'form':'two compact switchback flights and rear landing; visual guide, not dimensional stair certification','role':'office access, not map exit'},'roof_functional_coverage':{'target_fraction':.57,'method':'nonoverlapping projected functional coverage across main roof; visual estimate only','rear_service_platform':{'x':[.7,4.8],'y':[2,5.6],'area':14.76},'side_maintenance_canopy':{'x':[3.5,4.8],'y':[5.6,8.8],'area':4.16},'broad_exhaust_duct':{'x':[2.25,3.05],'y':[8.8,10.9],'area':1.68},'main_roof_plan_area':38.95,'planned_fraction':.529,'office_roof_functional_cover_fraction':.52,'support_connections':'rear platform posts, wall-supported maintenance canopy and duct saddles; raised functional weather/vent cover integrated with office roof, not paint' ,'do_not_duplicate_machinery':True}}],
 'nonbuilding_boundary_machine':{'x':[6.3,11],'y':[.3,4],'top_z':3.8,'role':'nonbuilding rotary sorter: exposed circular drum end, concentric rim, large toothed drive gear and separate projecting motor casing; no windows or human entrance; rear panels provide continuity','layout_adjustment':'main body starts at x6.3 within requested x5..11 zone to keep exterior stairs x4.8..6 clear; motor casing extends to x11.4, short of right path x11.8'},
 'rear_boundaries':{'x0':{'closed_y_intervals':[[0,12],[14.5,16]],'height':2.65},'y0':{'closed_x_intervals':[[0,11.8],[14.3,16]],'height':2.8},'corner_connection':'panels overlap at rear corner, no third gap'},
 'functional_exits':[{'id':'A','direction':'back_left/x0/about11oclock','boundary_interval_y':[12,14.5],'state':'open','form':'delivery floor entrance','approach':{'x':[0,7],'y':[12,14.5]},'post_clear_connection':'same unobstructed flat passage beyond x0','not_a_building_entry':True},{'id':'B','direction':'back_right/y0/about1oclock','boundary_interval_x':[11.8,14.3],'state':'open','form':'straight path under deep equipment service deck','clear_head_z':3.2,'deck':{'x':[11.35,14.75],'y':[.35,2.5],'underside_z':3.2,'top_z':3.55},'connection_to_sorter':'supported beam at x10.65..11.8,y1.15..1.65,z3.2..3.55 outside walking corridor','approach':{'x':[11.8,14.3],'y':[0,10]},'pillars':'four posts, x11.35..11.8 and14.3..14.75 at y0.35..0.8 and2.05..2.5, outside corridor','post_clear_connection':'same straight passage beyond y0'}],
 'central_clear_region':{'x':[6.2,14.3],'y':[6,14.5],'connected_to_both_exits':True,'props':'none in central/routes; scene-specific salvage only outside walking regions'},
 'cutaway_design':'two front planar faces; large ground layers, foundations, a few coarse functional utility forms; no underground third route',
 'visual_checks':['whole base and front corners visible','same-axis straight lines parallel','constant-depth top/bottom vectors','building footings and straight storey lines compare to base','barrel/rounded tangents separate','two visibly continuous rear boundaries and exactly two exits','closed workshop shutters not additional map transitions'],
 'actual_collision_mesh_uv_validation_required':False,'plan_is_not_final_image_pass':True,'final_png_review_required':True
}
(ROOT/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))

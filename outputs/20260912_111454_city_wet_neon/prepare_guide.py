from pathlib import Path
from PIL import Image, ImageDraw
import math, json, hashlib

P=Path(__file__).resolve().parent
ROOT=P.parents[1]
im=Image.new('RGB',(1300,1320),'#efece3');d=ImageDraw.Draw(im)
def pt(x,y,z): return (650+28*x-28*y,460+16*x+16*y-30*z)
def poly(v,c): d.polygon([pt(*a) for a in v],fill=c,outline='#344449',width=2)
def box(x,y,w,l,z,h,c):
    poly([(x,y+l,z),(x+w,y+l,z),(x+w,y+l,z+h),(x,y+l,z+h)],c[0])
    poly([(x+w,y,z),(x+w,y+l,z),(x+w,y+l,z+h),(x+w,y,z+h)],c[1])
    poly([(x,y,z+h),(x+w,y,z+h),(x+w,y+l,z+h),(x,y+l,z+h)],c[2])
def rounded(x,y,w,l,z,h,r,c):
    ring=[]
    for cx,cy,a0 in [(x+w-r,y+r,-90),(x+w-r,y+l-r,0),(x+r,y+l-r,90),(x+r,y+r,180)]:
        for i in range(9):
            a=math.radians(a0+i*90/8);ring.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    for i in range(len(ring)):
        a,b=ring[i],ring[(i+1)%len(ring)]
        if b[0]-a[0]<-0.0001 or b[1]-a[1]>0.0001: poly([(*a,z),(*b,z),(*b,z+h),(*a,z+h)],c[0] if b[0]<a[0] else c[1])
    poly([(*v,z+h) for v in ring],c[2])


base=['#7d8b90','#657983','#b7bdba'];wall=['#809398','#657f89','#b8c2c2']
box(0,0,16,16,-2.6,2.6,base)
for y,l in [(0,9.5),(12.7,3.3)]:box(0,y,.18,l,0,2.5,wall)
for x,w in [(0,12),(15,1)]:box(x,0,w,.18,0,2.5,wall)
# Continuous orthogonal road: both exits connected, broad open turn.
poly([(0,9.5,.015),(15,9.5,.015),(15,12.7,.015),(0,12.7,.015)],'#7e949f')
poly([(12,0,.015),(15,0,.015),(15,12.7,.015),(12,12.7,.015)],'#7e949f')
# A: four storeys, upper pair set back; different body widths/deep facade.
box(.6,.7,4.7,7,0,5.6,['#b2aaa0','#879ba6','#c2c7c5'])
box(.6,.7,3.6,5,5.6,5.6,['#a6adb0','#758d9e','#c5ccca'])
# Floor bands match the base axes. Windows recessed in common planes.
for z in [2.8,5.6]:
    poly([(.6,7.71,z-.08),(5.3,7.71,z-.08),(5.3,7.71,z+.08),(.6,7.71,z+.08)],'#4b626e')
    poly([(5.31,.7,z-.08),(5.31,7.7,z-.08),(5.31,7.7,z+.08),(5.31,.7,z+.08)],'#4b626e')
for z in [1,3.8]:
    for x in [1.0,2.4,3.8]:poly([(x,7.72,z),(x+1,7.72,z),(x+1,7.72,z+1.3),(x,7.72,z+1.3)],'#536c7a')
for z in [6.3,9.1]:
    for y in [1.1,2.7,4.3]:poly([(4.21,y,z),(4.21,y+1.05,z),(4.21,y+1.05,z+1.35),(4.21,y,z+1.35)],'#536c7a')
poly([(5.32,5.4,0),(5.32,6.8,0),(5.32,6.8,2.4),(5.32,5.4,2.4)],'#385464')
box(1.1,1.1,2.6,3.5,11.2,.55,wall)
box(1.0,5.95,3.9,1.35,5.6,.4,wall)
box(4.45,1.0,.6,3.6,5.6,.5,wall)
# B: two-storey rounded corner service building; no rooftop house.
rounded(7,.6,4.3,4.1,0,5.6,.85,['#b4a790','#8e9fa5','#c8c3b5'])
for z in [1.1,3.9]:
    poly([(7.9,4.72,z),(10.4,4.72,z),(10.4,4.72,z+1.25),(7.9,4.72,z+1.25)],'#516674')
poly([(11.32,2.4,0),(11.32,3.7,0),(11.32,3.7,2.4),(11.32,2.4,2.4)],'#385464')
box(7.5,1,3.3,2.8,5.6,.7,wall)
# A single parked car outside both street approaches and the turn.
rounded(6.6,13.7,4.1,1.65,.15,1.0,.4,['#778b9c','#536f82','#a4b2b8'])
box(7.55,13.85,1.9,1.3,1.15,.5,['#607988','#476575','#92a9b0'])
d.text((70,45),'SCENE GEOMETRY / one orthographic camera / all straight structure shares XY',fill='#203943')
d.text((70,75),'A four-storey setback. B two-storey curved corner. Two rear street exits.',fill='#203943')
d.text((70,1190),'Blue road zones are guide-only. Preserve clear street bend and base edge visibility.',fill='#203943')
d.text((70,1220),'No source labels in final. Round building corners do not change the square base.',fill='#203943')
im.save(P/'structure_guide.png')
plan={'camera':{'type':'orthographic_parallel','origin':[650,460],'X':[28,16],'Y':[-28,16],'Z':[0,-30]},'base':{'size':[16,16],'depth':2.6},'current_request_height_exception':'Explicit2–4storey request takes precedence over default approximate6.5m. A4storeys at2.8m plan; B2storeys at2.8m. Current scene only, no global master update/metric certification.','buildings':[{'id':'A','storeys':4,'main_lower_box':[.6,.7,5.3,7.7,0,5.6],'setback_upper_box':[.6,.7,4.2,5.7,5.6,11.2],'entrance':'ordinary closed human door on yard-facing ground floor','roof_plan':'main roof maintenance core9.1 of18=50.6%; lower setback roof maintenance canopies5.265+2.16 of14.9=49.8%, visual output check required'},{'id':'B','storeys':2,'box':[7,.6,11.3,4.7,0,5.6],'ground_corner_radius':.85,'entrance':'closed ordinary human door on right-facing ground floor','roof_plan':'integrated reclaimed heat-exchange canopy9.24 of17.63=52.4%; no duplicate house'}],'car':{'count':1,'parking':[6.6,13.7,10.7,15.35],'outside_through_lane':True},'exits':[{'direction':'rear-left','world':'x0,y9.5..12.7','type':'open street between side boundary and stepped building','route':'clear straight lane to broad central turn'},{'direction':'rear-right','world':'y0,x12..15','type':'open road continuation beside rounded building','route':'clear straight lane meeting same turn'}],'center':'broad flat road bend, no combat obstruction','weather':'night cool wet road neon','cutaway':'concrete foundation/drainage collector/repaired power trunk; no extra doorway','actual_collision_checked':False,'guide_is_not_forced_geometry':True}
(P/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')

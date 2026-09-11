from pathlib import Path
from PIL import Image, ImageDraw
import math, json, hashlib

P=Path(__file__).resolve().parent
ROOT=P.parents[1]
im=Image.new('RGB',(1300,1120),'#efece3');d=ImageDraw.Draw(im)
def pt(x,y,z): return (650+28*x-28*y,250+16*x+16*y-34*z)
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

base=['#a89477','#9e886e','#d4c7ab'];wall=['#798487','#63777e','#a3abad']
box(0,0,16,16,-2.3,2.3,base)
for y,l in [(0,10.5),(13.8,2.2)]:box(0,y,.18,l,0,2.8,wall)
for x,w in [(0,12),(14.8,1.2)]:box(x,0,w,.18,0,2.8,wall)
# The two transition surfaces are guide colors only.
poly([(0,10.5,.01),(5.8,10.5,.01),(5.8,13.8,.01),(0,13.8,.01)],'#a4d4ce')
poly([(12,0,.01),(14.8,0,.01),(14.8,6,.01),(12,6,.01)],'#a4d4ce')
# One rounded-corner workshop with a shorter attached stepped service tower.
rounded(.6,1,4.8,7.6,0,3.8,.7,['#b69d76','#b49f7f','#d6c5a4'])
rounded(.8,1.2,2.8,2.7,3.8,2,.4,['#809c9c','#6e888f','#a8b7b2'])
# Large supported roof service cover and a deliberate open maintenance strip.
box(1.1,4.2,3.8,3.8,3.8,.25,['#708a92','#6b8087','#a4b8b8'])
box(1.25,1.6,1.9,1.6,5.8,.3,wall)
box(3.95,1.6,.7,2.0,3.8,.6,wall)
# Recessed yard-facing workshop shutter on the main straight wall.
poly([(5.42,4.6,0),(5.42,7.0,0),(5.42,7.0,2.7),(5.42,4.6,2.7)],'#45585d')
for z in [.4,.8,1.2,1.6,2,2.4]:d.line([pt(5.44,4.6,z),pt(5.44,7,z)],fill='#9caaa9',width=2)
# Nonbuilding modular induction-sorter / charging rig, NOT a barrel or a second dwelling.
rounded(7,.5,4.8,3.0,0,2.6,.6,['#b9a578','#a99061','#d5c79e'])
rounded(7.1,.65,1.45,2.5,2.6,1.7,.25,['#788f92','#627f89','#9fb0ae'])
box(9.3,.9,1.5,1.5,2.6,.4,wall)
poly([(8.0,3.53,.7),(11.2,3.53,.7),(11.2,3.53,2.15),(8,3.53,2.15)],'#56696e')
for x in [8.45,9.1,9.75,10.4]:
    v=pt(x,3.57,1.4);d.ellipse([v[0]-8,v[1]-8,v[0]+8,v[1]+8],fill='#c6bc93',outline='#344449',width=2)
# Rear-right CLOSED roller gate, opens upward without a ground swing leaf.
box(11.8,0,.2,.5,0,3.35,wall);box(14.8,0,.2,.5,0,3.35,wall)
box(12,0,2.8,.4,0,3.0,['#687f87','#687f87','#9cacaa'])
box(11.8,0,3.2,.6,3,.4,wall)
for z in [.4,.8,1.2,1.6,2,2.4,2.8]:d.line([pt(12,.42,z),pt(14.8,.42,z)],fill='#b4c0ba',width=2)
# Low peripheral sorted scrap: do not conceal the long base comparison edges.
for x,y in [(1,14),(2.7,14),(13.9,10),(13.9,12)]:box(x,y,1.3,1.2,0,.8,wall)
poly([(6.3,7,.02),(10.2,7,.02),(10.2,11,.02),(6.3,11,.02)],'#b0b8aa')
d.text((70,45),'ORTHOGRAPHIC STRUCTURE / geometry and form only / no labels in final',fill='#263e44')
d.text((70,75),'Base X=(28,16), Y=(-28,16), Z=(0,-34). Same vectors at every height.',fill='#263e44')
d.text((70,980),'A: open delivery gap. B: closed upward roller gate. Two rear transitions only.',fill='#263e44')
d.text((70,1010),'All base corners / rear barrier ends inside frame. Curve tangents are not straight-axis edges.',fill='#263e44')
im.save(P/'structure_guide.png')
plan={'projection':'orthographic_parallel','guide_camera':{'origin':[650,250],'X':[28,16],'Y':[-28,16],'Z':[0,-34]},'base':{'square':[16,16],'depth':2.3},'buildings':[{'id':'workshop_with_service_tower','footprint':[.6,1,5.4,8.6],'ground_corner_radius':.7,'body_height':3.8,'tower_footprint':[.8,1.2,3.6,3.9],'total_height':5.8,'entrances':'closed human workshop shutter and ordinary personnel door; not map exits','roof_plan':'main maintenance canopy14.44 + tower7.56 + vent1.4 of36.48 =64%; tower functional cover3.04 of7.56=40.2%, approximate plan only'}],'nonbuilding':'stepped modular induction-sorter and charging rig, retro analog control bank','exits':[{'id':'A','direction':'rear-left','type':'open delivery gap','range_y':[10.5,13.8],'approach':'clear dry level route, no leaf'},{'id':'B','direction':'rear-right','type':'closed salvage roller gate','range_x':[12,14.8],'post_clear':'rolls upward into housing; level route to exterior','approach':'clear center to gate, no boxes in opening'}],'center':'clear center and transit paths; flush weighing pad','cutaway':'dry strata, foundations, broad old power conduits, no basement rooms','actual_collision_verified':False,'plan_is_not_result_QA':True}
(P/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')

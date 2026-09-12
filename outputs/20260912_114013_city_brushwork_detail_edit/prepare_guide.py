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



base=['#7d8b90','#657983','#b7bdba'];wall=['#809398','#657f89','#b8c2c2'];machine=['#516776','#395362','#789398'];house=['#b2aaa0','#879ba6','#c2c7c5']
box(0,0,16,16,-2.6,2.6,base)
for y,l in [(0,9.5),(12.7,3.3)]:box(0,y,.18,l,0,2.5,wall)
for x,w in [(0,12),(15,1)]:box(x,0,w,.18,0,2.5,wall)
poly([(0,9.5,.015),(15,9.5,.015),(15,12.7,.015),(0,12.7,.015)],'#8c9092')
poly([(12,0,.015),(15,0,.015),(15,12.7,.015),(12,12.7,.015)],'#8c9092')
# A floors 1 and 2; floor 3 all equipment; larger floor 4.
box(1.2,1.3,3.5,5.8,0,2.8,house)
for x in [1.2,4.45]:
 for y in [1.3,6.8]:box(x,y,.25,.3,0,2.6,wall)
box(.6,.7,4.7,7,2.6,.2,machine)
box(.6,.7,4.7,7,2.8,2.8,house)
box(.9,1,3.1,4.8,5.6,2.8,machine)
for x in [.9,3.75]:
 for y in [1,5.5]:box(x,y,.25,.3,5.6,2.8,wall)
box(.6,.7,4.1,5.8,8.4,2.8,house)
box(.6,.7,4.1,5.8,8.2,.2,machine)
box(1,1.1,3.2,3.9,11.2,.55,wall)
box(1,6.5,3.6,1,5.6,.5,wall)
# B equipment ground floor, larger translated upper level, rounded identity retained.
rounded(7,.6,4.3,4.1,0,2.8,.65,machine)
rounded(6.7,.7,5,4.7,2.8,2.8,.85,house)
box(7.1,1.1,4.0,3.2,5.6,.6,wall)
for x in [7,10.9]:
 for y in [1,4.2]:box(x,y,.28,.28,0,2.8,wall)
rounded(6.6,13.7,4.1,1.65,.15,1,.4,['#778b9c','#536f82','#a4b2b8'])
box(7.55,13.85,1.9,1.3,1.15,.5,wall)
d.text((70,45),'EDIT GEOMETRY ONLY / daylight, dry street / preserve target scene identity',fill='#203943')
d.text((70,75),'A: smaller ground floor / wider 2nd / equipment 3rd / larger 4th. B preserved.',fill='#203943')
d.text((70,1210),'Dark volumes = equipment storeys. One orthographic camera. No labels in final.',fill='#203943')
im.save(P/'structure_guide.png')

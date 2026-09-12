from pathlib import Path
from PIL import Image, ImageDraw
import math, json, hashlib

P=Path(__file__).resolve().parent
ROOT=P.parents[1]
im=Image.new('RGB',(1300,1360),'#efece3');d=ImageDraw.Draw(im)
def pt(x,y,z): return (650+24*x-24*y,390+14*x+14*y-29*z)
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




base=['#8a8c84','#737e80','#babcb5'];wall=['#9daca9','#7f979d','#c6cfca'];machine=['#4e6671','#334c5a','#829b9c'];a_color=['#b5b49b','#82958b','#d0cfb7'];b_color=['#809aa5','#576f80','#b8c5c5']
box(0,0,20,20,-2.7,2.7,base)
for y,l in [(0,10),(14,6)]:box(0,y,.22,l,0,2.7,wall)
for x,w in [(0,17),(19.8,.2)]:box(x,0,w,.22,0,2.7,wall)
# Road across the front and straight rear branch between two buildings.
poly([(0,10,.01),(20,10,.01),(20,14,.01),(0,14,.01)],'#858889')
poly([(17.2,0,.01),(19.8,0,.01),(19.8,14,.01),(17.2,14,.01)],'#858889')
# A at right: narrow occupied 1 / wide occupied 2 / narrow mechanical 3 / wide occupied 4.
box(12,1.8,4,3.5,0,2.6,a_color)
for x in [12,15.7]:
 for y in [1.8,5]:box(x,y,.3,.3,0,2.6,machine)
box(11,.8,6,5.5,2.6,2.6,a_color)
box(12.2,1.5,3.4,3.8,5.2,2.6,machine)
for x in [12.2,15.3]:
 for y in [1.5,5]:box(x,y,.3,.3,5.2,2.6,wall)
box(11.3,.8,5.5,5.5,7.8,2.6,a_color)
box(11.8,1.3,4.5,3.8,10.4,.5,wall)
# Recessed horizontal window strips on facing surfaces, distinct floor ledges.
for x,y,w,z in [(12,5.31,3.1,.75),(11.6,6.31,4.7,3.3),(11.9,6.31,4.2,8.5)]:
 poly([(x,y,z),(x+w,y,z),(x+w,y,z+1.1),(x,y,z+1.1)],'#385461')
# B left: large rounded occupied upper volume offset over industrial base.
box(1,1,4.6,4.8,0,2.8,machine)
for x in [1,5.3]:
 for y in [1,5.5]:box(x,y,.3,.3,0,2.8,wall)
rounded(.7,.7,6,5.8,2.8,2.7,.6,b_color)
box(1.2,1.2,4.5,3.4,5.5,.6,wall)
poly([(1.4,6.51,3.5),(5.9,6.51,3.5),(5.9,6.51,4.7),(1.4,6.51,4.7)],'#385461')
# Service disposal area: dumpster, refrigerator, washing machine, boxed waste.
box(1.0,7.2,2.2,1.5,0,1.4,machine)
box(3.5,7.4,.85,.9,0,1.75,wall)
box(4.6,7.7,.9,.9,0,.9,wall)
box(5.6,8.1,.7,.7,0,.55,a_color)
# TWO parked vehicles outside main road: sedan and visibly open-bed pickup.
rounded(2,16.1,4.5,1.85,.2,.85,.35,b_color)
box(3.05,16.25,2.05,1.55,1.05,.65,machine)
rounded(12,16,5.5,2.05,.2,1.0,.25,a_color)
box(12.8,16.1,1.8,1.85,1.2,.8,b_color)
box(15.05,16.12,2.25,1.8,1.2,.16,machine)
box(15.05,16.02,2.35,.16,1.2,.6,a_color)
box(15.05,17.89,2.35,.16,1.2,.6,a_color)
box(17.28,16.05,.16,1.95,1.2,.6,a_color)
box(11,8.9,.35,.4,0,.9,['#975a43','#703c2a','#be8761'])
d.text((65,50),'NEW CITY / orthographic structure / A four storeys / B two storeys',fill='#203943')
d.text((65,77),'2 vehicles: sedan + open-bed pickup. Appliances/dumpster beside B. Keep grey routes open.',fill='#203943')
d.text((65,1250),'Guide only: windows/entrances/machinery/large tile designs refined in final. No labels.',fill='#203943')
im.save(P/'structure_guide.png')

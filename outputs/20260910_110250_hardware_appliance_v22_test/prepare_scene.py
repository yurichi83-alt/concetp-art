from pathlib import Path
import json, math, hashlib
import numpy as np
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
W,H=1280,1050
im=Image.new('RGB',(W,H),'#17212e')
draw=ImageDraw.Draw(im)
faces=[]
segments=[]
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1050" viewBox="0 0 1280 1050"><rect width="1280" height="1050" fill="#17212e"/>']
def p(v):
 x,y,z=v
 return (640+32*(x-y),310+32/math.sqrt(3)*(x+y)-64/math.sqrt(3)*z)
def poly(v,col,stroke='#33414d',width=2):
 faces.append((v,col,stroke,width))
 pts=[p(q) for q in v]
 draw.polygon(pts,fill=col)
 draw.line(pts+[pts[0]],fill=stroke,width=width)
 svg.append('<polygon points="'+ ' '.join(f'{a:.3f},{b:.3f}' for a,b in pts)+'" fill="'+col+'" stroke="'+stroke+'" stroke-width="'+str(width)+'"/>')
def line(v,col='#6f858c',width=2):
 segments.append((v,col,width))
 pts=[p(q) for q in v]
 draw.line(pts,fill=col,width=width)
 svg.append('<polyline points="'+ ' '.join(f'{a:.3f},{b:.3f}' for a,b in pts)+'" fill="none" stroke="'+col+'" stroke-width="'+str(width)+'"/>')
def plane(a,b,c,d,z,col):
 poly([(a,c,z),(b,c,z),(b,d,z),(a,d,z)],col)
def box(a,b,c,d,z,h,colors=('#7e929b','#637986','#9aadb3')):
 poly([(b,c,z),(b,d,z),(b,d,h),(b,c,h)],colors[0])
 poly([(a,d,z),(b,d,z),(b,d,h),(a,d,h)],colors[1])
 plane(a,b,c,d,h,colors[2])
base=(0,16,0,16,-1.2,0)
box(*base,('#5d6675','#4d5666','#8b999e'))
for n in range(2,16,2):
 line([(n,0,.01),(n,16,.01)])
 line([(0,n,.01),(16,n,.01)])
# Protected walking surfaces: no marks required in the art.
plane(0,8,11,14,.02,'#809f9c')
plane(12.3,15.3,0,13.5,.02,'#809f9c')
plane(6,12.3,7,13.5,.025,'#95aaa3')
# Two perpendicular rear boundaries; one gate each. Beyond-threshold floor strip remains.
for c,d in [(0,11),(14,16)]:
 box(.45,.8,c,d,0,2.9,('#6c7e8a','#596b79','#82919a'))
box(.45,.8,11,14,2.55,2.9,('#6c7e8a','#596b79','#82919a'))
for a,b in [(0,12.3),(15.3,16)]:
 box(a,b,.45,.8,0,2.9,('#6c7e8a','#596b79','#82919a'))
box(12.3,15.3,.45,.8,2.55,2.9,('#6c7e8a','#596b79','#82919a'))
# Left ruined hardware room, retained modern structural frame, open front wall section.
plane(1,4.8,1,9.6,.035,'#868b83')
box(1,1.25,1,9.6,0,3.8,('#657c7c','#58716f','#88a09a'))
box(1,4.8,1,1.25,0,3.8,('#657c7c','#58716f','#88a09a'))
box(1,4.8,9.35,9.6,0,3.8,('#657c7c','#58716f','#88a09a'))
# Wall-side workbench and a power module leave interior aisle x2.3..4.5 free.
box(1.4,2.1,3.3,6.4,0,.85,('#8c887a','#797362','#b9ad90'))
box(1.4,2.1,7,8.3,0,1.7,('#858b81','#767d75','#a8afa0'))
box(1,2.0,1,9.6,3.62,3.8,('#667c7a','#596c69','#8ea29a'))
box(4.55,4.8,1,3,0,3.8,('#70857e','#697f76','#99a59a'))
box(4.55,4.8,8.7,9.6,0,3.8,('#70857e','#697f76','#99a59a'))
box(4.55,4.8,3,8.7,3.2,3.8,('#70857e','#697f76','#99a59a'))
# Debris confined below the hole; clear of y11..14 route and x>=6 center.
for a,b,c,d,h in [(4.85,5.35,4,4.7,.35),(4.9,5.65,5.6,6.1,.25),(4.9,5.45,7.5,8.2,.4)]:
 box(a,b,c,d,0,h,('#858a81','#747b70','#a6ac9c'))
# Appliance building: h=4.94 = hardware h*1.3. Left third is integrated mechanical service bay.
plane(5.4,11.4,1,6,.04,'#a9a695')
box(5.4,11.4,1,1.25,0,4.94,('#858882','#73796f','#a2a799'))
box(11.15,11.4,1,2.65,0,4.94,('#888e83','#757d72','#aeb0a0'))
box(11.15,11.4,2.65,6,0,.25,('#888e83','#757d72','#aeb0a0'))
box(5.4,7.4,1.25,6,0,4.94,('#918a73','#7c7867','#b7ac8c'))
# Showroom perimeter merchandise only, entry and aisle open.
for a,b,c,d,h in [(7.65,8.5,1.55,2.3,1.7),(8.8,9.6,1.55,2.3,1.25),(10.15,10.95,3.0,3.8,1.1)]:
 box(a,b,c,d,0,h,('#bdbaa1','#a6aa94','#d7d3b8'))
box(7.4,7.62,5.8,6,0,4.7,('#a0a18c','#8b907e','#c2c2a6'))
box(7.4,11.4,5.8,6,4.5,4.94,('#939986','#7a8474','#b3b8a0'))
# Retained rear roof; open front roof slice exposes real room depth.
box(7.4,11.4,1,2.65,4.72,4.94,('#9b9d8c','#8a9280','#c0c3ad'))
box(5.8,6.9,1.5,2.8,4.94,5.65,('#71808a','#596f7a','#8b9ca4'))
poly([(8,1.35,5.1),(10.8,1.35,5.1),(10.8,2.5,5.55),(8,2.5,5.55)],'#416579','#7591a1')
# Some large infrastructure inside planar cuts; corners stay straight.
line([(16,2,-.55),(16,13,-.55)],'#b49d72',10)
line([(3,16,-.6),(12.5,16,-.6)],'#6e9daa',10)
svg.append('</svg>')
# Render the new 3D schematic with a depth buffer; avoid painter-order occlusion errors.
canvas=np.full((H,W,3),[23,33,46],dtype=np.uint8)
depth=np.full((H,W),-1e9,dtype=float)
def rgb(c):
 return tuple(int(c[i:i+2],16) for i in (1,3,5))
def tri(v,col):
 q=np.array([p(a) for a in v]); zz=np.array([sum(a) for a in v])
 xmin=max(0,int(np.floor(q[:,0].min()))); xmax=min(W-1,int(np.ceil(q[:,0].max())))
 ymin=max(0,int(np.floor(q[:,1].min()))); ymax=min(H-1,int(np.ceil(q[:,1].max())))
 xx,yy=np.meshgrid(np.arange(xmin,xmax+1)+.5,np.arange(ymin,ymax+1)+.5)
 den=(q[1,1]-q[2,1])*(q[0,0]-q[2,0])+(q[2,0]-q[1,0])*(q[0,1]-q[2,1])
 if abs(den)<1e-9: return
 a=((q[1,1]-q[2,1])*(xx-q[2,0])+(q[2,0]-q[1,0])*(yy-q[2,1]))/den
 b=((q[2,1]-q[0,1])*(xx-q[2,0])+(q[0,0]-q[2,0])*(yy-q[2,1]))/den
 c=1-a-b; z=a*zz[0]+b*zz[1]+c*zz[2]
 db=depth[ymin:ymax+1,xmin:xmax+1]
 mask=(a>=-.0001)&(b>=-.0001)&(c>=-.0001)&(z>=db)
 db[mask]=z[mask]; canvas[ymin:ymax+1,xmin:xmax+1][mask]=rgb(col)
for v,col,stroke,width in faces:
 for k in range(1,len(v)-1): tri([v[0],v[k],v[k+1]],col)
def depthline(a,b,col,width):
 x1,y1=p(a); x2,y2=p(b)
 count=max(2,int(max(abs(x2-x1),abs(y2-y1))*2))
 for t in np.linspace(0,1,count):
  x=round(x1+(x2-x1)*t); y=round(y1+(y2-y1)*t); z=sum(a)+(sum(b)-sum(a))*t
  for dx in range(-(width//2),width//2+1):
   for dy in range(-(width//2),width//2+1):
    u,vv=x+dx,y+dy
    if 0<=u<W and 0<=vv<H and z+.07>=depth[vv,u]: canvas[vv,u]=rgb(col)
for v,col,stroke,width in faces:
 for a,b in zip(v,v[1:]+v[:1]): depthline(a,b,stroke,width)
for v,col,width in segments:
 for a,b in zip(v,v[1:]): depthline(a,b,col,width)
im=Image.fromarray(canvas)
im.save(RUN/'structure_plan.png')
routes=[
 {'id':'left_exit','box':[0,8,11,14,0,2.4],'gate':[.45,.8,11,14,0,2.55]},
 {'id':'right_exit','box':[12.3,15.3,0,13.5,0,2.4],'gate':[12.3,15.3,.45,.8,0,2.55]},
 {'id':'center','box':[6,12.3,7,13.5,0,2.4]},
 {'id':'hardware_interior','box':[2.3,4.5,3.1,8.5,0,2.4]},
 {'id':'showroom_interior','box':[8.5,10.0,2.5,6.5,0,2.4]}]
obstacles=[
 {'id':'hardware_body','box':[1,4.8,1,9.6,0,3.8]},
 {'id':'appliance_body','box':[5.4,11.4,1,6,0,4.94]},
 {'id':'rubble_reserved','box':[4.8,5.7,3.5,8.5,0,.5]}]
def intersects(a,b):
 return all(min(a[i+1],b[i+1]) > max(a[i],b[i]) for i in (0,2,4))
collisions=[(r['id'],o['id']) for r in routes[:3] for o in obstacles if intersects(r['box'],o['box'])]
assert not collisions, collisions
plan={'master_version':'2.2','projection':{'type':'orthographic','basis':{'X':[32,32/math.sqrt(3)],'Y':[-32,32/math.sqrt(3)],'Z':[0,-64/math.sqrt(3)]},'origin':[640,310]},'units':'scene meters for this plan only, not permanent master or pixel measurement','base':{'footprint':[0,16,0,16],'top_z':0,'bottom_z':-1.2,'corner_count':4,'bevel':False},'virtual_frame':[0,16,0,16,0,16],'routes':routes,'obstacles':obstacles,'building_height_ratio':4.94/3.8,'machine_bay_fraction':2/6,'route_collision_results':collisions,'validation_scope':'axis-aligned plan volumes; final image separately inspected; not a mesh or collider certification','guide_role':'current-run structure only, not a new approved positive master','method':'new geometric schematic generated from coordinates; no source/art images edited'}
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
wanted=['M02-01','M01-01','M03-10','M04-02','M03-06']
inputs=[{'order':1,'id':'scene_structure_guide','path':str(RUN/'structure_plan.png'),'role':'current scene structure guide','exclude':'guide flat colors/grid/route tint are not requested art markings','visually_inspected':False,'submitted':False}]
for i,key in enumerate(wanted,2):
 ref=next(r for r in manifest['references'] if r['id']==key)
 inputs.append({'order':i,'id':key,'path':str(ROOT/ref['path']),'role':ref['use_only'],'exclude':ref['exclude'],'sha256':ref['sha256'],'visually_inspected':True,'submitted':False})
(RUN/'references.json').write_text(json.dumps({'inputs':inputs,'omitted':'Other LDI supplements, preferred/generated outputs unnecessary for roles; rejected geometry outputs excluded.','master_version':'2.2','tool_input_mechanism':'referenced_image_paths'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'guide':str(RUN/'structure_plan.png'),'collisions':collisions,'input_count':len(inputs)}))

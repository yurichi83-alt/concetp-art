"""Task-specific orthographic blockout; not generated artwork or a previous output."""
from pathlib import Path
import json, math
from PIL import Image, ImageDraw, ImageColor
import numpy as np

OUT = Path(__file__).resolve().parent
W, H = 1600, 1200
S, CX, CY = 43.0, 800.0, 370.0
def p(x,y,z=0): return (CX+(x-y)*S*math.sqrt(3)/2, CY+(x+y)*S*.5-z*S)
faces=[]
def face(pts,fill,outline='#55575a'):
    faces.append((sum(x+y+z for x,y,z in pts)/len(pts), pts,fill,outline))
def box(x0,y0,z0,x1,y1,z1,top='#c9c8c1',left='#9c9d99',right='#b2b2ad'):
    face([(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)],top)
    face([(x0,y1,z0),(x1,y1,z0),(x1,y1,z1),(x0,y1,z1)],left)
    face([(x1,y0,z0),(x1,y1,z0),(x1,y1,z1),(x1,y0,z1)],right)

plan={
 'scope':'New scene geometric guide only; no previous generated images used.',
 'projection':{'type':'orthographic','world_axes':'X toward image lower right; Y toward image lower left; Z vertical up','formula':'u=800+(x-y)*43*sqrt(3)/2; v=370+(x+y)*43/2-z*43','image_size':[W,H],'scale_px_per_m':S,'same_z_drop_screen_vector_for_base':[0,1.2*S]},
 'base':{'square_xy':[[0,0],[14,0],[14,14],[0,14]],'surface_z':0,'bottom_z':-1.2,'front_cutaway_faces':['x=14','y=14'],'curvature':False,'bevels':False},
 'buildings':[
  {'id':'A','use':'Two-floor repaired machine service house','footprint':[[0,0],[3.4,0],[3.4,5.8],[0,5.8]],'height':5.2,'machine_design_target':0.4,'machine_ratio_note':'Approximate exterior design target: integrated lower machinery zone height 2.1 of 5.2; final image ratio remains visual estimate, not exact pixel/volume claim. Ground floor doorway remains visible.','entry':{'plane':'x=3.4','y_range':[4.3,5.35],'height':2.0,'role':'decorative building entrance'},'roof':[{'xy':[0.3,0.5,2.5,4.9],'z':[5.2,6.2],'use':'supported connected ventilation/power assembly'}],'roof_plan_occupancy':round(2.2*4.4/(3.4*5.8),4)},
  {'id':'B','use':'Low narrow service warehouse','footprint':[[6,0],[12.4,0],[12.4,3],[6,3]],'height':3.1,'entry':{'plane':'y=3','x_range':[8.3,10.1],'height':2.3,'role':'decorative closed shutter'},'roof':[{'xy':[6.5,0.45,11,2.55],'z':[3.1,3.85],'use':'connected storage/weather hood and exhaust module'}],'roof_plan_occupancy':round(4.5*2.1/(6.4*3),4)}
 ],
 'functional_exits':[
  {'id':'left_11','boundary':'x=0','boundary_interval_y':[7.4,9.8],'clear_corridor_xy':[0,7.4,5.7,9.8],'state':'open','width':2.4,'after_clear':'continue through same level boundary opening into unseen next alley','building_entry_shared':False},
  {'id':'right_1','boundary':'y=0','boundary_interval_x':[3.8,5.8],'clear_corridor_xy':[3.8,0,5.8,7.4],'state':'open','width':2.0,'after_clear':'continue through same level boundary opening into unseen next alley','building_entry_shared':False}
 ],
 'central_open_area_xy':[5.8,4.0,11.8,12.2],
 'props':[{'id':'bin','xy':[7.0,3.35,8.4,4.0]},{'id':'scrap','xy':[0.7,12,2.4,13.1]},{'id':'planks','xy':[1.0,10.5,2.4,11.7]}],
 'notes':['Buildings use world X/Y orthogonal edges throughout. Roof installations supported on flat roofs.','Boundary blockers fill both back edges except the two specified passages. No material pile or swinging gate enters either protected corridor.','Guide validates planned geometry only. Generated image needs independent geometry, occupancy, framing and exit QA.','Guide color blocks do not prescribe final palette, lighting or machine surface detail. No text is drawn into guide.']
}

# Base. Draw its top and two equal-depth front cutaway planes explicitly.
im=Image.new('RGB',(W,H),'#e8e7e1'); d=ImageDraw.Draw(im)
for pts,col in [([(0,0,0),(14,0,0),(14,14,0),(0,14,0)],'#bcbdb8'), ([(0,14,0),(14,14,0),(14,14,-1.2),(0,14,-1.2)],'#777b7c'), ([(14,0,0),(14,14,0),(14,14,-1.2),(14,0,-1.2)],'#929694')]:
    d.polygon([p(*q) for q in pts],fill=col,outline='#424a4e',width=4)
for axis in range(2):
    for n in [2,4,6,8,10,12]:
        a,b=((n,0,0),(n,14,0)) if axis==0 else ((0,n,0),(14,n,0))
        d.line([p(*a),p(*b)],fill='#b0b3ae',width=2)
# Light unobtrusive clear lane surfaces identify topology, not final paving design.
for e in plan['functional_exits']:
    x0,y0,x1,y1=e['clear_corridor_xy']
    d.polygon([p(x0,y0),p(x1,y0),p(x1,y1),p(x0,y1)],fill='#cbd2cb')

# West / left boundary. Building A fills y=0..5.8; passage 7.4..9.8.
box(0,5.8,0,.20,7.4,2.3)
box(0,9.8,0,.20,14,2.3)
# North / right boundary. Passage x=3.8..5.8; building B x=6..12.4.
box(3.4,0,0,3.8,.2,2.3)
box(5.8,0,0,6,.2,2.3)
box(12.4,0,0,14,.2,2.3)
# Two-floor A: lower machinery zone and upper intact wall volume.
box(0,0,0,3.4,5.8,2.1,top='#ab9d82',left='#8b8170',right='#a3987e')
box(0,0,2.1,3.4,5.8,5.2,top='#d3d0c2',left='#b9b5a8',right='#ccc6b5')
box(.3,.5,5.2,2.5,4.9,6.2,top='#b5b7b0',left='#8e9693',right='#a4aba5')
# House entry and upper windows on world X-facing facade.
face([(3.405,4.3,0),(3.405,5.35,0),(3.405,5.35,2),(3.405,4.3,2)],'#525b59')
for ya,yb in [(1.0,2.1),(3.6,4.7)]:
    face([(3.41,ya,3),(3.41,yb,3),(3.41,yb,4.15),(3.41,ya,4.15)],'#798782')
# Ground machinery only broad blocks; the supplied image provides actual design.
for ya,yb in [(.4,1.6),(2.0,3.4)]:
    box(3.4,ya,.25,3.7,yb,1.85,top='#a99d83',left='#938773',right='#b3a386')
box(6,0,0,12.4,3,3.1,top='#bbbebd',left='#989f9e',right='#a9b0ae')
box(6.5,.45,3.1,11,2.55,3.85,top='#adb5b3',left='#818e8c',right='#96a3a0')
face([(8.3,3.01,0),(10.1,3.01,0),(10.1,3.01,2.3),(8.3,3.01,2.3)],'#646f6d')
# Props kept outside every exit clear zone and central walking rectangle.
box(7,3.35,0,8.4,4.0,1.15,top='#87938a',left='#657468',right='#778579')
box(.7,12,0,2.4,13.1,.7,top='#979c99',left='#747c79',right='#87918b')
box(1,10.5,0,2.4,11.7,.25,top='#b8a78b',left='#8d806b',right='#a7967e')
# Orthographic triangle Z-buffer prevents coplanar facade details and foreground
# props being overwritten by an incorrect painter ordering.
pix=np.array(im); zb=np.full((H,W),-1e9,dtype=float)
for _,pts,col,line in faces:
    screen=np.array([p(*q) for q in pts]); depth=np.array([sum(q) for q in pts])
    for inds in [(0,1,2),(0,2,3)]:
        a,b,c=screen[list(inds)]; dz=depth[list(inds)]
        lx=max(0,int(np.floor(min(a[0],b[0],c[0])))); rx=min(W-1,int(np.ceil(max(a[0],b[0],c[0]))))
        ly=max(0,int(np.floor(min(a[1],b[1],c[1])))); ry=min(H-1,int(np.ceil(max(a[1],b[1],c[1]))))
        yy,xx=np.mgrid[ly:ry+1,lx:rx+1]
        den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
        if abs(den)<1e-8: continue
        aa=((b[1]-c[1])*(xx-c[0])+(c[0]-b[0])*(yy-c[1]))/den
        bb=((c[1]-a[1])*(xx-c[0])+(a[0]-c[0])*(yy-c[1]))/den
        cc=1-aa-bb; zz=aa*dz[0]+bb*dz[1]+cc*dz[2]
        tile=zb[ly:ry+1,lx:rx+1]; mask=(aa>=-1e-6)&(bb>=-1e-6)&(cc>=-1e-6)&(zz>=tile-1e-7)
        tile[mask]=zz[mask]; pix[ly:ry+1,lx:rx+1][mask]=ImageColor.getrgb(col)
# Visible edge segments only; compare their interpolated depth with the Z-buffer.
for _,pts,col,line in faces:
    for va,vb in zip(pts,pts[1:]+pts[:1]):
        aa=np.array(p(*va)); bb=np.array(p(*vb)); count=int(np.linalg.norm(bb-aa)*2)+1
        for t in np.linspace(0,1,count):
            q=aa*(1-t)+bb*t; x,y=int(round(q[0])),int(round(q[1])); z=sum(va)*(1-t)+sum(vb)*t
            if 1<=x<W-1 and 1<=y<H-1 and z>=zb[y,x]-.05:
                pix[y-1:y+2,x-1:x+2]=ImageColor.getrgb(line)
im=Image.fromarray(pix)

def overlap(a,b): return a[0]<b[2] and a[2]>b[0] and a[1]<b[3] and a[3]>b[1]
obstacles=[(b['id'],[min(v[0] for v in b['footprint']),min(v[1] for v in b['footprint']),max(v[0] for v in b['footprint']),max(v[1] for v in b['footprint'])]) for b in plan['buildings']]+[(x['id'],x['xy']) for x in plan['props']]
conflicts=[(e['id'],name) for e in plan['functional_exits'] for name,rect in obstacles if overlap(e['clear_corridor_xy'],rect)]
assert not conflicts, conflicts
assert all(.4<=b['roof_plan_occupancy']<=.8 for b in plan['buildings'])
points=[p(x,y,z) for x in [0,14] for y in [0,14] for z in [-1.2,0]]+[p(*v) for _,vs,_,_ in faces for v in vs]
assert all(50<x<W-50 and 50<y<H-50 for x,y in points)
plan['plan_validation']={'corridor_AABB_conflicts':conflicts,'orthogonal_building_footprints':True,'all_geometry_inside_50px_safe_frame':True,'roof_occupancies_in_range':True,'tallest_planned_structure_m':6.2,'projection_x_vector':list(p(1,0)[i]-p(0,0)[i] for i in [0,1]),'projection_y_vector':list(p(0,1)[i]-p(0,0)[i] for i in [0,1]),'disclaimer':'Analytic blockout validation, not final generated-image QA.'}
(OUT/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
im.save(OUT/'structure_guide.png')
print(json.dumps(plan['plan_validation'],ensure_ascii=False))

"""Fresh task-only massing guide. Rounded visual shells use simple axis-aligned bounds.
No earlier generated image is read. Only the rasterization math of a prior guide is reused.
"""
from pathlib import Path
import json, math
import numpy as np
from PIL import Image, ImageDraw, ImageColor

OUT=Path(__file__).resolve().parent
W,H=1600,1200
S,CX,CY=45.,800.,382.
def p(x,y,z=0): return (CX+(x-y)*S*math.sqrt(3)/2,CY+(x+y)*S*.5-z*S)
faces=[]
volumes=[]
def face(pts,col,edge='#555b5c'): faces.append((pts,col,edge))
def box(x0,y0,z0,x1,y1,z1,top='#c9c7bf',left='#989b99',right='#b6b9b4',record=None):
    face([(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)],top)
    face([(x0,y1,z0),(x1,y1,z0),(x1,y1,z1),(x0,y1,z1)],left)
    face([(x1,y0,z0),(x1,y1,z0),(x1,y1,z1),(x1,y0,z1)],right)
    if record: volumes.append({'id':record,'type':'box','visual_AABB':[x0,y0,z0,x1,y1,z1],'collision_AABB':[x0,y0,z0,x1,y1,z1]})
def rounded(x0,y0,z0,x1,y1,z1,r=.4,b=.16,color=(204,181,129),record=None):
    """Rounded XY shell with chamfered crown/bottom, distinct from a yaw-rotated wall."""
    def ring(z,inset):
        rr=max(.04,r-inset); xa,ya,xb,yb=x0+inset,y0+inset,x1-inset,y1-inset
        q=[]
        for cx,cy,aa in [(xb-rr,yb-rr,0),(xa+rr,yb-rr,90),(xa+rr,ya+rr,180),(xb-rr,ya+rr,270)]:
            for i in range(7):
                t=math.radians(aa+i*90/6);q.append((cx+rr*math.cos(t),cy+rr*math.sin(t),z))
        return q
    rings=[ring(z0,b),ring(z0+b,0),ring(z1-b,0),ring(z1,b)]
    top=rings[-1]; center=((x0+x1)/2,(y0+y1)/2,z1)
    for a,c in zip(top,top[1:]+top[:1]):face([center,a,c],tuple(min(255,int(v*1.08)) for v in color),None)
    for ra,rb in zip(rings,rings[1:]):
        for i in range(len(ra)):
            j=(i+1)%len(ra); mx=(ra[i][0]+ra[j][0])/2-(x0+x1)/2; my=(ra[i][1]+ra[j][1])/2-(y0+y1)/2
            light=.86+.12*(mx-my)/(abs(mx)+abs(my)+.01)
            face([ra[i],ra[j],rb[j],rb[i]],tuple(int(v*light) for v in color),None)
    if record: volumes.append({'id':record,'type':'rounded_visual_shell','visual_AABB':[x0,y0,z0,x1,y1,z1],'collision_AABB':[x0,y0,z0,x1,y1,z1],'note':'Collision bounds deliberately rectangular and aligned with common world X/Y; curved shell is a visual shape.'})
def pane_x(x,y0,z0,y1,z1,col='#666f6a'):face([(x,y0,z0),(x,y1,z0),(x,y1,z1),(x,y0,z1)],col)
def pane_y(y,x0,z0,x1,z1,col='#626e6c'):face([(x0,y,z0),(x1,y,z0),(x1,y,z1),(x0,y,z1)],col)

im=Image.new('RGB',(W,H),'#ecebe5');d=ImageDraw.Draw(im)
for pts,col in [([(0,0,0),(14,0,0),(14,14,0),(0,14,0)],'#c6c8c0'), ([(0,14,0),(14,14,0),(14,14,-1.15),(0,14,-1.15)],'#737e7c'), ([(14,0,0),(14,14,0),(14,14,-1.15),(14,0,-1.15)],'#909b99')]:d.polygon([p(*q) for q in pts],fill=col,outline='#4d5857',width=3)
exits=[{'id':'left_11','boundary':'x=0','boundary_interval':[8.,10.4],'protected_walking_volume':[0,8,0,6.5,10.4,3.0],'state':'open','width':2.4},{'id':'right_1','boundary':'y=0','boundary_interval':[4.9,7.2],'protected_walking_volume':[4.9,0,0,7.2,8,3.0],'state':'open','width':2.3}]
for e in exits:
    x0,y0,z0,x1,y1,z1=e['protected_walking_volume'];d.polygon([p(x0,y0),p(x1,y0),p(x1,y1),p(x0,y1)],fill='#d2d6cc')
# Straight boundary planes are broken only at the two functional exits.
box(0,6.9,0,.18,8,2.15)
box(0,10.4,0,.18,14,2.15)
box(4.6,0,0,4.9,.18,2.15)
box(7.2,0,0,8,.18,2.15)
box(12.9,0,0,14,.18,2.15)
# A: narrow ground house, rounded side machine room, tall machine spine.
box(.3,.3,0,2.9,5.65,2.65,top='#b8ae93',left='#938d7d',right='#aaa28b',record='A_ground_house')
rounded(2.85,.9,0,4.6,3.75,2.3,r=.55,b=.12,color=(161,175,169),record='A_round_ground_machine_annex')
box(3.05,1.1,2.3,4.25,3.35,2.65,top='#7f9186',left='#627a6d',right='#718a7c',record='A_load_bearing_machine_collar')
box(.3,.45,0,1.4,2.95,5.2,top='#a2aaa4',left='#757f7c',right='#939e98',record='A_vertical_machine_spine')
# Broad projecting upper capsule makes a genuinely changing main silhouette.
rounded(1.3,.45,2.65,4.6,3.7,5.65,r=.6,b=.3,color=(218,180,113),record='A_projecting_capsule_home')
# Rear upper room and a real unfilled terrace beside it.
box(.3,3.15,2.65,2.5,5.65,4.95,top='#ced1c4',left='#959f96',right='#b3beb0',record='A_setback_rear_home')
box(2.5,3.8,2.55,4.25,5.65,2.72,top='#c7b89a',left='#969185',right='#b0a790',record='A_terrace_slab')
for x,y in [(2.65,5.45),(4.05,5.45)]:box(x,y,0,x+.13,y+.13,2.55,top='#767e79',left='#65706b',right='#73827a',record='A_terrace_support')
for x in [2.6,3.35,4.1]:box(x,5.55,2.72,x+.05,5.6,3.45)
box(2.6,5.55,3.4,4.15,5.61,3.46)
# Two short orthogonal stair flights/landings, entirely inside A's visual reserve.
for i in range(8):box(.55,5.7+i*.145,0,1.55,5.7+(i+1)*.145,(i+1)*.17,top='#afbaa9',left='#7f8d83',right='#96a396')
box(.55,6.65,1.36,2.25,6.9,1.52)
for i in range(7):box(1.55+i*.14,5.72,1.36,1.55+(i+1)*.14,6.65,1.36+(i+1)*.17,top='#afbaa9',left='#7f8d83',right='#96a396')
pane_x(2.91,4.35,.05,5.2,2.15,'#576c61')
pane_x(4.601,1.25,3.35,2.8,4.65,'#7a8e88')
pane_x(4.601,1.4,.35,2.5,1.65,'#818e86')
pane_x(2.51,4,3.1,4.85,4.3,'#788b86')
# Machine connection across the two upper forms, and low rooftop functional equipment.
box(.55,3.8,4.95,2.15,5.2,5.6,top='#aab7ae',left='#72877d',right='#8fa094')
rounded(1.6,.85,5.65,3.85,2.7,6.12,r=.25,b=.1,color=(158,169,158))
box(.55,.6,5.2,1.15,1.7,6.25,top='#9aa89e',left='#687c70',right='#85978b')
# B: asymmetric stacked dwelling, split upper roofline and substantial open porch.
box(8,.3,0,12.9,3.8,2.6,top='#bec4bd',left='#899993',right='#a0b2a7',record='B_ground_shop')
box(8,.3,2.6,10.45,2.8,4.85,top='#b3c4bc',left='#7f9a91',right='#9fb9ad',record='B_upper_timber_home')
box(10.45,.3,2.6,12.55,1.9,5.25,top='#bcb6b4',left='#908583',right='#a79b96',record='B_taller_side_module')
# Single slope roof maintains fixed wall bases and common camera; real supported thickness.
face([(7.85,.15,5.15),(10.6,.15,5.15),(10.6,3.05,4.86),(7.85,3.05,4.86)],'#8b9e93')
face([(7.85,3.05,4.75),(10.6,3.05,4.75),(10.6,3.05,4.86),(7.85,3.05,4.86)],'#6e8278')
box(10.45,1.9,2.5,12.7,3.9,2.65,top='#b8a78a',left='#928771',right='#aa9c80',record='B_open_upper_deck')
for x in [10.5,11.5,12.6]:box(x,3.85,2.65,x+.05,3.9,3.38)
box(10.5,3.85,3.34,12.65,3.91,3.4)
for i in range(15):box(12.2,3.9+i*.15,0,13.05,3.9+(i+1)*.15,2.6-(i*.17),top='#9caf9e',left='#6d8174',right='#859987')
pane_y(3.81,8.45,.05,10.05,2.25,'#65776c')
pane_y(2.81,8.55,3.1,9.75,4.25,'#738b81')
pane_y(1.91,10.95,3.05,11.95,4.6,'#7c8a82')
box(11.05,.55,5.25,12.2,1.65,5.95,top='#b2beb3',left='#7c9083',right='#9aab9c')
box(8.3,.7,5.1,10.05,2,5.45,top='#9daaa2',left='#738277',right='#8a9b8c')
# Requested props occupy edges, avoiding all protected exit volumes.
props=[{'id':'large_bin','bounds':[8.5,4.15,0,9.9,5.05,1.2]},{'id':'scrap','bounds':[1.0,11.6,0,2.8,12.8,.7]},{'id':'planks','bounds':[.65,10.7,0,2.45,11.35,.28]}]
for a in props:box(*a['bounds'],top='#a2a48d',left='#798873',right='#929c84',record=a['id'])

# True orthographic triangle Z buffer, also supporting the many curved-shell facets.
pix=np.array(im);zb=np.full((H,W),-1e9,dtype=float)
for pts,col,line in faces:
    screen=np.array([p(*q) for q in pts]); depth=np.array([sum(q) for q in pts]);rgb=ImageColor.getrgb(col) if isinstance(col,str) else col
    for k in range(1,len(pts)-1):
        inds=[0,k,k+1];a,b,c=screen[inds];dz=depth[inds]
        lx=max(0,int(np.floor(min(a[0],b[0],c[0]))));rx=min(W-1,int(np.ceil(max(a[0],b[0],c[0]))));ly=max(0,int(np.floor(min(a[1],b[1],c[1]))));ry=min(H-1,int(np.ceil(max(a[1],b[1],c[1]))))
        yy,xx=np.mgrid[ly:ry+1,lx:rx+1];den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
        if abs(den)<1e-8:continue
        aa=((b[1]-c[1])*(xx-c[0])+(c[0]-b[0])*(yy-c[1]))/den;bb=((c[1]-a[1])*(xx-c[0])+(a[0]-c[0])*(yy-c[1]))/den;cc=1-aa-bb;zz=aa*dz[0]+bb*dz[1]+cc*dz[2]
        tile=zb[ly:ry+1,lx:rx+1];mask=(aa>=-1e-6)&(bb>=-1e-6)&(cc>=-1e-6)&(zz>=tile-1e-7);tile[mask]=zz[mask];pix[ly:ry+1,lx:rx+1][mask]=rgb
for pts,col,line in faces:
    if line is None:continue
    for va,vb in zip(pts,pts[1:]+pts[:1]):
        aa=np.array(p(*va));bb=np.array(p(*vb));count=int(np.linalg.norm(bb-aa)*2)+1
        for t in np.linspace(0,1,count):
            q=aa*(1-t)+bb*t;x,y=int(round(q[0])),int(round(q[1]));z=sum(va)*(1-t)+sum(vb)*t
            if 1<=x<W-1 and 1<=y<H-1 and z>=zb[y,x]-.05:pix[y-1:y+2,x-1:x+2]=ImageColor.getrgb(line)
Image.fromarray(pix).save(OUT/'structure_guide.png')
def overlap3(a,b):return all(a[i]<b[i+3] and a[i+3]>b[i] for i in range(3))
conflicts=[(e['id'],v['id']) for e in exits for v in volumes if overlap3(e['protected_walking_volume'],v['collision_AABB'])]
assert not conflicts,conflicts
points=[p(*v) for pts,_,_ in faces for v in pts]+[p(x,y,z) for x in [0,14] for y in [0,14] for z in [-1.15,0]]
assert all(45<x<W-45 and 45<y<H-45 for x,y in points)
plan={'scope':'This image only. No masters or approval files changed. Visual curves permitted at ground and upper room exteriors; gameplay bounds approximated by common-axis boxes. No engine collision asset is made.','projection':{'type':'orthographic','image_size':[W,H],'scale':S,'formula':'u=800+(x-y)*45*sqrt(3)/2;v=382+(x+y)*45/2-z*45'},'base':{'square_xy':[0,0,14,14],'top_z':0,'bottom_z':-1.15,'front_cutaway_faces':['x=14','y=14'],'straight_uniform_depth':True},'visual_volumes':volumes,'functional_exits':exits,'protected_central_play_space':[4.9,7,0,12,11,3],'buildings':[{'id':'A','description':'Different-depth rooms: large rounded projecting upper capsule, narrower rear room, visibly empty terrace, rounded ground machine annex and vertical machinery spine. Machine target about 40 percent of visible architectural design, distributed over side room, spine, roof and connections; not a lower-floor band or exact volumetric measurement.','people_entry':'x-facing rear ground wall at y=4.35..5.2','max_height':6.25,'roof_occupancy_target':.55,'roof_note':'Supported low service machinery arranged on each available roof area, adjust final rooftop plan coverage to 40-80 percent without filling the open terrace.'},{'id':'B','description':'Wide ground shop with two unequal upper room modules, supported sloping main roof and taller flat-roof side module, empty upper deck and external straight stair.','people_entry':'y-facing ground shop wall x=8.45..10.05','max_height':5.95,'roof_occupancy_target':.5,'roof_note':'Roof plant is supported and connected, retain roof profile and open deck.'}],'props':props,'plan_validation':{'protected_exit_collision_AABB_conflicts':conflicts,'all_geometry_within_45px_safe_frame':True,'largest_z_m':6.25,'common_axis_collision_bounds':True,'disclaimer':'Plan-level analytic geometry only. Final generated-image geometry, exits and framing require separate visual QA.'},'guide_role':'Massing, common projection, clear exits and square base only; no words, labels, arrows or collision lines are drawn. Neutral colors and smooth code rendering are not final surface style.'}
(OUT/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
# Separate review-only top view; never an image-generation input.
cp=Image.new('RGB',(800,800),'#f3f2ec');cd=ImageDraw.Draw(cp)
def q(x,y):return (60+x*47,60+y*47)
cd.rectangle([q(0,0),q(14,14)],outline='#333333',width=3)
for e in exits:
    a=e['protected_walking_volume'];cd.rectangle([q(a[0],a[1]),q(a[3],a[4])],fill='#cfe7d0')
for v in volumes:
    a=v['collision_AABB'];cd.rectangle([q(a[0],a[1]),q(a[3],a[4])],outline='#687683',width=2)
cp.save(OUT/'collision_plan.png')
print(json.dumps(plan['plan_validation'],ensure_ascii=False))

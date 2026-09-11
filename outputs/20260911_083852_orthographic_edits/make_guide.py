from PIL import Image,ImageDraw
from pathlib import Path
import math
root=Path(r"C:/Users/Yeon Hee Kang/OneDrive/문서/Codex/background-concept-art/concetp-art/outputs/20260911_083852_orthographic_edits")
im=Image.new("RGB",(1536,1100),(240,243,245)); d=ImageDraw.Draw(im)
def p(x,y,z=0): return (768+24*(x-y),280+24/math.sqrt(3)*(x+y)-24*z)
def poly(pts,fill): d.polygon([p(*v) for v in pts],fill=fill,outline=(35,50,65),width=3)
poly([(0,20,0),(20,20,0),(20,20,-4),(0,20,-4)],(150,170,190))
poly([(20,0,0),(20,20,0),(20,20,-4),(20,0,-4)],(130,150,175))
poly([(0,0,0),(20,0,0),(20,20,0),(0,20,0)],(217,225,229))
for i in range(2,20,2):
 d.line([p(i,0),p(i,20)],fill=(180,194,204),width=1)
 d.line([p(0,i),p(20,i)],fill=(180,194,204),width=1)
vs=[(0,0),(15,0),(15,4),(4,4),(4,14),(0,14)]
for a,b in zip(vs,vs[1:]+vs[:1]):
 poly([(*a,0),(*b,0),(*b,5),(*a,5)],(170,183,185))
poly([(*v,5) for v in vs],(205,216,219))
poly([(0,15,0),(0,19,0),(0,19,2.5),(0,15,2.5)],(126,174,161))
poly([(16,0,0),(19,0,0),(19,0,2.5),(16,0,2.5)],(126,174,161))
d.text((55,1000),"PARALLEL AXES ONLY - all horizontal X/Y lines +/-30 degrees; verticals parallel; equal base depth.",fill=(40,50,60))
im.save(root/"orthographic_guide.png")


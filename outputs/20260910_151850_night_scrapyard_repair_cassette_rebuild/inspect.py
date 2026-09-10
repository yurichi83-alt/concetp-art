from pathlib import Path
from PIL import Image
r=Path(__file__).resolve().parent
im=Image.open(r/'night_scrapyard_repair_cassette.png')
for name,box in [('junkyard',(330,330,650,585)),('repair',(800,360,1230,705)),('left_base_corner',(15,590,110,750)),('right_base_corner',(1290,580,1377,750))]:
    im.crop(box).resize(((box[2]-box[0])*2,(box[3]-box[1])*2)).save(r/(name+'_inspection_2x.png'))
print(im.size)

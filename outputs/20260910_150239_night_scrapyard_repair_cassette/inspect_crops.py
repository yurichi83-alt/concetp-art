from pathlib import Path
from PIL import Image
run=Path(__file__).resolve().parent
im=Image.open(run/'night_scrapyard_repair_cassette.png')
print(im.size)
for name,box in [('junkyard',(320,300,700,610)),('repair',(760,350,1200,700))]:
    im.crop(box).resize(((box[2]-box[0])*2,(box[3]-box[1])*2)).save(run/(name+'_inspection_2x.png'))
print('Inspection-only crops; original unchanged. Crop origins recorded in script, scale2.')

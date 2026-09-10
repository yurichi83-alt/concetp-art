from pathlib import Path
import json,hashlib
from PIL import Image
R=Path(__file__).resolve().parent
for name in ['20260910_152550_desert_reference','20260910_153000_desert_reference_corrected','20260910_153400_desert_reference_final']:
    p=R.parent/name/'references.json';d=json.loads(p.read_text(encoding='utf-8'));d['delivery_status']='returned_image_saved'
    if not d.get('submitted_to_generation'):d['submitted_to_generation']=d.get('planned_inputs',[])
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
p=R/'desert_outpost.png'
with Image.open(p) as im: size=list(im.size); im.verify()
(R/'result.json').write_text(json.dumps({'image':str(p),'size_px':size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'needs_revision','final_count':1,'prompt':str(R/'generation_prompt.md'),'review':str(R/'review.json'),'backend':'builtinimagegen'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Image saved and checked; geometry not marked PASS.')

from pathlib import Path
from PIL import Image
import json, hashlib, shutil, sys
R=Path(__file__).resolve().parent
P=R.parent/'20260910_134620_scrapyard_cassette'
I=P/'scrapyard_cassette_initial.png'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
source=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a089a3-c81b-7403-8631-dfe51add7b3c/exec-1ae7303d-eebe-423a-ab33-9b2f3f8a5523.png')
assert sha(source)==sha(I)
write(P/'result.json',{'status':'needs_revision','tool':'built-in image_gen.imagegen','intent':'new_generation','source_path':str(source),'saved_path':str(I),'sha256':sha(I),'source_sha256':sha(source),'byte_exact_copy':True,'dimensions':Image.open(I).size,'review':'review.md','fault':'L02/L03: right rear service passage ended at undifferentiated solid wall','correction_run':str(R),'independence':'No counterpart scene, guide, prompt or art and no previous generated artwork read/opened/reused. Only masters, own new guide, and explicit user cassette reference were image inputs.'})
write(R/'references.json',{'intent':'local_structural_edit','actual_transmission':'Own candidate passed via referenced_image_paths to built-in imagegen','input_count':1,'inputs':[{'order':1,'path':str(I),'sha256':sha(I),'visually_inspected':True,'role':'own initial candidate; edit only rear right passage wall; all unrelated structure/style preserved'}],'master_roles':'Masters read for first generation and persist through target preservation; no additional master paths sent during local edit.','excluded':'No counterpart, unrelated prior generated artworks or review_only sources.'})
shutil.copyfile(P/'structure_plan.json',R/'structure_plan.json')
(R/'structure_plan_note.md').write_text('Same own planned geometry; repair the generated wall that blocked the intended right exit. No coordinate redesign. Structure guide remains in the original run and was not an input to local edit.\n',encoding='utf-8')
if len(sys.argv)>1:
 finalsource=Path(sys.argv[1]); target=R/'scrapyard_cassette_final.png'
 if target.exists(): assert sha(target)==sha(finalsource)
 else: shutil.copyfile(finalsource,target)
 assert sha(target)==sha(finalsource)
 write(R/'result.json',{'status':'pending_final_review','tool':'built-in image_gen.imagegen','intent':'local_structural_edit','source_path':str(finalsource),'saved_path':str(target),'sha256':sha(target),'source_sha256':sha(finalsource),'byte_exact_copy':True,'dimensions':Image.open(target).size,'original_run':str(P),'review':'review.md','correction':'rear right wall opened for continuous service exit','master_unchanged':True,'independence':'Only own initial candidate used in correction. No counterpart or prior unrelated generation used.'})
 print(json.dumps({'path':str(target),'sha256':sha(target),'dimensions':Image.open(target).size},ensure_ascii=False))
else: print('Initial result and correction inputs recorded.')

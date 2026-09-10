from pathlib import Path
from PIL import Image
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
items=[('salvage','outputs/20260910_151110_night_scrapyard_repair_salvage_corrected','night_scrapyard_repair_salvage.png','uncertain'),('cassette','outputs/20260910_151850_night_scrapyard_repair_cassette_rebuild','night_scrapyard_repair_cassette.png','needs_revision')]
files=[]
for style,folder,name,status in items:
    d=ROOT/folder;p=d/name
    with Image.open(p) as im:
        im.verify()
    with Image.open(p) as im: size=list(im.size)
    refs=json.loads((d/'references.json').read_text(encoding='utf-8'))
    submitted=refs['submitted_to_generation']
    assert submitted, f'Actual input list not yet recorded: {style}'
    paths=[str(x.get('path','')) if isinstance(x,dict) else str(x) for x in submitted]
    other='night_scrapyard_repair_cassette' if style=='salvage' else 'night_scrapyard_repair_salvage'
    assert all(other not in s for s in paths), 'Independent variants crossed as inputs'
    files.append({'style':style,'image':str(p),'size_px':size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'prompt_path':str(d/'generation_prompt.md'),'actual_input_count':len(submitted),'status':status,'cross_variant_output_input':False})
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256'] for r in manifest['references'])
report={'final_deliverable_count':2,'generation_backend':'builtin_image_gen','independent_generation':True,'references_29_hashes_preserved':True,'image_files_valid':True,'geometry_all_pass':False,'deliverables':files,'scope':'Saved files and submitted input independence; geometry judgments from actual reviews.'}
(RUN/'delivery.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'files_valid':True,'independent':True,'count':2,'reference_hashes_preserved':29,'geometry_all_pass':False},ensure_ascii=False))

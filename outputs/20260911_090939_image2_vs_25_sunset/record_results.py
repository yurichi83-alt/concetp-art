raise SystemExit("Superseded by MODEL_IDENTITY_CORRECTION.md; do not restore unverified Image 2 labels.")
import hashlib, json
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parents[2]
run = Path(__file__).resolve().parent
prompt = (run / 'generation_prompt.md').read_text(encoding='utf-8').strip()
dry = json.loads((run / 'api25/dry_run.json').read_text(encoding='utf-8-sig'))
refs = json.loads((run / 'references.json').read_text(encoding='utf-8'))
assert dry['prompt'] == prompt
assert [Path(p).resolve() for p in dry['image']] == [Path(p).resolve() for p in refs['planned_inputs_both']]
assert dry['model'] == 'gpt-image-2.5-sunburst'
assert dry['n'] == 1
img = run / 'builtin/builtin_first_output.png'
with Image.open(img) as image:
    dimensions = list(image.size)
    assert image.format == 'PNG'
refs['actual_inputs_builtin'] = refs['planned_inputs_both']
refs['builtin_delivery_status'] = 'completed'
refs['prompt_metadata'] = {
    'sha256_utf8_stripped': hashlib.sha256(prompt.encode('utf-8')).hexdigest(),
    'characters': len(prompt), 'utf8_bytes': len(prompt.encode('utf-8')),
    'words_whitespace': len(prompt.split()),
    'same_text_verified_against_api_dry_run': True,
    'tokens': None, 'returned_revised_prompt': None,
    'per_call_model_snapshot': None
}
refs['api_plan']['dry_run_validated'] = True
(run / 'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
result = {
    'status':'partially_completed_api_key_required',
    'builtin':{
        'status':'generated_and_reviewed','qa_status':'needs_revision',
        'path':'builtin/builtin_first_output.png','size':dimensions,
        'first_output_only':True,'calls':1,'corrections':0,
        'documented_product_model':'gpt-image-2',
        'per_call_model_snapshot':None,'internal_quality':None,
        'generated_source':'C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-63441e49-1811-456d-bd47-e3d8e79e1d09.png'
    },
    'api25':{'status':'blocked_missing_api_key','actual_call_made':False,
        'target_model':'gpt-image-2.5-sunburst','quality':'auto',
        'size':'1536x1024','n':1,'dry_run_validated':True},
    'comparison':{'status':'pending_second_image','identical_prompt_verified':True,
        'identical_reference_order_verified':True,'first_outputs_only':True,
        'confounds':['different access paths','unexposed builtin quality and internal processing','uncontrolled randomness','one sample per model']},
    'master_updated':False
}
(run / 'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest_path = root / 'outputs/final_manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
source = img.relative_to(root).as_posix()
if not any(e['source']==source for e in manifest['images']):
    manifest['images'].append({
        'filename':'20260911_090939__builtin_image2_first_output.png',
        'source':source,'qa_status':'needs_revision',
        'selection_reason':'User-requested model comparison; first uncorrected built-in output, API25 pending.',
        'evidence':[(run/'builtin/review.md').relative_to(root).as_posix(),(run/'result.json').relative_to(root).as_posix()]
    })
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Saved built-in output metadata; identical API dry-run prompt and 4 reference paths verified.')
print('Image dimensions:',dimensions)

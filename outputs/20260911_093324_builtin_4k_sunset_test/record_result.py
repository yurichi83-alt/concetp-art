import json, hashlib
from pathlib import Path
from PIL import Image
run=Path(__file__).resolve().parent
root=run.parents[1]
source=run/'builtin_resolution_test.png'
prompt=(run/'generation_prompt.md').read_text(encoding='utf-8').strip()
prior=(root/'outputs/20260911_090939_image2_vs_25_sunset/generation_prompt.md').read_text(encoding='utf-8').strip()
expected=prior.replace('landscape 3:2 composition.','landscape 16:9 composition. Render the image at native 4K UHD resolution, 3840 x 2160 pixels. Keep the entire diorama within this wide canvas.')
assert prompt==expected
with Image.open(source) as im:
    size=list(im.size)
    fmt=im.format
refs=json.loads((run/'references.json').read_text(encoding='utf-8'))
refs['actual_submission']['status']='completed'
refs['actual_resolution']=size
refs['resolution_request_met']=size==[3840,2160]
refs['prompt_sha256']=hashlib.sha256(prompt.encode('utf-8')).hexdigest()
refs['prompt_characters']=len(prompt)
refs['only_declared_prompt_change_verified']=True
(run/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
result={
    'status':'resolution_test_completed_requested_size_not_met',
    'qa_status':'needs_revision',
    'backend':'builtin_image_gen',
    'documented_product_rollout':'Images2.5 includes Codex',
    'returned_model_snapshot':None,
    'requested_resolution':[3840,2160],
    'actual_resolution':size,
    'native_4k_request_met':size==[3840,2160],
    'actual_format':fmt,
    'actual_bytes':source.stat().st_size,
    'resize_upscale_crop_applied':False,
    'calls':1,'api_calls':0,
    'actual_image_source':'C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-b69e1c9c-ad3a-4a9e-9328-251a69637459.png',
    'saved_path':'builtin_resolution_test.png',
    'review':'review.md',
    'scope':'Observed result of this one built-in request; not a verified universal resolution ceiling.',
    'master_updated':False
}
(run/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest_path=root/'outputs/final_manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8-sig'))
relative=source.relative_to(root).as_posix()
if not any(e['source']==relative for e in manifest['images']):
    manifest['images'].append({
        'filename':'20260911_093324__builtin_resolution_test_1672x941.png',
        'source':relative,
        'qa_status':'needs_revision',
        'selection_reason':'User-requested native4K test: actual returned PNG1672x941, no upscaling. First output retained as test evidence.',
        'evidence':[(run/'result.json').relative_to(root).as_posix(),(run/'review.md').relative_to(root).as_posix()]
    })
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Native output:',size,fmt)
print('4K request met:',size==[3840,2160])
print('Unchanged scene prompt and four master inputs recorded.')


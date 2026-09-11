import hashlib, json, shutil
from pathlib import Path
run = Path(__file__).resolve().parent
root = run.parents[1]
history = run / 'metadata_before_rollout_correction'
history.mkdir(exist_ok=True)
for name in ['README.md','brief.md','preflight.md','references.json','result.json','record_results.py','api25/setup_status.json']:
    source = run / name
    saved = history / name
    saved.parent.mkdir(parents=True,exist_ok=True)
    if not saved.exists():
        shutil.copy2(source,saved)
launch = 'https://openai.com/index/introducing-chatgpt-images-2-5/'
guide = 'https://learn.chatgpt.com/docs/image-generation'
correction = {
    'date':'2026-09-11',
    'official_release_date':'2026-09-08',
    'official_release':launch,
    'official_release_claim':'Images 2.5 available / rolling out to all ChatGPT, ChatGPT Work and Codex users across desktop, mobile and web.',
    'conflicting_usage_guide':guide,
    'usage_guide_text_at_check':'Built-in image generation uses gpt-image-2.',
    'conclusion':'Do not claim API is required for Images 2.5 in Codex, or that this built-in output is a confirmed Image 2 baseline.',
    'actual_builtin_call_model_snapshot':None,
    'builtin_model_selection_parameter_available':False,
    'requires_api_key_for_builtin':False,
    'api_calls_made':0
}
result = json.loads((run/'result.json').read_text(encoding='utf-8'))
result['status']='comparison_on_hold_premise_corrected'
result['builtin']['documented_product_model']=None
result['builtin']['product_rollout_announcement']='ChatGPT Images 2.5 includes Codex'
result['builtin']['per_call_model_snapshot']=None
result['builtin']['display_label']='Current built-in image output; exact runtime model unverified'
result['api25']['status']='on_hold_comparison_premise_corrected'
result['comparison']['status']='not_validated_as_2_vs_25'
result['comparison']['required_clarification']='Choose explicit API model comparison only after the corrected product/runtime distinction is understood; API is optional for built-in Images 2.5.'
result['model_identity_correction']=correction
(run/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
refs = json.loads((run/'references.json').read_text(encoding='utf-8'))
refs['builtin_contract']['documented_product_model']=None
refs['builtin_contract']['product_rollout_announcement']='ChatGPT Images 2.5 includes Codex'
refs['builtin_contract']['per_call_model_snapshot']=None
refs['api_plan']['status']='on_hold_comparison_premise_corrected'
refs['model_identity_correction']=correction
if launch not in refs['sources']:
    refs['sources'].append(launch)
(run/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
setup=json.loads((run/'api25/setup_status.json').read_text(encoding='utf-8'))
setup['dependency_installation']='interrupted_after_user_queried_need_for_API; installation completeness not verified'
setup['exec_session_id']=None
setup['api_key_setup_required_for_builtin']=False
setup['next_step']='No automatic API invocation. Original 2-vs-2.5 premise withdrawn. Optional explicit API comparison remains available if requested after correction.'
(run/'api25/setup_status.json').write_text(json.dumps(setup,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for name in ['brief.md','preflight.md']:
    p=run/name
    old=p.read_text(encoding='utf-8')
    prefix='> 2026-09-11 정정: 아래는 생성 당시 계획 이력이다. Codex는 Images 2.5 제공 대상으로 발표되었으며, 이 출력의 실제 모델 버전은 도구 응답으로 확인되지 않았다. 내장2/2.5사용API필수라는 전제는 철회. 현재 판정은 MODEL_IDENTITY_CORRECTION.md 및 result.json을 따른다.\n\n'
    if not old.startswith('> 2026-09-11 정정:'):
        p.write_text(prefix+old,encoding='utf-8')
p=run/'record_results.py'
old=p.read_text(encoding='utf-8')
guard='raise SystemExit("Superseded by MODEL_IDENTITY_CORRECTION.md; do not restore unverified Image 2 labels.")\n'
if not old.startswith(guard):
    p.write_text(guard+old,encoding='utf-8')
manifest_path=root/'outputs/final_manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8-sig'))
source=(run/'builtin/builtin_first_output.png').relative_to(root).as_posix()
entry=next(e for e in manifest['images'] if e['source']==source)
old_name=entry['filename']
new_name='20260911_090939__builtin_first_output.png'
old_path=(root/'outputs/final'/old_name).resolve()
new_path=(root/'outputs/final'/new_name).resolve()
final_dir=(root/'outputs/final').resolve()
assert old_path.parent==final_dir and new_path.parent==final_dir
expected=hashlib.sha256((root/source).read_bytes()).hexdigest()
if old_path!=new_path:
    assert hashlib.sha256(old_path.read_bytes()).hexdigest()==expected
    assert not new_path.exists()
    old_path.rename(new_path)
entry['filename']=new_name
entry['selection_reason']='First uncorrected built-in comparison output; exact runtime model unverified. Previous Image 2 label withdrawn.'
ev=(run/'MODEL_IDENTITY_CORRECTION.md').relative_to(root).as_posix()
if ev not in entry['evidence']:
    entry['evidence'].append(ev)
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Corrected model metadata and final filename; image and submitted prompt unchanged; API calls = 0.')


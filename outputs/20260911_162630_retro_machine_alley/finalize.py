from pathlib import Path
from datetime import datetime
import hashlib
import json
import sys

RUN = Path(__file__).resolve().parent
ROOT = RUN.parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from validate_project import image_dimensions

source = RUN / sys.argv[1]
qa_status = sys.argv[2]
assert qa_status in ('candidate_pass','needs_revision','uncertain','not_reviewed')
assert source.resolve().is_relative_to(RUN.resolve()) and source.is_file()
data = source.read_bytes()
fmt, (width,height) = image_dimensions(data)
sha = hashlib.sha256(data).hexdigest()
protected = json.loads((RUN/'protected_before.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==old for p,old in protected.items()), 'Master changed unexpectedly'
result = dict(scene='night_retro_machine_alley',requested_images=1,backend='builtin_image_gen',
    selected_source=source.relative_to(ROOT).as_posix(),qa_status=qa_status,format=fmt,width=width,height=height,
    sha256=sha,bytes=len(data),master_version='2.6',execution_rules_version='1.7',
    master_files_unchanged=True,user_attachment_registered_as_master=False,
    machine_ratio='One building designed for about40% visible mechanical integration; visual estimate, not exact pixel/3D measurement.',
    final_prompt=source.parent.joinpath('generation_prompt.md').relative_to(ROOT).as_posix(),
    review=source.parent.joinpath('review.md').relative_to(ROOT).as_posix(),
    completed_at=datetime.now().isoformat(),internal_model_version='not_exposed')
assert (ROOT/result['final_prompt']).is_file()
assert (ROOT/result['review']).is_file()
filename='20260911_162630__retro_machine_alley.png'
manifest_path=ROOT/'outputs/final_manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8-sig'))
assert not any(e['filename']==filename for e in manifest['images']), 'Already registered'
manifest['images'].append(dict(filename=filename,source=result['selected_source'],qa_status=qa_status,
    selection_reason='레트로기계 밤골목 요청1장 선택본; 구조보정중간본은제외',
    evidence=[result['review'],(RUN/'tool_limit_resolution.md').relative_to(ROOT).as_posix()],sha256=sha,bytes=len(data)))
manifest.setdefault('excluded',[])
manifest['updated_date']=datetime.now().strftime('%Y-%m-%d')
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
result['final_collection_path']='outputs/final/'+filename
(RUN/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'selected':result['selected_source'],'qa_status':qa_status,'size':[width,height]},ensure_ascii=True))

from pathlib import Path
from datetime import datetime
import hashlib
import json
import sys

RUN=Path(__file__).resolve().parent
ROOT=RUN.parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_project import image_dimensions
source=(RUN/sys.argv[1]).resolve()
status=sys.argv[2]
assert source.is_relative_to(RUN.resolve()) and source.is_file()
assert status in ('candidate_pass','uncertain','needs_revision','not_reviewed')
data=source.read_bytes()
fmt,(w,h)=image_dimensions(data)
before=json.loads((RUN/'master_hashes_before.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==v for p,v in before.items()),'Master changed'
review=source.parent/'review.md'
prompt=source.parent/'generation_prompt.md'
assert review.is_file() and prompt.is_file()
filename='20260911_165430__curved_stacked_alley.png'
sha=hashlib.sha256(data).hexdigest()
manifest_path=ROOT/'outputs/final_manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8-sig'))
assert not any(e['filename']==filename for e in manifest['images'])
manifest['images'].append(dict(filename=filename,source=source.relative_to(ROOT).as_posix(),qa_status=status,
 selection_reason='곡면지상/상층·적층실루엣의이번만예외테스트 최종1장; 원본/중간본별도보존',
 evidence=[review.relative_to(ROOT).as_posix(),(RUN/'brief.md').relative_to(ROOT).as_posix()],
 sha256=sha,bytes=len(data)))
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
result=dict(backend='builtin_image_gen',internal_model_version='not_exposed',requested_final_images=1,
 source=source.relative_to(ROOT).as_posix(),final_collection_path='outputs/final/'+filename,
 width=w,height=h,format=fmt,bytes=len(data),sha256=sha,qa_status=status,
 actual_prompt=prompt.relative_to(ROOT).as_posix(),review=review.relative_to(ROOT).as_posix(),
 scene_only_curved_architecture_exception=True,orthogonal_collision_plan_only=True,
 engine_collision_implemented=False,master_files_unchanged=True,
 protected_files_count=len(before),prior_generated_scene_inputs=False,completed_at=datetime.now().isoformat())
(RUN/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source':result['source'],'qa_status':status,'dimensions':[w,h],'masters_unchanged':True},ensure_ascii=True))

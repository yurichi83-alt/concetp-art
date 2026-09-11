from pathlib import Path
import json, hashlib, struct
ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
args=read(RUN/'submitted_request.json')
for name in ['generation_prompt.txt','generation_prompt.md']:
    (RUN/name).write_text(args['prompt'],encoding='utf-8')
refs=read(RUN/'references.json')
refs.update(delivery_status='completed',actual_submitted_image_count=len(args['referenced_image_paths']))
refs['submitted_to_generation']=[dict(item,path=path,status='submitted') for item,path in zip(refs['planned_submission'],args['referenced_image_paths'])]
refs['submitted_prompt'].update(character_count=len(args['prompt']),utf8_bytes=len(args['prompt'].encode('utf-8')),whitespace_words=len(args['prompt'].split()),saved_text_matches_actual_argument=True)
write(RUN/'references.json',refs)
pic=RUN/'roadside_clean_planes_test.png'
dims=list(struct.unpack('>II',pic.read_bytes()[16:24]))
write(RUN/'result.json',{'image':pic.name,'dimensions':dims,'sha256':sha(pic),'backend':'builtin_imagegen','model_version':None,'generated_source':'C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-96291f99-466e-43da-b373-462242ccb155.png','image_calls':1,'requested_final_count':1,'selected_final':True,'edit_scope_status':'partial_visual_match','observed_small_puddles':2,'remaining_style_observations':['fine angular marks remain along some road brush edges','some wall patches still read jointly as paint wear'],'status':'needs_revision','geometry_status':'inherited_prior_C04_L07_and_guardhouse_roof_uncertainty','master_update':False,'review':'review.md'})
before=read(RUN/'master_hashes_before.json')
changed=[p for p,h in before.items() if not (ROOT/p).is_file() or sha(ROOT/p)!=h]
write(RUN/'master_integrity_check.json',{'files_checked':len(before),'changed':changed,'unchanged':not changed})
if changed: raise RuntimeError('Master files changed: '+repr(changed))
manifest=read(ROOT/'outputs/final_manifest.json')
rel=RUN.relative_to(ROOT).as_posix()
name='20260911_152626__roadside_clean_planes_test.png'
assert not any(e['filename']==name for e in manifest['images'])
manifest['images'].append({'filename':name,'source':rel+'/'+pic.name,'qa_status':'needs_revision','edit_scope_status':'partial_visual_match','selection_reason':'장면 한정 단색 면/큰 붓터치 테스트 전달본. 미세 도로 자국 일부 및 기존 기하 검수 상태 승계. 마스터 미반영.','evidence':[rel+'/review.md',rel+'/result.json'],'dimensions':dims})
manifest['excluded'].append({'source':rel+'/brush_color_reference.jpg','reason':'사용자 붓터치/색면 보조 참조 사본; 생성 결과 아님'})
write(ROOT/'outputs/final_manifest.json',manifest)
print(json.dumps({'dimensions':dims,'master_files_unchanged':len(before),'selected_final':name,'actual_image_inputs':len(args['referenced_image_paths'])}))


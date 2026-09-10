from pathlib import Path
import json, hashlib, struct
ROOT=Path(__file__).resolve().parents[2]
FINAL=Path(__file__).resolve().parent
PRIOR=ROOT/'outputs/20260910_110250_hardware_appliance_v22_test'
def save(path,data): path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
sources=[
 (PRIOR,'hardware_appliance_v22_candidate.png',Path(r'C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-b2569ac4-7c7b-40b7-94cd-9f0297b15d09.png'),'needs_revision'),
 (FINAL,'hardware_appliance_v22_test.png',Path(r'C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-f3db2498-fd75-48a1-9ecd-6d4258716192.png'),'candidate_pass')]
for folder,name,source,status in sources:
 dst=folder/name
 assert sha(source)==sha(dst)
 with dst.open('rb') as f:
  header=f.read(24)
 assert header[:8]==b'\x89PNG\r\n\x1a\n'
 width,height=struct.unpack('>II',header[16:24])
 refs=json.loads((folder/'references.json').read_text(encoding='utf-8-sig'))
 for i,ref in enumerate(refs['inputs']):
  submitted=(folder==FINAL or i<5)
  ref['submitted']=submitted
  ref['visually_inspected']=True
  ref['input_status']='submitted_via_referenced_image_paths' if submitted else 'inspection_only_omitted_for_five_image_limit'
  ref['sha256']=sha(Path(ref['path']))
 refs['actual_submitted_count']=sum(x['submitted'] for x in refs['inputs'])
 save(folder/'references.json',refs)
 result={'status':status,'output_file':name,'source_file':str(source),'width':width,'height':height,'sha256':sha(dst),'source_copy_hash_match':True,'backend':'builtin_image_gen','actual_generated_image_count':1,'requested_final_image_count':1,'master_version':'2.2','execution_rules_version':'1.3','review':'review.md','user_approved':False,'master_promoted':False,'prompt_file':'prompt.txt','references_file':'references.json'}
 if folder==FINAL:
  result['previous_run']=str(PRIOR.relative_to(ROOT))
  result['structural_correction']='L06 hardware room entry; local rubble and wall stump removal'
  result['structural_checks']={k:'PASS' for k in ['C01','C02','C03','C04','L01','L02','L03','L04','L05','L06']}
 else:
  result['next_run']=str(FINAL.relative_to(ROOT))
 save(folder/'result.json',result)
 scope=folder/'scope.json'
 data=json.loads(scope.read_text(encoding='utf-8-sig')) if scope.exists() else {'master_version':'2.2','execution_rules_version':'1.3','mode':'builtin_imagegen','master_update':False,'requested_final_count':1,'previous_run':str(PRIOR.relative_to(ROOT))}
 data['status']=status
 save(scope,data)
# Preserve the early painter-order SVG as an explicitly superseded draft; submitted guide was the depth-buffer PNG.
old=PRIOR/'structure_plan.svg'
draft=PRIOR/'structure_plan_painter_draft_not_input.svg'
if old.exists() and not draft.exists():
 assert old.resolve().is_relative_to(PRIOR.resolve()) and draft.resolve().is_relative_to(PRIOR.resolve())
 old.rename(draft)
p=PRIOR/'preflight.md'
s=p.read_text(encoding='utf-8-sig').replace('실제 전달 입력 6개 역할 지정, referenced_image_paths 지원 확인.','검토 자료 6개 역할 지정. 최종 실제 전달은 아래 한도 확인 후 5개로 정정.')
p.write_text(s,encoding='utf-8')
plan=json.loads((PRIOR/'structure_plan.json').read_text(encoding='utf-8'))
plan['guide_rendering']='depth-buffered coordinate geometry; final submitted guide is structure_plan.png'
plan['superseded_not_input']='structure_plan_painter_draft_not_input.svg'
save(PRIOR/'structure_plan.json',plan)
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
verified=0
for ref in manifest['references']:
 assert sha(ROOT/ref['path'])==ref['sha256'],ref['id']
 verified+=1
save(FINAL/'artifact_validation.json',{'ok':True,'copied_results_hash_verified':2,'reference_hashes_verified':verified,'master_modified':False,'final_structure_review':'candidate_pass, visual not metric','generated_results':2,'final_deliverables':1})
(FINAL/'generation_prompts.md').write_text('# 생성 지시 기록\n\n내장 image_gen 사용. 최종1장, 구조 보정1회.\n\n1. [초기 생성 지시](../20260910_110250_hardware_appliance_v22_test/prompt.txt)\n2. [최종 국소 보정 지시](prompt.txt)\n3. [구조 검수](review.md)\n\n입력 이미지와 실제 제출 여부는 각 run의 references.json에 기록했다.\n',encoding='utf-8')
print(json.dumps({'final':str(FINAL/'hardware_appliance_v22_test.png'),'sha256':sha(FINAL/'hardware_appliance_v22_test.png'),'reference_hashes_verified':verified,'status':'candidate_pass'},ensure_ascii=False))


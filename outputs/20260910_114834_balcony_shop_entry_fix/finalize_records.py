from pathlib import Path
import json, hashlib,struct
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
SRC=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0')
items=[('20260910_114238_tiny_shop_balcony','tiny_shop_balcony_candidate.png','exec-8f15ad6f-2de9-4483-9737-bf71ffdf5d34.png','needs_revision'),('20260910_114834_balcony_shop_entry_fix','tiny_city_shop_balcony_day.png','exec-9b664a65-3447-4f1c-82e4-7126e82f088b.png','candidate_pass')]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for i,(slug,name,source,status) in enumerate(items):
 folder=ROOT/'outputs'/slug;dst=folder/name;src=SRC/source
 assert sha(dst)==sha(src)
 w,h=struct.unpack('>II',dst.read_bytes()[16:24])
 refs=json.loads((folder/'references.json').read_text(encoding='utf-8'))
 for ref in refs['inputs']:ref.update(submitted=True,visually_inspected=True,sha256=sha(Path(ref['path'])))
 save(folder/'references.json',refs)
 save(folder/'result.json',{'status':status,'file':name,'source':str(src),'sha256':sha(dst),'source_copy_hash_match':True,'width':w,'height':h,'backend':'builtin_image_gen','master_version':'2.2','execution_rules_version':'1.3','architectural_revision':'architecture_entrances_roofs_20260910','requested_final_count':1,'master_promoted':False,'user_approved':False,'review':'review.md','prompt':'prompt.txt','previous_run':items[0][0] if i else None,'next_run':items[1][0] if not i else None})
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
for r in manifest['references']:assert sha(ROOT/r['path'])==r['sha256']
save(RUN/'artifact_validation.json',{'ok':True,'source_copies_verified':2,'reference_hashes_verified':len(manifest['references']),'final_count':1})
(RUN/'generation_prompts.md').write_text('# 생성 지시\n\n내장 image_gen 사용, 최종1장.\n\n1. [초기 생성 지시](../20260910_114238_tiny_shop_balcony/prompt.txt)\n2. [상점 입구 보정 지시](prompt.txt)\n3. [최종 검수](review.md)\n',encoding='utf-8')
print(json.dumps({'status':'candidate_pass','file':str(RUN/'tiny_city_shop_balcony_day.png'),'hash_checks':'passed'},ensure_ascii=False))


from pathlib import Path
import json, hashlib, struct
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
srcroot=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0')
items=[
('20260910_111843_tiny_city_shop_v22','tiny_city_shop_candidate.png','exec-9e122f08-bf2d-4f3b-a363-b4457ad994d1.png','needs_revision'),
('20260910_112435_tiny_shop_cutaway_fix','tiny_shop_cutaway_candidate.png','exec-033b447b-826e-429c-a084-fcf77cb7b20c.png','needs_revision'),
('20260910_112747_tiny_shop_full_frame','tiny_city_shop_day.png','exec-1526c0c3-c4ac-47f7-aa0f-6f2045e423ee.png','candidate_pass')]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,o): p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for i,(slug,name,source,status) in enumerate(items):
 folder=ROOT/'outputs'/slug; dst=folder/name; src=srcroot/source
 assert sha(dst)==sha(src)
 width,height=struct.unpack('>II',dst.read_bytes()[16:24])
 refs=json.loads((folder/'references.json').read_text(encoding='utf-8'))
 for ref in refs['inputs']:
  ref.update(submitted=True,visually_inspected=True,sha256=sha(Path(ref['path'])))
 save(folder/'references.json',refs)
 save(folder/'result.json',{'status':status,'file':name,'source':str(src),'sha256':sha(dst),'source_hash_match':True,'width':width,'height':height,'backend':'builtin_image_gen','master_version':'2.2','execution_rules_version':'1.3','requested_final_count':1,'user_approved':False,'master_promoted':False,'prompt':'prompt.txt','review':'review.md','previous_run':items[i-1][0] if i else None,'next_run':items[i+1][0] if i<2 else None})
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
for ref in manifest['references']: assert sha(ROOT/ref['path'])==ref['sha256']
save(RUN/'artifact_validation.json',{'ok':True,'source_copies_verified':3,'reference_hashes_verified':len(manifest['references']),'final_count':1})
(RUN/'generation_prompts.md').write_text('# 생성 지시 기록\n\n내장 image_gen 사용, 최종1장.\n\n1. [신규 생성](../20260910_111843_tiny_city_shop_v22/prompt.txt)\n2. [단면 보정](../20260910_112435_tiny_shop_cutaway_fix/prompt.txt)\n3. [전체 프레이밍 보정](prompt.txt)\n\n[최종 검수](review.md)\n',encoding='utf-8')
print(json.dumps({'final':str(RUN/'tiny_city_shop_day.png'),'verified':True,'status':'candidate_pass'},ensure_ascii=False))


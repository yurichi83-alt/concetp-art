from pathlib import Path
import json,hashlib,struct
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
src=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-717b99b5-8061-4fe5-8303-1af14ccaac39.png')
dst=RUN/'all_machines_cassette_futurism.png'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)==sha(dst)
refs=json.loads((RUN/'references.json').read_text(encoding='utf-8'))
for r in refs['inputs']:
 assert sha(Path(r['path']))==r['sha256']
 r['submitted']=True
(RUN/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
for r in manifest['references']: assert sha(ROOT/r['path'])==r['sha256']
w,h=struct.unpack('>II',dst.read_bytes()[16:24])
result={'status':'candidate_pass','backend':'builtin_image_gen','file':dst.name,'source':str(src),'sha256':sha(dst),'source_copy_hash_match':True,'width':w,'height':h,'master_version':'2.2','execution_rules_version':'1.3','actual_generation_count':1,'requested_final_count':1,'master_promoted':False,'user_approved':False,'review':'review.md','prompt':'prompt.txt','reference_hashes_verified':len(manifest['references'])}
(RUN/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':result['status'],'saved':str(dst),'hash_checks':'passed'},ensure_ascii=False))


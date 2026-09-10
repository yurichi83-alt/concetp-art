from pathlib import Path
import hashlib,json,struct
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
source=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-41ce5b16-30dd-4100-9c59-13092e54a6a7.png')
dst=RUN/'tiny_shop_windows_posters_motorcycle.png'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(dst)==sha(source)
w,h=struct.unpack('>II',dst.read_bytes()[16:24])
refs=json.loads((RUN/'references.json').read_text(encoding='utf-8'))
for ref in refs['inputs']:
 assert sha(Path(ref['path']))==ref['sha256']
 ref['submitted']=True
(RUN/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
for ref in manifest['references']: assert sha(ROOT/ref['path'])==ref['sha256']
result={'status':'candidate_pass','backend':'builtin_image_gen','file':dst.name,'source':str(source),'source_copy_hash_match':True,'sha256':sha(dst),'width':w,'height':h,'master_version':'2.2','execution_rules_version':'1.3','requested_final_count':1,'actual_generation_count':1,'master_promoted':False,'user_approved':False,'review':'review.md','prompt':'prompt.txt','reference_hashes_verified':len(manifest['references'])}
(RUN/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':result['status'],'hash_match':True,'path':str(dst)},ensure_ascii=False))


from pathlib import Path
import json,shutil,hashlib,struct
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
src=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-fac8296f-ef58-4a75-8256-f529d87ed189.png')
dst=RUN/'independent_alley_baseline.png';shutil.copy2(src,dst)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)==sha(dst)
w,h=struct.unpack('>II',dst.read_bytes()[16:24])
refs=json.loads((RUN/'references.json').read_text(encoding='utf-8'))
for r in refs['inputs']:r.update(submitted=True,visually_inspected=True,sha256=sha(Path(r['path'])))
(RUN/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
m=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
for r in m['references']:assert sha(ROOT/r['path'])==r['sha256']
res={'status':'candidate_pass','backend':'builtin_image_gen','master_version':'2.3','execution_version':'1.4','source':str(src),'output':str(dst),'sha256':sha(dst),'source_copy_hash_match':True,'size':[w,h],'requested_final_count':1,'pair_total_requested':2,'generation_mode':'independent_new_scene','cassette_futurism':False,'paired_output_input':False,'user_approved':False,'master_promoted':False,'prompt':'prompt.txt','review':'review.md','reference_hashes_verified':len(m['references'])}
(RUN/'result.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(dst),'size':[w,h],'copy_verified':True},ensure_ascii=False))

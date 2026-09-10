from pathlib import Path
import json,hashlib,struct
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
src=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-b3ffe47c-c931-4659-a864-3e179eb5b161.png')
dst=RUN/'scrapyard_grocery_salvage.png'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)==sha(dst)
refs=json.loads((RUN/'references.json').read_text(encoding='utf-8-sig'))
for r in refs['inputs']:
 assert r['submitted'] and r['visually_inspected']
 r['sha256']=sha(Path(r['path']))
(RUN/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
m=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
for r in m['references']:assert sha(ROOT/r['path'])==r['sha256']
size=list(struct.unpack('>II',dst.read_bytes()[16:24]))
result={'status':'candidate_pass','backend':'builtin_image_gen','master_version':'2.3','execution_version':'1.4','source':str(src),'output':str(dst),'sha256':sha(dst),'source_copy_hash_match':True,'size':size,'requested_final_count':1,'pair_total_requested':2,'generation_mode':'independent_new_scene','cassette_futurism':False,'scrapyard_mechanized_fraction_target':.5,'final_fraction_validation':'visual approximation, not exact volume measurement','paired_output_input':False,'user_approved':False,'master_promoted':False,'prompt':'prompt.txt','review':'review.md','reference_hashes_verified':len(m['references'])}
(RUN/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'size':size,'source_copy_match':True,'master_image_hashes_verified':len(m['references'])}))


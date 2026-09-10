from pathlib import Path
import json,shutil,hashlib,struct
root=Path("C:/Users/Yeon Hee Kang/OneDrive/문서/Codex/background-concept-art/concetp-art");run=root/"outputs/20260910_123650_alley_diverse_cutaway_fix"
src=Path("C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-7d64f4b8-6de6-4cc1-b84f-7d1d0f556e64.png")
dst=run/'alley_diverse_cassette_final.png'
shutil.copy2(src,dst)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)==sha(dst)
w,h=struct.unpack('>II',dst.read_bytes()[16:24])
refs=json.loads((run/'references.json').read_text(encoding='utf-8'))
for r in refs['inputs']:r.update(submitted=True,visually_inspected=True,sha256=sha(Path(r['path'])))
(run/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((root/'refs/manifest.json').read_text(encoding='utf-8-sig'))
checked=[]
for r in manifest['references']:
 if r.get('sha256'):
  assert sha(root/r['path'])==r['sha256'],r['id']
  checked.append(r['id'])
result={'status':'candidate_pass','backend':'builtin_image_gen','master_version':'2.2','execution_version':'1.3','output':str(dst),'source':str(src),'sha256':sha(dst),'source_copy_hash_match':True,'size':[w,h],'final_count':1,'master_updated':False,'user_approved':False,'master_promoted':False,'original_run':'../20260910_123045_alley_diverse_cassette','initial_prompt':'../20260910_123045_alley_diverse_cassette/prompt.txt','correction_prompt':'prompt.txt','review':'review.md','structural_correction':'C02 soil/foundation/utility exposure restored; above-ground design preserved','reference_hashes_verified':len(checked),'mechanical_body_fraction':'approximate20% visual design target, not exact raster volume measurement'}
(run/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(dst),'size':[w,h],'copy_hash_match':True,'reference_hashes_verified':len(checked)},ensure_ascii=False))

from pathlib import Path
import json,hashlib,shutil,struct
root=Path("C:/Users/Yeon Hee Kang/OneDrive/문서/Codex/background-concept-art/concetp-art");run=root/"outputs/20260910_124620_alley_polygon_building_fix"
src=Path("C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-418a0c52-2f24-48d9-8e57-07f1f63e5a5a.png")
dst=run/'alley_reference_varied_buildings_final.png';shutil.copy2(src,dst)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)==sha(dst)
w,h=struct.unpack('>II',dst.read_bytes()[16:24])
refs=json.loads((run/'references.json').read_text(encoding='utf-8'))
for r in refs['inputs']:r.update(submitted=True,visually_inspected=True,sha256=sha(Path(r['path'])))
(run/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((root/'refs/manifest.json').read_text(encoding='utf-8-sig'));checked=[]
for r in manifest['references']:
 if r.get('sha256'):
  assert sha(root/r['path'])==r['sha256'],r['id']
  checked.append(r['id'])
result={'status':'candidate_pass','backend':'builtin_image_gen','master_version':'2.2','execution_version':'1.3','output':str(dst),'source':str(src),'sha256':sha(dst),'source_copy_hash_match':True,'size':[w,h],'final_count':1,'master_updated':False,'user_approved':False,'master_promoted':False,'original_run':'../20260910_124032_alley_reference_shapes','initial_prompt':'../20260910_124032_alley_reference_shapes/prompt.txt','final_edit_prompt':'prompt.txt','review':'review.md','reference_hashes_verified':len(checked)}
(run/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(dst),'size':[w,h],'reference_hashes_verified':len(checked),'copy_hash_match':True},ensure_ascii=False))

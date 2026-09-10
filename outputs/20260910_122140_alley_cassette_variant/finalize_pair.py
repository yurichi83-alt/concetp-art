from pathlib import Path
import json,shutil,hashlib,struct
root=Path("C:/Users/Yeon Hee Kang/OneDrive/문서/Codex/background-concept-art/concetp-art")
run=root/"outputs/20260910_122140_alley_cassette_variant"
base=root/"outputs/20260910_121332_alley_baseline"
src=Path("C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/exec-d47d680e-8097-4d1f-b35a-3346a1a350de.png")
dst=run/"alley_cassette_futurism.png"
shutil.copy2(src,dst)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)==sha(dst)
w,h=struct.unpack(">II",dst.read_bytes()[16:24])
refs=json.loads((run/"references.json").read_text(encoding="utf-8"))
for r in refs["inputs"]:r.update(submitted=True,sha256=sha(Path(r["path"])))
(run/"references.json").write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding="utf-8")
result={"status":"candidate_pass","backend":"builtin_image_gen","master_version":"2.2","execution_version":"1.3","source":str(src),"output":str(dst),"width":w,"height":h,"sha256":sha(dst),"source_copy_hash_match":True,"pair_role":"cassette_variant","cassette_futurism":True,"user_approved":False,"master_promoted":False,"prompt":"prompt.txt","review":"review.md","baseline":str(base/"alley_baseline.png"),"comparison_limit":"visual preservation, not pixel-identical masking"}
(run/"result.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
manifest=json.loads((root/"refs/manifest.json").read_text(encoding="utf-8-sig"))
checked=[]
for r in manifest["references"]:
 p=root/r["path"]
 if r.get("sha256"):
  assert sha(p)==r["sha256"],r["id"]
  checked.append(r["id"])
pair={"requested_final_count":2,"final_count":2,"master_updated":False,"reference_hashes_verified":len(checked),"outputs":[json.loads((base/"result.json").read_text(encoding="utf-8")),result]}
(run/"pair_result.json").write_text(json.dumps(pair,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"output":str(dst),"size":[w,h],"source_copy_hash_match":True,"reference_hashes_verified":len(checked)},ensure_ascii=False))

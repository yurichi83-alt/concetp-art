from pathlib import Path
import json, hashlib, re, importlib.util, subprocess
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
HISTORY=ROOT/"state/history/20260910_103725_master_v2_2"
load=lambda p:json.loads(p.read_text(encoding="utf-8"))
result=load(RUN/"update_result.json")
snapshot=load(HISTORY/"snapshot_manifest.json")
errors=[]
# Preserve original newline conventions; fix suite-version particles without changing content.
for f in result["changed_files"]:
    path=ROOT/f
    text=path.read_text(encoding="utf-8").replace("v2.2과","v2.2와").replace("v2.2은","v2.2는")
    newline="\r\n" if b"\r\n" in (HISTORY/f).read_bytes() else "\n"
    with path.open("w",encoding="utf-8",newline=newline) as handle: handle.write(text)
def check(condition,label):
    if not condition: errors.append(label)
for item in snapshot["files"]:
    check(hashlib.sha256((HISTORY/item["path"]).read_bytes()).hexdigest()==item["sha256"],"backup changed: "+item["path"])
for item in snapshot["reference_image_hashes"]:
    check(hashlib.sha256((ROOT/item["path"]).read_bytes()).hexdigest()==item["sha256"],"image changed: "+item["id"])
project,manifest,approval=[load(ROOT/p) for p in ["project.json","refs/manifest.json","state/approvals.json"]]
oldproject,oldmanifest,oldapproval=[load(HISTORY/p) for p in ["project.json","refs/manifest.json","state/approvals.json"]]
aid="master_update_20260910_v2_2"
check(project["master_version"]==manifest["master_version"]==approval["master_version_approved"]=="2.2","suite version mismatch")
check(project["execution_rules_version"]=="1.3" and project["package_version"]=="1.2.0","execution/package version mismatch")
check(approval["entries"][:-1]==oldapproval["entries"],"historical approval entries changed")
entry=approval["entries"][-1]
check(entry["id"]==project["master_update_approval_id"]==aid,"latest approval link mismatch")
check(entry["evidence"]=="보강안 내용은 적절해보여. 승인할게 메인 래퍼런스 갱신해줘","approval evidence changed")
qa=(ROOT/"docs/06_QA.md").read_text(encoding="utf-8")
template=(ROOT/"templates/review.md").read_text(encoding="utf-8")
ids=lambda text:re.findall(r"^\|\s*([CL]\d{2})\s*\|",text,re.M)
expected=["C01","C02","C03","C04","L01","L02","L03","L04","L05","L06"]
check(ids(qa)==ids(template)==project["structural_correction_policy"]["checks"]==entry["structural_checks"]==expected,"QA/template/automatic correction IDs disagree")
check("C01~C04" in (ROOT/"docs/05_GENERATION_RULES.md").read_text(encoding="utf-8") and "L01~L06" in (ROOT/"docs/05_GENERATION_RULES.md").read_text(encoding="utf-8"),"execution check range missing")
check(len(manifest["references"])==len(oldmanifest["references"])==29,"reference count changed")
for before,after in zip(oldmanifest["references"],manifest["references"]):
    allowed={"use_only","role_clarification_approval_id"} if before["id"] in {"M01-01","M02-01"} else set()
    check({k:v for k,v in before.items() if k not in allowed}=={k:v for k,v in after.items() if k not in allowed},"reference properties changed outside scope: "+before["id"])
    if before["id"] in {"M01-01","M02-01"}:
        for f in ["refs/REFERENCE_MAP.md","REFERENCE_INDEX.html"]:
            check(after["use_only"] in (ROOT/f).read_text(encoding="utf-8"),"reference view mismatch: "+f+" "+before["id"])
for f in ["docs/03_VISUAL_STYLE_V2.md","docs/04_WORLD_DESIGN_V2.md"]:
    before=(HISTORY/f).read_text(encoding="utf-8")
    after=(ROOT/f).read_text(encoding="utf-8")
    check(after==before.replace("마스터 01~04 v2.1과","마스터 01~04 v2.2와"),"art/world body modified: "+f)
check(project["art_direction"]==oldproject["art_direction"] and project["world_setting"]==oldproject["world_setting"],"art/world config changed")
check(project["scoped_result_examples"]==oldproject["scoped_result_examples"],"scoped example approvals changed")
proposal=(ROOT/entry["proposal_path"]).read_text(encoding="utf-8")
clauses=re.findall(r"^> (.+)$",proposal.split("## 3.")[1].split("## 4.")[0],re.M)
owners=["docs/01_COMPOSITION.md"]*3+["docs/02_LAYOUT.md"]*3+["docs/06_QA.md"]
check(len(clauses)==7,"proposal clause count")
for i,(clause,f) in enumerate(zip(clauses,owners),1):
    check(clause in (ROOT/f).read_text(encoding="utf-8"),f"approved clause {i} not incorporated")
for f in ["AGENTS.md","README_KO.md","START_HERE_KO.md","FIRST_MESSAGE.txt","docs/00_INDEX.md",".agents/skills/game-env-art/SKILL.md"]:
    check("마스터 01~04 v2.1" not in (ROOT/f).read_text(encoding="utf-8"),"stale active suite reference: "+f)
spec=importlib.util.spec_from_file_location("package_validator",ROOT/"scripts/validate_project.py")
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
package=module.validate(ROOT)
check(package["ok"],"package validator failed")
diff=subprocess.run(["git","-c","core.excludesFile=","diff","--check"],cwd=ROOT,text=True,capture_output=True)
check(diff.returncode==0,"git diff --check failed: "+diff.stdout+diff.stderr)
report={"ok":not errors,"master_version":"2.2","execution_rules_version":"1.3","package_version":"1.2.0",
"master_images_unchanged":24,"preferred_images_unchanged":2,"review_images_unchanged":3,
"backups_verified":len(snapshot["files"]),"qa_template_config_checks_matched":expected,
"approved_clauses_verified":len(clauses),"historical_approvals_preserved":True if approval["entries"][:-1]==oldapproval["entries"] else False,
"style_world_bodies_preserved":"errors list reports any exception",
"package_validation":package,"git_diff_check_passed":diff.returncode==0,"errors":errors,
"scope":"File integrity, approval scope and policy consistency only; no image generation or geometry-model test performed."}
(RUN/"validation.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
result["status"]="complete" if not errors else "validation_failed"
result["validation_path"]="outputs/"+RUN.name+"/validation.json"
result["approved_clauses_verified"]=len(clauses)
(RUN/"update_result.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(0 if not errors else 1)


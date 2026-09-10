from pathlib import Path
import json,hashlib,difflib,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
HIST=ROOT/'state/history/20260910_131529_master_v2_3'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
snapshot=json.loads((HIST/'snapshot_manifest.json').read_text(encoding='utf-8'))
changed=[];diffs=[]
for rel,h in snapshot['files'].items():
 old=HIST/rel;now=ROOT/rel
 assert sha(old)==h,('history mutated',rel)
 if sha(now)!=h:
  changed.append(rel)
  diffs.extend(difflib.unified_diff(old.read_text(encoding='utf-8-sig').splitlines(keepends=True),now.read_text(encoding='utf-8-sig').splitlines(keepends=True),fromfile='before/'+rel,tofile='after/'+rel))
for rel,h in snapshot['reference_image_hashes'].items():assert sha(ROOT/rel)==h,('reference changed',rel)
oldm=json.loads((HIST/'refs/manifest.json').read_text(encoding='utf-8-sig'));newm=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8-sig'))
assert len(oldm['references'])==len(newm['references'])==29
for old,new in zip(oldm['references'],newm['references']):
 for k in ['id','path','sha256','width','height','reference_role','positive_reference','source_kind']:
  assert old.get(k)==new.get(k),(old['id'],k)
olda=json.loads((HIST/'state/approvals.json').read_text(encoding='utf-8-sig'));newa=json.loads((ROOT/'state/approvals.json').read_text(encoding='utf-8-sig'))
assert newa['entries'][:-1]==olda['entries'],'Historical approvals changed'
assert newa['entries'][-1]['id']=='master_update_20260910_v2_3'
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8-sig'))
assert (p['master_version'],p['execution_rules_version'],p['package_version'])==('2.3','1.4','1.3.0')
assert p['master_version']==newm['master_version']==newa['master_version_approved']
checks=p['structural_correction_policy']['checks']
assert len(checks)==len(set(checks)) and checks[-1]=='L07'
oldp=json.loads((HIST/'project.json').read_text(encoding='utf-8-sig'))
for k in ['art_direction','world_setting','approved_ldi_supplement_ids','scoped_result_examples']:
 assert p[k]==oldp[k],('Unrelated policy changed',k)
report=subprocess.run([sys.executable,'-X','utf8','scripts/validate_project.py','--json'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
assert report.returncode==0,report.stdout+report.stderr
validation=json.loads(report.stdout)
diffcheck=subprocess.run(['git','-c','core.excludesFile=','-c','core.safecrlf=false','diff','--check'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
assert diffcheck.returncode==0,diffcheck.stdout+diffcheck.stderr
(RUN/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
(RUN/'changes.diff').write_text(''.join(diffs),encoding='utf-8')
result={'status':'complete','approval_id':'master_update_20260910_v2_3','master_version':'2.3','execution_rules_version':'1.4','package_version':'1.3.0','changed_files':changed,'changed_file_count':len(changed),'backup_file_count':len(snapshot['files']),'unchanged_reference_images':len(snapshot['reference_image_hashes']),'historical_approval_entries_preserved':len(olda['entries']),'art_world_policy_preserved':True,'file_validation_pass':True,'git_diff_check_pass':True,'new_image_generation':False,'git_commit_push':False,'history':str(HIST.relative_to(ROOT)),'diff':'changes.diff','validation':'validation.json','scope':'approved master update only; integrity and document/config consistency, not image/3D validation'}
(RUN/'update_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':'complete','changed_files':len(changed),'backup_files':len(snapshot['files']),'reference_images_unchanged':len(snapshot['reference_image_hashes']),'validation_pass':True},ensure_ascii=False))


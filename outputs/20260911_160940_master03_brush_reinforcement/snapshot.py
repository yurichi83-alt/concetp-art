from pathlib import Path
import json,hashlib,shutil,subprocess
ROOT=Path(__file__).resolve().parents[2]; RUN=Path(__file__).resolve().parent
HIST=ROOT/'state/history/20260911_160940_master03_brush_reinforcement';HIST.mkdir(parents=True,exist_ok=False)
paths=['AGENTS.md','project.json','README_KO.md','START_HERE_KO.md','FIRST_MESSAGE.txt','REFERENCE_INDEX.html','refs/manifest.json','refs/REFERENCE_MAP.md','state/approvals.json','state/CHANGELOG.md','scripts/validate_project.py','outputs/final_manifest.json']
for folder in ['docs','templates','.agents']:
 paths.extend(p.relative_to(ROOT).as_posix() for p in (ROOT/folder).rglob('*') if p.is_file())
hashes={}
for rel in paths:
 p=ROOT/rel;out=HIST/rel;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out);hashes[rel]=hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
refs={r['path']:hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest() for r in m['references']}
f=json.loads((ROOT/'outputs/final_manifest.json').read_text(encoding='utf-8'))
finals={r['source']:hashlib.sha256((ROOT/r['source']).read_bytes()).hexdigest() for r in f['images']}
data={'snapshot_path':'state/history/20260911_160940_master03_brush_reinforcement','files':hashes,'original_reference_hashes':refs,'final_original_hashes':finals,'prior_approval_entries':len(json.loads((ROOT/'state/approvals.json').read_text(encoding='utf-8'))['entries']),'default_generation_priority_ids':json.loads((ROOT/'project.json').read_text(encoding='utf-8'))['default_generation_priority_ids']}
(RUN/'before.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(RUN/'git_status_before.txt').write_text(subprocess.run(['git','status','--short'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace').stdout,encoding='utf-8')
print(json.dumps({'snapshot_files':len(hashes),'old_references':len(refs),'existing_finals':len(finals),'approval_entries':data['prior_approval_entries']}))


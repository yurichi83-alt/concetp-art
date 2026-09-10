from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
HISTORY=ROOT/'state/history/20260910_141650_master_v2_4'
assert not HISTORY.exists(),'snapshot already exists'
HISTORY.mkdir(parents=True)
files=[ROOT/p for p in ['AGENTS.md','FIRST_MESSAGE.txt','README_KO.md','START_HERE_KO.md','REFERENCE_INDEX.html','project.json','refs/manifest.json','refs/REFERENCE_MAP.md','state/approvals.json','state/CHANGELOG.md','.agents/skills/game-env-art/SKILL.md','.agents/skills/game-env-art/agents/openai.yaml','scripts/validate_project.py']]
files+=sorted((ROOT/'docs').glob('*.md'))+sorted(p for p in (ROOT/'templates').iterdir() if p.is_file())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
records=[]
for p in files:
 rel=p.relative_to(ROOT);target=HISTORY/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
 records.append({'path':rel.as_posix(),'sha256':sha(p)})
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
for r in manifest['references']:assert sha(ROOT/r['path'])==r['sha256']
snapshot={'approval_pending_record':'master_update_20260910_v2_4','before_master':'2.3','before_execution':'1.4','files':records,'reference_images':[{'id':r['id'],'path':r['path'],'sha256':r['sha256']} for r in manifest['references']]}
(HISTORY/'snapshot_manifest.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'snapshot_files':len(records),'reference_hashes_verified':len(manifest['references']),'history':str(HISTORY)},ensure_ascii=False))


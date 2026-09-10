from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent;HIST=ROOT/"state/history/20260910_131529_master_v2_3"
HIST.mkdir(exist_ok=False)
paths=[p for p in ROOT.glob('*') if p.is_file() and p.suffix.lower() in ['.md','.txt','.json','.html']]
for folder in ['docs','templates','.agents']:
 paths += [p for p in (ROOT/folder).rglob('*') if p.is_file()]
paths += [ROOT/'refs/manifest.json',ROOT/'refs/REFERENCE_MAP.md',ROOT/'state/approvals.json',ROOT/'state/CHANGELOG.md']
paths=sorted(set(paths))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest={}
for p in paths:
 rel=p.relative_to(ROOT);target=HIST/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
 assert sha(p)==sha(target)
 manifest[rel.as_posix()]=sha(p)
ref=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8-sig'))
images={r['path']:sha(ROOT/r['path']) for r in ref['references']}
for r in ref['references']:assert images[r['path']]==r['sha256']
(HIST/'snapshot_manifest.json').write_text(json.dumps({'files':manifest,'reference_image_hashes':images,'master_version_before':'2.2','execution_before':'1.3'},ensure_ascii=False,indent=2),encoding='utf-8')
(RUN/'before_snapshot.json').write_text(json.dumps({'history':str(HIST.relative_to(ROOT)),'file_count':len(manifest),'reference_count':len(images)},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'backup_files':len(manifest),'preserved_images':len(images)}))


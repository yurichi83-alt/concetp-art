from pathlib import Path
import json,hashlib,shutil
root=Path("C:/Users/Yeon Hee Kang/OneDrive/문서/Codex/background-concept-art/concetp-art");run=root/"outputs/20260910_130219_geometry_gameplay_reference_proposal"
paths=[root/'AGENTS.md',root/'project.json',root/'.agents/skills/game-env-art/SKILL.md']
for folder in ['docs','templates','refs','state']:
 paths.extend(p for p in (root/folder).rglob('*') if p.is_file())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before={str(p.relative_to(root)):sha(p) for p in paths}
src=Path('C:/Users/YEONHE~1/AppData/Local/Temp/codex-clipboard-a4c15e75-a6af-4997-bf0f-6663337e4c55.png')
dst=run/'user_geometry_issue.png';shutil.copy2(src,dst)
assert sha(src)==sha(dst)
after={str(p.relative_to(root)):sha(p) for p in paths}
assert before==after
result={'status':'proposal_pending_user_approval','mode':'analysis_only','master_version_unchanged':'2.2','execution_version_unchanged':'1.3','master_files_written':False,'image_generation_calls':0,'proposal':'proposal_ko.md','attachment':str(dst),'attachment_sha256':sha(dst),'protected_files_verified_unchanged':len(before),'reviewed_output':'outputs/20260910_124620_alley_polygon_building_fix/alley_reference_varied_buildings_final.png','reassessment':'needs_revision under clarified building boundary requirement; prior C04 PASS insufficiently substantiated; old QA file preserved','new_current_approval':False}
(run/'analysis_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(run/'protected_file_hashes.json').write_text(json.dumps(before,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'proposal':str(run/'proposal_ko.md'),'protected_files_unchanged':len(before),'attachment_copy_verified':True},ensure_ascii=False))

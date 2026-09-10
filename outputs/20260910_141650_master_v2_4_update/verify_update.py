from pathlib import Path
import difflib
import hashlib
import importlib.util
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
HISTORY = ROOT / 'state/history/20260910_141650_master_v2_4'
def read(p): return p.read_text(encoding='utf-8')
def data(p): return json.loads(read(p))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks = []
def check(name, passed, detail=None):
    checks.append({'check': name, 'passed': bool(passed), 'detail': detail})

snapshot = data(HISTORY / 'snapshot_manifest.json')
check('Snapshot28 exact files', len(snapshot['files']) == 28 and all(sha(HISTORY / f['path']) == f['sha256'] for f in snapshot['files']))
check('All29 reference PNG hashes retained', len(snapshot['reference_images']) == 29 and all(sha(ROOT / f['path']) == f['sha256'] for f in snapshot['reference_images']))
before_m, after_m = data(HISTORY / 'refs/manifest.json'), data(ROOT / 'refs/manifest.json')
check('Reference entries and roles unchanged', before_m['references'] == after_m['references'])
before_a, after_a = data(HISTORY / 'state/approvals.json'), data(ROOT / 'state/approvals.json')
check('Prior approval entries identical; exactly one appended', after_a['entries'][:-1] == before_a['entries'] and len(after_a['entries']) == len(before_a['entries']) + 1)
check('Approval evidence exact', after_a['entries'][-1]['evidence'] == '좋아 보강해줘')
check('Previous changelog retained', read(ROOT / 'state/CHANGELOG.md').startswith(read(HISTORY / 'state/CHANGELOG.md').rstrip()))
before_p, p = data(HISTORY / 'project.json'), data(ROOT / 'project.json')
check('Version agreement', p['master_version'] == after_m['master_version'] == after_a['master_version_approved'] == '2.4' and p['execution_rules_version'] == '1.5' and p['package_version'] == '1.4.0')
protected = ['default_scene_count', 'architectural_design_policy', 'functional_exit_policy', 'boundary_object_policy', 'world_setting', 'art_direction', 'scoped_result_examples', 'preferred_result_reference_ids', 'auto_regenerate_scope']
check('Protected scene/art/exit/building policies retained', all(before_p[k] == p[k] for k in protected))
check('Structural authorization retained', all(v == p['structural_correction_policy'][k] for k, v in before_p['structural_correction_policy'].items()))
check('Prior geometry rules retained apart from workflow refinement', all(v == p['geometry_policy'][k] for k, v in before_p['geometry_policy'].items() if k != 'workflow'))
style_expected = read(HISTORY / 'docs/03_VISUAL_STYLE_V2.md').replace('마스터 01~04 v2.3', '마스터 01~04 v2.4').replace('01·02 v2.3', '01·02 v2.4')
check('Master03 art body preserved', read(ROOT / 'docs/03_VISUAL_STYLE_V2.md').rstrip() == style_expected.rstrip())
world_expected = read(HISTORY / 'docs/04_WORLD_DESIGN_V2.md').replace('마스터 01~04 v2.3', '마스터 01~04 v2.4')
world_lines = world_expected.splitlines()
world_lines[0] = world_lines[0].replace('v2.3', 'v2.4')
world_expected = '\n'.join(world_lines).replace('마스터 세트 v2.3 적용.', '마스터 세트 v2.4에서도 유지한다.')
check('Master04 world/building body preserved', read(ROOT / 'docs/04_WORLD_DESIGN_V2.md').rstrip() == world_expected.rstrip())
recheck = data(ROOT / p['latest_reassessments'][0]['review_path'])
check('Latest diagnostic status connected', recheck['overall_status'] == p['latest_reassessments'][0]['status'] == 'needs_revision' and sha(Path(recheck['source'])) == recheck['source_sha256'])
check('New prompt template connected', (ROOT / p['generation_prompt_template']).is_file() and 'templates/generation_prompt.md' in read(ROOT / 'scripts/validate_project.py'))

spec = importlib.util.spec_from_file_location('project_validation', ROOT / 'scripts/validate_project.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
package = module.validate(ROOT)
check('Existing project validator', package['ok'], package)

# No package installation: validate this deliberately narrow, known YAML shape
# as text. This is not a replacement claim for the unavailable PyYAML parser.
skill = read(ROOT / '.agents/skills/game-env-art/SKILL.md')
match = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: >-\n((?:  [^\n]+\n)+)---\n', skill)
description = ' '.join(line.strip() for line in match[2].splitlines()) if match else ''
check('Skill frontmatter manual shape/name/description review', match is not None and match[1] == 'game-env-art' and len(description) <= 1024 and not any(c in description for c in '<>') and '[TODO:' not in skill)
ui = read(ROOT / '.agents/skills/game-env-art/agents/openai.yaml')
short = re.search(r'^  short_description: "([^"]+)"$', ui, re.M)
check('Skill UI quoted strings and trigger retained', short is not None and 25 <= len(short[1]) <= 64 and 'Use $game-env-art' in ui and 'allow_implicit_invocation: true' in ui)

git = subprocess.run(['git', '-c', 'core.excludesFile=', '-c', 'core.safecrlf=false', 'diff', '--check'], cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
check('git diff --check', git.returncode == 0, git.stdout + git.stderr)
changed, chunks = [], []
for item in snapshot['files']:
    rel = item['path']
    old, new = read(HISTORY / rel), read(ROOT / rel)
    if old != new:
        changed.append(rel)
        chunks.extend(difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True), fromfile='before/' + rel, tofile='after/' + rel))
new_rel = 'templates/generation_prompt.md'
if (ROOT / new_rel).is_file():
    chunks.extend(difflib.unified_diff([], read(ROOT / new_rel).splitlines(keepends=True), fromfile='/dev/null', tofile='after/' + new_rel))
(RUN / 'changes.diff').write_text(''.join(chunks), encoding='utf-8')
report = {
    'ok': all(c['passed'] for c in checks), 'scope': 'Document, metadata and file integrity only. No new image generated or geometry quality validated.',
    'checks': checks, 'changed_existing_files': changed, 'new_template': new_rel,
    'skill_quick_validate': {'status': 'not_run_successfully', 'reason': 'PyYAML unavailable in both existing Python runtimes; no installation attempted. Narrow manual frontmatter and UI checks recorded above.'}
}
(RUN / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'ok': report['ok'], 'checks': len(checks), 'failed': [c for c in checks if not c['passed']], 'changed_existing': len(changed), 'new_templates': 1, 'scope': report['scope']}, ensure_ascii=False, indent=2))
raise SystemExit(0 if report['ok'] else 1)

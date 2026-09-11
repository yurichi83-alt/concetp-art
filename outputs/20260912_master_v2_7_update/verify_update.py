"""Verify this approved update against its pre-update snapshot (no mutations to masters)."""
from copy import deepcopy
from html.parser import HTMLParser
import hashlib
import importlib.util
import json
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SNAP = ROOT/'state/history/20260912_master_v2_7_architecture_forms'

def read(path):
    return json.loads(path.read_text())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

spec=importlib.util.spec_from_file_location('validator',ROOT/'scripts/validate_project.py')
validator=importlib.util.module_from_spec(spec);spec.loader.exec_module(validator)
manifest=read(ROOT/'refs/manifest.json');project=read(ROOT/'project.json')
snapshot=read(SNAP/'snapshot_manifest.json')
old_manifest=read(SNAP/'refs/manifest.json');old_project=read(SNAP/'project.json')
old_approvals=read(SNAP/'state/approvals.json');approvals=read(ROOT/'state/approvals.json')
checks={}
checks['existing_36_reference_bytes_preserved']=all(digest(ROOT/p)==h for p,h in snapshot['existing_reference_bytes'].items())
checks['previous_approval_entries_preserved']=approvals['entries'][:-1]==old_approvals['entries']
checks['existing_output_and_qa_files_preserved']=all(digest(ROOT/p)==h for p,h in snapshot['preserve_outputs'].items())
checks['default_reference_priorities_preserved']=all(project[k]==old_project[k] for k in ['default_inspection_ids','default_generation_priority_ids'])
checks['core_master_27_ids_paths_preserved']=[(r['id'],r['path']) for r in manifest['references'] if r.get('reference_role','master')=='master' and r['positive_reference']]==[(r['id'],r['path']) for r in old_manifest['references'] if r.get('reference_role','master')=='master' and r['positive_reference']]
checks['only_prior_m03_16_17_role_metadata_changed']=all(
    r==next(n for n in manifest['references'] if n['id']==r['id'])
    for r in old_manifest['references'] if r['id'] not in ['M03-16','M03-17'])
checks['master03_surface_component_unchanged']=project['visual_style_component_version']==old_project['visual_style_component_version']=='2.2'
checks['existing_surface_policy_unchanged']=project['surface_style_policy']==old_project['surface_style_policy']
checks['existing_world_and_art_direction_unchanged']=all(project[k]==old_project[k] for k in ['art_direction','world_setting'])
checks['existing_height_policy_and_roof_range_unchanged']=all(project['architectural_design_policy']['rooftop'][k]==old_project['architectural_design_policy']['rooftop'][k] for k in ['coverage_min','coverage_max','scope'])

class Catalog(HTMLParser):
    def __init__(self):
        super().__init__();self.figures=[];self.images=[];self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='figure':self.figures.append(d.get('id'))
        if tag=='img':self.images.append(d.get('src'))
        if tag=='a':self.links.append(d.get('href'))
catalog=Catalog();catalog.feed((ROOT/'REFERENCE_INDEX.html').read_text())
checks['catalog_47_unique_figure_ids']=len(catalog.figures)==len(set(catalog.figures))==len(manifest['references'])==47 and set(catalog.figures)=={r['id'] for r in manifest['references']}
checks['catalog_all_reference_image_paths_match']=set(catalog.images)=={r['path'] for r in manifest['references']}
checks['catalog_local_links_exist']=all((ROOT/p.split('#')[0]).is_file() for p in catalog.links if p and not p.startswith(('http:','https:','#')))

# Exercise failures through the real validator without rewriting package files.
original_read_text=Path.read_text
def simulated(mutation):
    m=deepcopy(manifest);p=deepcopy(project);mutation(m,p)
    def mocked(path,*args,**kwargs):
        if path==ROOT/'refs/manifest.json':return json.dumps(m)
        if path==ROOT/'project.json':return json.dumps(p)
        return original_read_text(path,*args,**kwargs)
    with patch.object(Path,'read_text',mocked):
        return validator.validate(ROOT)

def alter_ref(m,rid,key,value):
    next(r for r in m['references'] if r['id']==rid)[key]=value
scenarios=[
 ('comparison_cannot_be_generation_input',lambda m,p:alter_ref(m,'F-08','generation_input_allowed',True),'generation input permission'),
 ('form_cannot_be_global_default',lambda m,p:p['default_generation_priority_ids'].append('F-01'),'cannot appear in default_generation_priority_ids'),
 ('geometry_approval_not_inferred',lambda m,p:alter_ref(m,'F-08','geometry_approved',True),'cannot approve geometry'),
 ('qa_history_not_overwritten',lambda m,p:alter_ref(m,'F-08','overall_qa_status_at_registration','user_approved'),'must remain needs_revision'),
 ('reference_missing_is_rejected',lambda m,p:alter_ref(m,'F-01','path','refs/architecture_form/missing.png'),'Invalid reference record'),
 ('reference_hash_mismatch_rejected',lambda m,p:alter_ref(m,'F-01','sha256','0'*64),'hash mismatch'),
 ('architecture_count_mismatch_rejected',lambda m,p:m.update(architecture_form_reference_count=8),'Architecture form reference count mismatch'),
 ('unknown_approval_rejected',lambda m,p:alter_ref(m,'F-01','approval_id','unapproved'),'Unknown approved architecture scope'),
]
failure_tests=[]
for name,mutation,expected in scenarios:
    result=simulated(mutation)
    passed=not result['ok'] and any(expected in e for e in result['errors'])
    failure_tests.append({'name':name,'passed':passed,'errors':result['errors']})
validation=validator.validate(ROOT)
checks['package_file_validation_pass']=validation['ok']
checks['scope_guard_negative_cases_pass']=all(t['passed'] for t in failure_tests)
changed=[rel for rel,h in snapshot['files'].items() if digest(ROOT/rel)!=h]
report={'ok':all(checks.values()),'checks':checks,'validation':validation,'negative_tests':failure_tests,
        'changed_active_files':changed,'preserved_reference_hash_count':len(snapshot['existing_reference_bytes']),
        'preserved_output_and_qa_hash_count':len(snapshot['preserve_outputs']),
        'scope':'File/metadata/preservation and scoped-reference guard checks only; no generated image, visual regrading, actual collider or Codex runtime test.'}
(OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(OUT/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':report['ok'],'checks':checks,'changed_active_file_count':len(changed),'negative_tests_passed':sum(t['passed'] for t in failure_tests)},ensure_ascii=False,indent=2))
raise SystemExit(0 if report['ok'] else 1)

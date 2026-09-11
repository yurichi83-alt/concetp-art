from pathlib import Path
import json, hashlib, shutil
ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name, data): (RUN/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
target = ROOT/'outputs/final/20260911_150332__roadside_night_puddles.png'
anchor = ROOT/'refs/master03/ldi_10_storefront_style_anchor.png'
external = Path('C:/Users/Yeon Hee Kang/OneDrive/사진/ref/516752053_10165409110267784_3247313175898683043_n.jpg')
copied = RUN/'brush_color_reference.jpg'
shutil.copy2(external,copied)
roles = ['edit target: latest night scene; preserve content/layout/lighting, replace surface finish',
'M03-10: broad calm color planes and restrained material/light expression only',
'user attachment: sparse large neighboring-tone brush patches and grouped lighting only']
inputs = [{'index':i+1,'path':str(p),'role':role,'sha256':digest(p)} for i,(p,role) in enumerate(zip([target,anchor,copied],roles))]
prompt=(RUN/'generation_prompt.txt').read_text(encoding='utf-8')
(RUN/'generation_prompt.md').write_text(prompt,encoding='utf-8')
write('references.json',{'run_id':RUN.name,'master_version':'2.5','execution_rules_version':'1.6','catalog_revision':'2026-09-11-user-additions-02','delivery_status':'prepared','delivery_mechanism':'referenced_image_paths','actual_submitted_image_count':0,'inspected_for_planning':inputs,'planned_submission':inputs,'external_reference_source':str(external),'submitted_prompt':{'path':'generation_prompt.txt','character_count':len(prompt),'utf8_bytes':len(prompt.encode('utf-8')),'whitespace_words':len(prompt.split()),'saved_text_matches_actual_argument':True},'scope':'one scene-only clean color planes plus sparse broad tone brushwork test; no master update','omissions':'M01/M02/structure guide/M04 images omitted in this surface-only edit; target carries existing design and layout, retained requirements are stated in text. M03-10 explicitly included with supplementary brush reference.','tool_contract':{'tool':'builtin image_gen.imagegen','internal_model_version':None,'reference_weights':None,'referenced_image_paths_hard_limit':None}})
control=[ROOT/'AGENTS.md',ROOT/'project.json',ROOT/'state/approvals.json',ROOT/'state/CHANGELOG.md']
for folder in ['docs','refs','templates','.agents']:
    control += [p for p in (ROOT/folder).rglob('*') if p.is_file()]
write('master_hashes_before.json',{p.relative_to(ROOT).as_posix():digest(p) for p in control})
shutil.copy2(ROOT/'outputs/final_manifest.json',RUN/'final_manifest_before.json')
write('structure_plan.json',{'mode':'preserve_existing_scene_for_material_test','parent':'outputs/20260911_150332_roadside_night_puddles','geometry_reference':'outputs/20260911_142553_roadside_shops_dawn/structure_plan.json','projection_required':'single_orthographic_parallel','left_exit':'existing passage beside guardhouse; keep booth/bicycle out of approach','right_exit':'existing passage behind pickup; keep approach clear','building_entries':'retain doors/shutters as visual building entries, map exits separate','roofs':'retain all existing equipment/supports; inherited guardhouse coverage uncertainty','existing_geometry_status':'needs_revision: inherited C04/L07; prior repeated correction stopped without progress. This style test does not claim repair or promote source to geometry master.'})
print(json.dumps({'run':str(RUN),'paths':[x['path'] for x in inputs],'prompt_characters':len(prompt),'master_hash_count':len(control)},ensure_ascii=False))


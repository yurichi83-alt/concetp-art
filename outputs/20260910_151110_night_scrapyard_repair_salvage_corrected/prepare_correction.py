from pathlib import Path
import shutil,json
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
PREV=ROOT/'outputs/20260910_150225_night_scrapyard_repair_salvage'
for name in ['structure_guide.png','structure_plan.json']:
    shutil.copy2(PREV/name,RUN/name)
p=(RUN/'generation_prompt.md').read_text(encoding='utf-8').rstrip()
r=json.loads((PREV/'references.json').read_text(encoding='utf-8'))
r.update(run_id=RUN.name,own_correction_parent_run=PREV.name,delivery_status='submitted_call_initiated')
inputs=[{'id':'structure_guide','path':str(RUN/'structure_guide.png'),'role':'ONLY geometry/camera/layout source'}]+[i for i in r['planned_inputs'] if i['id'] in ['M03-10','M04-02']]
r['planned_inputs']=inputs;r['submitted_to_generation']=inputs;r['actual_submitted_image_count']=len(inputs)
r['omitted_references_and_reasons'] += ['M01/M02 inspected but omitted in corrective call to reduce camera interference; their topology/cutaway constraints retained in own guide and prompt. Faulty generated baseline excluded.']
r['submitted_prompt'].update(character_count=len(p),utf8_byte_count=len(p.encode('utf-8')),whitespace_word_count=len(p.split()),saved_text_matches_actual_argument=True)
(RUN/'references.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
b=(PREV/'brief.md').read_text(encoding='utf-8')
b=b.replace('Mode: independent new scene;', 'Mode: own structural correction of the same independent scene;')
b=b.replace('Only four master images and own guide.', 'Corrective actual inputs: two art/world masters and own guide; M01/M02 inspected but omitted as images, constraints retained.')
b += '\n\nCorrection evidence: previous review.json C02/C04FAIL. Revised input roles refer to actual three images; old image NOT input. Geometry plan retained as correct source, actual failed shape not preserved. Prompt strengthened for equal basevectors, same roof/ground axis and open right alley. Final QA pending.\n'
(RUN/'brief.md').write_text(b,encoding='utf-8')
(RUN/'preflight.md').write_text('# Structural correction preflight\n\nPLANNED: same orthogonal structure_plan and inspected guide, camera axes and constant depth; all scene keywords retained. Three actual input PNGs, no other independent scene or own faulty output. Fullprompt saved; no variables. Source M01/M02 omitted intentionally to reduce perspective conflicts; guide/text preserve their rules. Corrective clauses checked for both cuts, two exits, open routes, humanentries, perbuildingroof occupancy and coolnight scrapyard/autorepair/halfmechanized/chimney/bins/wrecks.\n\nGeometry evidence actual review pending; do not pass by plan.\n',encoding='utf-8')
print('Own-scene structural correction prepared with3 role-separated inputs.')

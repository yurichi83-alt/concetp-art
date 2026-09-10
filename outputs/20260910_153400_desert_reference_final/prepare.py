from pathlib import Path
import shutil,json
R=Path(__file__).resolve().parent;P=R.parent/'20260910_153000_desert_reference_corrected'
for f in ['structure_guide.png','structure_plan.json']:shutil.copy2(P/f,R/f)
p=(R/'generation_prompt.md').read_text(encoding='utf-8').rstrip()
(R/'references.json').write_text(json.dumps({'submitted_to_generation':[str(R/'structure_guide.png')],'delivery_status':'call_initiated','only_input_role':'geometry/camera','user_reference':'inspected/passedprevious2attempts; now subject/material/palette describedintext to avoidcamera influence','master':'2.4','execution':'1.5','parent':str(P),'prompt_chars':len(p),'utf8_bytes':len(p.encode('utf-8')),'backend':'builtinimagegen','internal_model_tokens_rewrite':'unknown'},ensure_ascii=False,indent=2),encoding='utf-8')
(R/'brief.md').write_text('# Single geometry-reference corrective pass\n\nSameuserdesertscene; finalcount1. Soleimageinput=ownsceneorthographicguide, previoussourcephotoremovedtoavoidcameracompetition. Sourcehangar/canvas/utilityvehicle/serviceplatform/daylightdesertvocabularyretainedintext. Allmasterspace/world/artconditionsunchanged. Seeparentbrief/planforcoverage; threepromptsectionsmapgeometry→C/L, scene→R/W04/W05, art→S/W.\n',encoding='utf-8')
(R/'preflight.md').write_text('# PLANNED\nOneinspectedPNGinput; guidedcornerpositions/axes/constantdepthretained. Currentkeywordsexpressed, no pendingvariables. Savedexactprompt. FinalimageQA pending, no PASS fromplan.\n',encoding='utf-8')

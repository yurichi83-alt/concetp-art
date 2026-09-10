from pathlib import Path
import json,shutil
R=Path(__file__).resolve().parent;P=R.parent/'20260910_152550_desert_reference'
for f in ['structure_guide.png','structure_plan.json','user_reference.png']:shutil.copy2(P/f,R/f)
s=(R/'generation_prompt.md').read_text(encoding='utf-8').rstrip()
d={'master':'2.4','execution':'1.5','own_parent':str(P),'submitted_to_generation':[str(R/'structure_guide.png'),str(R/'user_reference.png')],'delivery_status':'call_initiated','roles':['geometrytarget','desertsubjectonly'],'inspected':True,'source_art_world_masters':'inspected earlier; text preserved, omitted images for geometry correction','prompt_chars':len(s),'utf8_bytes':len(s.encode('utf-8')),'unknown':'model/token/rewrite','backend':'builtinimagegen'}
(R/'references.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
(R/'brief.md').write_text('# Own structural correction\n\nSame desertscene final1image. New strategy: guidegeometrycompletion, sourcevocabularyonly; no faultyoutput input. Unchangedmastergeometry/art/world/entry/roof/route requirements map tothreepromptsections. Allsubjectkeywords retained. No priornight/cassettepaircarryover. Seeparentbrief andcurrent exactprompt.\n',encoding='utf-8')
(R/'preflight.md').write_text('# PLANNED\n\nTwoactualinspectedPNGinputs, exactpromptstored, no unresolvedvariables. Parentplanroutes andorthogonalfootprints retained. Curvedhangarroofnotgroundcurve. Closedgateapproaches clear. ActualfinalQA pending.\n',encoding='utf-8')
print('Correction prepared')

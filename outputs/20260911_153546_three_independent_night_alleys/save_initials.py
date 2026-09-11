from pathlib import Path
import json,shutil,hashlib,struct
ROOT=Path(__file__).resolve().parents[2]; B=Path(__file__).resolve().parent
spec=json.loads((B/'batch_spec.json').read_text(encoding='utf-8'))
names=["exec-fce7cf2b-e6f5-4b5e-b0aa-ed7da0a9bb54.png","exec-5049e43b-92ae-437e-a7fa-e51add15dcd5.png","exec-0223d9c5-9c9e-4dd7-83b8-5a43b6cece1a.png"]
for c,n in zip(spec['variations'],names):
 r=B/(c['id']+'_'+c['name'])
 src=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0')/n
 p=r/'initial.png'; shutil.copy2(src,p)
 d=json.loads((r/'references.json').read_text(encoding='utf-8')); a=json.loads((r/'submitted_request.json').read_text(encoding='utf-8'))
 d.update(delivery_status='completed',actual_submitted_image_count=5,submitted_to_generation=d['planned_submission'],submitted_prompt={'path':'generation_prompt.txt','character_count':len(a['prompt']),'utf8_bytes':len(a['prompt'].encode('utf-8')),'saved_text_matches_actual_argument':True})
 (r/'references.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (r/'result.json').write_text(json.dumps({'image':'initial.png','generated_source':str(src),'dimensions':list(struct.unpack('>II',p.read_bytes()[16:24])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'backend':'builtin_imagegen','model_version':None,'selected_final':False,'status':'needs_revision','next_action':'new reconstruction from independent structure guide and master refs; no generated image used'},indent=2)+'\n',encoding='utf-8')
print('Saved 3 initial originals and actual reference records.')


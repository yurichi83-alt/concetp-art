from pathlib import Path
import json,shutil,hashlib,struct
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2];B=Path(__file__).resolve().parent
spec=json.loads((B/'batch_spec.json').read_text(encoding='utf-8'))
names=["exec-236d7183-d26a-4302-a916-78e80cd5ed12.png","exec-2f1a71c6-9aaa-4b96-ad46-f198958b899f.png","exec-47a51666-e6df-4fc1-ace0-55b19a3fc6e3.png"]
for c,n in zip(spec['variations'],names):
 run=B/(c['id']+'_'+c['name']); r=run/'reconstruction01'
 src=Path('C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0')/n
 shutil.copy2(src,r/'reconstructed.png')
 a=json.loads((r/'submitted_request.json').read_text(encoding='utf-8'))
 (r/'generation_prompt.txt').write_text(a['prompt'],encoding='utf-8')
 (r/'generation_prompt.md').write_text(a['prompt'],encoding='utf-8')
 records=[{'index':i+1,'path':p,'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest(),'role':role,'status':'submitted'} for i,(p,role) in enumerate(zip(a['referenced_image_paths'],['new independent orthographic structure guide','M02','M03-10','M04-02','brush/light reference']))]
 (r/'references.json').write_text(json.dumps({'actual_submitted_image_count':5,'submitted_to_generation':records,'delivery_status':'completed','mechanism':'referenced_image_paths','parent_run':str(run.relative_to(ROOT)),'previous_generated_images_used':False,'other_variations_used':False,'source_model':None,'prompt_characters':len(a['prompt'])},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (r/'result.json').write_text(json.dumps({'image':'reconstructed.png','dimensions':list(struct.unpack('>II',(r/'reconstructed.png').read_bytes()[16:24])),'status':'needs_revision','selected_final':c['id']=='03','backend':'builtin_imagegen','model_version':None,'source':str(src)},indent=2)+'\n',encoding='utf-8')
 if c['id']=='03': continue
 out=run/'reconstruction02';out.mkdir(exist_ok=True)
 im=Image.new('RGB',(1920,1440),'#dfe4ea');d=ImageDraw.Draw(im)
 def pr(x,y,z):return(round(960+32*(x-y)),round(470+16*(x+y)-44*z))
 def fp(box,z):
  x,y,u,v=box
  return [pr(x,y,z),pr(u,y,z),pr(u,v,z),pr(x,v,z)]
 t=fp([0,0,18,18],0);b=fp([0,0,18,18],-1.1)
 d.polygon([t[1],t[2],b[2],b[1]],fill='#91a1b5',outline='#34495f',width=3)
 d.polygon([t[2],t[3],b[3],b[2]],fill='#7d91a7',outline='#34495f',width=3)
 d.polygon(t,fill='#c4ced8',outline='#34495f',width=3)
 for e in c['exits']:d.polygon(fp(e['box'],.01),fill='#8bc1a8')
 for obj in sorted(c['buildings'],key=lambda o:o['box'][0]+o['box'][1]):
  top=fp(obj['box'],obj['h']);bt=fp(obj['box'],0)
  d.polygon([bt[1],bt[2],top[2],top[1]],fill='#a4a6b3',outline='#34495f',width=3)
  d.polygon([bt[2],bt[3],top[3],top[2]],fill='#c2bac0',outline='#34495f',width=3)
  d.polygon(top,fill='#d7d1d8',outline='#34495f',width=3)
  d.text(top[2],obj['id'],fill='#263444')
 d.polygon(fp(c['stairs'],.02),fill='#dbbb76',outline='#a38247',width=3)
 d.polygon(fp(c['dumpster'],.02),fill='#788776')
 im.save(out/'wide_margin_guide.png')
print('Saved 3 reconstruction originals; drew 2 new 4:3 guides with wide margins.')


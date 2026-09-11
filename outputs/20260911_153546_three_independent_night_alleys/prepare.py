from pathlib import Path
import json, hashlib, shutil
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[2]
BATCH=Path(__file__).resolve().parent
cfg=json.loads((BATCH/'batch_spec.json').read_text(encoding='utf-8'))
def write(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
original_refs=[Path(x) for x in cfg['master_reference_paths']]
shutil.copy2(original_refs[-1],BATCH/'brush_light_reference.jpg')
submitted_refs=original_refs[:-1]+[BATCH/'brush_light_reference.jpg']
controls=[ROOT/'AGENTS.md',ROOT/'project.json',ROOT/'state/approvals.json',ROOT/'state/CHANGELOG.md']
for folder in ['docs','refs','templates','.agents']:
 controls += [p for p in (ROOT/folder).rglob('*') if p.is_file()]
write(BATCH/'master_hashes_before.json',{p.relative_to(ROOT).as_posix():sha(p) for p in controls})
shutil.copy2(ROOT/'outputs/final_manifest.json',BATCH/'final_manifest_before.json')
def project(x,y,z): return (round(800+38*(x-y)),round(470+19*(x+y)-50*z))
def footprint(box,z=0):
 x1,y1,x2,y2=box
 return [project(x1,y1,z),project(x2,y1,z),project(x2,y2,z),project(x1,y2,z)]
for c in cfg['variations']:
 run=BATCH/(c['id']+'_'+c['name']); run.mkdir(exist_ok=True)
 (run/'generation_prompt.txt').write_text(c['prompt'],encoding='utf-8')
 (run/'generation_prompt.md').write_text(c['prompt'],encoding='utf-8')
 image=Image.new('RGB',(1600,1300),'#e5e8ed'); draw=ImageDraw.Draw(image)
 corners=[(0,0),(18,0),(18,18),(0,18)]
 top=[project(*xy,0) for xy in corners]; bottom=[project(*xy,-1.1) for xy in corners]
 draw.polygon([top[1],top[2],bottom[2],bottom[1]],fill='#8799ae',outline='#263445',width=3)
 draw.polygon([top[2],top[3],bottom[3],bottom[2]],fill='#72869c',outline='#263445',width=3)
 draw.polygon(top,fill='#c1cbd5',outline='#263445',width=3)
 for i in range(3,18,3):
  draw.line([project(i,0,0),project(i,18,0)],fill='#aeb9c5',width=1)
  draw.line([project(0,i,0),project(18,i,0)],fill='#aeb9c5',width=1)
 for e in c['exits']:
  draw.polygon(footprint(e['box'],0.02),fill='#80c3a5',outline='#237454',width=3)
 for b in sorted(c['buildings'],key=lambda b:b['box'][0]+b['box'][1]):
  box=b['box']; h=b['h']; bt=footprint(box,h); bb=footprint(box,0)
  col={'A':('#bd8163','#d29c7c','#e4b69b'),'B':('#6c87b2','#819bc2','#a5bade'),'C':('#8b8998','#aaa7b4','#c6c2cf')}[b['id']]
  draw.polygon([bb[1],bb[2],bt[2],bt[1]],fill=col[0],outline='#243142',width=3)
  draw.polygon([bb[2],bb[3],bt[3],bt[2]],fill=col[1],outline='#243142',width=3)
  draw.polygon(bt,fill=col[2],outline='#243142',width=3)
  if b['id']=='A':
   mid=footprint(box,h/2)
   draw.line([mid[1],mid[2],mid[3]],fill='#263445',width=4)
  draw.text(bt[2],b['id'],fill='#15253a')
 draw.polygon(footprint(c['stairs'],0.03),fill='#eec56c',outline='#a67820',width=3)
 draw.polygon(footprint(c['dumpster'],0.05),fill='#687d67',outline='#243b28',width=3)
 p=c['pole']; draw.line([project(*p,0),project(*p,4.6)],fill='#434344',width=6)
 draw.text((40,35),'PLANNING GUIDE ONLY | ORTHOGRAPHIC | NOT AN ART REFERENCE',fill='#243445')
 image.save(run/'structure_guide.png')
 # Simple independent plan checks; not final-image verification.
 blocks=c['buildings']
 for b in blocks:
  x1,y1,x2,y2=b['box']
  assert 0<=x1<x2<=18 and 0<=y1<y2<=18
 for i,a in enumerate(blocks):
  for b in blocks[i+1:]:
   x1,y1,x2,y2=a['box']; u1,v1,u2,v2=b['box']
   assert min(x2,u2)<=max(x1,u1) or min(y2,v2)<=max(y1,v1)
 assert len(blocks)==3 and len(c['exits'])==2
 write(run/'structure_plan.json',{'scene_id':c['id'],'projection':'single_orthographic_parallel','coordinate_frame':{'x':'rear corner toward screen lower-right','y':'rear corner toward screen lower-left','z':'vertical','base':[18,18,1.1]},'buildings':c['buildings'],'external_stair_footprint':c['stairs'],'dumpster':c['dumpster'],'utility_pole':c['pole'],'exits':c['exits'],'exits_plan_note':'variation02 right exit intentionally traverses ground floor of A, protected void reserved between supports; other exit corridors avoid all building footprints.','roof_coverage_planned':'about half of each building roof, visually inspect actual outcome','measurements':'planning only, not verified 3D dimensions/collision','guide':'structure_guide.png','guide_submitted':False})
 roles=['M01-01 structure/framing only','M02-01 exits/boundaries only','M03-10 calm base planes and selective material detail','M04-02 functional salvaged mechanical design only','user attachment: broad sparse neighboring-tone brush patches/light grouping only']
 records=[{'index':i+1,'path':str(p),'sha256':sha(p),'role':r} for i,(p,r) in enumerate(zip(submitted_refs,roles))]
 write(run/'references.json',{'run_id':run.name,'master_version':'2.5','execution_rules_version':'1.6','delivery_status':'prepared','actual_submitted_image_count':0,'planned_submission':records,'inspected_for_planning':records,'structure_guide':{'path':'structure_guide.png','role':'local new-scene geometric comparison guide','submitted':False},'omitted_references_and_reasons':['No previous generated output, preferred output or sibling variation used.','Local guide not submitted: keep five role-specific master/style inputs including both M03 anchor and new brush supplement.'],'scope':'temporary clean planes/brushwork test; master files unchanged','tool_contract':{'mode':'builtin_imagegen','internal_model':None,'reference_weights':None,'path_limit':None,'no_model_size_seed_controls_exposed':True}})
 write(run/'submitted_request.json',{'prompt':c['prompt'],'referenced_image_paths':[str(p) for p in submitted_refs]})
 (run/'brief.md').write_text('# '+c['title']+'\n\n'+cfg['user_request']+'\n\n새 장면 독립 생성 1장. 세 시안은 기존 생성물과 서로의 출력을 입력하지 않는다. 동일 마스터/표면 시험 조건만 공유한다.\nA=기계로 된 1층 위 주택/외부계단. B=폭 좁고 약30% 기계. C=3층.\n이번 표면 조건은 넓은 기본색+희소한 큰 인접톤 붓질. 붓질 전면 금지 해제는 이번 테스트에만 적용. 마스터 미갱신.\n구조/정사영/베이스 C01~04→STRUCTURE, 두 경계/출구/보행/계단 L01~07→STRUCTURE/CURRENT, 건물문/옥상 W04~05→STRUCTURE/CURRENT, 색면/기계/밤/소품 S/W/R→CURRENT/ART. 비율은 계획 및 시각적 추정이며 정확한2D/3D면적 측정 아님.\n',encoding='utf-8')
 (run/'preflight.md').write_text('# 사전 점검\n3개 비중첩 직교 건물/외부계단/두 출구/외곽 소품을 새로 계획. 계획 도해는 최종 QA PASS가 아님. 02의 우측 출구는 A 기계층 내부를 통과하는 보호된 빈 공간으로 설계. 옥상점유와 B의 기계30%는 별개. 밤/흰 등, 건조 지면; 이전 장면의 웅덩이/차량/경비실 미누적. 신규 생성 입력5장 모두 원본/사용자참조이며 outputs 생성 결과 입력 없음. 실제 PNG 후 검수.\n',encoding='utf-8')
write(BATCH/'batch_state.json',{'requested':3,'initial_calls':0,'master_updated':False,'independent':True,'status':'prepared'})
print(json.dumps({'runs':[c['id']+'_'+c['name'] for c in cfg['variations']],'reference_count':len(submitted_refs),'control_files':len(controls)}))

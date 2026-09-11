from pathlib import Path
import json,hashlib,struct,zipfile
ROOT=Path(__file__).resolve().parents[2];B=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
q=read(B/'final_qa.json')
manifest=read(ROOT/'outputs/final_manifest.json')
generated=[]
for p in B.rglob('*.png'):
 if p.name in ['initial.png','reconstructed.png','final.png']:generated.append(p)
generated_hashes={sha(p) for p in generated}
audit=[]
for request in B.rglob('submitted_request.json'):
 a=read(request)
 refs=[]
 for i,p in enumerate(a['referenced_image_paths']):
  p=Path(p); h=sha(p)
  assert h not in generated_hashes, 'Generated image reused: '+str(p)
  refs.append({'index':i+1,'path':str(p),'sha256':h,'role':('new scene guide' if 'guide' in p.name else 'original master or user style reference'),'status':'submitted'})
 run=request.parent
 assert (run/'generation_prompt.txt').read_text(encoding='utf-8').rstrip('\n')==a['prompt'].rstrip('\n')
 for name in ['generation_prompt.txt','generation_prompt.md']:(run/name).write_text(a['prompt'],encoding='utf-8')
 write(run/'references.json',{'delivery_status':'completed','actual_submitted_image_count':len(refs),'delivery_mechanism':'referenced_image_paths','submitted_to_generation':refs,'previous_generated_images_used':False,'sibling_generated_images_used':False,'master_version':'2.5','temporary_style_override':'broad base planes with sparse large neighboring-tone pigment patches','master_updated':False,'internal_model_version':None,'reference_weights':None,'submitted_prompt':{'path':'generation_prompt.txt','character_count':len(a['prompt']),'utf8_bytes':len(a['prompt'].encode('utf-8')),'saved_text_matches_actual_argument':True}})
 audit.append({'request':str(request.relative_to(ROOT)),'input_count':len(refs),'generated_output_hash_reuse':False})
selected_sources=set()
index=['# 새 키워드 독립 시안3장','','모든 시안/보정은 원본 참조와 새 구조 도해만 사용했습니다. 이전 생성물이나 서로의 출력을 입력하지 않았습니다. 마스터 미갱신. 내장 이미지 도구, 실제 출력1448×1086.','','기하 보정과 프레이밍 재구성을 진행했으며 일부 정사영 선군 차이, 2/3번의 출구 연결 불확실이 남았습니다. 전체 QA는 needs_revision입니다. 큰 색면/붓터치 마감은 사용자 비교 대기입니다.','','| 시안 | 최종 이미지 | 실제 전달 프롬프트 | 검수 |','|---|---|---|---|']
for i,e in enumerate(q,1):
 r=B/e['finalRel'];pic=r/e['image'];dims=list(struct.unpack('>II',pic.read_bytes()[16:24]))
 name=f'20260911_153546__night_alley_{i:02d}.png'
 relpic=pic.relative_to(ROOT).as_posix();selected_sources.add(relpic)
 checks=e['checks'];lines=['# '+e['title']+' 최종 전달 후보 검수','','실제 저장된 PNG1448×1086 원본 크기로 열람. 기준: 마스터2.5/실행1.6+이번 요청 한정 붓터치 허용. 전체 status: needs_revision. 사용자 승인 아님.','',e['observations'],'',e['exit'],'','| 검사 | 상태 |','|---|---|']+[f'| {k} | {v} |' for k,v in checks.items()]
 lines += ['','## 선군/상하 대응 근거','원본 화면 좌상단(0,0), 실제 보이는 선을 수동으로 대략 지정. 반복 포장선/경사지붕/그림자를 수평 기준선으로 혼동하지 않음. 좌표는 실제3D 각도/치수 검증이나 보편적인 허용오차가 아님.','']
 for k,v in e['edges'].items():lines.append(f'- {k}: {v[0]} -> {v[1]}')
 lines += ['','C04: 수평 지붕/건물 선군 일부가 같은 방향 베이스 선군과 다른 기울기. 최종 정사영을 완전히 충족했다고 하지 않음. C02는 대응점과 양면 단면의 보이는 일관성을 검사했으며2번은 판독/벡터 차이 UNCERTAIN. C03은 보이는 외곽에 큰 휨/모따기 없음을 뜻하며 물리적인 전체 바닥 평면 검증 아님.','L05 계단/문/장비의 시각 연결은 읽힘. L07 일부기단은기계/경계/소품으로가려 UNCERTAIN. L06은 실내를 보여달라는 요청이 없어 대체로 N/A이며2번은 기계층 통로 깊이 불확실.','R01 필수3동/집위기계층/계단/좁은기계건물/3층/밤/전봇대/쓰레기통/고철은 관찰됨. 기계30%는 시각적 목표이며 정확한 체적비율을 측정하지 않았으므로 해당정량항목은 UNCERTAIN. W05각지붕에 기능설비있으나40~80%면적은정확히검증하지않음.','S03는기존붓질FAIL규칙을이번사용자요청으로대체. 넓은기본색/선택적톤패치는보이나일부는박리처럼읽혀최종취향판정은보류.','새 구조 도해를 직접 주는 재구성에서도 수평선군 오차가 반복됨. 1/2번은 추가 여백 가이드로 크롭을 해소했으며 프레이밍 개선을 정사영 해결로 간주하지 않음. 같은 지시 반복만으로 추가 진전이 확인되지 않아 이 도구 안의 재시도는 중단. 별도3D/API/마스터 변경으로 범위를 확장하지 않음.']
 (r/'review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 write(r/'result.json',{'image':pic.name,'dimensions':dims,'sha256':sha(pic),'backend':'builtin_imagegen','model_version':None,'source':'C:/Users/Yeon Hee Kang/.codex/generated_images/01a08867-7e38-7162-8368-5c8c0df7a0c0/'+e['source'],'selected_final':True,'status':'needs_revision','scene_keywords':'present; exact30% mechanical volume not measurable','style_status':'partial_visual_match_pending_user','checks':checks,'generation_calls_for_this_variant':e['calls'],'previous_or_sibling_images_used':False,'master_updated':False,'review':'review.md'})
 assert not any(x['filename']==name for x in manifest['images'])
 manifest['images'].append({'filename':name,'source':relpic,'qa_status':'needs_revision','selection_reason':e['title']+' 독립 테스트 전달본. 전체 프레이밍 확보, 정사영 선군/일부 통로 불확실 기록. 마스터 미갱신.','evidence':[(r/'result.json').relative_to(ROOT).as_posix(),(r/'review.md').relative_to(ROOT).as_posix()],'dimensions':dims})
 index.append(f'| {i}. {e["title"]} | [이미지](../final/{name}) | [프롬프트]({e["finalRel"]}/generation_prompt.txt) | [검수]({e["finalRel"]}/review.md) |')
# Non-selected original attempts and every guide/reference excluded from the final collection.
for p in B.rglob('*'):
 if p.is_file() and p.suffix.lower() in ['.png','.jpg','.jpeg']:
  rel=p.relative_to(ROOT).as_posix()
  if rel in selected_sources:continue
  if any(x['source']==rel for x in manifest['excluded']):continue
  manifest['excluded'].append({'source':rel,'reason':'구조/프레이밍 보정 중간본' if p in generated else '새 구조 도해 또는 사용자 스타일 참조; 생성 최종 결과 아님'})
for c in read(B/'batch_spec.json')['variations']:
 r=B/(c['id']+'_'+c['name'])/'reconstruction01'
 if c['id']!='03':
  (r/'review.md').write_text('# 중간 재구성 검수\n실제 PNG 열람. 단면 내부와3개건물/기계층/계단은확인되나하단끝이프레임경계에닿고정사영선군오차가남음. needs_revision. 추가큰여백가이드로새로재구성; 이출력자체는입력하지않음.\n',encoding='utf-8')
before=read(B/'master_hashes_before.json')
changed=[p for p,h in before.items() if not (ROOT/p).is_file() or sha(ROOT/p)!=h]
assert not changed,changed
write(B/'integrity_audit.json',{'master_files_checked':len(before),'master_changes':changed,'request_records':audit,'generated_originals':len(generated),'independent_all_calls':True,'external_api_calls':0})
write(B/'batch_state.json',{'requested_final_count':3,'selected_final_count':3,'actual_generation_calls':len(audit),'independent_all_calls':True,'status':'delivered_test_candidates_with_qa_issues','master_updated':False})
write(ROOT/'outputs/final_manifest.json',manifest)
(B/'RESULTS.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
with zipfile.ZipFile(B/'final_prompts.zip','w',zipfile.ZIP_DEFLATED) as z:
 for i,e in enumerate(q,1):z.write(B/e['finalRel']/'generation_prompt.txt',f'night_alley_{i:02d}_prompt.txt')
print(json.dumps({'selected':3,'calls':len(audit),'master_unchanged':len(before),'independence_verified':True,'new_final_names':[f'20260911_153546__night_alley_{i:02d}.png' for i in range(1,4)]}))


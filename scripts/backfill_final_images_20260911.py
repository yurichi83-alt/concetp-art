import pathlib,json,re
root=pathlib.Path.cwd()
out=root/'outputs'
if (out/'final_manifest.json').exists():
 raise SystemExit('Backfill already completed; update final_manifest.json explicitly instead.')
prefixes='20260909_210805 20260909_213351 20260909_215624 20260909_220938 20260909_222803 20260909_224840 20260909_225844 20260909_230638 20260909_234825 20260910_001333 20260910_081337 20260910_082127 20260910_084302 20260910_091407 20260910_093731 20260910_094940 20260910_100548 20260910_111121 20260910_112747 20260910_114834 20260910_115606 20260910_120310 20260910_121332 20260910_122140 20260910_123650 20260910_124620 20260910_132734_independent_baseline 20260910_132734_independent_cassette_routefix 20260910_134620_scrapyard_baseline 20260910_134620_scrapyard_cassette_routefix 20260910_151110 20260910_151850 20260910_153400 20260910_154355 20260910_183400 20260910_185100 20260910_185824 20260910_191326'.split()
dirs=[]
for pref in prefixes:
 matches=[p for p in out.iterdir() if p.is_dir() and p.name.startswith(pref)]
 assert len(matches)==1,(pref,matches)
 dirs.extend(matches)
dirs+=sorted((out/'20260911_080215_l_building_sand_sunset').iterdir())
dirs=[p for p in dirs if p.is_dir()]
images=[]
for p in dirs:
 candidates=[f for f in p.glob('*.png') if not (f.name.startswith(('structure_','user_','attempt')) or 'inspection' in f.name)]
 assert len(candidates)==1,(p,candidates)
 f=candidates[0]
 result=p/'result.json'
 d=json.loads(result.read_text(encoding='utf-8-sig')) if result.exists() else {}
 status=d.get('qa_status',d.get('status',d.get('structural_status','not_recorded')))
 evidence=[]
 if result.exists():evidence.append(result.relative_to(root).as_posix())
 review=p/'review.md'
 if review.exists():
  evidence.append(review.relative_to(root).as_posix())
  if status=='not_recorded':
   m=re.search(r'- status:\s*(\S+)',review.read_text(encoding='utf-8-sig'))
   if m:status=m.group(1)
 reason='요청별 전달본; 자동 보정 중간본 제외'
 if '151110' in p.name or '151850' in p.name:
  status='uncertain' if '151110' in p.name else 'needs_revision'
  evidence.insert(0,'outputs/20260910_151950_scrapyard_repair_pair_delivery/delivery.json')
  reason='최종 delivery.json 지정본 (파일명/시각순서보다 전달 선택 우선)'
 if '134620_scrapyard_baseline' in p.name:
  status='needs_revision'
  evidence.insert(0,'outputs/20260910_140555_scrapyard_geometry_recheck/recheck.json')
  reason='전달본 보관; 후속 재검토 needs_revision 유지'
 if '20260911_' in str(p):
  evidence.insert(0,'outputs/20260911_080215_l_building_sand_sunset/README.md')
 stamp=p.name[:15] if p.name.startswith('2026') else p.parent.name[:15]
 filename=stamp+'__'+f.name
 images.append(dict(filename=filename,source=f.relative_to(root).as_posix(),qa_status=status,selection_reason=reason,evidence=evidence))
selected={e['source'] for e in images}
support=lambda f:(f.name.startswith(('structure_','user_','ldi_user_')) or 'inspection' in f.name) or 'inputs' in f.parts
excluded=[]
for f in sorted(out.rglob('*.png')):
 if f.relative_to(root).as_posix() in selected:continue
 excluded.append({'source':f.relative_to(root).as_posix(),'reason':'참조/가이드/검수 확대본' if support(f) else '자동 보정 중간본 또는 최종 전달 선택에서 제외된 시도'})
manifest={'schema_version':1,'purpose':'final_delivered_images_not_master_approval','selection_date':'2026-09-11','policy':'요청별 최종 전달본. 독립 시안 및 사용자 별도 수정 요청의 전달본은 각각 보존. 자동 보정 중간 시도, 참조/가이드 제외. QA 실패/보류도 실제 전달본이면 상태와 함께 보관.','images':images,'excluded':excluded}
(out/'final_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Selected:',len(images),'Excluded:',len(excluded))

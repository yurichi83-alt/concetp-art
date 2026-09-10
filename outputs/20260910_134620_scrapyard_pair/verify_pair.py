from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
BASE=ROOT/'outputs/20260910_134620_scrapyard_baseline'
CAS=ROOT/'outputs/20260910_134620_scrapyard_cassette'
FIX=ROOT/'outputs/20260910_134620_scrapyard_cassette_routefix'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
within=lambda p,d:Path(p).resolve().is_relative_to(d.resolve())
ref_audit=[]
for directory in [BASE,CAS,FIX]:
    doc=read(directory/'references.json')
    for item in doc['inputs']:
        p=Path(item['path']);assert p.is_file() and item['visually_inspected']
        assert sha(p)==item['sha256'].lower(),p
        if directory==BASE:
            assert within(p,BASE) or within(p,ROOT/'refs'),p
        elif directory==CAS:
            assert within(p,CAS) or within(p,ROOT/'refs') or p==(ROOT/'outputs/20260910_124032_alley_reference_shapes/user_cassette_reference.png'),p
        else:
            assert within(p,CAS),p
        ref_audit.append({'run':directory.name,'input':str(p),'sha256':sha(p)})
deliverables=[]
for directory,out_key,source_key in [(BASE,'output','source'),(FIX,'saved_path','source_path')]:
    r=read(directory/'result.json');assert r['status']=='candidate_pass',r['status']
    out,source=Path(r[out_key]),Path(r[source_key])
    assert sha(out)==sha(source)==r['sha256'].lower()
    deliverables.append({'path':str(out),'source':str(source),'sha256':sha(out),'byte_exact_copy':True})
manifest=read(ROOT/'refs/manifest.json')
for r in manifest['references']:assert sha(ROOT/r['path'])==r['sha256']
record={'status':'two_final_candidates_visually_reviewed','backend':'builtin_image_gen','master_version':'2.3','execution_version':'1.4','requested_final_count':2,'final_count':len(deliverables),'independent_initial_generations':True,'cross_reference_found':False,'cassette_correction_scope':'own candidate only, rear exit wall removal','keywords':'고물상, 식료품 상점 / 낮, 웜톤 / 고물상 건물의 절반은 기계화, 쓰레기통, 굴뚝','finals':deliverables,'actual_inputs_audited':ref_audit,'reference_hashes_verified':len(manifest['references']),'ratio_scope':'about half scrapyard whole architecture mechanized in both. Visual approximation, separate from per-building rooftop40–80%.','user_approved':False,'master_promoted':False}
(RUN/'validation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
link=lambda label,p:f'[{label}](<{p.as_posix()}>)'
lines=['# 고물상·식료품 상점 — 독립 테스트2장','',
'요청: 고물상, 식료품 상점 / 낮, 웜톤 / 고물상 건물의 절반은 기계화, 쓰레기통, 굴뚝.',
'내장 이미지 생성 도구로 각각 신규 생성. 서로의 이미지·구조안·프롬프트를 입력/설계 참고로 사용하지 않았습니다.',
'',
'- '+link('1. 기본 Salvage Cyberpunk',Path(deliverables[0]['path']))+' · '+link('생성 프롬프트',BASE/'prompt.txt')+' · '+link('시각 검수',BASE/'review.md'),
'- '+link('2. 카세트 퓨처리즘',Path(deliverables[1]['path']))+' · '+link('초기 생성 프롬프트',CAS/'prompt.txt')+' · '+link('출구 보정 프롬프트',FIX/'prompt.txt')+' · '+link('시각 검수',FIX/'review.md'),
'',
'두 시안 모두 고물상 건물의 약절반을 본체와 결합된 압축/선별 기계로 구성했습니다. 옥상 설비 점유와 구분되는 건물 구성의 시각 목표이며 정확한3D 체적 측정은 아닙니다.',
'기본안은 새 구조도와 공통 마스터를 사용했습니다. 카세트 시안은 별도로 만든 구조도와 공통 마스터 및 이전에 사용자가 첨부한 카세트 기계 디자인 이미지를 사용했습니다.',
'카세트 시안은 첫 결과의 오른쪽 통로 끝에 생긴 벽을 자기 후보만 사용해 국소 보정했습니다. 첫 후보는 보존하며 최종 전달 장수는2장입니다.',
'두 최종 PNG의 공통 투영·건물 직교 외곽·양면 단면·출구 접근·건물 입구·지붕 지지를 시각 검수했습니다. 기하의 실제 치수/콜라이더는 별도3D 검증 대상입니다.',
'',link('입력 독립성·원본 사본 해시 기록',RUN/'validation.json'),'']
(RUN/'README.md').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps({'final_count':len(deliverables),'independence_verified':True,'all_source_copies_verified':True,'reference_hashes_verified':len(manifest['references'])}))


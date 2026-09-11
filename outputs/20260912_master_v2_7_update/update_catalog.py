"""Synchronize approved reference descriptions and local catalog, preserving prior history."""
from pathlib import Path
import html
import json
import re

root = Path(__file__).resolve().parents[2]
manifest = json.loads((root/'refs/manifest.json').read_text())
old = json.loads((root/'state/history/20260912_master_v2_7_architecture_forms/refs/manifest.json').read_text())
for item in manifest['references']:
    if item['id'] == 'M03-16':
        item['use_only'] = item['use_only'].replace('높이·지붕 변주는 기존 직교 구조 안에서 해석', '높이·지붕·곡면 변주는 현재 공통 정사영·직선축과 접지 규칙 안에서 해석')
        item['role_scope_update_approval_id'] = 'master_update_20260912_v2_7_architecture_forms'
(root/'refs/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
refs = manifest['references']
forms = [r for r in refs if r.get('reference_role') == 'scoped_architecture_form']
examples = [r for r in refs if r.get('reference_role') == 'scoped_architecture_example']

def table(items):
    return '| ID | 파일 | 승인된 형태 역할 | 생성 입력 |\n|---|---|---|---|\n' + '\n'.join(
        f"| {r['id']} | [{r['title']}](../{r['path']}) | {r['use_only']} | {'필요할 때 선택' if r['generation_input_allowed'] else '비교 전용 · 자동 입력 금지'} |" for r in items) + '\n'

section = '''## 최신 건축 형태 보강 — v2.7 / 실행 v1.8 / 2026-09-12

승인: “좋아 메인 레퍼런스에 갱신해줘” (`master_update_20260912_v2_7_architecture_forms`). [승인된 제안](../outputs/20260912_master_architecture_update_proposal/proposal_ko.md)을 반영했다. 제안 파일의 당시 미반영 표기는 이력이며 현재 반영 여부는 이 문서와 승인 기록을 따른다.

- 큰 형태 → 외벽/기능 공간의 깊이 → 표면 표현 순으로 설계한다. 용도·증축·수리 이력이 날개, 후퇴/돌출, 외부 계단·데크·지붕 윤곽과 기계 외장을 결정한다. 모든 건물에 같은 묶음을 넣지 않는다.
- 주된 배치와 직선 구조는 공통 X/Y축을 따른다. 지상 외벽에도 둥근 모서리·곡면 외장·둥근 기계형 건축을 허용한다. 모호한 쐐기 틈·납득하기 어려운 접합·임의 사선 건물 회전은 피한다. 곡면 접선은 수평 구조축 검사와 구분하고 모든 곡면을 사각 받침으로 둘러싸지 않는다. 곡면 개수/반지름/비율은 고정하지 않는다. 정사각 베이스·두 전면 평면 단면·일정 깊이는 유지한다.
- 기계는 외벽 장식뿐 아니라 큰 외장, 구조 프레임, 설비 동 또는 비거주층 자체가 될 수 있다. '2층이 기계'는 그 층의 주된 부피가 설비라는 의미다. 각 건물의 사람용 입구와 윗면40~80% 기능 구성은 유지하고, 요청한 층별 기계 비중과 구분한다. 기계층 위에 같은 기계 세트를 중복 추가하지 않는다.
- 후면 두 방향에 기능 출구 하나씩, 총2개를 둔다. 건물·담·설비·컨테이너·차량·옹벽 등으로 경계를 만들고 문/셔터 겸용·골목·계단·램프·설비 사이/아래 통로를 기능에 맞게 선택한다. 열린 길의 우발적 차단은 잠긴 출구로 소급 해석하지 않는다. 중앙 공간은 유지하되 장소마다 같은 거대한 빈 마당을 복제하지 않는다.
- 최종 PNG의 공통 정사영, 바닥/기단/셔터/테라스/상층의 대응, 시각적 접지·지지·연결·동선은 검사한다. 실제 콜리전·메시·UV 제작/검증은 이 이미지 작업의 합격 조건이 아니며 미검증을 보류 사유로 쓰지 않는다. 구조 보정 시 의도된 큰 형태는 유지하면서 기하를 재구성한다.
- ㄱ자 건물·기계층 위치·40%/20%·반 크기 주택·건물 수·소품·시간대·팔레트는 장면 한정이다. 여러 장은 색이나 좌우 반전만 바꾸지 않고 큰 형태·깊이·배치 관계를 따로 설계한다.

기존 마스터27장·LDI 표현과 Master03 v2.2 표면 붓터치·Salvage Cyberpunk·기본 우선순위를 유지한다. 다음7장과4장은 별도 분류로 관리한다.

### 건축 형태 참조 7장 — F-01~07

'''+table(forms)+'''
이7장은 사용자 첨부 원본의 큰 형태와 외벽 깊이만 보강한다. 작가·출처·제작 방식은 미확인이며 LDI 자료로 분류하지 않는다. 원본의 카메라·배치·초고층 높이·수상 베이스·미세 질감·실사 밀도·네온·상호/인물은 가져오지 않는다. 필요한 자료만 선택하고 이 자료 때문에01/02 공간·03 표현·04 세계관 원본을 생략하지 않는다. 파일명/ID로 지정할 수 있으며 매번7장 전부를 입력하는 기준은 아니다.

### 형태 비교 예시 4장 — F-08~11

'''+table(examples)+'''
승인된 것은 표의 형태 속성이다. 기존 전체 QA `needs_revision` 및 C04 정사영 오차 등 기하 미승인 기록을 그대로 보존한다. 기본·자동 생성 입력이나 카메라·배치 기준으로 재사용하지 않는다. 후속 명시적 편집/속성 참조 요청은 해당 범위로 별도 처리한다. `positive_reference`는 `approved_aspects`만 승인하며 전체 이미지 합격이 아니다.

등록 원본 경로·해시·치수·입력 권한은 [manifest](../refs/manifest.json), 변경 전 파일은 [스냅샷](../state/history/20260912_master_v2_7_architecture_forms/snapshot_manifest.json), 반영 기록은 [갱신 결과](../outputs/20260912_master_v2_7_update/update_ko.md)에 있다.

'''
p = root/'docs/10_CURRENT_REFERENCES.md'
s = p.read_text()
s = s.replace('# 현재 마스터와 참조 사용 범위 — v2.6 / 2026-09-11','# 현재 마스터와 참조 사용 범위 — v2.7 / 2026-09-12')
s = s.replace('최신 기하 규칙 승인:', '정사영 규칙 승인:')
s = s.replace('마스터 01~04 v2.6은', '마스터 01~04 v2.7은')
s = s.replace('참조 목록 개정은 2026-09-11-brush-support-01이며 표면 보조 B03-01~04는 별도4장이다.', '참조 목록 개정은 2026-09-12-architecture-form-01이며 표면 보조 B03-01~04, 형태 참조 F-01~07, 형태 비교 F-08~11은 각각 별도다.')
s = s.replace('## 최신 표면 표현 보강', section+'## 표면 표현 보강')
s = s.replace('원통형은 기존에 허용한 비건물 탱크 등에 해석하고 건물 보행 경계는 직교를 유지한다.', '현재 v2.7에서는 원통형 등 지상 곡면 건축도 공통 투영·접지·명확한 보행 경계 안에서 해석한다. 임의 사선 건물 회전은 복사하지 않는다. 등록 당시 지상 곡면 제한은 v2.7로 대체되었고 원문은 스냅샷에 보존한다.')
s = s.replace('최신 등록 승인:', '당시 등록 승인:').replace('## 최신 건축 외관 추가', '## 건축 외관 추가 이력')
s = s.replace('## 승인된 v2.3 보강 — 2026-09-10\n', '## 승인된 v2.3 보강 — 2026-09-10\n아래는 당시 이력이다. 건물 곡면 전면 제한과 L07 명칭은 v2.7에서 지상 곡면 허용·시각적 경계 검사로 대체했다. 나머지 구조·출구·아트/세계관은 유지한다.\n')
s = s.replace('회전각·카메라 높이·배율의 영구 수치는 지정하지 않는다. 건물 직교 경계와', '당시 기준: 회전각·카메라 높이·배율의 영구 수치는 지정하지 않았다. 건물 경계의 곡면 제한은 현재 v2.7로 대체하며, 당시 건물 직교 경계와')
p.write_text(s)

p = root/'refs/REFERENCE_MAP.md'; s = p.read_text()
s = s.replace('마스터 v2.6 · 참조 목록 2026-09-11-brush-support-01','마스터 v2.7 · 참조 목록 2026-09-12-architecture-form-01')
for rid in ('M03-16','M03-17'):
    old_item=next(r for r in old['references'] if r['id']==rid)
    new_item=next(r for r in refs if r['id']==rid)
    for key in ('use_only','exclude'):
        s=s.replace(old_item[key],new_item[key])
s += '\n## 건축 형태 참조 7장 — 마스터27장과 별도\n\n큰 형태·외벽 깊이만 선택 입력한다. 원본 카메라·미세 재질·네온·높이/배치를 복사하지 않으며 LDI/세계관 기준은 유지한다.\n\n'+table(forms)
s += '\n## 형태 비교 예시 4장 — 자동 생성 입력 금지\n\n승인 속성만 비교한다. 기존 needs_revision 및 기하 미승인 판정을 보존한다.\n\n'+table(examples)
s += '\nv2.7: 지상 건물 곡면 허용과 공통 직선축·접지를 함께 적용한다. 베이스 곡률 금지는 유지한다. 실제 콜리전 검증은 이미지 합격 조건에서 제외한다. 앞선 날짜별 버전·수량·규칙 설명은 당시 이력이며 현재 해석은 docs/10_CURRENT_REFERENCES.md와 manifest를 따른다.\n'
p.write_text(s)

p=root/'REFERENCE_INDEX.html';s=p.read_text()
s=s.replace('마스터 v2.6', '마스터 v2.7')
s=s.replace('건물 평면은 직교하고 지붕·높이로 다양화한다.', '건물의 주된 직선 구조는 공통 X/Y축을 따르며 지상 곡면·날개·후퇴/돌출·외벽 깊이·지붕으로 다양화한다.')
s=s.replace('v2.5: 최종 이미지는', 'v2.7: 최종 이미지는')
s=s.replace('참조 목록 2026-09-11-brush-support-01:', '참조 목록 2026-09-12-architecture-form-01:')
for rid in ('M03-16','M03-17'):
    old_item=next(r for r in old['references'] if r['id']==rid)
    new_item=next(r for r in refs if r['id']==rid)
    for key in ('use_only','exclude'):
        s=s.replace(html.escape(old_item[key]),html.escape(new_item[key]))
addition='<h2>건축 형태 참조 7장 — 큰 형태·외벽 깊이</h2>\n<p class="scope">F-01~07은 필요한 경우 선택 입력한다. 기존27장·표면4장과 별도다. 원본 카메라·실사 질감·네온·초고층 높이·수상 베이스는 복사하지 않는다. LDI의 표현과 Salvage Cyberpunk를 유지한다.</p>\n'
for group in (forms, examples):
    if group is examples:
        addition+='<h2>형태 비교 예시 4장 — 자동 생성 입력 금지</h2>\n<p class="scope">F-08~11의 승인된 형태만 비교한다. 전체 QA needs_revision 및 기하 미승인 판정은 보존한다.</p>\n'
    for r in group:
        label='선택 입력 가능 · 형태 한정 · 기하 기준 아님' if r['generation_input_allowed'] else '비교 전용 · 자동 입력 금지 · needs_revision · 기하 미승인'
        addition+=f'''<figure id="{r['id']}">
<figcaption>{r['id']} {html.escape(r['title'])}</figcaption>
<p class="meta">{label} · {r['width']}×{r['height']}</p>
<a href="{r['path']}"><img loading="lazy" src="{r['path']}" alt="{r['id']} {html.escape(r['title'])}"></a>
<p><strong>참고 범위:</strong> {html.escape(r['use_only'])}</p>
<p class="exclude"><strong>제외 범위:</strong> {html.escape(r['exclude'])}</p>
</figure>
'''
s=s.replace('</body>',addition+'</body>')
p.write_text(s)

p=root/'state/CHANGELOG.md';s=p.read_text()
entry='''## 2026-09-12 — 건축 형태·곡면 경계 / 마스터2.7·실행1.8·패키지1.7.0
- 승인 “좋아 메인 레퍼런스에 갱신해줘”에 따라 큰 형태·외벽 깊이·증축/수리 이력·기계층 설계를 보강. 지상 곡면 외벽 허용과 공통 직선축/명료한 경계, 임의 사선 회전 제한, 사각 베이스 유지를 구분했다.
- 비건물 차단 경계와 문/골목/계단/램프/설비 통로 등 출구 선택을 실행 설계에 적용. 두 기능 출구·중앙 공간·입구·윗면40~80% 유지, 기계층/기계비율과 지붕 점유를 구분.
- 실제 콜리전·메시·UV 검증은 이미지 합격 조건에서 제외하고 공통 정사영·접지·지지·보이는 동선 검사는 유지. 보정 시 의도된 큰 형태를 단순 상자로 되돌리지 않는다.
- 원본27장·표면 보조4장·LDI 표현(Master03 v2.2)·Salvage Cyberpunk·기본 우선순위 유지. 첨부7장을 F-01~07 형태 한정 선택 참조로 등록하고, 최근4장은 F-08~11 비교 전용으로 연결. 기존 needs_revision/기하 미승인 기록은 보존.
- M03-16/17 역할 문구, 마스터01~04·실행/QA·템플릿·진입문서·프로젝트/목록·승인/갤러리·검증기를 동기화. ㄱ자·기계층 위치·40%/20%·건물 수·팔레트·소품은 장면 한정.
- 승인: master_update_20260912_v2_7_architecture_forms. 목록: 2026-09-12-architecture-form-01.
- 변경 전: state/history/20260912_master_v2_7_architecture_forms/. 반영·검증: outputs/20260912_master_v2_7_update/. 기존 출력·검수·이전 승인 보존.

'''
s=s.replace('# 기준 변경 이력\n\n','# 기준 변경 이력\n\n'+entry,1);p.write_text(s)
print('Catalog, roles, reference scope and changelog synchronized.')

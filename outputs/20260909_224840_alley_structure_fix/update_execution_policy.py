from pathlib import Path
import json, shutil
root=Path('/Users/hyojinnoh/Documents/Codex/GameConcept_Codex')
history=root/'state/history/20260909_224840_structural_correction_policy'
updates={
'AGENTS.md': [('요청한 장수만 생성하며 자동 재시도는 하지 않는다.', '요청 장수는 최종 전달 장수다. 실제 검수에서 구조 오류가 발견되면 사용자 재확인 없이 수정·재생성하고 다시 검수한다. 출구 수·위치, 경계, 건물·지면 정렬, 중앙 동선, 전체 프레이밍·단면이 대상이며 세부 실행/중단 기준은 docs/05_GENERATION_RULES.md를 따른다. 미관 취향만으로 자동 변형을 늘리지 않는다.')],
'.agents/skills/game-env-art/SKILL.md': [
('5. 준비되면 불필요한 추가 동의 없이 요청한 장수를 실제 생성한다.', '5. 준비되면 불필요한 추가 동의 없이 요청 장수를 최종 목표로 실제 생성한다.'),
('7. 결과를 제시하고 규칙 누락이 있으면 숨기지 않는다. 자동 추가 생성이나 자기 승인으로 마스터 변경을 하지 않는다.', '7. 실제 검수에서 출구·경계·건물/지면 배치·동선·프레이밍/단면 등 구조 오류가 있으면 docs/05_GENERATION_RULES.md에 따라 사용자 재확인 없이 수정·재생성하고 재검수한다. 구조가 맞으면 중단한다. 미관 취향만으로 추가 변형을 만들거나 자체 QA로 아트 마스터를 승인하지 않는다.')],
'docs/00_INDEX.md': [('생성 실행 규칙 v1 / 2026-09-09.', '생성 실행 규칙 v1.1 / 2026-09-09.')],
'docs/05_GENERATION_RULES.md': [
('# Generation Execution Rules v1', '# Generation Execution Rules v1.1'),
('요청 장수만 생성한다. “한 장”이면 QA 실패를 이유로 자동으로 더 생성하지 않는다.', '''요청 장수는 최종 전달할 장수다. 사용자가 2026-09-09에 승인한 구조 오류 자동 보정에 따라, 실제 검수에서 구조 오류가 발견되면 재확인 없이 수정·재생성한다.
- 대상: 출구 수·위치·가시성, 뒤쪽 경계, 건물 배치/각도와 지면 정렬, 중앙·출구 동선, 전체 프레이밍과 바닥 단면.
- 수정 전에 실제 오류와 유지할 요소를 기록한다. 바닥 연결이나 건물 배치 자체가 잘못되면 기존 이미지를 그대로 보존하려 하지 말고 M01/M02에 맞춰 재구성한다.
- 매 결과를 실제로 열어 구조를 검수한다. 구조 통과 시 최종 한 장으로 전달하고 추가 변형을 중단한다.
- 자동 보정 이력은 각각 고유 run에 입력·지시·결과·검수와 이전 run 연결을 보존한다. 잘못된 결과는 삭제/덮어쓰지 않는다.
- 스타일·색·손상 밀도에 대한 취향 차이만으로 자동 변형을 늘리지 않는다. 구조 보정 중 기존 아트/세계관/현재 키워드는 유지한다.
- 관찰 불가, 도구 오류/한도, 별도 과금 API·설치·권한 확대 필요, 사용자의 중지, 또는 동일 오류가 반복되고 새로운 수정 전략도 없는 상황에서는 추가 호출을 멈추고 상태를 설명한다. 같은 지시를 무작정 반복하지 않는다.
- 이 승인은 프로젝트 내 내장 도구의 구조 수정에 한정된다. 별도 API·설치·전역 설정·마스터 자동 승격 권한은 포함하지 않는다.'''),
('사용자가 재생성을 명시하면 실패한 부분과 유지 부분을 나눠 다음 run에서 수정한다.', '구조 오류는 위의 상시 승인에 따라 실패한 부분과 유지 부분을 나눠 다음 run에서 수정한다. 구조 외 추가 생성은 현재 사용자 요청 범위를 따른다.')],
'docs/06_QA.md': [
('| L04 | 전면 시야 확보 | 높은 전면 물체가 전투장/단면을 가림 |', '| L04 | 전면 시야 확보 | 높은 전면 물체가 전투장/단면을 가림 |\n| L05 | 지면 연결·건물 정렬 | 바닥이 비틀리거나 서로 다른 평면처럼 갈라짐, 건물 접지/방향과 포장 격자가 모순됨 |'),
('수정/재생성은 사용자가 요청한 범위와 장수 안에서 한다. 무제한 자동 반복 금지.', '구조 오류(C01~C02, L01~L05)는 사용자 상시 승인에 따라 수정·재생성하고 실제 이미지로 재검수한다. 최종 전달 장수는 유지한다. 구조 통과 후 중단하며 도구 장애/관찰 불가/진전 없는 반복의 중단 기준은 docs/05_GENERATION_RULES.md를 따른다. 스타일 취향만으로 추가 변형을 만들지 않는다.')],
'docs/10_CURRENT_REFERENCES.md': [('새 생성 요청 없이 이미지를 생성하지 않는다. 요청 장수만 생성하고 자동 재생성하지 않는다.', '새 작업은 사용자 생성 요청으로 시작한다. 요청 장수는 최종 전달 장수이며, 실제 구조 오류는 2026-09-09 상시 승인에 따라 사용자 재확인 없이 수정·재생성한다. 실행/중단 범위는 docs/05_GENERATION_RULES.md를 따른다. 구조 보정 승인은 아트 마스터/생성 결과의 자동 승격 승인이 아니다.')],
'START_HERE_KO.md': [
('자동 재생성은 하지 마.', '구조 오류가 있으면 알아서 수정·재생성하고 실제 결과를 다시 검수해줘.'),
('- 기본은 요청한 장수만 생성합니다. QA에서 문제가 나와도 추가 호출은 사용자가 재생성을 요청할 때 합니다.', '- 요청 장수는 최종 전달 장수입니다. 출구·배치·지면·동선·프레이밍 등 구조 오류는 실제 검수 후 자동 수정·재생성합니다. 구조가 맞으면 중단하며, 미관 취향만으로 추가 변형하지 않습니다.')],
'README_KO.md': [('4. 내장 생성 기능으로 요청한 장수만 만듭니다. 별도 API/설치는 동의 없이 사용하지 않습니다.', '4. 내장 생성 기능으로 요청 장수를 최종 목표로 만듭니다. 실제 구조 오류는 자동 수정·재생성하고 재검수합니다. 별도 API/설치는 동의 없이 사용하지 않습니다.')],
'templates/review.md': [
('- further_generation_authorized: false', '- further_generation_authorized: structural_errors_only (2026-09-09 standing approval)'),
('| L04 | NOT_REVIEWED | |', '| L04 | NOT_REVIEWED | |\n| L05 | NOT_REVIEWED | |'),
('Describe what to change and what to preserve; do not auto-regenerate.', 'Record structural faults and preserved elements. Correct and regenerate observed structural errors under docs/05_GENERATION_RULES.md, then inspect the real output again. Stop when structure passes; do not automatically iterate on taste alone.')],
}
all_paths=list(updates)+['project.json','state/approvals.json','state/CHANGELOG.md']
for rel in all_paths:
    src=root/rel
    dst=history/rel
    dst.parent.mkdir(parents=True,exist_ok=True)
    if not dst.exists():
        shutil.copy2(src,dst)
for rel, pairs in updates.items():
    p=root/rel
    content=p.read_text()
    for old,new in pairs:
        if old not in content:
            raise RuntimeError('Expected text missing: '+rel+' / '+old[:60])
        content=content.replace(old,new,1)
    p.write_text(content)
p=root/'project.json'
r=json.loads(p.read_text())
r['execution_rules_version']='1.1'
r['auto_regenerate']=True
r['auto_regenerate_scope']='observed_structural_errors_only'
r['requested_scene_count_semantics']='final_deliverables; structural correction attempts are preserved separately'
r['structural_correction_policy']={'approval_id':'structural_auto_correction_20260909','reference':'docs/05_GENERATION_RULES.md','checks':['C01','C02','L01','L02','L03','L04','L05'],'requires_actual_image_review':True,'stop_on':['structural_checks_pass','user_stop','tool_unavailable_or_limit','cannot_inspect_output','repeated_fault_without_new_corrective_strategy'],'external_api_requires_explicit_consent':True,'auto_master_promotion':False}
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=root/'state/approvals.json'
r=json.loads(p.read_text())
r['entries'].append({'id':'structural_auto_correction_20260909','date':'2026-09-09','type':'execution_policy_update','status':'active','evidence':'앞으로는 구조적으로 문제가 있을 때는 알아서 수정해서 재생성까지 해줘. 지금처럼 출구의 위치나 갯수가 틀리거나 이번에 생성한 건물들의 구조? 아니면 배치 각도 때문인지 지면 공간이 조금 이상하거든 우선 구초레 맞게 수정진행해줘.','scope':'앞으로 실제 구조 오류는 재확인 없이 수정·재생성·재검수. 이번 낮 골목의 출구 수/위치 및 건물·지면 배치 수정 포함. 최종 전달 장수 유지.','supersedes':'이전 자동 재생성 금지 지침 중 실제 구조 오류 보정에 해당하는 범위','approved_aspects':['structural_correction_regeneration','execution_rule_persistence'],'not_approved_aspects':['automatic_art_master_promotion','unrequested_aesthetic_variants','external_api_installation_or_global_config_changes']})
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=root/'state/CHANGELOG.md'
p.write_text(p.read_text()+'''\n## 2026-09-09 — 구조 오류 자동 보정 승인 / 실행 규칙 v1.1
- 사용자 명시 요청으로 출구·경계·배치·지면·동선·전체 프레이밍/단면 오류에 대해 자동 수정·재생성·실제 재검수 허용.
- 한 장은 최종 전달 장수로 해석하며 수정 시도별 원본·입력·지시·결과·검수를 보존.
- 구조 통과 시 중단. 도구/관찰 장애와 진전 없는 반복은 보고. 미관 취향만의 자동 변형과 아트 마스터 자동 승격은 승인 범위에 포함하지 않음.
- QA에 지면 연결·건물 정렬 L05 추가. 기존 01~04 아트/공간 기준과 원본 19장 유지.
- 변경 전 파일은 state/history/20260909_224840_structural_correction_policy/에 보관.
''')
print('Updated structural correction policy in '+str(len(all_paths))+' project files; previous versions preserved.')

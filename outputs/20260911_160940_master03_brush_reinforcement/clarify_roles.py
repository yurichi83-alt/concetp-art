"""Resolve final cross-file role wording found in review."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
APPROVAL = 'master_update_20260911_v2_6_brush_planes'

def read(path):
    return (ROOT / path).read_text(encoding='utf-8')

def write(path, text):
    (ROOT / path).write_text(text, encoding='utf-8')

manifest = json.loads(read('refs/manifest.json'))
for rid, new_text in [
    ('M03-16', '원본의 낮은 시점·원근·공간 배치, 중세/판타지 세계관, 대성당 높이, 인물·깃발·문자, 대각선 보행 경계 제외. 전체 장면·구조·세계관 복사로 기존 기준을 대체하지 않으며 승인된 Master03의 큰 색면·평면 붓터치는 적용'),
    ('M04-04', '이 세계관 자료의 붓질·선화 기법 직접 복사, 인물 직접 삽입·색상 고정 제외. 기능·디자인만 가져오고 최종 표면은 Master03의 승인된 큰 색면·평면 붓터치로 표현'),
]:
    row = next(r for r in manifest['references'] if r['id'] == rid)
    old_text = row['exclude']
    row['exclude'] = new_text
    row['surface_role_approval_id'] = APPROVAL
    for path in ['refs/REFERENCE_MAP.md', 'REFERENCE_INDEX.html']:
        text = read(path)
        assert old_text in text, (rid, path)
        write(path, text.replace(old_text, new_text))
write('refs/manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

template = json.loads(read('templates/references.json'))
template['reference_catalog_revision'] = '2026-09-11-brush-support-01'
write('templates/references.json', json.dumps(template, ensure_ascii=False, indent=2) + '\n')

for path, old, new in [
    ('docs/03_VISUAL_STYLE_V2.md', '사용자 지정으로 참조하더라도 색면·붓터치만 적용하고 기존 구조 오류나 출구 불확실성을 복사하지 않는다.', '현재 승인은 표면 비교 전용이며 생성 입력 허용을 추가하지 않는다. 이후 별도 사용자 요청으로 입력을 지정하면 그 요청 범위에 따라 처리하되, 이번 승인에서 기하·배치까지 승인된 것으로 해석하지 않는다.'),
    ('docs/05_GENERATION_RULES.md', '사용자 지정 시에도 승인된 표면 표현으로 범위를 제한한다.', '현재 승인은 비교 전용이며 생성 입력 허용을 추가하지 않는다. 향후 별도 사용자 입력 지정은 그 요청 범위에 따라 처리하고 이번 표면 승인을 기하·배치 승인으로 확대하지 않는다.'),
    ('templates/brief.md', 'If explicitly selected, apply only color-plane/brushwork traits; exclude their architecture/layout/geometry faults.', 'The current approval permits comparison only and does not authorize generation inputs. A later explicit user reference/edit request is handled within its own scope; this surface approval does not approve their architecture/layout/geometry.'),
]:
    text = read(path)
    assert old in text
    write(path, text.replace(old, new))

path = 'docs/00_INDEX.md'
text = read(path).replace('## 승인 이력 연결\n|', '## 승인 이력 연결\n\n|')
text = text.replace('기본 우선순위 유지 |\n\n| master_update_20260911_v2_6_brush_planes', '기본 우선순위 유지 |\n| master_update_20260911_v2_6_brush_planes')
write(path, text)

path = 'state/approvals.json'
approvals = json.loads(read(path))
approvals['entries'][-1]['implementation'].append('Clarify M03-16 and M04-04 source-role exclusions so they do not reject the approved Master03 surface brushwork.')
approvals['entries'][-1]['reference_ids'] = ['M03-10','M03-16','M04-04','B03-01','B03-02','B03-03','B03-04']
write(path, json.dumps(approvals, ensure_ascii=False, indent=2) + '\n')
print('Cross-file role clarification complete.')

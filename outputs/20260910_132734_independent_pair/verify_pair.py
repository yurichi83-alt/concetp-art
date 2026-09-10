from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
BASE = ROOT / 'outputs/20260910_132734_independent_baseline'
CASSETTE = ROOT / 'outputs/20260910_132734_independent_cassette'
FIX = ROOT / 'outputs/20260910_132734_independent_cassette_routefix'

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inputs(path):
    document = read(path)
    return document.get('inputs', document.get('selected', []))

def contained(path, directory):
    return Path(path).resolve().is_relative_to(directory.resolve())

groups = [(BASE, inputs(BASE / 'references.json')),
          (CASSETTE, inputs(CASSETTE / 'references.json')),
          (FIX, inputs(FIX / 'references.json'))]
audit = []
for group, references in groups:
    for reference in references:
        path = Path(reference['path'])
        assert path.is_file(), path
        assert reference['submitted'] and reference['visually_inspected'], reference
        if group == BASE:
            assert not contained(path, CASSETTE) and not contained(path, FIX), path
            assert contained(path, BASE) or contained(path, ROOT / 'refs'), path
        else:
            assert not contained(path, BASE), path
        if group == CASSETTE:
            allowed = contained(path, CASSETTE) or contained(path, ROOT / 'refs') or path.name == 'user_cassette_reference.png'
            assert allowed and not contained(path, FIX), path
        if group == FIX:
            assert contained(path, CASSETTE) or contained(path, FIX), path
        if reference.get('sha256'):
            assert sha(path) == reference['sha256'], path
        audit.append({'run': group.name, 'input': str(path), 'sha256': sha(path)})

manifest = read(ROOT / 'refs/manifest.json')
for reference in manifest['references']:
    assert sha(ROOT / reference['path']) == reference['sha256'], reference['path']

finals = [BASE / 'independent_alley_baseline.png', FIX / 'cassette_day_alley_final.png']
assert len(finals) == 2 and all(path.is_file() for path in finals)
record = {
    'status': 'two_final_candidates_visually_reviewed',
    'backend': 'builtin_image_gen',
    'master_version': '2.3',
    'execution_version': '1.4',
    'requested_final_count': 2,
    'final_count': 2,
    'independent_initial_generations': True,
    'cross_reference_found': False,
    'cassette_local_route_correction': 'Only its own initial candidate and geometry guide were referenced.',
    'finals': [{'path': str(path), 'sha256': sha(path)} for path in finals],
    'submitted_inputs_audited': audit,
    'unchanged_reference_image_count': len(manifest['references']),
    'visual_review': 'Both final saved PNGs inspected; no critical visible geometric/circulation defect found. This is visual concept QA, not exact 3D/collider validation.',
    'user_approved': False,
    'master_promoted': False,
}
(RUN / 'validation.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')

def link(label, path):
    return f'[{label}](<{path.as_posix()}>)'

lines = [
    '# 독립 생성 테스트 — 도심 속 골목 2장',
    '',
    '공통 키워드: 도심 속 골목 / 낮 / 폐건물과 쓰레기통 / 바닥에 널린 쓰레기.',
    '내장 이미지 생성 도구로 각각 신규 생성. 두 시안은 서로의 이미지나 구조안을 참조하지 않았습니다.',
    '',
    '- ' + link('1. 기본 Salvage Cyberpunk', finals[0]) + ' · ' + link('생성 프롬프트', BASE / 'prompt.txt') + ' · ' + link('시각 검수', BASE / 'review.md'),
    '- ' + link('2. 카세트 퓨처리즘', finals[1]) + ' · ' + link('초기 생성 프롬프트', CASSETTE / 'prompt.txt') + ' · ' + link('통로 보정 프롬프트', FIX / 'prompt.txt') + ' · ' + link('시각 검수', FIX / 'review.md'),
    '',
    '카세트 시안은 독립 생성 후, 우측 통로를 좁히는 소품을 그 시안만 사용해 보정했습니다. 최초 후보는 기록으로 보존하며 최종 전달 수는 2장입니다.',
    '기본안은 신규 구조안과 공통 마스터만, 카세트 시안은 별도의 신규 구조안과 공통 마스터 및 이전에 사용자가 첨부한 기계 디자인 참고만 사용했습니다.',
    '최종 PNG의 직교 건물, 공통 투영, 양면 단면, 두 출구와 접근 동선, 입구 및 옥상 배치를 시각적으로 검수했습니다. 정확한 3D 치수나 충돌체 검증은 아닙니다.',
    '',
    link('입력 독립성·파일 해시 검증', RUN / 'validation.json'),
    '',
]
(RUN / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
print(json.dumps({'final_count': 2, 'independence_verified': True, 'reference_hashes_verified': len(manifest['references']), 'record': str(RUN / 'validation.json')}, ensure_ascii=False))


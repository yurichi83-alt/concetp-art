"""Apply the user-approved surface policy; leave images and historical QA intact."""
from pathlib import Path
import hashlib
import html
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
HISTORY = ROOT / 'state/history/20260911_160940_master03_brush_reinforcement'
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_project import image_dimensions

APPROVAL = 'master_update_20260911_v2_6_brush_planes'
REVISION = '2026-09-11-brush-support-01'
BATCH = 'outputs/20260911_153546_three_independent_night_alleys'

def read(path):
    return (ROOT / path).read_text(encoding='utf-8-sig')

def write(path, value):
    (ROOT / path).write_text(value, encoding='utf-8')

def read_json(path):
    return json.loads(read(path))

def write_json(path, value):
    write(path, json.dumps(value, ensure_ascii=False, indent=2) + '\n')

manifest = read_json('refs/manifest.json')
assert not any(r['id'].startswith('B03-') for r in manifest['references']), 'Update already applied'
source = ROOT / BATCH / 'brush_light_reference.jpg'
destination = ROOT / 'refs/style_support/brush_planes_reference.jpg'
destination.parent.mkdir(parents=True, exist_ok=True)
assert not destination.exists(), 'Do not overwrite a reference'
shutil.copy2(source, destination)

aspects = ['large_clean_base_color_planes', 'sparse_broad_directional_flat_brushwork',
           'neighboring_hue_value_patches_independent_of_weathering']
use = '넓고 깨끗한 기본 색면, 온전한 면에도 드물게 얹힌 큰 방향성 붓터치와 인접 색·명도 변화. 붓터치는 표면의 평면 색 표현이며 손상·박리·부조와 구분'
exclude = '카메라·기하·건물과 출구 배치·형태 복제·특정 팔레트·시간대·물웅덩이·고정 노후화 비율은 승인 범위 밖'
support_specs = [
    ('B03-01', 'refs/style_support/brush_planes_reference.jpg', '넓은 색면과 평면 붓터치 — 외부 보조 자료', True, None),
    ('B03-02', 'outputs/final/20260911_153546__night_alley_01.png', '붓터치 승인 예시 1 — 서측 기계 주택', False, f'{BATCH}/01_western_machine_house/reconstruction02/final.png'),
    ('B03-03', 'outputs/final/20260911_153546__night_alley_02.png', '붓터치 승인 예시 2 — 동측 동력 주택', False, f'{BATCH}/02_eastern_power_house/reconstruction02/final.png'),
    ('B03-04', 'outputs/final/20260911_153546__night_alley_03.png', '붓터치 승인 예시 3 — 후면 압축기 주택', False, f'{BATCH}/03_rear_compressor_house/reconstruction01/reconstructed.png'),
]
supports = []
for rid, path, title, input_allowed, source_output in support_specs:
    data = (ROOT / path).read_bytes()
    fmt, (width, height) = image_dimensions(data)
    item = dict(id=rid, path=path, group='style_support', title=title, use_only=use,
                exclude=exclude, positive_reference=True, reference_role='scoped_style_support',
                source_kind='user_supplied_surface_style_reference' if input_allowed else 'generated_result_scoped_surface_approval',
                width=width, height=height, format=fmt, sha256=hashlib.sha256(data).hexdigest(),
                approved_aspects=aspects, approval_id=APPROVAL, registration_date='2026-09-11',
                default_generation_input=False, generation_input_allowed=input_allowed,
                reference_catalog_revision=REVISION)
    if input_allowed:
        item.update(original_filename='516752053_10165409110267784_3247313175898683043_n.jpg',
                    archived_source_path=f'{BATCH}/brush_light_reference.jpg',
                    provenance='User-supplied external painting; artist/work/source unconfirmed, not asserted to be Little Devil Inside.',
                    selection_scope='Optional surface-only input when relevant or explicitly requested; does not replace M03-10 or change default priorities.')
        item['exclude'] += '; 판타지 고가 건축·거대한 다리 구조·항구·배·인물·낮 조명 구성은 복사하지 않음'
    else:
        review_path = str(Path(source_output).parent.as_posix()) + '/review.md'
        assert (ROOT / review_path).is_file()
        item.update(source_output_path=source_output, review_path=review_path,
                    overall_qa_status_at_registration='needs_revision', geometry_approved=False,
                    selection_scope='Surface comparison only. Do not automatically submit as generation input or reuse layout; later explicit user edit/reference requests are separately scoped.')
    supports.append(item)

m03 = next(r for r in manifest['references'] if r['id'] == 'M03-10')
old_m03_use = m03['use_only']
m03['use_only'] = '큰 깨끗한 색면, 온전한 면에도 드문 큰 방향성 평면 붓터치와 인접 색·명도 변화, 별도로 선택적 손상, 특징적 큰 윤곽, 디테일 집중과 여백의 대비'
m03['surface_role_approval_id'] = APPROVAL
manifest['references'].extend(supports)
manifest.update(master_version='2.6', scoped_style_support_count=4,
                reference_catalog_revision=REVISION, reference_catalog_approval_id=APPROVAL,
                surface_style_approval_id=APPROVAL,
                scoped_positive_reference_semantics='For scoped_style_support, positive_reference approves only approved_aspects; it is not whole-image or geometry approval. The four supports are counted separately from the 27 masters.')
write_json('refs/manifest.json', manifest)

project = read_json('project.json')
project.update(package_version='1.6.0', master_version='2.6', execution_rules_version='1.7',
               visual_style_component_version='2.2', updated_date='2026-09-11',
               master_update_approval_id=APPROVAL, reference_catalog_revision=REVISION,
               reference_catalog_approval_id=APPROVAL,
               optional_surface_style_ids=['B03-01'], approved_surface_example_ids=['B03-02','B03-03','B03-04'])
project['generation_reference_selection'] = project['generation_reference_selection'].replace('Masters 01-04 v2.5:', 'Masters 01-04 v2.6:') + ' Apply Master03 v2.2 clean broad planes and sparse broad flat directional brushwork even on intact surfaces. B03-01 is optional surface-only support, never a new global priority; B03-02/03/04 are approved surface comparison examples, not automatic generation inputs or geometry anchors. Record the actual inputs and their assigned roles.'
project['art_direction']['reference_aspects'].extend(['broad_clean_color_planes', 'sparse_flat_directional_brushwork'])
project['surface_style_policy'] = {
    'approval_id': APPROVAL, 'reference': 'docs/03_VISUAL_STYLE_V2.md',
    'base': 'Large calm clean base-color planes remain dominant and readable.',
    'positive_treatment': 'Add selected sparse broad directional flat pigment strokes/patches in neighboring hue and value, including intact wall, road, roof and vehicle/body surfaces.',
    'weathering_relationship': 'Brushwork is pictorial color variation, independent of rust, grime, peeling or damage; do not require damage to justify a stroke.',
    'stroke_scale': 'Vary with the size and direction of each surface; no fixed pixel size or area percentage.',
    'avoid': ['embossed or impasto relief', 'wavy or broken-glass ripple texture', 'tiny mosaic fragments', 'all-over granular microdetail', 'uniform single-color dead planes'],
    'preserve': ['coherent large light/shadow groups', 'legible volume and silhouettes', 'structural thickness and grounding', 'distinct material response', 'existing mandatory orthographic geometry'],
    'scene_dependent': ['time of day', 'palette', 'lighting color', 'puddles', 'amount of wear'],
    'default_anchor_unchanged': 'M03-10',
    'optional_surface_input': 'B03-01', 'comparison_only_examples': ['B03-02','B03-03','B03-04'],
    'geometry_approval_from_examples': False,
    'auto_regeneration_scope_changed': False,
}
for item in supports[1:]:
    project['scoped_result_examples'].append({
        'reference_id': item['id'], 'path': item['path'], 'approved_aspects': aspects,
        'approval_id': APPROVAL, 'default_generation_input': False, 'generation_input_allowed': False,
        'geometry_approved': False, 'allowed_use': 'Surface treatment comparison only; preserve original needs_revision QA and exclude layout/geometry from approval.'})
write_json('project.json', project)

approvals = read_json('state/approvals.json')
approvals['master_version_approved'] = '2.6'
approvals['entries'].append({
    'approval_id': APPROVAL, 'date': '2026-09-11', 'status': 'approved',
    'user_request': '붓 터치 느낌 괜찮다. 그럼 마스터 레퍼런스에 반영하고 싶은데 반영하기 전에 한번 정리해줘',
    'user_confirmation': '좋아 승인할게 반영해줘',
    'scope': 'Master03 surface depiction reinforcement following the three independent night-alley tests; update positive generation instructions and QA together.',
    'approved_aspects': aspects,
    'implementation': ['Master03 v2.2; master set2.6; execution1.7', 'Broaden sparse flat brushwork to intact surfaces independently of weathering', 'Remove blanket brushwork rejection; retain material/volume/geometry checks', 'Keep M03-10 and all existing master priorities; register four scoped supporting examples separately'],
    'not_approved_aspects': ['test image geometry or layout', 'whole-image master promotion', 'fixed night/palette/puddles', 'fixed half-weathering ratio', 'fixed brush coverage/size'],
    'reference_ids': ['M03-10', 'B03-01','B03-02','B03-03','B03-04'],
    'master_image_count_before': 27, 'master_image_count_after': 27, 'scoped_style_support_count': 4,
    'master_version': '2.6', 'execution_rules_version': '1.7', 'package_version_after': '1.6.0',
    'reference_catalog_revision': REVISION,
    'historical_qa_preserved': True, 'existing_original_reference_bytes_preserved': True,
    'snapshot_path': HISTORY.relative_to(ROOT).as_posix(), 'update_record_path': RUN.relative_to(ROOT).as_posix(),
})
write_json('state/approvals.json', approvals)

tpl = read_json('templates/references.json')
tpl.update(masters_version='2.6', execution_rules_version='1.7')
tpl['reference_role_mapping']['surface_style_support_inputs'] = []
tpl['reference_role_mapping']['surface_style_scope'] = 'Master03 v2.2: broad clean base-color planes plus sparse broad directional flat nearby-tone brushwork, also on intact areas and separate from damage. M03-10 stays representative. B03-01 may be selected for surface-only support; B03-02/03/04 are comparison-only, not automatic generation inputs. Do not transfer their camera/layout/night/palette or promote geometry. Record actual submitted images and roles only.'
write_json('templates/references.json', tpl)

intro = '''## 2026-09-11 — Master03 큰 색면·평면 붓터치 보강 / 마스터2.6·실행1.7·패키지1.6.0
- 사용자 “좋아 승인할게 반영해줘”에 따라 Master03 본문v2.2로 보강. 넓은 깨끗한 색면에 드문 큰 방향성 붓터치·인접 색/명도 변화를 더하며 온전한 면에도 적용한다. 녹·박리와 구분하고 물결·유리·모자이크·부조처럼 보이는 질감을 배제한다.
- 붓질 자체를 배척하는 문구와 QA를 수정하고 생성 프롬프트·브리프·사전/최종 검수·로컬 스킬·메타데이터를 동기화.
- 마스터27장과 M03-10 대표/기본 우선순위 유지. B03-01 외부 표면 보조 자료와 B03-02~04 이번3장 표면 예시를 별도4장으로 등록. 생성 예시는 비교용이며 기존 needs_revision 검수와 기하·출구 승인 범위를 바꾸지 않음.
- 정사영·직교 건물·출구/동선·입구·옥상 및 Salvage Cyberpunk 유지. 밤·팔레트·물웅덩이·노후화 절반·고정 붓 크기/면적 비율은 전역화하지 않음.
- 승인: master_update_20260911_v2_6_brush_planes. 목록: 2026-09-11-brush-support-01.
- 변경 전: state/history/20260911_160940_master03_brush_reinforcement/. 검증/변경 기록: outputs/20260911_160940_master03_brush_reinforcement/.

'''
write('state/CHANGELOG.md', read('state/CHANGELOG.md').replace('# 기준 변경 이력\n\n', '# 기준 변경 이력\n\n' + intro, 1))

for path in ['docs/01_COMPOSITION.md','docs/02_LAYOUT.md','docs/04_WORLD_DESIGN_V2.md']:
    txt = read(path).replace('마스터 01~04 v2.5', '마스터 01~04 v2.6')
    if path == 'docs/01_COMPOSITION.md':
        txt = txt.replace('03 v2.1', '03 v2.2')
    write(path, txt)

idx = read('docs/00_INDEX.md').replace('마스터 01~04 v2.5', '마스터 01~04 v2.6')
idx = idx.replace('패키지 1.5.2 / 마스터 세트 v2.5 / 생성 실행 규칙 v1.6', '패키지 1.6.0 / 마스터 세트 v2.6 / 생성 실행 규칙 v1.7')
idx = idx.replace('참조 목록 개정: 2026-09-11-user-additions-02 — M03-17 추가, 현재27장, 규칙 버전과 기본 우선순위 유지.', '참조 목록 개정: 2026-09-11-brush-support-01 — 마스터27장과 기본 우선순위 유지, 표면 표현 전용 보조4장 별도 등록.')
idx = idx.replace('03 아트 본문은 v2.1 표현을 유지한다.', '03 아트 본문v2.2는 넓은 기본 색면과 온전한 면에도 드문 큰 방향성 평면 붓터치를 명시한다. 녹·박리와 구분하며 M03-10 대표 역할과 기존 LDI 표현 기반을 유지한다.')
idx = idx.replace('최신 등록 승인: 마스터3의 추가 이미지1장 등록 요청. 자세한 이력은 [승인 기록](../state/approvals.json)과 [변경 이력](../state/CHANGELOG.md). 변경 전 파일: state/history/20260911_141832_reference_registration/. 등록 기록: outputs/20260911_141832_reference_registration/.', '| master_update_20260911_v2_6_brush_planes | Master03 큰 색면·평면 붓터치 보강, 생성/검수 동기화, 표면 보조4장 분리 |\n\n최신 승인: 붓터치 테스트 확인 후 “좋아 승인할게 반영해줘”. [승인 기록](../state/approvals.json) · [변경 이력](../state/CHANGELOG.md). 변경 전: state/history/20260911_160940_master03_brush_reinforcement/. 변경·검증: outputs/20260911_160940_master03_brush_reinforcement/.')
idx += '\n표면 보조 B03-01은 필요한 경우 역할을 한정해 입력할 수 있다. B03-02~04는 표면 비교 예시이며 기본 생성 입력이나 기하 기준이 아니다. 상세: [현재 참조 범위](10_CURRENT_REFERENCES.md).\n'
write('docs/00_INDEX.md', idx)

surface_section = '''## 최신 표면 표현 보강 — Master03 v2.2 / 2026-09-11

승인: “붓 터치 느낌 괜찮다”에 이어 정리안을 확인하고 “좋아 승인할게 반영해줘” (`master_update_20260911_v2_6_brush_planes`).
넓고 깨끗한 기본 색면을 유지하며, 온전한 벽·도로·지붕·차량 면에도 큰 방향성의 평면 붓터치와 인접 색·명도 변화로 선택적인 변화를 더한다. 녹·먼지·박리는 별도이고 붓터치의 필수 조건이 아니다. 붓의 면적/방향에 맞춰 크기·밀도를 조절하며 고정 수치나 물결·유리·모자이크·부조 질감은 적용하지 않는다. 큰 명암 덩어리와 입체·접지·재질 구분은 유지한다.

마스터27장은 그대로이며 별도 표면 보조4장을 등록했다. M03-10은 대표이고 기본 우선순위는 그대로다. 이 보강은 밤·특정 색감·흰 조명·물웅덩이·노후화 절반을 전역 규칙으로 만들지 않는다.

| ID | 파일 | 허용 역할 / 생성 입력 |
|---|---|---|
| B03-01 | [brush_planes_reference.jpg](../refs/style_support/brush_planes_reference.jpg) | 외부 그림의 넓은 색면·큰 평면 색 터치만. 필요할 때 선택 입력 가능, 자동 기본 참조 아님 |
| B03-02 | [테스트1](../outputs/final/20260911_153546__night_alley_01.png) | 표면 표현 비교만. 자동 생성 입력 금지 |
| B03-03 | [테스트2](../outputs/final/20260911_153546__night_alley_02.png) | 표면 표현 비교만. 자동 생성 입력 금지 |
| B03-04 | [테스트3](../outputs/final/20260911_153546__night_alley_03.png) | 표면 표현 비교만. 자동 생성 입력 금지 |

B03-01 원본은 사용자 첨부 `516752053_10165409110267784_3247313175898683043_n.jpg`의 바이트 그대로인 보관 사본이다. 작가/작품/출처는 미확인이고 LDI로 단정하지 않는다. 원근·판타지 고가 건축·항구·인물·배·낮 조명 구성은 참고 범위 밖이다.
B03-02~04의 승인 대상은 이번에 확인한 색면/붓터치뿐이다. 기존 전체 QA `needs_revision`, 기하·출구의 불합격/불확실 기록은 유지하고 새 기하 기준으로 승격하지 않는다. 기존 생성물이나 서로를 참조하지 않는 독립 생성 요청에서 이 세 예시를 입력으로 재사용하지 않는다. `positive_reference`는 명시한 `approved_aspects`에만 해당한다.

본문: [Master03](03_VISUAL_STYLE_V2.md). 실제 입력은 선택 후 각 run의 `references.json`에 역할과 함께 기록한다. 원본 27장 등록과 보조4장 등록은 모든 이미지를 한 번에 전송한다는 뜻이 아니다.

'''
current = read('docs/10_CURRENT_REFERENCES.md')
current = current.replace('# 현재 마스터와 참조 사용 범위 — v2.5', '# 현재 마스터와 참조 사용 범위 — v2.6', 1)
current = current.replace('원본 구성과 03·04 아트/세계관은 이전 v2.1 승인에서 유지한다.', '원본 구성과 03·04 아트/세계관의 기반은 이전 v2.1 승인에서 유지하고 표면 표현은 아래 최신 Master03 v2.2 보강을 따른다.', 1)
current = current.replace('마스터 01~04 v2.5는', '마스터 01~04 v2.6은', 1)
current = current.replace('참조 목록 개정은 2026-09-11-user-additions-02이다.', '참조 목록 개정은 2026-09-11-brush-support-01이며 표면 보조 B03-01~04는 별도4장이다.', 1)
current = current.replace('## 추가 등록 — M03-17 / 2026-09-11', surface_section + '## 이전 추가 등록 — M03-17 / 2026-09-11', 1)
write('docs/10_CURRENT_REFERENCES.md', current)

refmap = read('refs/REFERENCE_MAP.md').replace('마스터 v2.5 · 참조 목록 2026-09-11-user-additions-02', f'마스터 v2.6 · 참조 목록 {REVISION}', 1)
refmap = refmap.replace(old_m03_use, m03['use_only'])
refmap += '\n## 표면 표현 보조 4장 — 마스터27장과 별도\n\nM03-10 대표와 기본 우선순위 유지. 긍정 참조는 승인된 표면 범위에만 해당하며 기하/배치 승인이 아니다. B03-01만 선택 입력 가능하고 B03-02~04는 비교용이다.\n\n| ID | 파일 | 역할 (`use_only`) | 제외 (`exclude`) |\n|---|---|---|---|\n'
for item in supports:
    refmap += f"| {item['id']} | [{Path(item['path']).name}](../{item['path']}) | {item['use_only']} | {item['exclude']} |\n"
write('refs/REFERENCE_MAP.md', refmap)

gallery = read('REFERENCE_INDEX.html').replace('마스터 v2.5', '마스터 v2.6').replace('참조 목록 2026-09-11-user-additions-02:', f'참조 목록 {REVISION}:', 1)
gallery = gallery.replace(old_m03_use, m03['use_only'])
gallery = gallery.replace('<h2>마스터 27장', '<p class="scope">v2.6 / Master03 v2.2: 넓은 깨끗한 기본 색면에 온전한 면에서도 드문 큰 방향성 평면 붓터치를 적용한다. 녹·박리와 구분하고 입체·명암·재질은 유지한다. 아래 표면 보조4장은 별도이며 기존27장·기본 우선순위와 기하 승인 범위를 바꾸지 않는다.</p>\n<h2>마스터 27장', 1)
cards = '<h2 id="surface-support">표면 표현 보조 4장 — 승인 범위: 색면·붓터치만</h2>\n<p>마스터27장과 별도다. B03-01은 필요한 경우 표면 전용 입력, B03-02~04는 비교 전용이다. 생성 예시의 기존 전체 QA needs_revision은 유지한다.</p>\n'
for item in supports:
    e = lambda key: html.escape(str(item[key]), quote=True)
    role = '선택 표면 입력 가능 / 기본 아님' if item['generation_input_allowed'] else '표면 비교용 / 자동 생성 입력 금지 / 기하 미승인'
    cards += f'<figure id="{e("id")}">\n<figcaption>{e("id")} {e("title")}</figcaption>\n<p class="meta">{role} · {item["width"]}×{item["height"]}</p>\n<a href="{e("path")}"><img loading="lazy" src="{e("path")}" alt="{e("id")} {e("title")}"></a>\n<p><strong>참고 범위 (use_only):</strong> {e("use_only")}</p>\n<p class="exclude"><strong>제외 범위 (exclude):</strong> {e("exclude")}</p>\n</figure>\n'
gallery = gallery.replace('</body>', cards + '</body>', 1)
write('REFERENCE_INDEX.html', gallery)

write_json(f'{RUN.relative_to(ROOT).as_posix()}/metadata_update.json', {'approval_id':APPROVAL, 'master_count':27, 'scoped_support_count':4, 'support_ids':[i['id'] for i in supports], 'master_version':'2.6', 'execution_rules_version':'1.7', 'visual_style_component_version':'2.2', 'package_version':'1.6.0'})
print('Applied approved surface policy and four scoped supporting records.')

import json
from pathlib import Path
p=Path('outputs/final_manifest.json')
d=json.loads(p.read_text(encoding='utf-8'))
for key in ['salvage_02','cassette_01']:
 folder=Path('outputs/20260911_083852_orthographic_edits')/key
 source=(folder/(key+'_orthographic_candidate.png')).as_posix()
 if not any(e['source']==source for e in d['images']):
  d['images'].append({'source':source,'filename':'20260911_083852__'+key+'_orthographic_candidate.png','qa_status':'needs_revision','selection_reason':'사용자 정투영 편집 요청의 최종 전달 보정본; 평행선 불일치가 남아 정투영 검증 미통과','evidence':[(folder/'result.json').as_posix(),(folder/'review.json').as_posix()]})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


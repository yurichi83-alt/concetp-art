import json
from pathlib import Path
b=Path("C:/Users/Yeon Hee Kang/OneDrive/문서/Codex/background-concept-art/concetp-art/outputs/20260911_153546_three_independent_night_alleys")
p=b/'batch_spec.json'
d=json.loads(p.read_text(encoding='utf-8'))
d['variations'][0]['pole']=[6.8,13.8]
for key in ['scene','prompt']:
 d['variations'][0][key]=d['variations'][0][key].replace('beside the inner end of the left rear passage','beside the outer foot of the house stair, outside its access and both exit passages')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for c in d['variations']:
 for e in c['exits']:
  ex=e['box']
  for role in ['stairs','dumpster']:
   r=c[role]
   assert min(ex[2],r[2])<=max(ex[0],r[0]) or min(ex[3],r[3])<=max(ex[1],r[1]),(c['id'],role)
  x,y=c['pole']
  assert not(ex[0]<=x<=ex[2] and ex[1]<=y<=ex[3]),c['id']
print('Exit approach plans clear of stairs, dumpster and pole in all three variations.')


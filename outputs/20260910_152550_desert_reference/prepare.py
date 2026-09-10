from pathlib import Path
import math,json,shutil
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;ROOT=R.parents[1]
shutil.copy2(Path('C:/Users/YEONHE~1/AppData/Local/Temp/codex-clipboard-20873b2f-11e1-4cc8-9440-72bee700e179.png'),R/'user_reference.png')
im=Image.new('RGB',(1536,1280),'#c5c3bb');d=ImageDraw.Draw(im)
def P(x,y,z=0): return(768+(x-y)*29.44486373,280+(x+y)*17-z*34)
def face(pts,c):
    p=[P(*v) for v in pts];d.polygon(p,fill=c);d.line(p+[p[0]],fill='#454c51',width=3)
def box(a,b,c,e,h,z=0):
    face([(a,e,z),(c,e,z),(c,e,h),(a,e,h)],'#849099');face([(c,b,z),(c,e,z),(c,e,h),(c,b,h)],'#75828d');face([(a,b,h),(c,b,h),(c,e,h),(a,e,h)],'#aeb8ba')
box(0,0,20,20,0,-2.6)
for v in range(2,20,2):
    d.line([P(v,0),P(v,20)],fill='#c1c8c8',width=2);d.line([P(0,v),P(20,v)],fill='#c1c8c8',width=2)
# Continuous rear barriers with designated closed slide gates.
box(0,11,0.2,20,2.4);box(6,0,9,0.2,2.4)
face([(0,13,0),(0,16,0),(0,16,2.3),(0,13,2.3)],'#607c89')
face([(6.1,0,0),(8.9,0,0),(8.9,0,2.3),(6.1,0,2.3)],'#607c89')
# Half-barrel roof extruded along Y, rectangle at ground.
box(0,0,6,11,2)
arc=[(3+3*math.cos(math.pi-i*math.pi/24),2+3*math.sin(math.pi-i*math.pi/24)) for i in range(25)]
for (x,z),(xx,zz) in zip(arc,arc[1:]):face([(x,0,z),(xx,0,zz),(xx,11,zz),(x,11,z)],'#b3b7af')
face([(0,11,0),(6,11,0)]+[(x,11,z) for x,z in reversed(arc)],'#969d99')
face([(1.2,11.01,0),(4.8,11.01,0),(4.8,11.01,2.8),(1.2,11.01,2.8)],'#414f58')
box(9,0,20,5,3.2);box(14,0,20,4,5.0)
box(15,0.5,19.3,3,6.1,5.0);box(10,1,13,3.8,4.0,3.2)
face([(14.8,4.01,0),(16.2,4.01,0),(16.2,4.01,2.3),(14.8,4.01,2.3)],'#42545e')
box(1.3,17,5,19,1.2)
im.save(R/'structure_guide.png')
plan={'projection':'parallel_orthographic','mapping':'u=768+(x-y)*29.44486;v=280+(x+y)*17-z*34','base':[0,0,20,20],'depth':2.6,'constant_depth_screen_px':88.4,'buildings':[{'id':'hangar','footprint':[0,0,6,11],'roof':'semicylinder x crosssection radius3 above z2, extrudedalongY','entry':'terminatingworkroom','roof_coverage_plan':.5},{'id':'service_tower','footprint':[9,0,20,5],'roof':'steppedlevelplatforms, heightmax6.1','entry':'decorativeclosedhumanentry','roof_coverage_plan':.6}], 'central_clear':[7,7,18,18], 'routes':[{'side':'left11','rect':[0,13,10,16],'state':'preclearclosedgate','postclear':'x<0'},{'side':'right1','rect':[6.1,0,8.9,14],'state':'preclearclosedgate','postclear':'y<0'}], 'props':[{'id':'vehicle','rect':[1.3,17,5,19]}], 'guide_not_enforced_geometry':True,'final_QA_pending':True}
def overlap(a,b):return min(a[2],b[2])>max(a[0],b[0]) and min(a[3],b[3])>max(a[1],b[1])
assert all(not overlap(b['footprint'],r['rect']) for b in plan['buildings'] for r in plan['routes'])
(R/'structure_plan.json').write_text(json.dumps(plan,indent=2),encoding='utf-8')
prompt=(R/'generation_prompt.md').read_text(encoding='utf-8').rstrip()
inputs=[str(R/'structure_guide.png'),str(R/'user_reference.png'),str(ROOT/'refs/master03/ldi_10_storefront_style_anchor.png'),str(ROOT/'refs/master04/world_02_heavy_mechanical_arms.png')]
refs={'master':'2.4','execution':'1.5','planned_inputs':inputs,'submitted_to_generation':[],'delivery_status':'prepared','roles':['ONLYgeometrycamera','userdesertsubject/paletteonly','M03artonly','M04designonly'],'omitted':'M01/M02 visually inspected earlier in same session, spatial constraints retained in own guide/text; omitted images to avoid competing cameras. No prior generated scene input.','tool':'builtinimagegen','path_limit_evidence':'previous runtime directly rejected morethan5;4used','prompt_chars':len(prompt),'utf8_bytes':len(prompt.encode('utf-8')),'words':len(prompt.split()),'internal_model_token_rewrite':'unknown'}
(R/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf-8')
(R/'brief.md').write_text('# 첨부 사막 거점 재구성 — 1장\n\n사용자첨부의 낮/사막/격납고/차양/차량/관제시설을 장면 기준으로 사용. 마스터2.4/실행1.5의Salvage세계관/LDI표현 적용. 이전밤/쿨톤/고물상50%기계화/2장비교는 이번요청에 자동계승하지않음.\n\n구조계획과 참조역할은 structure_plan.json/references.json. 건물직교평면, 곡면은격납고지붕에만. 두출구는의도된닫힘, 문앞공간/트랙과개방후연결계획확보. 건물별사람입구/윗면40-80%;차량비대상. 토층/기초/유체공급단면, 중앙비움.\n\n요구대응: STRUCTURE→C01-C04/L01-L05/L07; CURRENTSCENE의실내통로→L06, 입구/지붕→W04/W05, 첨부사막요소→R01/R02; ART/REFROLES→S01-S04/W01-W03/참조제외. 텍스트/아이콘명령으로해석안함. 모든프롬프트변수해결.\n\n정사영최종대조는베이스상하벡터와동일축기단/벽수평선으로실시. 아치곡면을수평축선으로오인하지않음. 중요가림은UNCERTAIN; 계획은결과PASS아님.\n',encoding='utf-8')
(R/'preflight.md').write_text('# PLANNED\n\n단일새이미지, 실제PNG4장참조, 이전출력입력없음. 공통XYZ/단일정사영/평면기본블록/일정단면깊이. 건물/통로겹침검사통과, 중심차량없음. 층별지붕/아치지지와설비적용. 실제결과검수미실시. 메인레퍼런스변경/외부API/설치없음.\n',encoding='utf-8')
print('Prepared four-input desert scene.')

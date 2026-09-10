from pathlib import Path
import math,json,shutil
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;ROOT=R.parents[1]
shutil.copy2('C:/Users/YEONHE~1/AppData/Local/Temp/codex-clipboard-c7a1b09e-52ca-421c-804c-17ebac18a52e.png',R/'user_reference.png')
e=math.radians(38);c=math.cos(e);s=math.sin(e);rt=math.sqrt(2)
def P(x,y,z=0):
    a,b=x-10,y-10;dep=95-(a+b)*c/rt-z*s
    return(768+3400*(a-b)/rt/dep,650-3400*(-(a+b)*s/rt+z*c)/dep)
im=Image.new('RGB',(1536,1280),'#1f2a3c');d=ImageDraw.Draw(im)
def face(points,fill):
    p=[P(*v) for v in points];d.polygon(p,fill=fill);d.line(p+[p[0]],fill='#233145',width=3)
def box(a,b,c,e,h,z=0):
    face([(a,e,z),(c,e,z),(c,e,h),(a,e,h)],'#708294');face([(c,b,z),(c,e,z),(c,e,h),(c,b,h)],'#5c7388');face([(a,b,h),(c,b,h),(c,e,h),(a,e,h)],'#9dacb4')
box(0,0,20,20,0,-2.5)
for v in range(2,20,2):d.line([P(v,0),P(v,20)],fill='#a9b7bc',width=2);d.line([P(0,v),P(20,v)],fill='#a9b7bc',width=2)
# Rear solid barriers; gate panels are intentional pre-clear locks.
box(0,10,.18,20,2.5);box(6,0,8,.18,2.5);box(15,0,20,.18,2.5)
face([(0,12,0),(0,15,0),(0,15,2.4),(0,12,2.4)],'#467e91')
face([(16,0,0),(19,0,0),(19,0,2.4),(16,0,2.4)],'#467e91')
box(0,0,6,10,3.5);box(0,0,4,6,5.1,3.5)
box(.5,.5,3.6,4.7,5.8,5.1);box(.5,6.5,4.8,9.4,4.2,3.5)
box(8,0,15,5.5,3.5);box(8.5,.4,12.5,3.6,4.4,3.5);box(13,.4,14.5,4.7,4.5,3.5)
face([(6.005,6,0),(6.005,7.4,0),(6.005,7.4,2.4),(6.005,6,2.4)],'#334251')
face([(10,5.505,0),(12.4,5.505,0),(12.4,5.505,2.4),(10,5.505,2.4)],'#334251')
box(1,17,4,19,.9);box(11.8,6.2,13.7,7.5,1.0)
im.save(R/'structure_guide.png')
plan={'projection':'single_coherent_mild_perspective','camera':{'distance':95,'focal_pixel':3400,'elevation_degrees':38,'azimuth_degrees':45,'target':[10,10,0]},'squarebase':[0,0,20,20],'depth':2.5,'buildings':[{'id':'left_workshop','rect':[0,0,6,10],'height':5.8,'roofcoverage':.55},{'id':'right_store','rect':[8,0,15,5.5],'height':4.5,'roofcoverage':.56}],'routes':[{'gate':'left11','rect':[0,12,10,15],'state':'preclearclosed','onward':'x<0'},{'gate':'right1','rect':[16,0,19,15],'state':'preclearclosed','onward':'y<0'}],'center':[7,9,15,18],'props':[[1,17,4,19],[11.8,6.2,13.7,7.5]],'guidance_not_hard_constraint':True,'final_measurement':'sameaxisVP/horizon andconsistentdepth, NOTequalpixelthickness required for perspective'}
def overlap(a,b):return min(a[2],b[2])>max(a[0],b[0]) and min(a[3],b[3])>max(a[1],b[1])
assert all(not overlap(b['rect'],r['rect']) for b in plan['buildings'] for r in plan['routes'])
assert all(not overlap(b,r['rect']) for b in plan['props'] for r in plan['routes'])
(R/'structure_plan.json').write_text(json.dumps(plan,indent=2),encoding='utf-8')
p=(R/'generation_prompt.md').read_text(encoding='utf-8').rstrip()
inputs=[str(R/'structure_guide.png'),str(R/'user_reference.png'),str(ROOT/'refs/master03/ldi_10_storefront_style_anchor.png'),str(ROOT/'refs/master04/world_02_heavy_mechanical_arms.png')]
(R/'references.json').write_text(json.dumps({'master':'2.4','execution':'1.5','submitted_to_generation':inputs,'delivery_status':'prepared','roles':['singlecamera/layout','userharborsubject/lightonly','M03artonly','M04functionaldesignonly'],'M01_M02':'inspectedearlier, ownnewguideandtextrulesretainspace; redundantcamerasomitted','prompt_chars':len(p),'utf8_bytes':len(p.encode('utf-8')),'word_count':len(p.split()),'internal_model_tokens_rewrite':'unknown','backend':'builtinimagegen'},ensure_ascii=False,indent=2),encoding='utf-8')
(R/'brief.md').write_text('# 야간 항만 참고 이미지 — 1장\n\n첨부의 창고/차양/젖은 바닥/배경항만/드럼통 불빛을 재구성. 원본 낮은 파노라마카메라 제외. 마스터2.4/실행1.5, Salvage세계관·LDI표현. 이전사막/차량/격납고/카세트비교 자동계승없음.\n\n사전선택: 단일약한투시. 계획카메라는새장면선택이며영구상수아님. 동일축소실점/지평선/깊이변화로최종검수; 정사영픽셀동일길이를요구하지않음. 상하모서리연결/평면단면은필수.\n\n출구:왼쪽x0 y12-15,오른쪽y0 x16-19;양쪽의도된닫힘,접근/개방후연결확보. 각건물장식용사람입구,屋上50-60%기능요소,겹침없는지지. 폐쇄실내L06미해당. 전면낮은소품,중앙빈공간.\n\n대응: STRUCTURE→C01-C04/L01-L05/L07; CURRENTSCENE→R01/R02/W04/W05와Salvage기능W01-W03; ART/REFROLES→S01-S04/참조역할. 미해결변수없음. 최종실제관찰근거별도,가림은UNCERTAIN.\n',encoding='utf-8')
(R/'preflight.md').write_text('# PLANNED, not finalQA\n\n새단일장면/요청장수1.4개PNG실제참조. 건물/소품과두통로의평면비충돌검사통과. 공통카메라/직교건물평면/평면단면/두폐쇄출구/입구/옥상점유/전면시야계획확보. 실제결과PASS아님. 추가API/설치/메인변경없음.\n',encoding='utf-8')
print('Harbor guide and prompt ready.')

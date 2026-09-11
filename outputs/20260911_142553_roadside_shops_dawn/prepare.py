from pathlib import Path
from PIL import Image, ImageDraw
import json, math
root=Path.cwd();run=root/"outputs/20260911_142553_roadside_shops_dawn"
run.mkdir(parents=True,exist_ok=True)
def dump(o):return json.dumps(o,ensure_ascii=False,indent=2)+"\n"
# Orthographic diagram, not generated concept art or a geometric image lock.
W,H=1600,1200; scale=33
def P(x,y,z=0):return (800+(x-y)*scale*math.sqrt(3)/2,290+(x+y)*scale/2-z*scale)
im=Image.new("RGB",(W,H),"#eceff1");d=ImageDraw.Draw(im)
def face(pts,c):d.polygon([P(*p) for p in pts],fill=c,outline="#536471",width=2)
def box(x0,y0,x1,y1,z0,z1,top="#c0c9cb",left="#8b989e",right="#a3b0b7"):
 face([(x0,y1,z0),(x1,y1,z0),(x1,y1,z1),(x0,y1,z1)],left)
 face([(x1,y0,z0),(x1,y1,z0),(x1,y1,z1),(x1,y0,z1)],right)
 face([(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)],top)
box(0,0,20,20,-2,0,"#a6b0b2","#75848f","#84939c")
for i in [4,7,10,13,16]:
 d.line([P(i,0),P(i,20)],fill="#919da3",width=1);d.line([P(0,i),P(20,i)],fill="#919da3",width=1)
# L-footprint: two orthogonal adjacent rectangles; no angled contact edge.
box(0,0,4,13,0,5.0)
box(4,0,13,4,0,3.3)
# Deliberate open alley gaps at x=0,y13..16 and y=0,x13..16.
box(0,16,0.45,20,0,2.7);box(16,0,20,0.45,0,2.7)
# Exits have clear level floor and no cross-gap beam.
# Roof occupied areas: left 28.6/52=55%; right 20/36~56%.
box(0.5,1,3.5,6.5,5,5.7,"#7a8c99")
box(0.5,7.0,2.7,12.5,5,5.5,"#7a8c99")
box(4.5,0.5,9.5,3,3.3,4.0,"#7a8c99")
box(10,0.5,12.5,3.5,3.3,3.85,"#7a8c99")
# Phone and pole are below y13 route strip; truck beyond x16 right route.
box(4.6,10.4,5.8,11.8,0,2.6,"#b7a890","#8b837b","#a29787")
box(5.3,8.3,5.55,8.55,0,5.8,"#8c806b")
box(16.7,9.0,19.0,13.0,0.4,1.0,"#a99788")
box(16.7,9.0,19.0,10.8,1.0,1.9,"#b6aaa1")
im.save(run/"structure_guide.png")
plan=dict(projection="orthographic_parallel",camera=dict(formula="(800+(x-y)*33*sqrt(3)/2,290+(x+y)*33/2-z*33)",scene_only=True),
 base=dict(footprint=[[0,0],[20,0],[20,20],[0,20]],top_z=0,bottom_z=-2),
 building=dict(id="L_shop",footprint=[[0,0],[13,0],[13,4],[4,4],[4,13],[0,13]],
 wings=[dict(bounds=[0,0,4,13],height=5,roof_coverage=28.6/52),dict(bounds=[4,0,13,4],height=3.3,roof_coverage=20/36)],
 entrances="human doors/shutters facing street, decorative; two map exits are separate alleys",
 roof="level supported equipment platforms and coherent roof height step"),
 exits=[dict(id="back_left",gap=[0,13,0.45,16],state="open",route_bounds=[0,13,10,16]),
 dict(id="back_right",gap=[13,0,16,0.45],state="open",route_bounds=[13,0,16,10])],
 clear_center=[7,7,14,14],props=dict(phone=[4.6,10.4,5.8,11.8],pole=[5.3,8.3,5.55,8.55],truck=[16.7,9,19,13]),
 intended_height_max=6.5,plan_checks=dict(orthogonal_footprint=True,clear_routes=True,roof_coverage_planned=True),
 limitations="2D diagram and scene coordinates are planning only, not hard image-generator geometry control or verified 3D gameplay collision.")
def intersects(a,b):return max(a[0],b[0])<min(a[2],b[2]) and max(a[1],b[1])<min(a[3],b[3])
for bounds in plan["props"].values():
 for e in plan["exits"]: assert not intersects(bounds,e["route_bounds"])
pts=plan["building"]["footprint"]
assert all((x1==x2) != (y1==y2) for (x1,y1),(x2,y2) in zip(pts,pts[1:]+pts[:1]))
(run/"structure_plan.json").write_text(dump(plan),encoding="utf-8")
manifest=json.loads((root/"refs/manifest.json").read_text(encoding="utf-8"))
ids=["M01-01","M02-01","M03-17","M04-08"]
refs=[next(x for x in manifest["references"] if x["id"]==i) for i in ids]
record=json.loads((root/"templates/references.json").read_text(encoding="utf-8"))
record.update(run_id=run.name,scene_id=run.name,delivery_status="prepared_not_submitted",delivery_mechanism="referenced_image_paths",actual_submitted_image_count=None,
 inspected_for_planning=[dict(id=x["id"],path=x["path"],use_only=x["use_only"],exclude=x["exclude"]) for x in refs],
 submitted_to_generation=[],selected_reference_ids=ids,
 requested_overrides=dict(master03="M03-17",master04="M04-08",scope="this first generation, not global defaults"),
 omitted_references_and_reasons=[dict(ids=["M03-10","M04-02"],reason="User selected M03-17/M04-08 for this request; not submitted."),dict(ids=["A-01","A-02"],reason="Avoid generated-result layout carryover; preserve the four role-specific masters plus scene guide.")])
record["structure_guide"].update(path=(run/"structure_guide.png").relative_to(root).as_posix(),coordinate_camera_source_path=(run/"structure_plan.json").relative_to(root).as_posix(),projection_mode="orthographic_parallel",inspected=False,submitted=False)
record["tool_contract"].update(checked_at="2026-09-11",tool_name="image_gen.imagegen",contract_source="current exposed tool schema",
 selected_image_parameter="referenced_image_paths",supported_input_formats_verified=["PNG","JPEG"],
 unexposed_or_unverified=dict(internal_model_version="unknown",reference_weights="unknown",prompt_text_limit="unknown",revised_prompt="unknown"),
 confirmed_contract_facts_with_evidence=["Prompt and referenced_image_paths accepted fields; no exposed model/size/seed control.","Prior observed path-input rejection above five images; this call plans five."])
(run/"references.json").write_text(dump(record),encoding="utf-8")
(run/"brief.md").write_text("""# 생성 브리프
요청: 도로변 상점가 / 새벽, 라이팅은 흰 톤으로 / ㄱ자 건물, 공중전화 박스, 전봇대, 잡초, 픽업트럭 / 한 장
이번 첫 생성 마스터3=M03-17, 마스터4=M04-08. 전역 기본값 변경 없음. 내장 이미지 생성, 신규 장면.
마스터v2.5 / 실행v1.6 / 참조 목록2026-09-11-user-additions-02.
한 ㄱ자 상점 건물, 지붕별 약55% 설비 계획, 뒤쪽 양면 끝 부근에 열린 골목 두 개. 건물 입구는 장식, 출구는 별도 골목. 중앙과 동선에 차량/전화부스/전봇대가 겹치지 않게 계획.
요구사항 대응: C01~C04=STRUCTURE의 정사영·전체베이스·평면단면·공통축; L01~L07=직교L평면·뒤쪽골목2개·장애물없는접근/접지/지붕지지; L06=불필요한 실내 노출 없음, 보이는 창에는 깊이.
W04/W05=CURRENT의 사람문·셔터/옥상40~80%; S01~04=ART의 큰색면·선택적손상·간결한3D/부피; W01~03=장면전체수리/회수기술과M04-08설비; R01=새벽백색등/ㄱ자/공중전화/전봇대/잡초/픽업1대; R02=기존사막/야간출력을입력하지않은새상점가.
""",encoding="utf-8")
(run/"preflight.md").write_text("""# 사전 확인
- 원본4장과 신규 구조 가이드, 총5개 경로를 첫 호출에 사용 예정.
- M03-17/M04-08 사용자 지정 적용, 다른03/04 대표 이미지 미첨부.
- 공통 정사영 좌표와 직교L외곽선 검사 완료. 소품 영역과 두 보호통로의 평면 겹침 없음.
- 원본 이미지 열람 완료; 가이드는 호출 전 실제 열람. 기하 계획은 최종 결과 PASS 증거가 아님.
- 요구사항은 brief 대응표 및 실제 프롬프트3구역에 포함. 새벽 흰 조명, 녹색CRT 제외.
- API/설치/전역 설정 변경 없음. 실제 반환 해상도/모델 정보는 호출 후 확인.
""",encoding="utf-8")
print(str(run))

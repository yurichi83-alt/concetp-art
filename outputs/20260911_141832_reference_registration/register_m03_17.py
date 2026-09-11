from pathlib import Path
import collections, hashlib, html, importlib.util, json, re, shutil, sys
from html.parser import HTMLParser
from PIL import Image
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parents[2]
out=root/"outputs/20260911_141832_reference_registration"
hist=root/"state/history/20260911_141832_reference_registration"
rev="2026-09-11-user-additions-02"
aid="reference_registration_20260911_m03_17"
def read(p): return (root/p).read_text(encoding="utf-8")
def dump(o): return json.dumps(o,ensure_ascii=False,indent=2)+"\n"
def once(t,a,b):
 assert t.count(a)==1,(a,t.count(a))
 return t.replace(a,b,1)
m=json.loads(read("refs/manifest.json")); p=json.loads(read("project.json")); a=json.loads(read("state/approvals.json"))
baseline=json.loads(dump(dict(manifest=m,project=p,approvals=a)))
assert m["master_image_count"]==26 and len(m["references"])==31
r=dict(id="M03-17",path="refs/master03/test_02.jpg",group="master03",
 title="다양한 건축 비례·지붕과 바랜 색면 표현",
 use_only="폭·높이·상층 후퇴에 따른 건축 덩어리와 실루엣의 변화, 다양한 지붕 윤곽, 창·발코니·외부 연결부의 선택적 디테일, 바랜 적색·청색·크림색의 큰 색면과 도장 박리, 넓은 명암으로 읽히는 재질",
 exclude="원본 카메라·원근·초고층 적층·과밀 배치·해안 도시 세계관·물/배/인물/식생의 자동 삽입 제외. 원통형 건물이나 회전된 건물의 보행 경계를 복사하지 않고 직교 건물 규칙 유지; 원통 형태는 허용된 비건물 탱크 등에 해석. 지붕 비움·높이·동선·구조 불일치의 근거로 사용하지 않음",
 width=1638,height=2048,format="JPEG",sha256="18081082d25a104b5830b5f5a27bfeb1659cb9f6b241311c240e60998387cbe3",
 reference_aspects=["architectural_proportions_and_silhouettes","roof_profile_variation","faded_color_planes","selective_paint_peeling","architectural_detail_hierarchy"],
 provenance_note="사용자가 마스터03 폴더에 추가한 외부 건축 아트. 작가·작품·출처 및 제작 방식 미확인; Little Devil Inside 자료로 단정하지 않음",
 positive_reference=True,source_kind="user_added_master",original_filename="test_02.jpg",
 reference_role="master",generation_input_allowed=True,registration_date="2026-09-11",approval_id=aid,reference_catalog_revision=rev,
 selection_scope="Approved optional reference. Select by explicit filename/ID or relevant approved aspects; existing global default priorities unchanged.")
with Image.open(root/r["path"]) as im:
 im.load(); assert (im.format,im.size)==("JPEG",(1638,2048))
assert hashlib.sha256((root/r["path"]).read_bytes()).hexdigest()==r["sha256"]
assert not any(x["id"]==r["id"] or x["path"]==r["path"] or x["sha256"]==r["sha256"] for x in m["references"])
m["references"].append(r)
m.update(master_image_count=27,approved_supplement_count=8,approved_user_addition_count=3,reference_catalog_revision=rev,reference_catalog_approval_id=aid)
p.update(package_version="1.5.2",reference_catalog_revision=rev,reference_catalog_approval_id=aid)
p["optional_scene_style_ids"].append(r["id"]);p["approved_user_added_reference_ids"].append(r["id"])
p["generation_reference_selection"]=once(p["generation_reference_selection"],"plus 2 user-added optional references (26 master images)","plus 3 user-added optional references (27 master images)").replace("M03-16/M04-08 are scoped optional masters.","M03-16/M03-17/M04-08 are scoped optional masters.")
entry=dict(id=aid,date="2026-09-11",type="user_added_master_reference_registration",status="active",
 evidence="마스터3 폴더에 한장 더 추가했어. 이것도 추가해줘",
 scope="test_02.jpg를 건축 비례·지붕·색면·손상 표현의 선택 가능한 마스터03 참조로 등록",
 reference_ids=["M03-17"],master_image_count_before=26,master_image_count_after=27,
 reference_catalog_revision=rev,master_version="2.5",execution_rules_version="1.6",package_version_after="1.5.2",
 source_records=[{k:r[k] for k in ("id","path","width","height","format","sha256")}],
 preserved_default_generation_priority_ids=p["default_generation_priority_ids"],
 history_path=hist.relative_to(root).as_posix(),update_record_path=out.relative_to(root).as_posix())
a["entries"].append(entry);a.update(reference_catalog_revision=rev,reference_catalog_approval_id=aid)
a["note"]+=" Catalog 2026-09-11-user-additions-02: 27 masters; optional M03-17 added, previous records and default priorities preserved."
t=json.loads(read("templates/references.json"));t["reference_catalog_revision"]=rev
t["reference_role_mapping"]["user_added_reference_scope"]+=" M03-17: architectural proportions, roof silhouettes, faded color planes and selective paint peeling only; exclude source perspective, vertical overcrowding and coastal scene content. Orthogonal building footprints and all existing structure/roof rules remain mandatory."
changes={k:dump(v) for k,v in [("refs/manifest.json",m),("project.json",p),("state/approvals.json",a),("templates/references.json",t)]}
for rel in ["AGENTS.md","README_KO.md","START_HERE_KO.md","docs/00_INDEX.md","docs/01_COMPOSITION.md","docs/02_LAYOUT.md","docs/03_VISUAL_STYLE_V2.md","docs/04_WORLD_DESIGN_V2.md","docs/05_GENERATION_RULES.md","docs/06_QA.md"]:
 t=read(rel)
 # Current banners/counts only; do not rewrite prior approvals or dated history.
 t=t.replace("사용자 추가 2장(총26장)","사용자 추가 3장(총27장)").replace("사용자 추가 2장(총 26장)","사용자 추가 3장(총 27장)")
 t=t.replace("사용자 추가2장인 마스터26장","사용자 추가3장인 마스터27장")
 t=t.replace("사용자 추가2장으로 총26장","사용자 추가3장으로 총27장")
 t=t.replace("마스터 레퍼런스 26장: 원본19장 + 승인된 LDI 보강5장 + 사용자 추가2장(구도1, 공간1, 시각스타일16, 세계관8)","마스터 레퍼런스 27장: 원본19장 + 승인된 LDI 보강5장 + 사용자 추가3장(구도1, 공간1, 시각스타일17, 세계관8)")
 t=t.replace("마스터 26장, 역할별 폴더","마스터 27장, 역할별 폴더").replace("보관된26장을","보관된27장을").replace("보관된 26장을","보관된 27장을")
 t=t.replace("새 M03-16/M04-08은 역할별 선택 후보","M03-16/M03-17/M04-08은 역할별 선택 후보")
 changes[rel]=t
changes["docs/03_VISUAL_STYLE_V2.md"]=changes["docs/03_VISUAL_STYLE_V2.md"].replace("M03-16은 사용자 추가 외부 아트 자료이며","M03-16/M03-17은 사용자 추가 외부 아트 자료이며")
scope=f"""
## 사용자 추가 표현 참조 — M03-17 / 2026-09-11

[test_02.jpg](../refs/master03/test_02.jpg)(1638×2048, 원본 JPEG)를 추가했다. {r["use_only"]}을 참고한다.

{r["exclude"]}. 원본의 작가·작품·출처와 제작 방식은 미확인이다. 기존 LDI 표현과 Salvage Cyberpunk 세계관을 유지하며 이 이미지의 세계관이나 회화 마감으로 일괄 교체하지 않는다. 파일명 또는 M03-17로 선택 가능하고 최우선 M03-10은 유지한다.
"""
changes["docs/03_VISUAL_STYLE_V2.md"]+=scope
t=read("docs/10_CURRENT_REFERENCES.md")
t=once(t,"사용자 추가 2장을 등록한 총 26장을 사용한다. 참조 목록 개정은 2026-09-11-user-additions-01이다.","사용자 추가 3장을 등록한 총 27장을 사용한다. 참조 목록 개정은 "+rev+"이다.")
t=t.replace("- 03 / M03-01~16:","- 03 / M03-01~17:")
t=once(t,"M03-16은 외부 아트의 건축 덩어리·색면·명암 표현을 보완하며 LDI 출처로 단정하지 않는다.","M03-16/M03-17은 외부 아트의 건축 덩어리·비례·지붕·색면·명암 표현을 보완하며 LDI 출처로 단정하지 않는다.")
t=t.replace("26장은 보관된 기준의 수","27장은 보관된 기준의 수").replace("장면별로 M03-11~16 등에서","장면별로 M03-11~17 등에서")
t=once(t,"최신 등록 승인: “마스터 3, 4","이전 등록 승인: “마스터 3, 4")
section=f"""## 추가 등록 — M03-17 / 2026-09-11

최신 등록 승인: “마스터3 폴더에 한장 더 추가했어. 이것도 추가해줘” ({aid}).
[test_02.jpg](../refs/master03/test_02.jpg), JPEG 1638×2048. 건축의 비례와 지붕·실루엣 변화, 바랜 색면과 큰 도장 박리, 선택적 창·발코니 디테일을 참고한다. 원본의 원근·높은 적층·과밀한 해안 도시 배치는 가져오지 않는다. 원통형은 기존에 허용한 비건물 탱크 등에 해석하고 건물 보행 경계는 직교를 유지한다. 출처는 미확인 외부 아트이며 LDI 자료로 단정하지 않는다.

실제 이미지 확인 후 원본 파일명·바이트를 보존해 등록했다. M03-17 또는 test_02.jpg로 지정할 수 있다. 최우선 M03-10/M04-02와 마스터 규칙v2.5/실행v1.6을 유지한다. 참조 목록 {rev}, 패키지1.5.2, 현재 마스터27장(03:17장/04:8장). 앞선2장 등록 기록은 당시 이력으로 보존한다.
변경 전 파일: {entry["history_path"]}/. 등록·검증: {entry["update_record_path"]}/.

"""
t=once(t,"## 사용자 추가 마스터 2장 —",section+"## 사용자 추가 마스터 2장 —")
changes["docs/10_CURRENT_REFERENCES.md"]=t
t=changes["docs/00_INDEX.md"].replace("패키지 1.5.1 /","패키지 1.5.2 /")
t=once(t,"참조 목록 개정: 2026-09-11-user-additions-01 — M03-16/M04-08 추가, 규칙 버전과 기본 우선순위 유지.","참조 목록 개정: "+rev+" — M03-17 추가, 현재27장, 규칙 버전과 기본 우선순위 유지.")
t=once(t,"| reference_registration_20260911_m03_16_m04_08 | 사용자 추가 M03-16/M04-08 등록, 총26장, 기본 우선순위 유지 |","| reference_registration_20260911_m03_16_m04_08 | 사용자 추가 M03-16/M04-08 등록, 총26장, 기본 우선순위 유지 |\n| "+aid+" | M03-17 추가 등록, 현재27장, 기본 우선순위 유지 |")
t=re.sub(r"최신 등록 승인:.*",f'최신 등록 승인: 마스터3의 추가 이미지1장 등록 요청. 자세한 이력은 [승인 기록](../state/approvals.json)과 [변경 이력](../state/CHANGELOG.md). 변경 전 파일: {entry["history_path"]}/. 등록 기록: {entry["update_record_path"]}/.',t,count=1)
changes["docs/00_INDEX.md"]=t
for rel in ["refs/REFERENCE_MAP.md","REFERENCE_INDEX.html"]:
 t=read(rel)
 t=t.replace("사용자 추가 2장을 등록한 총 26장이다.","사용자 추가 3장을 등록한 총 27장이다.")
 t=t.replace("매번 26장 모두","매번 27장 모두").replace("마스터 26장 — 원본 19장 + LDI 보강 5장 + 사용자 추가 2장","마스터 27장 — 원본 19장 + LDI 보강 5장 + 사용자 추가 3장")
 if rel.endswith(".md"):
  t=once(t,"# Reference Map — 마스터 v2.5 · 참조 목록 2026-09-11-user-additions-01","# Reference Map — 마스터 v2.5 · 참조 목록 "+rev)
  row=f'| {r["id"]} | [test_02.jpg](../{r["path"]}) | {r["use_only"]} | {r["exclude"]} |\n'
  t=once(t,"| M04-01 |",row+"| M04-01 |")
  t+=f"\n참조 목록 {rev}: M03-17(test_02.jpg) 사용자 추가 승인. 건축 비례·지붕·바랜 색면·박리 표현만 참고하며 기존 투영/공간/아트·세계관과 최우선 참조 유지. 현재 마스터27장.\n"
 else:
  t=t.replace("역할을 지정한 사용자 이미지2장을 추가했다.","역할을 지정한 사용자 이미지3장을 추가했다.")
  t=t.replace("참조 목록 2026-09-11-user-additions-01: M03-16/M04-08은","참조 목록 "+rev+": M03-16/M03-17/M04-08은")
  figure=f"""<figure id="M03-17">
<figcaption>M03-17 {html.escape(r["title"])}</figcaption>
<p class="meta">사용자 추가 마스터 · JPEG · 1638×2048</p>
<a href="{r["path"]}"><img loading="lazy" src="{r["path"]}" alt="M03-17 {html.escape(r["title"])}"></a>
<p><strong>참고 범위 (use_only):</strong> {html.escape(r["use_only"])}</p>
<p class="exclude"><strong>제외 범위 (exclude):</strong> {html.escape(r["exclude"])}</p>
</figure>
"""
  t=once(t,'<figure id="M04-01">',figure+'<figure id="M04-01">')
 changes[rel]=t
changes["state/CHANGELOG.md"]=once(read("state/CHANGELOG.md"),"# 기준 변경 이력\n",f"""# 기준 변경 이력

## 2026-09-11 — M03-17 추가 등록 / 패키지1.5.2
- 사용자 요청에 따라 test_02.jpg(1638×2048 JPEG)를 실제 확인하고 건축 비례·지붕·색면·선택적 박리 표현의 마스터로 등록.
- 마스터27장(01:1/02:1/03:17/04:8), 목록 개정 {rev}. 목록·선택 설정·갤러리·문서·승인 기록 동기화.
- 기존 원본 파일/역할·승인 이력·최우선 M03-10/M04-02와 정사영/직교 건물·동선·입구·지붕 규칙 유지.
- 변경 전 파일: {entry["history_path"]}/. 등록·검증: {entry["update_record_path"]}/.
""")
assert not hist.exists()
hist.mkdir(parents=True)
for rel in changes:
 dest=hist/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/rel,dest)
baseline["image_hashes"]={x["path"]:hashlib.sha256((root/x["path"]).read_bytes()).hexdigest() for x in m["references"]}
(hist/"registration_baseline.json").write_text(dump(baseline),encoding="utf-8")
for rel,t in changes.items(): (root/rel).write_text(t,encoding="utf-8",newline="\n")
(out/"registration.json").write_text(dump(dict(approval=entry,registered_reference=r,changed_files=list(changes),verification_status="pending")),encoding="utf-8")
# Verify the catalog, links, defaults, old records, and all original image hashes.
spec=importlib.util.spec_from_file_location("validator",root/"scripts/validate_project.py")
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
report=v.validate(root);assert report["ok"],report
assert m["references"][:-1]==baseline["manifest"]["references"]
assert a["entries"][:-1]==baseline["approvals"]["entries"]
allowed={"package_version","reference_catalog_revision","reference_catalog_approval_id","optional_scene_style_ids","approved_user_added_reference_ids","generation_reference_selection"}
for k,value in baseline["project"].items():
 if k not in allowed: assert p[k]==value,k
for rel,digest in baseline["image_hashes"].items():
 assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest,rel
class Gallery(HTMLParser):
 def __init__(self): super().__init__();self.ids=[];self.images=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=="figure":self.ids.append(d["id"])
  if tag=="img":self.images.append(d["src"])
g=Gallery();g.feed(read("REFERENCE_INDEX.html"))
assert len(g.ids)==32 and set(g.ids)=={x["id"] for x in m["references"]}
assert collections.Counter(g.images)==collections.Counter(x["path"] for x in m["references"])
for x in m["references"]:
 assert read("refs/REFERENCE_MAP.md").count("| "+x["id"]+" |")==1
 assert (root/x["path"]).is_file()
report.update(new_image_fully_decoded=True,preserved_image_hashes=32,prior_reference_records_preserved=31,
 prior_approval_entries_preserved=len(baseline["approvals"]["entries"]),gallery_links_and_ids=32,
 default_priorities_and_existing_policies_preserved=True)
(out/"validation.json").write_text(dump(report),encoding="utf-8")
reg=json.loads((out/"registration.json").read_text(encoding="utf-8"));reg.update(verification_status="passed",verification_report="validation.json")
(out/"registration.json").write_text(dump(reg),encoding="utf-8")
print(dump(report))


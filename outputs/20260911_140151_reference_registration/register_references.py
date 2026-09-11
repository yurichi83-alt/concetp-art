from pathlib import Path
import hashlib, html, json, re, shutil
ROOT = Path(__file__).resolve().parents[2]
REV = "2026-09-11-user-additions-01"
APPROVAL = "reference_registration_20260911_m03_16_m04_08"
HISTORY = "state/history/20260911_140151_reference_registration"
RECORD = "outputs/20260911_140151_reference_registration"
def read(rel): return (ROOT / rel).read_text(encoding="utf-8")
def js(obj): return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
def once(t, old, new):
    assert t.count(old) == 1, (old, t.count(old))
    return t.replace(old, new, 1)
manifest = json.loads(read("refs/manifest.json"))
project = json.loads(read("project.json"))
approvals = json.loads(read("state/approvals.json"))
before = dict(manifest=json.loads(js(manifest)), project=json.loads(js(project)), approvals=json.loads(js(approvals)))
assert manifest["master_image_count"] == 24 and len(manifest["references"]) == 29
new_refs = [
    dict(id="M03-16", path="refs/master03/test_01.jpg", group="master03",
         title="계단식 건축과 큰 색면·명암 표현",
         use_only="건축의 큰 덩어리·실루엣, 넓은 색면, 따뜻한 전경과 차가운 배경의 색 관계, 빛·그림자 위계, 선택적 큰 손상과 재질 단순화. 높이·지붕 변주는 기존 직교 구조 안에서 해석",
         exclude="원본의 낮은 시점·원근·공간 배치, 중세/판타지 세계관, 대성당 높이, 인물·깃발·문자, 대각선 보행 경계 제외. 프로젝트 전체를 회화풍으로 전환하지 않음",
         width=1444, height=1952, format="JPEG",
         sha256="3a44c7457cc2f91645060d14c3ff686a6ba1df782b2f4392565d70266738fd97",
         reference_aspects=["architectural_masses", "broad_color_planes", "light_shadow_hierarchy", "selective_material_damage"],
         provenance_note="사용자가 마스터03 폴더에 추가한 외부 아트 이미지. 작가·작품·출처 미확인; Little Devil Inside 자료로 단정하지 않음"),
    dict(id="M04-08", path="refs/master04/retro_futurism.png", group="master04",
         title="레트로 퓨처리즘 기계·가전 디자인 모음",
         use_only="둥근/각진 케이스의 다양한 비례와 실루엣, 다이얼·노브·손잡이·통풍구·안테나 등 아날로그 조작부, 모듈 조합과 기능적 결합. Salvage Cyberpunk의 회수·수리·개조된 설비와 소품으로 해석",
         exclude="콜라주 배치·흰 배경·원본 카메라·문자/로고·선화/회화 마감의 직접 복사, 화면·소형 장치의 무분별한 증식 제외. 기존 녹색 CRT 제외 지시는 별도 재허용 전까지 우선",
         width=1254, height=1254, format="PNG",
         sha256="bb4d6dbe04e77705d276038dcf2c869ade350a39b9a4eda5c2b0f4d15854c00c",
         reference_aspects=["varied_retro_device_silhouettes", "analog_controls", "modular_casings", "functional_repair_and_reuse"],
         provenance_note="사용자가 마스터04 폴더에 추가한 레트로 기기 디자인 모음. 작가·작품·출처 미확인"),
]
for r in new_refs:
    assert hashlib.sha256((ROOT/r["path"]).read_bytes()).hexdigest() == r["sha256"]
    assert not any(x["id"] == r["id"] for x in manifest["references"])
    r.update(positive_reference=True, source_kind="user_added_master", original_filename=Path(r["path"]).name,
             reference_role="master", generation_input_allowed=True, registration_date="2026-09-11",
             approval_id=APPROVAL, reference_catalog_revision=REV,
             selection_scope="Approved optional reference. Select by explicit filename/ID or relevant approved aspects; existing global default priorities unchanged.")
manifest["references"].extend(new_refs)
manifest.update(master_image_count=26, approved_supplement_count=7, approved_ldi_supplement_count=5,
                approved_user_addition_count=2, reference_catalog_revision=REV, reference_catalog_approval_id=APPROVAL)
project.update(package_version="1.5.1", reference_catalog_revision=REV, reference_catalog_approval_id=APPROVAL,
               approved_user_added_reference_ids=["M03-16", "M04-08"])
project["optional_scene_style_ids"].append("M03-16")
project["optional_world_reference_ids"].append("M04-08")
project["generation_reference_selection"] = once(project["generation_reference_selection"],
    "preserve the original 19 and add 5 scoped LDI architectural supplements (24 master images)",
    "preserve the original 19 and 5 scoped LDI architectural supplements, plus 2 user-added optional references (26 master images)")
project["generation_reference_selection"] += " M03-16/M04-08 are scoped optional masters. Explicit filename/ID selection applies to the current request; registration alone does not change global priorities, the LDI rendering baseline or Salvage Cyberpunk world, or mandate cassette futurism in every image."
approval = dict(id=APPROVAL, date="2026-09-11", type="user_added_master_reference_registration", status="active",
    evidence="마스터 3, 4 에 이미지를 한장씩 추가했는데 확인하고 마스터 이미지에 등록해줘",
    scope="마스터03의 test_01.jpg와 마스터04의 retro_futurism.png를 실제 확인하고 역할별 선택 가능한 마스터로 등록",
    reference_ids=["M03-16","M04-08"], master_image_count_before=24, master_image_count_after=26,
    reference_catalog_revision=REV, master_version="2.5", execution_rules_version="1.6", package_version_after="1.5.1",
    source_records=[{k:r[k] for k in ("id","path","sha256","width","height","format")} for r in new_refs],
    preserved_default_generation_priority_ids=project["default_generation_priority_ids"],
    preserved_aspects=["existing_reference_records_and_image_bytes","existing_approval_entries","orthographic_and_geometry_rules","LDI_art_baseline_and_salvage_world","existing_green_CRT_exclusion"],
    interpretation="Scoped registration of these two files; no global priority promotion or blanket cassette-style mandate.",
    history_path=HISTORY, update_record_path=RECORD)
approvals["entries"].append(approval)
approvals.update(reference_catalog_revision=REV, reference_catalog_approval_id=APPROVAL)
approvals["note"] += " Catalog 2026-09-11-user-additions-01: 26 masters, 2 preferred and 3 review-only images; scoped optional M03-16/M04-08 added with unchanged defaults."
template = json.loads(read("templates/references.json"))
template["reference_catalog_revision"] = REV
template["reference_role_mapping"]["user_added_reference_scope"] = "M03-16: architectural masses/color/value/material simplification only, not confirmed LDI; exclude source camera/world/layout. M04-08: varied retro casings/analog controls/modular joins, adapted to Salvage Cyberpunk and Master03 finish; retain existing green-CRT exclusion. Named selections apply to the current request without promoting global defaults."
changes = {p:js(o) for p,o in [("refs/manifest.json",manifest),("project.json",project),("state/approvals.json",approvals),("templates/references.json",template)]}
for rel in ["README_KO.md","START_HERE_KO.md","docs/00_INDEX.md","docs/01_COMPOSITION.md","docs/02_LAYOUT.md","docs/03_VISUAL_STYLE_V2.md","docs/04_WORLD_DESIGN_V2.md","docs/05_GENERATION_RULES.md","docs/06_QA.md"]:
    t=read(rel)
    t=t.replace("원본 19장+승인된 LDI 보강 5장(총24장)","원본 19장+승인된 LDI 보강 5장+사용자 추가 2장(총26장)")
    t=t.replace("원본 19장 + 승인된 LDI 보강 5장(총 24장)","원본 19장 + 승인된 LDI 보강 5장 + 사용자 추가 2장(총 26장)")
    changes[rel]=t
changes["AGENTS.md"]=once(read("AGENTS.md"),"원본19장+승인 LDI5장인 마스터24장","원본19장+승인 LDI5장+사용자 추가2장인 마스터26장")
changes["README_KO.md"]=changes["README_KO.md"].replace("마스터 레퍼런스 24장: 원본19장 보존 + 승인된 LDI 건축·재질·조명 보강5장(구도1, 공간1, 시각스타일15, 세계관7)","마스터 레퍼런스 26장: 원본19장 + 승인된 LDI 보강5장 + 사용자 추가2장(구도1, 공간1, 시각스타일16, 세계관8)").replace("마스터 24장, 역할별 폴더","마스터 26장, 역할별 폴더")
changes["START_HERE_KO.md"]=changes["START_HERE_KO.md"].replace("원본19장+보강5장으로 총24장","원본19장+LDI 보강5장+사용자 추가2장으로 총26장")
changes["docs/05_GENERATION_RULES.md"]=changes["docs/05_GENERATION_RULES.md"].replace("보관된24장을","보관된26장을").replace("보관된 24장을","보관된 26장을").replace("보류 중인 카세트 퓨처리즘 자료","미승인·보류 중인 자료")
changes["docs/05_GENERATION_RULES.md"]+="\n사용자가 파일명이나 관리 ID를 지정하면 해당 요청의 참조 선택에 반영하고 실제 전달 목록에 기록한다. 새 M03-16/M04-08은 역할별 선택 후보이며 기존 기본 우선순위를 자동 교체하지 않는다. 범위는 manifest와10_CURRENT_REFERENCES를 따른다.\n"
changes["docs/03_VISUAL_STYLE_V2.md"]=once(changes["docs/03_VISUAL_STYLE_V2.md"],"이들은 사용자가 Little Devil Inside 자료라고 지정한 이미지다.","기존 M03-01~15는 사용자가 Little Devil Inside 자료라고 지정한 이미지다. M03-16은 사용자 추가 외부 아트 자료이며 Little Devil Inside 출처로 단정하지 않는다.")
changes["docs/03_VISUAL_STYLE_V2.md"]+="""
## 사용자 추가 표현 참조 — M03-16 / 2026-09-11

[TEST_01](../refs/master03/test_01.jpg)(1444×1952, 원본 JPEG)를 건축의 큰 덩어리·색면·명암 위계·선택적 손상과 재질 단순화의 선택 가능한 마스터로 등록한다. 따뜻한 전경/차가운 배경의 관계와 높이·지붕의 변화는 현재 장소와 기존 직교 구조에 맞게 해석한다.

원본의 낮은 시점·원근, 중세/판타지 세계관, 대성당의 높이, 인물·깃발·문자와 공간 배치를 복사하지 않는다. 작가·작품·출처는 미확인이며 기존 LDI 표현의 기본값을 회화풍으로 일괄 변경하지 않는다. 파일명 test_01.jpg 또는 M03-16으로 선택할 수 있고 최우선 M03-10은 유지한다.
"""
changes["docs/04_WORLD_DESIGN_V2.md"]+="""
## 사용자 추가 기계 디자인 참조 — M04-08 / 2026-09-11

[retro_futurism.png](../refs/master04/retro_futurism.png)(1254×1254)를 레트로 퓨처리즘 기계·가전 디자인의 선택 가능한 마스터로 등록한다. 둥근/각진 케이스의 다양한 비례, 다이얼·노브·손잡이·통풍구·안테나, 모듈 조합과 기능적 결합을 참고한다. 이를 Salvage Cyberpunk의 회수·수리·개조된 설비와 생활 소품으로 옮기고 표면 마감은 마스터03을 따른다.

콜라주 배치·흰 배경·원본 카메라·문자/로고·선화 마감은 복사하지 않는다. 화면과 소형 기기를 무분별하게 늘리거나 녹색 CRT를 재도입하지 않는다. 기존 녹색 CRT 제외 지시는 별도 재허용 전까지 우선한다. 파일명 또는 M04-08로 선택 가능하며 최우선 M04-02는 유지한다. 이번 승인은 이 파일의 등록이며 모든 이미지의 카세트 퓨처리즘 의무화나 과거 미승인 자료 전체의 승격이 아니다.
"""
section=f"""## 사용자 추가 마스터 2장 — 2026-09-11

최신 등록 승인: “마스터 3, 4 에 이미지를 한장씩 추가했는데 확인하고 마스터 이미지에 등록해줘” ({APPROVAL}).

| ID | 파일 | 원본 | 참고 범위 |
|---|---|---|---|
| M03-16 | [test_01.jpg](../refs/master03/test_01.jpg) | JPEG · 1444×1952 | 건축 덩어리, 넓은 색면·명암 위계, 선택적 손상·재질 단순화 |
| M04-08 | [retro_futurism.png](../refs/master04/retro_futurism.png) | PNG · 1254×1254 | 다양한 레트로 기계 외형, 아날로그 조작부, 모듈과 기능적 결합 |

두 파일을 실제 열어 확인했으며 원본 파일명·형식·바이트를 보존했다. M03-16의 작가/작품/출처는 미확인이며 Little Devil Inside 이미지로 분류하지 않는다. 낮은 시점·원근·중세 세계관·인물·장면 배치는 가져오지 않는다. M04-08은 Salvage Cyberpunk에 맞게 수리·재사용하고 마감은03을 따른다. 콜라주·흰 배경·문자/로고는 제외하며 기존 녹색 CRT 제외 지시는 유지한다.

파일명이나 ID로 새 생성/수정의 참조를 지정할 수 있다. 예: “마스터3의 test_01.jpg와 마스터4의 retro_futurism.png를 참고해서 생성해줘.” 명시한 선택은 해당 요청에 반영하며 기본 우선순위 M03-10/M04-02는 그대로다. 새 이미지가 자동으로 모든 생성에 첨부되거나 카세트 퓨처리즘이 모든 장면의 의무 스타일이 되는 것은 아니다. 세부 역할·제외 범위는 manifest에 기록한다.

마스터 규칙v2.5/실행v1.6을 유지하고 참조 목록은 {REV}, 패키지는1.5.1로 개정했다. 이전 파일: {HISTORY}/. 등록·검증: {RECORD}/.

"""
t=read("docs/10_CURRENT_REFERENCES.md")
t=once(t,"최신 승인: “최종 이미지는","최신 기하 규칙 승인: “최종 이미지는")
t=once(t,"마스터 01~04 v2.5는 원본 19장을 보존하고 LDI 보강 5장을 추가한 총 24장을 사용한다.","마스터 01~04 v2.5는 원본 19장과 LDI 보강 5장을 보존하고 사용자 추가 2장을 등록한 총 26장을 사용한다. 참조 목록 개정은 "+REV+"이다.")
t=t.replace("- 03 / M03-01~15:","- 03 / M03-01~16: 기존 M03-01~15는").replace("- 04 / M04-01~07:","- 04 / M04-01~08:")
t=once(t,"M03-10은 대표 원본으로 유지하고 새 5장은 표현을 보강한다.","M03-10은 대표 원본으로 유지하고 LDI 보강 5장은 표현을 보강한다. M03-16은 외부 아트의 건축 덩어리·색면·명암 표현을 보완하며 LDI 출처로 단정하지 않는다.")
t=once(t,"기술의 기능과 사용 이력을 03의 간결한 표현으로 옮긴다.","기술의 기능과 사용 이력을 03의 간결한 표현으로 옮긴다. M04-08은 레트로 기계 케이스·아날로그 조작부의 형태 다양화를 보완한다.")
t=once(t,"## 추가 LDI 5장 —",section+"## 추가 LDI 5장 —")
t=once(t,"24장은 보관된 기준의 수","26장은 보관된 기준의 수")
t=once(t,"장면별로 M03-11~15 등에서 적합한 보강 자료를 선택한다.","장면별로 M03-11~16 등에서 적합한 표현 자료와 M04-08 등 세계관 디자인 자료를 선택한다. 사용자 지정 파일/ID는 해당 요청의 선택에 우선 반영하고 실제 전달 여부를 기록한다.")
changes["docs/10_CURRENT_REFERENCES.md"]=t
t=changes["docs/00_INDEX.md"].replace("패키지 1.5.0 /","패키지 1.5.1 /")
t=once(t,"사용자가 승인한 원칙을",f"참조 목록 개정: {REV} — M03-16/M04-08 추가, 규칙 버전과 기본 우선순위 유지.\n사용자가 승인한 원칙을")
t=once(t,"| master_update_20260911_v2_5 | 최종 정사영 필수·약한 투시 허용 폐지·생성/검수 동기화 |",
       "| master_update_20260911_v2_5 | 최종 정사영 필수·약한 투시 허용 폐지·생성/검수 동기화 |\n"+f"| {APPROVAL} | 사용자 추가 M03-16/M04-08 등록, 총26장, 기본 우선순위 유지 |")
t=re.sub(r"최신 승인:.*",f"최신 등록 승인: 사용자 추가 이미지2장의 마스터 등록 요청. 자세한 이력은 [승인 기록](../state/approvals.json)과 [변경 이력](../state/CHANGELOG.md). 변경 전 문서는 {HISTORY}/, 등록 기록은 {RECORD}/에 보존한다.",t,count=1)
changes["docs/00_INDEX.md"]=t

opening_old="원본 마스터 19장을 유지하고 승인된 Little Devil Inside 보강 5장을 더한 총 24장이다."
opening_new="원본 마스터 19장과 승인된 Little Devil Inside 보강 5장을 유지하고 사용자 추가 2장을 등록한 총 26장이다."
t=read("refs/REFERENCE_MAP.md").replace("마스터 v2.4","마스터 v2.5 · 참조 목록 "+REV,1)
t=t.replace(opening_old,opening_new).replace("매번 24장 모두","매번 26장 모두").replace("## 마스터 24장 — 원본 19장 + 승인 보강 5장","## 마스터 26장 — 원본 19장 + LDI 보강 5장 + 사용자 추가 2장")
def row(r): return f'| {r["id"]} | [{Path(r["path"]).name}](../{r["path"]}) | {r["use_only"]} | {r["exclude"]} |\n'
for r in before["manifest"]["references"]:
    if r.get("reference_role")=="master":
        t,n=re.subn(r"^\| "+re.escape(r["id"])+r" \|.*$",lambda m:row(r).rstrip("\n"),t,flags=re.M)
        assert n==1,r["id"]
t=once(t,"| M04-01 |",row(new_refs[0])+"| M04-01 |")
t=once(t,"\nM03-11~M03-15는 승인",row(new_refs[1])+"\nM03-11~M03-15는 승인")
t+=f"\n참조 목록 {REV}: M03-16/M04-08 사용자 추가 승인. 파일명/ID로 선택 가능하며 최우선 M03-10/M04-02 유지. M03-16의 LDI 출처는 미확인이고 M04-08 등록은 카세트 스타일의 일괄 의무화가 아니다. 날짜별24장·29장 기록은 당시 이력이다.\n"
changes["refs/REFERENCE_MAP.md"]=t
t=read("REFERENCE_INDEX.html").replace(opening_old,opening_new).replace("매번 24장 모두","매번 26장 모두")
t=t.replace("원본24장과 기존 아트/세계관은 보존한다.","기존24장과 아트/세계관을 보존하고 역할을 지정한 사용자 이미지2장을 추가했다.").replace("마스터 24장 — 원본 19장 + 승인 보강 5장","마스터 26장 — 원본 19장 + LDI 보강 5장 + 사용자 추가 2장")
for r in before["manifest"]["references"]:
    if r.get("reference_role")=="master":
        def sync(m):
            block=m.group(2)
            for label,key in [("참고 범위","use_only"),("제외 범위","exclude")]:
                block=re.sub(r"(<strong>"+label+r" \("+key+r"\):</strong> ).*?(</p>)",lambda q:q.group(1)+html.escape(r[key])+q.group(2),block)
            return m.group(1)+block+m.group(3)
        t,n=re.subn(r'(<figure id="'+re.escape(r["id"])+r'">)(.*?)(</figure>)',sync,t,flags=re.S)
        assert n==1,r["id"]
for r,marker in [(new_refs[0],'<figure id="M04-01">'),(new_refs[1],'<h2>선호')]:
    title=html.escape(r["id"]+" "+r["title"])
    figure=f"""<figure id="{r['id']}">
<figcaption>{title}</figcaption>
<p class="meta">사용자 추가 마스터 · {r['format']} · {r['width']}×{r['height']}</p>
<a href="{r['path']}"><img loading="lazy" src="{r['path']}" alt="{title}"></a>
<p><strong>참고 범위 (use_only):</strong> {html.escape(r['use_only'])}</p>
<p class="exclude"><strong>제외 범위 (exclude):</strong> {html.escape(r['exclude'])}</p>
</figure>
"""
    t=once(t,marker,figure+marker)
t=once(t,"<h2>마스터 26장",f'<p class="scope">참조 목록 {REV}: M03-16/M04-08은 파일명/ID로 선택 가능한 추가 마스터다. 기본 우선순위 M03-10/M04-02 유지. M03-16은 LDI 출처 미확인 외부 표현 자료이며 M04-08은 레트로 기계의 디자인 범위로 사용한다.</p>\n<h2>마스터 26장')
changes["REFERENCE_INDEX.html"]=t
changes["state/CHANGELOG.md"]=once(read("state/CHANGELOG.md"),"# 기준 변경 이력\n",f"""# 기준 변경 이력

## 2026-09-11 — 사용자 추가 마스터2장 등록 / 패키지1.5.1
- 사용자 요청 {APPROVAL}: M03-16 test_01.jpg(1444×1952)와 M04-08 retro_futurism.png(1254×1254)를 실제 확인해 등록.
- 총26장(01:1, 02:1, 03:16, 04:8). 기존19장·LDI5장·선호2장·검토3장, 승인 이력과 원본 바이트 보존.
- 역할·제외 범위와 파일명/ID 선택 기록. 최우선 M03-10/M04-02와 마스터v2.5/실행v1.6 유지. M03-16의 LDI 출처는 미확인이며 카세트 컨셉을 모든 장면에 의무화하지 않음.
- 참조 목록 {REV}. manifest/프로젝트/문서/갤러리/양식 동기화 및 원본 JPEG 치수 검증 지원.
- 이전 파일: {HISTORY}/. 등록·검증: {RECORD}/. 새 이미지 생성 없음.
""")
# Files prepared in memory; snapshot all existing content before writing.
snapshot=ROOT/HISTORY
assert not snapshot.exists(), "Existing snapshot: inspect before retrying."
snapshot.mkdir(parents=True)
for rel in list(changes)+["scripts/validate_project.py"]:
    dest=snapshot/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(ROOT/rel,dest)
before["preserved_image_hashes"]={r["path"]:hashlib.sha256((ROOT/r["path"]).read_bytes()).hexdigest() for r in before["manifest"]["references"]+new_refs}
(snapshot/"registration_baseline.json").write_text(js(before),encoding="utf-8")
for rel,text in changes.items(): (ROOT/rel).write_text(text,encoding="utf-8",newline="\n")
record=ROOT/RECORD
record.mkdir(parents=True,exist_ok=True)
(record/"registration.json").write_text(js(dict(approval=approval,registered_references=new_refs,changed_files=list(changes)+["scripts/validate_project.py"],verification_status="pending")),encoding="utf-8")
(record/"registration_ko.md").write_text(f"""# 사용자 추가 마스터 등록

- M03-16: test_01.jpg · 1444×1952 JPEG. 건축 덩어리·색면·명암·선택적 손상 표현.
- M04-08: retro_futurism.png · 1254×1254 PNG. 다양한 레트로 기기 외형·아날로그 조작부·모듈 결합.
- 마스터26장. 최우선 M03-10/M04-02와 원본 이미지 바이트 유지.
- 두 파일 실제 열람 완료. 출처 미확인 자료에 작가/작품/LDI 출처를 임의 지정하지 않음.
- 참조 목록 {REV}; 마스터 규칙v2.5/실행v1.6 유지.
- 변경 전 파일·기존 미커밋 내용: {HISTORY}/.
- 승인·해시·참고/제외 범위는 registration.json, 검증은 validation.json 참고.
""",encoding="utf-8")
print(js(dict(updated_files=len(changes),registered_ids=["M03-16","M04-08"],masters=26)))


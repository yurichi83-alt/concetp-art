from pathlib import Path
import collections, hashlib, importlib.util, json, sys
from html.parser import HTMLParser
from PIL import Image
sys.dont_write_bytecode = True
root=Path(__file__).resolve().parents[2]
record=root/"outputs/20260911_140151_reference_registration"
baseline=json.loads((root/"state/history/20260911_140151_reference_registration/registration_baseline.json").read_text(encoding="utf-8"))
manifest=json.loads((root/"refs/manifest.json").read_text(encoding="utf-8"))
project=json.loads((root/"project.json").read_text(encoding="utf-8"))
approvals=json.loads((root/"state/approvals.json").read_text(encoding="utf-8"))
spec=importlib.util.spec_from_file_location("validator",root/"scripts/validate_project.py")
validator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
report=validator.validate(root)
assert report["ok"],report
assert manifest["references"][:29]==baseline["manifest"]["references"]
assert approvals["entries"][:-1]==baseline["approvals"]["entries"]
for key in ["default_generation_priority_ids","default_inspection_ids","geometry_policy","architectural_design_policy","functional_exit_policy","boundary_object_policy","structural_correction_policy","art_direction","world_setting","master_version","execution_rules_version"]:
    assert project[key]==baseline["project"][key],key
assert project["optional_scene_style_ids"]==baseline["project"]["optional_scene_style_ids"]+["M03-16"]
assert project["optional_world_reference_ids"]==baseline["project"]["optional_world_reference_ids"]+["M04-08"]
for rel,digest in baseline["preserved_image_hashes"].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest,rel
counts=collections.Counter()
for r in manifest["references"]:
    with Image.open(root/r["path"]) as im:
        im.load()
        assert im.size==(r["width"],r["height"]),r["id"]
        fmt,wh=validator.image_dimensions((root/r["path"]).read_bytes())
        assert (fmt,wh)==(im.format,im.size),r["id"]
    if r.get("reference_role")=="master": counts[r["group"]]+=1
assert dict(counts)==dict(master01=1,master02=1,master03=16,master04=8),counts
class Gallery(HTMLParser):
    def __init__(self):
        super().__init__()
        self.figures=[]
        self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="figure": self.figures.append(a["id"])
        if tag=="img": self.images.append(a["src"])
g=Gallery()
g.feed((root/"REFERENCE_INDEX.html").read_text(encoding="utf-8"))
assert len(g.figures)==31 and len(set(g.figures))==31
assert set(g.figures)=={r["id"] for r in manifest["references"]}
assert collections.Counter(g.images)==collections.Counter(r["path"] for r in manifest["references"])
for path in g.images: assert (root/path).is_file(),path
text=(root/"refs/REFERENCE_MAP.md").read_text(encoding="utf-8")
for r in manifest["references"]:
    assert text.count("| "+r["id"]+" |")==1,r["id"]
    assert r["use_only"] in text and r["exclude"] in text,r["id"]
jpeg=(root/"refs/master03/test_01.jpg").read_bytes()
png=(root/"refs/master04/retro_futurism.png").read_bytes()
invalid=[b"",b"GIF89a",png[:20],jpeg[:2],jpeg[:20],b"\xff\xd8\xff\xd9",b"\xff\xd8\xff\xe0\x00\x01",b"\xff\xd8\xff\xe0\xff\xff"]
for data in invalid:
    try: validator.image_dimensions(data)
    except ValueError: pass
    else: raise AssertionError("Invalid header accepted")
report.update(group_counts=dict(counts),full_decoded_images=31,preserved_image_hashes=31,
              prior_reference_records_preserved=29,prior_approval_entries_preserved=len(baseline["approvals"]["entries"]),
              default_priorities_and_core_policies_unchanged=True,
              gallery_ids_and_links_verified=31,reference_map_rows_verified=31,rejected_invalid_headers=len(invalid))
(record/"validation.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
registration=json.loads((record/"registration.json").read_text(encoding="utf-8"))
registration["verification_status"]="passed"
registration["verification_report"]="validation.json"
(record/"registration.json").write_text(json.dumps(registration,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,ensure_ascii=False,indent=2))


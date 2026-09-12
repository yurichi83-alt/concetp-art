#!/usr/bin/env python3
"""Read-only package validation. No network, installations, or image-model calls.

Python 3.9+. Checks required files, reference integrity, IDs, and PNG/JPEG dimensions.
Does NOT verify visual layout, style, exits, or model availability.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path

REQUIRED = [
    "AGENTS.md", "START_HERE_KO.md", "FIRST_MESSAGE.txt", "README_KO.md",
    "project.json", "refs/manifest.json", "REFERENCE_INDEX.html",
    ".agents/skills/game-env-art/SKILL.md",
    ".agents/skills/game-env-art/agents/openai.yaml",
    "docs/00_INDEX.md", "docs/01_COMPOSITION.md", "docs/02_LAYOUT.md",
    "docs/03_VISUAL_STYLE_V2.md", "docs/04_WORLD_DESIGN_V2.md",
    "docs/05_GENERATION_RULES.md", "docs/06_QA.md", "docs/07_CODEX_SETUP.md",
    "docs/08_COMMANDS.md", "docs/09_SOURCES.md", "docs/10_CURRENT_REFERENCES.md", "state/setup_status.json",
    "state/approvals.json", "templates/brief.md", "templates/preflight.md",
    "templates/review.md", "templates/references.json", "templates/generation_prompt.md", "outputs/README.md",
]

def inside(root: Path, rel: str) -> Path:
    path = (root / rel).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Unsafe path outside project: {rel}") from exc
    return path

def image_dimensions(data: bytes) -> tuple[str, tuple[int, int]]:
    """Read PNG/JPEG header dimensions; this is not a full image decoder."""
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        if len(data) < 24 or data[8:16] != b"\x00\x00\x00\rIHDR":
            raise ValueError("Truncated or invalid PNG header")
        width, height = struct.unpack(">II", data[16:24])
        if not width or not height:
            raise ValueError("Invalid PNG dimensions")
        return "PNG", (width, height)
    if not data.startswith(b"\xff\xd8"):
        raise ValueError("Unsupported image format (expected PNG or JPEG)")
    pos = 2
    sof = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
    while pos < len(data):
        if data[pos] != 0xFF:
            raise ValueError("Invalid JPEG marker")
        while pos < len(data) and data[pos] == 0xFF:
            pos += 1
        if pos >= len(data):
            raise ValueError("Truncated JPEG marker")
        marker = data[pos]
        pos += 1
        if marker in (0xD9, 0xDA):
            break
        if marker == 0x01 or 0xD0 <= marker <= 0xD7:
            continue
        if marker in (0x00, 0xD8) or pos + 2 > len(data):
            raise ValueError("Invalid or truncated JPEG segment")
        length = int.from_bytes(data[pos:pos + 2], "big")
        if length < 2 or pos + length > len(data):
            raise ValueError("Truncated JPEG segment")
        if marker in sof:
            if length < 8:
                raise ValueError("Truncated JPEG frame")
            height, width = struct.unpack(">HH", data[pos + 3:pos + 7])
            if not width or not height:
                raise ValueError("Invalid JPEG dimensions")
            return "JPEG", (width, height)
        pos += length
    raise ValueError("JPEG frame dimensions not found")


def validate(root: Path) -> dict:
    errors, warnings = [], []
    for rel in REQUIRED:
        path = inside(root, rel)
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty file: {rel}")
    try:
        manifest = json.loads((root / "refs/manifest.json").read_text(encoding="utf-8"))
        project = json.loads((root / "project.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return {"ok": False, "errors": errors + [str(exc)], "warnings": warnings}
    refs = manifest.get("references", [])
    ids = set()
    masters, reviews, preferred, scoped_support = 0, 0, 0, 0
    architecture_forms, architecture_examples = 0, 0
    for item in refs:
        try:
            rid = item["id"]
            if rid in ids:
                errors.append(f"Duplicate reference id: {rid}")
            ids.add(rid)
            path = inside(root, item["path"])
            data = path.read_bytes()
            if hashlib.sha256(data).hexdigest() != item["sha256"]:
                errors.append(f"Reference changed/hash mismatch: {rid}")
            actual_format, wh = image_dimensions(data)
            if item.get("format") and item["format"] != actual_format:
                errors.append(f"Reference format mismatch: {rid}")
            if wh != (item["width"], item["height"]):
                errors.append(f"Reference dimensions changed: {rid}")
            if item.get("reference_role") == "scoped_style_support":
                scoped_support += 1
                if item.get("group") != "style_support" or item.get("positive_reference") is not True:
                    errors.append(f"Invalid scoped style support group/positive status: {rid}")
                aspects = item.get("approved_aspects")
                if not isinstance(aspects, list) or not aspects or not all(
                        isinstance(aspect, str) and aspect.strip() for aspect in aspects):
                    errors.append(f"Missing approved aspects for scoped style support: {rid}")
                if item.get("default_generation_input") is not False:
                    errors.append(f"Scoped style support cannot be a default generation input: {rid}")
                if not isinstance(item.get("generation_input_allowed"), bool):
                    errors.append(f"Missing generation input permission for scoped style support: {rid}")
                if not isinstance(item.get("approval_id"), str) or not item["approval_id"].strip():
                    errors.append(f"Missing approval id for scoped style support: {rid}")
            elif item.get("reference_role") in ("scoped_architecture_form", "scoped_architecture_example"):
                is_form = item["reference_role"] == "scoped_architecture_form"
                architecture_forms += int(is_form)
                architecture_examples += int(not is_form)
                expected_group = "architecture_form" if is_form else "architecture_example"
                if item.get("group") != expected_group or item.get("positive_reference") is not True:
                    errors.append(f"Invalid scoped architecture group/positive status: {rid}")
                aspects = item.get("approved_aspects")
                if not isinstance(aspects, list) or not aspects or not all(
                        isinstance(aspect, str) and aspect.strip() for aspect in aspects):
                    errors.append(f"Missing approved architecture aspects: {rid}")
                if item.get("default_generation_input") is not False:
                    errors.append(f"Scoped architecture cannot be a default generation input: {rid}")
                if item.get("generation_input_allowed") is not is_form:
                    errors.append(f"Wrong scoped architecture generation input permission: {rid}")
                if item.get("geometry_approved") is not False:
                    errors.append(f"Scoped architecture cannot approve geometry: {rid}")
                if not isinstance(item.get("approval_id"), str) or not item["approval_id"].strip():
                    errors.append(f"Missing scoped architecture approval id: {rid}")
                source = inside(root, item["archived_source_path"] if is_form else item["source_output_path"])
                if hashlib.sha256(source.read_bytes()).hexdigest() != item["sha256"]:
                    errors.append(f"Scoped architecture source/copy mismatch: {rid}")
                if not is_form:
                    if item.get("overall_qa_status_at_registration") != "needs_revision":
                        errors.append(f"Architecture example registration QA must remain needs_revision: {rid}")
                    for key in ("review_path", "result_path"):
                        if not inside(root, item[key]).is_file():
                            errors.append(f"Missing architecture example {key}: {rid}")
            elif item["positive_reference"]:
                if item.get("reference_role") == "preferred_result":
                    preferred += 1
                else:
                    masters += 1
                    if item.get("reference_role", "master") != "master":
                        errors.append(f"Unknown positive reference role: {rid}")
                if item["group"] == "review_only":
                    errors.append(f"Review-only image marked positive: {rid}")
            else:
                reviews += 1
        except (KeyError, OSError, ValueError, struct.error) as exc:
            errors.append(f"Invalid reference record: {exc}")
    if masters != manifest.get("master_image_count"):
        errors.append("Master reference count mismatch")
    if preferred != manifest.get("preferred_result_count", 0):
        errors.append("Preferred result reference count mismatch")
    if reviews != manifest.get("review_only_count"):
        errors.append("Review-only count mismatch")
    if scoped_support != manifest.get("scoped_style_support_count", 0):
        errors.append("Scoped style support reference count mismatch")
    if architecture_forms != manifest.get("architecture_form_reference_count", 0):
        errors.append("Architecture form reference count mismatch")
    if architecture_examples != manifest.get("architecture_form_example_count", 0):
        errors.append("Architecture form example count mismatch")
    for field in ("default_inspection_ids", "default_generation_priority_ids",
                  "optional_scene_style_ids", "optional_world_reference_ids", "preferred_result_reference_ids",
                  "approved_user_added_reference_ids", "optional_surface_style_ids", "approved_surface_example_ids",
                  "optional_architecture_form_ids", "approved_architecture_example_ids"):
        for rid in project.get(field, []):
            if rid not in ids:
                errors.append(f"Unknown {field} reference: {rid}")
                continue
            item = next(item for item in refs if item["id"] == rid)
            if not item.get("positive_reference"):
                errors.append(f"Inactive reference in default generation path: {rid}")
            is_scoped_support = item.get("reference_role") == "scoped_style_support"
            if field in ("default_inspection_ids", "default_generation_priority_ids") and is_scoped_support:
                errors.append(f"Scoped style support cannot appear in {field}: {rid}")
            is_architecture = item.get("reference_role") in ("scoped_architecture_form", "scoped_architecture_example")
            if field in ("default_inspection_ids", "default_generation_priority_ids") and is_architecture:
                errors.append(f"Scoped architecture cannot appear in {field}: {rid}")
            if field in ("optional_scene_style_ids", "optional_world_reference_ids", "preferred_result_reference_ids",
                         "approved_user_added_reference_ids") and is_architecture:
                errors.append(f"Scoped architecture must use its own project reference list: {rid}")
            if field in ("optional_architecture_form_ids", "approved_architecture_example_ids"):
                expected_role = "scoped_architecture_form" if field == "optional_architecture_form_ids" else "scoped_architecture_example"
                if item.get("reference_role") != expected_role:
                    errors.append(f"Wrong reference role in {field}: {rid}")
            if field in ("optional_surface_style_ids", "approved_surface_example_ids"):
                if not is_scoped_support:
                    errors.append(f"Wrong reference role in {field}: {rid}")
                expected_input_permission = field == "optional_surface_style_ids"
                if item.get("generation_input_allowed") is not expected_input_permission:
                    errors.append(f"Wrong generation input permission in {field}: {rid}")
    if architecture_forms or architecture_examples:
        for field, role in (("optional_architecture_form_ids", "scoped_architecture_form"),
                            ("approved_architecture_example_ids", "scoped_architecture_example")):
            actual = project.get(field, [])
            expected = {item["id"] for item in refs if item.get("reference_role") == role}
            if len(actual) != len(set(actual)) or set(actual) != expected:
                errors.append(f"Incomplete or duplicate project architecture references: {field}")
        try:
            approval_data = json.loads((root / "state/approvals.json").read_text(encoding="utf-8"))
            approval_ids = {e.get("approval_id", e.get("id")) for e in approval_data.get("entries", [])
                            if e.get("status") == "approved"}
            for item in refs:
                if item.get("reference_role") in ("scoped_architecture_form", "scoped_architecture_example"):
                    if item.get("approval_id") not in approval_ids:
                        errors.append(f"Unknown approved architecture scope: {item['id']}")
            if not (project.get("master_version") == manifest.get("master_version") == approval_data.get("master_version_approved")):
                errors.append("Active master versions disagree")
            for key in ("reference_catalog_revision", "reference_catalog_approval_id"):
                if not (project.get(key) == manifest.get(key) == approval_data.get(key)):
                    errors.append(f"Active reference catalog metadata disagree: {key}")
            template = json.loads((root / "templates/references.json").read_text(encoding="utf-8"))
            for template_key, project_key in (("masters_version", "master_version"),
                                               ("execution_rules_version", "execution_rules_version"),
                                               ("reference_catalog_revision", "reference_catalog_revision")):
                if template.get(template_key) != project.get(project_key):
                    errors.append(f"Reference template metadata disagree: {template_key}")
        except (OSError, ValueError) as exc:
            errors.append(f"Invalid architecture approval record: {exc}")
    for field in ("read_first", "execution_rules", "qa_rules", "reference_manifest", "approvals"):
        if not inside(root, project.get(field, "")).is_file():
            errors.append(f"Missing project config target: {field}")
    size = (root / "AGENTS.md").stat().st_size if (root / "AGENTS.md").exists() else 0
    if size >= 32768:
        warnings.append("AGENTS.md is large; review instruction-chain loading limits.")
    skill = (root / ".agents/skills/game-env-art/SKILL.md")
    if skill.exists():
        s = skill.read_text(encoding="utf-8")
        if not s.startswith("---\n") or "name: game-env-art" not in s or "description:" not in s:
            errors.append("Invalid skill front matter")
    for p in root.rglob("*.json"):
        if p.is_file() and "outputs" not in p.relative_to(root).parts:
            try:
                json.loads(p.read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                errors.append(f"Invalid JSON {p.relative_to(root)}: {exc}")
    return {"ok": not errors, "root": str(root), "master_images": masters,
            "review_only_images": reviews, "preferred_result_images": preferred,
            "scoped_style_support_images": scoped_support, "agents_bytes": size,
            "architecture_form_reference_images": architecture_forms,
            "architecture_form_example_images": architecture_examples,
            "errors": errors, "warnings": warnings,
            "scope": "Files only. No visual or Codex-runtime validation."}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true", help="Print machine-readable report")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"Project directory not found: {root}", file=sys.stderr)
        return 2
    report = validate(root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("PASS" if report["ok"] else "FAIL")
        print("Scope: file integrity only; no visual QA or native-generation test.")
        for key in ("master_images", "preferred_result_images", "review_only_images",
                    "scoped_style_support_images", "architecture_form_reference_images",
                    "architecture_form_example_images", "agents_bytes"):
            if key in report:
                print(f"{key}: {report[key]}")
        for message in report["errors"]:
            print("ERROR:", message)
        for message in report["warnings"]:
            print("WARNING:", message)
    return 0 if report["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())

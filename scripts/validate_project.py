#!/usr/bin/env python3
"""Read-only package validation. No network, installations, or image-model calls.

Python 3.9+. Checks required files, reference integrity, IDs, and PNG dimensions.
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
    masters, reviews, preferred = 0, 0, 0
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
            if data[:8] != b"\x89PNG\r\n\x1a\n":
                errors.append(f"Not a PNG file: {rid}")
            elif len(data) < 24:
                errors.append(f"Truncated PNG: {rid}")
            else:
                wh = struct.unpack(">II", data[16:24])
                if wh != (item["width"], item["height"]):
                    errors.append(f"Reference dimensions changed: {rid}")
            if item["positive_reference"]:
                if item.get("reference_role") == "preferred_result":
                    preferred += 1
                else:
                    masters += 1
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
    for field in ("default_inspection_ids", "default_generation_priority_ids",
                  "optional_scene_style_ids", "optional_world_reference_ids", "preferred_result_reference_ids"):
        for rid in project.get(field, []):
            if rid not in ids:
                errors.append(f"Unknown {field} reference: {rid}")
            elif not next(item for item in refs if item["id"] == rid)["positive_reference"]:
                errors.append(f"Inactive reference in default generation path: {rid}")
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
            "review_only_images": reviews, "preferred_result_images": preferred, "agents_bytes": size,
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
        for key in ("master_images", "preferred_result_images", "review_only_images", "agents_bytes"):
            if key in report:
                print(f"{key}: {report[key]}")
        for message in report["errors"]:
            print("ERROR:", message)
        for message in report["warnings"]:
            print("WARNING:", message)
    return 0 if report["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Copy explicitly selected deliverables; never infer finals from filenames or QA."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'outputs/final_manifest.json'
DEST = ROOT / 'outputs/final'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def source_path(value):
    p = (ROOT / value).resolve()
    p.relative_to((ROOT / 'outputs').resolve())
    if p.is_relative_to(DEST.resolve()) or p.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.webp'):
        raise ValueError('Source must be an original run image: ' + value)
    if not p.is_file():
        raise FileNotFoundError(p)
    return p

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', action='store_true', help='Read-only hash and inventory verification')
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text(encoding='utf-8-sig'))
    entries = data['images']
    expected = set()
    source_hashes = set()
    prepared = []
    for entry in entries:
        src = source_path(entry['source'])
        name = entry['filename']
        if Path(name).name != name or '/' in name or '\\' in name or name in expected:
            raise ValueError('Invalid/duplicate destination: ' + name)
        expected.add(name)
        sha = digest(src)
        if sha in source_hashes:
            raise ValueError('Duplicate image contents: ' + entry['source'])
        source_hashes.add(sha)
        dst = DEST / name
        if entry.get('sha256') and entry['sha256'] != sha:
            raise ValueError('Original image changed: ' + entry['source'])
        if dst.exists() and digest(dst) != sha:
            raise ValueError('Destination differs; preserve/reconcile explicitly: ' + name)
        if args.verify and (not dst.is_file() or entry.get('sha256') != sha):
            raise ValueError('Missing copy/hash record: ' + name)
        prepared.append((entry, src, dst, sha))
    extras = {p.name for p in DEST.iterdir()} - expected if DEST.exists() else set()
    if extras:
        raise ValueError('Unlisted files in final folder: ' + repr(sorted(extras)))
    if not args.verify:
        DEST.mkdir(parents=True, exist_ok=True)
        for entry, src, dst, sha in prepared:
            if not dst.exists():
                shutil.copy2(src, dst)
            if digest(dst) != sha:
                raise ValueError('Copy hash mismatch: ' + dst.name)
            entry['sha256'] = sha
            entry['bytes'] = src.stat().st_size
        MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        lines = ['# 최종 전달 이미지 목록', '', '최종 전달본 모음입니다. 검수 통과/마스터 승인 목록이 아닙니다. 기존 원본과 중간 작업은 보존합니다.', '', '| 이미지 | 원본 | 기록된 검수 상태 | 선택 근거 |', '|---|---|---|---|']
        for e in entries:
            src = e['source'].removeprefix('outputs/')
            lines.append(f"| [{e['filename']}](final/{e['filename']}) | [작업 원본]({src}) | {e['qa_status']} | {e['selection_reason']} |")
        (ROOT / 'outputs/FINAL_INDEX.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(('VERIFIED' if args.verify else 'COLLECTED') + f': {len(entries)} final images; byte-identical copies; no duplicate hashes')

if __name__ == '__main__':
    main()

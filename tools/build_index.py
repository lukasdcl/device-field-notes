#!/usr/bin/env python3
"""Rebuild the power table in README.md from the front matter of devices/**/*.md."""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START, END = "<!-- POWER-TABLE:START -->", "<!-- POWER-TABLE:END -->"


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    return yaml.safe_load(m.group(1)) or {}


def fmt(w):
    return "" if w is None else f"{w:g} W"


def build_rows():
    rows, errors = [], []
    for path in sorted((ROOT / "devices").rglob("*.md")):
        if path.name.startswith("_"):
            continue
        rel = path.relative_to(ROOT).as_posix()
        try:
            meta = front_matter(path)
        except yaml.YAMLError as e:
            errors.append(f"{rel}: invalid YAML ({e})")
            continue
        if meta is None:
            errors.append(f"{rel}: no front matter")
            continue
        missing = [k for k in ("brand", "model", "category") if not meta.get(k)]
        if missing:
            errors.append(f"{rel}: missing {', '.join(missing)}")
            continue
        name = f"[{meta['brand']} {meta['model']}]({rel})"
        for p in meta.get("power") or []:
            rows.append((
                meta["brand"].lower(), meta["model"].lower(),
                f"| {name} | {meta['category']} | {p.get('state', '')} | "
                f"{fmt(p.get('typical_w'))} | {fmt(p.get('peak_w'))} |",
            ))
    return [r[2] for r in sorted(rows)], errors


def main():
    rows, errors = build_rows()
    for e in errors:
        print(f"warning: {e}", file=sys.stderr)
    table = "\n".join([
        "| Device | Category | State | Typical | Peak |",
        "|---|---|---|---|---|",
        *rows,
    ])
    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    new = pattern.sub(f"{START}\n{table}\n{END}", readme)
    if new != readme:
        README.write_text(new, encoding="utf-8")
        print("README.md updated")
    else:
        print("README.md already up to date")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

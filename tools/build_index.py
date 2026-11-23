#!/usr/bin/env python3
"""Rebuild the power table in README.md from the front matter of devices/**/*.md."""
import html
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
    if w is None:
        return ""
    return f"{w:g} W" if isinstance(w, (int, float)) else f"{w} W"


def build_devices():
    """Return a list of devices, each with its rows of power readings in file order."""
    devices, errors = [], []
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
        rows = []
        for p in meta.get("power") or []:
            state = p.get("state", "")
            if isinstance(state, bool):  # YAML reads bare on/off as true/false
                state = "on" if state else "off"
            rows.append((str(state), fmt(p.get("typical_w")), fmt(p.get("peak_w"))))
        if rows:
            devices.append({
                "sort": (str(meta["brand"]).lower(), str(meta["model"]).lower()),
                "name": f"{meta['brand']} {meta['model']}",
                "link": rel,
                "category": str(meta["category"]),
                "rows": rows,
            })
    devices.sort(key=lambda d: d["sort"])
    return devices, errors


def render_table(devices):
    """HTML table, so each device's name and category span all of its rows."""
    e = html.escape
    out = [
        "<table>",
        "<tr><th>Device</th><th>Category</th><th>State</th><th>Typical</th><th>Peak</th></tr>",
    ]
    for d in devices:
        span = len(d["rows"])
        rs = f' rowspan="{span}"' if span > 1 else ""
        for i, (state, typical, peak) in enumerate(d["rows"]):
            cells = []
            if i == 0:
                cells.append(f'<td{rs}><a href="{e(d["link"])}">{e(d["name"])}</a></td>')
                cells.append(f"<td{rs}>{e(d['category'])}</td>")
            cells += [f"<td>{e(state)}</td>", f"<td>{e(typical)}</td>", f"<td>{e(peak)}</td>"]
            out.append("<tr>" + "".join(cells) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def main():
    devices, errors = build_devices()
    for err in errors:
        print(f"warning: {err}", file=sys.stderr)
    table = render_table(devices)
    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    new = pattern.sub(lambda m: f"{START}\n{table}\n{END}", readme)
    if new != readme:
        README.write_text(new, encoding="utf-8")
        print("README.md updated")
    else:
        print("README.md already up to date")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

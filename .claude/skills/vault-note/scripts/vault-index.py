#!/usr/bin/env python3
"""Print what's already in the vault: the tag vocabulary, and one line per note.

Enough context to pick tags that already exist and spot notes worth linking,
without reading every file.
"""

import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[4]  # vault root


def gist(body):
    """The note's first sentence — Claude's summary, or the user's own text."""
    m = re.search(r"(?ms)^# .*?\n(.*?)^## ", body)
    text = m.group(1).strip() if m else ""
    if text.startswith("Claude summary:"):
        text = text.split("\n", 1)[-1].strip()
    if not text:
        m = re.search(r"(?ms)^## Why do I bring this up\?\n(.*)\Z", body)
        text = m.group(1).strip() if m else ""
        text = re.sub(r"(?m)^### .*\n?", "", text).strip()  # drop author headings
        text = re.sub(r"^\*\*[\d-]+\*\* — ", "", text)         # drop the date stamp
    text = re.sub(r"^>\s*", "", text, flags=re.M).replace("\n", " ")
    return (text[:110].rsplit(" ", 1)[0] + "…") if len(text) > 110 else text


def main():
    notes, tags = [], set()
    synthesis = [f.stem for f in sorted(VAULT.glob("*.md")) if f.name != "README.md"]
    for f in sorted((VAULT / "reading").glob("*.md")):
        body = f.read_text(encoding="utf-8")
        fm = body.split("---", 2)[1] if body.startswith("---") else ""
        tb = re.search(r"(?m)^tags:((?:\n  - .*)+)", fm)
        if tb:
            tags.update(re.findall(r"- (.+)", tb[1]))
        kind = (re.search(r"^kind: *(\w+)", fm, re.M) or [None, "?"])[1]
        hb = re.search(r"(?m)^harness:((?:\n  - .*)+)", fm)
        harness = ",".join(re.findall(r"- (.+)", hb[1])) if hb else ""
        notes.append((f.stem, kind, harness, gist(body)))

    if not notes and not synthesis:
        print("vault is empty")
        return
    print("TAGS IN USE:", ", ".join(sorted(tags)) or "(none)")
    if synthesis:
        print("\nYOUR NOTES (vault root):")
        for name in synthesis:
            print(f"  {name}")

    seen = {}
    for slug, kind, harness, _ in notes:
        for h in filter(None, harness.split(",")):
            seen.setdefault(h, []).append(kind)
    if seen:
        print("\nBY HARNESS:")
        for h, kinds in sorted(seen.items()):
            print(f"  {h:<14} {', '.join(sorted(kinds))}")

    print(f"\n{len(notes)} READING NOTES:")
    width = max(len(n[0]) for n in notes)
    for slug, kind, harness, text in notes:
        label = f"[{kind}]" + (f"[{harness}]" if harness else "")
        print(f"  {slug:<{width}}  {label:<22} {text}")


if __name__ == "__main__":
    main()

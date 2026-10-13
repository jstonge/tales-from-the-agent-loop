"""Shared reading of the vault, so tools don't drift in how they parse notes."""

import re
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
READING = VAULT / "reading"


def frontmatter(body):
    """key -> str | list. Lists stay lists so tags and harness don't collide."""
    if not body.startswith("---"):
        return {}
    fm, out, key = body.split("---", 2)[1], {}, None
    for line in fm.strip("\n").split("\n"):
        if m := re.match(r"^(\w+):(.*)$", line):
            key, val = m[1], m[2].strip()
            out[key] = val or []
        elif (m := re.match(r"^  - (.*)$", line)) and key:
            if isinstance(out.get(key), str):
                out[key] = []
            out.setdefault(key, []).append(m[1])
    return out


def listed(fields, key):
    v = fields.get(key) or []
    return [v] if isinstance(v, str) and v else list(v)


def linked(fields, key):
    """A list field whose values are wikilinks, as plain names."""
    out = []
    for raw in listed(fields, key):
        out.append(raw.strip('"').strip("[]").split("|")[0].split("/")[-1])
    return out


def gist(body, limit=110):
    """The note's first sentence — Claude's summary, else the author's own text."""
    m = re.search(r"(?ms)^# .*?\n(.*?)^## ", body)
    text = m[1].strip() if m else ""
    if text.startswith("Claude summary:"):
        text = text.split("\n", 1)[-1].strip()
    if not text:
        m = re.search(r"(?ms)^## Why do I bring this up\?\n(.*)\Z", body)
        text = m[1].strip() if m else ""
        text = re.sub(r"(?m)^### .*\n?", "", text).strip()
        text = re.sub(r"^\*\*[\d-]+\*\* — ", "", text)
    text = re.sub(r"^>\s*", "", text, flags=re.M).replace("\n", " ").strip()
    return (text[:limit].rsplit(" ", 1)[0] + "…") if len(text) > limit else text


def reading_notes():
    """[(slug, fields, gist)] for every note in reading/."""
    out = []
    for f in sorted(READING.glob("*.md")):
        body = f.read_text(encoding="utf-8")
        out.append((f.stem, frontmatter(body), gist(body)))
    return out


def by_author(notes=None):
    """author name -> [(slug, fields, gist)], most-covered first."""
    groups = {}
    for slug, fields, g in notes if notes is not None else reading_notes():
        for b in linked(fields, "by"):
            groups.setdefault(b, []).append((slug, fields, g))
    return dict(sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])))


def by_harness(notes=None):
    """harness name -> [(slug, fields, gist)], sorted by how much we know."""
    groups = {}
    for slug, fields, g in notes if notes is not None else reading_notes():
        for h in listed(fields, "harness"):
            groups.setdefault(h, []).append((slug, fields, g))
    return dict(sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])))


def identity():
    """Who's writing. The git name is what a collaborator sees in the history
    anyway; whoami is the fallback when git isn't configured."""
    import subprocess
    for cmd in (["git", "config", "user.name"], ["whoami"]):
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    return "unknown"

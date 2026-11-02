#!/usr/bin/env python3
"""Build registry/papers.jsonl from the repository's own markdown records.

Honesty rules: fields are populated ONLY from text already in the repo
(sources-and-resources.md tables, topic-doc entries, README direction
sections). Anything not recorded is emitted as "UNRECORDED" or null --
never inferred from outside knowledge. arXiv IDs encode submission
year-month; that is recorded as submitted_ym with granularity noted.
"""
import re, json, glob, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
ABS = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")

files = sorted(glob.glob(str(ROOT / "**" / "*.md"), recursive=True))
texts = {f: pathlib.Path(f).read_text(errors="ignore") for f in files}
rel = {f: str(pathlib.Path(f).relative_to(ROOT)) for f in files}

ids = set()
for t in texts.values():
    ids |= set(ABS.findall(t))
ids = sorted(ids)

# --- titles: several in-repo patterns ---
title_votes = collections.defaultdict(collections.Counter)
pats = [
    re.compile(r"\[(\d{4}\.\d{4,5})\]\([^)]*\)\s*\|\s*([^|]{5,200}?)\s*\|"),
    re.compile(r"\*\*([^*]{5,200}?)\*\*\s*\nPrimary paper: https://arxiv\.org/abs/(\d{4}\.\d{4,5})"),
    re.compile(r"-\s*([^:\n]{5,200}?):\s*https://arxiv\.org/abs/(\d{4}\.\d{4,5})"),
    re.compile(r"-\s*([^—\n]{5,200}?)\s*—\s*https://arxiv\.org/abs/(\d{4}\.\d{4,5})"),
    re.compile(r"\|\s*([^|]{5,200}?)\s*\|\s*https://arxiv\.org/abs/(\d{4}\.\d{4,5})\s*\|"),
]
for f, t in texts.items():
    for p in pats:
        for m in p.finditer(t):
            if len(m.groups()) == 2:
                a, b = m.group(1), m.group(2)
                if re.fullmatch(r"\d{4}\.\d{4,5}", a):
                    aid, title = a, b
                elif re.fullmatch(r"\d{4}\.\d{4,5}", b):
                    aid, title = b, a
                else:
                    continue
                title = title.strip().strip("*").strip()
                if title and "http" not in title and title.lower() not in ("paper", "code"):
                    title_votes[aid][title] += 1

# --- research directions R01-R36 from 01-research/README.md sections ---
readme = texts[str(ROOT / "01-research" / "README.md")]
dir_map = collections.defaultdict(set)
sections = re.split(r"^### (R\d{2}) — ", readme, flags=re.M)
for i in range(1, len(sections), 2):
    code, body = sections[i], sections[i + 1]
    for aid in set(ABS.findall(body)):
        dir_map[aid].add(code)

TOPIC_DOCS = [rel[f] for f in files if rel[f].startswith("01-research/")
              and pathlib.Path(f).name not in ("README.md", "sources-and-resources.md")]

FULL_MARKERS = ("全文精读", "Full text read", "full text read", "全文审计")
SEL_MARKERS = ("正文选读", "选读", "selected-section", "Selected-section")
ABS_MARKERS = ("摘要/书目", "摘要级", "ABSTRACT", "abstract-level")

rows = []
for aid in ids:
    mentions = collections.Counter()
    tag_v, tag_l = collections.Counter(), collections.Counter()
    depth = "UNRECORDED"
    verdict = None
    for f, t in texts.items():
        r = rel[f]
        if aid not in t:
            continue
        for line in t.splitlines():
            if aid in line:
                mentions[r] += 1
                for v in re.findall(r"`?(V[0-3])`?", line):
                    tag_v[v] += 1
                for l in re.findall(r"`?(L[0-4])`?", line):
                    tag_l[l] += 1
                if any(m in line for m in FULL_MARKERS):
                    depth = "FULL_TEXT_AUDITED"
                elif depth != "FULL_TEXT_AUDITED" and any(m in line for m in SEL_MARKERS):
                    depth = "SELECTED_SECTIONS"
                elif depth == "UNRECORDED" and any(m in line for m in ABS_MARKERS):
                    depth = "ABSTRACT_AND_BIBLIO"
                # verdict candidate: longest prose cell of a table row mentioning the id
                if line.strip().startswith("|") and verdict is None:
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    prose = [c for c in cells if len(c) >= 40 and "http" not in c and aid not in c and "](" not in c and not c.startswith("[")]
                    if prose:
                        verdict = max(prose, key=len)[:400]
    topic_mentions = {d: mentions[d] for d in TOPIC_DOCS if mentions[d]}
    if topic_mentions:
        primary = max(topic_mentions.items(), key=lambda kv: (kv[1], kv[0]))[0]
    elif mentions.get("01-research/sources-and-resources.md"):
        primary = "01-research/sources-and-resources.md"
    elif mentions.get("01-research/README.md"):
        primary = "01-research/README.md"
    else:
        primary = mentions.most_common(1)[0][0] if mentions else None
    yy, mm = aid[:2], aid[2:4]
    rows.append({
        "arxiv_id": aid,
        "title": (title_votes[aid].most_common(1)[0][0] if title_votes[aid] else None),
        "submitted_date": None,
        "submitted_ym": f"20{yy}-{mm}",
        "submitted_ym_basis": "derived from arXiv ID prefix (submission year-month); exact day not recorded in repo",
        "primary_doc": primary,
        "research_dirs": sorted(dir_map.get(aid, [])),
        "observation_tag": (tag_v.most_common(1)[0][0] if tag_v else "UNRECORDED"),
        "supervision_tag": (tag_l.most_common(1)[0][0] if tag_l else "UNRECORDED"),
        "reading_depth": depth,
        "one_line_verdict": verdict,
        "cannot_prove": None,
    })

out = ROOT / "registry" / "papers.jsonl"
out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
cov = {
    "total": len(rows),
    "with_title": sum(1 for r in rows if r["title"]),
    "with_dirs": sum(1 for r in rows if r["research_dirs"]),
    "with_obs_tag": sum(1 for r in rows if r["observation_tag"] != "UNRECORDED"),
    "with_sup_tag": sum(1 for r in rows if r["supervision_tag"] != "UNRECORDED"),
    "full_text": sum(1 for r in rows if r["reading_depth"] == "FULL_TEXT_AUDITED"),
    "selected": sum(1 for r in rows if r["reading_depth"] == "SELECTED_SECTIONS"),
    "abstract": sum(1 for r in rows if r["reading_depth"] == "ABSTRACT_AND_BIBLIO"),
    "depth_unrecorded": sum(1 for r in rows if r["reading_depth"] == "UNRECORDED"),
    "with_verdict": sum(1 for r in rows if r["one_line_verdict"]),
}
print(json.dumps(cov, indent=1))

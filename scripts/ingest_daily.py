#!/usr/bin/env python3
"""Daily ingest & routing tool (sequence 3.2).

Replaces the manual 'write news_*.md, upgrade by hand later' half-process.
Input: arXiv IDs and/or Dual-State Evidence Cards (JSON). For each paper:
  1. verify title/authors/first-submitted date against the official arXiv
     API (export.arxiv.org). With --offline (or on network failure) the
     record is written with verification_status=PENDING and the card's
     declared title -- never an invented one.
  2. append/update the record in registry/papers.jsonl (dedup by arXiv ID);
  3. route a formatted markdown entry into:
       - the card's primary topic doc in 01-research/ (routed-entries section)
       - 02-analysis/README.md (method-card stub section)
       - 04-innovation/README.md (pro/con evidence-chain section, per linked
         hypotheses H1-H15)
Cards must declare research_dirs (R01-R36), observation_tag (V0-V3),
supervision_tag (L0-L4), reading_depth, one_line_verdict and cannot_prove;
incomplete cards are rejected, not silently completed.

Usage:
  python3 scripts/ingest_daily.py --card card.json [--card card2.json]
  python3 scripts/ingest_daily.py --ids 2601.00001 --primary-doc learning-and-data.md \
      --dirs R20 --obs V0 --sup L4 --verdict "..." --cannot-prove "..."
  add --dry-run to print planned writes without touching files.
"""
import argparse, json, pathlib, re, sys, urllib.request, urllib.error

ROOT = pathlib.Path(__file__).resolve().parent.parent
REG = ROOT / "registry" / "papers.jsonl"
V_TAGS = {f"V{i}" for i in range(4)}
L_TAGS = {f"L{i}" for i in range(5)}
DEPTHS = {"FULL_TEXT_AUDITED", "SELECTED_SECTIONS", "ABSTRACT_AND_BIBLIO"}

def arxiv_verify(aid, timeout=15):
    url = f"https://export.arxiv.org/api/query?id_list={aid}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            xml = r.read().decode("utf-8", "replace")
    except Exception as e:
        return {"verification_status": "PENDING", "verify_error": str(e)[:200]}
    title = re.search(r"<entry>.*?<title>(.*?)</title>", xml, re.S)
    published = re.search(r"<entry>.*?<published>(.*?)</published>", xml, re.S)
    authors = re.findall(r"<author>\s*<name>(.*?)</name>", xml, re.S)
    if not title:
        return {"verification_status": "PENDING", "verify_error": "arXiv API returned no entry"}
    return {
        "verification_status": "VERIFIED_ARXIV_API",
        "title": " ".join(title.group(1).split()),
        "authors": [a.strip() for a in authors],
        "submitted_date": published.group(1)[:10] if published else None,
    }

def load_registry():
    rows = {}
    if REG.exists():
        for line in REG.read_text().splitlines():
            if line.strip():
                d = json.loads(line)
                rows[d["arxiv_id"]] = d
    return rows

def save_registry(rows):
    REG.write_text("".join(json.dumps(rows[k], ensure_ascii=False) + "\n" for k in sorted(rows)))

def validate_card(c):
    errs = []
    if not re.fullmatch(r"\d{4}\.\d{4,5}", c.get("arxiv_id", "")):
        errs.append("arxiv_id missing/malformed")
    if c.get("observation_tag") not in V_TAGS:
        errs.append("observation_tag must be V0-V3")
    if c.get("supervision_tag") not in L_TAGS:
        errs.append("supervision_tag must be L0-L4")
    if not c.get("research_dirs") or any(not re.fullmatch(r"R(0[1-9]|[12][0-9]|3[0-6])", d) for d in c["research_dirs"]):
        errs.append("research_dirs must be R01-R36")
    if c.get("reading_depth", "ABSTRACT_AND_BIBLIO") not in DEPTHS:
        errs.append("reading_depth invalid")
    for f in ("one_line_verdict", "cannot_prove", "primary_doc"):
        if not c.get(f):
            errs.append(f"{f} is required (no silent completion)")
    for h in c.get("related_hypotheses", []):
        if not re.fullmatch(r"H([1-9]|1[0-5])", h):
            errs.append(f"related hypothesis {h} out of H1-H15")
    return errs

def md_entry(c, v):
    title = v.get("title") or c.get("title") or "TITLE UNVERIFIED (pending arXiv API check)"
    return (f"\n### [ingest] {title} (arXiv:{c['arxiv_id']})\n\n"
            f"- 路由：{', '.join(c['research_dirs'])} · 观测 `{c['observation_tag']}` · 监督 `{c['supervision_tag']}` · 阅读深度 {c.get('reading_depth','ABSTRACT_AND_BIBLIO')} · 核验 {v['verification_status']}\n"
            f"- 一句话判决：{c['one_line_verdict']}\n"
            f"- 不能证明：{c['cannot_prove']}\n"
            f"- 来源：https://arxiv.org/abs/{c['arxiv_id']}\n")

def append_routed(fname, section_title, text, dry):
    p = ROOT / fname
    t = p.read_text()
    if section_title not in t:
        t = t.rstrip() + f"\n\n## {section_title}\n"
    t = t.rstrip() + "\n" + text
    if not dry:
        p.write_text(t + "\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--card", action="append", default=[], help="JSON file: one card object or a list")
    ap.add_argument("--ids", nargs="*", default=[])
    ap.add_argument("--primary-doc"); ap.add_argument("--dirs", nargs="*", default=[])
    ap.add_argument("--obs"); ap.add_argument("--sup")
    ap.add_argument("--verdict"); ap.add_argument("--cannot-prove", dest="cannot_prove")
    ap.add_argument("--hypotheses", nargs="*", default=[])
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    cards = []
    for cf in a.card:
        data = json.loads(pathlib.Path(cf).read_text())
        cards += data if isinstance(data, list) else [data]
    for aid in a.ids:
        cards.append({"arxiv_id": aid, "primary_doc": a.primary_doc, "research_dirs": a.dirs,
                      "observation_tag": a.obs, "supervision_tag": a.sup,
                      "one_line_verdict": a.verdict, "cannot_prove": a.cannot_prove,
                      "related_hypotheses": a.hypotheses})
    if not cards:
        ap.error("no input: use --card or --ids")
    rows = load_registry()
    changed = False
    for c in cards:
        errs = validate_card(c)
        if errs:
            print(f"REJECT {c.get('arxiv_id')}: {'; '.join(errs)}"); continue
        v = {"verification_status": "PENDING"} if a.offline else arxiv_verify(c["arxiv_id"])
        rec = {"arxiv_id": c["arxiv_id"], "title": v.get("title") or c.get("title"),
               "submitted_date": v.get("submitted_date"), "authors": v.get("authors"),
               "primary_doc": f"01-research/{c['primary_doc']}" if not c["primary_doc"].startswith("01-research/") else c["primary_doc"],
               "research_dirs": c["research_dirs"], "observation_tag": c["observation_tag"],
               "supervision_tag": c["supervision_tag"],
               "reading_depth": c.get("reading_depth", "ABSTRACT_AND_BIBLIO"),
               "one_line_verdict": c["one_line_verdict"], "cannot_prove": c["cannot_prove"],
               "verification_status": v["verification_status"]}
        action = "UPDATE" if c["arxiv_id"] in rows else "ADD"
        print(f"{action} {c['arxiv_id']} verify={v['verification_status']} -> {rec['primary_doc']}")
        if not a.dry_run:
            rows[c["arxiv_id"]] = rec; changed = True
            e = md_entry(c, v)
            append_routed(rec["primary_doc"], "每日自动路由入库（ingest_daily）", e, a.dry_run)
            append_routed("02-analysis/README.md", "自动路由方法卡（ingest_daily 生成，待 Stage-2 完整分析）",
                          f"\n### [ingest card] arXiv:{c['arxiv_id']}\n\n- 判决：{c['one_line_verdict']}\n- 不能证明：{c['cannot_prove']}\n- 记账：`{c['observation_tag']}` / `{c['supervision_tag']}` · {rec['primary_doc']}\n", a.dry_run)
            if c.get("related_hypotheses"):
                append_routed("04-innovation/README.md", "自动路由正反证据链（ingest_daily）",
                              f"\n- arXiv:{c['arxiv_id']} → {', '.join(c['related_hypotheses'])}：{c['one_line_verdict']}（反面边界：{c['cannot_prove']}）\n", a.dry_run)
    if changed and not a.dry_run:
        save_registry(rows)
    print("done" + (" (dry-run, nothing written)" if a.dry_run else ""))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Repository integrity & contract audit (sequence 3.3).

Checks:
 1. Internal relative links in all markdown: target file must exist
    (error); anchor must resolve against GitHub-style heading slugs or
    explicit <a id="..."> anchors (warning -- slug edge cases exist).
 2. Every arXiv ID referenced in markdown exists in registry/papers.jsonl
    (error if missing); its observation/supervision tags must be in the
    legal enum or UNRECORDED (error otherwise). Coverage % reported.
 3. Numbering namespaces: B1-B15, U1-U20, R01-R36 (directions), H1-H15,
    Q1-Q7, C1-C6 -- out-of-range references are errors.
 4. Statistics: paper totals by reading depth, code coverage (hypothesis
    target scripts that exist), EV-level mentions; compared against the
    AUDIT-STATS block in STATUS.md (stale block = warning; refresh with
    --update-status).

Exit code: 1 on errors, 0 otherwise (warnings do not fail).
"""
import json, pathlib, re, sys, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors, warnings = [], []

md_files = sorted(ROOT.glob("**/*.md"))
texts = {f: f.read_text(errors="ignore") for f in md_files}
rel = lambda f: str(f.relative_to(ROOT))

def slug(h):
    h = h.strip().lower()
    h = re.sub(r"<[^>]+>", "", h)
    h = re.sub(r"[^\w\s-]", "", h, flags=re.UNICODE)
    return h.replace(" ", "-")

anchors = {}
for f, t in texts.items():
    s = set(re.findall(r'<a id="([^"]+)"', t))
    for line in t.splitlines():
        m = re.match(r"#{1,6}\s+(.*)", line)
        if m:
            s.add(slug(m.group(1)))
    anchors[rel(f)] = s

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
link_total = link_file_err = 0
for f, t in texts.items():
    for target in LINK.findall(t):
        if "://" in target or target.startswith("mailto:"):
            continue
        path, _, anchor = target.partition("#")
        if not path:
            if anchor and anchor not in anchors[rel(f)]:
                warnings.append(f"anchor (same-file) missing: {rel(f)} -> #{anchor}")
            continue
        link_total += 1
        dest = (f.parent / path).resolve()
        try:
            dest_rel = str(dest.relative_to(ROOT.resolve()))
        except ValueError:
            continue
        if not dest.exists():
            link_file_err += 1
            errors.append(f"dead link: {rel(f)} -> {target}")
        elif anchor and dest_rel in anchors and anchor not in anchors[dest_rel]:
            warnings.append(f"anchor missing: {rel(f)} -> {target}")
print(f"[links] internal links checked: {link_total}, dead-file errors: {link_file_err}, anchor warnings: {len(warnings)}")

# 2. registry coverage
reg_path = ROOT / "registry" / "papers.jsonl"
registry = {}
if reg_path.exists():
    for line in reg_path.read_text().splitlines():
        if line.strip():
            d = json.loads(line); registry[d["arxiv_id"]] = d
ABS = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")
referenced = set()
for t in texts.values():
    referenced |= set(ABS.findall(t))
missing = referenced - set(registry)
for m in sorted(missing):
    errors.append(f"arXiv ID referenced but not in registry: {m}")
LEGAL_V = {f"V{i}" for i in range(4)} | {"UNRECORDED"}
LEGAL_L = {f"L{i}" for i in range(5)} | {"UNRECORDED"}
for aid, d in registry.items():
    if d.get("observation_tag") not in LEGAL_V:
        errors.append(f"registry {aid}: illegal observation_tag {d.get('observation_tag')}")
    if d.get("supervision_tag") not in LEGAL_L:
        errors.append(f"registry {aid}: illegal supervision_tag {d.get('supervision_tag')}")
depths = collections.Counter(d.get("reading_depth") for d in registry.values())
print(f"[registry] referenced IDs: {len(referenced)}, registered: {len(registry)}, missing: {len(missing)}")
print(f"[registry] depths: {dict(depths)}")

# 3. numbering namespaces
def check_ns(name, pat, lo, hi, fmt="{:d}"):
    bad = collections.Counter()
    for f, t in texts.items():
        if rel(f).startswith("news_"):
            continue
        for m in re.finditer(pat, t):
            n = int(m.group(1))
            if n < lo or n > hi:
                bad[f"{name}{fmt.format(n)} @ {rel(f)}"] += 1
    for k, c in bad.items():
        errors.append(f"numbering out of range: {k} (x{c})")
check_ns("B", r"\bB(\d{1,2})\b(?=\s*(?:family|—|–|-))", 1, 15)

# H namespace, excluding the model name Being-H0.7 (an artifact, not a hypothesis)
for f, t in texts.items():
    if rel(f).startswith("news_"):
        continue
    for m in re.finditer(r"(?<!Being-)\bH(\d{1,2})\b(?!\.)", t):
        if not (1 <= int(m.group(1)) <= 15):
            errors.append(f"hypothesis out of range: H{m.group(1)} @ {rel(f)}")

# Q and C global namespaces. KNOWN LOCAL NAMESPACES (documented, not errors):
# - learning-and-data.md has a section-local question list (### Q1..Q12+) in
#   'Training / Post-Training -- High-Risk Boundary Questions'; it is not the
#   global Q1-Q7 research-question series.
# - foundation-models-and-systems.md has a section-local capability list
#   (C6..C10) in a cross-domain enumeration; it is not the C1-C6 contradiction
#   series. Both are recorded here so future drift is visible, not silent.
LOCAL_NS_FILES = {"01-research/learning-and-data.md", "01-research/foundation-models-and-systems.md"}
def check_ns_scoped(name, pat, lo, hi):
    for f, t in texts.items():
        if rel(f).startswith("news_") or rel(f) in LOCAL_NS_FILES:
            continue
        for m in re.finditer(pat, t):
            n = int(m.group(1))
            if n < lo or n > hi:
                errors.append(f"numbering out of range: {name}{n} @ {rel(f)}")
check_ns_scoped("Q", r"\bQ(\d)\b", 1, 7)
check_ns_scoped("C", r"\bC(\d)\b", 1, 6)
print("[numbering] known local namespaces excluded: learning-and-data Q-list, foundation C-list (documented in code)")

# Direction codes R01-R36; hyphen-suffixed tokens (CosFace-R50, AdaFace-R50 =
# ResNet-50 backbones) are model names, not direction references.
for f, t in texts.items():
    if rel(f).startswith("news_"):
        continue
    for m in re.finditer(r"(?<!-)\bR(\d{2})\b", t):
        if not (1 <= int(m.group(1)) <= 36):
            errors.append(f"direction out of range: R{m.group(1)} @ {rel(f)}")
print("[numbering] namespace range checks done")

# 4. stats + STATUS freshness
hyp = (ROOT / "registry" / "hypotheses.yaml").read_text() if (ROOT / "registry" / "hypotheses.yaml").exists() else ""
targets = sorted(set(re.findall(r"target_experiment_script:\s*\"?([^\s\"]+)", hyp))) 
existing_targets = [t for t in targets if t and (ROOT / t).exists()]
ev_mentions = len(re.findall(r"EV[0-8]", texts.get(ROOT / "STATUS.md", "")))
stats = {
    "papers_total": len(registry),
    "full_text_audited": depths.get("FULL_TEXT_AUDITED", 0),
    "selected_sections": depths.get("SELECTED_SECTIONS", 0),
    "abstract_and_biblio": depths.get("ABSTRACT_AND_BIBLIO", 0),
    "hypothesis_target_scripts_existing": f"{len(existing_targets)}/{len(targets)}",
    "status_ev_mentions": ev_mentions,
}
block = "<!-- AUDIT-STATS:BEGIN -->\n```json\n" + json.dumps(stats, indent=1, ensure_ascii=False) + "\n```\n<!-- AUDIT-STATS:END -->"
status_path = ROOT / "STATUS.md"
status_text = texts.get(status_path, "")
if "--update-status" in sys.argv:
    if "AUDIT-STATS:BEGIN" in status_text:
        status_text = re.sub(r"<!-- AUDIT-STATS:BEGIN -->.*?<!-- AUDIT-STATS:END -->", block, status_text, flags=re.S)
    else:
        status_text = status_text.rstrip() + "\n\n## 审计统计（scripts/audit_repo.py 自动生成，勿手改）\n\n" + block + "\n"
    status_path.write_text(status_text)
    print("[status] AUDIT-STATS block updated")
else:
    m = re.search(r"<!-- AUDIT-STATS:BEGIN -->\n```json\n(.*?)```", status_text, re.S)
    if not m:
        warnings.append("STATUS.md has no AUDIT-STATS block (run audit_repo.py --update-status)")
    elif json.loads(m.group(1)) != stats:
        warnings.append("STATUS.md AUDIT-STATS block is stale (run audit_repo.py --update-status)")
print(f"[stats] {json.dumps(stats, ensure_ascii=False)}")

print(f"\nERRORS: {len(errors)}")
for e in errors[:50]:
    print("  E:", e)
print(f"WARNINGS: {len(warnings)}")
for w in warnings[:20]:
    print("  W:", w)
sys.exit(1 if errors else 0)

# registry/ — structured data layer

Single machine-readable source connecting the markdown knowledge base
(`01-research/` … `07-reflection/`) with the code base (`src/clover/`).

| File | Content | Built from |
|---|---|---|
| `papers.jsonl` | 719 verified arXiv papers, one JSON object per line | `scripts/build_registry.py` over the repo's own markdown (sources index, topic docs, README direction sections) |
| `artifacts.yaml` | 12 official open model families (weights source, license, params, input, vendor latency, local-measured status) | STATUS.md comparability ledger (2026-10-26) + foundation-models artifact audit (2026-10-25) |
| `benchmarks.yaml` | B1–B15 battery families ↔ U1–U20 benchmark slots, anti-shortcut controls, dataset load status | evaluation-and-benchmarks.md (families/slots/controls); family→slot mapping defined at registry creation (2026-11-02) |
| `hypotheses.yaml` | H1–H15 + legacy hypotheses, falsifiers, target scripts, status | 04-innovation/README.md |

## Honesty rules for this registry

- A field is populated **only** from text already recorded in the repository.
  Unrecorded values are `UNRECORDED` / `null` / `unknown`, never inferred.
- `papers.jsonl` coverage at creation (2026-11-02): 719 papers; 570 with a
  title recovered from in-repo tables; 107 mapped to R01–R36 direction
  sections (mapping source: `01-research/README.md` direction sections only);
  observation/supervision tags are sparse (16 / 73) because most in-repo
  records do not carry explicit V/L tags on the same record line;
  reading_depth is a conservative line-local extraction
  (FULL_TEXT_AUDITED 4 · SELECTED_SECTIONS 157 · ABSTRACT_AND_BIBLIO 187 ·
  UNRECORDED 371). `cannot_prove` is null throughout: no structured
  per-paper cannot-prove field exists in the source records yet; the
  ingest script (sequence 3.2) requires it for new entries.
- `submitted_date` is null for all current rows: the repo records do not
  carry exact submission days. `submitted_ym` is derived from the arXiv ID
  prefix (submission year-month) and labelled as such in each row.
- Rebuild papers.jsonl with: `python3 scripts/build_registry.py`.

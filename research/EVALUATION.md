# Stage 6 — Evaluation
## Experiments, Results and Falsification

Last updated: 2026-10-14

**Status:** FRAMEWORK DEFINED; full execution is downstream of Analysis, Synthesis and selected implementations.

Evaluation asks whether the claimed capability actually appears under controlled conditions and whether it survives comparison with strong alternatives.

## Evidence ladder

```text
unit / synthetic diagnostic
→ controlled benchmark
→ controlled real-world test
→ unfamiliar real environment
→ long-horizon embodied task
```

Not every question requires the full ladder, but claims must not exceed the highest evidence level reached.

## Required result metadata

```text
hypothesis or baseline
exact model / checkpoint
exact code version
exact dataset / split
visual protocol V0–V3
learning provenance L0–L4
prompt / query protocol when applicable
hardware
metric definition
number of trials
uncertainty / variance
failure cases
reproduction status
```

## Evaluation dimensions

- geometry;
- identity;
- object permanence;
- temporal consistency;
- observability / unknown;
- memory / retrieval;
- belief revision;
- intuitive physics;
- quantitative / relational physics;
- causality / intervention;
- counterfactual reasoning;
- active perception;
- open-world generalization;
- camera / embodiment shift;
- planning usefulness;
- action success;
- recovery;
- latency / memory / energy when relevant.

## Baseline rule

Compare across qualitatively different method families, not only variants of Clover.

## Results rule

Report negative results. Preserve failures that kill an idea. Do not hide trade-offs behind one average score.

## Output

Stage 6 produces result tables, figures, ablations, failure logs and explicit hypothesis status changes. Interpretation belongs to Stage 7 Reflection.

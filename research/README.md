# Research

Clover is currently in the **Background Research / Problem Reconstruction** phase.

The fixed research question is:

> **How can a machine understand the real world through vision alone?**

The long-term target is:

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Primary entry points

Start here:

1. [`survey/BACKGROUND_RESEARCH.md`](survey/BACKGROUND_RESEARCH.md) — full problem-space synthesis.
2. [`survey/SOURCE_MAP.md`](survey/SOURCE_MAP.md) — exact source URLs, evidence levels, demonstrated capabilities, limitations and Clover landing points.
3. [`survey/README.md`](survey/README.md) — Survey navigation and current research posture.

Then use:

- [`survey/FRONTIER_METHODS.md`](survey/FRONTIER_METHODS.md) — competing method families and strongest current answers.
- [`survey/RESEARCH_QUESTIONS.md`](survey/RESEARCH_QUESTIONS.md) — cross-cutting questions that must be answered before the next architecture is frozen.
- [`survey/PAPERS.md`](survey/PAPERS.md) — curated primary papers, official project pages and code links.
- [`survey/BENCHMARKS_TASKS.md`](survey/BENCHMARKS_TASKS.md) — Understanding Battery and embodied task hierarchy.
- [`survey/DATASETS_CODE.md`](survey/DATASETS_CODE.md) — datasets, repositories, checkpoints and reproducibility resources.
- [`survey/CLOVER_HYPOTHESES.md`](survey/CLOVER_HYPOTHESES.md) — screened historical/internal hypotheses, not commitments.
- [`survey/FRONTIER_SIGNALS.md`](survey/FRONTIER_SIGNALS.md) — filtered frontier/news signals that are not automatically project truth.

## Current research order

```text
Background Research / Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
→ World Formation / Learning
→ Robot Brain
→ Real-world Evaluation
→ Hardware Co-design
```

The next Clover representation is deliberately downstream of baseline and failure evidence.

## Source policy

Every durable external claim should be traceable through a primary or official source.

Preferred chain:

```text
primary paper / preprint
or official technical/model page
or official open repository
→ demonstrated capability
→ limitation / confound
→ research contradiction
→ Clover landing
```

Company/lab capability reports remain `OFFICIAL_REPORTED_RESULT` unless independently reproduced. News and secondary articles remain `SURVEY_SIGNAL` until promoted through stronger evidence.

## Supporting material

- `decisions/` — research decision records (ADR style), including the phase-order clarification.
- `literature/` — older source indices and narrower literature notes.
- `../docs/research-map/` — earlier map-style organization, retained as secondary reference.
- `../docs/research-questions/` — earlier question-by-question synthesis, retained as secondary reference.

## Rule

Raw news, a strong paper, a company demo or a historical Clover idea does not become a Clover mechanism by appearing here.

The required path is:

```text
background evidence
→ unresolved contradiction
→ baseline / Understanding Battery evidence
→ Failure Matrix
→ candidate representation
→ falsifier
→ architecture decision
```

**The question is fixed. The answer is open.**

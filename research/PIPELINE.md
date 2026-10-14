# Clover Research Lifecycle

Last updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

This file defines the canonical research lifecycle for Clover. It is deliberately flat and agent-readable.

## The seven stages

```text
1. Research
   ↓
2. Analysis
   ↓
3. Synthesis
   ↓
4. Innovation
   ↓
5. Implementation
   ↓
6. Evaluation
   ↓
7. Reflection
   ↺ feeds the next Research / Analysis / Innovation cycle
```

The stages describe **epistemic maturity**, not software versions.

---

## 1 — Research

**Meaning:** survey, discovery and evidence collection.

**Current status:** **ACTIVE**.

Purpose:

- search broadly before narrowing;
- identify all materially relevant research directions;
- collect primary papers, official project pages, code, checkpoints, datasets and benchmarks;
- record what each source claims without prematurely deciding whether Clover should adopt it;
- preserve training/evidence provenance and evaluation conditions;
- maintain a current map of methods, labs, datasets and open problems.

Typical outputs:

- source inventory;
- methods inventory;
- dataset / benchmark inventory;
- laboratory / project watchlist;
- research-domain map;
- source URLs and evidence labels;
- unresolved questions.

Research is **collection before judgment**.

Primary file: [`RESEARCH.md`](RESEARCH.md).

---

## 2 — Analysis

**Meaning:** understand how each important method actually works.

**Status:** framework defined; large-scale execution comes after the Research inventory is sufficiently broad.

For every important method, produce a small method report covering:

```text
problem
inputs / supervision
internal representation
learning objective
architecture / mechanism
memory / temporal treatment
geometry / object / physics assumptions
action interface if any
datasets
benchmarks
reported results
strengths
limitations
confounds
reproducibility
what it implies for Clover
```

Analysis asks **how and why a method works**, not merely whether its headline score is high.

Primary file: [`ANALYSIS.md`](ANALYSIS.md).

---

## 3 — Synthesis

**Meaning:** compare analyzed methods across common dimensions.

**Status:** downstream of sufficient Analysis coverage.

Purpose:

- summarize advantages and disadvantages;
- identify repeated mechanisms across superficially different methods;
- separate solved problems from recurring failures;
- build capability and failure matrices;
- identify contradictions that existing approaches cannot jointly resolve;
- determine where evidence is still missing.

Typical outputs:

```text
method-family comparison
capability matrix
failure matrix
pros / cons summary
trade-off map
shared bottlenecks
research gaps
candidate falsifiers
```

Synthesis asks **what we have learned from the field as a whole**.

Primary file: [`SYNTHESIS.md`](SYNTHESIS.md).

---

## 4 — Innovation

**Meaning:** formulate Clover-original hypotheses and algorithms from the gaps identified by Synthesis.

**Status:** ideas may be recorded, but no idea is promoted to the project answer during the current Research stage.

Innovation may contain:

- original representation hypotheses;
- new variables and mathematical formalizations;
- new learning principles;
- new memory/state/update rules;
- new causal or active-perception mechanisms;
- new algorithmic combinations only when the combination follows from a demonstrated contradiction rather than framework stacking;
- discriminating experiments and kill conditions.

Required form:

```text
observed gap
→ why existing methods fail
→ original hypothesis
→ mathematical / algorithmic statement
→ prediction
→ falsifier
→ required experiment
```

Historical Clover mechanisms live here as candidate ideas until evidence promotes or rejects them.

Primary file: [`INNOVATION.md`](INNOVATION.md).

---

## 5 — Implementation

**Meaning:** implement only sufficiently motivated hypotheses, baselines and bounded diagnostics.

**Status:** future core phase; small diagnostic implementations may occur earlier only when needed to answer a research question.

Outputs:

- reproducible code;
- baseline adapters;
- dataset loaders;
- experiments;
- model / algorithm implementation;
- instrumentation and tracing;
- environment and dependency records.

Implementation does not retroactively justify an idea merely because substantial code exists.

Primary file: [`IMPLEMENTATION.md`](IMPLEMENTATION.md).

---

## 6 — Evaluation

**Meaning:** experiments, measurements and results.

This stage includes what earlier documents called the Understanding Battery, baseline comparison and real-world evaluation.

Outputs include:

- controlled diagnostics;
- benchmark results;
- real-world results;
- generalization tests;
- ablations;
- failure cases;
- uncertainty / calibration;
- action utility;
- latency, memory and energy when scientifically relevant.

Evaluation must preserve conditions such as:

- visual observation protocol (`V0–V3`);
- learning-evidence provenance (`L0–L4`);
- dataset split;
- model version;
- hardware when relevant;
- whether a result is independently reproduced or externally reported.

Primary file: [`EVALUATION.md`](EVALUATION.md).

---

## 7 — Reflection

**Meaning:** interpret the results and decide what changes next.

Reflection is not a narrative conclusion section. It is structured scientific feedback.

Questions:

- Which hypothesis survived?
- Which hypothesis failed?
- Which failure is architectural versus data/evaluation-related?
- Which assumptions were invalid?
- Did the experiment actually discriminate the intended question?
- What new contradiction appeared?
- What should be deleted rather than patched?
- What new research must be performed before the next Innovation cycle?

Outputs:

```text
result interpretation
failure postmortem
hypothesis status changes
revised assumptions
new research questions
next-cycle priorities
```

Primary file: [`REFLECTION.md`](REFLECTION.md).

---

## Current operating rule

Clover is currently in **Stage 1 — Research**.

The immediate goal is breadth, traceability and coverage:

```text
collect the problem space
collect the strongest methods
collect primary sources
collect code / datasets / benchmarks
collect counterexamples
collect current frontier directions
```

Do not force the repository into Stage 4 Innovation because one interesting paper or idea appears.

A method may be catalogued during Research without being endorsed. A Clover idea may be recorded during Innovation without being implemented. An implementation may exist without being scientifically validated.

These distinctions are intentional.

---

**Research broadly. Analyze carefully. Synthesize comparatively. Innovate only from demonstrated gaps. Implement reproducibly. Evaluate honestly. Reflect before iterating.**

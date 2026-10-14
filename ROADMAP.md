# Clover Roadmap

Last updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

The roadmap follows one flat scientific lifecycle:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next cycle
```

The ordering matters. Clover should not invent first and search for justification later.

---

## Stage 1 — Research

**CURRENT / ACTIVE**

Goal: collect the full problem space before narrowing.

Collect:

- research directions;
- canonical foundations;
- latest strong methods;
- primary papers;
- official project pages;
- official code/checkpoints;
- datasets;
- benchmarks;
- laboratories/projects to monitor;
- visual protocols and learning provenance;
- known limitations;
- open questions.

Primary files:

- `research/PIPELINE.md`
- `research/RESEARCH.md`
- `research/survey/SOURCE_MAP.md`
- supporting Survey and dossier material.

Research is broad by design. A direction does not need to fit an existing Clover mechanism to be included.

### Stage-1 exit condition

A new agent should be able to identify the major relevant fields, strongest current methods, sources, code, datasets, benchmarks and missing areas without relying on historical Clover assumptions.

---

## Stage 2 — Analysis

Goal: understand important methods one by one.

For each method, analyze:

```text
problem
inputs / supervision
representation
mechanism
objective
memory / time
geometry
objects / relations
physics
causality
action interface
datasets
benchmarks
results
strengths
weaknesses
confounds
reproducibility
```

Output: small method reports following `research/ANALYSIS.md`.

Baseline reconstruction may occur here when implementation/probing is necessary to understand a method rather than merely trust its paper.

---

## Stage 3 — Synthesis

Goal: understand the field comparatively.

Outputs:

- capability matrix;
- method-family comparison;
- pros / cons summary;
- trade-off map;
- Failure Matrix;
- recurring bottlenecks;
- evidence gaps;
- unresolved contradictions;
- candidate discriminating experiments.

This stage summarizes what existing approaches collectively teach us.

Output framework: `research/SYNTHESIS.md`.

---

## Stage 4 — Innovation

Goal: formulate Clover-original hypotheses and algorithms from well-supported gaps.

Innovation may include:

- representation hypotheses;
- mathematical variables;
- learning objectives;
- memory/update rules;
- causal mechanisms;
- active perception mechanisms;
- machine-native algorithms;
- new evaluation hypotheses.

Every serious idea must state:

```text
observed gap
existing methods considered
why they appear insufficient
original hypothesis
mathematical / algorithmic statement
prediction
falsifier
minimal experiment
```

Historical Clover concepts are ideas here, not protected answers.

Output framework: `research/INNOVATION.md`.

---

## Stage 5 — Implementation

Goal: build reproducible baselines, diagnostics and selected Clover hypotheses.

Outputs:

- code;
- data loaders;
- baseline adapters;
- training/inference pipelines;
- experiment configs;
- instrumentation;
- deployment experiments.

Implementation does not validate a scientific claim by itself.

Output framework: `research/IMPLEMENTATION.md`.

---

## Stage 6 — Evaluation

Goal: test claims and produce Results.

Evaluation may include:

- controlled diagnostics;
- public benchmarks;
- shortcut-resistant pairs;
- memory tests;
- causal/interventional tests;
- generalization;
- active perception;
- real-world tasks;
- long-horizon action;
- ablations;
- failure cases;
- latency/memory/energy when relevant.

What earlier documents called baseline comparison and the Understanding Battery are evaluation assets within this lifecycle, not separate top-level project phases.

Evidence should progress where relevant from:

```text
controlled synthetic
→ controlled real
→ unfamiliar real environments
```

Output framework: `research/EVALUATION.md`.

---

## Stage 7 — Reflection

Goal: interpret the evidence and decide the next cycle.

Reflection records:

- what survived;
- what failed;
- what remained ambiguous;
- which assumptions were wrong;
- which mechanisms should be removed;
- which benchmarks were insufficient;
- what new research questions appeared;
- whether a hypothesis should be kept, modified, rejected or superseded.

Output framework: `research/REFLECTION.md`.

Reflection feeds the next Research / Analysis / Innovation cycle.

---

## Long-term product integration

Across later cycles, validated work should converge toward the product loop:

```text
vision
→ world understanding
→ decision
→ capability / tool selection
→ execution
→ new visual evidence
→ updated understanding
```

Robot-brain integration, real-world evaluation and hardware co-design occur inside the Implementation/Evaluation/Reflection loop rather than being treated as reasons to skip Research, Analysis or Synthesis.

## Final rule

> **Research broadly. Analyze deeply. Synthesize comparatively. Innovate from demonstrated gaps. Implement reproducibly. Evaluate honestly. Reflect before the next cycle.**

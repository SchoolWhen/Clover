# ADR 0009 — Flat Seven-Stage Research Lifecycle

Date: 2026-10-14  
Status: **ACCEPTED**

## Context

The repository accumulated several useful but overlapping process descriptions: background research, baseline setup, Understanding Battery, Failure Matrix, representation hypothesis, world formation, robot brain, evaluation and hardware co-design.

Those terms describe important activities, but as top-level phases they made the project harder for a new agent to parse and mixed research maturity with evaluation assets and system layers.

The project needs a simpler canonical lifecycle that matches normal scientific work and keeps the current foundation stage broad.

## Decision

Use one flat lifecycle:

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

### Research
Collect fields, sources, methods, code, datasets, benchmarks and open questions.

### Analysis
Produce method-by-method mechanism reports.

### Synthesis
Compare capabilities, mechanisms, pros/cons, trade-offs, failures and gaps.

### Innovation
Formulate Clover-original hypotheses and algorithms from demonstrated gaps.

### Implementation
Build reproducible baselines, diagnostics and selected Clover ideas.

### Evaluation
Run experiments, Results, ablations, generalization and real-world tests.

### Reflection
Interpret results, reject failed assumptions and feed the next cycle.

## Current stage

**Stage 1 Research is active.**

The immediate priority is broad material collection rather than architecture design.

## How earlier process concepts map into the lifecycle

- **Research Map / Background Research** → Research.
- **Baseline inventory** → Research; baseline mechanism study → Analysis; baseline code → Implementation.
- **Understanding Battery** → Evaluation design.
- **Failure Matrix** → Synthesis, informed by Analysis/Evaluation.
- **Representation Hypothesis** → Innovation.
- **World Formation / Robot Brain** → Innovation/Implementation depending maturity.
- **Real-world Evaluation** → Evaluation.
- **Hardware co-design** → Implementation/Evaluation after scientific structure is known.

These concepts remain useful. They are no longer separate top-level project phases.

## Consequences

1. New agents have a simple first-entry model of the project.
2. Stage 1 can remain wide and include any relevant field without forcing it into the existing eight dossiers.
3. Method reports get a clear home in Analysis.
4. Pros/cons and field-level conclusions get a clear home in Synthesis.
5. Historical Clover ideas are naturally classified as Innovation candidates rather than hidden assumptions.
6. Code and scientific validation remain distinct.
7. Negative results feed Reflection rather than being patched automatically.

## Non-decision

This ADR does not choose a Clover representation, learning objective, architecture, benchmark or hardware strategy.

It changes only the research operating model.

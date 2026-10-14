# Contributing to Clover

Clover is a research project. A contribution should clearly belong to one stage of the canonical lifecycle:

```text
Research → Analysis → Synthesis → Innovation → Implementation → Evaluation → Reflection
```

The current primary stage is **Research**.

## Research contributions

Useful current contributions include:

- a missing research direction;
- a primary paper or official project page;
- official code / checkpoint;
- dataset or benchmark;
- a correction to an existing source record;
- a newly relevant 2026 method;
- a missing lab/project worth monitoring;
- evidence that a method’s claimed capability is narrower than currently described.

Please preserve:

```text
exact source URL
research direction
evidence level
what is demonstrated
what is not demonstrated
code / dataset / benchmark links when available
V0–V3 / L0–L4 provenance when material
```

## Analysis contributions

When deeper method study becomes appropriate, use the method-report structure in `research/ANALYSIS.md`.

Do not summarize only the abstract. Explain representation, objective, memory/time treatment, geometry/physics/causal assumptions, action interface, datasets, benchmarks, strengths, weaknesses and confounds.

## Synthesis contributions

Compare multiple analyzed methods on the same dimensions. Useful outputs include capability matrices, pros/cons, trade-offs, recurring failure modes and research gaps.

## Innovation contributions

Do not propose `Clover + framework X` as the contribution.

A serious original hypothesis should state:

1. observed gap;
2. evidence for the gap;
3. existing methods considered;
4. why they appear insufficient;
5. original mathematical / algorithmic hypothesis;
6. prediction;
7. falsifier;
8. minimal discriminating experiment.

## Implementation contributions

Prefer inspectable, testable and reproducible code. Record configuration, dependencies, data/model versions and hardware when relevant.

Implementation status is not scientific validation.

## Evaluation contributions

An experiment should record:

- research question;
- protocol;
- model / code version;
- dataset / split;
- baseline;
- metric;
- success and kill criteria;
- result;
- failures;
- limitations of the measurement.

Negative results are valid contributions.

## Reflection contributions

State what survived, what failed, what remained ambiguous, which assumptions should change and what the next research question should be.

## Final rule

Contributions should make the project know more, not merely make the repository contain more code or more paper names.

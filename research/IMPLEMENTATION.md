# Stage 5 — Implementation
## Reproducible Code and System Construction

Last updated: 2026-10-14

**Status:** FUTURE CORE STAGE. Small diagnostic implementations are allowed earlier only when they directly answer a research question.

Implementation turns selected baselines, diagnostics and Clover hypotheses into reproducible code.

## Required implementation record

```text
implemented claim / hypothesis
source or design document
code path
configuration
model / checkpoint version
dataset version
dependencies
hardware
seed / determinism notes
input protocol
output protocol
instrumentation
known limitations
```

## Implementation priorities

1. reproducibility;
2. correctness;
3. observability / tracing;
4. clear interfaces;
5. only then optimization.

## What belongs here

- baseline adapters;
- dataset loaders;
- benchmark runners;
- probing code;
- Clover algorithm implementation;
- training/inference pipelines;
- experiment configuration;
- logging and tracing;
- deployment experiments.

## What does not count as scientific evidence

- amount of code written;
- architecture complexity;
- visual quality of a demo;
- performance on one hand-selected example;
- an implementation matching its own design specification.

Implementation creates the object that Evaluation will test. It does not validate the hypothesis by itself.

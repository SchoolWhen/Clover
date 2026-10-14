# 0008 — Background research before representation hypothesis

**Status:** Accepted  
**Date:** 2026-10-14  
**Clarifies:** 0005 — Research before reproduction

## Context

The 2026-10-14 Research Reset explicitly requires Clover to establish strong baselines, a capability map and a benchmark battery before proposing the next representation hypothesis.

ADR 0005 correctly established that Clover should not rush directly into reproducing large frontier systems. However, one phrase in 0005 could be read as waiting for a sharper representation hypothesis **before** systematic baseline comparison. That ordering would risk reintroducing the old failure mode: choosing a representation first and then collecting evidence around it.

The Research Reset instead gives the stronger sequence:

```text
Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
```

## Decision

Clover's active phase ordering is:

```text
Background Research / Problem Reconstruction
→ Baseline Reconstruction
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
→ World Formation / Learning
→ Robot Brain
→ Real-world Evaluation
→ Hardware Co-design
```

Background research must be primary-source-backed and broad enough to include classical vision, modern self-supervised image/video learning, learned geometry, object-centric models, persistent memory, intuitive physics, causality, active perception, generative world models, VLM/VLA/world-action models and real robot foundation systems.

Baseline work is permitted and eventually required **before** a representation is frozen, when it is used to answer discriminating research questions rather than to optimize a leaderboard.

## What this changes

- `BACKGROUND_RESEARCH.md` and `SOURCE_MAP.md` become primary research surfaces.
- DINOv3, V-JEPA 2/2.1, VGGT/Ω, SAM 3.1 and strong embodied systems are treated as current comparators.
- Persistent memory, anti-shortcut physics, causal/interventional evaluation and active perception become first-class research dimensions.
- The next Clover representation is not selected until the baseline/battery/failure-map evidence exists.

## What this does not change

ADR 0005 remains correct that:

- reproduction is not an end in itself;
- benchmarks are instruments;
- external systems are counter-hypotheses/evidence rather than modules to stack into Clover;
- large expensive reproduction should wait until a smaller study cannot answer the relevant research question.

This ADR only clarifies the **ordering**: a representation hypothesis is downstream of baseline evidence, not a prerequisite for obtaining it.

## Consequences

A future architecture proposal must cite the failure matrix and state which observed cross-family failure it is intended to solve.

The following are not sufficient reasons to create a new mechanism:

```text
historical Clover already has it
another paper uses it
it sounds machine-native
it is faster on one benchmark
it fits the local hardware well
```

The admissible chain is:

```text
background evidence
→ unresolved contradiction
→ discriminating baseline/battery result
→ candidate representation
→ falsifier
→ implementation
```

## Final rule

> **Do not choose the answer before measuring the problem.**

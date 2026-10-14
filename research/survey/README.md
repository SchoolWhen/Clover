# Clover Survey

Last updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This folder is **supporting material for Stage 1 Research and later Stage 2 Analysis**.

The flat primary navigation is now:

1. [`../PIPELINE.md`](../PIPELINE.md)
2. [`../RESEARCH.md`](../RESEARCH.md)
3. [`../ANALYSIS.md`](../ANALYSIS.md)
4. [`../SYNTHESIS.md`](../SYNTHESIS.md)
5. [`../INNOVATION.md`](../INNOVATION.md)
6. [`../IMPLEMENTATION.md`](../IMPLEMENTATION.md)
7. [`../EVALUATION.md`](../EVALUATION.md)
8. [`../REFLECTION.md`](../REFLECTION.md)

**Current active stage: Research.**

## What this Survey folder is for

Use these files when the broad inventory needs deeper evidence:

- [`SOURCE_MAP.md`](SOURCE_MAP.md) — exact source URLs, evidence level, demonstrated capability and limitation.
- [`BACKGROUND_RESEARCH.md`](BACKGROUND_RESEARCH.md) — broad problem-space synthesis.
- [`RESEARCH_OVERVIEW.md`](RESEARCH_OVERVIEW.md) — visual map of domains and evidence flow.
- [`FRONTIER_METHODS.md`](FRONTIER_METHODS.md) — method-family references.
- [`RESEARCH_QUESTIONS.md`](RESEARCH_QUESTIONS.md) — unresolved technical questions.
- [`PAPERS.md`](PAPERS.md) — paper/project/code index.
- [`BENCHMARKS_TASKS.md`](BENCHMARKS_TASKS.md) — benchmark/task inventory.
- [`DATASETS_CODE.md`](DATASETS_CODE.md) — datasets and reproducibility resources.
- [`CLOVER_HYPOTHESES.md`](CLOVER_HYPOTHESES.md) — historical/internal ideas, not conclusions.
- [`FRONTIER_SIGNALS.md`](FRONTIER_SIGNALS.md) — discovery signals that still require primary-source verification.

The deeper [`../dossiers/`](../dossiers/) are topic notes, not separate project phases.

## Source discipline

During Research, record:

```text
research direction
method / source name
exact primary / official URL
code / checkpoint if available
dataset / benchmark if available
evidence level
what is demonstrated
what remains unknown
V0–V3 protocol when material
L0–L4 training provenance when material
```

Preferred evidence order:

```text
primary paper / preprint
official technical/project page
official code / checkpoint
official reported result
secondary signal only for discovery
```

## What Survey material does not mean

A paper appearing here does not mean its mechanism should be added to Clover.

A benchmark appearing here does not mean maximizing its score is the project objective.

A company demo appearing here does not mean its capability is independently validated.

A historical Clover idea appearing here does not mean it survives the current research process.

## Vision-only annotation

Observation:

- `V0` monocular RGB + temporal order;
- `V1` V0 + camera intrinsics;
- `V2` calibrated multi-camera RGB;
- `V3` active embodied vision.

Learning provenance:

- `L0` visual self-supervision;
- `L1` visual labels/annotations;
- `L2` language/world knowledge;
- `L3` action-conditioned experience;
- `L4` non-visual or privileged physical evidence.

## Current research landscape

The broad active inventory is maintained in [`../RESEARCH.md`](../RESEARCH.md), which currently includes classical and learned geometry, static/video SSL, 3D/4D reconstruction, neural scene representation, object-centric learning, semantic mapping, memory, physical reasoning, causality, active perception, system identification, world models, WAM, VLA, robot foundation models, human video transfer, affordance learning, control, uncertainty/OOD, continual learning, simulation, datasets, benchmark methodology and systems integration.

If a relevant direction is missing, add it to the broad Research inventory first. Deep analysis comes later.

---

**Survey widely first; architecture decisions come later.**

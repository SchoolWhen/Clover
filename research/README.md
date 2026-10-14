# Research

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

Clover uses one flat research lifecycle:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next research cycle
```

**Current stage: 1 — Research.**

## Read this folder in order

| Stage | File | Purpose | Current status |
|---|---|---|---|
| 0 | [`PIPELINE.md`](PIPELINE.md) | explains the complete lifecycle | canonical |
| 1 | [`RESEARCH.md`](RESEARCH.md) | broad source/method/dataset/benchmark inventory | **ACTIVE** |
| 2 | [`ANALYSIS.md`](ANALYSIS.md) | one-method-one-report mechanism analysis | template ready |
| 3 | [`SYNTHESIS.md`](SYNTHESIS.md) | compare strengths, weaknesses, trade-offs and gaps | future |
| 4 | [`INNOVATION.md`](INNOVATION.md) | Clover-original hypotheses / algorithms / ideas | ideas only |
| 5 | [`IMPLEMENTATION.md`](IMPLEMENTATION.md) | reproducible code and systems | future core stage |
| 6 | [`EVALUATION.md`](EVALUATION.md) | experiments and Results | framework ready |
| 7 | [`REFLECTION.md`](REFLECTION.md) | interpret failures and start the next cycle | future |

A new agent should start with `PIPELINE.md`, then read the active `RESEARCH.md` inventory before opening deeper survey material.

## Current Stage 1 goal

The current objective is not to decide the next Clover architecture.

It is to collect the field broadly enough that later analysis is not biased by a narrow set of papers or historical Clover ideas.

Collect:

```text
research directions
canonical foundations
latest strong methods
primary papers
official project pages
open code / checkpoints
datasets
benchmarks
reported capabilities
known limitations
labs / projects to monitor
open questions
```

`RESEARCH.md` currently tracks dozens of directions including epistemology, classical geometry, static/video SSL, 3D/4D reconstruction, neural scene representations, object-centric models, scene graphs, persistent memory, physical reasoning, causal learning, active perception, system identification, generative world models, world-action models, VLA, robot foundation models, egocentric video, affordance learning, model-based control, uncertainty/OOD, continual learning and simulation/data engines.

## Detailed Stage-1 assets

The flat stage files are the primary navigation. Existing deeper material remains available as supporting evidence:

- [`survey/RESEARCH_OVERVIEW.md`](survey/RESEARCH_OVERVIEW.md) — visual research map.
- [`survey/BACKGROUND_RESEARCH.md`](survey/BACKGROUND_RESEARCH.md) — broad background synthesis.
- [`survey/SOURCE_MAP.md`](survey/SOURCE_MAP.md) — source → evidence → claim → limitation map.
- [`survey/FRONTIER_METHODS.md`](survey/FRONTIER_METHODS.md) — method-family references.
- [`survey/PAPERS.md`](survey/PAPERS.md) — paper/project/code index.
- [`survey/BENCHMARKS_TASKS.md`](survey/BENCHMARKS_TASKS.md) — benchmark and task inventory.
- [`survey/DATASETS_CODE.md`](survey/DATASETS_CODE.md) — datasets and reproducibility resources.
- [`dossiers/`](dossiers/) — deeper domain notes. These support Stage 1 Research and later Stage 2 Analysis; they are not separate project phases.

## Source policy

For durable claims, prefer:

```text
primary paper / preprint
official technical or model page
official open-source repository
company/lab reported capability (explicitly labeled)
secondary signal only for discovery
```

Every important source should preserve:

```text
exact URL
what it demonstrates
what it does not demonstrate
input / training provenance
reproducibility status
relevant dataset / benchmark
```

## Current rule

Do not prematurely promote Research material into Innovation.

The intended flow is:

```text
collect broadly
→ analyze important methods one by one
→ synthesize strengths / weaknesses / gaps
→ propose original hypotheses
→ implement
→ evaluate
→ reflect
```

**Research broadly first. Protect the question, not the current answer.**

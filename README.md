# Clover

**Open research on how machines can understand the real world through vision alone.**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

Clover is a long-term open research project. **The question is fixed; the answer is open.** The repository is a public research record: evidence, hypotheses, decisions, architecture and eventual implementations are kept distinct so the project can change its answer without changing its question.

[中文说明](README.zh-CN.md)

## Start here

If you are an agent, contributor or researcher entering the repository for the first time, read in this order:

1. [`AGENTS.md`](AGENTS.md) — mandatory repository rules for research agents.
2. [`SSOT.md`](SSOT.md) — the highest research question, product goal and scientific stance.
3. [`PRINCIPLES.md`](PRINCIPLES.md) — research principles.
4. [`STATUS.md`](STATUS.md) — current phase and what has not been demonstrated.
5. [`research/survey/BACKGROUND_RESEARCH.md`](research/survey/BACKGROUND_RESEARCH.md) — full problem-space background.
6. [`research/survey/SOURCE_MAP.md`](research/survey/SOURCE_MAP.md) — source → evidence → claim → limitation → Clover landing.
7. [`research/survey/README.md`](research/survey/README.md) — survey navigation.

## Current phase — Background Research / Problem Reconstruction

The 2026-10-14 Research Reset moved Clover from architecture-first development to problem-first research.

The current order is:

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

We are **not** currently freezing a new Clover representation. The immediate objective is to make the background research deep and source-backed enough that later baselines and experiments can identify the failures shared by strong existing approaches.

## Primary research surfaces

- [Background Research](research/survey/BACKGROUND_RESEARCH.md)
- [Source Map](research/survey/SOURCE_MAP.md)
- [Frontier Methods](research/survey/FRONTIER_METHODS.md)
- [Research Questions](research/survey/RESEARCH_QUESTIONS.md)
- [Papers & Primary Sources](research/survey/PAPERS.md)
- [Benchmarks & Embodied Tasks](research/survey/BENCHMARKS_TASKS.md)
- [Datasets & Code](research/survey/DATASETS_CODE.md)
- [Clover Hypotheses](research/survey/CLOVER_HYPOTHESES.md)
- [Frontier Signals](research/survey/FRONTIER_SIGNALS.md)

Older `docs/research-map/`, `docs/research-questions/` and `research/literature/` structures remain as secondary reference and research history.

## What we want to build

The eventual product-level target is a general-purpose robotic brain:

```text
Vision
  ↓
World understanding
  ↓
Decision
  ↓
Tool / capability selection
  ↓
Execution
  ↓
new visual observation
  └──────────────→ updated world understanding
```

This is a product-level objective, not a commitment to a particular internal representation, neural architecture or module boundary.

## What we mean by understanding

The working research target includes the ability to form, maintain, use and revise world knowledge supporting:

- existence and observability;
- identity and object permanence;
- spatial and temporal structure;
- dynamics and physically plausible change;
- uncertainty, unknown and unobserved state;
- causal and counterfactual reasoning;
- memory and belief revision;
- generalization to unfamiliar objects, scenes, cameras and dynamics;
- active acquisition of missing visual evidence;
- measurable usefulness for decision, planning, execution and recovery.

See [`SSOT.md`](SSOT.md) and [What is Understanding?](docs/what-is-understanding.md).

## What we do not assume

Clover does **not** assume that:

- CPU computation is inherently superior to GPU computation;
- explicit world state is inherently superior to distributed latent representation;
- field crystallization is necessarily the final representation;
- objects, fields, geometry or tokens must be the primitive ontology;
- Transformers are inherently unsuitable for world understanding;
- prediction, reconstruction or generation is necessarily the correct learning objective;
- persistent explicit world state is necessarily required for strong robot behavior;
- a single benchmark can define world understanding;
- the current Clover prototype is the final architecture.

Hardware, representation, learning objective, memory model and software architecture are research variables.

## “Vision alone” protocol

Clover distinguishes the visual observation budget:

- `V0` — monocular RGB + temporal order;
- `V1` — V0 + camera intrinsics;
- `V2` — calibrated multi-camera RGB;
- `V3` — active embodied vision where action changes future visual evidence.

Background research also records training-data provenance when relevant (`L0` visual self-supervision through `L4` non-visual/privileged physical evidence). This prevents deployment-time RGB input from being confused with knowledge learned only from vision.

## Evaluation stance

Benchmarks are **measurement instruments**, not the SSOT.

The evidence standard must combine:

1. controlled visual/physical diagnostics;
2. shortcut-resistant paired tests;
3. persistent and streaming memory tests;
4. causal/interventional tests;
5. real-video/open-world generalization;
6. active perception;
7. world change and belief revision;
8. long-horizon embodied tasks in unfamiliar environments;
9. downstream action/recovery value;
10. efficiency after scientific capability is established.

See [Benchmarks & Embodied Tasks](research/survey/BENCHMARKS_TASKS.md).

## Existing Clover work

A substantial pre-reset Research Prototype 1 explored field-based visual evidence, persistent entities/spacetime support, typed world queries, epistemic licences, decision, tool-use and execution loops.

Those ideas remain research history and candidate hypotheses. They are **not frozen answers**. The current background research re-evaluates them against classical vision, modern self-supervised image/video models, learned geometry, object-centric learning, memory benchmarks, generative world models, VLA/robot foundation models, POMDP/active perception and causal-representation research.

## Repository navigation

### Current research

- [Survey](research/survey/README.md)
- [Background Research](research/survey/BACKGROUND_RESEARCH.md)
- [Source Map](research/survey/SOURCE_MAP.md)
- [Research decisions](research/decisions/)
- [Open questions](docs/open-questions.md)
- [Active hypotheses](docs/hypotheses/README.md)

### Secondary research references

- [Research map](docs/research-map/README.md)
- [Question synthesis](docs/research-questions/README.md)
- [Primary source index](research/literature/primary-sources.md)
- [2026 frontier watch](research/literature/2026-frontier.md)

### Project definition

- [SSOT](SSOT.md)
- [Principles](PRINCIPLES.md)
- [Status](STATUS.md)
- [Roadmap](ROADMAP.md)
- [Glossary](docs/glossary.md)

## Status vocabulary

- `IMPLEMENTED` — exists in code;
- `TESTED` — has direct test coverage;
- `RESEARCH_PROTOTYPE` — implemented as a research mechanism, not scientifically established;
- `SCIENTIFICALLY_VALIDATED` — supported by an explicit scientific protocol;
- `OPEN` — unresolved;
- `SUPERSEDED` — retained for history but no longer current.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). A new method or paper should enter the repository through the contradiction it helps answer, not as a framework to stack onto Clover.

## License

Apache License 2.0. See [LICENSE](LICENSE).

---

**The question is fixed. The answer is open.**

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
2. [`SSOT.md`](SSOT.md) — the highest research question, product goal and current scientific stance.
3. [`PRINCIPLES.md`](PRINCIPLES.md) — research principles.
4. [`STATUS.md`](STATUS.md) — what is current, what is open, and what has not been demonstrated.
5. [`research/survey/README.md`](research/survey/README.md) — the primary research survey and navigation layer.

## Current phase — Survey / Research Foundation

The 2026-10-14 Research Reset moved Clover from architecture-first development to problem-first research.

The immediate objective is to understand the strongest prior and current answers before freezing the next Clover representation. We are therefore prioritizing **survey and synthesis before reproduction or benchmark optimization**.

The primary research surface is intentionally flat:

- [Frontier Methods](research/survey/FRONTIER_METHODS.md)
- [Papers & Primary Sources](research/survey/PAPERS.md)
- [Benchmarks & Embodied Tasks](research/survey/BENCHMARKS_TASKS.md)
- [Datasets & Code](research/survey/DATASETS_CODE.md)
- [Research Questions](research/survey/RESEARCH_QUESTIONS.md)
- [Clover Hypotheses](research/survey/CLOVER_HYPOTHESES.md)
- [Frontier Signals](research/survey/FRONTIER_SIGNALS.md)

Older `docs/research-map/` and `research/literature/` structures remain as secondary reference and research history.

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
- generalization to unfamiliar objects, scenes and compositions;
- active perception;
- measurable usefulness for decision and action.

See [`SSOT.md`](SSOT.md) and [What is Understanding?](docs/what-is-understanding.md).

## What we do not assume

Clover does **not** assume that:

- CPU computation is inherently superior to GPU computation;
- explicit world state is inherently superior to distributed latent representation;
- field crystallization is necessarily the final representation;
- objects, fields, geometry or tokens must be the primitive ontology;
- Transformers are inherently unsuitable for world understanding;
- prediction, reconstruction or generation is necessarily the correct learning objective;
- a single benchmark can define world understanding;
- the current Clover prototype is the final architecture.

Hardware, representation, learning objective and software architecture are research variables.

## Evaluation stance

Benchmarks are **measurement instruments**, not the SSOT.

The eventual evidence standard must combine:

1. controlled visual/physical diagnostics;
2. real video and open-world generalization;
3. persistent world-state and revision tests;
4. intervention / causal tests;
5. active perception;
6. long-horizon embodied tasks in unfamiliar environments;
7. downstream decision and recovery value;
8. efficiency after scientific capability is established.

See [Benchmarks & Embodied Tasks](research/survey/BENCHMARKS_TASKS.md).

## Existing Clover work

A substantial pre-reset Research Prototype 1 explored field-based visual evidence, persistent entities/spacetime support, typed world queries, epistemic licences, decision, tool-use and execution loops.

Those ideas remain valuable research history and hypotheses. They are **not frozen answers**. The current Survey re-evaluates them against classical vision, modern video/self-supervised models, spatial intelligence, VLA/robot foundation models, model-based robotics and 2026 frontier work.

## Repository navigation

### Current research

- [Survey](research/survey/README.md)
- [Open questions](docs/open-questions.md)
- [Research decisions](research/decisions/)
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

# Clover

**Open research on how machines can understand the real world through vision alone.**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

Clover is a long-term open research project. The research question is fixed; the answer is open. The repository is a public research record: current evidence, active hypotheses, architecture, open questions, and decisions are kept separate so the project can change direction without rewriting its history.

[中文说明](README.zh-CN.md)

## Why this problem matters

A robot can sometimes map pixels directly to actions without maintaining a durable model of the world. Clover asks the deeper question: what internal structure is sufficient for a machine to recognize persistence, identity, space, time, dynamics, causality, uncertainty and change from visual experience — and to use that structure for decision and action?

The target is not a single benchmark score. Benchmarks are instruments. The eventual standard is real capability in unfamiliar physical environments.

## What we want to build

At the system level, the current decomposition is:

```text
Vision
  ↓
Worldview
  ↓
Decision
  ↓
Tool Use
  ↓
Execution
  ↓
new visual observation
  └──────────────→ Worldview
```

This is a system-level decomposition, not a commitment to one internal representation or one learning architecture.

## What we mean by understanding

Our working definition includes the ability to maintain and revise a world model that supports:

- persistent world state and object permanence;
- identity through time and occlusion;
- spatial and temporal structure;
- observability, unknown and unobserved state;
- dynamics and physically plausible change;
- causal and counterfactual reasoning;
- memory and belief revision;
- generalization to unfamiliar scenes and objects;
- measurable usefulness for decision and action.

The definition itself remains a research object. See [What is Understanding?](docs/what-is-understanding.md).

## What we do not assume

Clover does **not** assume that:

- CPU computation is inherently superior to GPU computation;
- explicit representations are always superior to learned latent representations;
- field crystallization is necessarily the final world representation;
- Transformers are inherently unsuitable for world understanding;
- one benchmark can define whether a machine understands the world;
- the current Clover architecture is the final architecture.

Hardware, representation and learning method are design variables. They should be selected by evidence.

## Current phase

The 2026-10-14 Research Reset moved Clover from architecture-first development to problem-first research.

We are now prioritizing **research before reproduction**: mapping what classical vision, modern representation learning, world models, spatial intelligence and real robot systems already solve before freezing the next Clover representation.

See [STATUS.md](STATUS.md) and [research decision 0005](research/decisions/0005-research-before-reproduction.md).

## Research map

The current map covers:

- classical computer vision and geometry;
- learned visual representations;
- self-supervised video/world models;
- spatial intelligence and learned geometry;
- object-centric representation;
- embodied reasoning and VLA systems;
- robot foundation models;
- model-based robotics and active perception;
- causality and lifelong learning;
- data, experience and interaction.

Start with the [Research Map](docs/research-map/README.md), then use the [Model & Literature Index](research/literature/model-index.md) for specific systems.

## Current prototype

A substantial Clover research prototype was developed before this public repository was initialized, exploring field-based visual evidence, persistent entities, typed world queries, epistemic licences, decision, tool-use and execution loops. That implementation is **Research Prototype 1**, not a frozen answer. Public code migration will follow a dedicated safety, build and documentation audit.

## Research hypotheses

Existing Clover mechanisms are tracked as hypotheses rather than project axioms, including field crystallization, machine-native primitives, explicit world state, spacetime structure, epistemic licences and world growth.

See [Active Hypotheses](docs/hypotheses/README.md).

## Evaluation

We maintain an [Evaluation Map](docs/evaluation/benchmark-map.md) and a working [Understanding Battery](docs/evaluation/understanding-battery.md). These are measurement plans, not immediate leaderboard objectives.

## Research principles

The central rules are in [PRINCIPLES.md](PRINCIPLES.md). In short:

1. The question comes first.
2. Evidence comes before architectural commitment.
3. Benchmarks are instruments, not the objective.
4. Real embodied capability matters.
5. Facts, hypotheses and plans remain separate.
6. External methods are studied for the contradiction they solve, not stacked as modules.
7. Hardware is a design variable.
8. Important mechanisms must be falsifiable.
9. Code must remain inspectable.
10. World understanding must eventually improve action.

## Documentation

- [Research question](docs/research-question.md)
- [Product goal](docs/product-goal.md)
- [What is understanding?](docs/what-is-understanding.md)
- [Research map](docs/research-map/README.md)
- [Model & literature index](research/literature/model-index.md)
- [Datasets & benchmarks index](research/literature/datasets-and-benchmarks.md)
- [Open questions](docs/open-questions.md)
- [Current architecture notes](docs/architecture/README.md)
- [Evaluation principles](docs/evaluation/evaluation-principles.md)
- [Glossary](docs/glossary.md)
- [Research decisions](research/decisions/)

## Status vocabulary

- `IMPLEMENTED` — exists in code;
- `TESTED` — has direct test coverage;
- `RESEARCH_PROTOTYPE` — implemented as a research mechanism, not scientifically established;
- `SCIENTIFICALLY_VALIDATED` — supported by an explicit scientific protocol;
- `OPEN` — unresolved;
- `SUPERSEDED` — retained for history but no longer current.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Research proposals should identify the contradiction they solve, relevant prior work, a falsifier, and expected impact on the central question.

## License

Apache License 2.0. See [LICENSE](LICENSE).

---

**The question is fixed. The answer is open.**

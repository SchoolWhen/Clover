# Clover

**Open research on how machines can understand the real world through vision alone.**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

Clover is a long-term open research project. The research question is fixed; the answer is open. The repository is being developed as a public research record: current evidence, active hypotheses, architecture, open questions, and future experiments are kept separate so that the project can change direction without rewriting its history.

[中文说明](README.zh-CN.md)

## Why this problem matters

A robot that only maps pixels directly to actions can be effective without necessarily maintaining a durable model of the world. Clover asks a different question: what internal structure is sufficient for a machine to recognize persistence, identity, space, time, dynamics, causality, uncertainty, and change from visual experience, and to use that structure for decision and action?

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

## Current research direction

The 2026-10-14 research reset moved Clover from architecture-first development to problem-first research. Current investigation spans:

- classical computer vision and geometry;
- self-supervised visual and video representation learning;
- video and action-conditioned world models;
- spatial intelligence and learned geometry;
- object-centric representation;
- embodied reasoning, VLA and robot foundation models;
- active perception and model-based robotics;
- causality, counterfactual reasoning and lifelong world growth.

See the [Research Map](docs/research-map/README.md).

## Current prototype

A substantial Clover research prototype has been developed outside this newly initialized public repository, exploring field-based visual evidence, persistent entities, typed world queries, epistemic licences, decision, tool-use and execution loops. That implementation is being treated as **Research Prototype 1**, not as a frozen answer. Public code migration will follow a repository safety and documentation audit.

The public status is tracked in [STATUS.md](STATUS.md).

## Research hypotheses

Existing Clover mechanisms are now tracked as hypotheses rather than project axioms. These include field crystallization, machine-native primitives, explicit world state, spacetime structure, epistemic licences and world growth.

See [docs/hypotheses](docs/hypotheses/README.md).

## Research principles

The central rules are in [PRINCIPLES.md](PRINCIPLES.md). In short:

1. The question comes first.
2. Evidence comes before architectural commitment.
3. Benchmarks are instruments, not the objective.
4. Real embodied capability matters.
5. Facts, hypotheses and plans must remain separate.
6. External methods are studied for the contradiction they solve, not stacked as modules.
7. Hardware is a design variable.
8. Important mechanisms must be falsifiable.
9. Code must remain inspectable.
10. World understanding must eventually improve action.

## Roadmap

The project is currently in **Phase 0 — Public Research Foundation** and **Phase 1 — Understanding the Problem**. See [ROADMAP.md](ROADMAP.md).

## Documentation

- [Research question](docs/research-question.md)
- [Product goal](docs/product-goal.md)
- [What is understanding?](docs/what-is-understanding.md)
- [Research map](docs/research-map/README.md)
- [Open questions](docs/open-questions.md)
- [Current architecture notes](docs/architecture/README.md)
- [Evaluation map](docs/evaluation/README.md)
- [Glossary](docs/glossary.md)
- [Research decisions](research/decisions/)

## Status vocabulary

Public documentation uses the following states:

- `IMPLEMENTED` — exists in code;
- `TESTED` — has direct test coverage;
- `RESEARCH_PROTOTYPE` — implemented as a research mechanism, not yet established scientifically;
- `SCIENTIFICALLY_VALIDATED` — supported by an explicit scientific protocol;
- `OPEN` — unresolved;
- `SUPERSEDED` — retained for history but no longer current.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Research proposals should identify the contradiction they solve, relevant prior work, a falsifier, and expected impact on the central question.

## License

Apache License 2.0. See [LICENSE](LICENSE).

---

**The question is fixed. The answer is open.**

# Clover Survey

Last updated: 2026-10-14  
Phase: **Survey / Research Foundation**

This directory is the compact, high-density research entry point for Clover.

The central question is:

> **How can a machine understand the real world through vision alone?**

The product target is:

> **A general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Why this Survey exists

Earlier Clover work accumulated original mechanisms, code, benchmarks, news notes and daily decisions quickly. The 2026-10-14 Research Reset changed the order of work:

```text
research question
→ prior art
→ capability map
→ unresolved contradiction
→ representation hypothesis
→ implementation
→ evaluation
```

rather than:

```text
interesting mechanism
→ implementation
→ find benchmark
→ defend mechanism
```

This Survey is the prior-art and synthesis layer. It is intentionally flatter than the older `docs/research-map/` structure: a small number of larger Markdown files should let a reader scan the whole research landscape quickly.

## Reading order

1. [`../../SSOT.md`](../../SSOT.md) — the research question, product goal and evidence standard.
2. [`FRONTIER_METHODS.md`](FRONTIER_METHODS.md) — the strongest method families and what they actually solve.
3. [`RESEARCH_QUESTIONS.md`](RESEARCH_QUESTIONS.md) — unresolved technical questions that should drive the next Clover design.
4. [`PAPERS.md`](PAPERS.md) — curated primary papers and official technical reports.
5. [`BENCHMARKS_TASKS.md`](BENCHMARKS_TASKS.md) — what existing evaluations measure and what they do not prove.
6. [`DATASETS_CODE.md`](DATASETS_CODE.md) — datasets, codebases, checkpoints and platform resources.
7. [`CLOVER_HYPOTHESES.md`](CLOVER_HYPOTHESES.md) — surviving internal candidate ideas from pre-reset Clover.
8. [`FRONTIER_SIGNALS.md`](FRONTIER_SIGNALS.md) — filtered 2026 signals from the internal news archive and current frontier scan.

## Source inputs used for this synthesis

This Survey incorporates screened material from three internal documents.

### Clover Research Reset — 2026-10-14
Kept: highest SSOT/product goal, benchmark-as-instrument, V0–V3 vision protocol, research map, benchmark/task map, hardware-as-design-variable, representation questions and primary links.

Not kept as current commitments: immediate reproduction schedule, CPU-first as scientific prior, or any pre-reset mechanism as a final answer.

### `news_answers.md`
Kept as candidate hypotheses: Evidence Replay, query-conditioned temporal support, epistemic/verification separation, auditability, counter-witness causality, event-like IR, epistemic compute scheduling, static/dynamic verification, geometry heuristic, state-transition affordance, active perception and long-horizon revision.

Old implementation priority labels are not SSOT.

### `news(5).md`
Used only as a signal archive. A news item becomes durable evidence only when primary/official material is available. Funding, secondary summaries and vendor claims remain signals.

## Evidence labels

- **PRIMARY_PAPER** — primary preprint or peer-reviewed paper.
- **OFFICIAL_PROJECT** — official model/project page.
- **OPEN_SOURCE** — public implementation/checkpoint.
- **OFFICIAL_REPORTED_RESULT** — company/lab result without independent reproduction.
- **SURVEY_SIGNAL** — useful trend, not a scientific result by itself.
- **INTERNAL_HYPOTHESIS** — Clover candidate.
- **OPEN** — unresolved.
- **SUPERSEDED** — historical, no longer current.

## Research landscape at a glance

| Route | Typical internal state | Primary strength | Typical weakness / unresolved issue |
|---|---|---|---|
| Classical geometry / SLAM | explicit pose, map, geometry | precision, observability, optimization | semantics, abstraction, open-world learning |
| Static self-supervised vision | distributed visual features | broad visual invariance | weak temporal persistence / dynamics |
| Video predictive representation | distributed temporal latent | motion, anticipation, prediction | state interpretability, persistent world identity |
| Geometry foundation model | learned depth / pose / point map | scalable spatial reconstruction | semantics, physics, causality |
| Object-centric model | slots / entities | compositionality, identity hypothesis | segmentation/object assumptions, scalability |
| Generative world model | latent simulator | rich rollout / world completion | truth vs plausible generation |
| Embodied VLM reasoning | multimodal context | flexible high-level reasoning | language priors, persistent state unclear |
| VLA / world-action model | action-conditioned latent | direct task performance | world-state semantics, failure attribution |
| Robot foundation policy | broad learned policy | real task breadth / transfer | what is actually represented internally? |
| Model-based robotics | explicit belief/state/dynamics | planning under uncertainty | representation acquisition / high-level semantics |
| Clover historical route | explicit candidate world + authority | inspectability / queryability hypothesis | not yet established as the best representation |

No row is declared the winner.

## Current strongest tensions

### Explicit vs distributed
Physical variables can emerge in distributed/hierarchical video representations rather than only compact classical state.
- Paper: https://arxiv.org/abs/2602.07050
- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

### Prediction vs reconstruction vs generation
- V-JEPA 2/2.1: predictive latent representation.
- VGGT/VGGT-Ω: learned geometry/reconstruction.
- Atlas: reconstruction + generation + simulation.
- Cosmos 3: reasoning + world generation + action generation.

Open question: **which learning objective produces state most useful for persistent understanding and action?**

### Observation vs interaction
Passive video can learn substantial dynamics; robot experience adds intervention/controllability information. Open question: **what causal/action knowledge cannot be identified from passive observation alone?**

### World state vs direct policy
Strong robot foundation/VLA systems are serious competing routes. Open question: **what measurable capability is gained by a persistent worldview that a sufficiently strong policy cannot obtain implicitly?**

### Visual truth vs plausible generation
A generative model can produce coherent rollouts while inventing underdetermined hidden details. Clover must preserve the distinction between plausible completion and evidence-supported state.

## Survey maturity criteria

For every major route we should answer:
1. representation;
2. learned vs engineered structure;
3. space/time treatment;
4. identity/persistence;
5. unknown/observability;
6. physics/causality;
7. memory;
8. action interface;
9. demonstrated real capability;
10. unresolved failures;
11. public code/data;
12. falsifiers relevant to Clover.

## Current phase boundary

We are **not** yet freezing a final world representation, explicit-vs-latent decision, Transformer-vs-non-Transformer choice, object-vs-field ontology, CPU-vs-GPU allocation, or final licence/authority mechanism.

The next Clover architecture should be a result of this Survey, not a prerequisite for it.

---

**The question is fixed. The answer is open.**

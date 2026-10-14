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

Kept:
- highest SSOT and product goal;
- benchmark-as-instrument principle;
- V0–V3 vision protocol;
- research map and benchmark/task map;
- hardware-as-design-variable principle;
- representation questions and primary links.

Not kept as current commitments:
- immediate reproduction schedule;
- CPU-first as a scientific prior;
- any pre-reset mechanism as a final answer.

### `news_answers.md`

Kept as candidate research hypotheses:
- Evidence Replay;
- query-conditioned temporal support;
- separation of epistemic state and verification lifecycle;
- proof/auditability ideas;
- counter-witness causality;
- sparse/event-like visual IR;
- epistemic compute scheduling;
- static/dynamic verification compilation;
- geometry as a proposal heuristic;
- state-transition affordance;
- active perception and long-horizon world-change evaluation.

Old implementation priority labels are not SSOT.

### `news(5).md`

Used only as a signal archive. A news item enters the Survey as durable evidence only when primary/official material is available. Funding, secondary summaries and vendor claims remain signals, not scientific facts.

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
Physical variables can emerge in distributed/hierarchical video representations rather than only compact classical state. This is direct counter-pressure against assuming that explicit state is always the correct answer.

- Paper: https://arxiv.org/abs/2602.07050
- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

### Prediction vs reconstruction vs generation
- V-JEPA 2/2.1: predictive latent representation.
- VGGT/VGGT-Ω: learned geometry and reconstruction.
- Atlas: reconstruction + generation + simulation.
- Cosmos 3: reasoning + world generation + action generation.

Open question: **which learning objective produces the state most useful for persistent understanding and action?**

### Observation vs interaction
V-JEPA 2 shows broad passive-video learning before a smaller action-conditioned stage; robot foundation models increasingly mix human video, robot data, simulation and self-play. Open question: **what information about causality, controllability and affordance is unavailable from passive observation alone?**

### World state vs direct policy
Gemini Robotics ER 2 explicitly separates high-level embodied reasoning from lower-level execution, while π0.5, Helix and Skild represent stronger policy/foundation routes. Open question: **what measurable capability is gained by a persistent worldview that a sufficiently strong policy cannot obtain implicitly?**

### Visual truth vs plausible generation
A generative model can produce coherent rollouts while inventing underdetermined hidden details. Clover must preserve the difference between plausible completion and evidence-supported world state.

## Survey maturity criteria

For every major route we should eventually answer:
1. What representation does it assume?
2. What is learned vs engineered?
3. How does it treat space and time?
4. How does it maintain identity?
5. How does it distinguish unknown from false?
6. How does it treat physical law?
7. Does it support interventions/counterfactuals?
8. What memory persists?
9. How does it connect to action?
10. What real capability has been demonstrated?
11. What remains unresolved?
12. What code/data is public?
13. What would falsify its relevance to Clover?

## Current phase boundary

We are **not** yet freezing:
- a final world representation;
- an explicit-vs-latent decision;
- a Transformer-vs-non-Transformer decision;
- an object-vs-field decision;
- a CPU-vs-GPU decision;
- a final licence/authority mechanism.

The next Clover architecture should be a result of this Survey, not a prerequisite for it.

---

**The question is fixed. The answer is open.**

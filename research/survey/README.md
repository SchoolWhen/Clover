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

This Survey is the prior-art and synthesis layer.

It is intentionally flatter than the older `docs/research-map/` structure: a small number of larger Markdown files should let a reader scan the whole research landscape quickly.

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

This Survey incorporates screened material from three internal documents:

### 1. Clover Research Reset — 2026-10-14

Kept:

- highest SSOT;
- product goal;
- "benchmark as instrument" principle;
- V0–V3 vision protocol;
- research map;
- benchmark/task map;
- hardware-as-design-variable principle;
- representation questions;
- model and dataset links.

Not kept as current commitments:

- immediate reproduction schedule;
- any implication that one baseline must be reproduced before research can proceed;
- CPU-first as a scientific prior.

### 2. `news_answers.md`

Kept as candidate research hypotheses:

- Evidence Replay;
- query-conditioned temporal support;
- separation of epistemic state and licence lifecycle;
- proof-carrying auditability;
- counter-witness causality;
- visual/event IR;
- epistemic compute scheduling;
- static/dynamic verification compilation;
- geometry as a proposal heuristic;
- shortcut/leakage audits;
- long-horizon world-change evaluation.

Not kept as SSOT:

- old P0/P1/P2 implementation ordering;
- historical architecture-specific assumptions;
- any old statement that explicit authority is already the final answer.

### 3. `news(5).md`

Used only as a signal archive.

A news item enters this Survey only when at least one of the following exists:

- a primary paper;
- an official model card;
- an official project page;
- an official code repository.

Secondary news and vendor claims remain useful for tracking, but they are not treated as independent scientific evidence.

## Evidence labels

Throughout the Survey:

- **PRIMARY_PAPER** — primary preprint or peer-reviewed paper;
- **OFFICIAL_PROJECT** — official project/model page;
- **OPEN_SOURCE** — public implementation/checkpoint;
- **OFFICIAL_REPORTED_RESULT** — company/lab result without independent reproduction;
- **SURVEY_SIGNAL** — useful trend, not a scientific result by itself;
- **INTERNAL_HYPOTHESIS** — Clover candidate;
- **OPEN** — unresolved;
- **SUPERSEDED** — historical, no longer current.

## Research landscape at a glance

The current landscape can be understood as several different answers to the world-understanding problem.

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

Meta's 2026 mechanistic analysis of video models argues that physical variables can be distributed and hierarchically organized rather than represented as compact classical state variables.

Primary paper: https://arxiv.org/abs/2602.07050  
Official Meta page: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

This is direct counter-evidence against assuming that "understanding" requires explicit compact variables.

### Prediction vs reconstruction vs generation

- V-JEPA 2/2.1: predictive latent representation.
- VGGT/VGGT-Ω: learned geometry and reconstruction.
- Atlas: reconstruction + generation + simulation.
- Cosmos 3: unified reasoning / world generation / action generation.

The unresolved question is not "which architecture is newest?" but:

> **Which learning objective produces the state most useful for persistent understanding and action?**

### Observation vs interaction

V-JEPA 2 demonstrates broad learning from passive web video and then adds comparatively little robot interaction data for action-conditioned planning.

Figure and Skild report large gains from human/robot experience scaling.

Open question:

> **What information about causality, controllability and affordance is fundamentally unavailable from passive observation?**

### World state vs direct policy

Gemini Robotics ER 2 explicitly separates embodied reasoning from low-level execution, while systems such as π0.5, Helix 2.5 and S1 show strong end-to-end or foundation-policy behavior.

Open question:

> **What measurable capability is gained by a persistent world state that a sufficiently strong policy cannot obtain implicitly?**

### Visual truth vs plausible generation

Generative world models can produce coherent rollouts, but plausible video is not identical to a correct world state.

This distinction is central for Clover.

## Current survey objective

The Survey is considered sufficiently mature only when we can answer, for each major route:

1. What representation does it assume?
2. What information is learned vs engineered?
3. How does it treat space?
4. How does it treat time?
5. How does it maintain identity?
6. How does it distinguish unknown from false?
7. How does it treat physical law?
8. Does it support interventions/counterfactuals?
9. What memory persists?
10. How does it connect to action?
11. What real capability has been demonstrated?
12. What remains unresolved?
13. What code/data is public?
14. What would falsify its relevance to Clover?

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

# Clover Survey

Last updated: 2026-10-14  
Phase: **Survey / Research Foundation**

This directory is the compact, high-density research entry point for Clover.

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Product target:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

## Why this Survey exists

The 2026-10-14 Research Reset changed the order of work:

```text
research question
→ prior art
→ capability map
→ unresolved contradiction
→ representation hypothesis
→ implementation
→ evaluation
```

rather than building a mechanism first and then searching for evidence to defend it.

The Survey is intentionally flat: a small number of larger Markdown files should let a reader understand the research landscape quickly.

## Reading order

1. [`../../SSOT.md`](../../SSOT.md)
2. [`FRONTIER_METHODS.md`](FRONTIER_METHODS.md)
3. [`RESEARCH_QUESTIONS.md`](RESEARCH_QUESTIONS.md)
4. [`PAPERS.md`](PAPERS.md)
5. [`BENCHMARKS_TASKS.md`](BENCHMARKS_TASKS.md)
6. [`DATASETS_CODE.md`](DATASETS_CODE.md)
7. [`CLOVER_HYPOTHESES.md`](CLOVER_HYPOTHESES.md)
8. [`FRONTIER_SIGNALS.md`](FRONTIER_SIGNALS.md)

## Source screening

This Survey incorporates screened material from three internal sources.

### Research Reset 2026-10-14
Kept: SSOT/product goal, benchmark-as-instrument, V0–V3 vision protocol, research/evaluation map, hardware-as-design-variable and representation questions. CPU-first and pre-reset mechanisms are not current scientific commitments.

### `news_answers.md`
Kept as candidate hypotheses: Evidence Replay, query-conditioned temporal persistence, epistemic/verification separation, auditability/provenance, counter-witness causality, sparse visual IR, compute scheduling, state-transition affordance and active perception. Old implementation-priority labels are not SSOT.

### `news(5).md`
Used as a signal archive only. Durable research entries require a primary paper, official project/model card or official code. Funding/secondary/vendor reports remain signals unless stronger evidence is available.

## Evidence labels

- `PRIMARY_PAPER`
- `OFFICIAL_PROJECT`
- `OPEN_SOURCE`
- `OFFICIAL_REPORTED_RESULT`
- `SURVEY_SIGNAL`
- `INTERNAL_HYPOTHESIS`
- `OPEN`
- `SUPERSEDED`

## Research landscape at a glance

| Route | Typical internal state | Strength | Unresolved issue |
|---|---|---|---|
| Classical geometry / SLAM | explicit pose/map/geometry | precision, observability | semantics, abstraction |
| Static SSL vision | distributed features | broad invariance | weak dynamics/memory |
| Predictive video representation | temporal latent | motion, anticipation | persistent state/interpretability |
| Geometry foundation model | learned 3D state | spatial reconstruction | semantics, physics, causality |
| Object-centric model | slots/entities | composition, identity | object assumptions/scaling |
| Generative world model | latent simulator | rollout/world completion | plausibility vs truth |
| Embodied VLM | multimodal context | flexible reasoning | language priors, persistence |
| VLA / WAM | action-conditioned latent | direct task performance | world semantics, failure attribution |
| Robot foundation policy | broad learned policy | transfer / real behavior | internal representation unclear |
| Model-based robotics | explicit belief/dynamics | uncertainty/planning | representation acquisition |
| Historical Clover | explicit candidate world/authority | queryability hypothesis | not established as best representation |

## Strongest current tensions

- **Explicit vs distributed:** physical variables can emerge in distributed/hierarchical representation: https://arxiv.org/abs/2602.07050
- **Prediction vs reconstruction vs generation:** V-JEPA, VGGT/Ω, Atlas and Cosmos optimize different forms of world structure.
- **Observation vs interaction:** passive video learns substantial dynamics; robot interaction adds controllability/action consequences.
- **World state vs direct policy:** explicit world representations must prove measurable value beyond strong VLA/foundation policies.
- **Visual truth vs plausible generation:** underdetermined hidden completion must not be confused with observed state.

## Survey maturity criteria

For every major route, we should know its representation, learning signal, space/time treatment, identity/persistence, observability, physics/causality, memory, action interface, demonstrated capability, unresolved failures, public resources and meaningful falsifiers.

## Current phase boundary

We are **not** yet freezing a final world representation, explicit-vs-latent decision, Transformer-vs-non-Transformer choice, object-vs-field ontology, CPU-vs-GPU allocation or final authority mechanism.

The next Clover architecture should be a result of the Survey.

---

**The question is fixed. The answer is open.**

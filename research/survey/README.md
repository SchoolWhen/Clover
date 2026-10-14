# Clover Survey

Last updated: 2026-10-14  
Phase: **Survey / Research Foundation**

This is Clover's compact, high-density research entry point.

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Product target:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

## Read in this order
1. [`../../SSOT.md`](../../SSOT.md)
2. [`FRONTIER_METHODS.md`](FRONTIER_METHODS.md)
3. [`RESEARCH_QUESTIONS.md`](RESEARCH_QUESTIONS.md)
4. [`PAPERS.md`](PAPERS.md)
5. [`BENCHMARKS_TASKS.md`](BENCHMARKS_TASKS.md)
6. [`DATASETS_CODE.md`](DATASETS_CODE.md)
7. [`CLOVER_HYPOTHESES.md`](CLOVER_HYPOTHESES.md)
8. [`FRONTIER_SIGNALS.md`](FRONTIER_SIGNALS.md)

## Research order

```text
research question
→ prior art
→ capability map
→ unresolved contradiction
→ representation hypothesis
→ implementation
→ evaluation
```

## Source screening

**Research Reset:** SSOT/product goal, benchmark-as-instrument, V0–V3 protocol, research/evaluation map and hardware-as-design-variable are current. CPU-first and old mechanisms are not axioms.

**`news_answers.md`:** durable candidate ideas were retained as hypotheses, including Evidence Replay, temporal persistence, epistemic/verification separation, auditability, counter-witness causality, sparse IR, compute scheduling, state-transition affordance and active perception.

**`news(5).md`:** used as a signal archive; durable entries require primary/official technical sources. Funding and secondary reporting remain signals.

## Evidence labels
`PRIMARY_PAPER` · `OFFICIAL_PROJECT` · `OPEN_SOURCE` · `OFFICIAL_REPORTED_RESULT` · `SURVEY_SIGNAL` · `INTERNAL_HYPOTHESIS` · `OPEN` · `SUPERSEDED`

## Landscape

| Route | State | Strength | Open issue |
|---|---|---|---|
| Classical geometry | pose/map/geometry | precision/observability | semantics/abstraction |
| Static SSL vision | distributed features | invariance | dynamics/memory |
| Predictive video | temporal latent | anticipation | persistent state |
| Learned geometry | 3D state | spatial reconstruction | physics/causality |
| Object-centric | slots/entities | composition/identity | ontology/scaling |
| Generative world model | simulator latent | rollout/completion | plausibility vs truth |
| Embodied VLM | multimodal context | flexible reasoning | language priors |
| VLA/WAM | action-conditioned latent | task performance | world semantics |
| Robot foundation policy | broad policy | transfer | internal state unclear |
| Model-based robotics | belief/dynamics | uncertainty/planning | representation acquisition |
| Historical Clover | explicit candidate world | queryability hypothesis | not established as best |

## Current tensions
- explicit vs distributed representation;
- prediction vs reconstruction vs generation;
- passive observation vs interaction;
- persistent world state vs strong direct policy;
- evidence-supported truth vs plausible generated completion.

## Phase boundary

We are **not** freezing a final representation, explicit-vs-latent decision, Transformer choice, object-vs-field ontology, CPU/GPU allocation or final authority mechanism yet.

The next Clover architecture should be a result of this Survey.

---

**The question is fixed. The answer is open.**

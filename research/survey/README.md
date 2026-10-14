# Clover Survey

Last updated: 2026-10-14  
Phase: **Survey / Research Foundation**

This directory is the compact, high-density research entry point for Clover.

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Product target:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

## Reading order

1. [`../../SSOT.md`](../../SSOT.md)
2. [`FRONTIER_METHODS.md`](FRONTIER_METHODS.md)
3. [`RESEARCH_QUESTIONS.md`](RESEARCH_QUESTIONS.md)
4. [`PAPERS.md`](PAPERS.md)
5. [`BENCHMARKS_TASKS.md`](BENCHMARKS_TASKS.md)
6. [`DATASETS_CODE.md`](DATASETS_CODE.md)
7. [`CLOVER_HYPOTHESES.md`](CLOVER_HYPOTHESES.md)
8. [`FRONTIER_SIGNALS.md`](FRONTIER_SIGNALS.md)

## Research order

The 2026-10-14 Research Reset established:

```text
research question
→ prior art
→ capability map
→ unresolved contradiction
→ representation hypothesis
→ implementation
→ evaluation
```

rather than building a mechanism first and searching for evidence afterward.

## Screened source policy

This Survey synthesizes three internal source documents rather than uploading them raw.

**Research Reset:** kept the SSOT/product goal, benchmark-as-instrument principle, V0–V3 protocol, research/evaluation map and hardware-as-design-variable stance. CPU-first and old mechanisms are not current axioms.

**`news_answers.md`:** retained durable candidate hypotheses such as Evidence Replay, temporal persistence, epistemic/verification separation, auditability/provenance, counter-witness causality, sparse IR, compute scheduling, state-transition affordance and active perception. Historical implementation-priority labels are not SSOT.

**`news(5).md`:** used as a signal archive. A durable research entry should have a primary paper, official model card/project page or official code. Funding/secondary reports remain signals, not scientific facts.

## Evidence labels

`PRIMARY_PAPER` · `OFFICIAL_PROJECT` · `OPEN_SOURCE` · `OFFICIAL_REPORTED_RESULT` · `SURVEY_SIGNAL` · `INTERNAL_HYPOTHESIS` · `OPEN` · `SUPERSEDED`

## Landscape at a glance

| Route | Typical state | Strength | Open issue |
|---|---|---|---|
| Classical geometry | explicit pose/map | precision/observability | semantics/abstraction |
| Static SSL vision | distributed features | broad invariance | time/memory |
| Predictive video | temporal latent | motion/anticipation | persistent state |
| Learned geometry | depth/pose/point maps | scalable spatial state | physics/causality |
| Object-centric | slots/entities | composition/identity | ontology/scaling |
| Generative world model | latent simulator | rollout/completion | plausibility vs truth |
| Embodied VLM | multimodal context | flexible reasoning | language priors/persistence |
| VLA/WAM | action-conditioned latent | task performance | state semantics/failure attribution |
| Robot foundation policy | broad policy | transfer/real behavior | internal world structure unclear |
| Model-based robotics | explicit belief/dynamics | uncertainty/planning | representation acquisition |
| Historical Clover | explicit candidate world | queryability hypothesis | not established as best representation |

## Strongest current tensions

- **Explicit vs distributed:** https://arxiv.org/abs/2602.07050
- **Prediction vs reconstruction vs generation:** V-JEPA vs VGGT/Ω vs Atlas/Cosmos.
- **Observation vs interaction:** what causal/controllability information requires acting?
- **World state vs direct policy:** what measurable value does a persistent worldview add?
- **Visual truth vs plausible generation:** what is evidence-supported vs imagined?

## Current phase boundary

We are **not** yet freezing a final representation, explicit-vs-latent decision, Transformer choice, object-vs-field ontology, CPU/GPU allocation or final verification/authority mechanism.

The next Clover architecture should be a result of this Survey.

---

**The question is fixed. The answer is open.**

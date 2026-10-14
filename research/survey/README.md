# Clover Survey

Last updated: 2026-10-14  
Phase: **Background Research / Problem Reconstruction**

This is Clover's primary research entry point.

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

The current task is **not** to freeze a new Clover architecture. It is to make the background research deep enough that future representation choices are constrained by prior art, strong baselines, discriminating evaluations and known failure modes.

## Read in this order

1. [`../../SSOT.md`](../../SSOT.md)
2. [`RESEARCH_OVERVIEW.md`](RESEARCH_OVERVIEW.md) — visual map from research question → domains → contradictions → baselines → battery → Failure Matrix
3. [`BACKGROUND_RESEARCH.md`](BACKGROUND_RESEARCH.md) — problem formulation and full research-domain synthesis
4. [`../dossiers/README.md`](../dossiers/README.md) — eight deep domain research dossiers
5. [`SOURCE_MAP.md`](SOURCE_MAP.md) — one-to-one evidence/URL/claim/landing map
6. [`FRONTIER_METHODS.md`](FRONTIER_METHODS.md) — method-family comparison
7. [`RESEARCH_QUESTIONS.md`](RESEARCH_QUESTIONS.md) — unresolved contradictions
8. [`PAPERS.md`](PAPERS.md) — curated primary papers, official pages and code
9. [`BENCHMARKS_TASKS.md`](BENCHMARKS_TASKS.md) — capability/evaluation map
10. [`DATASETS_CODE.md`](DATASETS_CODE.md) — datasets, repositories and implementation resources
11. [`CLOVER_HYPOTHESES.md`](CLOVER_HYPOTHESES.md) — screened historical/internal hypotheses, not commitments
12. [`FRONTIER_SIGNALS.md`](FRONTIER_SIGNALS.md) — filtered frontier/news signals

## Deep research dossiers

The broad Survey is now decomposed into eight domain-level dossiers:

- [`R-A Observability / Epistemology`](../dossiers/R-A-observability-epistemology.md)
- [`R-B Geometry`](../dossiers/R-B-geometry.md)
- [`R-C Representation`](../dossiers/R-C-representation.md)
- [`R-D Memory / Persistence`](../dossiers/R-D-memory-persistence.md)
- [`R-E Physics`](../dossiers/R-E-physics.md)
- [`R-F Causality / Interaction`](../dossiers/R-F-causality-interaction.md)
- [`R-G World Model ↔ Action`](../dossiers/R-G-world-action.md)
- [`R-H Active Perception / Lifelong`](../dossiers/R-H-active-perception-lifelong.md)

Each dossier uses the same discipline:

```text
fundamental question
→ canonical foundations
→ current frontier
→ exact URLs
→ demonstrated capability
→ limitation / confound
→ unresolved contradiction
→ baseline
→ discriminating experiment
→ kill condition
→ Clover implication
```

## Research order

```text
fixed research question
→ background research / research map
→ baseline setup
→ Understanding Battery
→ Failure Matrix
→ representation hypothesis
→ world formation / learning
→ robot brain
→ real-world evaluation
→ hardware co-design
```

Do not invert this sequence by choosing a preferred representation first and then searching for evidence to justify it.

## Source screening

### Research Reset

Current and controlling:

- research question and long-term goal;
- benchmark-as-instrument principle;
- V0–V3 vision protocols;
- research/evaluation map;
- hardware as a design variable;
- strong baseline + capability map + benchmark battery before a new representation hypothesis.

Not axioms:

- CPU-first;
- field crystallization;
- CSP / SEP / licence;
- LCPS / GCPS;
- explicit state;
- latent state;
- Transformer / non-Transformer choice.

### `news_answers.md`

Use as a screened hypothesis/experiment ledger. Durable ideas such as Evidence Replay, query-conditioned temporal support, epistemic/verification separation, auditability, counter-witness causality, sparse visual IR, compute scheduling and active perception remain **candidate hypotheses or diagnostics** unless the post-reset research process promotes them.

### `news(5).md`

Use as a signal/archive layer. News reports and secondary summaries do not become project truth. Graduate durable entries to the Survey only after locating primary papers, official technical reports, official project pages or open code.

## Evidence labels

`PRIMARY_PAPER` · `OFFICIAL_PROJECT` · `OPEN_SOURCE` · `OFFICIAL_REPORTED_RESULT` · `BACKGROUND_REFERENCE` · `SURVEY_SIGNAL` · `INTERNAL_HYPOTHESIS` · `OPEN` · `SUPERSEDED`

## Two-axis “vision alone” annotation

The Survey keeps the established **observation protocol**:

- `V0` monocular RGB + temporal order;
- `V1` V0 + camera intrinsics;
- `V2` calibrated multi-camera RGB;
- `V3` embodied active vision where action changes future visual evidence.

Background research additionally annotates **learning-evidence provenance** when material:

- `L0` visual self-supervision only;
- `L1` visual labels/annotations;
- `L2` language/world-knowledge supervision;
- `L3` action-conditioned robot/human experience;
- `L4` non-visual or privileged physical evidence.

This prevents “visual at deployment” from being confused with “learned only from vision.” See [`BACKGROUND_RESEARCH.md`](BACKGROUND_RESEARCH.md).

## Current landscape

| Route | Typical state | Demonstrated strength | Core open issue |
|---|---|---|---|
| Classical geometry | explicit pose/map/geometry | metric structure, localization, observability | semantics/abstraction/physics |
| Static SSL vision | distributed image features | invariance, dense features, depth/parts | persistent time/world state |
| Predictive video | temporal predictive latent | anticipation, temporal consistency, planning demos | persistent state/causal identifiability |
| Learned geometry | learned 3D/spatiotemporal state | reconstruction, cameras, depth, tracks | memory/physics/action sufficiency |
| Object-centric | slots/entities/tracks | composition, identity bias | scaling/open-world discovery |
| Persistent memory | evidence/world/episodic memory | long-horizon recall/permanence | retention/revision architecture |
| Generative world model | generative spatial/temporal latent | completion, reconstruction, simulation | plausible ≠ evidence-grounded truth |
| Embodied VLM | multimodal context | broad physical/spatial reasoning | language-prior confound, persistent state unclear |
| VLA/WAM | action-conditioned latent/policy | direct task behavior, future-aware control | world semantics and factorization unclear |
| Robot foundation policy | broad implicit policy | real-world transfer and long-horizon behavior | internal world state often opaque |
| POMDP / active perception | belief + dynamics + action | uncertainty-aware information gathering/planning | representation acquisition at scale |
| Historical Clover | explicit candidate world | queryability/auditability hypotheses | no evidence it is the best representation |

## Current primary contradictions

```text
explicit state vs distributed latent vs hybrid
reconstruction vs prediction vs generation
object-centric vs dense scene representation
passive observation vs interaction
persistent world state vs long context/direct policy
evidence-grounded belief vs plausible completion
```

These contradictions are more fundamental than historical Clover module names.

## Current phase exit condition

Background research is mature enough to begin systematic baseline reconstruction when we can answer, with primary evidence:

1. what major research families represent internally;
2. what each family has actually demonstrated;
3. what information each training regime uses;
4. which capabilities remain unresolved across families;
5. which claims are vulnerable to shortcut, language, simulator or sensor confounds;
6. which baselines can discriminate the major contradictions;
7. what the Understanding Battery must measure;
8. which failure dimensions must be recorded before proposing a new representation.

Systematic representation design remains downstream of **baseline setup → Understanding Battery → Failure Matrix**.

---

**The question is fixed. The answer is open.**

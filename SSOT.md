<a id="top"></a>

# Research contract

Maintained: **2026-10-25**. Current progress is maintained in [`STATUS.md`](STATUS.md).

<a id="topic-ssot"></a>
<a id="topic-docs-research-question"></a>

## Fixed question

> **How can a machine understand the real world through vision alone?**

This is Clover's highest scientific authority. The question is fixed; the answer is open.

The target is an embodied computational system that maintains and uses knowledge across time. The real world includes persistent entities outside the current view, incomplete observations, physical interactions, unfamiliar objects/environments and consequences of action. Controlled synthetic environments can isolate mechanisms; the scientific target extends to real environments.

<a id="topic-docs-product-goal"></a>

## Long-term product goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

The intended functional loop is visual experience → world understanding → decision → capability/tool selection → execution → new visual experience. This describes responsibilities, not a frozen network or module topology. Candidate decomposition and authority mechanisms live in [`04-innovation/README.md`](04-innovation/README.md#topic-docs-architecture-readme).

<a id="topic-docs-what-is-understanding"></a>

## Working definition of understanding

The definition remains a research object. Required capabilities include:

- **Existence, identity and persistence:** associate observations across time; preserve or deliberately suspend beliefs through occlusion; do not equate unseen with absent.
- **Spatial and temporal structure:** positions, containment, support, visibility, relations and change at task-relevant precision and timescales.
- **Dynamics and physics:** recognize plausible, quantitatively meaningful changes and violations, with appropriate uncertainty.
- **Causality and counterfactuals:** distinguish correlations, interventions, action consequences and alternatives.
- **Open-world epistemics:** distinguish observed, inferred, predicted, hypothetical/generated, ambiguous, unobserved, contradicted, refuted and model-incomplete state.
- **Memory and revision:** preserve long-horizon evidence and identity, and revise earlier beliefs after contradictory observations.
- **Generalization:** remain useful across new objects, scenes, cameras, dynamics, compositions and embodiments.
- **Active evidence acquisition:** obtain missing visual evidence when doing so is informative, permitted and worth its cost.
- **Decision usefulness:** improve planning, execution, recovery or action, eventually in unfamiliar real environments.

No single capability or benchmark establishes the whole definition.

## Independent evidence dimensions

| Axis | Required evidence |
|---|---|
| U — Understanding | Identity, persistence, space, time, observability, physics and causality |
| G — Generalization | New objects, scenes, cameras, dynamics, compositions and embodiments |
| P — Prediction | What will, could, cannot and would happen under intervention |
| A — Action usefulness | Decision, planning, execution and recovery value |
| R — Real-world transfer | Controlled settings through unfamiliar real environments |
| E — Efficiency | Latency, memory, energy, bandwidth and hardware once capability is established |

These axes do not substitute for each other. Benchmark SOTA is evidence about a defined protocol, not the project objective or proof of world understanding.

## Vision protocols and learning provenance

Observation protocol and learning evidence are independent labels. Record both for the exact experiment.

| Protocol | Permitted observation evidence |
|---|---|
| V0 | Monocular RGB frames plus temporal order/timestamps |
| V1 | V0 plus declared camera intrinsics |
| V2 | Calibrated multi-camera RGB |
| V3 | Embodied active vision: actions change future visual observations; sensory evidence remains visual |

Depth, LiDAR, tactile, force, IMU, ground-truth poses/identities and privileged simulator state are not silently counted as RGB vision. Posed images from one moving camera do not automatically become physical multi-camera V2; declare the actual capture/calibration conditions. Action commands used as conditioning must be recorded separately from sensory measurements.

| Learning label | Evidence used to acquire knowledge |
|---|---|
| L0 | Visual self-supervision |
| L1 | Visual labels/annotations |
| L2 | Language/world-knowledge supervision |
| L3 | Action-conditioned demonstrations or interaction experience |
| L4 | Non-visual/privileged physical evidence: proprioception, force/tactile, IMU, depth/LiDAR, measured physical priors or simulator state |

A deployed RGB model trained with language, actions, measured material priors or privileged state is not scientifically equivalent to V0/L0. Record privileged evidence used by the examiner separately from information used by the learner. Task instructions and question text also belong in the input record.

<a id="topic-principles"></a>

## Research principles

1. **Protect the question, not an old answer.** CPU-first, field crystallization, visual charge, CSP/SEP, licence envelopes, LCPS/GCPS, Visual World Compiler, Evidence Replay, explicit/latent/object-centric state, geometry, fields, Transformers and vendor backbones are candidate answers or resources.
2. **Evidence before commitment.** Compare the strongest explanations before freezing a representation, backbone, objective or training recipe. Historical Clover ideas may be revised, rejected or removed when evidence changes.
3. **Research before innovation.** Broad Research → method Analysis → comparative Synthesis → demonstrated unresolved gap → original hypothesis and falsifier → Implementation → Evaluation → Reflection. [`PROCESS.md`](PROCESS.md) defines the seven stages. Small diagnostics are allowed earlier only when needed to answer a research question.
4. **No framework stacking.** For an external method, record the problem, demonstrated/undemonstrated capability, mechanism, input/training provenance, observation assumptions, resources and competing explanation before considering adoption.
5. **Benchmarks are instruments.** Use shortcut-resistant, persistent/streaming, causal, active-vision, real-transfer and embodied evidence to distinguish claims; never redefine understanding around the easiest score.
6. **Facts and hypotheses stay separate.** Distinguish implemented, tested, validated, externally reported, hypothesized, planned, open and superseded. Source records retain exact URLs, check dates and reading depth.
7. **Mechanisms need falsifiers.** A name, analogy, implementation effort or appealing mathematical form is not evidence. State a discriminating prediction, counter-hypothesis and kill condition.
8. **Real capability must matter for action.** A representation should eventually show measurable decision, planning, recovery or execution value in unfamiliar physical environments.
9. **Hardware is a design variable.** Apple M4 is a local development reference, not the scientific constraint or assumed final robot computer. CPU, GPU, Metal, MPS and other accelerators are resources selected for the computation.
10. **Keep code and records inspectable.** Avoid hidden state, duplicated authority and unnecessary complexity. Preserve prior versions and refutation history in Git; keep the current reading tree minimal.
11. **Efficiency must preserve capability.** State the complete measurement boundary and capability changes under compression, quantization, sampling or asynchronous execution. Do not substitute cached inference or compute proxies for camera-to-action timing.
12. **The answer remains open.** Explicit, distributed, hybrid or as-yet-unknown representations are admissible. Adopt mechanisms only from discriminating evidence.

## Current operating posture

[`STATUS.md`](STATUS.md) is the only progress/stage authority; dated audit recommendations and directory creation do not advance the project automatically. The numbered stage directories own their current material and templates; this scientific contract applies throughout the lifecycle.

Read [`01-research/README.md`](01-research/README.md), then the relevant canonical topic and [`01-research/sources-and-resources.md`](01-research/sources-and-resources.md). Findings update those documents in place. Candidate Clover mechanisms remain in [`04-innovation/README.md`](04-innovation/README.md) until comparisons, prior-art checks and experiments justify promotion.

<a id="topic-docs-glossary"></a>

## Glossary


Definitions are **working definitions** unless marked otherwise.

- **Worldview** — the system responsible for forming and updating claims about the world from visual evidence.
- **World State** — the machine-readable state used to answer world queries at a given time.
- **Understanding** — the collection of capabilities described in `SSOT.md`; not synonymous with benchmark accuracy.
- **Evidence** — observation-derived information that can support or challenge a world claim.
- **Belief** — a current internal proposition or state supported to some degree by evidence.
- **Primitive** — a minimal representational element from which larger world structures may be composed.
- **Entity** — a persistent individuated structure in the represented world.
- **Identity** — continuity relation linking observations/entity state through time.
- **Type** — an abstraction grouping entities by relevant shared structure, behavior or dynamics.
- **Relation** — a structured dependency between entities, regions or states.
- **Dynamics** — rules or learned regularities governing change through time.
- **Causality** — structure connecting interventions or events to changes beyond mere correlation.
- **Observability** — whether evidence sufficient for a particular assertion is available from the current visual history.
- **Unknown** — an observed or represented question whose value cannot currently be determined.
- **Unobserved** — a region/state lacking sufficient visual observation; not equivalent to free or absent.
- **Licence** — a Clover candidate hypothesis for a machine-verifiable envelope granting authority to an assertion. Its final role remains under investigation.
- **Decision** — conversion of goals plus available world information and uncertainty into desired state changes/subgoals; a licence envelope is an optional hypothesis.
- **Tool Use** — selection of capabilities to realize desired state changes.
- **Execution** — closed-loop realization of a selected capability in the environment.

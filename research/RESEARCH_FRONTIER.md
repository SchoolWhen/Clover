# Stage 1 — Research Frontier Watch

Last updated: **2026-10-14**  
Freshness cutoff checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This file is a **thin current-edge index**. It is not a second survey and it does not make Clover design decisions.

Stable concepts belong in the Stage-1 topic files and source maps. Add a source here only when it materially changes what a new agent should know **now**.

## Evidence labels

- `PRIMARY_PAPER`
- `OFFICIAL_PROJECT`
- `OPEN_SOURCE`
- `OFFICIAL_REPORTED_RESULT`

---

## 1. Current frontier snapshot

| Date | Source | Evidence | Why it matters now | Does **not** prove | Stage-1 landing |
|---|---|---|---|---|---|
| 2026-10-13 | LIBERO-RIG — https://arxiv.org/abs/2610.18843 | `PRIMARY_PAPER` | holds tasks fixed while perturbing camera mounting/calibration, actuation gain, control rate, proprioception, base/table geometry and gripper setup; exposes hardware/setup fragility distinct from scene/task generalization | one benchmark covers all real hardware drift or simulator rig perturbations predict target-robot reliability | engineering validation · embodiment robustness · fault injection |
| 2026-10-13 | DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630 | `PRIMARY_PAPER` | separates RGB geometry from contact/friction properties calibrated by action-response; predicts executable physical consequences | passive RGB identifies friction/contact generally | physical properties · identifiability · model discovery |
| 2026-10-13 | Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/ | `OFFICIAL_REPORTED_RESULT` | strong general multimodal reasoner/tool-user spanning physical reasoning, Real2Sim and robot workflows | vision-only learning or persistent world state is sufficient/necessary | frontier comparator · general reasoner counter-hypothesis |
| 2026-10-13 | Mobility-Budget-Constrained Semantic Exploration — https://arxiv.org/abs/2610.17562 | `PRIMARY_PAPER` | explicit uncertainty/information gain remains a strong structured active-perception baseline | large learned world models are unnecessary in general | value of information |
| 2026-10-12 | Artisan — https://arxiv.org/abs/2610.13947 | `PRIMARY_PAPER` | evaluates articulation, collision, gravity stability, mass/material and function, not only appearance | passive RGB recovers physical parameters | physical properties · functional correctness |
| 2026-10-11 | SpecWM / World Modeling through Spectral Alignment — https://arxiv.org/abs/2610.15429 | `PRIMARY_PAPER` | explicitly controls what a latent representation preserves; kernel choice changes recoverable physical variables and planning behavior | one kernel/representation is universally sufficient | sufficient state · adaptive abstraction · aliasing |
| 2026-10-08 | Mental-Models for Multi-Agent Systems — https://arxiv.org/abs/2610.12453 · code https://github.com/hananshafi/Mental-Models | `PRIMARY_PAPER` / `OPEN_SOURCE` | explicit first/second-order partner-state representations improve multi-agent reasoning | mental state is visually identifiable or infinite recursive belief is needed | open-world epistemics · model discovery |
| 2026-10-08 | HWAM — https://arxiv.org/abs/2610.12026 | `PRIMARY_PAPER` | explicitly predicts realized post-execution body state, exposing commanded-action vs realized-state gap | explicit state is generally superior to latent state | embodiment · WAM · sufficient state |
| 2026-10-08 | Being-M0.7 — https://arxiv.org/abs/2610.11283 | `PRIMARY_PAPER` | strong latent visual-motion world-action route transferring human experience to humanoid control | latent future representations are open-world sufficient | WAM comparator |
| 2026-10-07 | RobotWorld — https://arxiv.org/abs/2610.10409 | `PRIMARY_PAPER` | exposes composition, retained task-state, recovery and completion-verification failures even when useful subroutines exist | one missing module explains system failure | systems integration · persistent state |
| 2026-10-04 | Identifiable World Models — https://arxiv.org/abs/2610.07028 | `PRIMARY_PAPER` | hybrid route: strong distributed representation + identifiable dynamical coordinates | assumptions hold for arbitrary real video or identified coordinates are planning-sufficient | identifiability · representation |
| 2026-10-03 | Video2World — https://arxiv.org/abs/2610.04432 | `PRIMARY_PAPER` | separates geometric/dynamic/functional correctness from visual similarity in reconstructed worlds | simulator reconstruction equals internal world understanding | functional equivalence · executability |
| 2026-09 | PointCast — https://arxiv.org/abs/2609.28393 | `PRIMARY_PAPER` | identity-bearing point state spans rigid, articulated, cloth and rope regimes | one representation already solves cross-material physics | world-state variables · deformables |
| 2026-09 | WROP — https://arxiv.org/abs/2609.28654 | `PRIMARY_PAPER` | directly trains object permanence/solidity priors | synthetic cognitive curriculum guarantees real-world permanence | persistence · memory |
| 2026-09 | Splat-CBF — https://arxiv.org/abs/2609.23100 | `PRIMARY_PAPER` | makes information gain compete with hard safety constraints during next-best-view control | maximum information gain is a safe policy | value of information · epistemic safety |
| 2026-09 | HEARTH — https://arxiv.org/abs/2609.23418 | `PRIMARY_PAPER` | temperature-aware RGB/thermal/3D manipulation exposes visible-spectrum hidden-state boundary | RGB determines temperature | physical properties · hidden state |
| 2026-09 | WorldContact — https://arxiv.org/abs/2609.19600 | `PRIMARY_PAPER` | contact-centric dynamics for deformable manipulation | RGB uniquely identifies contact/material parameters | contact · deformables |
| 2026-09 | PersistBench — https://arxiv.org/abs/2609.20819 | `PRIMARY_PAPER` | distinguishes current visibility from object permanence outside FOV | persistence alone yields general world understanding | memory · belief |
| 2026-09 | Riemann-1.0 — https://arxiv.org/abs/2608.27033 | `PRIMARY_PAPER` | unified causal sequence modeling observations, robot state and actions at large data scale | causal autoregression equals explicit causal identification | WAM counter-hypothesis |
| 2026-08 | ViTacPhys — https://arxiv.org/abs/2608.21355 | `PRIMARY_PAPER` | mass/friction/stiffness estimates help action, while relying on visual+tactile demonstrations | those properties came from vision alone | provenance · physical properties |
| 2026-08 | Embodiment Gap survey — https://arxiv.org/abs/2608.18433 | `PRIMARY_PAPER` | clarifies what still requires embodiment-specific adaptation | one universal action/state interface already exists | self/embodiment model |
| 2026-08 | Active Perception for Embodied Disambiguation — https://arxiv.org/abs/2608.13605 | `PRIMARY_PAPER` | ambiguity resolution through evidence-seeking interaction is becoming explicit | active perception alone solves persistent world modeling | value of information |
| 2026-08 | Unknown Unknowns: Model Misspecification in ML for Physics — https://arxiv.org/abs/2608.13633 | `PRIMARY_PAPER` | makes model-class misspecification / unknown-unknown detection a first-class scientific issue | one uncertainty score can certify model correctness | open-world epistemics · model discovery |
| 2026-08 | R4DSG — https://arxiv.org/abs/2608.11017 | `PRIMARY_PAPER` | RGB-only relative 4D scene-graph memory for persistent objects and long-term changes | relative scene graphs are a universal memory solution | memory · dynamic-world revision |
| 2026-07 | HUME — https://arxiv.org/abs/2607.06501 · code https://github.com/threefruits/HUME | `PRIMARY_PAPER` / `OPEN_SOURCE` | operationalizes hypothesis generation, verification, rejection and model expansion in open-world robot planning | its language-generated symbolic ontology is machine-ground truth | open-world epistemics · model discovery |
| 2026-07 | CG-World — https://arxiv.org/abs/2607.26452 | `PRIMARY_PAPER` | structured world-state/intervention/counterfactual branches with explicit physics/contact metadata | privileged synthetic state is available from real RGB | causal evaluation · intervention data |
| 2026-07 | OASIS-Map — https://arxiv.org/abs/2607.14899 | `PRIMARY_PAPER` | multi-session appeared/disappeared/moved/replaced-object revision | remembering old state is enough when world changes | belief revision |
| 2026-07 | Xiaomi-Robotics-U0 — https://arxiv.org/abs/2607.11643 | `PRIMARY_PAPER` | world foundation model used as generator, transfer mechanism and data engine | data-generation utility equals epistemic fidelity | world-model role taxonomy |
| 2026-06 | Qwen-RobotWorld — https://arxiv.org/abs/2606.17030 | `PRIMARY_PAPER` | language can serve as shared action abstraction for future-world generation across embodiments | language is a sufficient physical action representation | WAM / interface comparator |
| 2026-06 | CausalPhys — https://arxiv.org/abs/2606.05966 | `PRIMARY_PAPER` | physical reasoning benchmark includes intervention and explicit causal graphs | VQA success equals embodied causal competence | causal evaluation |
| 2026-06 | ATOM-CBF — https://proceedings.mlr.press/v331/yun26a.html | `PRIMARY_PAPER` | learned perception uncertainty changes safe-control conservatism under OOD input | uncertainty calibration alone solves open-world model mismatch | epistemic safety |
| 2026-06 | Learning Task-Sufficient World Models — https://proceedings.mlr.press/v306/feng26aa.html | `PRIMARY_PAPER` | closes active probing ↔ task-relevant latent-factor discovery ↔ compact state loop | task-sufficient representation is general-purpose/open-world sufficient | sufficient state · value of information |
| 2026-06 | SAGE — https://arxiv.org/abs/2606.31478 · code https://github.com/JieMaMagic/SAGE | `PRIMARY_PAPER` / `OPEN_SOURCE` | multiple working hypotheses + evidence-grounded failure attribution + grounded reporting | research-agent architecture transfers directly to robotic world models | model discovery · refutation memory |
| 2026-06 | Socratic autonomous scientific discovery — https://arxiv.org/abs/2606.26722 | `PRIMARY_PAPER` | real physical closed-loop hypothesis criticism, falsification criteria and experiment revision | same mechanism solves open-world robot vision | model discovery |
| 2026-06 | Intervention-only causal discovery — https://proceedings.mlr.press/v337/mazaheri26b.html | `PRIMARY_PAPER` | interventions can identify structure even when observational faithfulness fails, under stated assumptions | unrestricted real-world causal structure is identifiable | causal/mechanism discovery |
| 2026-06 | Recursive ToM — https://arxiv.org/abs/2606.11724 | `PRIMARY_PAPER` | explicit nested perspectives help higher-order belief reasoning | deep recursive beliefs are always needed in robotics | social hidden state |
| 2026-05 | What-If World — https://arxiv.org/abs/2605.27589 | `PRIMARY_PAPER` | paired physical interventions test whether generated futures change causally, not merely plausibly | generated counterfactual correctness implies executable world model | intervention evaluation |
| 2026-05 | CRONOS — https://arxiv.org/abs/2605.23699 | `PRIMARY_PAPER` | tests physical invariance under controlled viewpoint/scene/category/appearance changes | nuisance invariance alone implies causal understanding | anti-shortcut physics |
| 2026-05 | Constrained Bayesian Experimental Design — https://proceedings.mlr.press/v306/guo26g.html | `PRIMARY_PAPER` | sequential experiment design under changing costs/physical constraints | expected information gain alone is enough | model discovery · value of information |
| 2026-05 | Robust BOED under misspecification — https://proceedings.mlr.press/v300/tang26d.html | `PRIMARY_PAPER` | informative experiments can amplify errors when the model is wrong; representativeness/de-amplification matter | maximally informative probe is always best | model discovery · epistemic safety |
| 2026-04 | RoboWM-Bench — https://arxiv.org/abs/2604.19092 | `PRIMARY_PAPER` | generated video plausibility can fail when converted to embodied execution | video realism equals executable physics | world-model evaluation |
| current open baseline | GR00T N1.7 — https://github.com/NVIDIA/Isaac-GR00T | `OPEN_SOURCE` | strong reproducible direct-policy/VLA comparator | direct policy removes need to study world state | baseline comparator |

---

## 2. What changed in the comparison space

The current frontier strengthens these distinctions:

```text
pixels
≠
world state

visual plausibility
≠
physical correctness
≠
functional correctness
≠
executability

statistical predictability
≠
physical identifiability

state uncertainty
≠
parameter uncertainty
≠
model-structure uncertainty
≠
hypothesis-set incompleteness

prediction error
≠
automatically bad state estimate;
it may indicate observation corruption,
representation failure,
regime change,
or model-class misspecification

active exploration
≠
scientific experiment design

maximum information gain
≠
best probe under misspecification / risk / cost / irreversibility

current best hypothesis
≠
permanent truth

reflection
≠
falsification

compact task-sufficient state
≠
open-world sufficient state

strong general reasoner + tools
≠
proof of vision-only world understanding

world model for belief
≠
world simulator
≠
world data engine

scene / task generalization
≠
hardware / calibration / control-loop robustness

model accuracy
≠
runtime reliability
```

---

## 3. Immediate Stage-2 analysis queue

When Stage 2 begins, prioritize methods that discriminate **different scientific hypotheses**, not simply the newest models:

```text
SpecWM
Learning Task-Sufficient World Models
Identifiable World Models
HUME
DR-WM
V-JEPA 2 / 2.1
VGGT / VGGT-Ω
PersistBench + WROP
PointCast
Riemann-1.0
Being-M0.7 vs HWAM
Gemini 4 Argon vs explicit/persistent-state systems
GR00T N1.7 / OpenVLA / π0.5 direct-policy baselines
Video2World + RoboWM-Bench
What-If World / CRONOS / CausalPhys / CG-World
Splat-CBF / active-perception baselines
LIBERO-RIG / deployment-robustness baselines
Mental-Models / recursive-ToM references for social hidden state
```

Suggested comparison axes:

```text
visual protocol
learning provenance
observation/image-formation assumptions
representation/state type
sufficiency target
what information is deliberately preserved
what information is deliberately discarded
state aliasing risk
identifiability assumptions
persistent memory / belief revision
physical-property provenance
causal/intervention semantics
active evidence acquisition
experiment-selection criterion
model misspecification handling
hypothesis provenance/refutation memory
safety / cost / irreversibility / permission
self/embodiment modeling
hardware/setup robustness
runtime latency / jitter / deadline behavior
fault tolerance / recovery
world-model role: belief / simulator / data engine / direct policy
reproducibility
```

---

## 4. Frontier-watch rule

Add a source here only when it materially changes the Stage-1 map.

For every frontier source, preserve:

```text
date
exact primary/official/code URL
evidence level
what it demonstrates
what it does NOT demonstrate
input / training provenance
why it changes the current comparison space
which Stage-1 file owns the stable concept
```

Detailed notes belong in the relevant Stage-1 file, `survey/SOURCE_MAP.md`, or later Stage-2 method reports.

**Do not promote a frontier mechanism directly into Clover Innovation.**
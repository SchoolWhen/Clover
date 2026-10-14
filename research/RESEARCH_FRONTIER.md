# Stage 1 — Research Frontier Watch

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> **Research question:** How can a machine understand the real world through vision alone?

This file is a **thin current-edge index**. It is not a second survey and it does not make Clover design decisions.

As of 2026-10-15, the latest arXiv `cs.RO` batch visible in the daily listing is **Wed, 14 Oct 2026**. Several high-value papers in that batch were submitted on 2026-10-13 UTC. Preserve both the submission date and the day the batch became visible when freshness matters.

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
| 2026-10-13 | WorldOracle — https://arxiv.org/abs/2610.18826 | `PRIMARY_PAPER` | evaluates action-conditioned world models against paired **real-world executions** from the same initial observation and low-level action sequence; measures physical-state correctness, interaction alignment, key interaction regions and multi-view action coherence | high world-model score implies good policy, complete physical understanding, or vision-only learning | world-model evaluation · real-execution grounding · engineering validation |
| 2026-10-13 | RoboSimStudio — https://arxiv.org/abs/2610.18835 · project https://robosimstudio.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | makes solver/contact-model/physical-parameter choices explicit and editable for human- or agent-guided Real2Sim; includes visual, force-feedback and agentic Real2Sim2Real experiments | calibrated simulation is uniquely correct or simulator fit removes the reality gap | engineering validation · Real2Sim · model discovery |
| 2026-10-13 | LIBERO-RIG — https://arxiv.org/abs/2610.18843 | `PRIMARY_PAPER` | holds tasks fixed while perturbing eleven hardware/setup axes with five severity levels; pooled VLA success falls from 0.932 nominal to 0.767 mid-severity and 0.509 highest-severity | one benchmark covers all real hardware drift or simulated perturbations predict target-robot reliability | engineering validation · embodiment robustness · fault injection |
| 2026-10-13 | LoopWAM — https://arxiv.org/abs/2610.18873 · project https://loop-wam.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | learns from successful, suboptimal and failed deployment rollouts instead of discarding failures; reports repeated deployment/training rounds improving RoboChallenge Table30-V2 success from 23.67% to 43.33% | self-improvement is safe, monotonic, or free from deployment-selection bias | WAM · deployment learning · lifecycle / regression |
| 2026-10-13 | ForceWAM — https://arxiv.org/abs/2610.18852 · project https://force-wam.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | decouples task-compatible future prediction from local contact-response learning; combines future video with six-axis wrench trajectories and reports 85–95% mean success on evaluated real contact-rich tasks | contact forces are identifiable from RGB alone or force sensing is unnecessary | contact physics · WAM · provenance boundary |
| 2026-10-13 | RoboFQE — https://arxiv.org/abs/2610.18699 | `PRIMARY_PAPER` | evaluates visual robot policies from offline trajectories without new simulator/real-world rollouts; reports preserved policy rankings even on long-horizon tasks where autoregressive video evaluators degrade | offline evaluation can replace all closed-loop testing or eliminate distribution-shift concerns | engineering validation · offline evaluation · EV4 |
| 2026-10-13 | Grid or Nodes? — https://arxiv.org/abs/2610.18637 | `PRIMARY_PAPER` | directly compares grid memory with an oracle-fed node memory under partial observability; exposes strong memory/compute and motion-generalization trade-offs, including 14 KB vs 5.6 MB in the reported out-of-view comparison | oracle node tracking is a deployable learned solution or one representation wins universally | persistent memory · state abstraction · edge memory cost |
| 2026-10-13 | LADDER — https://arxiv.org/abs/2610.18053 · project https://ladder.insait.ai | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | scales manipulation horizon from 1 to 10 subgoals while holding environment structure controlled; reports low-level-policy success collapsing from 85.4% on one-subgoal tasks to near zero on extended tasks; orchestration improves but remains bounded by execution errors | high-level orchestration alone solves long-horizon robotics | long-horizon evaluation · systems integration · runtime cost |
| 2026-10-13 | GreenWAM — https://arxiv.org/abs/2610.18774 · project https://greenvla.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | unifies world-model and policy roles across a shared anatomical action space and reports real-humanoid adaptation plus single-step distillation for real-time control | one shared action representation is universally sufficient or distillation preserves every world-model capability | WAM comparator · cross-embodiment · edge distillation |
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
| 2026-08 | Unknown Unknowns: Model Misspecification in ML for Physics — https://arxiv.org/abs/2608.13633 | `PRIMARY_PAPER` | makes model-class misspecification / unknown-unknown detection a first-class scientific issue | one uncertainty score can certify model correctness | open-world epistemics · model discovery |
| 2026-07 | HUME — https://arxiv.org/abs/2607.06501 · code https://github.com/threefruits/HUME | `PRIMARY_PAPER` / `OPEN_SOURCE` | operationalizes hypothesis generation, verification, rejection and model expansion in open-world robot planning | its language-generated symbolic ontology is machine-ground truth | open-world epistemics · model discovery |
| 2026-06 | Learning Task-Sufficient World Models — https://proceedings.mlr.press/v306/feng26aa.html | `PRIMARY_PAPER` | closes active probing ↔ task-relevant latent-factor discovery ↔ compact state loop | task-sufficient representation is general-purpose/open-world sufficient | sufficient state · value of information |
| 2026-05 | What-If World — https://arxiv.org/abs/2605.27589 | `PRIMARY_PAPER` | paired physical interventions test whether generated futures change causally, not merely plausibly | generated counterfactual correctness implies executable world model | intervention evaluation |
| 2026-04 | RoboWM-Bench — https://arxiv.org/abs/2604.19092 | `PRIMARY_PAPER` | generated video plausibility can fail when converted to embodied execution | video realism equals executable physics | world-model evaluation |
| current open baseline | GR00T N1.7 — https://github.com/NVIDIA/Isaac-GR00T | `OPEN_SOURCE` | strong reproducible direct-policy/VLA comparator | direct policy removes need to study world state | baseline comparator |

---

## 2. What changed in the comparison space

The 2026-10-15 sweep strengthens these distinctions:

```text
predicted rollout
≠
real executed consequence

simulation fit
≠
validated digital twin

same task + new scene
≠
same task + changed hardware/calibration/control loop

offline policy ranking
≠
closed-loop robot validation

failed deployment rollout
≠
useless training data

future visual prediction
≠
contact-response knowledge

long-horizon planning quality
≠
long-horizon physical execution reliability

grid/dense memory capacity
≠
memory efficiency
≠
out-of-distribution motion generalization

world-model capability
≠
policy capability
≠
capability preserved after real-time distillation
```

Older core distinctions remain active:

```text
pixels ≠ world state
visual plausibility ≠ physical correctness ≠ functional correctness ≠ executability
statistical predictability ≠ physical identifiability
state uncertainty ≠ parameter uncertainty ≠ model-structure uncertainty ≠ hypothesis-set incompleteness
maximum information gain ≠ best probe under misspecification / risk / cost / irreversibility
compact task-sufficient state ≠ open-world sufficient state
world model for belief ≠ world simulator ≠ world data engine
scene/task generalization ≠ hardware/calibration/control-loop robustness
model accuracy ≠ runtime reliability
```

---

## 3. Immediate Stage-2 analysis queue

When Stage 2 begins, prioritize methods/benchmarks that discriminate **different scientific hypotheses**, not simply the newest models:

```text
WorldOracle
RoboSimStudio
LIBERO-RIG
RoboFQE
LADDER
Grid or Nodes?
LoopWAM
ForceWAM
GreenWAM
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
```

Suggested comparison axes:

```text
visual protocol
learning provenance
observation/image-formation assumptions
representation/state type
sufficiency target
what information is deliberately preserved / discarded
state aliasing risk
identifiability assumptions
persistent memory / belief revision
physical-property provenance
causal/intervention semantics
active evidence acquisition
experiment-selection criterion
model misspecification handling
hypothesis provenance/refutation memory
real-execution grounding
hardware/setup robustness
runtime latency / jitter / deadline behavior
memory footprint / state-storage growth
offline-evaluation assumptions
fault tolerance / recovery
simulator / Real2Sim provenance
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

Detailed notes belong in the relevant Stage-1 file, `survey/SOURCE_MAP.md`, `survey/BENCHMARKS_TASKS.md`, engineering support notes, or later Stage-2 method reports.

**Do not promote a frontier mechanism directly into Clover Innovation.**
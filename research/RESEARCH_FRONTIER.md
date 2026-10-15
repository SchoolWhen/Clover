# Stage 1 — Research Frontier Watch

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> **Research question:** How can a machine understand the real world through vision alone?

This file is a **thin current-edge index**. It is not a second survey and it does not make Clover design decisions.

As of 2026-10-15, the latest complete arXiv daily batches visible for the relevant categories include work submitted through **2026-10-13 UTC**, with some records revised on 2026-10-14. Preserve both submission/revision dates and the date Clover checked the source.

Stable concepts belong in the Stage-1 topic files. Fast-moving cross-boundary clusters are also summarized in [`emerging/JEPA_RSI_RUNTIME_2026-10-15.md`](emerging/JEPA_RSI_RUNTIME_2026-10-15.md).

## Evidence labels

- `PRIMARY_PAPER`
- `OFFICIAL_PROJECT`
- `OPEN_SOURCE`
- `OFFICIAL_REPORTED_RESULT`
- `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE`

---

## 1. Current frontier snapshot

| Date | Source | Evidence | Why it matters now | Does **not** prove | Stage-1 landing |
|---|---|---|---|---|---|
| 2026-10-13 / rev. 10-14 | Thinker-WM — https://arxiv.org/abs/2610.18447 · project https://thinkercosmos.ubtrobot.com | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | jointly evolves RGB, metric depth and robot action in a shared dynamics representation; exposes a strong unified-multimodal-state counter-hypothesis | depth/action-supervised training is vision-only, or one shared state is universally sufficient | representation · geometry · WAM · provenance |
| 2026-10-13 | AReaL-RSI — https://arxiv.org/abs/2610.18083 | `PRIMARY_PAPER` | makes recursive improvement a resource-allocation / role-specialization / evidence-sharing problem across persistent research campaigns | more agents automatically yield better or safer self-improvement | foundation-model systems · research automation · RSI evaluation |
| 2026-10-13 | WorldOracle — https://arxiv.org/abs/2610.18826 | `PRIMARY_PAPER` | evaluates action-conditioned world models against paired real executions from the same initial observation and low-level action sequence | world-model score implies good policy or complete physical understanding | world-model evaluation · real-execution grounding |
| 2026-10-13 | RoboSimStudio — https://arxiv.org/abs/2610.18835 · project https://robosimstudio.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | makes solver/contact/physical-parameter choices explicit for iterative Real2Sim and Real2Sim2Real | calibrated simulation is uniquely correct | engineering validation · Real2Sim · model discovery |
| 2026-10-13 | LIBERO-RIG — https://arxiv.org/abs/2610.18843 | `PRIMARY_PAPER` | holds tasks fixed while perturbing hardware/setup axes; separates task generalization from rig robustness | simulated perturbations fully predict target-robot reliability | hardware robustness · fault injection |
| 2026-10-13 | LoopWAM — https://arxiv.org/abs/2610.18873 · project https://loop-wam.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | learns from successful, suboptimal and failed deployment rollouts across repeated deployment/training rounds | self-improvement is safe or monotonic | deployment learning · WAM · lifecycle |
| 2026-10-13 | ForceWAM — https://arxiv.org/abs/2610.18852 · project https://force-wam.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | combines future visual prediction with local six-axis wrench/contact-response learning | contact forces are identifiable from RGB alone | contact physics · WAM · provenance |
| 2026-10-13 | RoboFQE — https://arxiv.org/abs/2610.18699 | `PRIMARY_PAPER` | enables offline visual-policy ranking without new simulator/real rollouts | offline evaluation replaces closed-loop testing | EV4 · offline policy evaluation |
| 2026-10-13 | Grid or Nodes? — https://arxiv.org/abs/2610.18637 | `PRIMARY_PAPER` | exposes representation/memory-cost/OOD-motion trade-offs under partial observability | oracle node tracking is a deployable general solution | persistent memory · edge state cost |
| 2026-10-13 | LADDER — https://arxiv.org/abs/2610.18053 · project https://ladder.insait.ai | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | controlled horizon scaling exposes compounding physical-execution failures | orchestration alone solves long-horizon robotics | long-horizon evaluation · systems integration |
| 2026-10-13 | GreenWAM — https://arxiv.org/abs/2610.18774 · project https://greenvla.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | unifies world/policy roles and distills to a real-time policy | distillation preserves every world-model capability | WAM · cross-embodiment · edge distillation |
| 2026-10-13 | DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630 | `PRIMARY_PAPER` | separates RGB geometry from contact/friction properties calibrated by action-response | passive RGB identifies friction/contact generally | physical properties · identifiability |
| 2026-10-13 | Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/ | `OFFICIAL_REPORTED_RESULT` | strong general multimodal reasoner/tool-user spanning physical reasoning, Real2Sim and robot workflows | vision-only learning or persistent world state is sufficient/necessary | general-reasoner counter-hypothesis |
| 2026-10-12 | MARS — https://arxiv.org/abs/2610.17141 · code https://github.com/PKU-VaLuE-Lab/MARS | `PRIMARY_PAPER` / `OPEN_SOURCE` | training-free WAM acceleration across attention, denoising and cross-query representation reuse with online verification | cached/reused inference state is always valid | runtime systems · WAM acceleration · state staleness |
| 2026-10-12 | Artisan — https://arxiv.org/abs/2610.13947 | `PRIMARY_PAPER` | evaluates articulation, collision, gravity stability, mass/material and function, not only appearance | passive RGB recovers physical parameters | physical properties · functional correctness |
| 2026-10-11 | Δ Flow Matching — https://arxiv.org/abs/2610.15794 | `PRIMARY_PAPER` | replaces fixed Gaussian source with recent-history-conditioned source for VLA/WAM flow matching; makes generative source distribution a training/inference variable | one source prior is universally optimal | training/post-training · runtime efficiency |
| 2026-10-11 | Vision-Predictor-Action — https://arxiv.org/abs/2610.15556 · code https://github.com/ylee-sling/Vision-Predictor-Action | `PRIMARY_PAPER` / `OPEN_SOURCE` | lightweight JEPA predictor + flow action chunk; preliminary Apple-M4 latency evidence makes it relevant to local proxy research | preliminary LIBERO result establishes general embodied intelligence | embodied JEPA · edge proxy |
| 2026-10-11 | SpecWM — https://arxiv.org/abs/2610.15429 | `PRIMARY_PAPER` | explicitly controls what latent representations preserve; kernel choice changes recoverable physical variables/planning | one kernel is universally sufficient | sufficient state · aliasing |
| 2026-10-10 | Harmony Harness — https://arxiv.org/abs/2610.15150 | `PRIMARY_PAPER` | multi-objective harness evolution separates reusable mechanisms from benchmark-specific adaptation | self-evolving harnesses generalize automatically | harness RSI · foundation systems |
| 2026-10-09 | Harness² — https://arxiv.org/abs/2610.14224 | `PRIMARY_PAPER` | studies recursive harness refinement in open-world tasks without ground-truth online verifiers and transfers task-level experience to future harnessing | self-generated evaluation is reliable by default | open-world RSI · evaluator quality |
| 2026-10-08 | Embodied Turing Machines / COAP — https://arxiv.org/abs/2610.12369 | `PRIMARY_PAPER` | strong counter-hypothesis: explicit state + reusable code policy, recursively improved by coding agents, can remove a large model from the runtime loop | code/state dominates VLA/WAM generally or state estimation is solved | explicit state · embodied RSI · systems counter-hypothesis |
| 2026-10-08 | Mental-Models for Multi-Agent Systems — https://arxiv.org/abs/2610.12453 · code https://github.com/hananshafi/Mental-Models | `PRIMARY_PAPER` / `OPEN_SOURCE` | explicit first/second-order partner-state representations improve multi-agent reasoning | mental state is directly visually identifiable | social hidden state |
| 2026-10-08 | HWAM — https://arxiv.org/abs/2610.12026 | `PRIMARY_PAPER` | predicts realized post-execution body state, exposing commanded-action vs realized-state gap | explicit state is universally superior | embodiment · WAM |
| 2026-10-08 | Being-M0.7 — https://arxiv.org/abs/2610.11283 | `PRIMARY_PAPER` | latent visual-motion prior from mixed human data transferred through robot mid-training/action post-training | latent future state is open-world sufficient | humanoid WAM · training provenance |
| 2026-10-07 | RoboJEPA — https://arxiv.org/abs/2610.10515 · code https://github.com/facebookresearch/robo_jepa | `PRIMARY_PAPER` / `OPEN_SOURCE` | 22M→8B action-conditioned latent predictors over frozen V-JEPA 2.1; 12 embodiments; scaling law plus latent MPC/CEM and real Franka deployment | JEPA latents contain every physical variable or scaling eliminates aliasing | embodied JEPA · scaling · latent planning |
| 2026-10-07 | LAC-WM — https://arxiv.org/abs/2610.10846 · project https://lacwm.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | unified learned latent action space improves evaluated cross-embodiment world-model adaptation compared with explicit action labels | one latent action space is universally physically sufficient | cross-embodiment action semantics |
| 2026-10-07 | RSI-Forge — https://arxiv.org/abs/2610.09426 | `PRIMARY_PAPER` | builds executable RSI environments from papers; human experts expose shortcut/faithfulness weaknesses missed by agent judges | automated evaluation is self-validating | RSI environments · evaluator design |
| 2026-10-07 | RSIGym — https://arxiv.org/abs/2610.10310 | `PRIMARY_PAPER` | exposes training/inference/rollout/eval services and separates Data, Harness and Joint improvement tracks | one RSI score proves broad self-improvement | RSI infrastructure · research automation |
| 2026-10-07 | RLHND — https://arxiv.org/abs/2610.09455 | `PRIMARY_PAPER` | repurposes a video diffusion foundation backbone as a clip-level perception representation for hand/contact learning | force/contact was learned from RGB alone | computer vision · generative-backbone-as-perception |
| 2026-10-07 | RobotWorld — https://arxiv.org/abs/2610.10409 | `PRIMARY_PAPER` | exposes composition, task-state retention, recovery and completion-verification failures | one missing component explains system failure | systems integration · persistent state |
| 2026-10-04 | DiVeR — https://arxiv.org/abs/2610.04933 | `PRIMARY_PAPER` | verifier-guided Best-of-N action selection shows deployed VLA performance depends on inference-time candidate/search budget as well as weights | verifier scaling changes the underlying policy representation | test-time VLA scaling · verifier attribution |
| 2026-10-04 | Identifiable World Models — https://arxiv.org/abs/2610.07028 | `PRIMARY_PAPER` | hybrid route: distributed representation + identifiable dynamical coordinates | assumptions hold for arbitrary real video | identifiability · representation |
| 2026-10-03 | Video2World — https://arxiv.org/abs/2610.04432 | `PRIMARY_PAPER` | separates geometric/dynamic/functional correctness from visual similarity | simulator reconstruction equals internal understanding | functional equivalence |
| 2026-10-02 | EVEWorld — https://arxiv.org/abs/2610.03374 | `PRIMARY_PAPER` | process-level instance/evolution supervision targets visually plausible but temporally/physically lazy world predictions | its metric captures all physical errors | physical-process supervision · evaluation |
| 2026-09-30 | EmbodiRSI — https://arxiv.org/abs/2609.38905 | `PRIMARY_PAPER` | real→task-specific-sim→failure-guided data acquisition→policy update→real refinement makes embodied recursive adaptation concrete | embodied RSI is safe, monotonic or universally data-efficient | Real2Sim2Real · post-training · deployment learning |
| 2026-09-28 | RSI-Master — https://arxiv.org/abs/2609.35561 | `PRIMARY_PAPER` | Experiment OS + Worker/Reviewer research DAG targets hacking and strategy lock-in in autonomous post-training R&D | autonomous research is trustworthy without external evaluation | research-agent RSI · experiment provenance |
| 2026-09-28 | WAMachine — https://arxiv.org/abs/2609.34608 | `PRIMARY_PAPER` | adapts retained inference state across replans, denoising and layers; makes stale-computation detection part of real-time WAMs | reuse is harmless under arbitrary distribution shift | WAM runtime · state validity |
| 2026-09-23 | RegenHarness — https://arxiv.org/abs/2609.27612 | `PRIMARY_PAPER` | embodied harness with proposal/execution/verification/commit/recovery separation and versioned evidence-gated updates | one harness revision proves recursive long-term improvement | embodied harness RSI · safety boundary |
| 2026-09-22 | AIDE² / Recursive self-improvement of AI research agents — https://arxiv.org/abs/2609.26457 | `PRIMARY_PAPER` | accepted code rewrites become the next research agent; hidden held-out evaluation and lineage make RSI claims more rigorous | gains guarantee indefinite or safe recursive improvement | research-agent RSI · hidden evaluation |
| 2026-09-21 | RRSI — https://arxiv.org/abs/2609.24972 · code https://github.com/google-research/rrsi | `PRIMARY_PAPER` / `OPEN_SOURCE` | regularizes harness evolution to reduce evolve-set overfitting and considers OOD benchmarks/token cost | harness evolution improves model weights or physical intelligence | harness RSI · generalization |
| 2026-09 | PointCast — https://arxiv.org/abs/2609.28393 | `PRIMARY_PAPER` | identity-bearing point state spans rigid, articulated, cloth and rope regimes | one representation solves cross-material physics | deformables · world state |
| 2026-09 | WROP — https://arxiv.org/abs/2609.28654 | `PRIMARY_PAPER` | trains object permanence/solidity priors | synthetic cognitive curriculum guarantees real-world permanence | persistence · memory |
| 2026-09 | WorldContact — https://arxiv.org/abs/2609.19600 | `PRIMARY_PAPER` | contact-centric dynamics for deformable manipulation | RGB uniquely identifies material/contact parameters | contact · deformables |
| 2026-09 | PersistBench — https://arxiv.org/abs/2609.20819 | `PRIMARY_PAPER` | distinguishes visibility from persistence outside FOV | persistence alone yields general understanding | memory · belief |
| 2026-08 | Unknown Unknowns: Model Misspecification in ML for Physics — https://arxiv.org/abs/2608.13633 | `PRIMARY_PAPER` | makes model-class misspecification a first-class scientific issue | one uncertainty score certifies model correctness | open-world epistemics |
| 2026-07 | HUME — https://arxiv.org/abs/2607.06501 · code https://github.com/threefruits/HUME | `PRIMARY_PAPER` / `OPEN_SOURCE` | hypothesis generation, verification, rejection and model expansion in open-world robot planning | language-generated symbolic ontology is ground truth | model discovery |
| 2026-06 | Learning Task-Sufficient World Models — https://proceedings.mlr.press/v306/feng26aa.html | `PRIMARY_PAPER` | closes active probing ↔ latent-factor discovery ↔ task-sufficient state loop | task-sufficient means open-world sufficient | sufficient state · value of information |
| 2026-05 | What-If World — https://arxiv.org/abs/2605.27589 | `PRIMARY_PAPER` | paired interventions test causal future differences | generated counterfactual correctness implies executable model | intervention evaluation |
| 2026-04 | RoboWM-Bench — https://arxiv.org/abs/2604.19092 | `PRIMARY_PAPER` | plausible generated video can still fail embodied execution | realism equals executable physics | world-model evaluation |
| current open baseline | GR00T N1.7 — https://github.com/NVIDIA/Isaac-GR00T | `OPEN_SOURCE` | strong reproducible direct-policy/VLA comparator | direct policy eliminates need to study world state | baseline comparator |

---

## 2. Open-source / engineering project watch

These projects are useful but should not be promoted to primary scientific evidence without a corresponding primary result.

| Project | Evidence | Useful role | Critical boundary |
|---|---|---|---|
| EmbodiedJev / 行知 — https://github.com/FBddcz/embodied-jev | `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE` | MuJoCo + Franka local workbench, structured/RGB inputs, model comparison, trajectory replay/export, pre-execution checks, macOS/Linux workflow | controller-provided candidates/geometry/safety are not model-learned capability; sim success is not real-robot success |
| AgentRSI — https://github.com/heng526/AgentRSI | `COMMUNITY_RESEARCH_REPOSITORY` | literature/reproduction workspace and append-only ResearchOps records for RSI research | repository organization is not proof of a specific RSI scientific result |

---

## 3. What changed in the comparison space

The current sweep adds these distinctions:

```text
predictive latent world model
≠
pixel-generative world model

JEPA imagination error
≠
complete world-state quality

cross-embodiment state alignment
≠
cross-embodiment action alignment

base VLA
≠
VLA + verifier + Best-of-N test-time compute

inference-state reuse
≠
inference-state validity

fast loop + slow loop
requires
temporal synchronization / stale-guidance semantics

self-evolution
≠
self-improvement

model-weight RSI
≠
harness RSI
≠
data/research-process RSI
≠
embodied deployment RSI

RSI evolve-set gain
≠
held-out/OOD gain

final endpoint score
≠
process-level self-improvement quality

generative video model
≠
only a generator;
it can also provide perception features

multi-camera token concatenation
≠
3D-consistent multi-view representation

explicit state + code policy
≠
learned foundation-model policy
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

## 4. Immediate Stage-2 analysis queue

Prioritize methods that discriminate different hypotheses, not simply the newest names:

```text
RoboJEPA / ThinkJEPA / LeapBot-WA / Demo-JEPA / V-JEPA 2.1
LAC-WM vs explicit action-conditioned world models
DiVeR vs base-policy inference
MARS / WAMachine / Δ-flow / asynchronous WAM execution
AIDE² / RRSI / RSI-Master / RSI-Forge / RSIGym / HELIX / Harmony Harness / Harness² / AReaL-RSI
EmbodiRSI / RegenHarness / Embodied Turing Machines
Thinker-WM / PAIWorld / RLHND / EVEWorld
WorldOracle
RoboSimStudio
LIBERO-RIG
RoboFQE
LADDER
LoopWAM
ForceWAM
GreenWAM
SpecWM
Learning Task-Sufficient World Models
Identifiable World Models
HUME
DR-WM
PersistBench + WROP
PointCast
Riemann-1.0
Being-M0.7 vs HWAM
Gemini 4 Argon vs explicit/persistent-state systems
GR00T N1.7 / OpenVLA / π0.5
Video2World + RoboWM-Bench
What-If World / causal-intervention benchmarks
```

Suggested new comparison axes:

```text
predictive target: pixel / latent / geometry / action / multimodal
visual backbone frozen vs adapted
predictor size / compute scaling
planner: direct / CEM / MPC / verifier/search
cross-embodiment action representation
test-time sampling/search budget
inference-state reuse + refresh criterion
stale-state detection
RSI editable surface
immutable evaluator / safety boundary
held-out evaluation
accepted-change inheritance / lineage
research budget
process-level retention / OOD transfer
```

---

## 5. Frontier-watch rule

For every frontier source preserve:

```text
date
exact primary / official / code URL
evidence level
what it demonstrates
what it does NOT demonstrate
input / training provenance
why it changes the comparison space
stable Stage-1 landing
```

Detailed notes belong in the relevant Stage-1 file, supporting audit, source map, benchmark map, engineering notes, or Stage-2 report.

**Do not promote a frontier mechanism directly into Clover Innovation.**
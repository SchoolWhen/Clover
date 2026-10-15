# Stage-1 Emerging Cross-Boundary Audit — Embodied JEPA, RSI, Runtime and Physical-AI Systems

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This is supporting Stage-1 material. It does **not** add a new project stage and it does **not** promote any current mechanism into Clover Innovation.

The purpose of this audit is to cover several fast-moving 2026 clusters that cut across the existing research map:

```text
latent predictive world modeling / JEPA
cross-embodiment latent action spaces
inference-time policy scaling / verifiers
world-action-model acceleration
recursive self-improvement of agents / harnesses / research systems
embodied recursive improvement
open-source local embodied experimentation
video-foundation-model features used for perception
multi-view / multimodal world-state unification
```

Keep evidence types explicit:

```text
PRIMARY_PAPER
OFFICIAL_PROJECT
OPEN_SOURCE
OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE
COMMUNITY_RESEARCH_REPOSITORY
```

A GitHub project or research workspace is not automatically primary scientific evidence.

---

# 1. Embodied JEPA / latent predictive control is now a distinct method cluster

The earlier Stage-1 map already tracked V-JEPA and predictive latent world models. The 2026 robot literature now justifies treating **action-conditioned JEPA / latent predictive control** as a concrete method family rather than only a generic video-prediction idea.

## 1.1 RoboJEPA — scaling robotic latent world models

Paper: https://arxiv.org/abs/2610.10515  
Official code: https://github.com/facebookresearch/robo_jepa  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

Key reported design:

```text
frozen V-JEPA 2.1 visual encoder
+
action-conditioned latent predictor
+
robot data from 12 embodiments
+
22M → 8B predictor scaling
+
CEM / MPC planning in latent space
```

The official repository releases multiple predictor sizes/checkpoints and deployment code.

Reported scientific signals:

- latent rollout / imagination error follows a compute scaling law in the reported regime;
- downstream planning improves predictably with compute;
- imagination error correlates with planning performance;
- zero-shot goal-image planning is demonstrated in RoboCasa and on a real Franka;
- future video decoding is optional rather than required for control.

What it does **not** establish:

```text
JEPA latent state is open-world sufficient
imagination error is a universal proxy for robot success
frozen V-JEPA preserves every physical variable
12 embodiments solve embodiment generalization generally
scaling to 8B removes state aliasing / uncertainty / causal limitations
```

High-priority Stage-2 question:

> Which information becomes better with predictor scale, and which information is irreversibly absent because the frozen visual representation never encoded it?

---

## 1.2 ThinkJEPA — dense dynamics + slow semantic thinker

Paper: https://arxiv.org/abs/2603.22281  
Code: https://github.com/Hai-chao-Zhang/ThinkJEPA  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

ThinkJEPA explicitly combines:

```text
fast / dense JEPA dynamics pathway
+
slower sparsely sampled VLM semantic pathway
```

This is a direct scientific comparator for Clover's existing fast-state-updater / slow-reasoner question.

Important boundary:

```text
semantic guidance
≠
physical state evidence
```

The VLM branch can inject language/world priors not learned from vision-only physical interaction.

---

## 1.3 Demo-JEPA — demonstration intent as future latent trajectory

Paper: https://arxiv.org/abs/2605.20811  
Evidence: `PRIMARY_PAPER`

Core counter-hypothesis:

```text
cross-embodiment imitation
need not align source actions directly;
visual demonstration can specify a target-compatible future latent trajectory.
```

This is relevant to human-video transfer, sufficient state and cross-embodiment learning.

It does not prove that latent future trajectories capture all contact / force / material constraints required for execution.

---

## 1.4 LeapBot-WA — JEPA as a world anchor

Paper: https://arxiv.org/abs/2607.23969  
Code: https://github.com/LeapWM/leapbot-wa  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

LeapBot-WA moves WAM training away from pixel-level future reconstruction toward predictive latent alignment and prunes the heavy dynamics anchor branch at inference.

This is a useful comparator for:

```text
pixel future generation
vs
latent future prediction
vs
future-state action inference
```

and for the question of whether training-time privileged dynamics structure can be removed without losing action-relevant information at deployment.

---

## 1.5 SkyJEPA — interpretable probes + embedded real-time control

Paper: https://arxiv.org/abs/2606.23444  
Evidence: `PRIMARY_PAPER`

SkyJEPA combines a latent dynamics model with a physics-inspired prober that maps frozen latent state into interpretable physical quantities, then uses sampling-based optimal control for quadrotor control and reports zero-shot sim-to-real experiments.

Research role:

```text
distributed latent
+
interpretable physical probe
+
model-based control
```

is another hybrid route between opaque latent state and fully explicit state.

---

## 1.6 Vision-Predictor-Action (VPA) — small predictive control on Apple M4

Paper: https://arxiv.org/abs/2610.15556  
Code: https://github.com/ylee-sling/Vision-Predictor-Action  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

Reported proof-of-concept configuration:

```text
shared vision encoder
frozen text encoder
JEPA next-latent predictor
skill selector
flow-matching action chunk
<20M trainable parameters
```

The paper reports roughly 10–14 ms per decision step on an Apple M4 for its single-camera reference configuration and 40% success over 200 LIBERO-10 episodes for the reported two-camera policy.

Treat this as **preliminary**, not as evidence that a small JEPA controller already solves general embodied intelligence.

It is nevertheless highly relevant to Clover's Mac-M4 proxy experiments because it demonstrates a tractable low-latency JEPA/action architecture on the project's hardware class.

---

# 2. Cross-embodiment action representation is becoming a first-class world-model variable

## LAC-WM

Paper: https://arxiv.org/abs/2610.10846  
Project: https://lacwm.github.io/  
Evidence: `PRIMARY_PAPER`

LAC-WM learns a shared latent action space across embodiments and compares it against explicit action-conditioned world modeling.

Reported result: explicit action conditioning forms more disjoint representations across embodiments, whereas the learned latent action space improves adaptation to unseen embodiments in the evaluated settings.

Stage-1 implication:

```text
state alignment
and
action alignment
are separate problems.
```

A universal world representation can still fail if action semantics fragment by embodiment.

Do not conclude that one latent action space is universally physically sufficient.

---

# 3. Test-time policy scaling must be separated from base-policy capability

## DiVeR

Paper: https://arxiv.org/abs/2610.04933  
Evidence: `PRIMARY_PAPER`

DiVeR treats a frozen VLA as a stochastic action proposer and trains a lightweight verifier, focusing supervision on sparse decision-critical states identified by dispersion in action-expert representations.

This adds an important system decomposition:

```text
base policy
+
number of sampled action candidates N
+
verifier
+
selection rule
+
inference budget
→ deployed behavior
```

Therefore future Clover evaluations must record test-time sampling / search / verifier budget separately from model weights.

New comparison axis:

```text
training-time scaling
vs
test-time action scaling
```

and:

```text
base-policy success
≠
policy + verifier + Best-of-N success.
```

---

# 4. WAM performance optimization now requires state-staleness semantics

## 4.1 MARS

Paper: https://arxiv.org/abs/2610.17141  
Code: https://github.com/PKU-VaLuE-Lab/MARS  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

MARS profiles and accelerates WAM inference across three sources of redundancy:

```text
attention computation
diffusion / flow denoising
cross-query future-visual representation reuse
```

It uses online verification before speculative reuse.

Stage-1 implication:

> An inference cache is not merely a systems optimization; in closed-loop robotics it has a **validity / staleness condition** tied to new observations and actions.

---

## 4.2 Δ Flow Matching

Paper: https://arxiv.org/abs/2610.15794  
Evidence: `PRIMARY_PAPER`

Instead of generating actions/future states from a fixed Gaussian source, Δ-flow starts from recent history plus mild noise and learns a smaller residual transport.

Reported experiments integrate it into π0.5, ImageWAM and Fast-WAM and show faster training / single-step inference in the evaluated settings.

Research implication:

```text
generative prior / source distribution
```

is a first-class training and inference variable for robot foundation models, not just an implementation detail.

---

## 4.3 WAMachine

Paper: https://arxiv.org/abs/2609.34608  
Evidence: `PRIMARY_PAPER`

WAMachine preserves/adapts intermediate computation across:

```text
closed-loop replans
denoising steps
Transformer layers
```

using trajectory remapping, observation rebinding and residual rescaling, with consistency/probe checks to decide when state must be refreshed.

Important Clover distinction:

```text
reusable inference state
≠
valid inference state
```

Cross-hardware / quantized / asynchronous implementations should measure stale-state failure, not only speed.

---

## 4.4 AsyncVLA and real-time WAM execution

AsyncVLA: https://arxiv.org/abs/2602.13476  
World Action Models in Real Time: https://arxiv.org/abs/2608.01880  
Evidence: `PRIMARY_PAPER`

AsyncVLA explicitly separates a remote >8B semantic policy from a lightweight onboard 76M Edge Adapter and evaluates dynamic communication delays up to six seconds.

The real-time WAM study shows that temporal alignment between observation, predicted chunk and executed action is fundamental; asynchronous execution can fail even when the underlying policy is strong.

Stage-1 implication:

```text
fast model + slow model
```

requires a synchronization / timestamp / stale-guidance model, not only two inference loops.

---

# 5. Recursive self-improvement needs a strict taxonomy

The 2026 RSI literature is growing quickly. Clover should not use “self-improvement” as a single undifferentiated label.

Use at least:

```text
RSI-A  artifact / memory / skill self-evolution
RSI-H  harness / prompt / tools / control-flow self-evolution
RSI-D  data / curriculum / training-recipe self-improvement
RSI-M  model-weight improvement
RSI-R  research-agent / experiment-process improvement
RSI-E  embodied deployment / policy improvement
RSI-J  joint model + harness + data co-evolution
```

Also record:

```text
editable surface
immutable evaluator
train/evolve tasks
hidden held-out tasks
resource budget
accepted-change lineage
rollback mechanism
whether the next cycle actually inherits the accepted change
```

A system is not demonstrated recursively self-improving merely because an agent writes a new prompt once.

---

# 6. Primary RSI references that materially change the map

## 6.1 AIDE² — research agent edits its own code

Paper: https://arxiv.org/abs/2609.26457  
Evidence: `PRIMARY_PAPER`

AIDE² proposes modifications to its own research-agent implementation, evaluates them, and carries accepted rewrites into the next improvement generation. The paper reports an autonomous eight-day run with seven successive improvements and held-out transfer across multiple AI-R&D domains.

High-value methodological lesson:

```text
self-improvement claim
requires
hidden / held-out evaluation
+
accepted-change inheritance
+
lineage
```

---

## 6.2 RRSI — regularize harness evolution against overfitting

Paper: https://arxiv.org/abs/2609.24972  
Code: https://github.com/google-research/rrsi  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

RRSI evolves prompts, control flow, tools, memory and context management around a frozen model while regularizing proposal/selection to reduce benchmark-specific overfitting.

Critical lesson:

```text
ID improvement under evolution tasks
≠
OOD improvement
```

RSI itself needs regularization and held-out generalization tests.

---

## 6.3 RSI-Master — structured autonomous post-training research

Paper: https://arxiv.org/abs/2609.35561  
Evidence: `PRIMARY_PAPER`

RSI-Master provides an Experiment OS plus Worker/Reviewer research DAG to reduce action hacking and strategy lock-in during autonomous post-training research.

Clover relevance is methodological:

```text
experiment traceability
alternative-hypothesis exploration
reviewer/worker separation
persistent research records
```

not evidence for a physical world representation.

---

## 6.4 RSI-Forge — research environment generation is itself a bottleneck

Paper: https://arxiv.org/abs/2610.09426  
Evidence: `PRIMARY_PAPER`

RSI-Forge turns published papers into executable improvement environments. It reports 210 environments over 18 fields, with 90 independently reviewed by domain experts.

Experts are more critical than agent judges about shortcut resistance and source-paper faithfulness.

Stage-1 lesson:

> Self-improvement quality is bounded by the quality of the evaluator/environment; automated judges can overestimate evaluator validity.

---

## 6.5 RSIGym — Data / Harness / Joint improvement tracks

Paper: https://arxiv.org/abs/2610.10310  
Evidence: `PRIMARY_PAPER`

RSIGym exposes training, inference, rollout, evaluation and sandbox services under shared budget/permission controls and explicitly separates:

```text
Data improvement
Harness improvement
Joint improvement
```

This is a useful systems reference for future autonomous Clover experimentation.

---

## 6.6 HELIX — model / harness / data co-evolution

Paper: https://arxiv.org/abs/2608.13951  
Code: https://github.com/HKUDS/HELIX  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

HELIX treats harness evolution as both immediate execution improvement and a source of verified successes, regressions, near misses and alternatives for subsequent model training.

Important loop:

```text
harness change
→ trajectories
→ verified training data
→ model update
→ new harness search
```

This should be kept separate from pure weight-only RSI.

---

## 6.7 Harmony Harness / Harness² — compositional and open-world harness evolution

Harmony Harness: https://arxiv.org/abs/2610.15150  
Harness²: https://arxiv.org/abs/2610.14224  
Evidence: `PRIMARY_PAPER`

Harmony Harness treats harness evolution as multi-objective optimization and separates reusable mechanisms from benchmark-specific adaptations.

Harness² studies recursive harness refinement when open-world tasks lack ground-truth online verifiers and adds a second recursion level that transfers experience from task-specific refinements into a continual improvement harness.

Stage-1 question:

> How should a self-improving system improve under incomplete evaluators without gradually optimizing the evaluator's blind spots?

---

## 6.8 AReaL-RSI — scaling recursive improvement is a resource-allocation problem

Paper: https://arxiv.org/abs/2610.18083  
Evidence: `PRIMARY_PAPER`

Submitted 2026-10-13.

AReaL-RSI organizes a persistent team of research agents, with role specialization, adaptive research orientations, conditional memory sharing and evidence-based review across campaigns.

New Stage-1 axis:

```text
RSI quality
is a function of
search budget + role allocation + memory sharing + evidence validity
```

not merely whether one agent can edit itself.

---

## 6.9 Process-level evaluation of self-evolution

Generalized Agent Iteration: https://arxiv.org/abs/2609.13406  
EvoPathBench / process-level evaluation: https://arxiv.org/abs/2609.24663  
Evidence: `PRIMARY_PAPER`

These works provide useful conceptual/evaluation constraints:

- distinguish whether the improvement mechanism belongs inside the agent;
- distinguish externally grounded evaluation from self-referential evaluation;
- evaluate successive evolution checkpoints, not only final endpoint performance;
- measure retention, OOD transfer and adaptation after unrelated updates.

---

# 7. Embodied RSI is now a real robot-learning subdirection

## 7.1 EmbodiRSI

Paper: https://arxiv.org/abs/2609.38905  
Evidence: `PRIMARY_PAPER`

EmbodiRSI closes a deployment-specific loop:

```text
real deployment scene
→ task-specific simulation
→ policy rollout / failure
→ corrective trajectories + adaptive data collection
→ policy update
→ real refinement
→ next cycle
```

The paper reports two recursive updates improving its scene-balanced simulation success and reports a data-efficient real-world adaptation result in the studied tabletop settings.

This directly links Clover's existing:

```text
Real2Sim2Real
+
failure / recovery data
+
post-training
+
model discovery
+
deployment adaptation
```

Do not generalize its reported gains into a claim that embodied RSI is safe, monotonic or universally data-efficient.

---

## 7.2 RegenHarness — evidence-gated embodied harness changes

Paper: https://arxiv.org/abs/2609.27612  
Evidence: `PRIMARY_PAPER`

RegenHarness separates proposal, execution, verification, commitment and bounded recovery, and allows versioned modifications to context rules, task templates, routing and recovery policies while preventing the agent from weakening its trusted commit gate.

This is a useful embodied reference for:

```text
self-improvement
+
immutable safety / verification boundary
+
versioned rollout / rollback
```

---

## 7.3 Embodied Turing Machines / COAP

Paper: https://arxiv.org/abs/2610.12369  
Evidence: `PRIMARY_PAPER`

This is a strong counter-hypothesis to always keeping a large learned model in the control loop.

COAP proposes:

```text
camera / proprioceptive evidence
→ explicit state
→ reusable code policy
```

and lets coding agents improve the shared code library across tasks.

The reported RoboDojo result is evidence for the evaluated system, not proof that explicit code/state dominates VLA/WAM generally.

Important Clover question:

> Which parts of embodied intelligence should remain learned, and which can be compiled into inspectable stateful code once the relevant state is reliably estimated?

---

# 8. AgentRSI GitHub repository — classify correctly

Repository: https://github.com/heng526/AgentRSI  
Evidence: `COMMUNITY_RESEARCH_REPOSITORY`

The repository describes itself as the canonical P0 repository for a CVPR-RSI research project and contains:

```text
paper translations / extracts
reproduction code and configurations
literature-search records
reading notes
robot scoring reports
ResearchOps protocol
```

Its ResearchOps layer uses append-only outbox records and reducer-owned state / ledgers.

Useful Clover lesson:

```text
research-agent actions
should produce immutable / auditable evidence records
```

But the repository itself is **not** evidence that a particular RSI scientific claim is valid. Use linked primary papers for method claims.

---

# 9. EmbodiedJev / 行知 — useful engineering reference, not a new scientific method

Repository: https://github.com/FBddcz/embodied-jev  
Evidence: `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE`

Current repository capabilities include:

```text
MuJoCo + Franka Panda
rule baseline
local MiniCPM5-2B
cloud/API model adapters
structured state / RGB-D / direct RGB options
external and wrist cameras
short-step and hierarchical action modes
same-task / same-seed multi-model comparison
trajectory replay / JSON export
pre-execution simulation checks
macOS / Linux workflow
```

The project itself explicitly distinguishes controller-generated geometry / candidate logic / safety checks from learned model capability.

Clover use:

```text
EV1 controlled simulation
EV6 local runtime / software HIL
Mac-M4 model comparison
trajectory / experiment provenance
fault / disturbance experiments
candidate-action preflight
```

Do **not** use EmbodiedJev results as evidence that:

```text
a model understands the real world
MuJoCo success transfers to real hardware
controller-provided structure was learned by the model
vendor APIs are comparable without pinning model/runtime/settings
```

It is a useful workbench/reference architecture, not a Clover baseline by default.

---

# 10. Computer-vision boundary: generative video backbones are becoming perception backbones

## RLHND

Paper: https://arxiv.org/abs/2610.09455  
Evidence: `PRIMARY_PAPER`

RLHND repurposes a pretrained Cosmos 3 video diffusion backbone as a deterministic clip-level representation for egocentric hand tracking, then adds a tactile expert for contact/force prediction.

Stage-1 implication:

```text
generative video foundation model
≠ only a generator;
it may also act as a strong motion / interaction representation.
```

But contact/force supervision is not RGB-only physical evidence; preserve provenance.

This suggests an Analysis comparison among:

```text
DINO-style static visual backbone
V-JEPA predictive backbone
video-diffusion backbone used as features
learned geometry backbone
```

under the same physical-state probes.

---

# 11. Multi-view / multimodal world models expose another representation boundary

## Thinker-WM

Paper: https://arxiv.org/abs/2610.18447  
Project: https://thinkercosmos.ubtrobot.com  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

Submitted 2026-10-13 and revised 2026-10-14.

Thinker-WM jointly models:

```text
RGB
metric depth
action
```

through a shared intermediate dynamics Transformer with modality-specific encoders/decoders.

Reported training corpus:

```text
~20K h egocentric video
~10K h real robot
~1K h simulation
~4K h real robot with aligned depth supervision
```

This is a strong counter-hypothesis that geometry, appearance and action should share dynamics parameters.

It does **not** demonstrate L0/L1 vision-only learning because depth and action supervision materially contribute to training.

## PAIWorld

Paper: https://arxiv.org/abs/2606.18375  
Evidence: `PRIMARY_PAPER`

PAIWorld explicitly adds cross-view communication and 3D geometric priors to multi-view world modeling.

Stage-1 implication:

```text
concatenating multiple camera tokens
≠
3D-consistent multi-view world state.
```

This should be tested explicitly under Clover's `V2` protocol.

---

# 12. Physical-process supervision: not only endpoint visual quality

## EVEWorld

Paper: https://arxiv.org/abs/2610.03374  
Evidence: `PRIMARY_PAPER`

EVEWorld argues that world models can exhibit “model laziness”: producing visually plausible output while violating instance-level physical evolution across time.

It introduces process-level temporal/instance supervision and a Model Laziness Rate diagnostic.

Clover relevance:

```text
endpoint appearance
≠
correct physical process
```

This complements WorldOracle / RoboWM-Bench / What-If World and should enter the world-model evaluation cluster.

---

# 13. What this audit adds to Stage 1

No new top-level project stage is needed. The stable Stage-1 map should absorb these as cross-boundary research clusters:

```text
C1 embodied JEPA / latent predictive control
C2 unified latent actions across embodiments
C3 test-time VLA scaling / verifier-guided action selection
C4 inference-state reuse with staleness / verification semantics
C5 recursive model / harness / data / research-system improvement
C6 embodied RSI / Real2Sim2Real self-improvement
C7 process-level self-evolution evaluation
C8 generative video backbones as perception representations
C9 explicit multi-view geometric consistency
C10 stateful code as a counter-hypothesis to always-on foundation models
```

These map into existing Stage-1 surfaces rather than becoming separate lifecycle stages.

---

# 14. New mandatory comparison fields for Stage 2

For relevant methods, record:

```text
predictive target: pixels / latent / geometry / action / multimodal
frozen or adapted visual backbone
latent scale / predictor scale
planning method: direct policy / CEM / MPC / search / verifier
cross-embodiment action representation
inference-time candidate count / verifier budget
inference-state reuse and refresh criterion
stale-state detection
fast/slow path synchronization
editable RSI surface
immutable evaluator / safety boundary
hidden / held-out evaluation
accepted-change inheritance
rollback / lineage
research / training compute budget
whether improvement persists across later cycles
whether model weights, harness, data, or code changed
```

---

# 15. Immediate Stage-2 additions from this audit

High-value clusters:

```text
RoboJEPA
vs ThinkJEPA
vs LeapBot-WA
vs Demo-JEPA
vs V-JEPA 2/2.1

LAC-WM
vs explicit cross-embodiment action conditioning

DiVeR
vs base VLA
vs policy + verifier / Best-of-N

MARS
vs WAMachine
vs Δ-flow
vs asynchronous WAM execution

AIDE²
RRSI
RSI-Master
RSI-Forge
RSIGym
HELIX
Harmony Harness / Harness²
AReaL-RSI

EmbodiRSI
RegenHarness
Embodied Turing Machines / COAP

Thinker-WM
PAIWorld
RLHND
EVEWorld
```

The goal is not to choose winners. The goal is to identify which mechanisms improve:

```text
world-state quality
physical correctness
open-world robustness
real-time execution
adaptation efficiency
research efficiency
```

and which gains come mainly from harness, evaluator, compute budget, privileged evidence or deployment engineering.

---

# Current conclusion

The latest arXiv/GitHub sweep does **not** reveal a missing foundational domain comparable to geometry, causality, memory or deployment.

It does reveal several fast-growing cross-boundary method families that materially change how Clover should analyze modern systems:

> **latent predictive control, test-time verification, stateful inference reuse, recursive improvement, and process-level evaluation now deserve first-class comparison axes.**

Continue Stage-1 freshness updates for these clusters, but keep the primary work moving toward method-by-method Stage-2 Analysis.
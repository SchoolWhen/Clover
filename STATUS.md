# Clover Status

Last updated: **2026-10-15**  
Stage-1 freshness checked through: **2026-10-15**

## Research question

> **How can a machine understand the real world through vision alone?**

## Long-term goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
```

Immediate objective: **coverage before commitment**. No Clover core representation or algorithm is frozen.

## Read first

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)
6. [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md)
7. [`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)
8. [`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md)
9. [`research/RESEARCH_STATE_ALIASING.md`](research/RESEARCH_STATE_ALIASING.md)
10. [`research/RESEARCH_ADAPTIVE_ABSTRACTION.md`](research/RESEARCH_ADAPTIVE_ABSTRACTION.md)
11. [`research/RESEARCH_VALUE_OF_INFORMATION.md`](research/RESEARCH_VALUE_OF_INFORMATION.md)
12. [`research/RESEARCH_OPEN_WORLD_EPISTEMICS.md`](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)
13. [`research/RESEARCH_MODEL_DISCOVERY.md`](research/RESEARCH_MODEL_DISCOVERY.md)
14. [`research/RESEARCH_ENGINEERING_VALIDATION.md`](research/RESEARCH_ENGINEERING_VALIDATION.md)
15. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
16. [`research/README.md`](research/README.md)

Engineering support:

- [`research/engineering/DEPLOYMENT_LIFECYCLE.md`](research/engineering/DEPLOYMENT_LIFECYCLE.md)
- [`research/engineering/VALIDATION_RESOURCES.md`](research/engineering/VALIDATION_RESOURCES.md)

## Current Stage-1 surfaces

```text
1  broad research inventory
2  world-state variables
3  identifiability / information limits
4  observation physics
5  hidden physical properties / irreversible change
6  minimum sufficient world state
7  state aliasing / representation failure
8  adaptive abstraction / state granularity
9  value of information / probing actions
10 open-world epistemics / model mismatch / epistemic safety
11 model discovery / experiment design / falsification / provenance
12 engineering / edge deployment / simulation / validation
13 current frontier
```

## 2026-10-15 final freshness sweep

The latest high-value additions now tracked in Stage 1 include:

### Real-execution world-model evaluation

- **WorldOracle** — https://arxiv.org/abs/2610.18826
  - same initial observation + same low-level action sequence;
  - compare predicted rollout against paired real-world execution;
  - evaluates physical-state correctness, interaction alignment, key interaction regions and multi-view action coherence.

Central distinction:

```text
predicted plausible future
≠
actual executed consequence
```

### Real2Sim / simulation-model revision

- **RoboSimStudio** — https://arxiv.org/abs/2610.18835 · https://robosimstudio.github.io
  - exposes solver, contact model and physical parameters as editable hypotheses;
  - studies visual, force-feedback and agentic Real2Sim2Real refinement.

Central distinction:

```text
simulator calibration
≠
unique identification of real physics
```

### Hardware/setup robustness

- **LIBERO-RIG** — https://arxiv.org/abs/2610.18843
  - 11 hardware/setup perturbation axes;
  - 5 severity levels;
  - 210 conditions across four LIBERO suites;
  - nine evaluated VLAs;
  - reported pooled success: `0.932 → 0.767 → 0.509` from nominal to middle to highest severity.

Central distinction:

```text
scene/task generalization
≠
hardware/calibration/control-loop robustness
```

### Long-horizon reliability

- **LADDER** — https://arxiv.org/abs/2610.18053 · https://ladder.insait.ai
  - 1–10 subgoals;
  - 145 tasks;
  - 8 categories;
  - 2 embodiments;
  - 2,024 simulated episodes per system;
  - reported low-level-policy success drops from 85.4% at one subgoal to near zero on extended tasks.

Central distinction:

```text
local skill competence
≠
long-horizon physical reliability
```

### Offline evaluation without new rollouts

- **RoboFQE** — https://arxiv.org/abs/2610.18699
  - estimates policy return from offline trajectories;
  - reported to preserve policy rankings on simulated/real manipulation, including long horizons where autoregressive video evaluators degrade.

Central distinction:

```text
offline policy evaluation
≠
closed-loop robot validation
```

### Deployment-rollout learning

- **LoopWAM** — https://arxiv.org/abs/2610.18873 · https://loop-wam.github.io
  - learns from successes, suboptimal behavior and failures;
  - reports RoboChallenge Table30-V2 success `23.67% → 43.33%` after three deployment/training rounds;
  - reports shirt-folding `13.20% → 55.56%` after two deployment-driven rounds.

Keep deployment self-training separate from claims of safe or monotonic improvement.

### Contact-rich future / response learning

- **ForceWAM** — https://arxiv.org/abs/2610.18852 · https://force-wam.github.io
  - predicts future video + six-axis wrench trajectories;
  - uses task-agnostic play to learn action/contact response;
  - reports 85–95% mean success on evaluated real tasks and +15–45 percentage points from play data.

This is strong evidence for the utility of contact evidence, not evidence that contact force is available from RGB alone.

### Memory representation / edge cost

- **Grid or Nodes?** — https://arxiv.org/abs/2610.18637
  - reported out-of-view comparison: `14 KB` oracle node memory vs `5.6 MB` FloWM grid;
  - diagonal-motion diagnostic: `93%` tracker vs `11%` FloWM.

Use as a controlled representation/memory-cost diagnostic; the oracle tracker is not a deployable solution.

### Joint world-model / policy / real-time adaptation

- **GreenWAM** — https://arxiv.org/abs/2610.18774 · https://greenvla.github.io
  - shared anatomical action representation across 20 robot families;
  - joint world-model/world-action/policy training;
  - reports real-humanoid adaptation and single-step policy distillation for real-time control.

Central question for later Analysis:

```text
what world-model capability survives policy distillation?
```

## Validation evidence ladder while no target robot exists

```text
EV0 mathematical / synthetic diagnostic
EV1 controlled single-simulator test
EV2 randomized in-simulator robustness
EV3 sim-to-sim transfer
EV4 offline real-data / offline policy evaluation
EV5 real-to-sim / digital-twin validation
EV6 deployment-runtime / compute hardware in the loop
EV7 proxy physical hardware
EV8 target real robot
```

The absence of a current target robot limits claim strength but does not justify weak testing.

## Current local development reference

```text
Mac mini with Apple M4
```

Treat it as a measured development/deployment reference, **not** the final robot computer and not a scientific constraint.

Current practical local paths:

- MLX — https://github.com/ml-explore/mlx
- Apple Core AI / Core ML — https://developer.apple.com/core-ai/ · https://developer.apple.com/documentation/coreml
- ExecuTorch Core ML / MLX backends — https://docs.pytorch.org/executorch/stable/backends/coreml/coreml-overview.html · https://docs.pytorch.org/executorch/stable/backends/mlx/mlx-overview.html
- MuJoCo — https://github.com/google-deepmind/mujoco

Optional remote Linux/NVIDIA path when specifically required:

- Isaac Sim / Isaac Lab;
- large-scale GPU simulation;
- photorealistic sensor generation;
- NVIDIA-specific system-identification workflows.

Do not make Isaac Sim/NVIDIA a mandatory local dependency.

## Current benchmark expansion

[`research/survey/BENCHMARKS_TASKS.md`](research/survey/BENCHMARKS_TASKS.md) now extends the candidate battery through `U20`, adding:

```text
U16 WorldOracle      real-execution world-model fidelity
U17 LIBERO-RIG       hardware/setup robustness
U18 LADDER           long-horizon compounding failure
U19 RoboFQE          rollout-free offline policy evaluation
U20 Grid-or-Nodes    memory efficiency / inductive bias diagnostic
```

U19/U20 are supporting diagnostics; they do not replace real closed-loop evaluation.

## Current engineering distinctions

```text
current development machine
≠ final edge computer
≠ scientific hypothesis

model inference latency
≠ closed-loop latency

peak throughput
≠ sustained real-time performance

quantized benchmark accuracy
≠ preserved uncertainty / memory / persistence

same-simulator robustness
≠ cross-simulator robustness
≠ sim2real transfer

fitted simulator trajectory
≠ validated digital twin

predicted world rollout
≠ real executed consequence

offline policy ranking
≠ closed-loop deployment validation

short-horizon competence
≠ long-horizon reliability

successful deployment self-training
≠ guaranteed safe / monotonic improvement
```

## Current non-goals

We are not currently:

- freezing a final representation;
- implementing a new Clover core architecture;
- choosing explicit vs latent vs hybrid state;
- treating compact state or hierarchy as automatically superior;
- treating information gain as the final control objective;
- treating world-model prediction as ground truth;
- assuming the correct hypothesis/model class is always known;
- designing the science around Mac mini M4;
- claiming sim2real success without real hardware;
- making Isaac Sim/NVIDIA mandatory;
- treating one benchmark as the definition of understanding.

## Remaining collection gaps after the 2026-10-15 sweep

Stage 1 is now broad. The remaining gaps are narrower and should be filled only with strong evidence:

```text
unknown-unknown diagnostics in real embodied environments
nonparametric / open-set mechanism discovery
persistent hypothesis provenance / refutation-memory benchmarks
representation reversibility after compression
self-model ↔ external-world-model coupling
safe exploration under irreversible actions
social permission / consent for probing
correlated uncertainty / model-ensemble collapse
world-model-specific edge benchmarks on NPU/ANE-class hardware
quantization effects on uncertainty / permanence / memory
standardized sim2sim → sim2real predictive correlation
formal persistent-state rollback after model rollback
world-state / memory poisoning benchmarks
robot-world-model shadow/canary deployment protocols
standardized manipulation fault injection across sensor + compute + actuation
energy-aware active perception under edge power budgets
numerical divergence of stateful models across hardware backends
```

## Stage-1 exit condition

Stage 2 Analysis becomes primary only when a new agent can identify:

1. major competing directions and strongest representatives;
2. source/evidence provenance;
3. observation assumptions;
4. world variables represented;
5. identifiability assumptions;
6. sufficiency target;
7. likely state-aliasing failure;
8. abstraction/granularity/timescale assumptions;
9. information-gathering strategy and cost;
10. open-world epistemic failure mode (`E1–E8`) where relevant;
11. hypothesis/model class and falsification assumptions where relevant;
12. deployment/runtime assumptions and hardware constraints;
13. validation evidence level (`EV0–EV8`) and simulator/hardware provenance;
14. datasets/benchmarks that discriminate claims;
15. methods deserving one-method-one-report Analysis.

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, final representation, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, validated sim2real transfer, validated original algorithm, or final hardware mapping.

These remain research targets.

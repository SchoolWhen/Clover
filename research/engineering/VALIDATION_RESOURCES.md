# Engineering / Validation Resources — Current Snapshot

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

Companion to [`../RESEARCH_ENGINEERING_VALIDATION.md`](../RESEARCH_ENGINEERING_VALIDATION.md).

This file is a compact resource table for downstream validation. It is not a Clover architecture proposal.

## Current high-value resources

| Resource | Primary/official URL | What it is useful for | Current quantitative / structural signal | Does **not** establish |
|---|---|---|---|---|
| WorldOracle | https://arxiv.org/abs/2610.18826 | action-conditioned world-model evaluation against paired real executions | evaluates physical-state correctness, spatial interaction alignment, key interaction areas and multi-view coherence over long successful/failed executions | policy quality, universal physical correctness, vision-only learning |
| RoboSimStudio | https://arxiv.org/abs/2610.18835 · https://robosimstudio.github.io | interactive Real2Sim / Real2Sim2Real; explicit solver/contact/parameter hypotheses | supports visual, force-feedback and agentic Real2Sim2Real refinement using an editable physics stack | one calibrated simulator is uniquely correct |
| LIBERO-RIG | https://arxiv.org/abs/2610.18843 | hardware/setup robustness with task semantics held fixed | 11 perturbation axes × 5 severity levels; 210 conditions; pooled success 0.932 nominal → 0.767 mid → 0.509 highest severity across nine VLAs | target-hardware reliability or complete embodiment robustness |
| RoboFQE | https://arxiv.org/abs/2610.18699 | rollout-free offline policy evaluation when new robot/simulator rollouts are costly | preserves policy rankings in reported simulated/real manipulation studies, including long horizons where autoregressive video evaluators degrade | closed-loop safety, real-world transfer, causal validity |
| LADDER | https://arxiv.org/abs/2610.18053 · https://ladder.insait.ai | long-horizon manipulation scaling and compounding-error analysis | 1–10 subgoals; 145 tasks; 8 categories; 2 embodiments; 2,024 simulated episodes/system; low-level success 85.4% at one subgoal → near zero on extended tasks | orchestration alone solves physical execution |
| LoopWAM | https://arxiv.org/abs/2610.18873 · https://loop-wam.github.io | deployment-rollout learning from successful, suboptimal and failed experience | RoboChallenge Table30-V2 success reported 23.67% → 43.33% after three deployment/training rounds; shirt folding 13.20% → 55.56% after two rounds | monotonic/safe self-improvement or immunity to feedback-loop bias |
| ForceWAM | https://arxiv.org/abs/2610.18852 · https://force-wam.github.io | contact-rich WAM with future video + six-axis force/torque prediction and play-data response learning | reported 85–95% mean success on evaluated real tasks; play data adds 15–45 percentage points | RGB-only force/contact identifiability |
| Grid or Nodes? | https://arxiv.org/abs/2610.18637 | memory representation / edge-memory diagnostic under partial observability | reported out-of-view comparison: node memory 14 KB vs FloWM grid 5.6 MB; diagonal-motion detection 93% tracker vs 11% FloWM | oracle node memory is a deployable learned solution |
| GreenWAM | https://arxiv.org/abs/2610.18774 · https://greenvla.github.io | joint world-model/policy role, cross-embodiment action representation and real-time distillation | reports real-humanoid adaptation and a distilled single-step policy for real-time control | distillation preserves all world-model capabilities or one anatomical action space is universal |
| FreeBar | https://arxiv.org/abs/2610.14997 | asynchronous VLA action-chunk alignment under real-time execution | reports +10–15% average success over naive asynchronous execution and >45% lower per-chunk latency than RTC in the evaluated settings | asynchronous execution is solved generally or safety follows from chunk consistency |
| REACT | https://arxiv.org/abs/2610.12007 | rolling denoising and decoupled sensing/encoding/action streaming | reports improved reactivity and smoother execution across RoboTwin 2.0 and multiple real platforms | one streaming schedule is universally optimal |

## How to use these resources with the EV ladder

```text
EV0–EV2
controlled mechanism / simulation robustness

EV3
cross-simulator transfer

EV4
RoboFQE + offline real-data evaluation

EV5
RoboSimStudio / Real2Sim calibration + held-out trajectories

EV6
deployment runtime on Mac M4 or proxy edge compute
+ FreeBar/REACT-style timing stress tests where relevant

EV7
low-cost proxy hardware
+ LIBERO-RIG-inspired setup perturbations

EV8
target robot
+ WorldOracle-style predicted-vs-real consequence comparison
```

## Required claim discipline

Keep these distinctions explicit:

```text
offline policy ranking
≠ closed-loop validation

real2sim fit
≠ uniquely identified real physics

world-model visual quality
≠ real-execution consequence fidelity

one-step / short-horizon success
≠ long-horizon reliability

scene robustness
≠ hardware/setup robustness

real-time distillation
≠ preserved epistemic / memory / causal capability

successful deployment self-training
≠ safe monotonic improvement
```

## Current Mac mini M4 relevance

The present Mac mini M4 can already support meaningful validation work before a target robot exists:

```text
MLX / Core ML profiling
quantization / memory studies
stateful streaming prototypes
MuJoCo diagnostics
fault / latency injection
offline real-video evaluation
RoboFQE-style offline evaluation if the required trajectories are available
```

Remote Linux/NVIDIA compute should be introduced only when a chosen experiment specifically requires Isaac Sim/Isaac Lab or large-scale GPU simulation.

## Remaining validation gaps

Still weakly covered by current literature:

```text
world-model-specific edge benchmark on Apple / NPU-class devices
quantization effects on uncertainty / persistence / state aliasing
standardized sim2sim → sim2real predictive correlation
formal persistent-state rollback after model rollback
world-state / memory poisoning benchmark
shadow/canary deployment protocols for robot world models
standard manipulation fault-injection suite spanning sensor + compute + actuation
energy-aware active perception under real edge power budgets
numerical divergence of stateful world models across hardware backends
```

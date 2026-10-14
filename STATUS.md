# Clover Status

Last updated: 2026-10-14  
Stage-1 freshness checked through: **2026-10-14**

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

Immediate objective: **coverage before commitment**. No new Clover core representation or algorithm is frozen.

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

## Newly strengthened surface: engineering and validation

[`research/RESEARCH_ENGINEERING_VALIDATION.md`](research/RESEARCH_ENGINEERING_VALIDATION.md) now tracks:

```text
edge inference / runtime feasibility
latency / memory / power / thermal behavior
quantization / compression effects
hardware-accelerator mapping
end-to-end camera→state→decision→action timing
simulation fidelity
simulator-specific shortcuts
sim2sim transfer
sim2real / real2sim / real2sim2real
system identification / digital twins
hardware-in-the-loop / proxy hardware
reproducibility metadata
```

Current local development reference:

```text
Mac mini with Apple M4
```

This is a measured development environment, **not** the assumed final robot computer and not a scientific constraint.

Current practical stack references include:

- MLX — https://github.com/ml-explore/mlx
- Apple Core AI / Core ML — https://developer.apple.com/core-ai/ · https://developer.apple.com/documentation/coreml
- ExecuTorch Core ML / MLX backends — https://docs.pytorch.org/executorch/stable/backends/coreml/coreml-overview.html · https://docs.pytorch.org/executorch/stable/backends/mlx/mlx-overview.html
- MuJoCo — https://github.com/google-deepmind/mujoco
- Isaac Sim SysID — https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_robot_setup_sysid.html
- reality-gap survey — https://arxiv.org/abs/2510.20808
- Real-is-Sim — https://arxiv.org/abs/2504.03597

Current Isaac Sim standard requirements do not support macOS/non-NVIDIA hardware, so Isaac/Isaac-Lab should be treated as an optional remote Linux/NVIDIA research path rather than a local project dependency.

## Validation evidence ladder while no target robot exists

```text
EV0 mathematical / synthetic diagnostic
EV1 controlled single-simulator test
EV2 randomized in-simulator robustness
EV3 sim-to-sim transfer
EV4 offline real-data validation
EV5 real-to-sim / digital-twin validation
EV6 deployment-runtime / compute hardware in the loop
EV7 proxy physical hardware
EV8 target real robot
```

Important rule:

```text
sim-only evidence
≠ sim2real evidence
≠ target-robot validation
```

The absence of a current target robot limits claim strength but should not postpone rigorous testing.

## Current engineering distinctions

```text
current development machine
≠ final edge computer
≠ scientific hypothesis

model inference latency
≠ closed-loop latency

peak throughput
≠ sustained real-time performance

average latency
≠ p95 / p99 / deadline behavior

quantized benchmark accuracy
≠ preserved uncertainty / memory / persistence

same-simulator robustness
≠ cross-simulator robustness

fitted simulator trajectory
≠ validated digital twin

cross-simulator success
≠ real-world transfer
```

## Current frontier refresh

[`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md) remains a thin current-edge table rather than a second survey.

Important current additions include SpecWM, DR-WM, Gemini 4 Argon for Robotics, Mental-Models, Identifiable World Models, RobotWorld, Video2World, HUME, Learning Task-Sufficient World Models and robust experimental design under misspecification.

These are research materials and comparators, not Clover components.

## Current non-goals

We are not currently:

- freezing a final representation;
- implementing a new Clover core architecture;
- choosing explicit vs latent vs hybrid state;
- treating compact state as automatically superior;
- treating hierarchy as automatically superior;
- treating information gain as the final control objective;
- treating a world-model prediction as ground truth;
- assuming the correct hypothesis/model class is always known;
- treating language-generated hypotheses as physical truth;
- assuming the robot body/controller/camera is permanently fixed;
- designing the science around Mac mini M4;
- claiming sim2real success without real hardware;
- making Isaac Sim/NVIDIA a mandatory project dependency;
- treating one benchmark as the definition of understanding.

## Remaining collection gaps

Stage 1 still needs stronger primary embodied evidence for:

```text
unknown-unknown diagnostics in real environments
nonparametric / open-set mechanism discovery
persistent hypothesis provenance and refutation-memory benchmarks
slow drift versus abrupt changepoint detection
representation reversibility after compression
self-model ↔ external-world-model coupling
safe exploration under irreversible actions
human-query / escalation cost models
social permission / consent for probing actions
multi-agent recursive belief from embodied observations
correlated uncertainty / model-ensemble collapse
robot-edge runtime benchmarks for streaming world models
quantization effects on calibration / permanence / memory
cross-simulator benchmark standardization
sim2sim-to-sim2real correlation
reality-gap metrics for world models rather than only policies
hardware-in-the-loop benchmarks for learned world models
low-cost proxy-robot validation protocols
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
12. deployment/runtime assumptions and hardware constraints where relevant;
13. validation evidence level (`EV0–EV8`) and simulator/hardware provenance;
14. datasets/benchmarks that discriminate claims;
15. methods deserving one-method-one-report Analysis.

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, a final representation, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, validated sim2real transfer, a validated original algorithm, or a final hardware mapping.

These remain research targets.
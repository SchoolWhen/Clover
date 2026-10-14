# Stage 1 — Engineering, Deployment and Validation Constraints

Last updated: 2026-10-14  
Freshness cutoff checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** constrain Clover to one hardware platform, one simulator, one runtime, or one robot.

Its purpose is to make the downstream engineering and validation problem explicit **before** an algorithm is frozen.

The central questions are:

```text
Can the model run fast enough where the robot actually runs?
What is the real end-to-end latency from camera frame to action/state update?
How much memory, bandwidth, storage and power does it consume?
What accuracy/capability is lost under quantization or compression?
Which operators prevent hardware acceleration?
How do we test without a real robot?
What does simulation prove, and what does it not prove?
How do we distinguish simulator bugs, physics mismatch and model failures?
How should sim-only evidence graduate toward real-world evidence?
```

---

## 1. Hardware is a constraint and research variable — not the scientific answer

Current local development reference for this project:

```text
Mac mini with Apple M4
```

The exact installed RAM/storage configuration should be recorded when performance experiments are run rather than assumed here.

Important distinction:

```text
current development machine
≠
final robot edge computer
≠
scientific hypothesis
```

Clover should remain scientifically portable across CPU/GPU/NPU/ANE-class hardware.

However, deployment constraints can expose scientifically relevant trade-offs:

```text
rich state vs memory
long history vs latency
high-resolution vision vs bandwidth
large world model vs control frequency
generative rollout vs deadline
persistent evidence vs storage
active perception vs energy
```

A representation that cannot satisfy a realistic closed-loop deadline may be scientifically interesting but operationally insufficient for robotics.

---

## 2. Apple-Silicon development / deployment research path

### MLX

Official project: https://github.com/ml-explore/mlx  
Documentation: https://github.com/ml-explore/mlx/blob/main/docs/src/index.rst  
Evidence: `OPEN_SOURCE` / `OFFICIAL_PROJECT`

MLX is designed for Apple silicon and uses unified memory shared between CPU/GPU execution. It supports autodiff, compilation, training/inference and distributed communication.

Relevant Stage-1 questions:

```text
Which Clover operations map efficiently to MLX?
Does persistent state benefit from unified memory?
What becomes bandwidth-bound rather than compute-bound?
Which custom operations require Metal kernels?
How much host↔device orchestration remains?
```

Current distributed reference:
https://github.com/ml-explore/mlx/blob/main/docs/src/usage/distributed.rst

Do not assume distributed Mac execution is required; keep it as a future scaling path.

### Core AI / Core ML

Apple Core AI overview: https://developer.apple.com/core-ai/  
Core ML: https://developer.apple.com/documentation/coreml

Current Apple tooling supports hardware-aware model authoring/profiling, conversion and execution across CPU/GPU/Neural Engine where operations are supported.

Relevant optimization topics:

```text
operator compatibility
compute-unit placement
quantization
palettization
model specialization
cold load / warm load
memory footprint
custom Metal kernels
```

Core AI optimization explicitly supports quantization/palettization:
https://developer.apple.com/core-ai/

Core AI / Core ML profiling:
https://developer.apple.com/documentation/coreai/inspecting-debugging-and-profiling-core-ai-models
https://developer.apple.com/documentation/coreml/analyzing-a-core-ml-models-performance-in-xcode

Important rule:

```text
model FLOPs
≠
actual device latency
```

because unsupported operations, memory traffic, shape specialization, graph partitions and CPU/GPU/ANE placement can dominate runtime.

### ExecuTorch on Apple platforms

Core ML backend:
https://docs.pytorch.org/executorch/stable/backends/coreml/coreml-overview.html

MLX backend:
https://docs.pytorch.org/executorch/stable/backends/mlx/mlx-overview.html

Current MLX delegate status should be treated as evolving/experimental where documented.

Use these as deployment comparators, not assumptions about the final Clover runtime.

---

## 3. Edge-deployment metrics Clover should eventually report

Do not report only average FPS.

For each serious deployment configuration, record:

```text
model / commit
input resolution / context length
precision / quantization
runtime/backend
hardware + RAM
OS/runtime versions
```

### Latency

```text
cold model load
first inference
warm p50 latency
p95 latency
p99 latency
state-update latency
camera→state latency
camera→decision latency
camera→action-command latency
```

Robotics often cares more about worst-tail latency and deadline misses than peak throughput.

### Throughput

```text
frames/s
tokens/s if language/model reasoning is used
simulated worlds/s
state updates/s
planning rollouts/s
```

### Memory

```text
model weights
peak resident memory
persistent world-state memory
KV/cache/history memory
working buffers
raw-evidence storage growth
```

On unified-memory machines, total memory pressure matters even when explicit CPU↔GPU copies are reduced.

### Compression quality

For FP16 / INT8 / INT4 / palettized or pruned variants, report:

```text
memory reduction
latency change
energy/power change where measurable
capability degradation
calibration degradation
state-aliasing increase
rare-event / unknown-state degradation
```

A compressed model that keeps benchmark accuracy but loses uncertainty calibration or persistence is not equivalent.

### Sustained behavior

Benchmark not only short bursts but prolonged runtime:

```text
thermal state
sustained latency
memory growth / leak
cache growth
state drift
long-horizon degradation
```

Apple profiling references:

- Xcode/Core ML performance reports — https://developer.apple.com/documentation/coreml/analyzing-a-core-ml-models-performance-in-xcode
- memory profiling — https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use
- Instruments / performance — https://developer.apple.com/documentation/xcode/performance-and-metrics

---

## 4. Real-time robotics is an end-to-end systems problem

Model inference is only one component.

A future robot loop may include:

```text
camera exposure / sensor readout
→ frame transfer
→ preprocessing
→ perception / representation update
→ memory retrieval
→ world-state update
→ planning / reasoning
→ policy / controller
→ command serialization
→ actuator/controller delay
→ physical response
→ next camera observation
```

Therefore:

```text
model latency
≠
closed-loop latency
```

Eventually measure the full perception-to-action cycle and timing jitter.

Important future systems topics:

- asynchronous sensing and control;
- dropped/late frames;
- timestamp alignment;
- camera/control clock drift;
- state update races;
- stale plans;
- interrupted inference;
- watchdog/failsafe behavior;
- degraded-mode execution;
- logging without blocking the control loop.

These are downstream engineering concerns but can invalidate scientific conclusions if ignored.

---

## 5. We currently do not have a real robot — validation must use a ladder

The absence of a target robot does **not** mean evaluation should be postponed.

It means claims must be tiered by evidence strength.

Suggested research validation ladder:

### EV0 — mathematical / unit / synthetic diagnostic

Test equations, invariances, state-update logic and falsifiers on controlled synthetic examples.

Proves only local mechanism behavior.

### EV1 — single-simulator controlled tasks

Use deterministic scenarios with privileged ground truth.

Useful for:

```text
state identifiability tests
aliasing tests
controlled interventions
counterfactual branches
memory/world-change tests
```

Does not prove transfer.

### EV2 — randomized in-simulator robustness

Randomize:

```text
textures / lighting / camera
mass / friction / damping
geometry / object pose
sensor noise / latency
action noise / controller parameters
```

Purpose: expose brittle simulator-specific solutions.

Domain randomization is a robustness tool, not evidence that the real distribution is covered.

### EV3 — sim-to-sim transfer

Train/calibrate in simulator A, evaluate in simulator B with matched task semantics.

Possible mismatch sources:

```text
contact solver
integration scheme
friction model
collision geometry
rendering / camera pipeline
actuator model
controller timing
```

Cross-simulator survival is stronger than same-simulator generalization because it removes some engine-specific shortcuts.

NVIDIA currently documents sim-to-sim system-identification recovery and explicitly separates parameter recovery from solver parity:
https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_system_identification_simsim.html

### EV4 — offline real-data validation

Before owning a robot, use recorded real-world datasets/video to test:

```text
perception
persistence
world change
physical reasoning
uncertainty
OOD
state reconstruction
```

But offline real video does not validate action consequences or closed-loop control.

### EV5 — real-to-sim / digital-twin validation when any real telemetry becomes available

Use recorded trajectories or measurements to calibrate simulator parameters and hold out trajectories for validation.

System-identification reference:
https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_robot_setup_sysid.html

Real-is-Sim reference:
https://arxiv.org/abs/2504.03597

Important distinction:

```text
fitting simulation to one trajectory
≠
validated digital twin
```

Use held-out trajectories, interventions and task outcomes.

### EV6 — software / compute hardware in the loop

Before a robot is available, run the real deployment runtime on the intended or proxy edge computer while physics/sensors remain simulated.

This can validate:

```text
runtime latency
serialization
ROS / message interfaces
frame timing
memory
watchdogs
real-time scheduling assumptions
```

It does **not** validate real actuator/contact physics.

### EV7 — proxy physical hardware

A low-cost arm/mobile base/camera rig can later provide limited reality-gap measurements before target hardware exists.

Claims must state that embodiment differs from the target.

### EV8 — target real robot

Final transfer / closed-loop real-world evaluation.

Only this tier can support strong target-robot execution claims.

---

## 6. Sim2Sim should be a first-class test, not an afterthought

Why sim2sim matters:

A model can overfit not only a dataset but a **physics engine**.

If a policy/world model fails when the same scenario is moved from one simulator to another, likely causes include:

```text
solver-specific contact
incorrect friction assumptions
rendering shortcuts
state-coordinate assumptions
actuator semantics
hidden simulator metadata
```

A useful protocol is:

```text
same semantic task
same nominal geometry
same initial conditions where possible
same observation protocol
↓
engine A
engine B
↓
compare state/action/outcome divergence
```

Do not require numerical trajectory equality; compare task-relevant and physically meaningful invariants.

Reference example using Isaac Sim → Gazebo → real ROS 2 robot:
https://arxiv.org/abs/2501.02902

---

## 7. Sim2Real, Real2Sim and Real2Sim2Real solve different problems

### Sim2Real

```text
simulation training/testing
→ real deployment
```

Tools include:

```text
domain randomization
domain adaptation
robust policies
system identification
state/action abstraction
sim-real co-training
```

Reality-gap survey:
https://arxiv.org/abs/2510.20808

### Real2Sim

```text
real observations / telemetry
→ calibrated digital/simulation model
```

Useful for identifying where simulator parameters or geometry are wrong.

### Real2Sim2Real

```text
real evidence
→ calibrated/randomized simulator
→ training / analysis
→ real deployment
→ new evidence
→ recalibration
```

This is likely the more realistic long-term workflow for a general robot because the simulator itself should remain revisable.

However:

```text
better simulator fit
≠
correct world model
```

because multiple physical parameter sets can explain the same trajectories.

Keep identifiability analysis from earlier Stage-1 research active here.

---

## 8. Simulator choice under the current Mac mini M4 constraint

### MuJoCo — strong local baseline

Official repository: https://github.com/google-deepmind/mujoco

Current releases provide universal macOS binaries and native Python bindings.

Good local uses:

```text
rigid/contact dynamics
controlled state variables
system identification experiments
model-based control
fast deterministic diagnostics
cross-solver comparison
```

Do not treat MuJoCo rendering/physics as reality.

### ManiSkill — limited Mac path

Official repository: https://github.com/haosulab/ManiSkill
Documentation: https://maniskill.readthedocs.io/

Current documentation emphasizes Linux/NVIDIA for full GPU simulation. Mac support is limited and GPU simulation is not available in the documented support matrix.

Use cloud/Linux GPU environments for serious large-scale ManiSkill experiments if needed.

### NVIDIA Isaac Sim / Isaac Lab — remote/Linux-NVIDIA path

Official requirements:
https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/requirements.html

Current Isaac Sim does not support macOS/non-NVIDIA hardware for its standard workstation/library path.

Therefore do **not** make local Isaac Sim a project prerequisite.

Possible research workflow:

```text
Mac M4
  local model development
  local MuJoCo / synthetic diagnostics
  Apple deployment profiling
       ↓
remote/cloud Linux + NVIDIA only when needed
  Isaac Sim / Isaac Lab
  large-scale GPU simulation
  photorealistic sensor generation
       ↓
cross-simulator evaluation
```

This keeps current hardware from blocking research while avoiding premature infrastructure cost.

---

## 9. Simulation failure taxonomy

When an experiment fails in simulation, classify the failure before blaming the algorithm.

### SF1 — scenario/modeling bug

Wrong units, transforms, collision mesh, camera intrinsics, reset logic, asset scale, etc.

### SF2 — simulator numerical/solver artifact

Timestep, contact solver, penetration, friction discretization, integration instability.

### SF3 — synthetic perception shortcut

Textures, perfect segmentation, deterministic camera, unrealistic lighting, metadata leakage.

### SF4 — actuator/controller mismatch

Command semantics, latency, stiffness/damping, saturation, gear/backlash model.

### SF5 — policy/model overfitting to simulator

Uses engine-specific dynamics or rendering regularities.

### SF6 — genuine algorithmic failure

Failure persists across controlled simulator variations and alternative engines.

### SF7 — reality-gap failure

Works across simulation tests but fails on real data/hardware.

This taxonomy should be used later in Reflection.

---

## 10. Validation should be vector-valued

A future Clover model should not be validated with one scalar score.

Track at least:

```text
scientific capability
prediction / belief quality
uncertainty calibration
state persistence / revision
causal/intervention correctness
closed-loop task success
simulator robustness
sim2sim transfer
real-data generalization
real-time latency
memory footprint
compute utilization
power/thermal behavior
recovery / failure detection
reproducibility
```

This mirrors the Stage-1 principle that benchmarks are instruments, not the definition of understanding.

---

## 11. Reproducibility / systems metadata

Every later experiment should preserve:

```text
Git commit
model checkpoint hash
runtime/backend version
OS version
hardware and memory
simulator version
physics timestep
renderer settings
random seed
assets/version/hash
camera parameters
control frequency
observation/action delay
precision / quantization
benchmark dataset version
```

For simulation experiments additionally preserve:

```text
physics engine
solver settings
collision settings
friction/contact parameters
domain-randomization distributions
privileged simulator state used during training/evaluation
```

Without this metadata, sim2sim and sim2real comparisons can become irreproducible.

---

## 12. Future deployment-ablation matrix

For important Clover candidates, later compare:

```text
full precision vs quantized
full state vs compressed state
all history vs summarized history
CPU vs GPU vs NPU/ANE-capable path
local edge vs remote compute
single-frame vs streaming
cold start vs sustained loop
single simulator vs cross simulator
nominal sim vs randomized sim
sim-only vs offline real data
```

Crucially, do not optimize only speed.

Measure whether acceleration changes the **science**:

```text
Does quantization increase state aliasing?
Does memory pruning damage permanence?
Does lower resolution damage physical identifiability?
Does shorter context break world-change detection?
Does batching increase control latency?
Does asynchronous execution make belief stale?
```

---

## 13. Stage-1 engineering gaps still worth collecting

```text
robot-edge runtime benchmarks for multimodal/world models
ANE/NPU operator-compatibility studies for streaming models
quantization effects on uncertainty/calibration/memory
stateful streaming inference on edge devices
memory-bandwidth-aware world representation
low-power active perception
real-time scheduling for learned world models
cross-simulator benchmark standardization
simulator uncertainty / solver disagreement
sim2sim-to-sim2real correlation
reality-gap metrics for world models rather than only policies
hardware-in-the-loop benchmarks for learned robot world models
low-cost proxy-robot validation protocols
automatic real2sim system identification
sensor/actuator latency randomization
fault injection / degraded hardware testing
reproducible end-to-end camera→action profiling
```

---

## Current rule

Do not design Clover around the Mac mini M4.

Do use the Mac mini M4 as a **measured reference deployment/development environment** now.

Do not claim sim2real success without real hardware.

Do build a validation ladder so that each stage provides stronger evidence than the previous one.

The target is:

```text
scientific mechanism
+
measured runtime feasibility
+
simulation robustness
+
cross-simulator robustness
+
real-data evidence
+
eventual real-robot evidence
```

not any one of those alone.

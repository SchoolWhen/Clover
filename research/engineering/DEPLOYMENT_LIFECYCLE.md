# Stage-1 Supporting Research — Deployment Lifecycle, Fault Injection and Runtime Reliability

Last updated: 2026-10-14  
Freshness cutoff checked through: **2026-10-14**

> Companion to [`../RESEARCH_ENGINEERING_VALIDATION.md`](../RESEARCH_ENGINEERING_VALIDATION.md).

This file studies what happens after a model is scientifically interesting but before it can be trusted as a robot subsystem.

It does **not** propose a Clover architecture.

---

## 1. Deployment profiles should be explicit

Do not report one latency number without saying **where the model is expected to run**.

### DP0 — local research workstation

Current Clover reference:

```text
Mac mini / Apple M4
```

Primary roles:

```text
model development
MLX / Core AI / Core ML profiling
local MuJoCo diagnostics
offline real-video evaluation
quantization / compression studies
stateful streaming prototypes
```

Apple references:

- Core AI — https://developer.apple.com/core-ai/
- Core AI profiling/debugging — https://developer.apple.com/documentation/coreai/inspecting-debugging-and-profiling-core-ai-models
- Core ML Xcode performance report — https://developer.apple.com/documentation/coreml/analyzing-a-core-ml-model-s-performance-in-xcode

Apple's performance tooling can report load/prediction timing and operation placement across CPU/GPU/Neural Engine. Memory and power require separate measurement.

### DP1 — proxy edge compute

Examples:

```text
Apple-silicon device
Jetson Orin-class device
other CPU/GPU/NPU embedded target
```

NVIDIA Orin reference:
https://developer.nvidia.com/sites/default/files/akamai/Jetson_AGX_Orin_Developer_Kit_RG_0.pdf

The purpose is not to choose NVIDIA now. The purpose is to expose portability issues:

```text
unsupported operators
memory-bandwidth dependence
precision dependence
runtime-specific graph partitioning
thermal throttling
power envelope
camera / middleware integration
```

### DP2 — target robot compute

This profile only exists once the actual robot, cameras, controller and compute budget are known.

Rule:

```text
performance on DP0
≠
performance on DP1
≠
performance on DP2
```

---

## 2. Edge feasibility is an end-to-end timing question

A model can be fast in isolation and still be too slow for closed-loop robotics.

Measure:

```text
sensor exposure / readout
capture → memory transfer
preprocessing
representation update
memory retrieval
world-state update
planning / policy
message serialization
controller / actuator delay
```

Report:

```text
p50
p95
p99
maximum / deadline miss rate
jitter
cold start
first inference
sustained latency
```

Do not hide batching delay behind throughput.

### Deployment-oriented edge comparator

**LiteVLA-Edge**  
Primary paper: https://arxiv.org/abs/2603.03380  
Evidence: `PRIMARY_PAPER`

The work targets fully on-device VLA inference on Jetson Orin-class hardware and reports a ROS 2 integrated perception→reasoning→action pipeline. Its importance for Clover is not the specific VLA architecture, but the systems lesson:

```text
model compression
+
runtime choice
+
middleware
+
full-loop timing
```

must be measured together.

It does **not** establish that its latency is sufficient for every robot or that 4-bit quantization preserves persistent-world-model properties.

---

## 3. Fault injection should be part of validation, not an emergency-only test

A later Clover candidate should be evaluated under controlled deployment perturbations.

### FI1 — camera-stream faults

```text
frame drop
bursty frame loss
stale frame reuse
partial image loss
camera disconnect / reconnect
```

### FI2 — image-quality / observation degradation

```text
motion blur
exposure shift
occlusion
compression artifacts
lighting shift
reflection / transparency
```

### FI3 — calibration / rig drift

```text
camera bump
camera remount
intrinsic drift
camera↔robot extrinsic error
base pose change
table / scene geometry offset
```

### FI4 — compute perturbation

```text
inference delay
jitter
CPU/GPU contention
memory pressure
thermal throttling
background process load
```

### FI5 — state / timing faults

```text
out-of-order timestamp
clock drift
stale world state
late memory retrieval
dropped control message
```

### FI6 — actuator / controller perturbation

```text
actuation gain shift
control-rate shift
latency
saturation
backlash / wear
joint / gripper degradation
```

### FI7 — persistent-state corruption

```text
wrong memory write
stale fact retained
incorrect identity merge
malicious / poisoned memory
world-state provenance lost
```

### Current benchmark anchors

**LIBERO-RIG**  
Primary paper: https://arxiv.org/abs/2610.18843  
Evidence: `PRIMARY_PAPER`

This 2026-10-13 benchmark holds LIBERO tasks fixed while perturbing the **hardware/setup** across axes including camera geometry/calibration, actuation gain, control rate, proprioception, base pose, table height and gripper configuration.

Stage-1 lesson:

```text
scene/task generalization
≠
hardware-setup robustness.
```

A model may tolerate visual augmentation while still fail under faults that do not look like image corruptions.

**Bench2Drive-Robust**  
Primary paper: https://arxiv.org/abs/2605.18059  
Open code: https://github.com/Thinklab-SJTU/Bench2Drive-Robust  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

The benchmark injects camera-stream failures, ego-state errors and compute/control delay in a closed loop. It is automotive rather than manipulation, but it is an excellent methodological reference for **deployment perturbation testing**.

**When Sensors Fail**  
Primary paper: https://arxiv.org/abs/2603.04648  
Evidence: `PRIMARY_PAPER`

Studies temporally persistent sensor dropout and observation drift in control. It is useful evidence that robustness to transient image corruptions is not enough when observation failures persist over time.

---

## 4. Runtime monitoring is different from offline evaluation

A system can pass a benchmark and still need a runtime mechanism that detects impending failure.

### Deployment-Time Reliability of Learned Robot Policies

Primary source: https://arxiv.org/abs/2603.11400  
Evidence: `PRIMARY_PAPER`

The work organizes deployment reliability around:

```text
runtime failure monitoring
training-data attribution for diagnosis
long-horizon policy coordination / feasibility
```

Stage-1 implication:

A future Clover deployment should not only predict the world; it should expose signals that allow the system to recognize:

```text
my predicted progress disagrees with observed progress
my action is not producing the expected consequence
I am entering an unfamiliar / failure-prone region
```

### Runtime monitoring questions

Later measure:

```text
failure-detection recall
false alarm rate
detection lead time
recovery success
human-escalation rate
cost of unnecessary stops
```

A monitor that fires only after a collision is not an adequate early-warning system.

---

## 5. Regression testing must include capability regression, not only software correctness

Every new checkpoint can improve one score and silently damage another capability.

A later regression suite should cover:

```text
perception
persistence
belief revision
unknown / abstention
causal intervention
active perception
latency
memory
calibration
sim2sim transfer
recovery
security / provenance
```

For each release candidate preserve:

```text
previous checkpoint
new checkpoint
dataset delta
code delta
runtime delta
simulator delta
hardware delta
metric vector delta
```

### Release statuses worth considering later

```text
research-only
simulation-qualified
real-data-qualified
proxy-hardware-qualified
target-hardware candidate
target-hardware qualified
```

These labels should indicate evidence strength, not marketing maturity.

---

## 6. Rollback should be planned before online adaptation is enabled

Continual/test-time adaptation creates a new risk:

```text
model update improves current regime
but corrupts previously valid capability
```

Before allowing an online model update, a deployment system should eventually define:

```text
update trigger
validation gate
protected capability set
rollback checkpoint
rollback trigger
state / memory migration rule
```

Important research question:

```text
If model weights roll back,
what happens to world memory learned under the newer model?
```

Weight rollback and belief/memory rollback are not automatically the same operation.

---

## 7. Data / checkpoint / experiment provenance should be first-class

A result should be traceable from robot behavior back to the exact evidence and software that produced it.

Preserve where possible:

```text
Git commit
checkpoint hash
training-data manifest + version
preprocessing version
calibration file
simulator + asset versions
randomization distributions
runtime/backend
hardware / firmware
camera configuration
controller parameters
experiment seed
raw episode / video IDs
```

### Generalization should be grounded relative to training data

**RADAR — Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs**  
Primary paper: https://arxiv.org/abs/2603.11426  
Evidence: `PRIMARY_PAPER`

The paper compares evaluation settings directly with training examples to characterize what kind of generalization is actually being tested.

Stage-1 lesson:

```text
unseen benchmark episode
≠
necessarily meaningfully novel experience.
```

A later Clover evaluation should report what is actually novel relative to its training/evidence distribution.

---

## 8. Security and world-state integrity belong in deployment validation

A persistent world model creates attack surfaces that ordinary stateless perception does not have.

### Security of Foundation-Model-Powered Embodied Agents

Primary survey: https://arxiv.org/abs/2608.16843  
Evidence: `PRIMARY_PAPER`

The survey identifies attack surfaces spanning:

```text
model supply chain
user instruction
context / memory
physical semantic environment
multimodal perception
world state
reasoning / planning
action interfaces
middleware
multi-agent communication
execution control
```

It specifically highlights long-term memory, middleware/networking, world-state integrity and multi-agent trust as comparatively underexplored.

### Security of World-Model-Based Embodied AI

Primary survey: https://arxiv.org/abs/2607.28226  
Evidence: `PRIMARY_PAPER`

Important Stage-1 distinction:

```text
world model as safety shield
≠
world model is trustworthy.
```

A corrupted predictive model can create **predictive safety illusions**.

### Persistent-memory poisoning reference

MemSentry: https://arxiv.org/abs/2609.08747

This is not a robotics result, but it is a useful warning that a malicious or low-quality persistent-memory write can affect behavior long after the original observation disappears.

Future Clover security tests should therefore include:

```text
memory-write provenance
state-update authorization
contradictory evidence handling
poisoned observation persistence
rollback / quarantine of suspect memory
```

---

## 9. No real robot yet: use existing robot ecosystems before buying expensive hardware

The absence of hardware should not block data/model experimentation.

### LeRobot

Official documentation: https://huggingface.co/docs/lerobot/index

LeRobot explicitly supports a no-hardware workflow using public robot datasets and simulation benchmarks, while retaining a path to real hardware later.

### SO-101 as a future EV7 proxy option

Official guide: https://huggingface.co/docs/lerobot/en/so101

This low-cost arm is not a final Clover embodiment, but it could later provide:

```text
real camera timing
calibration drift
servo latency
contact / execution instability
real dataset collection
failure/recovery traces
```

without committing to an expensive target robot.

### Existing SO-101 evaluation reference

**Benchmarking Vision-Language-Action Models on SO-101: Failure and Recovery Analysis**  
Primary paper: https://arxiv.org/abs/2606.08881  
Evidence: `PRIMARY_PAPER`

Its useful methodological contribution is failure/recovery analysis on affordable real hardware, not proof that SO-101 should be Clover's target platform.

---

## 10. Hardware robustness and model robustness should not be conflated

A later evaluation matrix should separate:

```text
new scene
new object
new task
new lighting
new camera
new calibration
new controller gain
new control rate
new gripper / wear
new robot embodiment
new runtime/backend
```

These are different generalization axes.

The latest LIBERO-RIG evidence is particularly important because it shows why visual robustness alone cannot cover perturbations that do not manifest as ordinary image changes.

---

## 11. Suggested future Clover deployment test suite

### DT1 — device portability

Run the same frozen model on:

```text
Mac M4 reference
another backend / hardware class
```

Compare numerical behavior, latency and capability vector.

### DT2 — quantization stress

```text
full precision
FP16
INT8
INT4 / palettized where supported
```

Measure not just task score but calibration, persistence and aliasing.

### DT3 — latency injection

Inject controlled:

```text
fixed delay
random jitter
bursty delay
```

into the closed loop.

### DT4 — camera fault suite

Frame drops, camera shifts, calibration error, blur and stale frames.

### DT5 — actuator / controller fault suite

Gain, rate, delay, saturation and unavailable joint/gripper conditions.

### DT6 — world-state integrity

Inject false/stale/poisoned persistent facts and test evidence-based correction.

### DT7 — restart / recovery

Kill/restart runtime processes while preserving or restoring state deliberately. Measure whether the system resumes with valid belief rather than silently stale memory.

### DT8 — checkpoint regression

Run the same fixed episode battery across every serious checkpoint.

### DT9 — cross-simulator / cross-runtime

Move the same task/state definition across simulators or runtimes and identify which failures come from representation versus infrastructure.

---

## 12. Current research gaps

Still worth collecting:

```text
standard robotics fault-injection suites beyond driving
world-model-specific edge benchmarks
persistent-memory corruption benchmarks for embodied systems
robot-model canary/shadow deployment protocols
formal rollback semantics for stateful learned world models
power/energy measurement standards across heterogeneous edge devices
runtime deadline guarantees for learned world models
correlation between sim2sim robustness and eventual sim2real performance
security evaluation with physically realizable long-horizon attacks
hardware-setup robustness across non-manipulation embodiments
```

---

## Current rule

Do not wait for a target robot to begin deployment validation.

Do not interpret simulation as real-world proof.

Do not interpret benchmark success as runtime reliability.

Do not interpret model accuracy as hardware robustness.

A credible future Clover claim should carry both:

```text
scientific evidence level
+
deployment / validation evidence level
```

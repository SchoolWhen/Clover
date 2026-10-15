# Stage-1 Emerging Audit — Remaining CV, Embodiment and Serving Boundaries

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This audit follows [`JEPA_RSI_RUNTIME_2026-10-15.md`](JEPA_RSI_RUNTIME_2026-10-15.md) and asks whether the latest arXiv/GitHub sweep exposes any remaining boundary that the stable Stage-1 map still underweights.

Conclusion: no new top-level lifecycle stage is needed, but the following cross-boundaries should be explicit.

---

# 1. Frame RGB is a design choice, not the definition of all visual sensing

Clover's current scientific protocols `V0–V3` deliberately use RGB. Keep that constraint stable when making Clover claims.

However, adjacent **visual-only sensor families** are useful counterfactuals because they reveal information that frame RGB may discard before learning begins.

## EventCV / event-based robotic vision

Paper: https://arxiv.org/abs/2609.21330  
Project: https://eventcv.net  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

Event cameras provide asynchronous per-pixel brightness-change events at microsecond-scale temporal resolution, with high dynamic range and low power characteristics. EventCV provides a robotics-oriented library with denoising, geometry, feature learning, motion estimation, video-to-event simulation and ONNX inference, and reports Jetson Orin AGX case studies.

Stage-1 role:

```text
frame RGB
vs
event vision
```

is **not** a Clover baseline contest. It is a sensor-information diagnostic.

Questions:

```text
Which fast contact/slip/impact/motion evidence is aliased by ordinary frame sampling?
How much can higher RGB frame rate recover?
What is lost because of exposure / motion blur rather than model architecture?
What information requires a different optical sensor?
```

Important rule:

```text
event-camera result
≠ V0–V3 RGB result
```

Do not silently broaden “vision alone” from RGB to arbitrary visual sensors in Clover claims.

---

# 2. World models can be hardware-locked because body morphology changes dynamics

## Morphology-conditioned quadrupedal world models

Paper: https://arxiv.org/abs/2604.08780  
Evidence: `PRIMARY_PAPER`

The paper studies world models conditioned explicitly on engineering morphology specifications instead of forcing the model to infer static properties such as limb length/mass only from motion history.

It motivates a distinction already implicit in Clover but worth making explicit:

```text
environment dynamics
≠
robot morphology
≠
actuator/controller dynamics
```

and:

```text
world model generalization
≠
embodiment generalization
≠
morphology generalization
```

The authors themselves characterize the method as distribution-bounded within the studied quadruped family, not a universal physics engine.

Stage-1 landing:

- self/body schema;
- embodiment-conditioned state/action semantics;
- adaptive abstraction;
- engineering/hardware robustness;
- system identification.

Future Clover experiment:

> Hold scene/task fixed while changing body geometry or actuator parameters; test whether the world-state representation separates external-world change from embodiment change.

---

# 3. Affordance is becoming a foundation-model target rather than only an auxiliary head

## AFUN — affordance foundation model

Paper: https://arxiv.org/abs/2606.02551  
Project: https://www.zhaoningwang.com/AFUN  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

AFUN predicts both:

```text
where to interact
+
how the object should move after contact
```

from task-conditioned RGB-D input, and aligns heterogeneous robot/human/simulation/scan data into a standardized affordance schema.

Why it matters:

```text
object identity
≠
object geometry
≠
functional affordance
```

and affordance may depend jointly on:

```text
world state
× task
× embodiment
```

rather than being a fixed intrinsic label.

Boundary:

- RGB-D means this is not a strict V0 result;
- language/task conditioning injects semantic priors;
- strong affordance prediction does not prove complete object physics.

This should strengthen Stage-2 analysis of R26 affordance/action-relevant perception.

---

# 4. Test-time adaptation is broader than verifier-guided Best-of-N

## RoboTTT — context compressed into fast weights

Paper: https://arxiv.org/abs/2607.15275  
Project: https://research.nvidia.com/labs/gear/robottt/  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

RoboTTT introduces another answer to the long-context problem:

```text
raw token / KV history
vs
explicit persistent memory
vs
history compressed into adaptive fast weights
```

Its recurrent state is partly represented by model parameters updated through gradient descent during training and inference. The paper reports context scaling to 8K robot timesteps without inference latency growing with context length in its design.

Required Clover questions:

```text
What facts are retained in fast weights?
Can a fact be revised selectively?
How is provenance represented?
Can updates contaminate unrelated skills?
What is rollback semantics?
How does fast-weight memory compare under equal bytes/latency with explicit state + evidence retrieval?
```

This belongs simultaneously to:

- long context vs memory;
- test-time adaptation;
- continual learning;
- stateful rollback;
- post-training / deployment learning.

## RA-VLA — retrieval-augmented test-time adaptation

Paper: https://arxiv.org/abs/2608.25585  
Evidence: `PRIMARY_PAPER`

RA-VLA is a useful counter-hypothesis in which expert context is retrieved and grounded at test time without changing the base policy through conventional fine-tuning.

Keep distinct:

```text
retrieval-conditioned adaptation
≠
fast-weight adaptation
≠
verifier/search scaling
≠
online gradient fine-tuning
```

These methods should not all be reported under the vague label `test-time improvement`.

---

# 5. JEPA/WAM naming itself now requires artifact-level disambiguation

Two different papers submitted on 2026-10-08 use the name **LeWAM**.

## LeWAM A — End-to-End World and Action Modeling with JEPAs

Paper: https://arxiv.org/abs/2610.12818

Core idea:

```text
joint next-latent prediction
+
action flow matching
+
latent-distribution constraint
```

with one model supporting both direct policy execution and sampled-action planning.

## LeWAM B — A JEPA World Action Model with Diffusion-Steering-Based MPC

Paper: https://arxiv.org/abs/2610.12407

Core idea:

```text
bidirectional JEPA dynamics/policy model
+
forward/backward/inverse/policy modes
+
planning in policy-noise space to reduce model exploitation
```

These are scientifically distinct methods despite the shared acronym/name.

Repository rule:

```text
method name alone is never a stable identifier.
```

For every fast-moving method preserve:

```text
exact title
arXiv / DOI id
authors
version/date
code repository
checkpoint/config if relevant
```

This rule is especially important for WAM/VLA/RSI literature where naming collisions and version drift are common.

---

# 6. Video-model continued pretraining is becoming part of WAM design

## Video Prediction Policy 2 (VPP2)

Paper: https://arxiv.org/abs/2610.10270  
Evidence: `PRIMARY_PAPER`

VPP2 attributes WAM failures partly to a base video model not being specialized for manipulation. Its recipe includes:

```text
large-scale manipulation-video continued pretraining
+
event-level video pretraining
+
post-training/distillation into a single-step visual planner
+
Mixture-of-Transformers action module
```

Stage-1 implication:

> The quality of a WAM is not only a function of the action head or world-action objective. The **video foundation model's domain curriculum** can materially determine downstream physical prediction/action quality.

This reinforces Clover's training rule:

```text
backbone architecture
≠
backbone pretraining domain
≠
continued pretraining
≠
action post-training
```

---

# 7. Multi-robot serving / edge-cloud scheduling is different from single-model latency

## Robion — efficient VLA management and serving for robot factories

Paper: https://arxiv.org/abs/2609.12075  
Evidence: `PRIMARY_PAPER`

Robion treats VLA serving under multiple robots/models and safety-relevant service-level objectives (SLOs) as a systems problem. It co-schedules VLM and action-diffusion stages, manages GPU placement and prioritizes requests by remaining SLO budget.

Why this matters for Clover later:

```text
single-robot local latency
≠
shared edge-server latency
≠
fleet SLO reliability
```

A future deployment may choose among:

```text
fully onboard
onboard fast path + remote slow path
shared edge inference
cloud frontier comparator
```

Required metrics:

```text
p50 / p95 / p99 camera→action latency
deadline miss rate
queueing delay
network delay
robot concurrency
model-switch/load cost
fairness / starvation
fallback behavior when server/network is unavailable
```

Throughput alone is insufficient for embodied control.

---

# 8. New boundary taxonomy from this audit

Add these as comparison axes, not lifecycle stages:

```text
B-SENSOR  frame RGB vs adjacent visual sensor evidence
B-BODY    external world vs morphology/body dynamics
B-AFF     object state vs embodiment/task-relative affordance
B-TTA     retrieval vs fast-weight vs verifier/search vs gradient test-time adaptation
B-ID      artifact identity / naming / version disambiguation
B-CURR    generic video pretraining vs manipulation-specialized continued pretraining
B-SERVE   local single-robot vs shared edge/fleet serving
```

---

# 9. Does this reveal a missing foundational domain?

No.

These findings fit existing Stage-1 surfaces:

```text
Observation Physics
State Variables
Adaptive Abstraction / Embodiment
Affordance / Action-Relevant Perception
Foundation Model Systems
Training / Post-Training
Engineering / Deployment
Frontier
```

The important change is analytical discipline: future Stage-2 reports must distinguish sensor information, body morphology, memory mechanism, test-time adaptation type, training curriculum and serving topology instead of attributing all gains to “the model.”

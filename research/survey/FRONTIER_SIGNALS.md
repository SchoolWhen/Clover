# Frontier Signals — Filtered 2026 Watchlist

Last updated: 2026-10-14

This file is the screened successor to the internal `news(5).md` archive.

A frontier signal is **not automatically a scientific result or a Clover design decision**. We keep a signal when it changes how the central problem should be framed, reveals a new competing approach, exposes an evaluation failure, or points to a primary paper/project worth deeper study.

Evidence labels:

- `PRIMARY_PAPER`
- `OFFICIAL_PROJECT`
- `OPEN_SOURCE`
- `OFFICIAL_REPORTED_RESULT`
- `SURVEY_SIGNAL`

---

## S1 — World models are moving from visual fidelity toward task-relevant state

### ReWAM

- Paper: https://arxiv.org/abs/2609.38163
- Evidence: `PRIMARY_PAPER`

Signal:

Reconstruction fidelity and generic perceptual features are not guaranteed to produce the representation most useful for policy learning.

Why Clover cares:

The scientific objective cannot simply be “reconstruct the world accurately.” The relevant state may be a task-/action-sensitive subset of the world's structure.

---

## S2 — Intended action and realized physical consequence must be separated

### HWAM

- Paper: https://arxiv.org/abs/2610.12026
- Evidence: `PRIMARY_PAPER`

Signal:

Humanoid control exposes a reference–execution gap: a command and the state actually reached are different objects.

Why Clover cares:

A robot brain must model:

```text
intention
→ execution
→ observed consequence
```

rather than treating action tokens as ground-truth world transition.

---

## S3 — Large passive-video learning is now a serious answer to physical representation

### V-JEPA 2

- Paper: https://arxiv.org/abs/2506.09985
- Official: https://ai.meta.com/vjepa/
- Code: https://github.com/facebookresearch/vjepa2
- Evidence: `PRIMARY_PAPER + OPEN_SOURCE`

Signal:

Web-scale action-free video can learn representations useful for motion, anticipation and, after action-conditioned adaptation, robot planning.

Open question:

What information is still missing until the system interacts?

### V-JEPA 2.1

- Paper: https://arxiv.org/abs/2603.14482
- Evidence: `PRIMARY_PAPER`

Signal:

Dense, temporally consistent self-supervised features strengthen the case that a single learned representation may cover semantics, space and time more effectively than older modular pipelines.

---

## S4 — Physical variables may emerge in distributed representations

### Interpreting Physics in Video World Models

- Paper: https://arxiv.org/abs/2602.07050
- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Evidence: `PRIMARY_PAPER`

Signal:

Physical quantities need not appear as a small human-designed state vector. Distributed population codes are a serious representation candidate.

Why Clover cares:

This is one of the strongest direct challenges to historical explicit-state assumptions.

---

## S5 — Memory architecture can unlock capability without changing model weights

### VISTA

- Paper: https://arxiv.org/abs/2610.02200
- Evidence: `PRIMARY_PAPER`

Signal:

Lossless visual memory, active retrieval and reorganization can dramatically alter long-horizon visual reasoning while keeping the underlying model fixed.

Why Clover cares:

The world representation and the evidence-memory system may need to be distinct.

---

## S6 — Evidence selection and viewpoint planning are first-class reasoning variables

### Vantage

- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage
- Evidence: `PRIMARY_PAPER + OPEN_SOURCE`

Signal:

Spatial reasoning can improve by choosing and organizing the right views rather than modifying the base reasoning model.

Why Clover cares:

Active perception and evidence scheduling may be core to world understanding, especially under occlusion/partial observability.

---

## S7 — Confidence is useful, but confidence is not truth

### SpatialCORE

- Paper: https://arxiv.org/abs/2609.38716
- Code: https://github.com/rafiibnsultan/SpatialCORE
- Evidence: `PRIMARY_PAPER + OPEN_SOURCE`

Signal:

A model's own grounding confidence can become a training signal.

Clover boundary:

```text
confidence can guide learning / compute
≠
confidence is world authority
```

---

## S8 — Hierarchical world representations remain a live response to long horizons

### H-WM

- Paper: https://arxiv.org/abs/2602.11291
- Evidence: `PRIMARY_PAPER`

Signal:

Combining high-level logical transition with low-level visual transition directly attacks the long-horizon tradeoff between symbolic robustness and visual grounding.

Why Clover cares:

Any future hierarchy must explain why one representation scale cannot cover both demands.

---

## S9 — Identifiability may provide a bridge between latent and explicit state

### Identifiable World Models from Pretrained Diffusion Representations

- Paper: https://arxiv.org/abs/2610.07028
- Evidence: `PRIMARY_PAPER`

Signal:

An explicit/interpretable coordinate system may be recoverable on top of a powerful frozen distributed representation.

Why Clover cares:

The choice may not be binary:

```text
explicit state
vs
latent state
```

A hybrid interface may be more powerful.

---

## S10 — Learned geometry is increasingly a foundation representation

### VGGT

- Paper: https://arxiv.org/abs/2503.11651
- Code: https://github.com/facebookresearch/vggt

### VGGT-Ω

- Paper: https://arxiv.org/abs/2605.15195
- Project: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

Evidence: `PRIMARY_PAPER + OPEN_SOURCE`

Signal:

Camera, depth, point maps, tracks and increasingly dynamic reconstruction can be recovered through learned geometry models at foundation-model scale.

Why Clover cares:

Any new spatial primitive must justify what it contributes beyond modern learned reconstruction.

---

## S11 — Spatial world models are merging reconstruction, generation and simulation

### World Labs Atlas

- Official: https://www.worldlabs.ai/blog/atlas
- Evidence: `OFFICIAL_PROJECT`

Signal:

A single spatial model can be framed as reconstruction engine, generator, simulator and robotics real-to-sim tool.

Clover caution:

When hidden space is underdetermined, generated completion is a hypothesis about the world, not observed truth.

---

## S12 — World foundation models increasingly merge reasoning, generation and action

### Cosmos 3

- Paper: https://arxiv.org/abs/2606.02800
- Code/ecosystem: https://github.com/nvidia/cosmos
- Evidence: `PRIMARY_PAPER + OPEN_SOURCE`

Signal:

The boundaries between “world model”, “reasoner”, “video generator” and “action model” are becoming less clean.

Why Clover cares:

The traditional modular decomposition must earn its value empirically rather than being protected philosophically.

---

## S13 — Direct robot foundation models are a serious falsifier for explicit worldview claims

### Figure Helix 2.5

- Official: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Evidence: `OFFICIAL_REPORTED_RESULT`

Signal:

Figure reports substantial zero-shot improvement in unseen homes from broad human-experience pretraining.

### Skild S1

- Official: https://skild.ai/blogs/s1
- Evidence: `OFFICIAL_REPORTED_RESULT`

Signal:

Skild reports in-context task learning from video demonstrations and long-horizon unseen tasks.

### Physical Self-Play

- Official: https://skild.ai/blogs/physical-self-play

Signal:

Self-generated physical interaction may extend beyond imitation data.

Why Clover cares:

If these systems can generalize/recover without explicit persistent world state, Clover must prove exactly what a worldview adds.

---

## S14 — VLA remains a real competing route, not a straw man

Primary references:

- RT-2: https://arxiv.org/abs/2307.15818
- OpenVLA: https://arxiv.org/abs/2406.09246
- OpenVLA code: https://github.com/openvla/openvla
- π0.5: https://arxiv.org/abs/2504.16054

Signal:

Large vision-language-action systems increasingly transfer web knowledge, task semantics and action priors directly into control.

Research consequence:

The Clover question is not “how to avoid VLA?” It is whether a world representation gives measurable benefits VLA cannot obtain as reliably or efficiently.

---

## S15 — World-Action Models are becoming their own research category

### 2026 WAM survey

- Paper: https://arxiv.org/abs/2609.16074
- Evidence: `PRIMARY_PAPER`

Signal:

Recent robotics work increasingly couples future-world prediction and executable action generation, with open challenges in world-action factorization, action alignment, long-horizon memory and efficient inference.

Why Clover cares:

World and action should be studied jointly without assuming they must be represented by the same state or network.

### Being-M0.7

- Paper: https://arxiv.org/abs/2610.11283
- Evidence: `PRIMARY_PAPER`

Signal:

Being-M0.7 pretrains on more than 10,000 hours of mixed human video/motion data and jointly predicts future latent visual state and motion before adapting to humanoid control. This is a concrete example of learning future-aware visual-motion priors from non-robot experience, then grounding them in robot actions.

### Being-H0.7

- Paper: https://arxiv.org/abs/2605.00078
- Evidence: `PRIMARY_PAPER`

Signal:

Future-aware reasoning can be trained in latent space with a training-only future branch while avoiding pixel rollout at inference. This strengthens the case that “world modeling” for control may be a compact predictive interface rather than a video generator.

---

## S16 — Physical consistency needs process/state supervision, not only pretty rollouts

### EVEWorld

- Paper: https://arxiv.org/abs/2610.03374
- Evidence: `PRIMARY_PAPER`

Signal:

Embodied video world models can exhibit “model laziness”: visually plausible trajectories with poor instance/evolution consistency. Process-level supervision can target this failure.

### RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718
- Evidence: `PRIMARY_PAPER`

Signal:

Evaluation is moving toward state reconstruction and execution-grounded physics rather than visual quality alone.

Clover implication:

```text
plausible video ≠ correct world state ≠ useful action consequence
```

---

## S17 — Pixels-to-physics systems are explicitly adding physical latent structure

### DR-WM / From Pixels to Executable Physics

- Paper: https://arxiv.org/abs/2610.17630
- Evidence: `PRIMARY_PAPER`

Signal:

A recent quadruped world-model line reconstructs geometry and integrates terrain contact priors/action-response data so identical action commands can yield different predicted physical outcomes on different terrain.

Why Clover cares:

Visual world understanding for action may require state variables that are not fully identifiable from appearance alone and must be calibrated through interaction.

---

## S18 — Active/sparse perception remains important for efficiency

### Motion-aware Event Suppression

- Paper: https://arxiv.org/abs/2602.23204
- Evidence: `PRIMARY_PAPER`

Signal:

Sparse event processing can produce high-rate motion representations and reduce downstream token cost.

Clover implication:

The useful abstraction is “compute on informative change”, not necessarily “use event cameras”.

---

## S19 — Tactile/force sensing defines a boundary condition for “vision alone”

The news archive repeatedly surfaced tactile hands, tactile world models and contact-rich manipulation. These are important **boundary signals**, but they do not invalidate the research question.

The correct distinction is:

```text
Can vision infer a useful hypothesis about hidden physical properties?
vs
Can vision uniquely measure force/friction/internal contact state?
```

Clover should not silently treat non-identifiable quantities as observed facts. Future product systems may use additional sensors, while the scientific vision-only protocol remains explicit.

---

## S20 — The capability frontier is long-horizon, unfamiliar, closed-loop behavior

The durable industrial signal across Figure, Skild, Google and other robotics programs is not one benchmark number. It is movement toward:

- unseen environments;
- longer tasks;
- whole-body / mobile manipulation;
- active perception;
- world change and recovery;
- broad experience pretraining.

This supports the current Clover evaluation hierarchy: diagnostic benchmarks first, but eventual validation through real embodied capability.

---

# Signals not promoted to current research conclusions

The raw news archive contains many items that remain useful historically but are **not** promoted into the current Survey as evidence, including:

- funding/valuation news;
- supply-chain announcements;
- secondary media claims without primary technical material;
- single-demo success claims;
- benchmark numbers without clear protocol;
- pre-reset interpretations phrased as “this proves Clover is right”;
- claims whose primary paper/project could not yet be verified.

These may be revisited when primary material becomes available.

---

# How to add a future signal

A durable entry should contain:

```text
name
primary/official URL
evidence class
what changed
what it does NOT prove
why the Clover SSOT cares
research question affected
```

A frontier signal is a reason to investigate, not a reason to stack a new framework into Clover.

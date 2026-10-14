# Clover Status

Last updated: 2026-10-14  
Stage-1 freshness checked through: **2026-10-14**

## Research question

> **How can a machine understand the real world through vision alone?**

## Long-term goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

Lifecycle:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
```

The immediate objective is **coverage before commitment**. No new Clover core representation or algorithm is currently frozen.

## Read first

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)
6. [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md)
7. [`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)
8. [`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md)
9. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
10. [`research/README.md`](research/README.md)

## Current Stage-1 research surfaces

### 1. Broad research inventory

[`research/RESEARCH.md`](research/RESEARCH.md)

Collects methods, theories, datasets, benchmarks, projects and open directions across geometry, video representation, memory, physics, causality, active perception, world models, WAM/VLA, robot learning, uncertainty, continual learning and related areas.

### 2. World-state variables

[`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)

Tracks candidate world-state dimensions including:

```text
geometry
identity / permanence
articulation
mass / density / inertia
friction / stiffness / contact
fluid / granular / deformable state
function / affordance
causal / controllability state
epistemic state
social / intentional state
```

and records whether current evidence comes from static RGB, passive video, active viewpoints, action-response or non-visual/privileged sensing.

### 3. Identifiability and information limits

[`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)

Separates:

```text
predictability
observability
identifiability
calibration / epistemic correctness
action sufficiency
```

Central rule:

```text
statistically predictable from pixels
≠
physically identifiable from pixels
```

### 4. Observation physics

[`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md)

Studies the observation operator itself:

```text
world state
→ light transport / image formation
→ camera acquisition
→ RGB pixels
```

including illumination/material ambiguity, transparency/refraction, specular reflection, occlusion, motion blur, rolling shutter, exposure and sensor limits.

Central rule:

```text
world-state ambiguity
≠
image-formation ambiguity
≠
sensor/acquisition corruption
```

### 5. Hidden physical properties and irreversible change

[`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)

Covers mass/inertia, friction, stiffness, temperature, fluids, granular media, contact/deformation, cutting/splitting/merging/breakage and intervention/counterfactual datasets.

Central rule:

```text
property useful for action
≠
property learned from vision alone
```

### 6. Minimum sufficient world state

[`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md)

Compares belief state, Predictive State Representations, information states, state abstraction/bisimulation and modern compact future-state/world-model representations.

Sufficiency labels:

```text
S-PRED   prediction
S-CTRL   control
S-PLAN   planning
S-MEM    memory / revision
S-CAUSE  intervention / counterfactuals
S-EPI    uncertainty / belief
S-OPEN   open-world / future-task optionality
```

Central rule:

```text
complete physical description
≠
minimal predictive state
≠
minimal control-sufficient state
≠
general-purpose world state
```

### 7. Current frontier

[`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)

Tracks current primary/official work that materially changes the comparison space. Recent high-value references include DR-WM, Gemini 4 Argon for Robotics, GR00T N1.7, Riemann-1.0, Qwen-RobotWorld, Xiaomi-Robotics-U0, Being-M0.7, HWAM, Identifiable World Models, Artisan, Vantage, RobotWorld and Video2World.

## Important current theory references

- POMDP robotics survey — https://arxiv.org/abs/2209.10342
- Predictive Representations of State — https://papers.nips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html
- Approximate Information State — https://www.jmlr.org/beta/papers/v23/20-1165.html
- Lambda Discrepancy / partial-observability diagnostic — https://proceedings.neurips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html
- Latent State Design under Sufficiency Constraints — https://arxiv.org/abs/2605.01694
- DELE-w0.5 — https://arxiv.org/abs/2608.22067
- Representation World Model — https://arxiv.org/abs/2609.29171

## Important observation-physics references

- Recent Trends in Inverse Rendering — https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70592
- inverse-rendering ambiguity analysis — https://arxiv.org/abs/2404.12819
- Trans2Occ — https://arxiv.org/abs/2606.01777
- UnReflectAnything — https://arxiv.org/abs/2512.09583
- motion-blur VPR benchmark — https://arxiv.org/abs/2412.07751
- EvSLAM — https://arxiv.org/abs/2604.24033

## Current non-goals

We are not currently:

- freezing a final representation;
- implementing a new Clover core architecture;
- optimizing leaderboard scores;
- claiming explicit state is superior to latent state;
- claiming compact state is automatically better than rich state;
- claiming a direct policy is sufficient;
- claiming a generative world model is sufficient;
- treating photometric reconstruction as proof of physical-state recovery;
- treating dataset predictability as proof of physical identifiability;
- choosing hardware before the scientific mechanism;
- treating one benchmark as the definition of understanding.

## Stage-1 exit condition

Stage 2 Analysis becomes primary only when the research inventory is broad enough that a new agent can identify:

1. major competing research directions;
2. strongest representative methods and primary sources;
3. what evidence each method actually uses;
4. what its observation/image-formation assumptions are;
5. what world variables it attempts to represent;
6. what its representation is sufficient for;
7. what datasets/benchmarks can discriminate its claims;
8. which capabilities remain unmeasured or under-specified;
9. which assumptions are contradicted by current evidence;
10. which methods deserve one-method-one-report analysis.

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, a final representation, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, a validated original algorithm, or a final hardware mapping.

These remain research targets.

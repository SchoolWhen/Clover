# Datasets, Code, Checkpoints and Platform Resources

Last updated: 2026-10-14

Practical resource map for the Clover Stage-1 research and later baseline/evaluation phases. Listing a resource does **not** mean it should be reproduced immediately.

Before running anything substantial, record:

```text
research question
expected discriminatory result
why this resource is necessary
smaller alternative
observation protocol V0–V3
learning-evidence provenance L0–L4
compute/storage requirements
M4/MPS/CUDA compatibility
licence terms
evidence level
```

---

## Static visual representation

### DINOv3 — primary current SSL baseline

- Paper — https://arxiv.org/abs/2508.10104
- Research page — https://ai.meta.com/research/publications/dinov3/
- Project — https://ai.meta.com/research/dinov3/
- Code — https://github.com/facebookresearch/dinov3

Use for frozen feature probing, dense representation analysis and comparison against temporal/world-model representations.

### DINOv2 — retained predecessor

- Paper — https://arxiv.org/abs/2304.07193
- Code — https://github.com/facebookresearch/dinov2

Useful for historical continuity and lighter existing tooling.

---

## Video / predictive representation

### V-JEPA 2 / 2.1

- V-JEPA 2 paper — https://arxiv.org/abs/2506.09985
- V-JEPA 2 research — https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- Code/checkpoints — https://github.com/facebookresearch/vjepa2
- V-JEPA 2.1 paper — https://arxiv.org/abs/2603.14482
- Physics interpretation — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Initial work should prioritize pretrained inference and probing, not pretraining from scratch.

---

## Visible entity detection / segmentation / tracking

### SAM 3 / SAM 3.1 — primary current visible-entity baseline

- Research — https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
- Paper — https://arxiv.org/abs/2511.16719
- Code — https://github.com/facebookresearch/sam3
- SAM 3.1 release notes — https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

Use as a strong comparator for visible identity/tracking. Do not interpret successful mask tracking as hidden-state object permanence.

### SAM 2 — predecessor

- Paper — https://arxiv.org/abs/2408.00714
- Code — https://github.com/facebookresearch/sam2

### TAO-Amodal — amodal/occlusion diagnostic

- Paper — https://arxiv.org/abs/2312.12433

Use to keep the distinctions explicit:

```text
visible tracking
≠
amodal completion
≠
re-identification
≠
object permanence
```

---

## Geometry / spatial / dynamic-4D reconstruction

- ORB-SLAM3 — https://arxiv.org/abs/2007.11898 · https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT — https://arxiv.org/abs/2003.12039 · https://github.com/princeton-vl/RAFT
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651 · https://github.com/facebookresearch/vggt
- VGGT-Ω — https://arxiv.org/abs/2605.15195 · https://vggt-omega.github.io/ · https://github.com/facebookresearch/vggt-omega
- 4DVGGT-D — https://arxiv.org/abs/2605.12027
- DP-DeGauss — https://arxiv.org/abs/2604.07986
- 4D reconstruction survey/resources — https://arxiv.org/abs/2609.39960 · https://github.com/ZiyangYan/Awesome-4D-Scene-Reconstruction
- Vantage — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
- SpatialCORE — https://arxiv.org/abs/2609.38716 · https://github.com/rafiibnsultan/SpatialCORE

Use 4DVGGT-D and DP-DeGauss specifically when studying camera ego-motion vs object-motion separation in dynamic scenes.

VGGT-family official examples may be CUDA-oriented. Small-sequence pretrained inference/probing should be attempted before any expensive adaptation.

---

## Persistent visual / episodic / semantic / dynamic-world memory

### PersistBench

- Paper — https://arxiv.org/abs/2609.20819
- Project/code/data — https://guangzhaohe.com/persistbench

Use for object permanence, motion continuity and appearance preservation after objects leave the field of view.

### WROP — object-permanence training/exam infrastructure

- Paper — https://arxiv.org/abs/2609.28654

WROP provides cognitive-science-inspired object-permanence/solidity tasks, a large synthetic training corpus and a held-out exam for video world models.

Use it to distinguish:

```text
training a permanence prior
vs
testing persistent memory in realistic scenes
```

### S-EMBER

- Research page — https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper — https://arxiv.org/abs/2607.02689

Use for streaming grounded episodic retrieval and temporal evidence localization.

### VISTA

- Paper — https://arxiv.org/abs/2610.02200

Relevant to memory/retrieval-harness comparisons. Reproduce only when the exact harness question becomes active.

### PerSeM

- Paper — https://arxiv.org/abs/2609.19542

Training-free persistent semantic memory baseline for long-horizon open-vocabulary mapping. Useful as a comparator for frame-wise semantics vs persistent world-space aggregation.

### OASIS-Map

- Paper — https://arxiv.org/abs/2607.14899
- Project — https://dynamic.robots.ox.ac.uk/projects/oasis-map/

Use for multi-session object-level world change:

```text
appeared
disappeared
moved
replaced
re-associated across revisits
```

This is a strong baseline for the distinction between **memory** and **belief revision after the real world changed**.

### R4DSG

- Paper — https://arxiv.org/abs/2608.11017
- Project — https://dualtransparency.github.io/R4DSG/

RGB-only relative 4D scene-graph memory for long egocentric video. Useful for persistent identity, anchor-relative object change and long-horizon object-centric retrieval without assuming a globally aligned metric reconstruction.

---

## Physical quantities, material properties and system identification

### Physically Guided Visual Mass Estimation

- Paper — https://arxiv.org/abs/2601.20303

Single-RGB mass estimator that explicitly treats mass inference as ill-posed and uses geometry/volume and material/density-related priors.

Use for studying:

```text
statistical mass prediction
vs
physical identifiability
```

### PhysQuantAgent / VisPhysQuant

- Paper — https://arxiv.org/abs/2603.16958

Real-object mass-estimation benchmark with multi-view RGB-D videos and measured mass ground truth.

Protocol caution: RGB-D is not a strict V0/V1 RGB-only condition.

### Visual + haptic friction mapping

- Paper — https://arxiv.org/abs/2010.08277

Important foundational evidence that friction is often poorly constrained by appearance alone and benefits from physical exploration.

### Generalizable Friction Coefficient Estimation

- Paper — https://arxiv.org/abs/2604.24188

Uses material embeddings learned from measured proxy interactions rather than assuming friction is directly visible.

### DR-WM / From Pixels to Executable Physics

- Paper — https://arxiv.org/abs/2610.17630

Separates RGB geometry from terrain/contact properties calibrated through action-response experience.

Use as a key Stage-1 system-identification reference.

---

## Deformable, articulated and cross-regime world models

### PointCast

- Paper — https://arxiv.org/abs/2609.28393
- Project — https://pointcast-wm.github.io/

Identity-bearing 3D point-set world model evaluated across rigid objects, cloth, rope and multi-joint cabinets.

Use to probe whether a common representation can span qualitatively different physical regimes.

### PointWorld

- Paper — https://arxiv.org/abs/2601.03782
- Project — https://point-world.github.io/

3D point-flow action/world representation spanning rigid pushing, deformable/articulated manipulation and tool use.

Protocol caution: uses RGB-D rather than strict monocular RGB.

### WorldContact

- Paper — https://arxiv.org/abs/2609.19600

Contact-centric world modeling for deformable-object manipulation. Relevant to bags, cloth and other tasks where geometry alone is insufficient.

### Learning to Unfold Cloth

- Paper — https://arxiv.org/abs/2602.16675

Dreamer-style deformable-object world model with surface-normal input and real-robot transfer.

Protocol caution: surface normals provide stronger geometric evidence than raw monocular RGB.

### ManiSoft

- Paper — https://arxiv.org/abs/2605.18617
- Project/code/data — https://buaa-colalab.github.io/ManiSoft

Benchmark for visual-language manipulation with soft continuum robot arms. Important because the robot body itself can be deformable and visually uncertain.

### DexSim2Real²

- Paper — https://arxiv.org/abs/2409.08750

Uses active one-step interaction to construct an explicit world model/digital twin of unseen articulated objects.

---

## Liquid / weakly visible physical properties

### VLM-based Physical Reasoning for Robot Liquid Perception

- Paper — https://arxiv.org/abs/2404.06904

Useful as a boundary example: vision-only liquid reasoning was weaker than a setup that incorporated interaction-derived force/torque information encoded visually.

Do not classify viscosity estimation from this work as passive-RGB evidence.

---

## Uncertainty / selective prediction under partial visual evidence

### Decision-Aware Uncertainty Evaluation of VLM Early Action Anticipation

- Paper — https://arxiv.org/abs/2603.10061

Use for calibration/selective-prediction protocols under temporally partial egocentric observations.

Relevant measurements:

```text
calibration
coverage
selective risk
confidence vs evidence amount
abstention quality
```

---

## Physical / causal / embodied-reasoning evaluation

### IntPhys 2

- Research — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code — https://github.com/facebookresearch/IntPhys2

### MVP / Minimal Video Pairs

- Research — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

### CausalVQA

- Research — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

### Principia

- Paper — https://arxiv.org/abs/2609.04200

### RoboPhys-3D

- Paper — https://arxiv.org/abs/2608.28718

### Perception Test

- Code/data — https://github.com/google-deepmind/perception_test

Use visual-only subsets where the experiment claims a V0–V3 vision protocol.

### ERQA — Embodied Reasoning Question Answer

- Code/data/evaluation harness — https://github.com/embodiedreasoning/ERQA

Open 400-example multimodal embodied/spatial reasoning diagnostic. Useful for low-cost model comparison before real-robot evaluation, but do not interpret ERQA accuracy as persistent world understanding; language/world-knowledge priors are a major confound.

### RobotWorld

- Paper — https://arxiv.org/abs/2610.10409

Useful for system-level physical-agent capability across heterogeneous tasks and for studying composition, retained task/world state, recovery and completion verification.

### RoboWM-Bench

- Paper — https://arxiv.org/abs/2604.19092

Use for the distinction between visually plausible generated behavior and robot-executable behavior.

### RoboTrustBench

- Paper — https://arxiv.org/abs/2606.01600

Use for constraint-sensitive, counterfactual and adversarial world-model evaluation.

### Video2World

- Paper — https://arxiv.org/abs/2610.04432

Use for geometry/dynamics/functional correctness of reconstructed simulation worlds rather than render similarity alone.

---

## Physically grounded articulated / functional 3D assets

### Artisan

- Paper — https://arxiv.org/abs/2610.13947
- Project link is exposed from the arXiv record: https://physicalvision.github.io

Artisan and its benchmark expand 3D evaluation beyond geometry/appearance/articulation to collision-free motion, stability under gravity, mass/material properties and downstream functional behavior.

Important boundary:

```text
physically grounded generated asset
≠
proof that real mass/material properties are identifiable from passive RGB
```

Use as a Stage-1 reference for articulated-object function, physical asset quality and simulation-grounded evaluation.

---

## Open robot / VLA baselines

### OpenVLA

- Paper — https://arxiv.org/abs/2406.09246
- Code — https://github.com/openvla/openvla

OpenVLA remains a useful established open VLA comparator.

Do not start with full training. First document architecture, action representation, input history, BridgeData/Open X data assumptions, LIBERO evaluation and whether persistent world state is externally represented.

### NVIDIA Isaac GR00T N1.7 — current open humanoid VLA reference

- Code — https://github.com/NVIDIA/Isaac-GR00T
- Model — https://huggingface.co/nvidia/GR00T-N1.7-3B
- Official technical overview — https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/

Use as a strong reproducible direct-policy counter-hypothesis when embodied evaluation becomes active. Its training uses robot demonstrations plus large-scale human/egocentric data, so do not classify it as `L0` visual-only learning.

---

## Robot datasets

- DROID — https://droid-dataset.github.io/droid/
- Open X-Embodiment code/data — https://github.com/google-deepmind/open_x_embodiment
- Open X overview — https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/
- BridgeData V2 — https://rail-berkeley.github.io/bridgedata/

These datasets often include action/robot-state information and therefore are not `L0` visual-only learning evidence.

---

## Human / egocentric video

- Ego4D — https://ego4d-data.org/ · https://ego4d-data.org/docs/
- EPIC-KITCHENS — https://epic-kitchens.github.io/
- Something-Something — https://developer.qualcomm.com/software/ai-datasets/something-something

Useful for motion, interaction, anticipation and long-horizon visual history.

Current robot-policy systems increasingly use large human/egocentric-video corpora. Stage 1 should always distinguish raw visual pretraining from paired motion/action supervision.

---

## Robot simulation / task suites

- LIBERO — https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/ · https://robocasa.ai/leaderboard.html
- ManiSkill — https://github.com/haosulab/ManiSkill

These are future embodied evaluation resources, not current optimization targets.

When simulator state is used for labels/evaluation, keep privileged GT outside the model evidence path unless the experiment explicitly studies an `L4` condition.

---

## Generative / physical world models

### NVIDIA Cosmos 3

- Project — https://research.nvidia.com/labs/cosmos-lab/cosmos3/
- Technical report — https://arxiv.org/abs/2606.02800
- Code — https://github.com/nvidia/cosmos

### World Labs Atlas

- Official technical overview — https://www.worldlabs.ai/blog/atlas
- World-model taxonomy — https://www.worldlabs.ai/blog/taxonomy-of-world-models

Atlas is early-access/closed for full reproduction; study through official technical material, published evaluations, demonstrations and any available access.

### Behavior-grounded / executable physics

- DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630

DR-WM is especially useful for Stage 1 because it explicitly separates geometry available from RGB from contact/friction properties calibrated through real action-response experience.

### Other world/action model references

- EVEWorld — https://arxiv.org/abs/2610.03374
- ReWAM — https://arxiv.org/abs/2609.38163
- HWAM — https://arxiv.org/abs/2610.12026
- Being-H0.7 — https://arxiv.org/abs/2605.00078
- Being-M0.7 — https://arxiv.org/abs/2610.11283
- H-WM — https://arxiv.org/abs/2602.11291
- Identifiable World Models — https://arxiv.org/abs/2610.07028
- WAM survey — https://arxiv.org/abs/2609.16074
- WAM resource page — https://rcl-robotics.github.io/Awesome-World-Action-Models

---

## Action/world interface and visual calibration

### SyncWorld

- Paper — https://arxiv.org/abs/2609.09155

Uses visual calibration episodes to specify environment/embodiment-specific action→visual mappings, highlighting that identical numerical actions need not have identical pixel/world meaning.

### Robot-Factored World Models via Robot Rendering

- Paper — https://arxiv.org/abs/2607.22535

Factors robot action realization and rendered robot geometry away from environment-response prediction. Useful for cross-view/cross-embodiment interface studies.

---

## Closed / partially closed robot-brain and reasoning references

### Gemini Robotics / Gemini 4 Argon

- Gemini Robotics ER 2 overview — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- ER 2 model card — https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Gemini Robotics 2 — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/
- ERQA open evaluation resource — https://github.com/embodiedreasoning/ERQA

Argon is a general multimodal reasoning/tool-use reference rather than evidence for a vision-only learned robot world model. Its published robotics workflows mix visual input with tools, geometry, simulation and robot-state information.

### Figure

- Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

### Skild

- S1 — https://www.skild.ai/blogs/s1
- General-purpose robot brain — https://skild.ai/blogs/building-the-general-purpose-robotic-brain
- Physical Self-Play — https://skild.ai/blogs/physical-self-play

### Physical Intelligence

- π0.5 paper — https://arxiv.org/abs/2504.16054
- π0.5 project — https://www.pi.website/blog/pi05

For closed systems, use:

```text
paper / model card
official technical report
API/preview if available
published evaluation protocol
videos/demos
task reconstruction when scientifically useful
```

Do not convert company claims into independently reproduced facts.

---

## Active perception / evidence acquisition

- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
- Agentic Video Understanding with Gemini — https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/
- Mobility-budget-constrained semantic exploration — https://arxiv.org/abs/2610.17562

Use these to compare learned or agentic evidence selection against explicit uncertainty/information-gain planning. Do not conflate better evidence acquisition with better internal world representation.

---

## Causal representation learning background

- General Identifiability and Achievability for CRL — https://proceedings.mlr.press/v238/varici24a.html
- Multi-node interventional CRL — https://proceedings.mlr.press/v236/bing24a

These are theory resources for understanding when latent causal variables can or cannot be identified from observational/interventional environments.

---

## Apple M4 / local compute

Local platform is Mac mini M4; an engineering resource, not a scientific constraint.

- Specs — https://support.apple.com/en-gb/121555
- Metal — https://developer.apple.com/metal/
- Unified memory API — https://developer.apple.com/documentation/metal/mtldevice/hasunifiedmemory
- Metal Performance Shaders — https://developer.apple.com/documentation/MetalPerformanceShaders
- PyTorch MPS — https://pytorch.org/docs/stable/notes/mps.html
- Core ML — https://developer.apple.com/documentation/coreml

Policy:

```text
science question
→ representation
→ algorithm
→ compute graph
→ CPU/GPU/Metal/Neural Engine mapping
```

Do not alter the science question to fit MPS or avoid external GPU use when a scientifically important baseline requires CUDA.

---

## Reproduction metadata template

When reproduction becomes active, each run should record:

```text
source URL
paper/version date
git commit/checkpoint hash
dataset version/split
licence
V0–V3 observation protocol
L0–L4 learning-evidence provenance
hardware/backend
RAM/VRAM/storage
install command
run command
patches
input/output schema
metrics
known deviations from paper
raw results location
```

The purpose is to make later baseline and Failure Matrix claims independently inspectable.

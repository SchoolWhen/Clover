# Datasets, Code, Checkpoints and Platform Resources

Last updated: 2026-10-14

Practical resource map for the Clover background-research and baseline phases. Listing a resource does **not** mean it should be reproduced immediately.

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

---

## Geometry / spatial reconstruction

- ORB-SLAM3 — https://arxiv.org/abs/2007.11898 · https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT — https://arxiv.org/abs/2003.12039 · https://github.com/princeton-vl/RAFT
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651 · https://github.com/facebookresearch/vggt
- VGGT-Ω — https://arxiv.org/abs/2605.15195 · https://vggt-omega.github.io/ · https://github.com/facebookresearch/vggt-omega
- Vantage — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
- SpatialCORE — https://arxiv.org/abs/2609.38716 · https://github.com/rafiibnsultan/SpatialCORE

VGGT-family official examples may be CUDA-oriented. Small-sequence pretrained inference/probing should be attempted before any expensive adaptation.

---

## Persistent visual / episodic memory

### PersistBench

- Paper — https://arxiv.org/abs/2609.20819
- Project/code/data — https://guangzhaohe.com/persistbench

Use for object permanence, motion continuity and appearance preservation after objects leave the field of view.

### S-EMBER

- Research page — https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper — https://arxiv.org/abs/2607.02689

Use for streaming grounded episodic retrieval and temporal evidence localization.

### VISTA

- Paper — https://arxiv.org/abs/2610.02200

Relevant to memory/retrieval-harness comparisons. Reproduce only when the exact harness question becomes active.

---

## Physical / causal evaluation

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

---

## Open robot/VLA

### OpenVLA

- Paper — https://arxiv.org/abs/2406.09246
- Code — https://github.com/openvla/openvla

OpenVLA-7B is the primary open VLA comparator once embodied task evaluation is ready.

Do not start with full training. First document architecture, action representation, input history, BridgeData/Open X data assumptions, LIBERO evaluation and whether persistent world state is externally represented.

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

### Other world/action model references

- EVEWorld — https://arxiv.org/abs/2610.03374
- DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630
- ReWAM — https://arxiv.org/abs/2609.38163
- HWAM — https://arxiv.org/abs/2610.12026
- Being-H0.7 — https://arxiv.org/abs/2605.00078
- Being-M0.7 — https://arxiv.org/abs/2610.11283
- H-WM — https://arxiv.org/abs/2602.11291
- WAM survey — https://arxiv.org/abs/2609.16074
- WAM resource page — https://rcl-robotics.github.io/Awesome-World-Action-Models

---

## Closed / partially closed robot-brain references

### Gemini Robotics

- ER 2 overview — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- ER 2 model card — https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Robotics 2 — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/

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

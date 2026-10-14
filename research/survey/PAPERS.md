# Papers and Primary Sources

Last updated: 2026-10-14

Curated reading index for the Clover Survey. Sources are grouped by the research contradiction they constrain.

> **Research question:** How can a machine understand the real world through vision alone?

Use [`SOURCE_MAP.md`](SOURCE_MAP.md) when you need the one-to-one mapping from source → demonstrated capability → limitation → Clover landing.

---

## Foundations: uncertainty, partial observability and active perception

- POMDPs in Robotics survey — https://arxiv.org/abs/2209.10342
- Probabilistic Robotics — https://mitpress.mit.edu/9780262201629/probabilistic-robotics/
- Bajcsy, Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Spelke et al., Origins of Knowledge — https://pubmed.ncbi.nlm.nih.gov/1454901/
- Physics for infants review — https://pubmed.ncbi.nlm.nih.gov/26302470/

## Historical representation shift

- SIFT — https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- HOG — https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf
- AlexNet — https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet — https://arxiv.org/abs/1512.03385
- Vision Transformer — https://arxiv.org/abs/2010.11929
- CLIP — https://arxiv.org/abs/2103.00020

## Classical geometry / motion

- Multiple View Geometry — https://www.robots.ox.ac.uk/~vgg/hzbook/
- ORB-SLAM3 — https://arxiv.org/abs/2007.11898 · https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT — https://arxiv.org/abs/2003.12039 · https://github.com/princeton-vl/RAFT

## Static self-supervised visual representation

- I-JEPA — https://arxiv.org/abs/2301.08243
- DINOv2 — https://arxiv.org/abs/2304.07193 · https://github.com/facebookresearch/dinov2
- DINOv3 research — https://ai.meta.com/research/publications/dinov3/
- DINOv3 paper — https://arxiv.org/abs/2508.10104
- DINOv3 code — https://github.com/facebookresearch/dinov3

## Predictive video representation / video world models

- V-JEPA — https://arxiv.org/abs/2404.08471
- V-JEPA 2 — https://arxiv.org/abs/2506.09985 · https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/ · https://github.com/facebookresearch/vjepa2
- V-JEPA 2.1 — https://arxiv.org/abs/2603.14482
- Interpreting Physics in Video World Models — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

## Geometry and spatial intelligence

- NeRF — https://arxiv.org/abs/2003.08934
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651 · https://github.com/facebookresearch/vggt
- VGGT-Ω — https://arxiv.org/abs/2605.15195 · https://vggt-omega.github.io/ · https://github.com/facebookresearch/vggt-omega

## Object-centric representation / visible entities

- Slot Attention — https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html
- PLATO — https://www.nature.com/articles/s41562-022-01394-8
- SAM 2 — https://arxiv.org/abs/2408.00714 · https://github.com/facebookresearch/sam2
- SAM 3 — https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/ · https://arxiv.org/abs/2511.16719
- SAM 3 / 3.1 code — https://github.com/facebookresearch/sam3
- SAM 3.1 release notes — https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

## Persistent visual / episodic memory

- PersistBench — https://arxiv.org/abs/2609.20819 · https://guangzhaohe.com/persistbench
- S-EMBER — https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/ · https://arxiv.org/abs/2607.02689
- VISTA — https://arxiv.org/abs/2610.02200

## Active evidence / spatial reasoning

- Vantage — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
- SpatialCORE — https://arxiv.org/abs/2609.38716 · https://github.com/rafiibnsultan/SpatialCORE

## Intuitive physics / physical consistency

- IntPhys 2 — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ · https://github.com/facebookresearch/IntPhys2
- MVP / Minimal Video Pairs — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- Principia — https://arxiv.org/abs/2609.04200
- Interpreting Physics in Video World Models — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- RoboPhys-3D — https://arxiv.org/abs/2608.28718

## Causality / intervention / counterfactuals

- CausalVQA — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- General Identifiability and Achievability for Causal Representation Learning — https://proceedings.mlr.press/v238/varici24a.html
- Identifying Linearly-Mixed Causal Representations from Multi-Node Interventions — https://proceedings.mlr.press/v236/bing24a

## World models for control

- DreamerV3 — https://arxiv.org/abs/2301.04104
- TD-MPC2 — https://arxiv.org/abs/2310.16828
- H-WM — https://arxiv.org/abs/2602.11291
- Identifiable World Models — https://arxiv.org/abs/2610.07028

## Generative / spatial world models

- World Labs Atlas — https://www.worldlabs.ai/blog/atlas
- World Labs world-model taxonomy — https://www.worldlabs.ai/blog/taxonomy-of-world-models
- Cosmos 3 project — https://research.nvidia.com/labs/cosmos-lab/cosmos3/
- Cosmos 3 report — https://arxiv.org/abs/2606.02800
- Cosmos code — https://github.com/nvidia/cosmos
- EVEWorld — https://arxiv.org/abs/2610.03374
- DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630

## VLA / world-action models

- RT-2 — https://arxiv.org/abs/2307.15818
- OpenVLA — https://arxiv.org/abs/2406.09246 · https://github.com/openvla/openvla
- π0.5 — https://arxiv.org/abs/2504.16054 · https://www.pi.website/blog/pi05
- ReWAM — https://arxiv.org/abs/2609.38163
- HWAM — https://arxiv.org/abs/2610.12026
- Being-H0.7 — https://arxiv.org/abs/2605.00078
- Being-M0.7 — https://arxiv.org/abs/2610.11283
- WAM survey — https://arxiv.org/abs/2609.16074
- WAM resource page — https://rcl-robotics.github.io/Awesome-World-Action-Models

## Embodied reasoning / robot-brain systems

- Gemini Robotics ER 2 overview — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Gemini Robotics ER 2 model card — https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Gemini Robotics 2 — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Figure Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — https://www.skild.ai/blogs/s1
- Skild general-purpose robot brain — https://skild.ai/blogs/building-the-general-purpose-robotic-brain
- Skild Physical Self-Play — https://skild.ai/blogs/physical-self-play

## General video / egocentric data and evaluation

- Perception Test — https://github.com/google-deepmind/perception_test
- Ego4D — https://ego4d-data.org/ · https://ego4d-data.org/docs/
- EPIC-KITCHENS — https://epic-kitchens.github.io/
- Something-Something — https://developer.qualcomm.com/software/ai-datasets/something-something

## Robot datasets / embodied task suites

- DROID — https://droid-dataset.github.io/droid/
- Open X-Embodiment — https://github.com/google-deepmind/open_x_embodiment
- BridgeData V2 — https://rail-berkeley.github.io/bridgedata/
- LIBERO — https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/ · https://robocasa.ai/leaderboard.html
- ManiSkill — https://github.com/haosulab/ManiSkill

## Sparse computation

- Motion-aware Event Suppression — https://arxiv.org/abs/2602.23204

## Surveys

- Physical AI survey — https://arxiv.org/abs/2510.04978
- World-Action Models survey — https://arxiv.org/abs/2609.16074
- POMDPs in Robotics survey — https://arxiv.org/abs/2209.10342

---

## Reading priority

### Tier 0 — problem foundations

POMDP/Probabilistic Robotics → Active Perception → classical geometry → cognitive/object-physics background.

### Tier 1 — strongest representation counter-hypotheses

DINOv3 → V-JEPA 2/2.1 → Interpreting Physics → VGGT/Ω → Slot Attention/PLATO → PersistBench/S-EMBER.

### Tier 2 — world/action alternatives

Atlas/Cosmos 3 → OpenVLA/π0.5 → Gemini ER 2 → Helix 2.5 → Skild S1 → WAM survey + representative WAMs.

### Tier 3 — evaluation/falsification

IntPhys 2 → MVP → Principia → CausalVQA → PersistBench → S-EMBER → RoboPhys-3D → real unseen-environment long-horizon tasks.

### Rule

Do not read only systems that resemble historical Clover. Strong counter-hypotheses are higher-value research targets than confirming examples.

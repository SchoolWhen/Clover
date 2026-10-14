# Papers and Primary Sources

Last updated: 2026-10-14

Curated reading index for the Clover Survey. A source is included because it constrains the central question:

> **How can a machine understand the real world through vision alone?**

## Historical representation shift
- SIFT — https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- HOG — https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf
- AlexNet — https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet — https://arxiv.org/abs/1512.03385
- Vision Transformer — https://arxiv.org/abs/2010.11929
- CLIP — https://arxiv.org/abs/2103.00020

These works frame the shift from handcrafted/task-specific representation to learned scalable representation, data and accelerator co-evolution.

## Self-supervised visual/video representation
- I-JEPA — https://arxiv.org/abs/2301.08243
- DINOv2 — https://arxiv.org/abs/2304.07193 · https://github.com/facebookresearch/dinov2
- V-JEPA — https://arxiv.org/abs/2404.08471
- V-JEPA 2 — https://arxiv.org/abs/2506.09985 · https://ai.meta.com/vjepa/ · https://github.com/facebookresearch/vjepa2
- V-JEPA 2.1 — https://arxiv.org/abs/2603.14482 · https://github.com/facebookresearch/vjepa2
- Interpreting Physics in Video World Models — https://arxiv.org/abs/2602.07050 · https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

## Geometry and spatial intelligence
- ORB-SLAM3 — https://arxiv.org/abs/2007.11898 · https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT — https://arxiv.org/abs/2003.12039 · https://github.com/princeton-vl/RAFT
- NeRF — https://arxiv.org/abs/2003.08934
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651 · https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html · https://github.com/facebookresearch/vggt
- VGGT-Ω — https://arxiv.org/abs/2605.15195 · https://vggt-omega.github.io/ · https://github.com/facebookresearch/vggt-omega
- Slot Attention — https://arxiv.org/abs/2006.15055
- SAM 2 — https://arxiv.org/abs/2408.00714 · https://github.com/facebookresearch/sam2

## Memory and evidence organization
- VISTA — https://arxiv.org/abs/2610.02200
- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
- SpatialCORE — https://arxiv.org/abs/2609.38716 · https://github.com/rafiibnsultan/SpatialCORE

## World models for control
- DreamerV3 — https://arxiv.org/abs/2301.04104
- TD-MPC2 — https://arxiv.org/abs/2310.16828
- H-WM — https://arxiv.org/abs/2602.11291
- Identifiable World Models — https://arxiv.org/abs/2610.07028

## VLA and world-action models
- RT-2 — https://arxiv.org/abs/2307.15818 · https://proceedings.mlr.press/v229/zitkovich23a.html
- OpenVLA — https://arxiv.org/abs/2406.09246 · https://github.com/openvla/openvla
- π0.5 — https://arxiv.org/abs/2504.16054 · https://www.pi.website/blog/pi05
- ReWAM — https://arxiv.org/abs/2609.38163
- HWAM — https://arxiv.org/abs/2610.12026
- Being-H0.7 — https://arxiv.org/abs/2605.00078
- Being-M0.7 — https://arxiv.org/abs/2610.11283
- World-Action Models survey — https://arxiv.org/abs/2609.16074 · https://rcl-robotics.github.io/Awesome-World-Action-Models

## Embodied reasoning / robot-brain systems
- Gemini Robotics ER 2 — https://deepmind.google/models/model-cards/gemini-robotics-er-2/ · https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Figure Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — https://skild.ai/blogs/s1
- Skild Physical Self-Play — https://skild.ai/blogs/physical-self-play

Closed-company results are tracked as `OFFICIAL_REPORTED_RESULT`, not independent reproduction.

## Generative / physical world foundation models
- World Labs Atlas — https://www.worldlabs.ai/blog/atlas
- Cosmos 3 — https://arxiv.org/abs/2606.02800 · https://github.com/nvidia/cosmos · https://www.nvidia.com/en-us/ai/cosmos/
- EVEWorld — https://arxiv.org/abs/2610.03374
- From Pixels to Executable Physics / DR-WM — https://arxiv.org/abs/2610.17630

## Physical / causal evaluation
- IntPhys 2 — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ · https://github.com/facebookresearch/IntPhys2
- MVPBench — https://arxiv.org/abs/2506.09987 · https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- CausalVQA — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- RoboPhys-3D — https://arxiv.org/abs/2608.28718

## Sparse / event-based computation
- Motion-aware Event Suppression — https://arxiv.org/abs/2602.23204

## Broad surveys
- Physical AI survey — https://arxiv.org/abs/2510.04978 · https://github.com/AI4Phys/Awesome-AI-for-Physics
- World-Action Models survey — https://arxiv.org/abs/2609.16074

## Reading priority

**Tier 1 — representation:** V-JEPA 2/2.1 → Interpreting Physics → VGGT/VGGT-Ω → ReWAM → VISTA → Identifiable World Models.

**Tier 2 — robot-brain alternatives:** Gemini Robotics ER 2 → π0.5/OpenVLA → Being-H/M0.7 → Helix 2.5 → Skild S1 → H-WM/HWAM.

**Tier 3 — foundations:** ORB-SLAM3/RAFT → Slot Attention → DreamerV3/TD-MPC2 → active perception/POMDP literature.

**Tier 4 — evaluation:** IntPhys 2 → MVPBench → CausalVQA → RoboPhys-3D → real long-horizon unseen-environment robot tasks.

The purpose of reading is to determine what the next Clover hypothesis must explain that these methods do not already solve.

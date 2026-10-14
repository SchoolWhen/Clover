# Datasets, Code, Checkpoints and Platform Resources

Last updated: 2026-10-14

This file is the practical resource map for Clover's Survey phase. Listing a resource does **not** mean it should be reproduced now.

## Visual representation
- **DINOv2** — paper https://arxiv.org/abs/2304.07193 · code https://github.com/facebookresearch/dinov2
- **V-JEPA 2** — paper https://arxiv.org/abs/2506.09985 · official https://ai.meta.com/vjepa/ · code/checkpoints https://github.com/facebookresearch/vjepa2
- **V-JEPA 2.1** — paper https://arxiv.org/abs/2603.14482 · code/checkpoints https://github.com/facebookresearch/vjepa2
- **SAM 2** — paper https://arxiv.org/abs/2408.00714 · code https://github.com/facebookresearch/sam2

## Geometry / spatial code
- **ORB-SLAM3** — paper https://arxiv.org/abs/2007.11898 · code https://github.com/UZ-SLAMLab/ORB_SLAM3
- **RAFT** — paper https://arxiv.org/abs/2003.12039 · code https://github.com/princeton-vl/RAFT
- **VGGT** — paper https://arxiv.org/abs/2503.11651 · code https://github.com/facebookresearch/vggt
- **VGGT-Ω** — paper https://arxiv.org/abs/2605.15195 · project https://vggt-omega.github.io/ · code https://github.com/facebookresearch/vggt-omega
- **Vantage** — paper https://arxiv.org/abs/2610.11810 · code https://github.com/q1xiangchen/Vantage
- **SpatialCORE** — paper https://arxiv.org/abs/2609.38716 · code https://github.com/rafiibnsultan/SpatialCORE

## Open robot/VLA code
- **OpenVLA** — paper https://arxiv.org/abs/2406.09246 · code https://github.com/openvla/openvla

## Robot datasets
- **DROID** — https://droid-dataset.github.io/droid/
- **Open X-Embodiment** — https://github.com/google-deepmind/open_x_embodiment · overview https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/
- **BridgeData V2** — https://rail-berkeley.github.io/bridgedata/

## Human / egocentric video
- **Ego4D** — https://ego4d-data.org/ · docs https://ego4d-data.org/docs/
- **EPIC-KITCHENS** — https://epic-kitchens.github.io/
- **Something-Something** — https://developer.qualcomm.com/software/ai-datasets/something-something

## Physical / causal evaluation
- **IntPhys 2** — official https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ · code https://github.com/facebookresearch/IntPhys2
- **MVPBench** — paper https://arxiv.org/abs/2506.09987 · official https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- **CausalVQA** — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- **Perception Test** — https://github.com/google-deepmind/perception_test
- **RoboPhys-3D** — https://arxiv.org/abs/2608.28718

## Robot simulation / task suites
- **LIBERO** — https://libero-project.github.io/main.html · code https://github.com/Lifelong-Robot-Learning/LIBERO
- **CALVIN** — https://github.com/mees/calvin
- **RoboCasa** — https://robocasa.ai/ · leaderboard https://robocasa.ai/leaderboard.html
- **ManiSkill** — https://github.com/haosulab/ManiSkill

## World-model / physical-AI ecosystems
- **NVIDIA Cosmos** — https://www.nvidia.com/en-us/ai/cosmos/ · code https://github.com/nvidia/cosmos · Cosmos 3 https://arxiv.org/abs/2606.02800
- **World Labs Atlas** — https://www.worldlabs.ai/blog/atlas

## Closed / partially closed robot-brain references
- **Gemini Robotics ER 2** — model card https://deepmind.google/models/model-cards/gemini-robotics-er-2/ · product https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- **Figure Helix 2.5** — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- **Skild S1** — https://skild.ai/blogs/s1 · self-play https://skild.ai/blogs/physical-self-play
- **π0.5** — paper https://arxiv.org/abs/2504.16054 · official https://www.pi.website/blog/pi05

## WAM / physical-world-model frontier
- Being-H0.7: https://arxiv.org/abs/2605.00078
- Being-M0.7: https://arxiv.org/abs/2610.11283
- HWAM: https://arxiv.org/abs/2610.12026
- ReWAM: https://arxiv.org/abs/2609.38163
- H-WM: https://arxiv.org/abs/2602.11291
- EVEWorld: https://arxiv.org/abs/2610.03374
- DR-WM / Pixels to Executable Physics: https://arxiv.org/abs/2610.17630
- WAM survey: https://arxiv.org/abs/2609.16074
- WAM project index: https://rcl-robotics.github.io/Awesome-World-Action-Models

## Apple M4 / local compute

Local platform is Mac mini M4; it is an engineering resource, not a scientific constraint.

- Specs: https://support.apple.com/en-gb/121555
- Metal: https://developer.apple.com/metal/
- Unified memory API: https://developer.apple.com/documentation/metal/mtldevice/hasunifiedmemory
- Metal Performance Shaders: https://developer.apple.com/documentation/MetalPerformanceShaders
- PyTorch MPS: https://pytorch.org/docs/stable/notes/mps.html
- Core ML: https://developer.apple.com/documentation/coreml

Policy:

```text
science question
→ representation
→ algorithm
→ compute graph
→ CPU/GPU/Metal/Neural Engine mapping
```

## Resource-selection policy

Before reproduction, record the exact research question, expected discriminatory result, why the resource is necessary, whether a smaller analysis could answer it, compute/storage needs, M4/external-GPU requirements, licence terms and expected evidence level.

When reproduction becomes active, add commit/checkpoint hashes, dataset versions, disk/RAM/VRAM requirements, backend support, run commands and patches.

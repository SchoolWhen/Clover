# Datasets, Code, Checkpoints and Platform Resources

Last updated: 2026-10-14

This file is the practical resource map for Clover's Survey phase.

> Listing a resource does **not** mean it should be reproduced now. The current phase is survey-first.

## Visual representation

### DINOv2
- Paper: https://arxiv.org/abs/2304.07193
- Code: https://github.com/facebookresearch/dinov2
- Future use: generic static visual-feature baseline and probing.

### V-JEPA 2 / 2.1
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- Official: https://ai.meta.com/vjepa/
- Code/checkpoints: https://github.com/facebookresearch/vjepa2
- Future use: predictive video representation, physical-variable probing, planning/state comparison.

### SAM 2
- Paper: https://arxiv.org/abs/2408.00714
- Code: https://github.com/facebookresearch/sam2
- Future use: strong segmentation/video entity baseline.

## Geometry / spatial code

### ORB-SLAM3
- Paper: https://arxiv.org/abs/2007.11898
- Code: https://github.com/UZ-SLAMLab/ORB_SLAM3
- Future use: explicit pose/map/relocalization baseline.

### RAFT
- Paper: https://arxiv.org/abs/2003.12039
- Code: https://github.com/princeton-vl/RAFT
- Future use: dense correspondence/motion baseline.

### VGGT
- Paper: https://arxiv.org/abs/2503.11651
- Code: https://github.com/facebookresearch/vggt

### VGGT-Ω
- Paper: https://arxiv.org/abs/2605.15195
- Project: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

### Vantage
- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

### SpatialCORE
- Paper: https://arxiv.org/abs/2609.38716
- Code: https://github.com/rafiibnsultan/SpatialCORE

## Open robot/VLA code

### OpenVLA
- Paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla
- Role: future open VLA comparator, not a current dependency.

## Robot datasets

### DROID
- Project: https://droid-dataset.github.io/droid/
- Role: in-the-wild robot interaction/action-conditioned representation.

### Open X-Embodiment
- Code/data hub: https://github.com/google-deepmind/open_x_embodiment
- Overview: https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/
- Role: cross-embodiment abstraction and transfer.

### BridgeData V2
- Project: https://rail-berkeley.github.io/bridgedata/
- Role: manipulation-policy data and generalization research.

## Human / egocentric visual experience

### Ego4D
- Official: https://ego4d-data.org/
- Docs: https://ego4d-data.org/docs/
- Questions: long-term memory, place/object continuity, forecasting.

### EPIC-KITCHENS
- Official: https://epic-kitchens.github.io/
- Questions: egocentric object interaction and action anticipation.

### Something-Something
- Resource: https://developer.qualcomm.com/software/ai-datasets/something-something
- Question: motion-sensitive transformation semantics.

## Physical / causal evaluation resources

### IntPhys 2
- Official: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

### MVPBench
- Paper: https://arxiv.org/abs/2506.09987
- Official: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

### CausalVQA
- Official: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

### Perception Test
- Code: https://github.com/google-deepmind/perception_test

### RoboPhys-3D
- Paper: https://arxiv.org/abs/2608.28718

## Robot simulation / task suites

### LIBERO
- Project: https://libero-project.github.io/main.html
- Code: https://github.com/Lifelong-Robot-Learning/LIBERO

### CALVIN
- Code: https://github.com/mees/calvin

### RoboCasa
- Project: https://robocasa.ai/
- Leaderboard: https://robocasa.ai/leaderboard.html

### ManiSkill
- Code: https://github.com/haosulab/ManiSkill

Before future use, verify Mac/MPS/CUDA compatibility instead of adapting the scientific question to local hardware.

## World-model / physical-AI ecosystems

### NVIDIA Cosmos
- Official: https://www.nvidia.com/en-us/ai/cosmos/
- Code: https://github.com/nvidia/cosmos
- Cosmos 3: https://arxiv.org/abs/2606.02800

### World Labs Atlas
- Official: https://www.worldlabs.ai/blog/atlas
- Role now: capability/conceptual reference; relatively closed compared with academic code.

## Closed / partially closed robot-brain references

### Gemini Robotics ER 2
- Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Product: https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Evidence: `OFFICIAL_PROJECT`

### Figure Helix 2.5
- Official: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Evidence: `OFFICIAL_REPORTED_RESULT`

### Skild S1 / Physical Self-Play
- S1: https://skild.ai/blogs/s1
- Self-play: https://skild.ai/blogs/physical-self-play
- Evidence: `OFFICIAL_REPORTED_RESULT`

### π0.5
- Paper: https://arxiv.org/abs/2504.16054
- Official: https://www.pi.website/blog/pi05

## WAM / physical-world-model frontier resources

- Being-H0.7: https://arxiv.org/abs/2605.00078
- Being-M0.7: https://arxiv.org/abs/2610.11283
- HWAM: https://arxiv.org/abs/2610.12026
- ReWAM: https://arxiv.org/abs/2609.38163
- H-WM: https://arxiv.org/abs/2602.11291
- EVEWorld: https://arxiv.org/abs/2610.03374
- DR-WM / Pixels to Executable Physics: https://arxiv.org/abs/2610.17630
- WAM survey: https://arxiv.org/abs/2609.16074
- WAM resource page: https://rcl-robotics.github.io/Awesome-World-Action-Models

## Apple M4 / local compute

Local development platform: Mac mini M4. This is an engineering resource, not a scientific constraint.

- Mac mini M4 specs: https://support.apple.com/en-gb/121555
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

not:

```text
local hardware
→ force scientific representation
```

## Resource-selection policy

Before reproduction, record:

1. exact research question;
2. expected discriminatory result;
3. why this resource is necessary;
4. whether a smaller analysis can answer the same question;
5. compute/storage requirements;
6. M4 compatibility or external GPU requirement;
7. licence terms;
8. expected evidence level.

When reproduction becomes active, add commit/checkpoint hashes, dataset versions, disk/RAM/VRAM requirements, OS/backend support, run commands and known patches.

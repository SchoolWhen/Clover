# Datasets, Code, Checkpoints and Platform Resources

Last updated: 2026-10-14

This file is the practical resource map for Clover's Survey phase.

It answers:

> If we later need to inspect, reproduce or compare a method, where are the primary code, data and platform resources?

The current phase is research-first, so listing a resource does **not** mean it must be downloaded or reproduced now.

---

# 1. Core visual representation code

## DINOv2

- Paper: https://arxiv.org/abs/2304.07193
- Code: https://github.com/facebookresearch/dinov2

Potential future use:

- generic visual feature baseline;
- static representation probe;
- object/part feature analysis.

---

## V-JEPA 2 / 2.1

- Paper V-JEPA 2: https://arxiv.org/abs/2506.09985
- Paper V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- Official page: https://ai.meta.com/vjepa/
- Code/checkpoints: https://github.com/facebookresearch/vjepa2

Potential future use:

- temporal representation baseline;
- physical variable probing;
- prediction/planning comparison.

---

## SAM 2

- Paper: https://arxiv.org/abs/2408.00714
- Code: https://github.com/facebookresearch/sam2

Potential future use:

- video mask/track baseline;
- persistence/entity diagnostics.

---

# 2. Classical / geometric code

## ORB-SLAM3

- Paper: https://arxiv.org/abs/2007.11898
- Code: https://github.com/UZ-SLAMLab/ORB_SLAM3

Potential future use:

- explicit geometric state baseline;
- camera tracking;
- map persistence;
- relocalization.

---

## RAFT

- Paper: https://arxiv.org/abs/2003.12039
- Code: https://github.com/princeton-vl/RAFT

Potential future use:

- dense motion baseline;
- optical-flow derived event/evidence experiments.

---

## VGGT

- Paper: https://arxiv.org/abs/2503.11651
- Code: https://github.com/facebookresearch/vggt

Potential future use:

- learned 3D geometry;
- depth/camera/track baseline;
- spatial feature probing.

---

## VGGT-Ω

- Paper: https://arxiv.org/abs/2605.15195
- Project: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

Potential future use:

- dynamic/scalable learned geometry baseline.

---

## Vantage

- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

Potential future use:

- view/evidence planning;
- active perception inspiration;
- multi-view reasoning baseline.

---

## SpatialCORE

- Paper: https://arxiv.org/abs/2609.38716
- Code: https://github.com/rafiibnsultan/SpatialCORE

Potential future use:

- confidence-aware grounding analysis.

---

# 3. Open VLA / robot policy code

## OpenVLA

- Paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla

Potential future role:

Open VLA comparator once Clover reaches an embodied evaluation stage.

Not a current implementation dependency.

---

# 4. Robot datasets

## DROID

- Project: https://droid-dataset.github.io/droid/
- Paper/resources: linked from project site.

Description:

Large-scale in-the-wild robot manipulation data.

Clover relevance:

- interaction vs passive observation;
- action-conditioned representation;
- consequence modeling.

V-JEPA 2-AC uses DROID robot video for action-conditioned post-training.

---

## Open X-Embodiment

- Repository: https://github.com/google-deepmind/open_x_embodiment
- DeepMind overview: https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/

Why relevant:

Cross-embodiment robot experience provides evidence about:

- shared action abstractions;
- embodiment-specific state;
- representation transfer.

---

## BridgeData V2

OpenVLA ecosystem resource.

- Project: https://rail-berkeley.github.io/bridgedata/

Potential relevance:

Robot manipulation policy learning and generalization.

---

# 5. Human / egocentric video datasets

## Ego4D

- Official: https://ego4d-data.org/
- Documentation: https://ego4d-data.org/docs/

Potential research questions:

- persistent egocentric memory;
- long-term activity context;
- place recognition;
- anticipation;
- object continuity.

---

## EPIC-KITCHENS

- Official: https://epic-kitchens.github.io/

Potential research questions:

- object interaction;
- action anticipation;
- kitchen dynamics;
- first-person physical experience.

---

## Something-Something

- Dataset resource: https://developer.qualcomm.com/software/ai-datasets/something-something

Potential research questions:

- motion-sensitive semantics;
- transformation/action representation.

---

# 6. Physical / causal benchmark resources

## IntPhys 2

- Official page: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Use later:

Controlled physics diagnostic.

---

## MVPBench

- Paper: https://arxiv.org/abs/2506.09987
- Official page: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Use later:

Shortcut-resistant physical video reasoning.

---

## CausalVQA

- Official page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Use later:

Causal/counterfactual video reasoning.

---

## Perception Test

- Repository: https://github.com/google-deepmind/perception_test

Use later:

Broad video perception/reasoning diagnostics.

---

# 7. Robot simulation / task suites

## LIBERO

- Project: https://libero-project.github.io/main.html
- Code: https://github.com/Lifelong-Robot-Learning/LIBERO

Focus:

- lifelong learning;
- transfer;
- task suites.

---

## CALVIN

- Code: https://github.com/mees/calvin

Focus:

- long-horizon sequence tasks;
- language-conditioned manipulation.

---

## RoboCasa

- Project: https://robocasa.ai/
- Leaderboard: https://robocasa.ai/leaderboard.html

Focus:

- household/kitchen tasks;
- compositional tasks;
- scene diversity.

---

## ManiSkill

- Code: https://github.com/haosulab/ManiSkill

Focus:

- scalable manipulation simulation;
- task generation/evaluation.

Current caveat:

Mac support and GPU simulation capabilities should be checked before any future reproduction plan.

---

# 8. World-model / generative ecosystems

## NVIDIA Cosmos

- Official: https://www.nvidia.com/en-us/ai/cosmos/
- Code/ecosystem: https://github.com/nvidia/cosmos
- Cosmos 3 paper: https://arxiv.org/abs/2606.02800

Use later:

- generative physical AI comparison;
- synthetic data / simulation;
- world/action model taxonomy.

---

## World Labs Atlas

- Official report: https://www.worldlabs.ai/blog/atlas

Current availability:

Early-access/closed relative to open academic code.

Use now:

Conceptual and capability reference.

---

# 9. Closed / partially closed robot-brain references

These are important even when code is not open.

## Gemini Robotics ER 2

- Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Product page: https://deepmind.google/models/gemini-robotics/embodied-reasoning/

Evidence class:

`OFFICIAL_PROJECT`

---

## Figure Helix 2.5

- Official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

Evidence class:

`OFFICIAL_REPORTED_RESULT`

---

## Skild S1

- Official report: https://skild.ai/blogs/s1
- Physical Self-Play: https://skild.ai/blogs/physical-self-play

Evidence class:

`OFFICIAL_REPORTED_RESULT`

---

## π0.5

- Paper: https://arxiv.org/abs/2504.16054
- Official: https://www.pi.website/blog/pi05

Evidence class:

`PRIMARY_PAPER + OFFICIAL_PROJECT`

---

# 10. Apple M4 / local compute resources

The local development platform is a Mac mini M4.

This is an engineering resource, not a scientific constraint.

## Apple Mac mini M4 specs

- https://support.apple.com/en-gb/121555

## Apple Silicon / unified memory

- Metal `hasUnifiedMemory`:
  https://developer.apple.com/documentation/metal/mtldevice/hasunifiedmemory

## Metal

- https://developer.apple.com/metal/

## Metal Performance Shaders

- https://developer.apple.com/documentation/MetalPerformanceShaders

## PyTorch MPS backend

- https://pytorch.org/docs/stable/notes/mps.html

## Core ML

- https://developer.apple.com/documentation/coreml

Future principle:

```text
science question
→ representation
→ algorithm
→ compute graph
→ CPU/GPU/Metal/Neural Engine mapping
```

not:

```text
M4 hardware
→ force scientific representation
```

---

# 11. Resource selection policy

A resource should not be downloaded merely because it is popular.

Before reproduction, record:

1. exact research question;
2. expected discriminatory result;
3. why this specific code/data is needed;
4. whether a smaller analysis can answer the same question;
5. compute/storage requirements;
6. M4 compatibility or external GPU need;
7. licence terms;
8. expected evidence level.

This prevents the Survey phase from turning into an unstructured reproduction campaign.

---

# 12. Future resource metadata

When actual reproduction begins, add for each resource:

```text
version / commit SHA
checkpoint hash
dataset version
licence
expected disk
expected RAM/VRAM
supported OS
MPS/CUDA requirements
run command
known patches
```

That information is intentionally deferred until reproduction becomes an active task.

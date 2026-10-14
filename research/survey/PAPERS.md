# Papers and Primary Sources

Last updated: 2026-10-14

This is a curated reading index for the Clover Survey.

It is not a bibliography dump. A paper is included because it constrains at least one part of the central question:

> **How can a machine understand the real world through vision alone?**

Priority is given to primary papers, official model cards, official project pages and open implementations.

---

# A. Historical representation shift

## A1. SIFT — hand-designed local invariance

**David Lowe, "Distinctive Image Features from Scale-Invariant Keypoints" (IJCV 2004)**

- Topic: handcrafted local visual representation.
- Why read: shows the strength and limits of explicit engineered invariances.
- Paper: https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf

Key Clover question:

> Which invariances should still be engineered because they are mathematically well understood, and which should emerge from data?

---

## A2. HOG — engineered shape representation

**Dalal & Triggs, "Histograms of Oriented Gradients for Human Detection" (CVPR 2005)**

- Topic: local orientation statistics / engineered visual features.
- Paper: https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf

Why read:

HOG is a reminder that "CPU-era CV" was not simply weak. It contained strong representations, but representation design was task-specific and manually specified.

---

## A3. AlexNet — learned representation + scalable GPU training

**Krizhevsky, Sutskever, Hinton, "ImageNet Classification with Deep Convolutional Neural Networks" (NeurIPS 2012)**

- Paper: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf

Why read:

The transition was not "GPU beats CPU" in isolation.

It combined:

```text
learned hierarchy
+ large labeled data
+ optimization
+ hardware capable of training it
```

---

## A4. ResNet — optimization of deep learned hierarchies

**He et al., "Deep Residual Learning for Image Recognition"**

- Paper: https://arxiv.org/abs/1512.03385

Why read:

Representation capacity only matters if the optimization system can train it reliably.

---

## A5. Vision Transformer

**Dosovitskiy et al., "An Image is Worth 16x16 Words"**

- Paper: https://arxiv.org/abs/2010.11929

Why read:

Demonstrates that strong visual representation can emerge with weaker hand-designed spatial inductive bias when data/scale are sufficient.

---

## A6. CLIP

**Radford et al., "Learning Transferable Visual Models From Natural Language Supervision"**

- Paper: https://arxiv.org/abs/2103.00020

Clover relevance:

CLIP demonstrates enormous semantic transfer, but language supervision introduces a confound for "vision alone".

---

# B. Self-supervised visual representation

## B1. I-JEPA

**Assran et al., "Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture"**

- Paper: https://arxiv.org/abs/2301.08243

Why read:

JEPA explicitly shifts prediction away from raw pixels toward representation space.

This idea later becomes central in video/world-model work.

---

## B2. DINOv2

**Oquab et al., "DINOv2: Learning Robust Visual Features without Supervision"**

- Paper: https://arxiv.org/abs/2304.07193
- Code: https://github.com/facebookresearch/dinov2

Key question:

> How much spatial/object structure already emerges from static self-supervised features?

---

## B3. V-JEPA

**Bardes et al., "Revisiting Feature Prediction for Learning Visual Representations from Video"**

- Paper: https://arxiv.org/abs/2404.08471

Why read:

Early direct bridge from JEPA to temporal video representation.

---

## B4. V-JEPA 2

**Assran et al., "V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning"**

- Paper: https://arxiv.org/abs/2506.09985
- Official page: https://ai.meta.com/vjepa/
- Code: https://github.com/facebookresearch/vjepa2

Key evidence:

- web-scale action-free video learning;
- motion/action anticipation;
- action-conditioned latent planning with robot video.

Core Clover question:

> Can a distributed predictive embedding become a sufficient world representation for planning without explicit persistent symbolic state?

---

## B5. V-JEPA 2.1

**Mur-Labadia et al., "V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning"**

- Paper: https://arxiv.org/abs/2603.14482
- Code: https://github.com/facebookresearch/vjepa2

Why read:

Adds dense predictive learning and stronger spatial-temporal grounding.

---

## B6. Interpreting Physics in Video World Models

**Joseph et al., "Interpreting Physics in Video World Models"**

- Paper: https://arxiv.org/abs/2602.07050
- Meta page: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Central result for Clover:

Physical variables can appear as distributed, hierarchical representations rather than compact factorized states.

This is one of the most important counterarguments to assuming that explicit world variables are necessarily the correct representation.

---

# C. Geometry and spatial intelligence

## C1. ORB-SLAM3

**Campos et al., "ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM"**

- Paper: https://arxiv.org/abs/2007.11898
- Code: https://github.com/UZ-SLAMLab/ORB_SLAM3

Why read:

Persistent explicit geometric state, map reuse, localization and uncertainty are mature problems with decades of theory behind them.

---

## C2. RAFT

**Teed & Deng, "RAFT: Recurrent All-Pairs Field Transforms for Optical Flow"**

- Paper: https://arxiv.org/abs/2003.12039
- Code: https://github.com/princeton-vl/RAFT

Why read:

Dense temporal correspondence baseline.

---

## C3. NeRF

**Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"**

- Paper: https://arxiv.org/abs/2003.08934

Clover relevance:

A neural continuous field can encode scene appearance/geometry, but novel-view synthesis is not automatically a world state suitable for causality or planning.

---

## C4. DUSt3R

**Wang et al., "DUSt3R: Geometric 3D Vision Made Easy"**

- Paper: https://arxiv.org/abs/2312.14132

Why read:

Learned point-map prediction collapses parts of a classical multi-stage reconstruction pipeline into a learned model.

---

## C5. VGGT

**Wang et al., "VGGT: Visual Geometry Grounded Transformer"**

- Paper: https://arxiv.org/abs/2503.11651
- CVPR page: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html
- Code: https://github.com/facebookresearch/vggt

Outputs include:

- camera;
- depth;
- point maps;
- tracks.

Research question:

> Is learned reconstruction a sufficient spatial substrate for a robot worldview?

---

## C6. VGGT-Ω

- Paper: https://arxiv.org/abs/2605.15195
- Project: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

Why read:

Pushes learned geometry toward larger scale, dynamic scenes and reusable downstream representation.

---

## C7. Slot Attention

**Locatello et al., "Object-Centric Learning with Slot Attention"**

- Paper: https://arxiv.org/abs/2006.15055

Clover question:

> Should persistent entities be explicit slots/primitives, or should objectness remain emergent/distributed?

---

## C8. SAM 2

**Ravi et al., "SAM 2: Segment Anything in Images and Videos"**

- Paper: https://arxiv.org/abs/2408.00714
- Code: https://github.com/facebookresearch/sam2

Role:

Perception/entity tracking baseline, not a world model.

---

# D. Visual memory and evidence organization

## D1. VISTA

**Han et al., "VISTA: A Visual Harness for Reasoning in an Interactive World"**

- Paper: https://arxiv.org/abs/2610.02200

Core contribution:

- lossless visual memory;
- active retrieval of historical observations;
- visual input reorganization;
- same underlying multimodal model.

Clover question:

> How much world-state capability should live in model weights versus evidence memory and retrieval?

---

## D2. S-EMBER

**Meta, Streaming Egocentric Memory Retrieval benchmark**

- Official publication listing: https://ai.meta.com/results/?content_types%5B0%5D=publication&research_areas%5B0%5D=computer-vision

Why track:

Persistent egocentric memory is closer to robot-world continuity than isolated video QA.

---

# E. Spatial reasoning and evidence selection

## E1. Vantage

**Chen et al., "Seek-and-View Reasoning for Multi-View Spatial Understanding"**

- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

Why read:

Shows that spatial reasoning may improve by actively organizing viewpoints/evidence, even without changing the base VLM.

---

## E2. SpatialCORE

**Sultan et al., "SpatialCORE: Confidence-Aware Grounded Spatial Reasoning in Large Vision-Language Models"**

- Paper: https://arxiv.org/abs/2609.38716
- Code: https://github.com/rafiibnsultan/SpatialCORE

Why read:

A concrete example of grounding confidence becoming a learning signal.

Important Clover distinction:

```text
confidence can guide learning
≠
confidence is truth
```

---

# F. World models for control

## F1. DreamerV3

**Hafner et al., "Mastering Diverse Domains through World Models"**

- Paper: https://arxiv.org/abs/2301.04104

Question:

> What state is sufficient for control even if it is not directly interpretable?

---

## F2. TD-MPC2

**Hansen et al., "TD-MPC2: Scalable, Robust World Models for Continuous Control"**

- Paper: https://arxiv.org/abs/2310.16828

Why read:

Strong evidence that compact learned latent dynamics can be highly useful for planning/control.

---

## F3. H-WM

**Chen et al., "H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model"**

- Paper: https://arxiv.org/abs/2602.11291

Main tension:

```text
symbolic long-horizon robustness
vs
visual grounding
```

The paper combines both.

Clover should understand this contradiction before inventing a separate hierarchical world system.

---

## F4. Identifiable World Models from Pretrained Diffusion Representations

**Sandilya et al.**

- Paper: https://arxiv.org/abs/2610.07028

Why read:

Predictive/generative latents need not be directly interpretable, but a lightweight aligned identifiable coordinate system may recover intervention-relevant state.

This may offer a hybrid alternative to:

```text
fully explicit world
vs
fully distributed world
```

---

# G. Vision-language-action and world-action models

## G1. RT-2

**Zitkovich et al., "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"**

- Paper: https://arxiv.org/abs/2307.15818
- PMLR: https://proceedings.mlr.press/v229/zitkovich23a.html

Why read:

One of the clearest action-first alternatives to explicit world modeling.

---

## G2. OpenVLA

**Kim et al., "OpenVLA: An Open-Source Vision-Language-Action Model"**

- Paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla

Why read:

Open implementation / eventual VLA comparator.

---

## G3. π0.5

**Physical Intelligence**

- Paper: https://arxiv.org/abs/2504.16054
- Official project: https://www.pi.website/blog/pi05

Why read:

Long-horizon/open-world robot generalization with heterogeneous multimodal and robot training.

---

## G4. ReWAM

**Jiang et al., "Rethinking Representations for World-Action Modeling"**

- Paper: https://arxiv.org/abs/2609.38163

Key result:

Neither visual reconstruction fidelity nor generic pretrained perceptual features alone guarantee a representation useful for policy learning.

This paper should be central in any future Clover representation objective discussion.

---

## G5. HWAM

**Yang et al., "Humanoid World Action Model With Joint State--Action Generation"**

- Paper: https://arxiv.org/abs/2610.12026

Key issue:

```text
reference action
≠
physically executed motion
```

The realized post-execution state must be modeled.

---

# H. Embodied reasoning and robot-brain systems

## H1. Gemini Robotics ER 2

- Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Product page: https://deepmind.google/models/gemini-robotics/embodied-reasoning/

Evidence label: `OFFICIAL_PROJECT`

Why read:

A direct industrial answer to the high-level "robot brain" problem.

Critical Clover question:

> How much of ER 2's physical reasoning is grounded in visual evidence versus inherited multimodal/language knowledge?

---

## H2. Figure Helix 2.5

- Official technical report/blog: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

Evidence label: `OFFICIAL_REPORTED_RESULT`

Reported result:

- 30 unseen homes;
- whole-body household tasks;
- zero environment-specific adaptation;
- 9% → 56% zero-shot success from Index pretraining.

Why read:

Shows how strongly broad human experience can affect real-world generalization.

---

## H3. Skild S1

- Official report: https://skild.ai/blogs/s1

Evidence label: `OFFICIAL_REPORTED_RESULT`

Why read:

In-context task specification from video demonstration, with reported long-horizon unseen task behavior.

---

## H4. Physical Self-Play

- Official report: https://skild.ai/blogs/physical-self-play

Why read:

Raises the possibility that physical intelligence requires self-generated experience beyond passive observation and imitation.

---

# I. Generative / physical world foundation models

## I1. Atlas

**World Labs**

- Official report: https://www.worldlabs.ai/blog/atlas

Evidence label: `OFFICIAL_PROJECT`

Reported architecture:

- multimodal autoregressive diffusion transformer;
- text/image/video/3D spatial context;
- reconstruction;
- generation;
- simulation;
- robotics real-to-sim.

Important conceptual distinction:

Atlas may infer plausible hidden space.

Clover must separate:

```text
plausible hidden completion
from
epistemically justified world state
```

---

## I2. Cosmos 3

- Paper: https://arxiv.org/abs/2606.02800
- Code/ecosystem: https://github.com/nvidia/cosmos
- Official: https://www.nvidia.com/en-us/ai/cosmos/

Why read:

Represents the broad physical-AI world foundation model direction where reasoning, generation and action are increasingly unified.

---

# J. Physical and causal understanding

## J1. IntPhys 2

- Official page: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Capabilities tested include:

- permanence;
- immutability;
- spatio-temporal continuity;
- solidity.

Use:

diagnostic only, not definition of understanding.

---

## J2. MVPBench

**Krojer et al., "A Shortcut-aware Video-QA Benchmark for Physical Understanding via Minimal Video Pairs"**

- Paper: https://arxiv.org/abs/2506.09987
- Official page: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Why read:

Minimal paired examples explicitly target shortcut exploitation.

This should influence Clover evaluation design even if the final system is not QA-based.

---

## J3. CausalVQA

- Official page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Why read:

Tests causal/counterfactual/hypothetical/anticipation reasoning over physical video.

---

## J4. RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

Why track:

Embodied world-model evaluation increasingly requires reconstructed state and execution-grounded evaluation rather than perceptual/video quality alone.

---

# K. Sparse/event-based vision

## K1. Motion-aware Event Suppression

**Pellerito et al.**

- Paper: https://arxiv.org/abs/2602.23204

Why read:

Demonstrates a high-speed sparse visual computation regime and provides an example where event filtering improves downstream compute.

The Clover lesson is about exploiting visual change sparsity, not necessarily adopting event cameras.

---

# L. Broad survey

## L1. Physical AI Survey

**"Aligning Perception, Reasoning, Modeling and Interaction: A Survey on Physical AI"**

- Paper: https://arxiv.org/abs/2510.04978

Use:

Broad context only. Primary works should still be read directly.

---

# Reading priority

## Tier 1 — representation question

1. V-JEPA 2
2. V-JEPA 2.1
3. Interpreting Physics in Video World Models
4. VGGT
5. VGGT-Ω
6. ReWAM
7. VISTA
8. Identifiable World Models

## Tier 2 — robot-brain alternatives

1. Gemini Robotics ER 2
2. π0.5
3. OpenVLA
4. Helix 2.5
5. Skild S1
6. H-WM
7. HWAM

## Tier 3 — foundations / controls

1. ORB-SLAM3
2. RAFT
3. Slot Attention
4. DreamerV3
5. TD-MPC2
6. active perception / POMDP literature

## Tier 4 — evaluation

1. IntPhys 2
2. MVPBench
3. CausalVQA
4. RoboPhys-3D
5. real long-horizon robot tasks

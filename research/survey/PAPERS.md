# Papers and Primary Sources

Last updated: 2026-10-14

This is a curated reading index for the Clover Survey. It is not a bibliography dump: a source is included because it constrains at least one part of the central question:

> **How can a machine understand the real world through vision alone?**

Priority is given to primary papers, official model cards, official project pages and open implementations.

## Historical representation shift

- **SIFT — Lowe (2004)** — engineered local invariance. Paper: https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- **HOG — Dalal & Triggs (2005)** — engineered orientation/shape statistics. Paper: https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf
- **AlexNet — Krizhevsky et al. (2012)** — learned hierarchy + large data + GPU-scale training. Paper: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- **ResNet — He et al.** — deep residual optimization. Paper: https://arxiv.org/abs/1512.03385
- **Vision Transformer — Dosovitskiy et al.** — weaker hand-designed visual bias under scale. Paper: https://arxiv.org/abs/2010.11929
- **CLIP — Radford et al.** — language-supervised transferable vision, important confound for “vision alone”. Paper: https://arxiv.org/abs/2103.00020

## Self-supervised visual/video representation

- **I-JEPA** — joint-embedding prediction for images. Paper: https://arxiv.org/abs/2301.08243
- **DINOv2** — self-supervised general visual features. Paper: https://arxiv.org/abs/2304.07193 · Code: https://github.com/facebookresearch/dinov2
- **V-JEPA** — temporal feature prediction. Paper: https://arxiv.org/abs/2404.08471
- **V-JEPA 2** — understanding/prediction/planning from large-scale passive video plus action-conditioned robot post-training. Paper: https://arxiv.org/abs/2506.09985 · Official: https://ai.meta.com/vjepa/ · Code: https://github.com/facebookresearch/vjepa2
- **V-JEPA 2.1** — dense predictive learning and temporally consistent dense features. Paper: https://arxiv.org/abs/2603.14482 · Code: https://github.com/facebookresearch/vjepa2
- **Interpreting Physics in Video World Models** — distributed/hierarchical physical representations. Paper: https://arxiv.org/abs/2602.07050 · Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

## Geometry and spatial intelligence

- **ORB-SLAM3** — persistent explicit visual geometry. Paper: https://arxiv.org/abs/2007.11898 · Code: https://github.com/UZ-SLAMLab/ORB_SLAM3
- **RAFT** — learned dense optical flow. Paper: https://arxiv.org/abs/2003.12039 · Code: https://github.com/princeton-vl/RAFT
- **NeRF** — neural radiance-field scene representation. Paper: https://arxiv.org/abs/2003.08934
- **DUSt3R** — learned point-map geometry. Paper: https://arxiv.org/abs/2312.14132
- **VGGT** — camera/depth/point-map/track foundation geometry. Paper: https://arxiv.org/abs/2503.11651 · CVPR: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html · Code: https://github.com/facebookresearch/vggt
- **VGGT-Ω** — scalable/dynamic learned geometry. Paper: https://arxiv.org/abs/2605.15195 · Project: https://vggt-omega.github.io/ · Code: https://github.com/facebookresearch/vggt-omega
- **Slot Attention** — object-centric slots. Paper: https://arxiv.org/abs/2006.15055
- **SAM 2** — streaming image/video segmentation memory; useful perception/entity baseline, not a world model. Paper: https://arxiv.org/abs/2408.00714 · Code: https://github.com/facebookresearch/sam2

## Memory and evidence organization

- **VISTA: A Visual Harness for Reasoning in an Interactive World** — lossless visual memory, active retrieval and reorganization. Paper: https://arxiv.org/abs/2610.02200
- **Vantage / Seek-and-View** — view planning + geometry-grounded evidence + VLM reasoning. Paper: https://arxiv.org/abs/2610.11810 · Code: https://github.com/q1xiangchen/Vantage
- **SpatialCORE** — confidence-aware grounded spatial reasoning. Paper: https://arxiv.org/abs/2609.38716 · Code: https://github.com/rafiibnsultan/SpatialCORE

## World models for control

- **DreamerV3** — latent world model for behavior learning. Paper: https://arxiv.org/abs/2301.04104
- **TD-MPC2** — scalable latent dynamics + planning/control. Paper: https://arxiv.org/abs/2310.16828
- **H-WM** — hierarchical logical + visual world transitions for task/motion planning. Paper: https://arxiv.org/abs/2602.11291
- **Identifiable World Models from Pretrained Diffusion Representations** — identifiable coordinates over frozen distributed world representations. Paper: https://arxiv.org/abs/2610.07028

## VLA and world-action models

- **RT-2** — vision-language-action transfer from web knowledge to robotic control. Paper: https://arxiv.org/abs/2307.15818 · PMLR: https://proceedings.mlr.press/v229/zitkovich23a.html
- **OpenVLA** — open VLA implementation. Paper: https://arxiv.org/abs/2406.09246 · Code: https://github.com/openvla/openvla
- **π0.5** — open-world robot generalization. Paper: https://arxiv.org/abs/2504.16054 · Official: https://www.pi.website/blog/pi05
- **ReWAM** — representation shaping for world-action modeling; reconstruction fidelity alone is insufficient. Paper: https://arxiv.org/abs/2609.38163
- **HWAM** — joint state/action generation and reference–execution gap. Paper: https://arxiv.org/abs/2610.12026
- **Being-H0.7** — latent future-aware world-action model from egocentric video, no pixel rollout at inference. Paper: https://arxiv.org/abs/2605.00078
- **Being-M0.7** — mixed human video/motion pretraining transferred to humanoid loco-manipulation. Paper: https://arxiv.org/abs/2610.11283
- **World-Action Models for Robot Learning and Control: A Survey** — 2026 taxonomy covering representation, transition, action interfaces, data and evaluation. Paper: https://arxiv.org/abs/2609.16074 · Project: https://rcl-robotics.github.io/Awesome-World-Action-Models

## Embodied reasoning and robot-brain systems

- **Gemini Robotics ER 2** — high-level embodied/spatial/physical reasoning system. Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/ · Product: https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- **Figure Helix 2.5** — reported zero-shot whole-body household generalization in unseen homes. Official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- **Skild S1** — reported in-context robot learning from video demonstration. Official report: https://skild.ai/blogs/s1
- **Skild Physical Self-Play** — self-generated embodied experience. Official report: https://skild.ai/blogs/physical-self-play

Closed-company results above are tagged in the Survey as `OFFICIAL_REPORTED_RESULT`, not independent reproductions.

## Generative / physical world foundation models

- **World Labs Atlas** — reconstruction, generation, simulation and spatial world modeling. Official: https://www.worldlabs.ai/blog/atlas
- **Cosmos 3** — omnimodal physical-AI world/reasoning/action model family. Paper: https://arxiv.org/abs/2606.02800 · Code: https://github.com/nvidia/cosmos · Official: https://www.nvidia.com/en-us/ai/cosmos/
- **EVEWorld** — physical-evolution supervision and “model laziness” diagnosis for embodied world models. Paper: https://arxiv.org/abs/2610.03374
- **From Pixels to Executable Physics / DR-WM** — geometry + terrain/contact dynamics for action-consequence prediction. Paper: https://arxiv.org/abs/2610.17630

## Physical / causal evaluation papers

- **IntPhys 2** — permanence, immutability, spatio-temporal continuity, solidity. Official: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ · Code: https://github.com/facebookresearch/IntPhys2
- **MVPBench** — shortcut-aware physical video QA through minimal video pairs. Paper: https://arxiv.org/abs/2506.09987 · Official: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- **CausalVQA** — causal/counterfactual/hypothetical physical video reasoning. Official: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- **RoboPhys-3D** — state/execution-grounded physical evaluation for embodied world models. Paper: https://arxiv.org/abs/2608.28718

## Sparse / event-based computation

- **Motion-aware Event Suppression** — sparse high-rate visual processing and downstream compute reduction. Paper: https://arxiv.org/abs/2602.23204

## Broad surveys

- **Aligning Perception, Reasoning, Modeling and Interaction: A Survey on Physical AI** — Paper: https://arxiv.org/abs/2510.04978 · Resource: https://github.com/AI4Phys/Awesome-AI-for-Physics
- **World-Action Models for Robot Learning and Control: A Survey** — Paper: https://arxiv.org/abs/2609.16074

## Reading order for Clover

### Tier 1 — representation

V-JEPA 2/2.1 → Interpreting Physics → VGGT/VGGT-Ω → ReWAM → VISTA → Identifiable World Models.

### Tier 2 — robot-brain alternatives

Gemini Robotics ER 2 → π0.5/OpenVLA → Being-H/M0.7 → Helix 2.5 → Skild S1 → H-WM/HWAM.

### Tier 3 — foundations

ORB-SLAM3/RAFT → Slot Attention → DreamerV3/TD-MPC2 → active perception/POMDP literature.

### Tier 4 — evaluation

IntPhys 2 → MVPBench → CausalVQA → RoboPhys-3D → real long-horizon unseen-environment robot tasks.

The purpose of reading is not to find a framework to import. It is to determine what the next Clover hypothesis must explain that these methods do not already solve.

# Clover Model & Literature Index

Last verified: 2026-10-14

This is a navigation index, not a ranking. Closed-system results are marked as vendor-reported when appropriate.

| Work | Area | Main contribution relevant to Clover | Public artifact | Evidence note |
|---|---|---|---|---|
| ORB-SLAM3 | classical geometry | persistent visual geometry / relocalization / maps | https://github.com/UZ-SLAMLab/ORB_SLAM3 | open code |
| RAFT | motion | learned optical flow estimator | https://github.com/princeton-vl/RAFT | open code |
| DINOv2 | image SSL | robust generic visual features | https://github.com/facebookresearch/dinov2 | open code/models |
| Slot Attention | object-centric | exchangeable object slots | https://arxiv.org/abs/2006.15055 | paper; ecosystem implementations |
| SAM 2 | video entities | segmentation with streaming memory | https://ai.meta.com/research/sam2/ | open code/models |
| V-JEPA 2 | video world model | action-free video SSL; prediction/planning bridge | https://github.com/facebookresearch/vjepa2 | open code/models |
| V-JEPA 2.1 | dense video SSL | temporally consistent dense features | https://github.com/facebookresearch/vjepa2 | open code/models |
| Interpreting Physics in Video World Models | interpretability | probes distributed physical variables | https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/ | primary paper |
| VGGT | spatial intelligence | feed-forward camera/depth/point-map/track inference | https://github.com/facebookresearch/vggt | open code/models |
| VGGT-Ω | spatial intelligence | scalable static/dynamic reconstruction | https://github.com/facebookresearch/vggt-omega | training/repro materials public |
| DUSt3R | learned geometry | point-map multi-view reconstruction | https://arxiv.org/abs/2312.14132 | paper/code ecosystem |
| Atlas | general world model | reconstruction + generation + simulation | https://www.worldlabs.ai/blog/atlas | vendor technical release |
| Cosmos 3 | physical AI | reasoning + generation + action in one open model family | https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai/ | NVIDIA-reported/open ecosystem |
| RT-2 | VLA | web VLM knowledge to action | https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/ | paper/project |
| OpenVLA | VLA | open-source VLA baseline | https://github.com/openvla/openvla | open code/models |
| π0.5 | VLA | open-world home generalization through heterogeneous co-training | https://www.pi.website/blog/pi05 | paper + vendor experiments |
| Gemini Robotics ER 2 | embodied reasoning | high-level physical reasoning/planning brain | https://deepmind.google/models/gemini-robotics/embodied-reasoning/ | official model card/product access |
| Gemini Robotics 2 | VLA | lower-level robot action model | https://deepmind.google/models/gemini-robotics/ | official system |
| Helix 2.5 | robot foundation model | reported zero-shot 30-home whole-body generalization | https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization | vendor-reported real robot study |
| Skild S1 | robot foundation model | in-context learning from video demonstrations | https://www.skild.ai/blogs/s1 | vendor technical report |
| Open X-Embodiment | robot data | cross-embodiment dataset and transfer | https://github.com/google-deepmind/open_x_embodiment | open data tooling/models |
| LIBERO | lifelong robotics | knowledge transfer over task sequences | https://libero-project.github.io/main.html | open benchmark |
| CALVIN | long-horizon control | language-conditioned multi-step manipulation | https://github.com/mees/calvin | open benchmark |
| Perception Test | video benchmark | tracking, memory, physics, semantics | https://github.com/google-deepmind/perception_test | open benchmark |

## Reading priority now

The current project phase is **research before reproduction**. Read for the representation and learning assumptions first; implementation comparison comes later.

### Tier A — central to the world-representation question

1. V-JEPA 2 / 2.1
2. VGGT / VGGT-Ω
3. classical multi-view geometry / SLAM
4. object-centric representation
5. mechanistic interpretation of video models

### Tier B — central to the robot-brain/product question

1. Gemini Robotics ER 2
2. π0.5
3. Helix 2.5
4. Skild S1
5. OpenVLA

### Tier C — evaluation and long-term learning

1. IntPhys 2 / MVPBench / CausalVQA
2. Perception Test
3. LIBERO / CALVIN / RoboCasa
4. Ego4D / DROID / Open X-Embodiment

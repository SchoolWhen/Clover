# Clover Research Map

This map is organized around approaches to the question:

> **How can a machine understand the real world through vision alone?**

The goal is not to rank camps prematurely. Each area is studied for its representation, learning mechanism, treatment of time/physics/memory, demonstrated capability and unresolved limitations.

## Areas

- [Classical vision and geometry](classical-vision.md)
- [Video and world models](video-world-models.md)
- [Spatial intelligence](spatial-intelligence.md)
- [Object-centric representation](object-centric-representation.md)
- [Embodied reasoning and VLA](embodied-reasoning.md)
- [Robot foundation models](robot-foundation-models.md)
- [Active perception](active-perception.md)
- [Causality](causality.md)
- [Lifelong learning](lifelong-learning.md)

## Representative systems currently tracked

| Area | Representative work | Why it matters to Clover |
|---|---|---|
| Classical geometry | ORB-SLAM3, SfM/BA, optical flow | Shows what explicit geometry already solves |
| Generic visual SSL | DINOv2 | Strong learned visual representation without robot actions |
| Video world representation | V-JEPA, V-JEPA 2/2.1 | Directly targets understanding, prediction and planning from video |
| Learned geometry | DUSt3R, VGGT, VGGT-Ω | Tests whether scalable reconstruction is a route to spatial understanding |
| Object-centric | Slot Attention and successors | Alternative to dense latent or field representations |
| Video entities | SAM 2 | Strong segmentation/memory baseline for persistent visual entities |
| Embodied reasoning | Gemini Robotics ER 2 | High-level physical reasoning / planning as a robotic brain layer |
| VLA | RT-2, OpenVLA, π0.5, Gemini Robotics 2 | Direct vision/language-to-action alternative to persistent world state |
| Robot foundation models | Figure Helix 2.5, Skild S1 | Real long-horizon generalization capability targets |
| General spatial world models | World Labs Atlas, NVIDIA Cosmos | Generative/reconstructive alternatives for world representation |

## Source index

Primary links are kept in the topic pages. Representative starting points:

- V-JEPA 2: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- V-JEPA 2 code: https://github.com/facebookresearch/vjepa2
- VGGT: https://github.com/facebookresearch/vggt
- VGGT-Ω: https://vggt-omega.github.io/
- Gemini Robotics: https://deepmind.google/models/gemini-robotics/
- OpenVLA: https://github.com/openvla/openvla
- Figure Helix 2.5: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1: https://www.skild.ai/blogs/s1
- World Labs Atlas: https://www.worldlabs.ai/blog/atlas
- NVIDIA Cosmos: https://www.nvidia.com/en-us/ai/cosmos/

This map will be expanded through structured literature notes rather than daily-news accumulation.

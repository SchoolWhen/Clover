# Source Map — Evidence → Research Question → Clover Landing

Last updated: 2026-10-14

This file maps important external evidence to the exact Clover research question it constrains. It is designed for fast review and to prevent source drift.

Evidence labels:

- `PRIMARY_PAPER` — peer-reviewed paper or primary preprint.
- `OFFICIAL_PROJECT` — official project/model/research page.
- `OPEN_SOURCE` — public code/checkpoint/resource.
- `OFFICIAL_REPORTED_RESULT` — company/lab result not independently reproduced here.
- `BACKGROUND_REFERENCE` — foundational book/review/historical source.

A source appearing here does **not** mean its mechanism is adopted.

---

## 1. Foundations: partial observability, uncertainty, active perception

| Source | URL | Evidence | What it constrains | Clover landing |
|---|---|---|---|---|
| POMDPs in Robotics survey | https://arxiv.org/abs/2209.10342 | `PRIMARY_PAPER` | Real robot state is often partially observable; belief/state uncertainty is a first-class decision variable. | `BACKGROUND_RESEARCH.md` §1; `RESEARCH_QUESTIONS.md` observability/active perception |
| Probabilistic Robotics | https://mitpress.mit.edu/9780262201629/probabilistic-robotics/ | `BACKGROUND_REFERENCE` | Bayesian state estimation, localization and mapping under uncertainty. | Geometry/state-estimation background |
| Bajcsy, Active Perception | https://ieeexplore.ieee.org/abstract/document/5968 | `BACKGROUND_REFERENCE` | Perception includes selecting sensing actions to gain information. | Active-perception domain and V3 protocol |
| Spelke et al., Origins of Knowledge | https://pubmed.ncbi.nlm.nih.gov/1454901/ | `BACKGROUND_REFERENCE` | Continuity and solidity are useful object/physics research dimensions. | Intuitive-physics taxonomy |
| Physics for infants review | https://pubmed.ncbi.nlm.nih.gov/26302470/ | `BACKGROUND_REFERENCE` | Reviews continuity, solidity, cohesion and object/substance reasoning. | Benchmark interpretation; not a mandate to copy human cognition |

---

## 2. Classical geometry and motion

| Source | URL | Evidence | Demonstrates | Does not establish | Clover landing |
|---|---|---|---|---|---|
| Multiple View Geometry | https://www.robots.ox.ac.uk/~vgg/hzbook/ | `BACKGROUND_REFERENCE` | Projective/multi-view geometry has explicit mathematical structure. | Semantics, physics, causality. | Classical geometry background |
| ORB-SLAM3 paper | https://arxiv.org/abs/2007.11898 | `PRIMARY_PAPER` | Explicit pose/map/trajectory estimation, relocalization, multi-map reuse. | Open-world world understanding. | Classical baseline |
| ORB-SLAM3 code | https://github.com/UZ-SLAMLab/ORB_SLAM3 | `OPEN_SOURCE` | Reproducible SLAM baseline. | — | Baseline setup |
| RAFT paper | https://arxiv.org/abs/2003.12039 | `PRIMARY_PAPER` | Strong dense optical flow / temporal correspondence. | Identity, permanence, causal state. | Motion baseline |
| RAFT code | https://github.com/princeton-vl/RAFT | `OPEN_SOURCE` | Reproducible flow baseline. | — | Baseline setup |

---

## 3. Static self-supervised visual representation

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| DINOv3 research | https://ai.meta.com/research/publications/dinov3/ | `OFFICIAL_PROJECT` | Large-scale label-free image SSL; strong frozen dense features. | How much world structure still requires time/state? | `FRONTIER_METHODS.md`; generic visual baseline |
| DINOv3 paper | https://arxiv.org/abs/2508.10104 | `PRIMARY_PAPER` | 7B-scale SSL, 1.7B-image training, broad dense-task performance. | Static representation vs persistent world model. | Baseline/probing |
| DINOv3 code | https://github.com/facebookresearch/dinov3 | `OPEN_SOURCE` | Current reproducible Meta SSL baseline. | — | `DATASETS_CODE.md` |
| DINOv2 paper | https://arxiv.org/abs/2304.07193 | `PRIMARY_PAPER` | Historical predecessor and established SSL baseline. | Superseded as primary current static SSL comparator by DINOv3. | Historical comparison |

---

## 4. Predictive video representation and learned physical structure

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| V-JEPA 2 research | https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/ | `OFFICIAL_PROJECT` | Web-scale video SSL plus small robot post-training can support planning. | Does latent predictive state replace explicit state? | Video-world baseline |
| V-JEPA 2 paper | https://arxiv.org/abs/2506.09985 | `PRIMARY_PAPER` | Understanding, anticipation and action-conditioned planning. | What is encoded and how persistent is it? | Baseline/probing |
| V-JEPA 2 code | https://github.com/facebookresearch/vjepa2 | `OPEN_SOURCE` | Reproducible pretrained baseline. | — | `DATASETS_CODE.md` |
| V-JEPA 2.1 | https://arxiv.org/abs/2603.14482 | `PRIMARY_PAPER` | Dense, spatially structured and temporally consistent SSL features. | Dense latent vs explicit/entity state. | `FRONTIER_METHODS.md` |
| Interpreting Physics in Video World Models | https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/ | `PRIMARY_PAPER` | Physical variables can emerge as distributed/high-dimensional population codes. | Compact explicit physics variables are not automatically necessary. | Explicit-vs-distributed contradiction |

---

## 5. Learned geometry and spatial reconstruction

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| DUSt3R | https://arxiv.org/abs/2312.14132 | `PRIMARY_PAPER` | Learned point-map reconstruction bridges learned and classical geometry. | Learned vs explicit geometry division of labor. | Geometry map |
| VGGT | https://arxiv.org/abs/2503.11651 | `PRIMARY_PAPER` | Cameras, depth, point maps and tracks from image sets. | Reconstruction vs world understanding. | Spatial baseline |
| VGGT code | https://github.com/facebookresearch/vggt | `OPEN_SOURCE` | Reproducible learned geometry. | — | Baseline setup |
| VGGT-Ω | https://arxiv.org/abs/2605.15195 | `PRIMARY_PAPER` | Scaled static/dynamic reconstruction; scene registers help VLA/language alignment. | Is reconstruction a sufficient spatial proxy? | Primary learned-geometry baseline |
| VGGT-Ω project | https://vggt-omega.github.io/ | `OFFICIAL_PROJECT` | Project/evaluation resources. | — | `PAPERS.md` / `DATASETS_CODE.md` |
| VGGT-Ω code | https://github.com/facebookresearch/vggt-omega | `OPEN_SOURCE` | Reproducibility resource. | — | Baseline setup |

---

## 6. Object-centric representation and visible entity tracking

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| Slot Attention | https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html | `PRIMARY_PAPER` | Exchangeable object-like slots and compositional generalization. | Scaling and real-world object discovery. | Object-centric route |
| PLATO | https://www.nature.com/articles/s41562-022-01394-8 | `PRIMARY_PAPER` | Object-centric inductive bias can support intuitive-physics learning. | Whether object-centric state is necessary at scale. | Physics/object comparison |
| SAM 3 research | https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/ | `PRIMARY_PAPER` | Open-vocabulary detection, segmentation and video tracking. | Visible tracking is not object permanence. | Perception baseline |
| SAM 3.1 code | https://github.com/facebookresearch/sam3 | `OPEN_SOURCE` | Current code/checkpoints for SAM 3/3.1. | — | `DATASETS_CODE.md` |
| SAM 3.1 release | https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md | `OPEN_SOURCE` | Current multi-object tracking efficiency improvements. | Does not create hidden-state permanence. | Primary contemporary tracking comparator |

---

## 7. Persistent visual memory

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| PersistBench paper | https://arxiv.org/abs/2609.20819 | `PRIMARY_PAPER` | 4D/world models lose object permanence, motion continuity and appearance consistency after objects leave view. | Seeing/reconstruction vs remembering. | Memory battery |
| PersistBench project/code | https://guangzhaohe.com/persistbench | `OPEN_SOURCE` | Dataset/metric access. | — | `BENCHMARKS_TASKS.md` |
| S-EMBER research | https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/ | `OFFICIAL_PROJECT` | Streaming grounded episodic retrieval exposes temporal localization gap. | Long context/scale vs grounded recall. | Memory battery |
| S-EMBER paper | https://arxiv.org/abs/2607.02689 | `PRIMARY_PAPER` | 388 h streaming egocentric benchmark with temporal evidence localization. | Memory architecture remains open. | `BENCHMARKS_TASKS.md` |
| VISTA | https://arxiv.org/abs/2610.02200 | `PRIMARY_PAPER` | Memory/evidence harness can be varied independently from model weights. | Replay vs recurrent/latent memory. | Evidence Replay hypothesis comparator |

---

## 8. Physics and anti-shortcut evaluation

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| IntPhys 2 | https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ | `PRIMARY_PAPER` | Permanence, immutability, continuity and solidity remain difficult. | Synthetic intuitive physics vs real-world transfer. | Understanding Battery |
| IntPhys 2 code | https://github.com/facebookresearch/IntPhys2 | `OPEN_SOURCE` | Reproducible benchmark. | — | Battery setup |
| MVP / Minimal Video Pairs | https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/ | `PRIMARY_PAPER` | Minimal pairs reveal shortcut-based physical reasoning. | QA still mixes language and visual evidence. | Anti-shortcut policy |
| Principia | https://arxiv.org/abs/2609.04200 | `PRIMARY_PAPER` | Relational physics can be tested without absolute calibration; current generators/VLMs remain weak. | Relational consistency vs executable physical state. | Physics battery |
| RoboPhys-3D | https://arxiv.org/abs/2608.28718 | `PRIMARY_PAPER` | State/execution-grounded metrics expose failures missed by appearance/VLM metrics. | How much 3D-grounded state predicts real task success. | World-model evaluation |

---

## 9. Causality and intervention

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| CausalVQA | https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/ | `PRIMARY_PAPER` | Real-video counterfactual, hypothetical, anticipation and planning questions remain difficult. | Language QA vs machine-native causal state. | Causal battery |
| CRL identifiability — Varici et al. | https://proceedings.mlr.press/v238/varici24a.html | `PRIMARY_PAPER` | Interventions can make latent causal models identifiable under stated assumptions. | What intervention structure is available to a robot. | Theory background |
| CRL multi-node interventions | https://proceedings.mlr.press/v236/bing24a | `PRIMARY_PAPER` | Extends identifiability analysis to multi-node interventions. | Passive-video-only causality remains underconstrained. | Active interaction rationale |

---

## 10. Active perception

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| Bajcsy, Active Perception | https://ieeexplore.ieee.org/abstract/document/5968 | `BACKGROUND_REFERENCE` | Perception can select actions that reduce uncertainty. | How to learn information value end-to-end. | V3 protocol |
| Vantage | https://arxiv.org/abs/2610.11810 | `PRIMARY_PAPER` | View planning/evidence acquisition can improve spatial reasoning. | General active world learning. | Active-perception benchmark |
| Vantage code | https://github.com/q1xiangchen/Vantage | `OPEN_SOURCE` | Reproducibility resource. | — | Baseline setup |

---

## 11. Generative spatial/world models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| World Labs Atlas | https://www.worldlabs.ai/blog/atlas | `OFFICIAL_REPORTED_RESULT` | Unified generation, reconstruction and space-time simulation with spatial context. | Plausible completion vs evidence-grounded belief. | Generative world-model route |
| World-model taxonomy | https://www.worldlabs.ai/blog/taxonomy-of-world-models | `OFFICIAL_PROJECT` | Clarifies renderer/simulator/planner functions commonly conflated as “world model.” | Taxonomy is not independent empirical validation. | Terminology background |
| Cosmos 3 project | https://research.nvidia.com/labs/cosmos-lab/cosmos3/ | `OFFICIAL_PROJECT` | Open omnimodal world-model family spanning reasoning, generation and action. | General benchmark strength vs robust persistent world truth. | Generative/WAM comparator |
| Cosmos 3 report | https://arxiv.org/abs/2606.02800 | `PRIMARY_PAPER` | Unifies language/image/video/audio/action in one architecture. | Whether unified generation/action is sufficient for robot belief. | Frontier method map |
| Cosmos code | https://github.com/nvidia/cosmos | `OPEN_SOURCE` | Public implementation/checkpoints/resources. | — | `DATASETS_CODE.md` |

---

## 12. VLA, embodied reasoning and robot foundation models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| OpenVLA | https://arxiv.org/abs/2406.09246 | `PRIMARY_PAPER` | Open 7B VLA trained on 970k robot demonstrations. | Direct policy vs persistent world state. | Open action baseline |
| OpenVLA code | https://github.com/openvla/openvla | `OPEN_SOURCE` | Fine-tuning/evaluation access. | — | Future embodied baseline |
| π0.5 | https://arxiv.org/abs/2504.16054 | `PRIMARY_PAPER` | Long-horizon manipulation in entirely new homes with heterogeneous multimodal co-training. | Visual understanding vs language/semantic/action priors. | Strong direct-policy falsifier |
| π0.5 project | https://www.pi.website/blog/pi05 | `OFFICIAL_PROJECT` | Qualitative/system context. | — | Robot foundation map |
| Gemini Robotics ER 2 | https://deepmind.google/models/gemini-robotics/embodied-reasoning/ | `OFFICIAL_PROJECT` | High-level physical/spatial reasoning separated from lower-level VLA execution. | Persistent world-state semantics remain unspecified publicly. | Hierarchical embodied comparator |
| Gemini ER 2 model card | https://deepmind.google/models/model-cards/gemini-robotics-er-2/ | `OFFICIAL_PROJECT` | Inputs, outputs, model dependency and limitation documentation. | — | Source of truth for claims |
| Gemini Robotics 2 | https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/ | `OFFICIAL_REPORTED_RESULT` | Whole-body VLA/control capabilities. | Independent reproducibility. | Robot-brain landscape |
| Figure Helix 2.5 | https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization | `OFFICIAL_REPORTED_RESULT` | Reports zero-shot long-horizon whole-body tasks across 30 unseen homes; controlled pretraining ablation. | Closed system; no independent Clover reproduction. | Generalization reference |
| Skild S1 | https://www.skild.ai/blogs/s1 | `OFFICIAL_REPORTED_RESULT` | Reports in-context robot learning from video demonstrations and long-horizon unseen tasks. | Closed-system evidence. | Long-horizon/direct-policy reference |
| Skild general-purpose brain | https://skild.ai/blogs/building-the-general-purpose-robotic-brain | `OFFICIAL_PROJECT` | Omni-bodied foundation-model thesis. | Does not establish world-state representation requirements. | Embodiment-invariance question |

---

## 13. World-action models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| WAM survey | https://arxiv.org/abs/2609.16074 | `PRIMARY_PAPER` | Taxonomy linking future-state modeling and executable action generation. | Which factorization is actually necessary. | WAM research map |
| WAM resource index | https://rcl-robotics.github.io/Awesome-World-Action-Models | `OFFICIAL_PROJECT` | Current paper/resource map. | Curation is not evaluation. | Frontier tracking |
| HWAM | https://arxiv.org/abs/2610.12026 | `PRIMARY_PAPER` | Explicitly models reference action vs realized state/action gap. | Whether joint state-action generation is best generally. | Execution-gap comparator |
| Being-M0.7 | https://arxiv.org/abs/2610.11283 | `PRIMARY_PAPER` | Transfers visual-motion priors from large human data before humanoid adaptation. | Human-motion priors vs learned world state. | Human-video route |
| ReWAM | https://arxiv.org/abs/2609.38163 | `PRIMARY_PAPER` | Action-grounded representation shaping challenges reconstruction-only objectives. | What state is minimally sufficient for action. | Reconstruction-vs-action contradiction |

---

## 14. Repository policy for adding new sources

Every new source should record:

```text
source
→ evidence level
→ exact URL
→ demonstrated capability
→ limitation / what it does not establish
→ research contradiction
→ Clover landing file
```

Do not add a paper only because it is recent. Do not use a news summary when a primary paper or official source is available. `news(5).md` remains a discovery/signal archive; durable claims must graduate to primary or official evidence before entering the main Survey.

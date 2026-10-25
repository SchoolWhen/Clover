<a id="top"></a>

# Research map

Maintained: **2026-10-25** · Current project stage: **Research** ([status](STATUS.md)).

The broad problem space, competing research families and breadth coverage. Read the current collection queue before adding more names.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<a id="current-collection-queue"></a>

## 当前调研结论与待补证据

本轮核验日期：2026-10-25。继续 Stage 1；原研究问题与长期目标不变。

| 资料缺口 | 当前新增证据 | 尚未闭合的更强问题 |
|---|---|---|
| 被动 RGB 镜面外观锚点 | [Ref-NeRF / NeRFactor](PERCEPTION.md#reflection-evidence) | 相机/视角/光照/材质先验各贡献多少；渲染拟合何时支持真实物理分解？ |
| 未知交互目标与真实成像 | [BISCUIT / 真实光学负结果](ACTION.md#causal-identification-evidence) | 可识别性假设在噪声、遮挡、混杂与自然机器人视频中是否成立？ |
| 视觉压缩效率参照 | [FastV / FrameFusion](REPRESENTATION.md#compression-evidence) | 未知后续任务需要的短暂历史证据是否丢失；还能否安全再观察？ |

下一轮优先：RGB-only 可变形/颗粒状态；自然真实机器人视频的因果恢复；同字节/时延预算下的延迟提问与证据恢复；封闭原文的合法全文入口。先登记来源与反例，再决定后续区分实验。不能用“没搜到”推出领域不存在，也不能把定理充分条件改写为全域不可能性。具体版本、阅读深度和检索词见 [新增来源](SOURCES.md#verified-additions)。

## Contents

- [Research](#topic-research-research)
- [Background Research Foundation](#topic-research-survey-background_research)
- [SURVEY_BREADTH — Breadth Foundation for Stage-1 Research](#topic-survey_breadth)

<a id="topic-research-research"></a>

## Research

### Survey, Discovery and Evidence Collection

Source record updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

This is the primary file for the current stage.

The purpose of Stage 1 is **coverage before commitment**. We want to know what relevant directions exist, who is working on them, what methods currently represent the frontier, what datasets and benchmarks exist, what code is reproducible, and where the strongest unresolved questions remain.

This file is deliberately broad and relatively flat so a new research agent can understand the landscape before entering deeper documents.

Detailed mechanism reports belong to Stage 2 [`PROCESS.md`](PROCESS.md#topic-research-analysis), not here.

---

### 1. Research-source record

Every durable entry should preserve, when available:

```text
name
research direction
primary paper URL
official project URL
official code URL
dataset / benchmark URL
year / version
evidence level
visual protocol V0–V3
learning provenance L0–L4
one-sentence demonstrated capability
one-sentence limitation / unresolved question
```

Evidence labels:

- `PRIMARY_PAPER`
- `OFFICIAL_PROJECT`
- `OPEN_SOURCE`
- `OFFICIAL_REPORTED_RESULT`
- `BACKGROUND_REFERENCE`
- `SURVEY_SIGNAL`

Research-stage inclusion means **relevant enough to study**, not adopted by Clover.

---

### 2. Broad research inventory

The mother question touches substantially more than “world models” or “VLA.” The working inventory currently contains the following directions.

### R01 — Epistemology, inverse problems and partial observability

Why it matters: images are observations generated from hidden physical state; pixels do not uniquely identify every property of the world.

Study:

- inverse problems;
- observability;
- uncertainty;
- Bayesian belief state;
- POMDPs;
- ambiguity and indistinguishability;
- observed vs inferred vs unobserved state.

Sources:

- POMDPs in Robotics survey — https://arxiv.org/abs/2209.10342
- Probabilistic Robotics — https://mitpress.mit.edu/9780262201629/probabilistic-robotics/
- Active Perception — https://ieeexplore.ieee.org/abstract/document/5968

Current question: what can vision establish, what can it only infer, and what requires more evidence or action?

---

### R02 — Human vision, developmental cognition and core physical knowledge

Why it matters: human developmental results provide hypotheses about useful capabilities such as continuity, solidity, object permanence and cohesion. They are evidence about problems worth studying, not architecture blueprints.

Study:

- object permanence;
- continuity;
- solidity;
- intuitive physics;
- perceptual organization;
- predictive processing;
- active visual exploration.

Sources:

- Origins of Knowledge — https://pubmed.ncbi.nlm.nih.gov/1454901/
- Physics for infants review — https://pubmed.ncbi.nlm.nih.gov/26302470/

Current question: which apparently “core” capabilities are useful computational targets, and which are human-specific priors that should not be copied blindly?

---

### R03 — Classical projective and multi-view geometry

Study:

- camera models;
- epipolar geometry;
- triangulation;
- PnP;
- bundle adjustment;
- structure from motion;
- stereo;
- visual odometry;
- SLAM.

Sources:

- Multiple View Geometry — https://www.robots.ox.ac.uk/~vgg/hzbook/
- ORB-SLAM3 — https://arxiv.org/abs/2007.11898
- ORB-SLAM3 code — https://github.com/UZ-SLAMLab/ORB_SLAM3

Current question: which parts of “world structure” already have precise mathematical solutions and therefore should not be rediscovered unnecessarily?

---

### R04 — Motion estimation, correspondence and tracking

Study:

- optical flow;
- feature correspondence;
- point tracks;
- multi-object tracking;
- video segmentation;
- visible entity continuity.

Sources:

- RAFT — https://arxiv.org/abs/2003.12039
- RAFT code — https://github.com/princeton-vl/RAFT
- SAM 3 — https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
- SAM 3 / 3.1 code — https://github.com/facebookresearch/sam3

Important distinction:

```text
tracking while visible
≠
object permanence while not visible
```

---

### R05 — Static self-supervised visual representation

Study:

- invariance;
- dense visual features;
- semantic emergence;
- part structure;
- representation scaling;
- frozen-backbone transfer.

Current reference:

- DINOv3 — https://arxiv.org/abs/2508.10104
- DINOv3 research page — https://ai.meta.com/research/publications/dinov3/
- DINOv3 code — https://github.com/facebookresearch/dinov3

Historical anchors:

- DINOv2 — https://arxiv.org/abs/2304.07193
- I-JEPA — https://arxiv.org/abs/2301.08243
- CLIP — https://arxiv.org/abs/2103.00020

Current question: how far can a static representation go before persistent temporal state becomes necessary?

---

### R06 — Predictive video representation and latent world prediction

Study:

- temporal representation;
- latent prediction;
- future state;
- temporal consistency;
- physical-variable emergence;
- action-conditioned post-training.

Sources:

- V-JEPA — https://arxiv.org/abs/2404.08471
- V-JEPA 2 — https://arxiv.org/abs/2506.09985
- V-JEPA 2 code — https://github.com/facebookresearch/vjepa2
- V-JEPA 2.1 — https://arxiv.org/abs/2603.14482
- Interpreting Physics in Video World Models — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Current question: can a distributed predictive latent become sufficient world state without an explicit persistent model?

---

### R07 — Learned geometry foundation models

Study:

- point maps;
- learned camera recovery;
- learned depth;
- large-scale multi-view reconstruction;
- dynamic reconstruction;
- learned geometry vs classical geometry.

Sources:

- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651
- VGGT code — https://github.com/facebookresearch/vggt
- VGGT-Ω — https://arxiv.org/abs/2605.15195
- VGGT-Ω project — https://vggt-omega.github.io/
- VGGT-Ω code — https://github.com/facebookresearch/vggt-omega

Current question: is reconstruction a strong enough proxy for spatial understanding, or only one component of it?

---

### R08 — Neural scene representations, NeRF, Gaussian Splatting and 4D reconstruction

Study:

- NeRF;
- 3D Gaussian Splatting;
- dynamic NeRF / dynamic 3DGS;
- 4D representation;
- appearance vs geometry vs motion representation;
- persistent scene memory.

Sources:

- NeRF — https://arxiv.org/abs/2003.08934
- 3D Gaussian Splatting — https://arxiv.org/abs/2308.04079
- Reconstructing the Dynamic World: A Representation-Centric View of 4D Scene Reconstruction — https://arxiv.org/abs/2609.39960

Current question: when a model can render/reconstruct an evolving scene, which world-understanding properties still remain missing?

---

### R09 — Object-centric representation

Study:

- slots;
- object files;
- entity binding;
- compositional representation;
- object discovery;
- object-centric dynamics.

Sources:

- Slot Attention — https://arxiv.org/abs/2006.15055
- PLATO — https://www.nature.com/articles/s41562-022-01394-8
- Object-centric robotic manipulation survey — https://arxiv.org/abs/2408.11537

Current question: are objects necessary primitives, emergent abstractions, query-dependent structures, or merely one useful factorization?

---

### R10 — Scene graphs, relational state and semantic mapping

Study:

- object-relation graphs;
- spatial scene graphs;
- semantic maps;
- open-vocabulary 3D maps;
- persistent relational memory;
- viewpoint-dependent spatial relations.

Current source:

- EmbodimentSemantic — https://arxiv.org/abs/2607.00020

Related direction:

- semantic 3D Gaussian grounding for manipulation — https://arxiv.org/abs/2608.10756

Current question: when does explicit relational structure improve reasoning or action beyond dense features?

---

### R11 — Persistent visual memory and episodic memory

Study:

- long-video memory;
- streaming memory;
- evidence retrieval;
- object permanence;
- event memory;
- memory compression;
- retrieval vs recurrent state;
- raw evidence vs world-state memory.

Sources:

- PersistBench — https://arxiv.org/abs/2609.20819
- PersistBench project — https://guangzhaohe.com/persistbench
- S-EMBER — https://arxiv.org/abs/2607.02689
- VISTA — https://arxiv.org/abs/2610.02200

Current question: is long context enough, or does robust world understanding require a persistent and revisable memory abstraction?

---

### R12 — Belief revision, contradiction and forgetting

Study:

- update under contradictory evidence;
- stale memory;
- selective forgetting;
- catastrophic forgetting;
- local vs global revision;
- evidence provenance;
- continual world update.

This direction overlaps memory, epistemology and continual learning but should remain visible as its own problem.

Current question: can a machine change its world model cleanly when the real world changes?

---

### R13 — Intuitive physical reasoning

Study:

- object permanence;
- continuity;
- solidity;
- support;
- collision;
- physically plausible change;
- shortcut-resistant physical judgment.

Sources:

- IntPhys 2 — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- IntPhys 2 code — https://github.com/facebookresearch/IntPhys2
- Minimal Video Pairs — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Current question: does a model understand physical constraints or only recognize common-looking motion patterns?

---

### R14 — Quantitative and relational physics

Study:

- velocity;
- acceleration;
- relative quantities;
- conservation-like constraints;
- calibration-free physical relations;
- measurable dynamics.

Sources:

- Principia — https://arxiv.org/abs/2609.04200
- QuantiPhy — retain as a tracked quantitative-physics benchmark family; verify the primary project/paper before treating any individual claim as settled.
- RoboPhys-3D — https://arxiv.org/abs/2608.28718

Current question: can visually learned systems reason about physical variables beyond qualitative plausibility?

---

### R15 — Physics-informed / differentiable / structured world models

Study:

- differentiable physics;
- conservation constraints;
- structured latent dynamics;
- 3D physical fields;
- physics-principled prediction;
- hybrid learned + analytical models.

Current example:

- PhysMani — https://arxiv.org/abs/2607.01938

Current question: when should physical structure be imposed, learned, or inferred dynamically?

---

### R16 — Causal representation learning and identifiability

Study:

- causal variables;
- interventions;
- latent causal discovery;
- identifiability;
- observational equivalence;
- partially observable causality.

Sources:

- Causal Representation Learning from Multiple Distributions / interventions — https://proceedings.mlr.press/v238/varici24a.html
- Multi-node interventions — https://proceedings.mlr.press/v236/bing24a

Current question: which causal structure can passive visual observation identify, and what fundamentally requires intervention?

---

### R17 — Counterfactual and causal visual reasoning

Study:

- “what if” reasoning;
- causal event attribution;
- anticipation;
- intervention twins;
- counterfactual consistency.

Source:

- CausalVQA — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Current question: does a system encode causal mechanisms, or generate linguistically plausible explanations after the fact?

---

### R18 — Active perception and next-best-view

Study:

- information gain;
- viewpoint planning;
- ambiguity reduction;
- active camera movement;
- question-conditioned sensing;
- active evidence acquisition.

Sources:

- Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage — https://arxiv.org/abs/2610.11810
- Vantage code — https://github.com/q1xiangchen/Vantage

Current question: can the system know what it does not know well enough to decide what to look at next?

---

### R19 — Active interaction, system identification and learning action consequences

Study:

- action → observation;
- controllability;
- intervention;
- system identification;
- online dynamics learning;
- action-conditioned state transitions.

This is different from adding non-visual sensors: under `V3`, action may change future evidence while the sensory evidence remains visual.

Current question: what knowledge becomes learnable only when the agent changes the world or viewpoint?

---

### R20 — Generative world models and spatial simulation

Study:

- video generation;
- spatial generation;
- world simulation;
- controllable generation;
- hidden-region completion;
- generative planning.

Sources:

- World Labs Atlas — https://www.worldlabs.ai/blog/atlas
- World Labs world-model taxonomy — https://www.worldlabs.ai/blog/taxonomy-of-world-models
- NVIDIA Cosmos 3 — https://arxiv.org/abs/2606.02800
- Cosmos code — https://github.com/nvidia/cosmos

Critical distinction:

```text
plausible completion
≠
evidence-grounded belief
```

---

### R21 — World-action models and future-state action models

Study:

- joint world/action prediction;
- future latent state;
- video-based world-action generation;
- state-action coupling;
- realized execution state;
- latent future planning.

Sources:

- World Model for Robot Learning survey — https://arxiv.org/abs/2605.00080
- World-Action Models survey — https://arxiv.org/abs/2609.16074
- ReWAM — https://arxiv.org/abs/2609.38163
- Being-M0.7 — https://arxiv.org/abs/2610.11283
- HWAM — https://arxiv.org/abs/2610.12026
- Inferring Action from Future Latent State / DELE-w0.5 — https://arxiv.org/abs/2608.22067

Current question: does action require dense video rollout, compact future state, or no explicit world rollout at all?

---

### R22 — Vision-language-action models and direct policies

Study:

- action tokens;
- diffusion / flow policies;
- language-conditioned robot control;
- cross-embodiment datasets;
- end-to-end policies;
- direct-policy memory.

Sources:

- RT-2 — https://arxiv.org/abs/2307.15818
- OpenVLA — https://arxiv.org/abs/2406.09246
- OpenVLA code — https://github.com/openvla/openvla
- π0.5 — https://arxiv.org/abs/2504.16054

Current question: if a direct policy behaves well without exposing a persistent world state, what additional measurable value must an explicit worldview provide?

---

### R23 — Embodied reasoning models and hierarchical robot brains

Study:

- high-level physical reasoning;
- spatial reasoning;
- task decomposition;
- success detection;
- separation between reasoning and motor control.

Sources:

- Gemini Robotics ER 2 — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Gemini Robotics ER 2 model card — https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Gemini Robotics 2 — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/

Current question: is high-level physical reasoning best represented separately from motor policy, or does the distinction disappear with scale?

---

### R24 — Robot foundation models and open-world generalization

Study:

- general-purpose robot policies;
- cross-task transfer;
- unseen homes;
- long-horizon behavior;
- in-context task learning;
- omni-bodied / cross-embodiment generalization.

Sources:

- Figure Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — https://www.skild.ai/blogs/s1
- Skild general-purpose robotic brain — https://skild.ai/blogs/building-the-general-purpose-robotic-brain

Treat these as `OFFICIAL_REPORTED_RESULT` unless independently reproduced.

---

### R25 — Human video, egocentric video and learning by watching

Study:

- egocentric video;
- human demonstrations;
- embodiment gap;
- hand-object interaction;
- learning manipulation without robot data;
- web-video physical priors.

Sources / resources:

- Ego4D — https://ego4d-data.org/
- HumanEgo — https://arxiv.org/abs/2605.24934
- Being-M0.7 — https://arxiv.org/abs/2610.11283
- Skild learning by watching — https://skild.ai/blogs/learning-by-watching

Current question: how much actionable world knowledge can be learned from human visual experience before robot-specific interaction is needed?

---

### R26 — Affordance learning and action-relevant perception

Study:

- graspability;
- support affordances;
- reachability;
- action-conditioned object representation;
- task-relevant state;
- semantic vs geometric affordance.

Related sources:

- object-centric manipulation survey — https://arxiv.org/abs/2408.11537
- Embodied multimodal grounding with Semantic-3DGS — https://arxiv.org/abs/2608.10756

Current question: should affordance be an intrinsic world property or a relation between world state and embodiment?

---

### R27 — Model-based control, planning and belief-space decision making

Study:

- model predictive control;
- planning in latent state;
- planning under uncertainty;
- belief-space planning;
- learned dynamics;
- compact control-oriented state.

Sources:

- DreamerV3 — https://arxiv.org/abs/2301.04104
- TD-MPC2 — https://arxiv.org/abs/2310.16828
- POMDP survey — https://arxiv.org/abs/2209.10342

Current question: a world representation can be predictive yet still fail to be decision-sufficient; what state is sufficient for control?

---

### R28 — Semantic memory and open-vocabulary robotics

Study:

- visual-semantic memory;
- open-vocabulary retrieval;
- semantic navigation;
- language-grounded object memory;
- ambiguity in natural-language object reference.

Source:

- OK-Robot — https://arxiv.org/abs/2401.12202
- project — https://ok-robot.github.io/

Current question: how should semantic knowledge interface with evidence-grounded world state without turning language priors into visual truth?

---

### R29 — Uncertainty, calibration and selective prediction

Study:

- calibrated confidence;
- abstention;
- selective prediction;
- epistemic vs aleatoric uncertainty;
- uncertainty under temporal prefixes;
- decision-aware uncertainty.

Current example:

- Decision-Aware Uncertainty Evaluation for VLM action anticipation — https://arxiv.org/abs/2603.10061

Current question: can the machine know when its visual conclusion is unreliable enough to refuse, inspect, or gather more evidence?

---

### R30 — Open-world recognition, OOD generalization and novelty

Study:

- unknown object;
- unknown dynamics;
- unknown composition;
- camera shift;
- environment shift;
- novelty detection;
- open-set recognition;
- test-time adaptation.

This direction should be evaluated separately from ordinary in-distribution accuracy.

Current question: what representation remains stable when both object identity and physical context change?

---

### R31 — Continual learning and lifelong adaptation

Study:

- continual self-supervision;
- online adaptation;
- catastrophic forgetting;
- replay;
- memory consolidation;
- growing world knowledge;
- concept drift.

Current question: can a robot continuously learn new visual structure without silently destroying previously useful world knowledge?

---

### R32 — Simulation, synthetic data and digital worlds

Study:

- procedural simulation;
- synthetic scenes;
- physics engines;
- digital twins;
- domain randomization;
- generated training data;
- simulator ground truth;
- sim-to-real.

Resources:

- ManiSkill — https://github.com/haosulab/ManiSkill
- RoboCasa — https://robocasa.ai/
- LIBERO — https://libero-project.github.io/main.html
- CALVIN — https://github.com/mees/calvin

Current question: which claims require controlled simulator truth, and which require real-world evidence?

---

### R33 — Large robot datasets and cross-embodiment data

Resources:

- DROID — https://droid-dataset.github.io/droid/
- Open X-Embodiment — https://github.com/google-deepmind/open_x_embodiment
- BridgeData V2 — track as an important manipulation dataset through the OpenVLA / Open X-Embodiment ecosystem.
- Ego4D — https://ego4d-data.org/

Study:

- embodiment diversity;
- camera diversity;
- task diversity;
- annotation provenance;
- robot vs human data;
- action alignment.

---

### R34 — Benchmark design and anti-shortcut evaluation

Study:

- minimal pairs;
- counterfactual pairs;
- intervention twins;
- hidden-state evaluation;
- causal evidence;
- shortcut auditing;
- contamination;
- real-world transfer;
- coverage vs correctness.

Important principle:

```text
benchmark score
≠
world understanding
```

Benchmarks are diagnostic instruments.

---

### R35 — Systems integration and compounded failure

Study:

- perception→planning error propagation;
- semantic retrieval failures;
- controller mismatch;
- action feasibility;
- long-horizon compounding errors;
- interface contracts between components.

Source:

- OK-Robot — https://arxiv.org/abs/2401.12202

Current question: are failures caused by representation itself, or by interfaces between otherwise strong components?

---

### R36 — Unified physical AI / integrated perception-reasoning-modeling-action

Surveys useful for coverage:

- Physical AI survey — https://arxiv.org/abs/2510.04978
- World Model for Robot Learning — https://arxiv.org/abs/2605.00080
- Toward Unified Robot Learning: Bridging Representation, VLA, and World Models — https://arxiv.org/abs/2609.03927

These surveys are discovery maps. Individual scientific claims should still be traced back to primary work when possible.

---

### 3. Current methods inventory — compact view

This table is intentionally short. Detailed analysis belongs to Stage 2.

| Family | Representative current references | What to collect next |
|---|---|---|
| Classical geometry | ORB-SLAM3, RAFT | exact assumptions, failure modes, observability limits |
| Static SSL | DINOv3 | dense probing, temporal limits |
| Predictive video | V-JEPA 2 / 2.1 | latent contents, temporal persistence, action conditioning |
| Learned geometry | VGGT / VGGT-Ω / DUSt3R | static vs dynamic state, failure under occlusion |
| 4D scene reconstruction | NeRF / 3DGS / 4D survey | persistence vs rendering fidelity |
| Visible tracking | SAM 3 / 3.1 | identity under occlusion / re-entry |
| Object-centric | Slot Attention / PLATO | scaling and open-world discovery |
| Persistent memory | PersistBench / S-EMBER / VISTA | memory architecture and revision |
| Physical reasoning | IntPhys 2 / MVP / Principia / RoboPhys-3D | qualitative vs quantitative physics |
| Causal learning | CausalVQA / CRL | observational vs interventional identifiability |
| Active perception | Vantage + classical active perception | information value and next-view planning |
| Generative world model | Atlas / Cosmos 3 | truth vs plausible completion |
| World-action | ReWAM / Being-M0.7 / HWAM / DELE-w0.5 | future-state representation vs video generation |
| VLA | OpenVLA / π0.5 | direct policy vs persistent world state |
| Embodied reasoning | Gemini Robotics ER 2 | language priors vs visual world state |
| Robot foundation policy | Helix 2.5 / Skild S1 | independent reproducibility, long-horizon state |
| Human video transfer | HumanEgo / Being-M0.7 | embodiment gap and visual priors |
| Model-based control | DreamerV3 / TD-MPC2 | decision-sufficient state |
| Semantic maps / scene graphs | EmbodimentSemantic / Semantic-3DGS | explicit relation utility |
| Physics-structured 3D | PhysMani | hard/soft physical priors |

---

### 4. Dataset and benchmark inventory

### Visual / video

- Ego4D — https://ego4d-data.org/
- Perception Test — https://github.com/google-deepmind/perception_test

### Robot demonstrations / embodiment

- DROID — https://droid-dataset.github.io/droid/
- Open X-Embodiment — https://github.com/google-deepmind/open_x_embodiment

### Manipulation / robot task suites

- LIBERO — https://libero-project.github.io/main.html
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/
- ManiSkill — https://github.com/haosulab/ManiSkill

### Physics / causal / memory diagnostics

- IntPhys 2 — https://github.com/facebookresearch/IntPhys2
- Minimal Video Pairs — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- CausalVQA — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- PersistBench — https://guangzhaohe.com/persistbench
- S-EMBER — https://arxiv.org/abs/2607.02689
- Principia — https://arxiv.org/abs/2609.04200
- RoboPhys-3D — https://arxiv.org/abs/2608.28718
- EmbodimentSemantic — https://arxiv.org/abs/2607.00020

During Research, collect benchmark **purpose, input modality, supervision, hidden ground truth, metrics, shortcuts and licensing**. Do not yet optimize for scores.

---

### 5. Research groups / projects to monitor

This is a monitoring list, not an endorsement ranking.

| Group / project | Why relevant | Entry point |
|---|---|---|
| Meta FAIR | DINO, JEPA, SAM, physical/video reasoning, memory benchmarks | https://ai.meta.com/research/ |
| Google DeepMind Robotics | embodied reasoning, VLA, Open X-Embodiment, Perception Test | https://deepmind.google/research/ |
| World Labs | spatial intelligence and general world models | https://www.worldlabs.ai/ |
| NVIDIA Cosmos | physical-AI world foundation models | https://research.nvidia.com/labs/cosmos-lab/ |
| Physical Intelligence | general robot policies / π family | https://www.pi.website/ |
| Figure | humanoid whole-body policy systems | https://www.figure.ai/ |
| Skild AI | general-purpose robot foundation models / self-play | https://www.skild.ai/ |
| Stanford / Berkeley robot-learning ecosystem | robot representation, manipulation, world models, imitation | track primary papers and official project pages |
| Open robot-learning community | OpenVLA, DROID, Open X-Embodiment, LIBERO, ManiSkill | use official repositories/project pages |

Prefer project/paper URLs over social-media summaries.

---

### 6. Collection gaps — explicit backlog

The current inventory is broad but not complete. Research agents should actively search for missing high-quality work in:

- open-world visual recognition and novelty detection;
- uncertainty calibration for embodied systems;
- semantic / metric neural maps;
- scene graphs and relation memory;
- active visual exploration and next-best-view;
- system identification from images;
- differentiable and hybrid physics;
- contact / friction / mass inference from RGB;
- deformable-object understanding;
- fluids, cloth and articulated objects;
- human-object interaction;
- social and multi-agent physical reasoning;
- navigation and large-scale persistent mapping;
- long-horizon household memory;
- cross-camera and cross-embodiment invariance;
- test-time adaptation;
- continual self-supervised learning;
- visual-language prior contamination;
- data leakage and benchmark shortcuts;
- quantitative physical variables;
- real-world causal intervention benchmarks;
- robust refusal / unknown-state evaluation;
- world-model truthfulness and hallucination metrics;
- efficient visual state compression;
- action-relevant representation sufficiency;
- real robot failure datasets;
- safety-relevant visual uncertainty;
- visual learning under severe occlusion and partial views;
- embodiment-independent versus embodiment-specific state.

If a new direction materially affects the mother question, add it here even if it does not fit the current eight dossiers.

---

### 7. Stage-1 exit condition

Research is broad enough to enter systematic Analysis when a new agent can answer:

1. What major research directions exist?
2. What are the strongest representative methods in each?
3. Where are their primary papers, official projects and code?
4. What datasets and benchmarks measure each capability?
5. What training evidence does each method use?
6. What is vision-only at inference versus vision-only during learning?
7. Which methods are open/reproducible and which are vendor-reported only?
8. Which important capabilities have no convincing benchmark or baseline?
9. Which current methods directly contradict assumptions in historical Clover ideas?
10. Which areas require deeper method-by-method reports in Stage 2?

The goal is not to claim that the search is permanently complete. The goal is to make the coverage sufficiently broad and traceable that later analysis does not begin from a distorted subset of the field.

---

**Current instruction: keep searching broadly. Do not freeze the answer.**

---

<a id="topic-research-survey-background_research"></a>

## Background Research Foundation

Source record updated: 2026-10-14
Phase: **Background Research / Problem Reconstruction**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

This document is the problem-space foundation for Clover after the 2026-10-14 Research Reset. It does **not** propose the next Clover architecture. It reconstructs what must be understood before a representation hypothesis is allowed to become a design commitment.

The operative sequence is:

```text
Background Research / Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
→ World Formation / Learning
→ Robot Brain
→ Real-world evaluation
→ Hardware co-design
```

Historical Clover mechanisms — field crystallization, CSP, SEP, licences, LCPS/GCPS, Visual World Compiler, CPU-first computation and related machinery — remain candidate hypotheses only.

---

### 1. Problem formulation

A camera does not observe the physical world state directly. It observes an image produced by the interaction of world state, viewpoint, visibility, lighting and sensor characteristics.

A useful abstraction is:

```text
hidden physical state S_t
+ camera/view state C_t
+ visibility/lighting/sensor process
→ visual observation O_t
```

A vision-based machine receives a history:

```text
O_1, O_2, ... O_t
```

and must construct some internal state `Z_t` that is sufficient for future queries and action.

The research problem is therefore not merely image recognition. It is:

> **What internal structure, learned or constructed from visual experience, is sufficient to support stable state estimation, identity, persistence, space, time, physics, causality, uncertainty, prediction, active evidence acquisition and action?**

This immediately makes the problem a partially observed inverse problem rather than a direct pixels→truth mapping.

Important background:

- POMDPs formalize decision-making when the real state is not directly observable: https://arxiv.org/abs/2209.10342
- Probabilistic Robotics formalizes state estimation, uncertainty, localization and mapping: https://mitpress.mit.edu/9780262201629/probabilistic-robotics/
- Active perception treats sensing as an action-selection problem rather than passive data intake: https://ieeexplore.ieee.org/abstract/document/5968

#### Core implication

```text
pixels ≠ unique world state
```

A serious world-understanding system must therefore represent some combination of:

```text
observed
inferred
predicted
ambiguous
unobserved
contradicted
```

without silently treating plausible completion as measured fact.

---

### 2. “Vision alone” needs two independent labels

The existing V0–V3 protocol describes **what sensory evidence is available at inference/evaluation time**.

#### Observation protocol

- **V0 — Strict monocular vision:** RGB + temporal order/timestamps only.
- **V1 — Calibrated monocular vision:** V0 + declared intrinsics.
- **V2 — Multi-camera vision:** calibrated RGB from multiple cameras.
- **V3 — Embodied active vision:** the agent may move to obtain new visual evidence; sensory evidence remains visual.

However, modern models may use language, robot demonstrations, proprioception or privileged simulator state during pretraining. Deployment-time visual input alone does not prove the representation was learned from vision alone.

Therefore background research should also annotate a second, orthogonal axis.

#### Learning-evidence provenance (proposed research annotation)

- **L0 — visual self-supervision only:** images/video without semantic labels or non-visual supervision.
- **L1 — visual supervision:** human labels, masks, tracks, geometry labels or other annotations derived for vision tasks.
- **L2 — language/world-knowledge supervision:** captions, text corpora, VLM pretraining, semantic internet supervision.
- **L3 — action-conditioned experience:** robot demonstrations, action labels, teleoperation, action-conditioned video.
- **L4 — non-visual/privileged physical evidence:** proprioception, force/tactile, IMU, depth/LiDAR, simulator state or equivalent privileged variables.

These are annotations, not a hierarchy of quality. They prevent a major confound:

```text
visual input at deployment
≠
knowledge learned only from vision
```

A Clover result should report both axes when relevant, for example `V0/L0`, `V1/L3`, or `V3/L3`.

---

### 3. Research domain A — classical geometry and state estimation

Before asking a neural model to “understand space,” Clover must understand what projective geometry already solves exactly or approximately.

#### Key sources

- Multiple-view geometry foundations: https://www.robots.ox.ac.uk/~vgg/hzbook/
- ORB-SLAM3 paper: https://arxiv.org/abs/2007.11898
- ORB-SLAM3 code: https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT optical flow: https://arxiv.org/abs/2003.12039
- RAFT code: https://github.com/princeton-vl/RAFT

#### What this route demonstrates

Classical/optimization-based vision can produce explicit, inspectable variables such as:

```text
camera pose
trajectory
correspondence
multi-view geometry
map structure
relocalization
uncertainty/state estimates
```

#### What it does not establish

It does not by itself solve:

```text
open-world semantics
persistent object identity under arbitrary occlusion
physical dynamics
causal structure
counterfactual reasoning
long-horizon task state
```

#### Clover question

> Which geometric invariants should remain explicit because mathematics already gives them strong structure, and which variables should instead be learned from data?

---

### 4. Research domain B — static self-supervised visual representation

The question here is what large-scale visual experience can provide before explicit temporal/world modeling is introduced.

#### DINOv3

- Meta research page: https://ai.meta.com/research/publications/dinov3/
- Project page: https://ai.meta.com/research/dinov3/
- Paper: https://arxiv.org/abs/2508.10104
- Code: https://github.com/facebookresearch/dinov3

DINOv3 scales label-free image self-supervision to 7B-parameter models and 1.7B images and produces strong frozen dense features for detection, segmentation, depth and related tasks.

#### Research significance

DINOv3 should replace DINOv2 as the primary current static SSL baseline in the Survey, while DINOv2 remains historically important.

#### Clover question

> If a static visual representation already gives strong object/part/depth structure, what world-understanding capabilities specifically require persistent temporal state rather than a stronger image encoder?

---

### 5. Research domain C — predictive video representation

#### V-JEPA 2

- Meta research page: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- Paper: https://arxiv.org/abs/2506.09985
- Code: https://github.com/facebookresearch/vjepa2

V-JEPA 2 pretrains from more than one million hours of internet video and then uses less than 62 hours of robot video for action-conditioned post-training and zero-shot image-goal planning.

#### V-JEPA 2.1

- Paper: https://arxiv.org/abs/2603.14482

V-JEPA 2.1 strengthens dense, spatially structured and temporally consistent features and reports gains in anticipation, navigation, depth and robot grasping.

#### Mechanistic evidence

- Interpreting Physics in Video World Models: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

This work reports that speed, acceleration and direction become decodable across video-model depth, with motion direction represented as a high-dimensional population code rather than a tiny set of compact “physics neurons.”

#### Clover implication

This is a direct counter-hypothesis to any claim that useful physical understanding must be represented as a compact hand-designed explicit variable set.

The correct comparison is empirical:

```text
explicit/factorized state
vs
distributed predictive latent
vs
hybrid/identifiable latent
```

---

### 6. Research domain D — learned geometry and spatial reconstruction

#### VGGT / VGGT-Ω

- VGGT paper: https://arxiv.org/abs/2503.11651
- VGGT code: https://github.com/facebookresearch/vggt
- VGGT-Ω paper: https://arxiv.org/abs/2605.15195
- VGGT-Ω project: https://vggt-omega.github.io/
- VGGT-Ω code: https://github.com/facebookresearch/vggt-omega

VGGT-family models show that feed-forward learned reconstruction can recover cameras, depth, point maps and tracks at foundation-model scale. VGGT-Ω extends this toward larger-scale static and dynamic reconstruction and reports that learned scene registers can improve VLA models and language alignment.

#### Central hypothesis to test

> **Can reconstruction be a scalable proxy task for spatial understanding?**

This is important but must not be silently upgraded to:

```text
reconstruction = world understanding
```

Spatial reconstruction still leaves open memory, observability, physics, causal structure and action relevance.

---

### 7. Research domain E — objects, entities and visible tracking

Object-centric representations are one possible answer to compositionality and identity, but not the only one.

#### Key sources

- Slot Attention: https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html
- PLATO / object-centric intuitive physics: https://www.nature.com/articles/s41562-022-01394-8
- SAM 3 research: https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
- SAM 3 / 3.1 code: https://github.com/facebookresearch/sam3
- SAM 3.1 release notes: https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

SAM 3.1 is the current relevant open-vocabulary video detection/segmentation/tracking baseline. It should replace SAM 2 as the primary contemporary visible-entity baseline, while SAM 2 remains an architectural predecessor.

#### Important distinction

```text
visible tracking
≠
object permanence
```

Tracking an object while it is observed does not prove the model maintains a world-state hypothesis after it leaves the field of view.

---

### 8. Research domain F — persistent visual memory

This domain must be first-class because world understanding requires maintaining facts beyond the current view.

#### PersistBench

- Paper: https://arxiv.org/abs/2609.20819
- Project/code: https://guangzhaohe.com/persistbench

PersistBench uses 360° video as omniscient reference and evaluates object permanence, motion continuity and appearance preservation after objects leave the normal field of view. Current 4D/world models degrade substantially once objects disappear from view.

Its central lesson is:

> **Seeing is not remembering.**

#### S-EMBER

- Meta research page: https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper: https://arxiv.org/abs/2607.02689

S-EMBER evaluates grounded episodic retrieval in a causal streaming setting rather than giving the model an entire offline video file. It exposes a gap between semantic answer quality and precise temporal grounding.

#### VISTA

- Paper: https://arxiv.org/abs/2610.02200

VISTA is relevant because it isolates memory/evidence organization from base-model weights, making the memory harness itself a research variable.

#### Clover questions

```text
What must be remembered?
raw visual evidence?
compressed world state?
episodic events?
object state?
task state?
which information can be forgotten safely?
```

Evidence Replay remains one candidate answer, not a commitment.

---

### 9. Research domain G — intuitive physics and physical variables

Clover needs to distinguish at least three levels:

```text
visual plausibility
→ predictive physical regularity
→ quantitative/action-relevant physical state
```

#### Core benchmarks and sources

- IntPhys 2: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- IntPhys 2 code: https://github.com/facebookresearch/IntPhys2
- MVP / Minimal Video Pairs: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- Principia: https://arxiv.org/abs/2609.04200
- Interpreting Physics in Video World Models: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

IntPhys 2 evaluates permanence, immutability, spatiotemporal continuity and solidity. MVP tests whether apparent physical reasoning survives minimal-pair shortcut controls. Principia evaluates relational Newtonian consistency without requiring absolute camera calibration.

#### Cognitive-science anchors

- Spelke et al., Origins of Knowledge: https://pubmed.ncbi.nlm.nih.gov/1454901/
- Review of early object/physics knowledge: https://pubmed.ncbi.nlm.nih.gov/26302470/

These sources motivate continuity, solidity, persistence and object structure as useful research dimensions, not as a requirement that Clover copy human infant representations.

#### Epistemic boundary

Some quantities can be visually estimated from learned priors but are not directly measured by RGB. Exact force, friction, internal material parameters and hidden geometry should not automatically be treated as observations.

---

### 10. Research domain H — causality and counterfactuals

Prediction alone does not imply causal identification.

#### Sources

- CausalVQA: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- General identifiability and achievability for causal representation learning: https://proceedings.mlr.press/v238/varici24a.html
- Identifying linearly mixed causal representations from multi-node interventions: https://proceedings.mlr.press/v236/bing24a

Interventional causal-representation work shows why observational video alone may leave multiple causal explanations compatible with the same data unless additional structural assumptions or interventions are available.

#### Clover implication

V3 active vision/action is scientifically important because action can create new visual evidence:

```text
current belief
→ action/intervention
→ changed world
→ new visual evidence
→ revised causal hypothesis
```

This still respects vision as the sensory evidence channel.

Counter-Witness First Causality remains a Clover hypothesis to compare against ordinary learned dynamics and causal-representation baselines.

---

### 11. Research domain I — generative world models

A different answer to “world model” is a model that can generate or simulate plausible futures rather than expose a persistent queryable state.

#### World Labs Atlas

- Official technical overview: https://www.worldlabs.ai/blog/atlas
- Functional taxonomy of world models: https://www.worldlabs.ai/blog/taxonomy-of-world-models

Atlas unifies generation, reconstruction and space-time simulation inside a spatially grounded multimodal model.

#### NVIDIA Cosmos 3

- Official project: https://research.nvidia.com/labs/cosmos-lab/cosmos3/
- Technical report: https://arxiv.org/abs/2606.02800
- Code: https://github.com/nvidia/cosmos

Cosmos 3 jointly processes/generates language, image, video, audio and action sequences and explicitly collapses boundaries between VLMs, video generators, simulators and world-action models.

#### Fundamental Clover distinction

```text
plausible hidden completion
≠
observed fact
≠
evidence-supported belief
```

Atlas can intentionally imagine unseen parts of a world. That is useful for generation and simulation, but a robot world state needs to know which parts are observed, inferred or merely plausible.

---

### 12. Research domain J — VLM/VLA and robot foundation models

These systems are the strongest falsifiers of the claim that explicit persistent world state is obviously required.

#### Open VLA baseline

- OpenVLA paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla

#### π0.5

- Paper: https://arxiv.org/abs/2504.16054
- Project/blog: https://www.pi.website/blog/pi05

π0.5 combines image observations, language, semantic subtasks, object detections and low-level actions and demonstrates long-horizon manipulation in unseen homes.

#### Gemini Robotics ER 2 / Robotics 2

- ER 2 overview: https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Robotics 2 overview: https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/

Gemini Robotics ER 2 explicitly separates a high-level embodied reasoning model from lower-level VLA execution. This is evidence that hierarchical reasoning/action remains competitive; it does not establish that Clover's historical hierarchy is correct.

#### Figure Helix 2.5

- Official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

Figure reports zero-shot whole-body autonomy across 30 unseen homes and a controlled pretraining comparison from 9% to 56% success. Treat this as `OFFICIAL_REPORTED_RESULT`, not independently reproduced science.

#### Skild S1

- Official report: https://www.skild.ai/blogs/s1
- General-purpose brain overview: https://skild.ai/blogs/building-the-general-purpose-robotic-brain

Skild reports in-context robot task learning from video demonstrations and unseen long-horizon tasks. Also `OFFICIAL_REPORTED_RESULT` unless independently reproduced.

#### Core experiment eventually required

```text
strong direct/implicit policy
vs
matched strong policy + persistent world representation
```

If the explicit worldview does not improve generalization, planning cost, recovery, sample efficiency, unjustified-action rate or long-horizon success, its necessity is not established.

---

### 13. Research domain K — world-action models

- World-Action Models survey: https://arxiv.org/abs/2609.16074
- Resource page: https://rcl-robotics.github.io/Awesome-World-Action-Models
- HWAM: https://arxiv.org/abs/2610.12026
- Being-M0.7: https://arxiv.org/abs/2610.11283
- ReWAM: https://arxiv.org/abs/2609.38163

WAMs explicitly couple future world prediction with action generation. They sharpen several questions Clover must answer:

```text
Should world and action be factorized?
Which future state is worth predicting?
Does pixel rollout help control more than latent/state prediction?
How is execution reality distinguished from commanded/reference action?
```

News-derived WAM ideas should remain research signals until their primary papers and evaluation protocols are understood.

---

### 14. Research domain L — active perception and information gathering

A robot cannot solve open-world uncertainty only by waiting for more frames. It may need to move to create the missing evidence.

#### Foundational source

- Ruzena Bajcsy, Active Perception: https://ieeexplore.ieee.org/abstract/document/5968

#### Contemporary source

- Vantage: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

#### Core loop

```text
ambiguity
→ estimate information need
→ select viewpoint/action
→ collect new RGB evidence
→ update world belief
```

This is a central bridge between “understanding through vision alone” and “robot brain that acts.”

---

### 15. Evaluation must be grounded in state and action, not appearance alone

#### RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

RoboPhys-3D evaluates generated/world-model rollouts using pixel fidelity, 3D consistency, state-level understanding and task-level completeness. It reports that state/execution-grounded metrics expose failures missed by perceptual or generic VLM judgments.

#### Required evaluation hierarchy

```text
controlled capability diagnostic
+ anti-shortcut test
+ persistent memory test
+ interventional/causal test
+ real video transfer
+ active-perception test
+ long-horizon embodied task
+ action usefulness
```

No single benchmark is allowed to define “understanding.”

---

### 16. The six primary contradictions to resolve

The next Clover representation should emerge from experiments that discriminate these competing explanations.

#### C1 — explicit vs distributed state

```text
explicit geometry / entities / variables
vs
distributed latent
vs
hybrid identifiable latent
```

#### C2 — reconstruction vs prediction vs generation

```text
recover current world
vs
predict relevant future
vs
generate/simulate possible worlds
```

#### C3 — object-centric vs dense scene representation

```text
objects/entities
vs
dense feature/field
vs
mixed hierarchy
```

#### C4 — passive observation vs interaction

```text
watching
vs
acting and observing consequences
```

#### C5 — persistent world state vs long context/direct policy

```text
maintained world belief
vs
implicit context/policy memory
```

#### C6 — evidence-grounded belief vs plausible completion

```text
what evidence supports
vs
what a generative prior can plausibly imagine
```

These contradictions are more fundamental than historical Clover module names.

---

### 17. Current background conclusions — constraints, not architecture

The present evidence supports the following research constraints:

1. **World understanding is partially observable.** Unknown/unobserved state must be represented rather than silently completed.
2. **Classical geometry already solves meaningful structure.** Learned systems should be compared against it, not reinvent it without evidence.
3. **Static SSL is stronger than the old Survey baseline implied.** DINOv3 is now a primary generic visual representation baseline.
4. **Distributed video representations contain real physical information.** Compact explicit variables are not automatically superior.
5. **Reconstruction is powerful but insufficient evidence for persistence, causality or action utility.**
6. **Visible tracking is not object permanence.** PersistBench makes this distinction measurable.
7. **Streaming memory is a separate capability.** S-EMBER shows that long-context scale does not automatically solve precise grounded recall.
8. **Generation and truth have different epistemic roles.** Plausible unseen completion must not be mislabeled observed state.
9. **Interaction can add causal/controllability information unavailable from passive observation alone.**
10. **Direct VLA/robot foundation models are serious counter-hypotheses.** Explicit world state must earn its complexity through measurable embodied value.
11. **Active perception is part of intelligence, not merely camera control.** The agent should know when it needs more evidence and obtain it.
12. **Hardware comes after scientific structure.** Apple M4 is a useful local platform, not a prior on the representation.

---

### 18. What Clover must not claim yet

The repository does **not** currently establish that:

```text
explicit > latent
object-centric > dense
field > transformer
reconstruction > prediction
auditability is necessary for intelligence
Evidence Replay is necessary
CSP/SEP/licence is the correct world language
CPU-first is superior
Clover > VLA/world model
```

Each may become supported, transformed or rejected after baseline, battery and failure-map evidence.

---

### 19. Immediate research deliverables

Before the next architecture proposal, complete and keep current:

1. `RESEARCH.md` — problem-space synthesis.
2. `SOURCES.md` — one-to-one source/evidence/landing map.
3. `SOURCES.md` — method-family comparison.
4. `SOURCES.md` — primary-source reading index.
5. `EVALUATION.md` — capability measurement map.
6. `SOURCES.md` — reproducibility resources.
7. `QUESTIONS.md` — unresolved contradictions.
8. baseline reconstruction notes/results when experiments begin.
9. Understanding Battery protocol.
10. Failure Matrix.

Only after these are strong enough should a new Clover representation hypothesis be frozen.

---

### 20. Final research posture

> **Protect the question, not the current answer.**

The fixed target is a machine that forms a useful understanding of the real world from visual experience and uses it to decide and act. Whether the best internal machinery is geometry, objects, predictive latents, fields, generative simulation, explicit belief state, a hybrid, or something not yet named remains an empirical research question.

---

<a id="topic-survey_breadth"></a>

## SURVEY_BREADTH — Breadth Foundation for Stage-1 Research

**Source checks:** 2026-10-19–20; new targeted checks are listed above.
**Companion:** [`SOURCES.md`](SOURCES.md#topic-research-emerging-frontier_sweep_2026-10-19) tracks the *frontier*; this file builds the *breadth* underneath it.

The 2026-10-19 frontier sweep found that recent intake was almost entirely VLA / world-action-model / industry-brain news, with **zero new material on six breadth axes**. Rule adopted there and kept here:

```text
a sweep with frontier but no breadth counts as failed
```

This file records verified anchor sources for those six axes, plus the standing tracking channels that keep both breadth and frontier current. Entries follow the AGENTS §4.4 record shape (problem / demonstrates / does-not-demonstrate / assumptions / counter-hypothesis) in compact form. Anchors were located and bibliographically verified on 2026-10-19; nine of them were then read in full text and recorded into [`SOURCES.md`](SOURCES.md#topic-research-survey-source_map) (marked **FULL READ** below), and the remaining gap hunts were completed on 2026-10-20 (see §7). Remaining entries are abstract/bibliographic level, labelled as such. No entry here is an architecture decision (§4.2, §26).

---

### 0. Standing tracking channels

| Channel | What it feeds | Cadence |
|---|---|---|
| arXiv listings cs.RO / cs.CV / cs.LG / cs.AI | frontier papers | daily digest |
| CoRL (2026: Austin, workshops 12 Nov 2026; CFP explicitly lists *video models and latent world models for robot learning* and *robot foundation models*) | top-venue robot learning | proceedings sweep at publication |
| RSS (2027: Athens, 6–11 Jul 2027; extended-abstract deadline 2026-12-04) | top-venue robotics | proceedings sweep |
| ICRA / IROS / CVPR / ICCV / NeurIPS / ICLR / ICML / AISTATS | method + theory anchors | proceedings sweep |
| Journals: T-RO, IJRR, Science Robotics, PNAS, Nature Machine Intelligence, Artificial Intelligence | durable results | monthly scan |
| Official industry sources only (NVIDIA, Google DeepMind, Physical Intelligence, Figure, NEURA, OpenAI, Tesla) | industry claims as `OFFICIAL_*` / `SURVEY_SIGNAL` | daily digest |

Company statements never become scientific fact silently (§4.5). News remains a discovery layer; durable conclusions must be upgraded to `PRIMARY_PAPER` / `OFFICIAL_*` and recorded in `SOURCES.md` / `SOURCES.md`.

---

### 1. Axis A — Partial observability & identifiability theory

**Why this axis:** Clover's core promise is a *licensed* world state from vision alone. Whether a hidden variable is determined by visual evidence at all — and under what extra assumptions — is a theorem-level question, not an architecture preference (§7: predictability is not identifiability).

#### A1. POMDP formalism — Kaelbling, Littman & Cassandra (1998)

- **Source:** *Planning and acting in partially observable stochastic domains*, Artificial Intelligence 101(1–2):99–134. DOI: https://doi.org/10.1016/S0004-3702(98)00023-X · `PRIMARY_PAPER` · **FULL READ 2026-10-19** (witness algorithm; belief-MDP optimality; finite-memory controller extraction; the paper's own complexity warning — exact polynomial solving in all parameters would imply NP = RP)
- **Problem:** optimal action when the true state is never directly observed and both actions and observations are stochastic.
- **Demonstrates:** belief state (a distribution over world states) is a sufficient statistic for the observation history; exact solution is computationally hard even for small domains.
- **Does not demonstrate:** how to *learn* the model or the belief representation from raw pixels; assumes a given state space and observation model.
- **Landing for Clover:** the belief/licence discipline has a classical formal home — "unobserved ≠ free, unknown is a state" is POMDP orthodoxy, not a Clover invention. Any Clover state claim should name which POMDP assumption it keeps or drops.

#### A2. Identifiability of learned latent state — Khemakhem et al. (2020)

- **Source:** *Variational Autoencoders and Nonlinear ICA: A Unifying Framework*, AISTATS 2020, PMLR 108:2207–2217. http://proceedings.mlr.press/v108/khemakhem20a.html · `PRIMARY_PAPER` · **FULL READ 2026-10-19** (main text incl. corrigendum; supplementary proofs not read)
- **Problem:** when is a learned latent representation *the* latent state, rather than one of infinitely many equivalent reparameterisations?
- **Demonstrates:** with an auxiliary variable conditioning the prior (iVAE), the latent model is identifiable up to simple transformations; plain VAEs / unconditional latent models are provably **non-identifiable**. Precision from the full read: identifiability needs the auxiliary variable's λ-differences to span the full space — a *stationary* world in u collapses it; with k = 1 and location-only change, orthogonal transforms remain indistinguishable (the authors' own Proposition 1); and the paper's discrete-observation claim was **retracted in a corrigendum**. Experiments are synthetic sources + fMRI — never real video.
- **Does not demonstrate:** identifiability from raw video alone without auxiliary structure; the auxiliary variable is an added assumption, not a free lunch.
- **Landing for Clover:** pairs with *Identifiable World Models* (arXiv:2610.07028, already tracked in the frontier survey). Together they set the Stage-1 question precisely: *what auxiliary structure (temporal contrast, action, multi-view, intervention) makes a visual world state identifiable, and what equivalence class remains?* Any "learned world state" claim that cannot answer this is incomplete.

---

#### A3. The identifiability ladder, modern steps — CITRIS (2022) & iCITRIS (2023)

- **Sources:** Lippe et al., *CITRIS: Causal Identifiability from Temporal Intervened Sequences*, ICML 2022 (Spotlight), PMLR 162:13557–13603, https://proceedings.mlr.press/v162/lippe22a.html · Lippe et al., *iCITRIS: Causal Representation Learning for Instantaneous and Temporal Effects in Interactive Systems*, **ICLR 2023** (venue and arXiv ID corrected during verification: arXiv:2206.06169). https://arxiv.org/abs/2206.06169 · `PRIMARY_PAPER` (bibliographic + claim-level verified 2026-10-20; iCITRIS record is abstract/author-page level)
- **The ladder:** A2 buys identifiability of independent *sources* with a static auxiliary variable. CITRIS adds **time + known intervention targets** and buys identifiability of the intervention-*affected parts* of causal variables (including multidimensional factors) — assuming all causal relations are temporal and targets are observed. iCITRIS adds **instantaneous effects** (frame rate slower than the true dynamics) and buys the causal *graph* as well — but only with **partially-perfect interventions** that sever a variable's instantaneous parents.
- **Does not demonstrate:** anything on real-world robotic video (all experiments are synthetic/stylised); intervention targets are always *given*, never discovered; unaffected parts of variables remain unidentified at every rung.
- **Landing for Clover:** CITRIS and iCITRIS establish identifiability under their stated temporal, observation and intervention assumptions. These sufficient-condition results do not prove that every passive-video setting is non-identifiable. Without an applicable structural restriction or discriminating auxiliary evidence, observational equivalence can remain; under other assumptions, temporal variation, calibrated views or observed natural interventions may provide useful structure. The robot's own actions are one candidate source of such evidence, not the only possible source. Any Clover claim must specify the hypothesis class, observation process, available auxiliary variables, intervention assumptions and remaining equivalence class. Whether a commanded action supplies the required intervention on a latent factor must itself be checked.

### 2. Axis B — Human & developmental visual cognition

**Why this axis:** infants solve a version of the mother question from vision with almost no language. Their constraint set — what is present early, what is absent — is evidence about what visual world understanding minimally requires, and the violation-of-expectation paradigm is a ready-made falsification instrument.

#### B1. Core knowledge — Spelke et al. (1992)

- **Source:** *Origins of knowledge*, Psychological Review 99(4):605–632. DOI 10.1037/0033-295X.99.4.605 · PubMed: http://www.ncbi.nlm.nih.gov/pubmed/1454901 · `PRIMARY_PAPER` (abstract verified 2026-10-19)
- **Demonstrates:** early infant physical reasoning accords with **continuity** (objects move on connected paths) and **solidity** (no two objects in the same place at the same time).
- **Does not demonstrate — equally important:** early reasoning does **not** accord with **gravity** or **inertia**. The honest reading is a *partial* constraint set, not a full physics engine at birth.
- **Full-read refinement (2026-10-20):** the 1992 full text remains paywalled (abstract-level here), but Spelke (1994), *Initial knowledge: six suggestions*, Cognition 50:431–445, was read in full: the object-domain principles are stated as **cohesion, continuity, contact**; gravity/inertia are excluded with the rationale that initial knowledge captures what is most *true*, not what is most obvious (unsupported objects do not always fall perceptibly, motion is not always smooth); and a task-specificity caveat — 6-month-olds' looking-time inferences follow continuity-not-inertia while their predictive *reaching* extrapolates along the line of motion. Looking knowledge ≠ acting knowledge.
- **Landing for Clover:** continuity + solidity are candidate Stage-1 test constraints (object permanence across occlusion); gravity/inertia must be treated as *learned or absent*, not assumed as priors. This also warns against importing a complete "core knowledge" checklist as an axiom set (§4.1).

#### B2. Violation-of-expectation — Baillargeon (1985; Baillargeon & Graber 1987)

- **Source:** Baillargeon, Spelke & Wasserman (1985), *Object permanence in five-month-old infants*, Cognition 20:191–208, DOI 10.1016/0010-0277(85)90008-3; and the tall/short-rabbit screen experiments (Baillargeon & Graber 1987). · `BACKGROUND_REFERENCE` — **primary abstract read 2026-10-20; full text confirmed closed-access** (Semantic Scholar openAccessPdf: CLOSED), so this entry stays abstract-level by evidence, not by omission.
- **Demonstrates:** in the 1985 drawbridge study, 5-month-olds (n=21) looked longer at the impossible event (screen rotating through the space of a hidden box) than at the possible event (screen stopping at the box); a control experiment (n=22, box placed *beside* the screen) rules out a simple rotation-length preference. Infants maintain occluded objects and expectations about them.
- **Does not demonstrate:** the internal representation format; looking time is an expectation signal, not a state readout. The paradigm's interpretation has known critiques (perceptual-novelty confounds), which any borrowing must record.
- **Landing for Clover:** VoE is a transferable *evaluation* design — possible vs impossible event pairs with matched perceptual novelty — directly usable as a shortcut-resistant test shape for object permanence (see Axis F).

#### B3. Intuitive physics engine — Battaglia, Hamrick & Tenenbaum (2013)

- **Source:** *Simulation as an engine of physical scene understanding*, PNAS 110(45):18327–18332. DOI 10.1073/pnas.1306572110 · Open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC3831455/ · `PRIMARY_PAPER` · **FULL READ 2026-10-19**
- **Demonstrates:** a single probabilistic-simulation model fits human judgments across five psychophysical tasks (stability, support, tearing, containment…), including human illusions and biases — humans appear to run *approximate, noisy* simulation, not exact physics. Full-read specifics: uncertainty lives in the *input* (geometry σ ≈ 20% of a block's shorter side, latent forces φ, mass ratio μ); human trial variance implies only ~3–7 stochastic samples; and the scene inputs were sampled from a distribution **based on ground truth** — no visual front end was built (listed as future work). A feature-heuristic alternative fared consistently worse.
- **Does not demonstrate:** that the brain literally contains a physics engine of this form, nor that simulation is the only route; it is a computational-level fit to adult judgments.
- **Landing for Clover:** a competing hypothesis to keep visible (§4.4): world understanding as *approximate simulation over an inferred scene* vs Clover-style *queryable state with licences*. The two make different predictions under occlusion and counterfactual queries — a discriminating test belongs in Stage 2.

---

### 3. Axis C — Classical geometry, SLAM & SfM

**Why this axis:** the geometry tradition is the strongest existing answer to "state from vision alone" and the baseline any learned world state must beat or honestly differ from. Its failure records are as valuable as its successes.

#### C1. DROID-SLAM — Teed & Deng (2021)

- **Source:** *DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras*, NeurIPS 2021. https://arxiv.org/pdf/2108.10869 · Code: https://github.com/princeton-vl/DROID-SLAM · `PRIMARY_PAPER` + `OPEN_SOURCE` · **FULL READ 2026-10-19**
- **Demonstrates:** learned recurrent updates + a **differentiable dense bundle-adjustment layer** achieve large accuracy gains and far fewer catastrophic failures than prior systems, generalising across camera setups. Full-read specifics: zero tracking failures on TartanAir/EuRoC/TUM-RGBD; EuRoC mono ATE 2.2 cm (43% better than ORB-SLAM3); and the load-bearing ablation — training *without* the DBA layer in the loop makes the system unstable, so the geometric optimiser must be inside learning, not bolted on at inference.
- **Does not demonstrate:** object-level or physical world state; output is camera pose + per-pixel depth. Notably, the learned front-end did **not** replace geometric optimisation — the state is still produced by bundle adjustment.
- **Landing for Clover:** evidence that "end-to-end learned" claims in this space quietly keep a geometric solver at the core. Any Clover geometric claim must state its relation to BA-style global consistency explicitly. Training provenance is `L4`, full stop: a single model trained entirely on synthetic TartanAir video with ground-truth pose/depth supervision (pose + flow losses); stereo/RGB-D enter only at test time through the DBA objective. Deployment input being RGB does not make it vision-alone learning (§5). Pinhole intrinsics are assumed known (`V1`).

#### C2. ORB-SLAM3 — Campos et al. (2021)

- **Source:** *ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multimap SLAM*, IEEE Transactions on Robotics 37(6):1874–1890, 2021. https://arxiv.org/abs/2007.11898 · `PRIMARY_PAPER` / `OPEN_SOURCE` · **FULL READ 2026-10-20**
- **Demonstrates:** the mature classical stack (feature tracking, local mapping, loop closure, map merging via the Atlas multi-map system, visual-inertial fusion) and its documented operating envelope. Full-read specifics: stereo-inertial EuRoC ATE ≈ 3.5 cm RMS, multi-session operation 2.6–3.2× better than VINS-Mono; the authors' own accuracy thesis is that exploiting short/mid/long-term **and multi-map** data association "overpowers" front-end choices.
- **Does not demonstrate:** robustness in low-texture, dynamic, or badly lit scenes — the classical failure triad that motivated learned methods. The full read names the frontier precisely: **low texture is the stated main failure case** (descriptor matching loses to photometric LK tracking on near-featureless dark sequences); dynamic objects exist only as outliers to reject; pure rotation blocks monocular depth; IMU initialisation needs gravity/roll-pitch excitation (a car on flat ground may never initialise); long outdoor runs drift 10–70 m in inertial parameters; far/sky points are discarded by hand rules. Calibrated intrinsics are a required input (`V1`-adjacent); monocular scale is unobservable.
- **Landing for Clover:** the reference failure catalogue for Axis D: classical geometry fails exactly where image formation stops cooperating. A vision-alone brain must degrade *licences*, not silently hallucinate state, in the same conditions.

---

### 4. Axis D — Image formation & adverse visual conditions (observation physics)

**Why this axis:** §6 — world-state ambiguity ≠ image-formation ambiguity ≠ sensor corruption. What the pixels *cannot* contain is set by optics and acquisition before any model runs.

#### D1. Brightness constancy & the aperture problem — Horn & Schunck (1981)

- **Source:** *Determining Optical Flow*, Artificial Intelligence 17:185–203, 1981. Reprint locator: http://dev.ipol.im/git/?p=coco/ipol_phs.git;a=blob_plain;f=doc/ipol_horn_schunck_draft.pdf;h=dc931ccba98cafe3742ffeb819d161ac361e3cbb;hb=575a90230da4c38969a1674748b29c9bb5fedf70 · `PRIMARY_PAPER` (bibliographic verified 2026-10-19)
- **Demonstrates:** under brightness constancy, one pixel yields one equation for two unknowns (the aperture problem): local image evidence *provably underdetermines* motion; their smoothness prior is an added assumption that fills the gap — visibly, the field's first explicit "licence" for inferred state.
- **Does not demonstrate:** validity under illumination change, specularity, transparency or occlusion boundaries — exactly where brightness constancy breaks.
- **Landing for Clover:** the canonical template for every observation-physics entry: name the image-formation assumption, name what it licenses, name where it dies. Full assumption checklist lives in [`PERCEPTION.md`](PERCEPTION.md#topic-research-research_observation_physics).

#### D2. Adverse-condition boundary — Bijelic et al. (2020) — *counter-anchor, not vision evidence*

- **Source:** *Seeing Through Fog Without Seeing Fog: Deep Multimodal Sensor Fusion in Unseen Adverse Weather*, CVPR 2020, pp. 11682–11692. https://openaccess.thecvf.com/content_CVPR_2020/html/Bijelic_Seeing_Through_Fog_Without_Seeing_Fog_Deep_Multimodal_Sensor_Fusion_CVPR_2020_paper.html · arXiv:1902.08913 (preprint under an earlier title) · `PRIMARY_PAPER` (bibliographic + abstract verified 2026-10-19)
- **Demonstrates:** on a 100k-label multimodal dataset (>10,000 km of northern-Europe driving plus a controlled fog chamber), RGB object detection degrades severely in fog/snow/rain while lidar, radar and gated NIR degrade *asymmetrically*; an entropy-driven fusion network trained on clean data survives adverse weather by leaning on the non-RGB sensors.
- **Does not demonstrate:** anything about vision-alone understanding — the paper is multimodal **by design**; its point is precisely that the camera stream fails. The gated camera is active sensing (backscatter gating), not passive vision.
- **Landing for Clover:** this is the honest boundary marker for Axis D. It documents *which* observation regimes defeat RGB-only perception and how other sensors compensate. Any Clover claim scoped to adverse conditions must state its observation-physics regime; this paper must never be cited as vision-alone support.

#### D3. Low light, passive RGB — Chen, Chen, Xu & Koltun (2018)

- **Source:** *Learning to See in the Dark*, CVPR 2018. https://arxiv.org/abs/1805.01934 · `PRIMARY_PAPER` (verified 2026-10-20)
- **Demonstrates:** a fully-convolutional network operating directly on raw sensor data replaces the traditional ISP pipeline and restores clean, colourful images from extreme low-light (<0.1 lux) short exposures; introduces the SID dataset (5,094 raw short-exposure images paired with long-exposure references).
- **Does not demonstrate:** world-state estimation — this is image restoration. And the restoration is *supervised by a privileged pairing* (long-exposure references): it shows the photon-noise floor can be learned around with paired data, not that low-light RGB yields reliable state for free.
- **Landing for Clover:** the first genuinely passive-RGB adverse-condition anchor. Low-light claims inherit its condition: restoration quality is bought with paired supervision; without pairs, the noise floor is the honest limit.

#### D4. Low-light detection benchmark — Loh & Chan (2019)

- **Source:** *Getting to know low-light images with the Exclusively Dark dataset*, Computer Vision and Image Understanding 178:30–42, 2019. DOI 10.1016/j.cviu.2018.10.010 · `PRIMARY_PAPER` (verified 2026-10-20)
- **Demonstrates:** ExDark — 7,363 low-light images captured in visible light only, 10 lighting conditions, bounding-box annotations over 12 object classes — and the finding that low-light corruption reaches far deeper into hand-crafted and learned features than "illumination invariance" fixes.
- **Landing for Clover:** passive-side corroboration of D2's lesson: degraded RGB corrupts features non-superficially, so adverse-condition capability claims need examiners that go beyond invariance assumptions. **Coverage update 2026-10-25:** motion blur and RGB-D transparency anchors are recorded below; passive posed-RGB specular anchors are now recorded in [PERCEPTION.md](PERCEPTION.md#reflection-evidence). RGB-only transparency and unique physical decomposition remain separate questions.

---

#### D5. Transparent materials — Sajjan et al. (2020, ClearGrasp)

- **Source:** *Clear Grasp: 3D Shape Estimation of Transparent Objects for Manipulation*, ICRA 2020, pp. 3634–3642. https://arxiv.org/abs/1910.02550 · `PRIMARY_PAPER` (verified 2026-10-20)
- **Demonstrates:** from a single RGB-D image, networks predict surface normals, transparent-surface masks and occlusion boundaries, and use them to *complete the depth* of transparent objects (trained on 50,000+ synthetic RGB-D images; 286-image real benchmark); grasping on novel transparent objects improves out of the box.
- **The observation-physics fact it documents:** standard depth sensors pointed at transparent objects return values belonging to the surfaces *behind* them — the depth channel is not merely noisy, it is systematically wrong, and learning repairs it from RGB appearance cues. Input is RGB-**D** and training is synthetic-supervised (`L4`): an RGB-D boundary anchor, never RGB-alone evidence.
- **Landing for Clover:** transparency is a regime where "the sensor said so" is false by construction; state licences in transparent scenes must be issued from the appearance-based completion, with its synthetic-training provenance attached.

#### D6. Motion blur, passive RGB — Nah, Kim & Lee (2017)

- **Source:** *Deep Multi-Scale Convolutional Neural Network for Dynamic Scene Deblurring*, CVPR 2017, pp. 3883–3891. https://openaccess.thecvf.com/content_cvpr_2017/html/Nah_Deep_Multi-Scale_Convolutional_CVPR_2017_paper.html · `PRIMARY_PAPER` (verified 2026-10-20)
- **Demonstrates:** end-to-end restoration of sharp images from single blurred photos without explicit kernel estimation (PSNR 29.23 on the GoPro benchmark introduced by the paper, SOTA at publication).
- **Caveat that matters:** GoPro "blur" is *synthesised* by averaging consecutive high-frame-rate sharp frames — an approximation of true long-exposure blur; models trained on it transfer imperfectly to real blur (RealBlur evidence). The restoration works insofar as the dataset's blur physics are invertible by construction.
- **Landing for Clover:** motion blur closes the Axis-D set with the same lesson in a third form (cf. D3's paired supervision, D5's corrupted channel): photometric repair is possible, but the repaired pixels are *inference*, and any state built on them inherits that status. The former passive-specular source gap is now covered by Ref-NeRF and NeRFactor; see [the qualified 2026-10-25 record](PERCEPTION.md#reflection-evidence). This closes an inventory gap, not material identifiability.

### 5. Axis E — Deformable, fluid & granular dynamics

**Why this axis:** rigid-body benchmarks dominate the frontier intake; household worlds are cloth, dough, liquid, cables and piles. A brain claim scoped to rigid scenes must say so.

#### E1. PlasticineLab — Huang et al. (2021)

- **Source:** *PlasticineLab: A Soft-Body Manipulation Benchmark with Differentiable Physics*, ICLR 2021. https://arxiv.org/pdf/2104.03311 · Project: http://plasticinelab.csail.mit.edu · `PRIMARY_PAPER` + `OPEN_SOURCE` · **FULL READ 2026-10-19**
- **Demonstrates:** a differentiable elastoplastic simulator (DiffTaichi) with 10 soft-body manipulation tasks; gradient-based planning solves many tasks in tens of iterations where RL largely fails — **but gradient methods still fall short on multi-stage, long-horizon tasks**. Full-read specifics: agents observe a privileged downsampled particle-landmark state, never pixels; gradient winners are *open-loop* trajectory optimisations assuming full environment knowledge (e.g. RollingPin 0.93, Assembly 0.90 soft-IoU) while SAC/TD3 score ~0 on several tasks; the multi-stage failure mechanism is named precisely — gradients vanish at detachment/reattachment (Pinch, Writer).
- **Does not demonstrate:** perception of deformable state from pixels (state is privileged simulator state, `L4`); no visual state estimation is evaluated.
- **Landing for Clover:** two open problems in one paper — (i) deformable world state from vision alone is essentially unmeasured; (ii) even with perfect state and gradients, long-horizon deformable planning is unsolved. Simulation evidence tier: `EV1` (§23) — not sim2real evidence.

#### E2. DiffTaichi — Hu et al. (2020)

- **Source:** *DiffTaichi: Differentiable Programming for Physical Simulation*, ICLR 2020 (bibliographic record via PlasticineLab lineage, verified 2026-10-19). `PRIMARY_PAPER`
- **Landing:** the tooling layer under E1; relevant when Stage 2 needs differentiable-physics falsifiers.

#### E3. Learned fluid / granular / deformable dynamics — Sanchez-Gonzalez et al. (2020)

- **Source:** *Learning to Simulate Complex Physics with Graph Networks* (GNS), ICML 2020, PMLR 119:8459–8468. https://arxiv.org/abs/2002.09405 · `PRIMARY_PAPER` (bibliographic + abstract verified 2026-10-19)
- **Demonstrates:** a graph-network simulator over particle state generalises across fluids, rigid solids and deformable materials (Water/Sand/Goop domains from SPH/MPM simulators), rolling out thousands of timesteps with ~10× more particles at test time than in training.
- **Does not demonstrate:** perception — inputs are privileged particle positions, velocities and material properties (`L4`); there are no pixels anywhere in the paper.
- **Landing for Clover:** the dynamics-side anchor for this axis, and it sharpens the open problem by contrast: learned *dynamics from state* is demonstrated (E1, E3); *state from vision alone* for deformable/fluid/granular matter remains unmeasured. That perception-side gap stays **open** (§28.22).

#### E4. Particle dynamics with real-world control — Li et al. (2019, DPI-Net)

- **Source:** *Learning Particle Dynamics for Manipulating Rigid Bodies, Deformable Objects, and Fluids*, ICLR 2019. https://arxiv.org/abs/1810.01566 · `PRIMARY_PAPER` (bibliographic + provenance verified 2026-10-20)
- **Demonstrates:** a learned graph-network particle simulator (dynamic graphs, hierarchical propagation) spanning fluids, rigid bodies and deformables; its dynamics plus MPC control real tasks (fluid shaking, foam/rice-grip moulding), beating PPO baselines on sample efficiency.
- **State provenance — the decisive audit:** `MIXED`, leaning privileged. Training is entirely in simulation against simulator ground truth; for the real-world task, particles are *randomly sampled inside a mesh reconstructed from a depth camera via TSDF fusion* — geometry arrives from a classical reconstruction pipeline, never from a learned pixel estimator; the dynamics model never consumes an image.
- **Landing for Clover:** sibling dynamics anchor to E3, and the provenance verdict is its value: even the flagship "learning particle dynamics" system gets its real-world state from depth-camera reconstruction. The perception half remains unbuilt here.

#### E5. Perception-side deformable state — Shi et al. (2022, RoboCraft)

- **Source:** *RoboCraft: Learning to See, Simulate, and Shape Elasto-Plastic Objects with Graph Networks*, RSS 2022. DOI 10.15607/RSS.2022.XVIII.008 · https://www.roboticsproceedings.org/rss18/p008.html · `PRIMARY_PAPER` (bibliographic + provenance verified 2026-10-20)
- **Demonstrates:** a full perception→dynamics→planning loop for elasto-plastic objects: particles are sampled from an RGB-D point cloud / reconstructed mesh; the GNN dynamics model is trained **directly from raw visual data** (10 minutes of real-world interaction, distribution-based losses, no particle-to-particle temporal correspondence); MPC then shapes plasticine into target shapes — including unseen ones — at untrained-human level.
- **State provenance:** `PIXELS`, with two honest caveats: input is RGB-**D** (depth participates — outside the RGB-only `V0–V2` protocol), and particle sampling leans on classical mesh reconstruction (alpha shapes / ball pivoting) with shape-prior refinements, not an end-to-end learned pixel→state estimator.
- **Landing for Clover:** the first true perception-side anchor on this axis — the closest existing demonstration of the capability the mother question demands for deformable matter. Its boundary defines the successor's target: same loop, from RGB alone, without classical reconstruction in the middle. Fluid/granular perception-side anchors remain **open** (§28.22).

---

#### E6. Hidden fluid fields from visualisations — Raissi, Yazdani & Karniadakis (2020)

- **Source:** *Hidden fluid mechanics: Learning velocity and pressure fields from flow visualizations*, Science 367(6481):1026–1030, 2020. DOI 10.1126/science.aaw4741 · `PRIMARY_PAPER` (verified 2026-10-20)
- **Demonstrates:** a Navier–Stokes-informed network infers *unobservable* velocity and pressure fields from spatio-temporal images of a passive scalar (dye/smoke concentration), robust to low resolution and substantial noise — including extracting lift/drag and wall shear stress in an aneurysm where direct measurement is impossible.
- **State provenance:** `MIXED`, and the mix is the lesson: inputs are genuinely image-domain (pixels → hidden physical fields, the exact *form* of the mother question), but the governing PDE is **supplied as prior** — this is data assimilation solving an inverse problem, not physics learned from vision — and the benchmark visualisations are generated by direct numerical simulation, so no camera optics, occlusion or clutter are present.
- **Landing for Clover:** the flagship proof that hidden physical state *can* be recovered from visual observation — and simultaneously the honesty anchor for its price: identifiability here is bought with a known physics class (cf. Axis A: without the Navier–Stokes prior, the same images are underdetermined). The open remainder is doing this with *real camera* observations and an *un*supplied physics class.

#### E7. Granular state from real robot cameras — Schenck, Tompson, Fox & Levine (2017)

- **Source:** *Learning Robotic Manipulation of Granular Media*, CoRL 2017. Full text: https://rse-lab.cs.washington.edu/papers/corl2017_granularmedia.pdf · `PRIMARY_PAPER` · **FULL READ 2026-10-20**
- **Demonstrates:** the first ConvNet dynamics model of granular media, learned from a real robot fleet scooping and dumping pinto beans in a tray; the structured dynamics model beats a hand-crafted heuristic and an implicit value network, and its predictions drive actions that shape target configurations.
- **State provenance:** `PIXELS`-adjacent, observed-not-privileged: the state is a heightmap (~1 cm cells) **computed from the depth image** (RGB → depth → heightmap); no simulator state or mocap anywhere. Boundaries: the state is the *observable surface only* (no stress, no per-grain identity), effectively 2.5D, and RGB texture is discarded.
- **Search status:** the repository's 2026-10-20 search did not register a primary source demonstrating the specified RGB-only granular-state setting. This is a recorded coverage gap, not proof that no such work exists. The original query log, searched sources and inclusion criteria were not preserved in sufficient detail for an exhaustive-search claim.
- **Landing for Clover:** the registered perception-side anchors use RGB-D/depth, supplied physics, or restricted state targets. The stronger conjunction—RGB-only observations, learned state estimation, relevant hidden-state coverage and downstream control—remains unclosed by the evidence registered here. Do not infer a field-wide absence from this inventory.

### 6. Axis F — Evaluation methodology (shortcut resistance, examiner isolation)

**Why this axis:** a world-understanding claim is only as strong as the test that could have refuted it. This axis is the methodological licence for every capability claim in the repository.

#### F1. Shortcut learning — Geirhos et al. (2020)

- **Source:** *Shortcut Learning in Deep Neural Networks*, Nature Machine Intelligence 2:665–673, 2020. DOI 10.1038/s42256-020-00257-z · https://arxiv.org/abs/2004.07780 · `PRIMARY_PAPER` · **FULL READ 2026-10-19** (adds two cautions: a usable o.o.d. test must satisfy three non-trivial conditions — clear shift, a well-defined intended solution, current models actually struggling — and good o.o.d. tests *decay* as models improve, cf. Winograd schemas; the proposed "Morgan's Canon for ML" is a methodological norm, not a result)
- **Demonstrates:** many benchmark successes are decision rules that perform on the test distribution yet fail under modest distribution change; shortcut behaviour appears in biological learners too — it is a property of learning systems, not a DNN quirk.
- **Does not demonstrate:** a complete remedy; it offers benchmarking recommendations, not a certification procedure.
- **Landing for Clover:** mandatory audit shape for any internal result — (1) what is the cheapest cue that solves this test without the claimed capability? (2) does the test include a condition where that cue misleads? (3) is the examiner isolated from the system's inputs (pixels-only discipline)? VoE pairs (Axis B2) are one concrete anti-shortcut instrument. Internal precedent: the frozen CPU-track S0 audit recorded its own TaskSuite as *not pixels-only* (`FALSIFIED + OPEN`) — this axis exists so that class of error is caught by design, not by luck.

#### F2. Data contamination — Sainz et al. (2023)

- **Source:** *NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark*, Findings of EMNLP 2023, pp. 10776–10787. https://arxiv.org/abs/2310.18018 · `PRIMARY_PAPER` (position paper; abstract-level verified 2026-10-20)
- **Demonstrates/argues:** the worst contamination — a model trained on a benchmark's test split, then evaluated on it — silently overestimates performance and corrupts published conclusions (correct results get discarded); the extent is unknown precisely because exposure is not measured. Prescription: measure contamination **per benchmark**, per model.
- **Landing for Clover:** contamination has embodied forms this paper's taxonomy predates: *simulator-asset leakage* (test worlds drawn from the same public asset libraries / simulator as training), *pretraining-corpus leakage* (the visual front-end's web-scale training already contains the benchmark's public datasets), and *examiner non-isolation* (grader shares channels with the system — the repository's own S0 FALSIFIED precedent). A "we filtered the data" claim without a per-benchmark measurement is not evidence.

#### F3. Contamination-limited design — White et al. (2024, LiveBench)

- **Source:** *LiveBench: A Challenging, Contamination-Limited LLM Benchmark*, ICLR 2025 Spotlight. https://arxiv.org/abs/2406.19314 · Project: https://livebench.ai · `PRIMARY_PAPER` (abstract-level verified 2026-10-20)
- **Design:** questions built from *recently released* sources and refreshed monthly with dated releases (the test is always younger than training cutoffs); scoring is automatic against objective ground truth — explicitly rejecting LLM-as-judge; difficulty headroom is a design goal (top models < 70% at release) so the instrument stays discriminative. The title's "limited", not "free", is deliberate: freshness is a moving defence, not a proof of non-exposure.
- **Landing for Clover:** the translation to embodied evaluation writes itself — **dated, regenerated evaluation worlds** (scene/asset generation seeded after the training-data cutoff, generation provenance recorded, no fixed public test set) + **code-computed physical predicates** (contact, support, occlusion-recovery) as the scorer instead of VLM judges or human ratings. A static simulated benchmark is a memorisation target in exactly the way a static test split is.

---

### 7. What this file changes, and the read queue

1. **Every Stage-1 surface now has at least one primary anchor or an explicitly recorded gap.** Axes A–F map to surfaces 3, 2/5, 1/7, 4, 5, and 11/15 respectively in [`STATUS.md`](STATUS.md).
2. **Full-text read queue — status 2026-10-20:** DONE and recorded in `SOURCES.md`: Battaglia 2013 · Khemakhem 2020 · Kaelbling 1998 · DROID-SLAM 2021 · PlasticineLab 2021 · Geirhos 2020 · ORB-SLAM3 2021 · Spelke 1994 (companion to B1). Closed at abstract level by access, not by choice: Spelke 1992 and Baillargeon 1985 full texts are paywalled/closed (verified 2026-10-20); their entries carry the abstract-level label permanently until access changes.
3. **Current coverage gaps — updated 2026-10-25:** the passive-specular inventory now has Ref-NeRF/NeRFactor anchors; real optical CRL has a qualified negative-result anchor. Still open in this inventory: RGB-only deformable/granular state with downstream evidence; robust identification in natural real-robot video; safe recovery of evidence discarded before a future query; and full-text access to Spelke 1992 / Baillargeon 1985. Existing anchors do not establish scientific closure of any entire capability class.
4. **Next frontier sweep obligation (unchanged):** include at least one *new primary source* per axis above, or state why the axis produced nothing — silence is not coverage.

*Update rule: this is a living root file. New anchors are appended per axis with the same record shape and verification date; superseded entries are marked `SUPERSEDED`, never silently deleted (§15).*

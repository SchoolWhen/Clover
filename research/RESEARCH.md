# Stage 1 — Research
## Survey, Discovery and Evidence Collection

Last updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

This is the primary file for the current stage.

The purpose of Stage 1 is **coverage before commitment**. We want to know what relevant directions exist, who is working on them, what methods currently represent the frontier, what datasets and benchmarks exist, what code is reproducible, and where the strongest unresolved questions remain.

This file is deliberately broad and relatively flat so a new research agent can understand the landscape before entering deeper documents.

Detailed mechanism reports belong to Stage 2 [`ANALYSIS.md`](ANALYSIS.md), not here.

---

# 1. Research-source record

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

# 2. Broad research inventory

The mother question touches substantially more than “world models” or “VLA.” The working inventory currently contains the following directions.

## R01 — Epistemology, inverse problems and partial observability

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

## R02 — Human vision, developmental cognition and core physical knowledge

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

## R03 — Classical projective and multi-view geometry

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

## R04 — Motion estimation, correspondence and tracking

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

## R05 — Static self-supervised visual representation

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

## R06 — Predictive video representation and latent world prediction

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

## R07 — Learned geometry foundation models

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

## R08 — Neural scene representations, NeRF, Gaussian Splatting and 4D reconstruction

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

## R09 — Object-centric representation

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

## R10 — Scene graphs, relational state and semantic mapping

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

## R11 — Persistent visual memory and episodic memory

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

## R12 — Belief revision, contradiction and forgetting

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

## R13 — Intuitive physical reasoning

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

## R14 — Quantitative and relational physics

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

## R15 — Physics-informed / differentiable / structured world models

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

## R16 — Causal representation learning and identifiability

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

## R17 — Counterfactual and causal visual reasoning

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

## R18 — Active perception and next-best-view

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

## R19 — Active interaction, system identification and learning action consequences

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

## R20 — Generative world models and spatial simulation

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

## R21 — World-action models and future-state action models

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

## R22 — Vision-language-action models and direct policies

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

## R23 — Embodied reasoning models and hierarchical robot brains

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

## R24 — Robot foundation models and open-world generalization

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

## R25 — Human video, egocentric video and learning by watching

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

## R26 — Affordance learning and action-relevant perception

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

## R27 — Model-based control, planning and belief-space decision making

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

## R28 — Semantic memory and open-vocabulary robotics

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

## R29 — Uncertainty, calibration and selective prediction

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

## R30 — Open-world recognition, OOD generalization and novelty

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

## R31 — Continual learning and lifelong adaptation

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

## R32 — Simulation, synthetic data and digital worlds

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

## R33 — Large robot datasets and cross-embodiment data

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

## R34 — Benchmark design and anti-shortcut evaluation

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

## R35 — Systems integration and compounded failure

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

## R36 — Unified physical AI / integrated perception-reasoning-modeling-action

Surveys useful for coverage:

- Physical AI survey — https://arxiv.org/abs/2510.04978
- World Model for Robot Learning — https://arxiv.org/abs/2605.00080
- Toward Unified Robot Learning: Bridging Representation, VLA, and World Models — https://arxiv.org/abs/2609.03927

These surveys are discovery maps. Individual scientific claims should still be traced back to primary work when possible.

---

# 3. Current methods inventory — compact view

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

# 4. Dataset and benchmark inventory

## Visual / video

- Ego4D — https://ego4d-data.org/
- Perception Test — https://github.com/google-deepmind/perception_test

## Robot demonstrations / embodiment

- DROID — https://droid-dataset.github.io/droid/
- Open X-Embodiment — https://github.com/google-deepmind/open_x_embodiment

## Manipulation / robot task suites

- LIBERO — https://libero-project.github.io/main.html
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/
- ManiSkill — https://github.com/haosulab/ManiSkill

## Physics / causal / memory diagnostics

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

# 5. Research groups / projects to monitor

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

# 6. Collection gaps — explicit backlog

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

# 7. Stage-1 exit condition

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

# Source Map — Evidence → Research Question → Clover Landing

Last updated: 2026-10-19

This file maps important external evidence to the exact Clover research question it constrains. It is designed for fast review and to prevent source drift.

Evidence labels:

- `PRIMARY_PAPER` — peer-reviewed paper or primary preprint.
- `OFFICIAL_PROJECT` — official project/model/research page.
- `OPEN_SOURCE` — public code/checkpoint/resource.
- `OFFICIAL_REPORTED_RESULT` — company/lab result not independently reproduced here.
- `BACKGROUND_REFERENCE` — foundational book/review/historical source.

A source appearing here does **not** mean its mechanism is adopted.

Domain-level synthesis now lives in [`../dossiers/README.md`](../dossiers/README.md).

---

## 1. Foundations: partial observability, uncertainty, active perception

| Source | URL | Evidence | What it constrains | Clover landing |
|---|---|---|---|---|
| POMDPs in Robotics survey | https://arxiv.org/abs/2209.10342 | `PRIMARY_PAPER` | Real robot state is often partially observable; belief/state uncertainty is a first-class decision variable. | `BACKGROUND_RESEARCH.md` §1; `R-A-observability-epistemology.md` |
| Probabilistic Robotics | https://mitpress.mit.edu/9780262201629/probabilistic-robotics/ | `BACKGROUND_REFERENCE` | Bayesian state estimation, localization and mapping under uncertainty. | `R-A`; `R-B` |
| Bajcsy, Active Perception | https://ieeexplore.ieee.org/abstract/document/5968 | `BACKGROUND_REFERENCE` | Perception includes selecting sensing actions to gain information. | `R-H-active-perception-lifelong.md`; V3 protocol |
| Spelke et al., Origins of Knowledge | https://pubmed.ncbi.nlm.nih.gov/1454901/ | `BACKGROUND_REFERENCE` | Continuity and solidity are useful object/physics research dimensions. Companion full text read 2026-10-20: Spelke (1994) "Initial knowledge: six suggestions", Cognition 50:431–445, states the object-domain principles as **cohesion, continuity, contact** — and explicitly *not* gravity or inertia (rationale: initial knowledge captures what is most *true*, not most obvious); looking-time knowledge ≠ reaching knowledge (task-specificity caveat). | `R-E-physics.md`; 1992 full text itself still paywalled (abstract-level) |
| Baillargeon, Spelke & Wasserman 1985 — drawbridge | https://doi.org/10.1016/0010-0277(85)90008-3 | `BACKGROUND_REFERENCE` | 5-month-olds (n=21) look longer when a screen rotates *through* a hidden box than when it stops at it; control (n=22, box beside the screen) rules out rotation-length preference. Primary abstract read 2026-10-20; full text closed-access. | `R-E-physics.md`; methodological ancestor of violation-of-expectation evaluation — must be paired with the perceptual-novelty counter-hypothesis (impossible event is more similar to habituation) |
| Physics for infants review | https://pubmed.ncbi.nlm.nih.gov/26302470/ | `BACKGROUND_REFERENCE` | Reviews continuity, solidity, cohesion and object/substance reasoning. | Benchmark interpretation; not a mandate to copy human cognition |
| Kaelbling, Littman & Cassandra 1998 — POMDP | https://doi.org/10.1016/S0004-3702(98)00023-X | `PRIMARY_PAPER` | Belief state is a sufficient statistic for history; optimal behaviour is a policy over beliefs; information-gathering actions are valued inside the value function (tiger problem: listening is provably optimal under uncertainty). Full text read 2026-10-19 (see [`SURVEY_BREADTH.md`](../../SURVEY_BREADTH.md) Axis A). | `R-A-observability-epistemology.md`; belief/licence discipline precedent — but assumes a complete, correct, enumerative model; no model learning, no vision |
| Khemakhem et al. 2020 — iVAE / nonlinear ICA identifiability | http://proceedings.mlr.press/v108/khemakhem20a.html | `PRIMARY_PAPER` | Learned latent state is identifiable (up to linear, resp. permutation + pointwise, indeterminacy) **only** with an observed auxiliary variable modulating a factorised exponential-family prior; unconditional latent models are provably non-identifiable. Corrigendum: the discrete-observation claim was retracted. Full text read 2026-10-19. | `R-F` theory background; every claimed world variable must name its auxiliary structure (time / action / multi-view) and its remaining equivalence class |
| Battaglia, Hamrick & Tenenbaum 2013 — intuitive physics engine | https://pmc.ncbi.nlm.nih.gov/articles/PMC3831455/ | `PRIMARY_PAPER` | Human physical judgments across 5 experiments are fit by approximate probabilistic simulation over an inferred scene distribution (uncertainty parameters σ/φ/μ; ~3–7 effective samples), including human illusions a ground-truth model misses. Full text read 2026-10-19. | `R-E-physics.md`; also §8 — named rival to the queryable-state hypothesis; scene inputs were ground-truth-based, not estimated from pixels |

---

## 2. Classical geometry and motion

| Source | URL | Evidence | Demonstrates | Does not establish | Clover landing |
|---|---|---|---|---|---|
| Multiple View Geometry | https://www.robots.ox.ac.uk/~vgg/hzbook/ | `BACKGROUND_REFERENCE` | Projective/multi-view geometry has explicit mathematical structure. | Semantics, physics, causality. | `R-B-geometry.md` |
| ORB-SLAM3 paper | https://arxiv.org/abs/2007.11898 | `PRIMARY_PAPER` | Explicit pose/map/trajectory estimation, relocalization, multi-map (Atlas) reuse across mono/stereo/RGB-D × visual/visual-inertial; stereo-inertial EuRoC ATE ≈3.5 cm, multi-session 2.6–3.2× better than VINS-Mono; accuracy thesis: exploiting short/mid/long-term **and** multi-map data association beats front-end choices. Full text read 2026-10-20. | Open-world world understanding; named failure frontier: low texture (its stated main failure case), dynamic objects (outliers only, never state), pure rotation blocks monocular depth, IMU init needs gravity/roll-pitch excitation. | Classical baseline; `R-B` — degrade licences, never hallucinate state, exactly in its failure regimes |
| ORB-SLAM3 code | https://github.com/UZ-SLAMLab/ORB_SLAM3 | `OPEN_SOURCE` | Reproducible SLAM baseline. | — | Baseline setup |
| RAFT paper | https://arxiv.org/abs/2003.12039 | `PRIMARY_PAPER` | Strong dense optical flow / temporal correspondence. | Identity, permanence, causal state. | Motion baseline; `R-B` |
| RAFT code | https://github.com/princeton-vl/RAFT | `OPEN_SOURCE` | Reproducible flow baseline. | — | Baseline setup |
| DROID-SLAM paper | https://arxiv.org/abs/2108.10869 | `PRIMARY_PAPER` | Learned recurrent correspondence + differentiable dense bundle adjustment (Gauss–Newton over poses and per-pixel inverse depth); one model across mono/stereo/RGB-D; zero tracking failures on TartanAir/EuRoC/TUM-RGBD (EuRoC mono ATE 2.2 cm); ablation: removing DBA from training makes the system unstable. Full text read 2026-10-19. | Pose + dense depth only — no object/physical state; training is `L4` (synthetic TartanAir, ground-truth pose/depth supervision); pinhole intrinsics assumed known. | Learned-geometry baseline; `R-B` — the learned front-end did not replace geometric optimisation |
| DROID-SLAM code | https://github.com/princeton-vl/DROID-SLAM | `OPEN_SOURCE` | Reproducible learned-SLAM baseline. | — | Baseline setup |
| Bijelic et al. 2020 — seeing through fog | https://openaccess.thecvf.com/content_CVPR_2020/html/Bijelic_Seeing_Through_Fog_Without_Seeing_Fog_Deep_Multimodal_Sensor_Fusion_CVPR_2020_paper.html | `PRIMARY_PAPER` | Documents how RGB detection degrades in fog/snow/rain relative to lidar/radar/gated-NIR (100k-label multimodal dataset, >10,000 km + fog chamber); entropy-driven fusion survives by falling back to non-RGB sensors. Bibliographic + abstract verified 2026-10-19. | **Not vision-alone evidence** — multimodal by design; usable only as an adverse-condition boundary / falsifier reference. | Observation-physics counter-anchor ([`SURVEY_BREADTH.md`](../../SURVEY_BREADTH.md) Axis D); any adverse-condition claim must state its observation regime |

---

## 3. Static self-supervised visual representation

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| DINOv3 research | https://ai.meta.com/research/publications/dinov3/ | `OFFICIAL_PROJECT` | Large-scale label-free image SSL; strong frozen dense features. | How much world structure still requires time/state? | `R-C-representation.md`; generic visual baseline |
| DINOv3 paper | https://arxiv.org/abs/2508.10104 | `PRIMARY_PAPER` | 7B-scale SSL, 1.7B-image training, broad dense-task performance. | Static representation vs persistent world model. | Baseline/probing |
| DINOv3 code | https://github.com/facebookresearch/dinov3 | `OPEN_SOURCE` | Current reproducible Meta SSL baseline. | — | `DATASETS_CODE.md` |
| DINOv2 paper | https://arxiv.org/abs/2304.07193 | `PRIMARY_PAPER` | Historical predecessor and established SSL baseline. | Superseded as primary current static SSL comparator by DINOv3. | Historical comparison |

---

## 4. Predictive video representation and learned physical structure

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| V-JEPA 2 research | https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/ | `OFFICIAL_PROJECT` | Web-scale video SSL plus small robot post-training can support planning. | Does latent predictive state replace explicit state? | `R-C`; `R-G` |
| V-JEPA 2 paper | https://arxiv.org/abs/2506.09985 | `PRIMARY_PAPER` | Understanding, anticipation and action-conditioned planning. | What is encoded and how persistent is it? | Baseline/probing |
| V-JEPA 2 code | https://github.com/facebookresearch/vjepa2 | `OPEN_SOURCE` | Reproducible pretrained baseline. | — | `DATASETS_CODE.md` |
| V-JEPA 2.1 | https://arxiv.org/abs/2603.14482 | `PRIMARY_PAPER` | Dense, spatially structured and temporally consistent SSL features. | Dense latent vs explicit/entity state. | `R-C` |
| Interpreting Physics in Video World Models | https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/ | `PRIMARY_PAPER` | Physical variables can emerge as distributed/high-dimensional population codes. | Compact explicit physics variables are not automatically necessary. | `R-C`; `R-E` |
| Identifiable World Models | https://arxiv.org/abs/2610.07028 | `PRIMARY_PAPER` | Frozen diffusion latents can be aligned to identifiable state coordinates in studied systems. | Whether hybrid identifiable state scales to open-world robotics. | `R-C`; `R-F` |

---

## 5. Learned geometry and spatial reconstruction

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| DUSt3R | https://arxiv.org/abs/2312.14132 | `PRIMARY_PAPER` | Learned point-map reconstruction bridges learned and classical geometry. | Learned vs explicit geometry division of labor. | `R-B-geometry.md` |
| VGGT | https://arxiv.org/abs/2503.11651 | `PRIMARY_PAPER` | Cameras, depth, point maps and tracks from image sets. | Reconstruction vs world understanding. | Spatial baseline; `R-B` |
| VGGT code | https://github.com/facebookresearch/vggt | `OPEN_SOURCE` | Reproducible learned geometry. | — | Baseline setup |
| VGGT-Ω | https://arxiv.org/abs/2605.15195 | `PRIMARY_PAPER` | Scaled static/dynamic reconstruction; scene registers help VLA/language alignment. | Is reconstruction a sufficient spatial proxy? | `R-B`; `R-C` |
| VGGT-Ω project | https://vggt-omega.github.io/ | `OFFICIAL_PROJECT` | Project/evaluation resources. | — | `PAPERS.md` / `DATASETS_CODE.md` |
| VGGT-Ω code | https://github.com/facebookresearch/vggt-omega | `OPEN_SOURCE` | Reproducibility resource. | — | Baseline setup |

---

## 6. Object-centric representation and visible entity tracking

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| Slot Attention | https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html | `PRIMARY_PAPER` | Exchangeable object-like slots and compositional generalization. | Scaling and real-world object discovery. | `R-C-representation.md` |
| PLATO | https://www.nature.com/articles/s41562-022-01394-8 | `PRIMARY_PAPER` | Object-centric inductive bias can support intuitive-physics learning. | Whether object-centric state is necessary at scale. | `R-C`; `R-E` |
| SAM 3 research | https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/ | `PRIMARY_PAPER` | Open-vocabulary detection, segmentation and video tracking. | Visible tracking is not object permanence. | `R-B`; `R-D` |
| SAM 3.1 code | https://github.com/facebookresearch/sam3 | `OPEN_SOURCE` | Current code/checkpoints for SAM 3/3.1. | — | `DATASETS_CODE.md` |
| SAM 3.1 release | https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md | `OPEN_SOURCE` | Shared-memory object multiplexing improves multi-object tracking efficiency. | Does not create hidden-state permanence. | Primary contemporary tracking comparator |

---

## 7. Persistent visual memory

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| PersistBench paper | https://arxiv.org/abs/2609.20819 | `PRIMARY_PAPER` | 4D/world models lose object permanence, motion continuity and appearance consistency after objects leave view. | Seeing/reconstruction vs remembering. | `R-D-memory-persistence.md`; Memory Battery |
| PersistBench project/code | https://guangzhaohe.com/persistbench | `OPEN_SOURCE` | Dataset/metric access. | — | `BENCHMARKS_TASKS.md` |
| S-EMBER research | https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/ | `OFFICIAL_PROJECT` | Streaming grounded episodic retrieval exposes temporal localization gap. | Long context/scale vs grounded recall. | `R-D`; Memory Battery |
| S-EMBER paper | https://arxiv.org/abs/2607.02689 | `PRIMARY_PAPER` | 388 h streaming egocentric benchmark with temporal evidence localization. | Memory architecture remains open. | `BENCHMARKS_TASKS.md` |
| VISTA | https://arxiv.org/abs/2610.02200 | `PRIMARY_PAPER` | Memory/evidence harness can be varied independently from model weights. | Replay vs recurrent/latent memory. | `R-D`; Evidence Replay hypothesis comparator |
| VISTA project | https://vista-research.github.io/ | `OFFICIAL_PROJECT` | Describes lossless visual memory and model-directed inspection. | Interactive-game evidence is not yet real-robot memory proof. | `R-D` |
| VISTA code | https://github.com/joshhhhhan/VISTA | `OPEN_SOURCE` | Reproducible harness implementation. | — | Future harness comparison |

---

## 8. Physics and anti-shortcut evaluation

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| IntPhys 2 | https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ | `PRIMARY_PAPER` | Permanence, immutability, continuity and solidity remain difficult. | Synthetic intuitive physics vs real-world transfer. | `R-E-physics.md`; Understanding Battery |
| IntPhys 2 code | https://github.com/facebookresearch/IntPhys2 | `OPEN_SOURCE` | Reproducible benchmark. | — | Battery setup |
| MVP / Minimal Video Pairs | https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/ | `PRIMARY_PAPER` | Minimal pairs reveal shortcut-based physical reasoning. | QA still mixes language and visual evidence. | `R-E`; anti-shortcut policy |
| MVP code | https://github.com/facebookresearch/minimal_video_pairs | `OPEN_SOURCE` | Reproducible minimal-pair benchmark. | — | Battery setup |
| QuantiPhy | https://arxiv.org/abs/2512.19526 | `PRIMARY_PAPER` | Quantitative size/velocity/acceleration estimation exposes gap between verbal plausibility and numerical grounding. | How much quantitative state is needed for action. | `R-E`; quantitative physics battery |
| Principia | https://arxiv.org/abs/2609.04200 | `PRIMARY_PAPER` | Relational physics can be tested without absolute calibration; current generators/VLMs remain weak. | Relational consistency vs executable physical state. | `R-E`; Physics battery |
| Principia project | https://principiabench.github.io/ | `OFFICIAL_PROJECT` | Benchmark protocol/resources. | — | Battery setup |
| RoboPhys-3D | https://arxiv.org/abs/2608.28718 | `PRIMARY_PAPER` | State/execution-grounded metrics expose failures missed by appearance/VLM metrics. | How much 3D-grounded state predicts real task success. | `R-E`; `R-G`; world-model evaluation |
| Geirhos et al. 2020 — shortcut learning | https://arxiv.org/abs/2004.07780 | `PRIMARY_PAPER` | Decision rules that pass i.i.d. tests but fail o.o.d. unify many DNN failures (texture counting, hospital-token detection, context cues); shortcuts also occur in animal/human learning; o.o.d. tests themselves decay as models improve. Full text read 2026-10-19. | Perspective, not a certification procedure; the "intended solution" must be defined by the researcher. | Anti-shortcut audit for every capability claim (cheapest cue → misleading condition → examiner isolation); `R-E` |
| PlasticineLab | https://arxiv.org/abs/2104.03311 | `PRIMARY_PAPER` | 10 soft-body tasks / 50 configurations on differentiable MLS-MPM elastoplastic simulation; gradient-based open-loop planning solves many single-stage tasks (e.g. RollingPin 0.93 soft-IoU) where SAC/TD3/PPO largely fail; multi-stage tasks (Pinch, Writer) fail even with perfect state — gradients vanish at detachment/reattachment. Full text read 2026-10-19. | State is privileged particle landmarks (`L4`); no perception evaluated; open-loop plans assume full environment knowledge. | Deformable-planning evidence with an explicit "no perception-side benchmark exists" disclaimer; `R-E` |
| GNS — Sanchez-Gonzalez et al. 2020 | https://arxiv.org/abs/2002.09405 | `PRIMARY_PAPER` | Learned graph-network simulator over particle state generalises across fluids, rigid solids and deformable materials (Water/Sand/Goop), to ~10× particles and thousands of timesteps at test time. Abstract verified 2026-10-19. | Input is privileged particle state (`L4`) from classical simulators (SPH/MPM/PBD) — evidence about dynamics computation, not about observing state from vision. | Axis-E dynamics anchor ([`SURVEY_BREADTH.md`](../../SURVEY_BREADTH.md)); separates "dynamics from state" from "state from vision" |
| DPI-Net — Li et al. 2019 | https://arxiv.org/abs/1810.01566 | `PRIMARY_PAPER` | Learned particle dynamics (dynamic graph, hierarchical propagation) for fluids/rigid/deformables; dynamics + MPC control real foam/fluid tasks, beating PPO on sample efficiency. Bibliographic + provenance verified 2026-10-20. | State provenance is `MIXED`/privileged: training in simulation; real-world particles are sampled inside a depth-camera TSDF mesh — no learned pixel→state estimator anywhere. | Axis-E dynamics anchor; sharpens that real-world deformable state still arrives via classical reconstruction |
| RoboCraft — Shi et al. 2022 | https://www.roboticsproceedings.org/rss18/p008.html | `PRIMARY_PAPER` | Full perception→dynamics→planning loop for elasto-plastic shaping: particles sampled from RGB-D point cloud / reconstructed mesh; GNN dynamics trained **directly from raw visual data** (10 min real interaction, distribution losses, no particle correspondence); MPC shaping reaches untrained-human level incl. unseen target shapes. Bibliographic + provenance verified 2026-10-20. | Input is RGB-**D** (beyond RGB-only `V0–V2`); particle sampling leans on classical mesh reconstruction + shape priors, not an end-to-end learned estimator. | Axis-E **perception-side** anchor — closest existing "state from visual observation" demonstration for deformables; defines what a vision-alone successor must beat |
| Learning to See in the Dark — Chen et al. 2018 | https://arxiv.org/abs/1805.01934 | `PRIMARY_PAPER` | A network on raw sensor data replaces the ISP pipeline and restores clean images from extreme low light (<0.1 lux) short exposures; SID dataset: 5,094 raw short-exposure images with long-exposure references. Verified 2026-10-20. | Image restoration, not state estimation; supervision is a privileged pairing (long-exposure references). | Axis-D passive-RGB boundary anchor: the low-light noise floor can be learned *around* only with paired supervision |
| ExDark — Loh & Chan 2019 | https://doi.org/10.1016/j.cviu.2018.10.010 | `PRIMARY_PAPER` | 7,363 visible-light-only low-light images, 10 lighting conditions, box annotations for 12 classes; low-light corruption reaches deep into hand-crafted and learned features. Verified 2026-10-20. | Detection benchmark, low light only (no fog/rain/specularity); image+box annotations. | Axis-D boundary evidence: degraded RGB corrupts features non-superficially — "illumination invariance" is not a sufficient answer |

---

## 9. Causality and intervention

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| CausalVQA | https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/ | `PRIMARY_PAPER` | Real-video counterfactual, hypothetical, anticipation and planning questions remain difficult. | Language QA vs machine-native causal state. | `R-F-causality-interaction.md`; Causal Battery |
| CausalVQA paper | https://arxiv.org/abs/2506.09943 | `PRIMARY_PAPER` | Primary preprint for the benchmark. | — | `R-F` |
| CausalVQA code | https://github.com/facebookresearch/CausalVQA | `OPEN_SOURCE` | Reproducible benchmark/data interface. | — | Battery setup |
| Interventional CRL — Ahuja et al. | https://proceedings.mlr.press/v202/ahuja23a.html | `PRIMARY_PAPER` | Interventional data can identify latent causal factors under stated assumptions. | Which interventions a robot can obtain. | `R-F` theory background |
| CRL identifiability — Varici et al. | https://proceedings.mlr.press/v238/varici24a.html | `PRIMARY_PAPER` | Interventions can make latent causal models identifiable under broad stated assumptions. | What intervention structure is available to a robot. | `R-F` theory background |
| CRL multi-node interventions | https://proceedings.mlr.press/v236/bing24a | `PRIMARY_PAPER` | Extends identifiability analysis to multi-node interventions. | Passive-video-only causality remains underconstrained. | Active interaction rationale |
| Partially Observable CRL | https://proceedings.mlr.press/v235/xu24ac.html | `PRIMARY_PAPER` | Studies causal representation when observations expose changing subsets of latent state. | Scaling from synthetic assumptions to open-world vision. | `R-A`; `R-F` |

---

## 10. Active perception

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| Bajcsy, Active Perception | https://ieeexplore.ieee.org/abstract/document/5968 | `BACKGROUND_REFERENCE` | Perception can select actions that reduce uncertainty. | How to learn information value end-to-end. | `R-H-active-perception-lifelong.md`; V3 protocol |
| Vantage | https://arxiv.org/abs/2610.11810 | `PRIMARY_PAPER` | View planning/evidence acquisition can improve spatial reasoning. | General active world learning. | `R-H`; active-perception baseline |
| Vantage code | https://github.com/q1xiangchen/Vantage | `OPEN_SOURCE` | Reproducibility resource. | — | Baseline setup |
| Vision in Action | https://arxiv.org/abs/2506.15666 | `PRIMARY_PAPER` | Learns task-relevant searching/tracking/focusing camera behavior from human demonstrations. | Information-gain objective vs imitation. | `R-H` |
| SaPaVe | https://arxiv.org/abs/2603.12193 | `PRIMARY_PAPER` | Joint active perception/manipulation while decoupling camera and manipulation actions. | Generality beyond studied tasks. | `R-H`; sensing-action semantics |

---

## 11. Generative spatial/world models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| World Labs Atlas | https://www.worldlabs.ai/blog/atlas | `OFFICIAL_REPORTED_RESULT` | Unified generation, reconstruction and space-time simulation with spatial context. | Plausible completion vs evidence-grounded belief. | Generative world-model route; C6 |
| World-model taxonomy | https://www.worldlabs.ai/blog/taxonomy-of-world-models | `OFFICIAL_PROJECT` | Clarifies renderer/simulator/planner functions commonly conflated as “world model.” | Taxonomy is not independent empirical validation. | Terminology background |
| Cosmos 3 project | https://research.nvidia.com/labs/cosmos-lab/cosmos3/ | `OFFICIAL_PROJECT` | Open omnimodal world-model family spanning reasoning, generation and action. | General benchmark strength vs robust persistent world truth. | Generative/WAM comparator |
| Cosmos 3 report | https://arxiv.org/abs/2606.02800 | `PRIMARY_PAPER` | Unifies language/image/video/audio/action in one architecture. | Whether unified generation/action is sufficient for robot belief. | Frontier method map |
| Cosmos code | https://github.com/nvidia/cosmos | `OPEN_SOURCE` | Public implementation/checkpoints/resources. | — | `DATASETS_CODE.md` |

---

## 12. VLA, embodied reasoning and robot foundation models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| OpenVLA | https://arxiv.org/abs/2406.09246 | `PRIMARY_PAPER` | Open 7B VLA trained on 970k robot demonstrations. | Direct policy vs persistent world state. | `R-G-world-action.md`; open action baseline |
| OpenVLA code | https://github.com/openvla/openvla | `OPEN_SOURCE` | Fine-tuning/evaluation access. | — | Future embodied baseline |
| π0.5 | https://arxiv.org/abs/2504.16054 | `PRIMARY_PAPER` | Long-horizon manipulation in entirely new homes with heterogeneous multimodal co-training. | Visual understanding vs language/semantic/action priors. | `R-G`; strong direct-policy falsifier |
| π0.5 project | https://www.pi.website/blog/pi05 | `OFFICIAL_PROJECT` | Qualitative/system context. | — | Robot foundation map |
| Gemini Robotics ER 2 | https://deepmind.google/models/gemini-robotics/embodied-reasoning/ | `OFFICIAL_PROJECT` | High-level physical/spatial reasoning separated from lower-level VLA execution. | Persistent world-state semantics remain unspecified publicly. | `R-A`; `R-G` |
| Gemini ER 2 model card | https://deepmind.google/models/model-cards/gemini-robotics-er-2/ | `OFFICIAL_PROJECT` | Inputs, outputs, model dependency and limitation documentation. | — | Source of truth for claims |
| Gemini Robotics 2 | https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/ | `OFFICIAL_REPORTED_RESULT` | Whole-body VLA/control capabilities. | Independent reproducibility. | Robot-brain landscape |
| Figure Helix 2.5 | https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization | `OFFICIAL_REPORTED_RESULT` | Reports zero-shot long-horizon whole-body tasks across 30 unseen homes; controlled pretraining ablation. | Closed system; no independent Clover reproduction. | `R-G`; generalization reference |
| Skild S1 | https://www.skild.ai/blogs/s1 | `OFFICIAL_REPORTED_RESULT` | Reports in-context robot learning from video demonstrations and long-horizon unseen tasks. | Closed-system evidence. | `R-G`; `R-H` |
| Skild general-purpose brain | https://skild.ai/blogs/building-the-general-purpose-robotic-brain | `OFFICIAL_PROJECT` | Omni-bodied foundation-model thesis. | Does not establish world-state representation requirements. | Embodiment-invariance question |

---

## 13. World-action models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| WAM survey | https://arxiv.org/abs/2609.16074 | `PRIMARY_PAPER` | Taxonomy linking future-state modeling and executable action generation. | Which factorization is actually necessary. | `R-G`; WAM research map |
| WAM resource index | https://rcl-robotics.github.io/Awesome-World-Action-Models | `OFFICIAL_PROJECT` | Current paper/resource map. | Curation is not evaluation. | Frontier tracking |
| World Action Models: Next Frontier | https://arxiv.org/abs/2605.12090 | `PRIMARY_PAPER` | Complementary cascaded/joint WAM taxonomy and evaluation framing. | Which taxonomy predicts robust embodied performance. | `R-G` |
| HWAM | https://arxiv.org/abs/2610.12026 | `PRIMARY_PAPER` | Explicitly models reference action vs realized state/action gap. | Whether joint state-action generation is best generally. | Execution-gap comparator; `R-G` |
| Being-M0.7 | https://arxiv.org/abs/2610.11283 | `PRIMARY_PAPER` | Transfers visual-motion priors from >10k h mixed human data before humanoid adaptation. | Human-motion priors vs learned world state. | `R-G`; human-video route |
| ReWAM | https://arxiv.org/abs/2609.38163 | `PRIMARY_PAPER` | Reconstruction/perceptual fidelity alone does not guarantee policy-useful state; action-grounded shaping matters. | What state is minimally sufficient for action. | `R-C`; `R-G` |

---

## 14. Lifelong learning, replay and self-generated experience

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| Lifelong Representations survey | https://arxiv.org/abs/2607.09785 | `PRIMARY_PAPER` | Taxonomy of continual self-supervised vision and forgetting-mitigation strategies. | Scaling continual adaptation to robot-scale open streams. | `R-H` |
| WAM continual imitation / REGEN | https://arxiv.org/abs/2606.27374 | `PRIMARY_PAPER` | Generative replay can reduce forgetting without stored original demonstrations; long-horizon/action-observation consistency are bottlenecks. | Synthetic replay truth vs useful rehearsal. | `R-H`; C6 |
| Skild Physical Self-Play | https://skild.ai/blogs/physical-self-play | `OFFICIAL_REPORTED_RESULT` | Reports self-play post-training in simulation followed by humanoid transfer. | Generality and independent reproduction. | `R-F`; `R-H`; interaction/self-generated experience |

---

## 15. Repository policy for adding new sources

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

Prefer landing the source in one of the eight research dossiers as well as this map when it materially changes the research picture.

Do not add a paper only because it is recent. Do not use a news summary when a primary paper or official source is available. `news(5).md` remains a discovery/signal archive; durable claims must graduate to primary or official evidence before entering the main Survey.

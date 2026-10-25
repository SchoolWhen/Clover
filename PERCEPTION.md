<a id="top"></a>

# Perception and identifiability

Maintained: **2026-10-25** · Current project stage: **Research** ([status](STATUS.md)).

World variables, image formation, geometry, hidden physical properties and the limits of visual evidence.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<a id="reflection-evidence"></a>

## 2026-10-25 当前补充：镜面外观与物理分解

### Ref-NeRF：拟合反射外观不等于证明真实物理分解

- **来源：** Dor Verbin 等，*Ref-NeRF: Structured View-Dependent Appearance for Neural Radiance Fields*，CVPR 2022，5491–5500。[论文与书目信息](https://openaccess.thecvf.com/content/CVPR2022/html/Verbin_Ref-NeRF_Structured_View-Dependent_Appearance_for_Neural_Radiance_Fields_CVPR_2022_paper.html) · [作者项目与数据](https://dorverbin.github.io/refnerf/) · [官方代码](https://github.com/google-research/multinerf)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`。
- **实际证据：** 将随视角变化的辐射改为反射方向参数化，并用法线正则改善光泽表面新视角渲染；项目提供 Shiny 合成场景和真实采集场景。
- **观测与学习来源：** 多视图 RGB 加相机内外参；属于校准多视图条件，不能记为不带校准的 `V0`。单移动相机的 posed views 也不应直接改记为物理多相机 `V2`；须按采集实例记录。场景拟合主要是光度自监督 `L0`，相机位姿的取得方式另记。官方代码说明自己的真实图像流程使用 COLMAP 求位姿。
- **没有证明：** 可编辑、可解释的外观参数不是反射率、光照和真实表面法线唯一可识别的定理；也未检验持续物体身份、接触状态或因果预测。
- **阅读深度与复现边界：** 核对会议摘要、作者项目及代码说明，未复核完整正文与证明；官方 MultiNeRF 仓库于 2025-02-11 归档，且说明 Ref-NeRF 结果可能与原内部实现略有差异，不能把公开代码存在写成复现成功。

### NeRFactor：“无监督”的场景拟合仍可以包含测量先验

- **来源：** Xiuming Zhang 等，*NeRFactor: Neural Factorization of Shape and Reflectance Under an Unknown Illumination*，ACM TOG / SIGGRAPH Asia 2021。[论文](https://arxiv.org/abs/2106.01970) · [作者项目、模型和数据](https://xiuming.info/projects/nerfactor/) · [官方代码](https://github.com/google/nerfactor)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`。
- **实际证据：** 在同一未知光照下使用 posed 多视图 RGB，分解法线、可见性、反照率与 BRDF，用于重光照和材质编辑。
- **观测与学习来源：** 相机位姿已给定的多视图观测；光度重渲染损失 `L0` 加平滑先验，以及从真实 MERL BRDF 测量学习的材质先验 `L4`。场景图像不带材质标签，不等于整条学习链只使用视觉证据。
- **没有证明：** 单一未知照明下的物理分解唯一；也没有证明未知材质族或动态场景中的开放世界识别。
- **阅读深度：** 核对论文摘要和作者项目的输入、先验、数据及模型发布说明；未做完整正文复核。

**当前结论：** “镜面材质缺少被动 RGB 一手锚点”的资料空缺可由上述工作补上。仍开放的是：何种视角覆盖、相机校准、材质先验及照明条件，允许把“能重现图像”升级为可检验的真实几何/材质判断。后续分析应分别比较留出视角、改变光照、真实几何误差与下游接触判断；不能仅比较渲染分数。这里没有选择神经辐射场作为 Clover 表示。

## Contents

- [World-State Variables & Observability Map](#topic-research-research_state_variables)
- [Identifiability, Observability and Information Limits](#topic-research-research_identifiability)
- [Observation Physics and Image-Formation Limits](#topic-research-research_observation_physics)
- [Hidden Physical Properties, Contact and Irreversible Change](#topic-research-research_physical_properties)
- [R-A — Observability, Epistemology and Belief State](#topic-research-dossiers-r-a-observability-epistemology)
- [R-B — Geometry: What Is Already Solved?](#topic-research-dossiers-r-b-geometry)
- [R-E — Physical Understanding: Plausibility, Quantification and Relational Structure](#topic-research-dossiers-r-e-physics)
- [Classical Computer Vision and Geometry](#topic-docs-research-map-classical-vision)
- [Spatial Intelligence](#topic-docs-research-map-spatial-intelligence)

<a id="topic-research-research_state_variables"></a>

## World-State Variables & Observability Map

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This file is a Stage-1 research inventory, not a Clover architecture specification.

Its purpose is to make the phrase **“understand the real world”** less vague by asking a more concrete question:

> Which world variables matter, and what evidence is currently known to constrain them?

The map deliberately separates what may be inferred from a static RGB image, passive temporal video, active visual exploration, physical action-response, and non-visual sensing.

It does **not** claim that the labels below are mathematical impossibility theorems. They are a working evidence map grounded in current literature and should be revised as stronger results appear.

---

### 1. Evidence routes

Use the following evidence-route language when discussing a world variable.

```text
P0  single / static RGB evidence
P1  passive temporal RGB/video evidence
P2  active visual evidence: move camera/viewpoint, but sensory evidence remains visual
P3  action-response evidence: act on the world, observe visual consequence
N   non-visual / privileged evidence such as depth sensor, force, tactile, proprioception,
    IMU, simulator state or measured physical parameters
```

These are not new Clover sensor protocols. They are a Stage-1 way of stating **what kind of evidence a paper actually uses**.

Map them back to the canonical V0–V3 / L0–L4 protocol whenever a result is later evaluated.

---

### 2. High-level observability map

Legend:

- `strong` — substantial direct evidence exists;
- `possible-with-priors` — estimable, but strongly prior/model/data dependent;
- `history-important` — temporal evidence materially helps;
- `interaction-important` — controlled action-response materially improves identifiability;
- `non-visual-common` — current strong methods commonly rely on non-RGB state/sensing;
- `open` — no strong general conclusion yet.

| World variable | P0 static RGB | P1 passive video | P2 active view | P3 action-response | N non-visual | Current Stage-1 interpretation |
|---|---|---|---|---|---|---|
| image appearance / texture | strong | strong | strong | not required | not required | directly observed but viewpoint/illumination dependent |
| 2D position / mask | strong | strong | strong | not required | not required | visible support, not hidden existence |
| correspondence / optical flow | weak from one frame | strong | strong | useful | not required | motion evidence, not identity by itself |
| camera pose | possible-with-priors | strong | strong | useful | common for GT/eval | classical/learned geometry already strong |
| depth / metric scale | possible-with-priors | stronger | stronger | useful | depth sensor often used | monocular scale remains prior-dependent |
| 3D shape | possible-with-priors | stronger | strong | useful | RGB-D common | reconstruction does not imply physics/function |
| object identity | possible-with-priors | history-important | stronger | useful | not inherently required | visible tracking is weaker than permanence |
| amodal shape / hidden extent | possible-with-priors | history-important | stronger | useful | GT often privileged | completion may be prior-driven hallucination |
| object permanence | weak from one image | history-important | stronger | useful | omniscient GT useful for eval | must distinguish belief from observation |
| articulation state | possible-with-priors | stronger | stronger | interaction-important | joint GT common | configuration easier than unknown kinematic mechanism |
| kinematic constraints / joints | possible-with-priors | stronger | stronger | interaction-important | GT/sim common | active one-step interaction can reveal mechanism |
| mass | possible-with-priors | possible-with-priors | possible-with-priors | interaction-important | measured mass useful | RGB-only estimation is ill-posed and prior dependent |
| density / material semantics | possible-with-priors | possible-with-priors | possible-with-priors | interaction-important | direct measurement useful | appearance correlates with material but does not uniquely determine density |
| center of mass / inertia | open | possible-with-priors | possible-with-priors | interaction-important | force/state measurements common | especially important for manipulation and stability |
| friction | weak / prior-driven | weak / prior-driven | weak / prior-driven | interaction-important | haptic/force measurements common | current literature explicitly treats vision alone as insufficient in many settings |
| stiffness / compliance | weak / prior-driven | possible-with-priors | possible-with-priors | interaction-important | force/tactile common | deformation under known action is highly informative |
| contact state / topology | sometimes visible | stronger | stronger | interaction-important | force/tactile useful | contact may be visually ambiguous under occlusion |
| deformation state | possible | strong | stronger | interaction-important | depth/state common | cloth/rope/bag require state beyond rigid geometry |
| viscosity / fluid properties | weak / prior-driven | possible-with-priors | possible-with-priors | interaction-important | force/flow measurements common | appearance often insufficient for visually similar liquids |
| support / stability | possible-with-priors | stronger | stronger | useful | not inherently required | physical reasoning benchmark target |
| affordance / function | possible-with-priors | stronger | stronger | interaction-important | demonstrations useful | category/appearance priors can shortcut true function |
| action effect / controllability | not identifiable from one image | possible if natural interventions occur | stronger | strong | robot state often used | system identification is fundamentally action-linked |
| causal relation | weak | possible under assumptions | useful | strong | intervention metadata useful | observational equivalence is a core theoretical limitation |
| uncertainty / unknown state | model-dependent | history-important | stronger | stronger | not inherently required | calibration must be evaluated, not assumed from confidence scores |
| social/intentional state | weak / prior-driven | history-important | active observation useful | interaction-important | language/context often used | physical world includes other agents, not only objects |

The central implication is not that every useful variable must become an explicit coordinate in Clover.

The implication is that **future representations should be judged by whether they preserve the evidence needed to infer, revise, or act on these variables**.

---

### 3. Mass, density and scale

#### 3.1 Single-image mass estimation is explicitly ill-posed

**Physically Guided Visual Mass Estimation from a Single RGB Image**
Primary paper: https://arxiv.org/abs/2601.20303
Evidence: `PRIMARY_PAPER`

The paper explicitly frames visual mass estimation as ill-posed because mass depends on both volume and material-dependent density, neither directly observed from a single RGB image.

Its solution uses learned monocular 3D geometry plus coarse material semantics to constrain plausible volume/density factors.

Stage-1 interpretation:

```text
RGB appearance
+ learned geometry prior
+ material/world prior
→ mass estimate
```

is not equivalent to:

```text
RGB uniquely determines mass
```

This is an important example of the distinction between **useful statistical inference** and **physical identifiability**.

#### 3.2 Real-object mass benchmark

**PhysQuantAgent / VisPhysQuant**
Primary paper: https://arxiv.org/abs/2603.16958
Evidence: `PRIMARY_PAPER`

VisPhysQuant contains multi-view RGB-D video with measured object masses. The method uses visual prompting, scale reasoning and inferred internal cross-sections to improve mass estimation.

Important Clover caveat:

RGB-D is outside strict `V0/V1` RGB-only observation. Use the benchmark as evidence about physical-quantity reasoning, but do not silently report it as a pure RGB result.

Stage-2 question:

> How much of mass estimation performance comes from geometry, material/world priors, metric scale, or memorized object-category statistics?

---

### 4. Friction is a strong example of interaction-limited knowledge

#### 4.1 Visual + haptic friction mapping

**Probabilistic Surface Friction Estimation Based on Visual and Haptic Measurements**
Primary paper: https://arxiv.org/abs/2010.08277
Evidence: `PRIMARY_PAPER`

This work explicitly states that visual observation alone does not convey enough information to estimate surface friction reliably. It combines visual correlation with limited haptic exploration.

This older result remains conceptually important because it gives a concrete case where:

```text
appearance similarity
≠
physical interaction equivalence
```

#### 4.2 Material-pair friction requires interaction structure

**Generalizable Friction Coefficient Estimation via Material Embedding and Proxy Interaction Modeling**
Primary paper: https://arxiv.org/abs/2604.24188
Evidence: `PRIMARY_PAPER`

The method predicts pairwise friction through measured interactions against a small fixed proxy-material set, rather than inferring friction directly from RGB appearance.

Stage-1 implication:

Friction is not merely an intrinsic property of one visible object. It is often a **pairwise interaction property** depending on two materials and contact conditions.

#### 4.3 Behavior-grounded terrain/contact calibration

**DR-WM — From Pixels to Executable Physics**
Primary paper: https://arxiv.org/abs/2610.17630
Submitted: 2026-10-13
Evidence: `PRIMARY_PAPER`

DR-WM reconstructs scene geometry from RGB and calibrates spatial terrain/contact priors using real robot action-response experience before simulating candidate actions.

This creates a particularly useful boundary case:

```text
geometry from vision
+
physical parameter calibration from action-response
```

Stage-2 question:

> Which action-relevant physical parameters can be inferred statistically from appearance, and which require system identification through interaction?

---

### 5. Articulation, function and physically usable object models

#### 5.1 Active interaction can reveal unknown articulated structure

**DexSim2Real²**
Primary paper: https://arxiv.org/abs/2409.08750
Evidence: `PRIMARY_PAPER`

The system constructs an explicit digital twin of unseen articulated objects using the world state before and after an active one-step interaction.

This is valuable Stage-1 evidence that articulation may be partially observable from appearance, but precise manipulation benefits from **interaction that reveals kinematic structure**.

#### 5.2 Physical function goes beyond visual asset quality

**Artisan**
Primary paper: https://arxiv.org/abs/2610.13947
Submitted: 2026-10-09; revised 2026-10-12
Evidence: `PRIMARY_PAPER`

Artisan evaluates articulated asset generation not only by appearance, but also through collision, gravity stability, mass/material attributes and downstream functional use.

Key distinction:

```text
looks like a usable object
≠
has correct articulation
≠
is dynamically stable
≠
functions correctly
```

Stage-1 implication:

Object understanding should eventually include **what motions are physically permitted and what function the object supports**, not only category or geometry.

---

### 6. One state representation may need to span rigid, articulated and deformable objects

#### PointCast

Primary paper: https://arxiv.org/abs/2609.28393
Project: https://pointcast-wm.github.io
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

PointCast represents objects and the robot end-effector as persistent identity-bearing 3D point sets and predicts future point trajectories conditioned on recent history and commanded motion.

The same architecture/training recipe is applied across:

- rigid objects;
- cloth;
- rope;
- multi-joint cabinets.

The checkpoints are trained separately by regime, so this does **not** yet establish one universally shared physical model.

Why it matters for Clover:

It is a strong counterexample to assuming that every material class requires a completely different ontology. A topology-agnostic point-state can span several regimes while retaining explicit correspondence.

Stage-2 question:

> Which properties are genuinely shared across rigid, articulated and deformable dynamics, and which require regime-specific latent structure?

---

### 7. Deformation, cloth, rope and soft systems

#### 7.1 Cloth world models

**Learning to Unfold Cloth: Scaling up World Models to Deformable Object Manipulation**
Primary paper: https://arxiv.org/abs/2602.16675
Evidence: `PRIMARY_PAPER`

The work modifies a Dreamer-style world model for cloth manipulation, including surface-normal input and changes to replay/data augmentation, and evaluates zero-shot physical-robot transfer.

Important protocol note:

Surface normals are stronger geometric evidence than raw monocular RGB and should be annotated accordingly when comparing to strict vision-only systems.

#### 7.2 Contact-centric deformable dynamics

**WorldContact**
Primary paper: https://arxiv.org/abs/2609.19600
Evidence: `PRIMARY_PAPER`

WorldContact makes contact structure central for deformable manipulation and uses model-generated trajectories to expand policy data.

Stage-1 question:

> Does a general world model need an explicit contact representation, or can contact emerge reliably inside a distributed predictive state?

#### 7.3 Soft robot embodiment itself is deformable state

**ManiSoft**
Primary paper: https://arxiv.org/abs/2605.18617
Project/code/data: https://buaa-colalab.github.io/ManiSoft
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

ManiSoft shows that not only manipulated objects but the robot body itself can be deformable. Reported failures include inaccurate visual estimation of the robot's own proprioceptive state and poor exploitation of deformability under randomized scenes.

This expands the mother question:

```text
understanding external world state
+
understanding the body's own changing physical state
```

may both be required for general embodied intelligence.

---

### 8. Liquids and hidden physical properties

#### Vision-Language Model-based Physical Reasoning for Robot Liquid Perception

Primary paper: https://arxiv.org/abs/2404.06904
Evidence: `PRIMARY_PAPER`

The study evaluates common household liquids and reports that vision-only reasoning is substantially weaker than a setup where force/torque responses are converted into visual plots and jointly reasoned over.

The system estimates viscosity by using **interaction-derived non-visual evidence encoded visually**, so it must not be classified as proof that viscosity is recoverable from passive RGB.

Stage-1 implication:

For visually similar liquids, interaction response may be more informative than appearance.

Stage-2 question:

> Which fluid variables can be estimated from passive flow video, and which require known perturbations, metric calibration or force evidence?

---

### 9. Ego-motion and object-motion must be disentangled

#### 4DVGGT-D

Primary paper: https://arxiv.org/abs/2605.12027
Evidence: `PRIMARY_PAPER`

The paper identifies coupling between camera ego-motion and object motion as a core failure source for dynamic 4D reconstruction and proposes a progressive pose/dynamic decoupling pipeline.

Stage-1 implication:

A changing image can result from:

```text
camera moved
object moved
object deformed
lighting changed
scene changed
some combination of the above
```

A world representation that conflates these causes may reconstruct pixels while getting the world transition wrong.

#### DP-DeGauss

Primary paper: https://arxiv.org/abs/2604.07986
Evidence: `PRIMARY_PAPER`

Egocentric 4D reconstruction explicitly decomposes background, hands and manipulated objects, showing that first-person scenes require component-aware motion separation under strong occlusion and camera movement.

---

### 10. Object permanence can be trained explicitly, not only measured

#### WROP — Training Object Permanence in World Models

Primary paper: https://arxiv.org/abs/2609.28654
Evidence: `PRIMARY_PAPER`

WROP introduces 150 cognitive-science-inspired object-permanence/solidity tasks, large randomized training data and a held-out exam for video world models.

Why it matters:

PersistBench asks whether a system **remembers** out-of-view objects in realistic 4D settings. WROP asks whether core-permanence behavior can be **deliberately trained** through controlled synthetic curricula.

These should not be conflated:

```text
training cognitive prior
≠
measuring persistent real-world memory
```

Stage-2 question:

> Does synthetic permanence training create a transferable world-state capability or primarily task-family competence?

---

### 11. Active calibration can define the action/world interface

#### SyncWorld

Primary paper: https://arxiv.org/abs/2609.09155
Evidence: `PRIMARY_PAPER`

SyncWorld studies a subtle but important issue: the same numerical robot action does not have a universal pixel-space meaning across camera views, environments or robot embodiments.

It uses a visual calibration episode — paired actions and observed frames — to specify an environment/embodiment-specific action→visual mapping in context.

Stage-1 implication:

```text
same action vector
≠
same visible world transition
```

unless embodiment, controller, camera and geometry are accounted for.

This is central for cross-embodiment world models.

---

### 12. Robot-factored visual interfaces are another route to cross-embodiment transfer

#### Robot-Factored World Models via Robot Rendering

Primary paper: https://arxiv.org/abs/2607.22535
Evidence: `PRIMARY_PAPER`

The method separates:

1. commanded action;
2. nominal realized robot trajectory through known controller/kinematics;
3. rendered robot geometry;
4. scene response to that geometry.

It argues that direct action conditioning forces the world model to learn robot-specific action realization, while future-state conditioning can leak the answer.

Stage-1 question:

> What is the correct interface between embodiment-specific action and embodiment-general world dynamics?

This source should be compared with SyncWorld, PointWorld, Riemann-style sequence models and direct VLAs.

---

### 13. 3D point-flow world models make a different claim about transferable physical state

#### PointWorld

Primary paper: https://arxiv.org/abs/2601.03782
Project: https://point-world.github.io/
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

PointWorld represents both action and predicted scene change as 3D point flow and reports one pretrained model across rigid pushing, deformable/articulated manipulation and tool use.

Important protocol caveat:

PointWorld takes RGB-D inputs, so it is not a strict `V0/V1` monocular RGB baseline.

Research value:

It is a strong comparator for the hypothesis that **shared 3D geometric action/state coordinates** can improve cross-embodiment world modeling.

---

### 14. Uncertainty must be decision-aware

#### Decision-Aware Uncertainty Evaluation for Early Action Anticipation

Primary paper: https://arxiv.org/abs/2603.10061
Evidence: `PRIMARY_PAPER`

The work evaluates VLM confidence under partial temporal observation for human-robot interaction and studies calibration/selective prediction rather than only recognition accuracy.

Why it matters:

For world understanding, an answer is not enough. The system must also know when current visual evidence is insufficient.

Relevant metrics include:

```text
calibration
selective prediction
coverage
risk under abstention
prefix length / evidence amount
```

Stage-1 implication:

Epistemic correctness should eventually include:

```text
correct when confident
uncertain when evidence is insufficient
willing to seek more evidence
able to revise after new evidence
```

---

### 15. Affordance is a distinct state variable from category and geometry

#### RoboAfford++ / RoboAfford-Eval

Primary paper: https://arxiv.org/abs/2511.12436
Evidence: `PRIMARY_PAPER`

The dataset separates:

- object affordance recognition;
- functional interaction-point prediction;
- spatial affordance / free-space localization.

Stage-1 implication:

Knowing **what an object is** and **where it is** does not fully specify **how it can be used**.

Affordance may depend on geometry, material, articulation, task, embodiment and current world state.

---

### 16. A stronger working decomposition of “world state”

For Stage 1, it is useful to keep at least the following layers distinct.

```text
A. observation state
   pixels, masks, visible features, tracks

B. geometric state
   pose, depth, shape, camera, 3D structure

C. entity state
   identity, existence, articulation, hidden/occluded state

D. physical state
   velocity, acceleration, support, contact, deformation

E. latent physical parameters
   mass, density, inertia, friction, stiffness, viscosity, material properties

F. functional state
   affordance, articulation limits, usable parts, task-relevant constraints

G. causal / controllability state
   what changes what, action-response, intervention sensitivity

H. epistemic state
   observed, inferred, predicted, uncertain, unobserved, contradicted

I. social / intentional state
   other-agent goals, likely actions, interaction history
```

A future Clover representation does not need to expose all of these explicitly.

But Stage 2 and Stage 3 should ask, for each major method family:

> Which of these layers can be decoded or used reliably, under what evidence conditions, and with what failure modes?

---

### 17. Key Stage-1 distinctions strengthened by this map

```text
appearance ≠ material property
shape ≠ mass
material label ≠ friction coefficient
geometry ≠ contact dynamics
visible motion ≠ causal mechanism
commanded action ≠ realized action
static pose ≠ articulation mechanism
object category ≠ affordance
plausible video ≠ executable physics
confidence score ≠ calibrated uncertainty
long context ≠ correct persistent belief
RGB-only deployment ≠ knowledge learned only from vision
```

And most importantly:

```text
statistically predictable from pixels
≠
physically identifiable from pixels
```

This distinction should remain explicit throughout Clover research.

---

### 18. Priority Stage-2 reports implied by this map

When Stage 2 becomes active, prioritize reports that can clarify the evidence boundary:

```text
Physically Guided Visual Mass Estimation
PhysQuantAgent / VisPhysQuant
DR-WM
PointCast
PointWorld
WorldContact
DexSim2Real²
Artisan
SyncWorld
Robot-Factored World Models
WROP
Decision-Aware Uncertainty Evaluation
```

Suggested common questions:

```text
What is observed directly?
What is inferred using learned priors?
What requires temporal history?
What requires controlled action?
What uses privileged/non-visual evidence?
What is actually identifiable?
What is only statistically predictable?
What uncertainty is reported?
How does the representation revise after contradictory evidence?
Does the inferred state improve real action?
```

---

### 19. Open collection gaps

Stage 1 should continue searching for strong primary work on:

- center-of-mass and inertia estimation from visual evidence;
- stiffness/compliance identification from RGB video under known actions;
- passive-video friction inference without haptics;
- real-world fluid dynamics and viscosity from controlled visual interventions;
- granular materials;
- breakage, cutting, tearing and irreversible topology change;
- thermal state and temperature when not visually observable;
- acoustic/visual physical inference while preserving a strict visual-only ablation;
- amodal 3D/4D object state under long occlusion;
- dynamic semantic maps with object replacement/removal;
- visual system identification across unseen robot embodiments;
- uncertainty calibration for long-horizon world state, not only classification;
- causal intervention datasets with real RGB observations;
- negative results showing which physical quantities cannot be recovered robustly from RGB.

A missing result is itself useful Stage-1 information when it marks a plausible identifiability boundary.

---

**Stage-1 rule:** collect the variables and evidence conditions first. Do not decide the Clover ontology yet.

---

<a id="topic-research-research_identifiability"></a>

## Identifiability, Observability and Information Limits

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 theory/background document. It does **not** propose a Clover algorithm.

Its purpose is to prevent a recurring category error:

> A model predicting a hidden variable accurately on a dataset does not by itself show that the variable is uniquely determined by the visual evidence.

Stage 1 must distinguish **prediction**, **observability**, **identifiability**, **calibration**, and **action usefulness** before Stage 2 compares mechanisms.

---

### 1. Minimal formal problem

Let the real world have latent physical state

```text
S_t
```

and let a visual observation be generated by

```text
O_t = G(S_t, C_t, L_t, N_t)
```

where, conceptually:

- `C_t` — camera/viewpoint/calibration;
- `L_t` — illumination/appearance conditions;
- `N_t` — noise/unmodeled observation factors.

A passive visual learner receives an observation history

```text
O_1:t
```

and forms some internal representation

```text
Z_t = F(O_1:t).
```

An embodied active learner may also choose actions

```text
A_t
```

that change either the viewpoint or the physical world, producing later observations:

```text
S_{t+1} ~ T(S_t, A_t)
O_{t+1} ~ G(S_{t+1}, C_{t+1}, ...)
```

The research question is therefore not simply:

```text
Can F predict labels from O?
```

It is closer to:

```text
What aspects of S can be inferred from visual evidence?
Under what assumptions?
With what uncertainty?
Which aspects become identifiable only after additional views or interventions?
Which representation preserves enough information for prediction, revision and action?
```

---

### 2. Five concepts that must not be conflated

#### 2.1 Predictability

A variable may be statistically predictable because the training distribution contains strong correlations.

Example:

```text
visual appearance → likely material → likely density → likely mass
```

This can be useful without making mass uniquely observable from the image.

#### 2.2 Observability

In control/state-estimation language, observability asks whether hidden state can be recovered from available outputs over time under a specified model and input sequence.

For Clover the key lesson is conceptual:

```text
state recoverability depends on
observation process
+
dynamics
+
time
+
actions
+
assumptions
```

not on pixels alone in the abstract.

#### 2.3 Identifiability

Identifiability asks whether the underlying variables/model are uniquely recoverable — often only up to an allowed equivalence class — from the available data and assumptions.

Two different world models can generate the same observed evidence.

If so, no learning algorithm can distinguish them **from that evidence alone** without additional assumptions or interventions.

#### 2.4 Calibration / epistemic correctness

A system may be unable to identify the true hidden state but still be scientifically useful if it represents uncertainty correctly.

Correct behavior may be:

```text
I do not know
multiple worlds remain possible
I need another view
I need to interact
```

rather than forcing one state estimate.

#### 2.5 Action sufficiency

A representation need not reconstruct every property of reality to be useful for a robot.

A state can be action-sufficient even if it omits variables irrelevant to the task.

Conversely, a visually rich representation can be action-insufficient if it loses contact, constraint, identity or uncertainty information required for control.

---

### 3. Observational equivalence is central to “vision alone”

Define two candidate world states `S` and `S'` as observationally equivalent under an observation protocol if they generate indistinguishable allowed observations.

Conceptually:

```text
G(S) = G(S')
```

for all evidence available under that protocol.

Then the machine cannot uniquely know whether the true state is `S` or `S'` without:

- stronger priors;
- additional viewpoints;
- longer temporal history;
- controlled interaction;
- or another sensor modality.

Examples include:

- different metric scales producing similar monocular projection;
- visually similar materials with different density/friction;
- closed articulated mechanisms whose joint constraints are hidden;
- identical-looking containers holding liquids with different viscosity;
- hidden objects that may still exist, may have moved, or may have been removed while unobserved.

This motivates maintaining a **belief over plausible worlds** rather than silently converting one plausible completion into fact.

---

### 4. Geometry already contains classical ambiguity results

#### Multiple-view geometry / projective ambiguity

Background source:

- Multiple View Geometry — https://www.robots.ox.ac.uk/~vgg/hzbook/

Classical multi-view vision shows that reconstruction depends on camera geometry, calibration and motion constraints. Projective structure may be recoverable before metric/Euclidean structure.

#### Auto-calibration ambiguity

Primary/background source:

- Resolving Ambiguities in Auto-calibration — https://www.robots.ox.ac.uk/~vgg/publications/1998/Zisserman98/

The paper demonstrates that even common calibration constraints can fail to resolve specific geometric ambiguities under certain camera motions.

Stage-1 implication:

> “More frames” does not automatically mean “all geometry is determined.”

The information content depends on viewpoint diversity and degeneracy.

This is a useful precedent for modern learned world models: scale/model capacity cannot manufacture evidence absent from the observation process.

---

### 5. Passive temporal observation can make hidden state more observable — but not universally

Video adds:

- correspondence;
- velocity/motion;
- repeated views;
- temporal constraints;
- natural interventions caused by other actors;
- evidence about persistence and change.

But passive video still inherits ambiguity when multiple latent mechanisms produce similar visual trajectories.

Examples:

```text
same visible displacement
← different mass + force combinations

same sliding motion
← different friction + applied-force combinations

same deformation
← different stiffness + contact-force combinations
```

Without knowing the applied cause, inverse physical inference can remain underdetermined.

This is why Stage 1 should distinguish:

```text
passive dynamics observation
vs
controlled system identification
```

---

### 6. POMDPs formalize why belief state matters

Primary/background survey:

- Partially Observable Markov Decision Processes in Robotics: A Survey — https://arxiv.org/abs/2209.10342

Related robotics review:

- POMDPs and Robotics — https://arxiv.org/abs/2107.07599

The POMDP framework treats the true world state as only partially observed and maintains a belief distribution over possible states.

Clover is **not** assumed to require a textbook POMDP implementation.

The relevance is the distinction:

```text
true hidden state
≠
current observation
≠
agent belief about state
```

A general visual robotic brain should eventually answer:

- what has been observed directly?
- what is inferred?
- what remains uncertain?
- what evidence would reduce uncertainty?
- how should uncertainty affect action?

---

### 7. Active perception changes the information available without changing the sensor modality

Foundational source:

- Bajcsy, Active Perception — https://ieeexplore.ieee.org/abstract/document/5968

Active perception treats sensing as a controlled process: the agent chooses actions that acquire informative observations.

This is highly relevant to the Clover phrase **vision alone**.

A robot may remain visually sensed while moving the camera/body to obtain a better view:

```text
uncertainty
→ choose viewpoint
→ new RGB evidence
→ update belief
```

This is still fundamentally different from passively receiving a video stream.

Current reference:

- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810
- Code — https://github.com/q1xiangchen/Vantage

Stage-1 question:

> Which ambiguities can active viewpoint selection resolve without touching the world?

---

### 8. Physical interaction is an intervention, not merely another frame

When an agent pushes, lifts, opens, compresses or otherwise perturbs the world, the resulting observation contains information about how the world responds to a known action.

Conceptually:

```text
known action
+
visual response
→ constraints on hidden dynamics / physical parameters
```

This is system identification through embodied visual interaction.

Examples already tracked in Stage 1:

- DR-WM — https://arxiv.org/abs/2610.17630
- DexSim2Real² — https://arxiv.org/abs/2409.08750
- SyncWorld — https://arxiv.org/abs/2609.09155

The key research distinction is:

```text
active vision: move to see
vs
active intervention: act to make hidden physics reveal itself
```

Both can remain **vision as the sensory evidence** if non-visual state is withheld from the learner, but they have very different identifiability power.

---

### 9. Causal representation learning shows why interventions can make latent variables identifiable

#### Interventional Causal Representation Learning

Primary source:

- https://proceedings.mlr.press/v202/ahuja23a.html

The paper proves identifiability results for latent causal factors under interventional data and explicit assumptions.

#### General Identifiability and Achievability for CRL

Primary source:

- https://proceedings.mlr.press/v238/varici24a.html

The work gives identifiability/achievability guarantees under multiple hard interventions per latent node for general nonlinear transformations under its stated assumptions.

#### Multi-node interventions

Primary source:

- https://proceedings.mlr.press/v236/bing24a.html

This work explicitly starts from the fact that causal representation learning from low-level observations is fundamentally underconstrained and derives identifiability conditions using diverse multi-node intervention environments.

#### Grouped observational variables

Primary source:

- https://proceedings.mlr.press/v235/morioka24a.html

This line shows that interventions are not the only theoretical route: sufficiently strong structural assumptions on grouped observations can also restore identifiability.

Stage-1 implication:

There is no universal statement such as:

```text
causal variables require interaction
```

or

```text
passive observation is always enough
```

The correct question is:

> Under which assumptions and data regimes is a particular latent structure identifiable?

---

### 10. Experiment design and representation identifiability are linked

Primary source:

- An Interventional Perspective on Identifiability in Gaussian LTI Systems with ICA — https://proceedings.mlr.press/v236/rajendran24a.html

This work connects diverse intervention signals with system-parameter identifiability in dynamical systems.

For Clover, the broader lesson is important:

```text
representation learning
and
data acquisition policy
cannot always be studied independently
```

A poor experiment may make a good representation impossible to identify.

A well-chosen intervention may expose structure that passive data hides.

---

### 11. Modern world models are beginning to target identifiable coordinates explicitly

#### Identifiable World Models from Pretrained Diffusion Representations

Primary paper:

- https://arxiv.org/abs/2610.07028

The method keeps a pretrained distributed diffusion representation and learns an alignment layer that can recover identifiable dynamical coordinates under explicit nonlinear-ICA assumptions.

This strengthens a third representation route:

```text
fully hand-designed explicit state
vs
fully opaque distributed latent
vs
powerful latent + identifiable coordinates
```

Stage-1 caution:

Theoretical identifiability depends on assumptions. Success in controlled physical/robotic systems does not prove arbitrary real-world RGB state will be identifiable.

---

### 12. Identifiability should be stated per variable, not for “the world” as one object

A real scene contains heterogeneous variables with different evidence requirements.

For example:

```text
visible color/texture             directly observed
2D mask                           directly observed while visible
3D shape                          inferred from geometry/prior/multiple views
object identity                   temporal association + priors
hidden existence                  belief / memory
mass                              geometry + density prior or interaction
friction                          material/contact interaction
stiffness                         deformation under force/action
articulation mechanism            geometry + motion + often interaction
causal dependency                 temporal structure + assumptions/intervention
intent of another agent           behavioral history + model assumptions
```

Therefore, the phrase:

```text
"the representation identifies the world state"
```

is too coarse unless the paper states **which state variables and under which equivalence class**.

---

### 13. A Stage-1 taxonomy of ambiguity

#### A. Geometric ambiguity

Examples:

- scale;
- depth;
- calibration;
- symmetry;
- occluded shape.

Typical remedies:

- multi-view geometry;
- calibration priors;
- active viewpoint changes;
- learned scene priors.

#### B. Identity ambiguity

Examples:

- similar objects crossing;
- long occlusion;
- object leaves and re-enters FOV;
- object replacement while unobserved.

Typical evidence:

- temporal continuity;
- appearance;
- spatial context;
- persistent memory;
- re-observation.

#### C. Physical-parameter ambiguity

Examples:

- mass;
- density;
- friction;
- stiffness;
- viscosity;
- inertia.

Typical evidence:

- statistical material priors;
- observed natural dynamics;
- known perturbations;
- action-response;
- force/tactile/state measurements.

#### D. Causal ambiguity

Examples:

- correlation vs direct cause;
- hidden common cause;
- multiple mechanisms producing similar outcomes.

Typical remedies:

- structural assumptions;
- environment changes;
- interventions;
- counterfactual constraints.

#### E. Epistemic ambiguity

Examples:

- object unobserved vs absent;
- low confidence because of lack of evidence vs model weakness;
- generated completion vs evidence-supported state.

Required capability:

- calibrated uncertainty;
- provenance;
- abstention;
- active evidence acquisition;
- belief revision.

---

### 14. Implication for Stage-2 method reports

Every serious Stage-2 analysis should include an **identifiability section**:

```text
Target variables:
What does the method claim to represent/predict?

Observation evidence:
Static RGB / passive video / multi-view / active view / action-response / non-visual state?

Assumptions:
Rigid world? Known camera? Known action? Known embodiment? Known material class?

Ambiguities:
Which alternative worlds are still compatible with the same evidence?

Priors:
What is being supplied by pretrained language/vision/world knowledge?

Intervention:
Does the method receive controlled perturbations or only observational data?

Uncertainty:
Does it represent multiple plausible states or force a point estimate?

Identifiability claim:
Is there a theorem, controlled empirical evidence, or only predictive performance?

Action value:
Does distinguishing the latent state improve decisions or execution?
```

This will prevent later Synthesis from comparing methods as if they had equal information budgets.

---

### 15. Implication for evaluation

Future Clover experiments should intentionally construct pairs of worlds that are:

#### observationally indistinguishable under a weaker protocol

but

#### distinguishable under a stronger protocol.

Examples:

```text
same appearance, different mass
→ passive image ambiguous
→ lift/push response discriminates

same object hidden behind occluder
→ current frame ambiguous
→ memory/re-observation discriminates

same visible pose, different articulation constraint
→ image ambiguous
→ controlled push discriminates

same object trajectory, different force/friction explanation
→ passive video underdetermined
→ known applied action discriminates
```

This suggests an eventual hierarchy of **identifiability batteries**, not just recognition benchmarks.

---

### 16. What “vision alone” should mean scientifically

Clover should continue separating two claims:

#### Sensor claim

> The machine's evidence channel at inference is visual.

#### Learning/knowledge claim

> The machine learned the relevant physical/world structure only from visual evidence.

These are not equivalent.

A robot may:

- see RGB only at inference;
- have learned material density from text;
- have learned action dynamics from robot-state demonstrations;
- use camera calibration supplied externally;
- use simulator state during training.

All can improve prediction without proving visual identifiability.

This is why the V0–V3 observation protocol and L0–L4 learning-evidence provenance remain necessary.

---

### 17. Current Stage-1 theoretical position

The evidence does **not** currently support any simple universal statement such as:

```text
all world variables can be learned from passive vision
```

or

```text
an explicit physics engine is necessary
```

or

```text
interaction is always required
```

Instead, the more defensible research position is:

> Real-world visual understanding is a family of inverse problems under partial observability. Different latent variables have different identifiability conditions. Temporal history, viewpoint control, physical interventions and prior knowledge change what can be inferred. A general robotic brain should represent not only a best world estimate, but the uncertainty and evidence conditions under which that estimate is justified.

This is a research constraint, not yet a representation design.

---

### 18. Priority open questions

1. Which physical variables are identifiable from monocular RGB video under realistic motion diversity?
2. Which variables require known actions but no non-visual sensing?
3. Which variables remain poorly identifiable even with visual action-response?
4. Can large pretrained visual/video representations discover intervention-relevant coordinates without explicit supervision?
5. Can a model distinguish uncertainty caused by occlusion from uncertainty caused by model ignorance?
6. How should active perception optimize evidence acquisition for multiple competing world hypotheses?
7. What is the minimal sufficient world state for reliable robot action?
8. When does explicit uncertainty/persistent belief improve behavior over long-context policies?
9. How do language/world priors distort claims of visual physical understanding?
10. Can identifiability assumptions be tested empirically rather than merely assumed?

---

**Stage-1 rule:** before asking which representation is best, ask whether the target variable can be determined from the evidence supplied.

---

<a id="topic-research-research_observation_physics"></a>

## Observation Physics and Image-Formation Limits

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a different source of ambiguity from hidden world state:

> Even when the world state is fixed, the image formation process can hide, mix, distort or erase information before the machine sees the pixels.

The central distinction is:

```text
world-state ambiguity
≠
image-formation ambiguity
≠
sensor / camera corruption
```

A machine cannot recover a physically correct world state merely by becoming a better pattern recognizer if multiple scene configurations can generate the same visual evidence or if the imaging process destroys the relevant information.

---

### 1. Minimal image-formation view

A useful Stage-1 abstraction is:

```text
O_t = Camera(
    Geometry_t,
    Material_t,
    Illumination_t,
    Viewpoint_t,
    Motion_t,
    Medium_t,
    Exposure_t,
    Sensor_t,
    Noise_t
)
```

where the RGB observation `O_t` is the result of multiple coupled physical factors.

The inverse problem is therefore not simply:

```text
pixels → geometry
```

but more generally:

```text
pixels
→ possible combinations of
  geometry + material + lighting + motion + camera/sensor state.
```

Recent inverse-rendering literature explicitly emphasizes that many distinct geometry/material/lighting combinations can explain the same image.

Current survey:

- Recent Trends in Inverse Rendering — https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70592

Useful ambiguity analysis:

- Unveiling the Ambiguity in Neural Inverse Rendering: A Parameter Compensation Analysis — https://openaccess.thecvf.com/content/CVPR2024W/NRI/html/Kouros_Unveiling_the_Ambiguity_in_Neural_Inverse_Rendering_A_Parameter_Compensation_CVPRW_2024_paper.html
- arXiv version — https://arxiv.org/abs/2404.12819
- Diffusion Posterior Illumination for Ambiguity-aware Inverse Rendering — https://arxiv.org/abs/2310.00362

Stage-1 lesson:

```text
one plausible decomposition
≠
the uniquely correct physical decomposition.
```

---

### 2. Observation-physics map

| Observation phenomenon | What changes in pixels | What may become ambiguous | Stage-1 significance |
|---|---|---|---|
| projective viewpoint | scale, foreshortening, visibility | metric size/depth, hidden geometry | classical multi-view geometry reduces but does not eliminate all ambiguity |
| occlusion | evidence disappears | existence, identity, hidden shape/state | requires memory, uncertainty and/or active view |
| illumination change | intensity/color/shadow | material vs lighting | appearance constancy is not physical-state recovery |
| cast shadow | local darkness | geometry/material/light attribution | shadow can be evidence or nuisance depending on task |
| specular reflection | view-dependent highlight/reflection | surface color, texture, normal/shape | violates simple diffuse/Lambertian assumptions |
| transparency/refraction | background rays are displaced/mixed | surface geometry, depth, occupancy | ordinary RGB-D may also fail because depth sensors can be corrupted |
| motion blur | temporal integration within exposure | correspondence, pose, object motion | fast motion can erase spatial detail before inference |
| rolling shutter | different rows captured at different times | rigid-scene geometry vs camera-motion distortion | camera model must be part of the observation model |
| exposure / HDR saturation | clipping / missing dark detail | color, texture, feature correspondence | information may be physically lost by acquisition |
| sensor noise/compression | stochastic/quantization artifacts | fine texture and correspondence | representation robustness cannot recover information that was never recorded |
| atmospheric medium | haze/rain/fog/scatter | contrast, depth, appearance | observed radiance includes medium effects, not only object properties |

This is a working map, not a complete optics textbook.

---

### 3. Geometry, material and illumination can compensate for one another

Inverse rendering is a useful foundation because it makes explicit that vision is attempting to invert a forward image-formation process.

The 2026 inverse-rendering survey organizes work around recovering:

```text
geometry
material / reflectance
illumination
```

from images, and identifies the problem as inherently ill-posed.

A bright region may be explained by, for example:

```text
bright material
strong illumination
specular reflection
surface orientation
viewpoint-dependent effect
```

or combinations of these.

The CVPR 2024 parameter-compensation analysis demonstrates that inverse-rendering systems can compensate an error in one estimated scene property by changing another scene property while still explaining the observations.

Stage-1 implication:

> Photometric reconstruction error can be low even when the recovered physical decomposition is wrong.

This directly parallels Clover's broader distinction:

```text
reconstruct the observation
≠
recover the true world state.
```

---

### 4. Transparent and refractive objects expose a hard image-formation failure

#### 4.1 Trans2Occ

**Trans2Occ: Voxel Occupancy Estimation and Grasp for Transparent Objects from Simulation to Reality**
Primary paper: https://arxiv.org/abs/2606.01777
Evidence: `PRIMARY_PAPER`

Transparent objects are difficult because refraction and reflection can make conventional depth sensing unreliable. Trans2Occ predicts voxel occupancy from a single RGB image using large-scale synthetic supervision and transfers the representation to real robotic grasping.

Why it matters:

```text
successful occupancy prediction from RGB
```

can depend on learned shape/material priors and synthetic training distributions; it does not imply that transparent geometry is uniquely determined by the pixels.

#### 4.2 SR3D

**SR3D: Unleashing Single-view 3D Reconstruction for Transparent and Specular Object Grasping**
Primary paper: https://arxiv.org/abs/2505.24305
Evidence: `PRIMARY_PAPER`

SR3D combines single-view reconstruction and RGB-D scene information to recover usable transparent/specular object geometry for grasping.

Protocol warning:

It is not strict RGB-only evidence because RGB-D scene input is part of the localization/reconstruction pipeline.

Stage-2 question:

> How much transparent-object geometry comes from actual visual evidence versus category/generative shape priors?

---

### 5. Specular reflection changes the meaning of appearance

#### UnReflectAnything

**UnReflectAnything: RGB-Only Highlight Removal by Rendering Synthetic Specular Supervision**
Primary paper: https://arxiv.org/abs/2512.09583
Project: https://alberto-rota.github.io/UnReflectAnything/
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

The work treats specular highlights as corruption that can obscure texture and hinder geometry reasoning. It trains using physically motivated synthetic highlights and predicts a reflection-free diffuse reconstruction.

Stage-1 implication:

A pixel can contain information about:

```text
object reflectance
+
illumination
+
view direction
+
surface normal
```

rather than a stable intrinsic object color.

Therefore:

```text
appearance feature
≠
intrinsic material state.
```

---

### 6. Motion blur is information integration, not just image noise

**On Motion Blur and Deblurring in Visual Place Recognition**
Primary paper: https://arxiv.org/abs/2412.07751
Evidence: `PRIMARY_PAPER`

The work benchmarks visual place recognition under different motion-blur intensities and studies when deblurring improves localization.

Why it matters:

Motion blur is produced because a conventional frame integrates light over a nonzero exposure interval.

Conceptually:

```text
one RGB frame
≈
integral of changing scene/camera projections over exposure time.
```

Consequently, the observation is not necessarily an instantaneous world state.

Stage-1 questions:

```text
When should the world model model exposure-time integration explicitly?
How should uncertainty grow when blur destroys correspondence evidence?
Can temporal context reconstruct information lost in one frame, or only guess it from priors?
```

---

### 7. Rolling shutter means one frame may not correspond to one camera pose

**Rolling-Shutter Modelling for Direct Visual-Inertial Odometry**
Primary paper: https://arxiv.org/abs/1911.01015
Evidence: `BACKGROUND_REFERENCE`

Rolling-shutter cameras capture different image rows at different times. Ignoring this effect can strongly degrade geometric state estimation.

The cited method uses IMU information and therefore is not a vision-only baseline; its value here is conceptual.

Stage-1 implication:

```text
frame timestamp
```

is not always equivalent to:

```text
all pixels observed from one pose at one instant.
```

The camera acquisition process can itself create apparent nonrigid deformation in a rigid scene.

---

### 8. Low light, overexposure and illumination shifts alter observability

**Benchmarking Visual Feature Representations for LiDAR-Inertial-Visual Odometry Under Challenging Conditions**
Primary paper: https://arxiv.org/abs/2603.18589
Evidence: `PRIMARY_PAPER`

The paper studies low light, overexposure, illumination changes and high-parallax conditions and reports degradation/failure of ordinary photometric visual methods under severe photometric inconsistency.

Protocol warning:

The evaluated system is LiDAR-inertial-visual, so it is evidence about visual degradation and multimodal compensation, not a strict RGB-only result.

Stage-1 implication:

A general visual brain must distinguish:

```text
world changed
```

from:

```text
lighting/exposure changed.
```

Otherwise illumination variation can be mistaken for object/material/world-state change.

---

### 9. Event cameras are an informative non-RGB counterexample

**Event-based SLAM Benchmark for High-Speed Maneuvers (EvSLAM)**
Primary paper: https://arxiv.org/abs/2604.24033
Evidence: `PRIMARY_PAPER`

Event cameras react asynchronously to brightness changes and are studied specifically because conventional frames struggle under high-speed motion and extreme lighting.

Event cameras are outside Clover's strict RGB target.

Their Stage-1 role is diagnostic:

> When another sensing architecture is introduced specifically to avoid motion blur / dynamic-range limitations, that reveals information limitations of ordinary frame acquisition that a vision-only RGB system must either tolerate, model or express as uncertainty.

---

### 10. Observation failure and world uncertainty should not be conflated

Suppose a robot cannot determine whether an object is present.

Possible causes include:

```text
object is behind another object
image is overexposed
object is transparent
surface is mirror-like
motion blur erased the contour
camera viewpoint is insufficient
world genuinely contains two plausible hidden states
```

These should not all collapse into one generic low-confidence scalar.

A useful later Analysis taxonomy is:

```text
EPISTEMIC-WORLD uncertainty
    multiple real-world states fit the evidence

OBSERVATION uncertainty
    image-formation/acquisition process is unreliable

MODEL uncertainty
    learner is outside its competence/data distribution
```

Stage 1 does not yet prescribe how Clover should represent these categories; it records that they are different sources of uncertainty.

---

### 11. Active vision can change the observation operator

Active perception is useful not only because another viewpoint reveals an occluded object.

Changing viewpoint can also change:

```text
parallax
specular reflection
refraction path
shadow geometry
surface visibility
scale / foreshortening
```

Therefore an active agent can choose views that make an inverse problem better conditioned.

Relevant foundational/current references:

- Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810
- Vantage code — https://github.com/q1xiangchen/Vantage

Stage-2 question:

> Can an agent learn which viewpoint specifically disambiguates geometry/material/light explanations rather than merely collecting more images?

---

### 12. Proposed Stage-2 analysis dimensions

For methods that claim world reconstruction or persistent visual understanding, later Analysis should record:

```text
camera model
exposure model
rolling/global shutter assumption
illumination assumption
reflectance/material assumption
transparent/specular handling
occlusion handling
metric-scale source
static/dynamic scene assumption
whether image formation is explicitly modeled
whether ambiguity is represented or collapsed to one estimate
whether active viewpoint selection is supported
```

A method should not receive credit for recovering physical state when the evaluation only shows photometric reconstruction under the same observation assumptions.

---

### 13. Current open questions

1. How much of modern foundation-model robustness is true image-formation invariance versus learned dataset prior?
2. Can a general RGB world model maintain multiple physically plausible inverse-rendering hypotheses rather than one generated explanation?
3. How should the system separate illumination/material change from actual object/world change?
4. Which camera effects must be modeled explicitly, and which can safely be absorbed by learned representations?
5. When does active viewpoint control resolve transparent/specular/occlusion ambiguity?
6. Can uncertainty be calibrated according to the source of missing information: world ambiguity, observation failure or model ignorance?
7. Which downstream actions are sensitive enough that image-formation ambiguity must be preserved rather than averaged away?

---

### Stage-1 provisional conclusion

The visible image is not the real world state.

More precisely:

```text
real world
→ light transport / image formation
→ camera acquisition
→ RGB pixels
→ learned representation
```

Each arrow can discard or entangle information.

Therefore a scientifically serious answer to:

> How can a machine understand the real world through vision alone?

must study not only the latent world behind the pixels, but also the **physical and computational observation operator that produced those pixels**.

**Do not treat the camera as a transparent window onto state.**

---

<a id="topic-research-research_physical_properties"></a>

## Hidden Physical Properties, Contact and Irreversible Change

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research inventory. It does **not** propose a Clover architecture.

Its purpose is to deepen one part of [`PERCEPTION.md`](#topic-research-research_state_variables): the real world contains important state that is only weakly visible, becomes informative only through temporal change or intervention, or changes irreversibly under contact.

The central questions are:

```text
Which physical properties are directly visible?
Which are only statistically predictable from appearance?
Which require observing dynamics?
Which become identifiable only through controlled interaction?
Which remain better measured through non-visual sensing?
How should a world model represent irreversible change?
```

Use the evidence-route notation from `PERCEPTION.md`:

```text
P0  static RGB
P1  passive temporal RGB/video
P2  active viewpoint changes while sensory evidence remains visual
P3  physical action-response observed visually
N   non-visual / privileged sensing or measured ground truth
```

---

### 1. Physical-property map

| Property / phenomenon | Current strongest evidence route | Stage-1 interpretation |
|---|---|---|
| visible geometry / shape | P0–P2 | strongly visually constrained, but metric scale and hidden surfaces remain prior-dependent |
| mass | P0/P1 possible with priors; P3 stronger | appearance/category/geometry can support prediction, but mass is not uniquely visible |
| density | P0/P1 possible with material priors; P3/N stronger | appearance may correlate with material, but density is a hidden physical parameter |
| center of mass | P3/N usually stronger | internal mass distribution is weakly constrained by appearance alone |
| moment of inertia | P3/N usually stronger | depends on mass distribution relative to axes, not just outer geometry |
| friction | P3/N | often pairwise/contact-condition dependent; appearance is not enough in general |
| stiffness / compliance | P1 under deformation; P3/N stronger | known perturbation and deformation response provide much stronger evidence than static appearance |
| temperature | N thermal/temperature sensing | RGB appearance generally does not expose object temperature reliably |
| viscosity | P1 possible from flow; P3/N stronger | flow under known perturbation is more informative than static appearance |
| granular packing / cohesion | P1/P3/N | hidden preparation state can substantially change interaction outcome |
| contact state | P1/P3; N tactile useful | visual contact may be ambiguous under occlusion |
| deformable configuration | P1–P3 | topology and dense geometry can change continuously |
| topology | P1/P3 | cutting, tearing, splitting and merging create state classes that cannot be represented as rigid pose updates |
| damage / breakage | P1/P3 | often irreversible; world-state identity and affordance may need revision after the event |
| function / affordance | P1–P3 | visual/category priors help, but interaction can reveal whether an object actually works as expected |

This table is an evidence map, not a theorem of impossibility.

---

### 2. Inertial properties: mass, center of mass and inertia

#### 2.1 Mass can be predicted visually without being visually identifiable

**Physically Guided Visual Mass Estimation from a Single RGB Image**
Primary paper: https://arxiv.org/abs/2601.20303
Evidence: `PRIMARY_PAPER`

The paper explicitly formulates single-image mass estimation as an ill-posed problem. Its solution combines learned monocular geometry with material semantics to constrain volume and density.

Stage-1 distinction:

```text
RGB
+ geometry prior
+ material/world prior
→ useful mass estimate
```

is not equivalent to:

```text
RGB uniquely determines mass.
```

#### 2.2 Physical-quantity benchmarks frequently rely on stronger sensing

**PhysQuantAgent / VisPhysQuant**
Primary paper: https://arxiv.org/abs/2603.16958
Evidence: `PRIMARY_PAPER`

VisPhysQuant provides multi-view RGB-D observations with measured object masses. It is useful for physical-quantity reasoning, but RGB-D is not a strict `V0/V1` observation protocol.

#### 2.3 Inertial parameters are a long-standing interaction problem

**Estimation and Exploitation of Objects' Inertial Parameters in Robotic Grasping and Manipulation: A Survey**
Primary paper: https://arxiv.org/abs/1911.04397
Evidence: `BACKGROUND_REFERENCE`

The survey organizes inertial-parameter estimation by interaction level: purely visual, exploratory interaction and fixed-object identification. This remains useful background because it makes center of mass and inertia explicitly different from simple appearance recognition.

#### Stage-1 gap

As of the current scan, we do **not** have a convincing modern general result showing that arbitrary real-object center of mass or moment of inertia is reliably identifiable from passive RGB alone.

Keep this as an explicit open problem rather than filling it with a category prior.

Stage-2 questions:

```text
How much inertial prediction comes from object-category memory?
Which controlled pushes/lifts/rotations most efficiently identify inertial parameters visually?
Should a robot maintain a probability distribution over inertial parameters until interaction reduces uncertainty?
```

---

### 3. Friction is an interaction property, not just an appearance label

#### 3.1 Visual + haptic friction mapping

**Probabilistic Surface Friction Estimation Based on Visual and Haptic Measurements**
Primary paper: https://arxiv.org/abs/2010.08277
Evidence: `PRIMARY_PAPER`

The work explicitly argues that vision alone does not provide enough information for reliable friction estimation and combines visual correlation with limited haptic exploration.

#### 3.2 Pairwise material interaction matters

**Generalizable Friction Coefficient Estimation via Material Embedding and Proxy Interaction Modeling**
Primary paper: https://arxiv.org/abs/2604.24188
Evidence: `PRIMARY_PAPER`

The method models friction through interactions between material pairs and measured proxy-material contacts instead of treating friction as a simple single-object image attribute.

#### 3.3 Behavior-grounded friction/contact in a world model

**DR-WM — From Pixels to Executable Physics**
Primary paper: https://arxiv.org/abs/2610.17630
Evidence: `PRIMARY_PAPER`

DR-WM obtains geometry visually, then calibrates spatial terrain/contact priors from real action-response evidence before simulating candidate actions.

Stage-1 implication:

```text
surface appearance
≠
friction coefficient
≠
pairwise contact behavior
```

and:

```text
world observation
+
controlled action
+
observed response
```

can reveal state that passive viewing leaves ambiguous.

---

### 4. Stiffness, compliance and tactile-grounded physical state

#### 4.1 ViTacPhys

**ViTacPhys: Physical Property-Aware Grasping from Human Visual-Tactile Demonstrations**
Primary paper: https://arxiv.org/abs/2608.21355
Evidence: `PRIMARY_PAPER`

ViTacPhys estimates mass classes, friction-coefficient classes and continuous stiffness from temporal human visual-tactile demonstrations and transfers the learned physical-property conditioning into robot grasping.

Why it matters:

The task demonstrates that explicit physical-property estimates can improve manipulation, but it is also a strong provenance warning:

```text
property is useful for action
≠
property came from vision alone
```

Tactile evidence is a central part of the method.

#### 4.2 Tactile world models

**DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation**
Primary paper: https://arxiv.org/abs/2609.20649
Evidence: `PRIMARY_PAPER`

DexTouch-WM combines a pretrained video expert with tactile features and action conditioning, and scales human interaction data to improve robot-domain visual, geometric and contact prediction.

#### 4.3 Tactile-grounded world-action policy

**TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation**
Primary paper: https://arxiv.org/abs/2609.19613
Evidence: `PRIMARY_PAPER`

TacSushi explicitly uses fingertip tactile features and predicts future visual/tactile/contact-related quantities during training.

Stage-1 implication:

Tactile-world-model results are useful **counterexamples** when defining a vision-only research goal: they reveal which difficult variables current researchers choose to measure through touch rather than infer from RGB.

---

### 5. Temperature is a clean example of a hidden state outside visible RGB

#### HEARTH

**HEARTH: An Object-Centric RGB-Thermal-3D Dataset for Temperature-Aware Robot Manipulation**
Primary paper: https://arxiv.org/abs/2609.23418
Evidence: `PRIMARY_PAPER`

HEARTH associates everyday objects with RGB, thermal measurements, reconstructed geometry and measured temperature state. Its robot-task ablation reports substantially better temperature-dependent object selection when thermal observations are added compared with RGB alone.

Why it matters:

Temperature gives Stage 1 a particularly clear boundary condition:

```text
same visible object appearance
can correspond to
different task-relevant thermal states.
```

Therefore a robot may need to represent:

```text
unknown temperature
```

rather than hallucinate a temperature from category or appearance.

This does not make thermal sensing part of Clover's sensory target. It provides evidence about what strict visible-spectrum vision may not determine.

---

### 6. Liquids and viscosity

**Vision-Language Model-based Physical Reasoning for Robot Liquid Perception**
Primary paper: https://arxiv.org/abs/2404.06904
Evidence: `PRIMARY_PAPER`

The study reasons about household liquids and reports stronger performance when interaction-derived force/torque information is converted into visual plots and combined with ordinary visual evidence.

The method must **not** be counted as proof that viscosity is recoverable from passive RGB: its strongest setting includes non-visual interaction evidence represented visually.

Stage-2 questions:

```text
What fluid properties are inferable from free-flow video?
What requires a known perturbation or pouring protocol?
How should uncertainty be represented for visually similar liquids?
```

---

### 7. Granular materials have hidden preparation state

**Robot Excavation and Manipulation of Geometrically Cohesive Granular Media**
Primary paper: https://arxiv.org/abs/2507.19999
Evidence: `PRIMARY_PAPER`

The experiments show large differences in transported mass depending on initial substrate compaction, and connect those differences to packing/cohesion/entanglement through physical testing.

Why it matters:

Granular material state is not fully summarized by visible surface geometry. Two visually similar piles may respond differently because of hidden preparation history.

Stage-1 distinction:

```text
visible surface shape
≠
internal packing / cohesion state
≠
interaction response.
```

This is a strong reason to keep **history-dependent material state** in the research inventory.

---

### 8. Deformable objects and contact-rich state

#### PointCast

Primary paper: https://arxiv.org/abs/2609.28393
Project: https://pointcast-wm.github.io
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

PointCast uses persistent identity-bearing 3D point sets to model rigid objects, cloth, rope and articulated cabinets with one general representation family.

#### WorldContact

Primary paper: https://arxiv.org/abs/2609.19600
Evidence: `PRIMARY_PAPER`

WorldContact makes contact-centric state central for deformable manipulation.

#### Learning to Unfold Cloth

Primary paper: https://arxiv.org/abs/2602.16675
Evidence: `PRIMARY_PAPER`

Adapts a world-model approach to cloth manipulation and reports real-robot transfer, but uses surface normals in addition to ordinary RGB.

#### ManiSoft

Primary paper: https://arxiv.org/abs/2605.18617
Project/code/data: https://buaa-colalab.github.io/ManiSoft
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

ManiSoft makes the robot body's own deformable state part of the problem, exposing visual estimation of self-state as a failure mode.

Stage-1 implication:

A general robotic brain may need to model:

```text
external deformable state
+
robot-body deformable state
+
contact state between them.
```

---

### 9. Irreversible topology change: cutting, splitting, tearing and breakage

Rigid-object tracking typically assumes that identity and topology survive action. Real manipulation violates that assumption.

#### 9.1 DoughNet

**DoughNet: A Visual Predictive Model for Topological Manipulation of Deformable Objects**
Primary paper: https://arxiv.org/abs/2404.12524
Evidence: `PRIMARY_PAPER`

DoughNet represents deformable objects with varying topology as sets of latent codes and predicts geometric deformation together with topology changes such as splitting/merging.

Why it matters:

```text
state update
```

cannot always mean:

```text
same entity, new pose.
```

A manipulation may create new entities, merge entities, destroy previous affordances or change connectivity.

#### 9.2 CulinaryCut-VLAP

**CulinaryCut-VLAP: A Vision-Language-Action-Physics Framework for Food Cutting via a Force-Aware Material Point Method**
Primary paper: https://arxiv.org/abs/2601.06451
Evidence: `PRIMARY_PAPER`

The framework couples robotic manipulation with a Material Point Method simulator for deformable food cutting, where cuts produce large deformation, contact forces and topology changes. Its dataset includes multi-view visual observations plus force-torque/tool-pose labels.

Protocol warning:

This is not a pure vision-only learning setup; privileged physical simulation and force/tool-state labels are part of the training/evaluation infrastructure.

#### 9.3 Sashimi-Bot

**Sashimi-Bot: autonomous tri-manual advanced manipulation and cutting of deformable objects**
Peer-reviewed article: https://www.nature.com/articles/s44182-026-00098-9
Evidence: `PRIMARY_PAPER`

Sashimi-Bot performs manipulation and cutting of natural deformable salmon using visual and tactile feedback, explicitly treating slicing as topology-altering state change.

Stage-1 implication:

A world representation intended for general robotics eventually needs a principled answer for:

```text
entity split
entity merge
material removal
irreversible deformation
breakage / damage
new affordances after transformation
invalidated old identity assumptions.
```

These are qualitatively different from reversible rigid-body motion.

---

### 10. Counterfactual and intervention datasets are becoming much more explicit

#### 10.1 What-If World

**What-If World: A Causal Benchmark for General World Models in Embodied Scenarios**
Primary paper: https://arxiv.org/abs/2605.27589
Evidence: `PRIMARY_PAPER`

The benchmark builds paired prompts from real nuScenes and DROID frames while varying one physical detail and evaluates whether generated futures change in the physically correct way.

This directly attacks a failure mode where two individually plausible videos do not respond correctly to an intervention.

#### 10.2 CRONOS

**CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models**
Primary paper: https://arxiv.org/abs/2605.23699
Evidence: `PRIMARY_PAPER`

CRONOS systematically intervenes on viewpoint, scene, object category and appearance while holding the physical event type fixed.

It is useful for testing whether physical prediction is invariant to nuisance visual changes.

#### 10.3 CausalPhys

**Causal Scaffolding for Physical Reasoning: A Benchmark for Causally-Informed Physical World Understanding in VLMs**
Primary paper: https://arxiv.org/abs/2606.05966
Evidence: `PRIMARY_PAPER`

CausalPhys contains image/video questions across perception, anticipation, intervention and goal-oriented reasoning together with expert-annotated causal graphs.

#### 10.4 CG-World

**CG-World: A Large-Scale World-State Dataset and Protocol for World Models**
Primary paper: https://arxiv.org/abs/2607.26452
Evidence: `PRIMARY_PAPER`

CG-World explicitly records latent world state, geometry, skeletal/controller state, physics caches, contact events, render passes and branch metadata. Its branch structure includes observation, action and mechanism interventions plus counterfactual branches.

Critical protocol note:

CG-World is highly structured synthetic/CG supervision. It is valuable because it gives precise ground truth that real video usually lacks, but it is not evidence that such state is available from real RGB input.

#### 10.5 Dream2Fix / counterfactual failure synthesis

**Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis**
Primary paper: https://arxiv.org/abs/2603.13528
Evidence: `PRIMARY_PAPER`

Dream2Fix perturbs actions inside a generative world model to synthesize paired failure/correction rollouts from successful real demonstrations and filters them for task validity, visual coherence and kinematic safety.

Why it matters:

Counterfactual data can be used not only for abstract causal QA but for **recovery behavior**.

---

### 11. Intervention-sensitive evaluation should become standard

Several 2026 results converge on the same warning:

```text
future looks plausible
```

does not imply:

```text
future changes correctly when the intervention changes.
```

Relevant sources:

- What-If World — https://arxiv.org/abs/2605.27589
- CRONOS — https://arxiv.org/abs/2605.23699
- RoboTrustBench — https://arxiv.org/abs/2606.01600
- CausalPhys — https://arxiv.org/abs/2606.05966
- Overcoming Statistical Bias in Action-Controllable World Models — https://arxiv.org/abs/2608.04653

This motivates a future Stage-3 distinction:

```text
plausible
→ controllable / intervention-sensitive
→ actionable
```

rather than ranking world models mainly by perceptual quality.

Related survey:

**World Models for Embodied Intelligence: From Plausible to Controllable to Actionable**
Primary paper: https://arxiv.org/abs/2609.16697

---

### 12. What this means for “vision alone”

The current evidence suggests at least four qualitatively different cases.

#### Case A — visually observable or strongly constrained

Examples:

```text
2D appearance
visible geometry
motion/correspondence
some articulation state
```

#### Case B — visually predictable but prior-dependent

Examples:

```text
mass from category/material/shape
material semantics
affordance from familiar object appearance
some hidden geometry
```

#### Case C — interaction reveals much stronger evidence

Examples:

```text
friction
stiffness/compliance
center of mass / inertia
action controllability
contact response
unknown articulation mechanism
```

#### Case D — current strong systems commonly use non-visual sensing

Examples:

```text
temperature
fine contact force
some tactile properties
high-precision proprioceptive failure timing
```

A future Clover representation should therefore not be judged only by how many hidden properties it can guess.

It should be judged by whether it can:

```text
separate observation from prior
represent uncertainty
request/choose informative visual or physical interaction
update beliefs after interaction
distinguish reversible from irreversible change
retain provenance for why a hidden property is believed
avoid converting missing evidence into false certainty.
```

---

### 13. Priority Stage-2 report queue from this file

High-value future method reports:

```text
Physically Guided Visual Mass Estimation
DR-WM
ViTacPhys
HEARTH
PointCast
WorldContact
DoughNet
CulinaryCut-VLAP
Sashimi-Bot
What-If World
CRONOS
CG-World
CausalPhys
Dream2Fix
```

Important comparison axes:

```text
P0/P1/P2/P3/N evidence route
visual-only vs multimodal provenance
explicit physical variables vs latent state
reversible vs irreversible transition
entity identity under split/merge
contact representation
uncertainty / calibration
counterfactual sensitivity
real-world versus simulator supervision
action usefulness
```

---

### 14. Open gaps that Stage 1 should continue searching

```text
pure-RGB center-of-mass estimation with strong real-world validation
pure-RGB moment-of-inertia estimation
passive-video stiffness/compliance identification
visual estimation of fracture / failure thresholds
visual thermal-state inference versus explicit thermal sensing
fluid property identification under controlled visual perturbations
granular internal-state estimation
real-world cutting/tearing datasets with topology ground truth
real-world causal-intervention datasets with matched initial conditions
cross-material generalization for hidden physical properties
uncertainty benchmarks for physical property inference
minimal intervention policies for identifying hidden physical parameters
```

Do not silently replace these gaps with language-model priors.

---

**A machine that understands the physical world must know not only what is visible, but which hidden properties are merely guessed, which have been identified through evidence, and when action changes the ontology of the world itself.**

---

<a id="topic-research-dossiers-r-a-observability-epistemology"></a>

## R-A — Observability, Epistemology and Belief State

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

A camera does not observe the physical state directly. It observes an image generated by hidden world state, viewpoint, visibility, illumination and sensor characteristics.

A minimal abstraction is:

```text
hidden state S_t
+ camera/view C_t
+ visibility / illumination / sensor process
→ RGB observation O_t
```

The research question is therefore not `pixels → truth`, but:

> **What can be identified from visual history, what remains ambiguous or unobserved, and what internal belief/state semantics are required for useful action under partial observability?**

This domain constrains all later representation choices.

### 2. Canonical foundations

#### POMDPs

- Survey: https://arxiv.org/abs/2209.10342

POMDPs formalize agents that must make decisions when the real state is not directly observable. The key object is a belief over possible states rather than a single guaranteed state.

**Demonstrates:** uncertainty-aware decision making under partial observation is a mature formal problem.

**Does not establish:** what visual representation should instantiate a scalable real-world belief state.

#### Probabilistic Robotics

- Book: https://mitpress.mit.edu/9780262201629/probabilistic-robotics/

Bayesian localization, mapping, filtering and state estimation provide a strong baseline for what uncertainty semantics already exist in robotics.

**Clover implication:** do not invent new words for `unknown`, `uncertain` or `unobserved` without comparing against Bayesian filtering and belief-state semantics.

### 3. Vision-only identifiability is limited

Monocular RGB generally does not make every physical variable uniquely observable.

Examples of possible ambiguity include:

- metric scale without calibration/prior;
- hidden geometry behind occlusion;
- exact mass, friction, force or internal material parameters from appearance alone;
- multiple world states that explain the same image history.

Therefore the project should distinguish at least:

```text
observed
inferred
unobserved
ambiguous / indistinguishable
contradicted
```

These are epistemic categories, not necessarily a commitment to a historical Clover licence implementation.

### 4. Partial observability also matters for causal representation

#### Partially Observable Causal Representation Learning

- ICML 2024: https://proceedings.mlr.press/v235/xu24ac.html

This work explicitly studies causal representation learning when each observation contains only a subset of latent causal state.

**Demonstrates:** representation learning and causal discovery become harder when observability changes instance by instance; identifiability can require explicit assumptions.

**Open contradiction:** can a visual world model discover stable state under changing visibility without privileged supervision?

### 5. Language and prior knowledge are epistemic confounds

A model that receives only RGB at deployment may still have learned substantial world knowledge from text, labels, robot state or privileged simulation.

Clover therefore uses two independent annotations:

```text
V-axis = inference-time visual observation protocol
L-axis = learning-evidence provenance
```

Current learning-evidence tags:

- `L0`: visual self-supervision only;
- `L1`: visual labels/annotations;
- `L2`: language/world-knowledge supervision;
- `L3`: action-conditioned experience;
- `L4`: non-visual or privileged physical evidence.

The purpose is not to reject multimodal models. It is to avoid attributing non-visual knowledge to vision itself.

### 6. Current strongest counterexamples

#### Gemini Robotics ER 2

- Official model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Official model page: https://deepmind.google/models/gemini-robotics/embodied-reasoning/

Gemini Robotics ER 2 is a VLM positioned as a high-level robot reasoner with spatial, temporal and physical reasoning.

**Why it matters:** it is a strong comparator for flexible embodied reasoning.

**Confound:** its capability includes large-scale language/world priors, so success cannot automatically be attributed to visual world formation.

### 7. Operational research questions

1. When an object is not visible, should the system represent `absent`, `unknown`, `occluded`, or a distribution over hypotheses?
2. How should confidence differ from observability?
3. How should contradictory new evidence update prior state?
4. Which physical variables are visually identifiable, approximately inferable, or fundamentally underdetermined?
5. Does explicit belief state improve action compared with a strong recurrent/latent policy?
6. Can a system know that two visually plausible hypotheses are currently indistinguishable?

### 8. Best baseline families

| Baseline | What it isolates |
|---|---|
| Bayesian filtering / occupancy | explicit uncertainty and observation update |
| ORB-SLAM3 | geometry/state estimation with explicit observability assumptions |
| V-JEPA 2 / recurrent latent | implicit predictive belief-like state |
| Gemini Robotics ER 2 | multimodal reasoner with strong prior knowledge |
| direct VLA policy | action without exposed belief state |

### 9. Discriminating experiments

#### T-A-01 — Unknown vs absent

Hide an object or region without providing evidence of removal.

Measure:

```text
false absence assertions
coverage / refusal
recovery after reappearance
planning error caused by false certainty
```

#### T-A-02 — Indistinguishable worlds

Create two worlds with identical visual histories up to time `t` but different hidden states.

Correct behavior before new evidence is not to guess the hidden state with unjustified certainty.

#### T-A-03 — Belief revision

```text
initial visual evidence
→ plausible world hypothesis
→ new contradictory evidence
→ local revision
→ downstream query / plan update
```

Measure revision latency, stale-state errors and unnecessary global recomputation.

#### T-A-04 — Provenance ablation

Compare models with the same inference RGB but different learning-evidence provenance (`L0/L2/L3/L4`) to estimate how much apparent physical reasoning comes from visual evidence versus external priors.

### 10. Kill conditions for explicit epistemic machinery

An explicit belief/epistemic layer should not survive merely because it is conceptually clean.

It should be reduced or removed if a simpler latent/recurrent model gives equal or better:

- unknown/absence correctness;
- calibration;
- belief revision;
- long-horizon task success;
- recovery;
- compute/memory cost.

### 11. Clover landing

This dossier does **not** promote licences or any historical authority mechanism.

It establishes a stricter requirement:

> **The next Clover representation must state what is observed, what is inferred, what is unobserved, what is ambiguous, and how these distinctions affect future queries and actions — or demonstrate empirically that an implicit alternative handles them better.**

---

<a id="topic-research-dossiers-r-b-geometry"></a>

## R-B — Geometry: What Is Already Solved?

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **Which parts of real-world visual understanding already have strong geometric formulations, and where do learned representations add genuinely new capability?**

Clover should not force a neural architecture to rediscover mature projective geometry if an explicit solution is already stronger, more interpretable and more reliable. Conversely, classical geometry should not be treated as sufficient for semantics, persistence, physics or causality.

### 2. Canonical foundations

#### Multiple View Geometry

- Hartley & Zisserman: https://www.robots.ox.ac.uk/~vgg/hzbook/

Key structures include:

```text
camera projection
homography
epipolar geometry
triangulation
multi-view reconstruction
bundle adjustment
```

These define exact geometric relationships independent of current deep-learning fashion.

#### Probabilistic state estimation

- Probabilistic Robotics: https://mitpress.mit.edu/9780262201629/probabilistic-robotics/

Geometry in a robot is not only reconstruction; it also involves state uncertainty, data association and sequential estimation.

### 3. Classical explicit baselines

#### ORB-SLAM3

- Paper: https://arxiv.org/abs/2007.11898
- Code: https://github.com/UZ-SLAMLab/ORB_SLAM3

**Demonstrates:** explicit camera trajectory, mapping, relocalization and multi-map reuse can be highly effective with engineered geometric structure.

**Does not establish:** semantic object identity, open-world category understanding, intuitive physics, hidden-state persistence or causality.

#### RAFT

- Paper: https://arxiv.org/abs/2003.12039
- Code: https://github.com/princeton-vl/RAFT

**Demonstrates:** dense temporal correspondence / optical flow is a strong motion primitive.

**Does not establish:** that a tracked pixel correspondence is a persistent entity or causal object.

### 4. Learned geometry changes the boundary

#### DUSt3R

- Paper: https://arxiv.org/abs/2312.14132

DUSt3R predicts point maps directly from image pairs and reduces dependence on a long classical correspondence→pose→triangulation pipeline.

**Research significance:** the useful question is no longer `classical geometry or learning?`; it is where explicit constraints and learned priors should divide labor.

#### VGGT

- Paper: https://arxiv.org/abs/2503.11651
- Code: https://github.com/facebookresearch/vggt

VGGT predicts multiple geometric quantities from images, including camera parameters, depth, point maps and tracks.

**Demonstrates:** a foundation model can serve as a broad learned geometry estimator rather than a task-specific depth or pose model.

**Does not establish:** persistent world memory, physical dynamics, causal state or action usefulness by itself.

#### VGGT-Ω

- Paper: https://arxiv.org/abs/2605.15195
- Project: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

VGGT-Ω extends the learned-geometry direction toward static and dynamic scene reconstruction and representation useful to downstream embodied systems.

**Key hypothesis to test:** reconstruction may be a scalable proxy for spatial understanding.

**Counter-question:** how far does reconstruction remain correct or useful once an object leaves the field of view, undergoes state change, or requires causal reasoning?

### 5. Geometry is not world understanding

A strong geometry system may correctly estimate:

```text
camera pose
depth
point correspondence
surface / point-map structure
motion
```

while still failing:

```text
same object after long occlusion?
object still exists outside view?
what is unknown versus empty?
what physical property caused an outcome?
what will an intervention change?
which geometry matters to a task?
```

This boundary must be measured rather than assumed.

### 6. Geometry and visible entities

#### SAM 3.1

- Official overview: https://ai.meta.com/blog/segment-anything-model-3/
- Code: https://github.com/facebookresearch/sam3
- Release notes: https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

SAM 3.1 improves efficient multi-object video detection/segmentation/tracking through shared-memory object multiplexing.

**Use for Clover:** a strong contemporary baseline for visible entity tracking.

**Important limit:**

```text
visible tracking
≠ object permanence
≠ persistent world state
```

A system that tracks an object while visible has not yet shown it can represent that object correctly after it leaves the field of view.

### 7. Geometry under missing views

#### Vantage

- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

Vantage plans a question-relevant view and then uses geometry-grounded evidence to improve multi-view spatial reasoning.

**Demonstrates:** failure can come from missing evidence, not just weak reasoning; viewpoint selection changes the observable geometry.

**Clover implication:** geometry and active perception should be linked in V3 experiments rather than treated as independent modules.

### 8. Operational research questions

1. Which geometric quantities are reliable enough to remain explicit?
2. Which quantities are better estimated by learned geometry foundation models?
3. Does learned geometry improve robustness mainly through priors, or does it encode task-relevant world structure absent from classical pipelines?
4. How should dynamic objects and camera motion be separated?
5. Can geometric state persist through long occlusion without a separate memory mechanism?
6. Does metric 3D reconstruction improve planning, generalization or recovery compared with a strong direct policy?
7. When geometry is uncertain, how should that uncertainty propagate into downstream decisions?

### 9. Best baseline matrix

| Family | Baseline | Isolates |
|---|---|---|
| Classical geometry | ORB-SLAM3 | explicit camera/map state |
| Dense motion | RAFT | short-term correspondence |
| Learned pairwise geometry | DUSt3R | learned point-map estimation |
| Geometry foundation model | VGGT | broad learned spatial state |
| Dynamic learned geometry | VGGT-Ω | dynamic reconstruction / global spatial representation |
| Visible entity tracking | SAM 3.1 | detection/segmentation/tracking while visible |

### 10. Discriminating experiments

#### T-B-01 — Geometry-only capability boundary

Use the same V0/V1 video and compare:

```text
ORB-SLAM3
RAFT
VGGT / VGGT-Ω
```

Queries:

```text
Where is the camera?
What moved?
Which points correspond?
What is behind / in front?
Same object after occlusion?
Still exists outside view?
What changed causally?
```

The purpose is to identify exactly where geometry stops being sufficient.

#### T-B-02 — Reconstruction vs persistence

Evaluate a reconstruction model before, during and after long out-of-FOV intervals using PersistBench-style ground truth.

Measure:

- geometric continuity;
- object identity continuity;
- appearance preservation;
- stale hallucinated geometry;
- uncertainty when evidence is absent.

#### T-B-03 — Geometry value for action

Matched comparison:

```text
strong policy
vs
same policy + explicit / learned geometry state
```

Measure unseen-scene success, planning cost, collision/reachability error and recovery.

#### T-B-04 — Camera shift

Hold world/task constant while changing intrinsics, viewpoint and trajectory.

This separates a genuinely geometric representation from camera-specific visual shortcuts.

### 11. Kill conditions

A geometry pathway should not be preserved as a privileged world representation if it adds no measurable benefit to:

- spatial correctness;
- generalization under camera shift;
- long-horizon persistence;
- planning/search cost;
- recovery;
- task success.

Likewise, a learned geometry model should not replace exact classical structure merely because it is newer if it is less reliable or less observable in the relevant regime.

### 12. Clover landing

Current conclusion:

> **Geometry is a solved-to-strongly-solved subproblem in several regimes, not a solved world-understanding problem. The next Clover representation must treat geometry as prior art to beat or reuse, then demonstrate what additional state is required for identity, memory, physics, causality and action.**

---

<a id="topic-research-dossiers-r-e-physics"></a>

## R-E — Physical Understanding: Plausibility, Quantification and Relational Structure

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **What does it mean for a vision-only system to understand physical behavior rather than merely recognize visually familiar motion?**

A useful ladder is:

```text
perceptual continuity
→ intuitive plausibility
→ quantitative kinematics
→ relational physical consistency
→ intervention-sensitive prediction
→ counterfactual consistency
→ improved action / recovery
```

No single benchmark covers this ladder.

### 2. Intuitive physics

#### IntPhys 2

- Paper: https://arxiv.org/abs/2506.09849
- Code: https://github.com/facebookresearch/IntPhys2
- Official Meta publication: https://ai.meta.com/results/?content_types%5B0%5D=publication&page=7

IntPhys 2 evaluates four principles:

```text
Permanence
Immutability
Spatio-Temporal Continuity
Solidity
```

using violation-of-expectation video pairs in controlled synthetic scenes.

**Demonstrates:** many strong models remain weak on controlled intuitive-physics violations despite good general visual capability.

**Limit:** synthetic controlled plausibility is not yet real-world quantitative physics or action-grounded causal understanding.

### 3. Shortcut-resistant physical reasoning

#### Minimal Video Pairs / MVPBench

- Paper: https://arxiv.org/abs/2506.09987
- Code/data reference: https://github.com/facebookresearch/minimal_video_pairs
- Meta physical-reasoning overview: https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/

MVP-style evaluation pairs videos that differ minimally but require opposite answers.

**Research value:** minimal pairs reduce the ability to solve a benchmark using background, language or coarse appearance shortcuts.

**Clover implication:** future physical-understanding claims should include paired intervention/perturbation controls, not only aggregate benchmark accuracy.

### 4. Quantitative physical reasoning

#### QuantiPhy

- Paper: https://arxiv.org/abs/2512.19526

QuantiPhy evaluates numerical estimation of physical properties such as size, velocity and acceleration from video.

**Demonstrates:** qualitative verbal plausibility can remain strong while numerical physical estimates are poor; models may rely heavily on pretrained world knowledge rather than the actual provided evidence.

**Clover implication:** physical understanding should include machine-checkable quantities, not only natural-language explanations.

### 5. Relational physics without calibration dependence

#### Principia

- Paper: https://arxiv.org/abs/2609.04200
- Project: https://principiabench.github.io/

Principia evaluates paired-object relational consistency for phenomena including:

- gravity;
- restitution;
- friction;
- rotational inertia;
- projectile motion;
- momentum;
- pendulum motion;
- mass-spring oscillation.

Its key methodological idea is that relative relationships between objects can remain diagnostic even when absolute scale, frame rate or camera calibration are ambiguous.

**Clover significance:** this is especially relevant to V0 vision, where exact metric calibration may be unavailable.

### 6. Physical variables can emerge in distributed representations

#### Interpreting Physics in Video World Models

- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Paper: https://arxiv.org/abs/2602.07050

The study finds layerwise emergence of speed, acceleration and motion direction, with direction encoded as a high-dimensional population code.

**Implication:** a model can carry useful physical information without exposing a compact symbolic physics state.

Therefore:

```text
physical understanding
≠ automatically explicit physics variables
```

### 7. Physics as prediction is still not physics as execution

#### RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

RoboPhys-3D evaluates world-model rollouts at multiple levels including pixel fidelity, 3D geometry consistency, state-level understanding and task-level completeness.

**Key lesson:** visually plausible generated video can still fail state- and execution-grounded metrics.

For Clover:

```text
plausible future video
≠ correct physical state
≠ executable consequence
```

### 8. Visually inferred physical properties must remain hypotheses

Vision may support useful estimates of:

```text
support
contact likelihood
relative mass hypothesis
slip risk
deformation tendency
material-like behavior
```

But exact hidden quantities such as force, friction coefficient or internal material parameters are not generally direct visual observations.

A scientifically careful system must distinguish:

```text
measured visually
inferred from dynamics
inferred from appearance prior
not identifiable from current evidence
```

### 9. Operational research questions

1. Which physical laws are learnable from passive video alone?
2. Which physical variables require interaction to become identifiable?
3. Is relational physics more robust than absolute metric prediction under V0?
4. Does a predictive latent encode enough physics for action without explicit state?
5. How much physical accuracy is hidden by visually realistic generation metrics?
6. Can the system distinguish visually plausible but physically impossible rollouts?
7. Do explicit physical variables improve novel-object transfer and recovery?

### 10. Best baseline battery

| Capability | Baseline / benchmark | What it measures |
|---|---|---|
| Intuitive plausibility | IntPhys 2 | permanence, continuity, solidity, immutability |
| Shortcut resistance | MVPBench | minimal visual changes with answer flips |
| Quantitative kinematics | QuantiPhy | numerical size/velocity/acceleration |
| Relational laws | Principia | calibration-independent Newtonian consistency |
| Latent physical representation | V-JEPA 2/2.1 probing | decodability of physical information |
| Execution-grounded state | RoboPhys-3D | world-model state and task consequences |

### 11. Discriminating experiments

#### T-E-01 — Qualitative vs quantitative split

Use the same video to ask:

```text
Will it fall?
How fast is it moving?
Which of two objects accelerates more?
What numerical acceleration is supported?
```

This separates language-level plausibility from quantitative grounding.

#### T-E-02 — Relational invariance

Vary:

```text
camera scale
frame rate
viewpoint
object appearance
```

while preserving the physical relation.

Measure whether the model preserves the correct relation.

#### T-E-03 — Appearance prior conflict

Construct objects whose visual appearance suggests one material/dynamics prior but whose observed motion supports another.

Measure whether the model follows actual visual dynamics or pretrained semantic expectation.

#### T-E-04 — Passive vs action-conditioned physics

Compare the same base representation before and after action-conditioned experience.

Measure gains in:

- consequence prediction;
- affordance transfer;
- intervention sensitivity;
- quantitative dynamics.

#### T-E-05 — State-grounded rollout

Evaluate generated/predicted futures by downstream reconstructed state and executable consequences, not by video quality alone.

### 12. Kill conditions

A proposed explicit physics mechanism should be removed if it does not outperform strong latent/video baselines on at least one of:

- quantitative prediction;
- relational invariance;
- intervention transfer;
- novel dynamics;
- planning/recovery;
- sample efficiency.

Likewise, a generative model should not be called physically grounded if its advantage exists only on perceptual/video metrics while state/action consequences are wrong.

### 13. Clover landing

Current conclusion:

> **Physical understanding should be treated as a layered empirical target—from plausibility through quantitative and relational constraints to intervention and action—not as a single score or a commitment to explicit physics variables.**

---

<a id="topic-docs-research-map-classical-vision"></a>

## Classical Computer Vision and Geometry

### Why Clover must study this seriously

Before deep learning, computer vision developed explicit mathematical machinery for recovering structure and motion from images. Clover should not force a learned model to rediscover every well-understood invariant merely to appear end-to-end.

The important question is:

> **Which parts of visual world understanding already have reliable mathematical structure, and where do those methods stop?**

### Core bodies of prior work

#### Projective and multi-view geometry

Provides explicit relationships among camera projection, epipolar constraints, triangulation, pose and 3D structure.

#### Structure from Motion / Bundle Adjustment

Jointly estimates camera states and 3D landmarks by minimizing geometric reprojection errors.

#### Visual odometry and SLAM

Maintains a spatial estimate while a camera moves through a scene. Modern SLAM systems add loop closure, relocalization and multi-map operation.

#### Optical flow

Estimates image-plane motion. Flow is not itself world motion, but it is a key observable for temporal geometry.

#### Tracking and filtering

Kalman filters, particle filters and data association formalize uncertainty, temporal prediction and observation updates.

#### Occupancy / mapping

Explicitly distinguishes observed free space, occupied space and often unknown space — a distinction directly relevant to Clover's observability semantics.

### ORB-SLAM3

ORB-SLAM3 is an open-source real-time system supporting visual, visual-inertial and multi-map SLAM across monocular, stereo and RGB-D configurations.

Primary source:

- https://github.com/UZ-SLAMLab/ORB_SLAM3

Clover should use it as an intellectual baseline for explicit persistent geometry, not as a module to import blindly.

### RAFT

RAFT is a learned optical-flow model built around recurrent all-pairs field transforms.

Primary source:

- https://github.com/princeton-vl/RAFT

It is useful as a reminder that the boundary between 'classical variable' and 'learned estimator' is already porous: the variable can remain explicit while the estimator is learned.

### What classical approaches solve well

- camera geometry under stated assumptions;
- metric/relative structure from multiple views;
- explicit state estimation and uncertainty propagation;
- loop closure/relocalization in structured environments;
- interpretable failure modes tied to observability and geometry.

### What they do not solve by themselves

- open-ended semantic abstraction;
- general object type formation;
- high-level physical common sense;
- causal understanding;
- broad transfer from large visual experience;
- deformable/non-rigid everyday worlds at general scope;
- task relevance and language-level goals.

### Clover research tension

The modern question is not classical **or** learning. A more useful decomposition is:

> **Which invariants should be structural, which estimators should be learned, and which abstractions must emerge from experience?**

This is likely more productive than rebuilding a purely hand-engineered or purely learned stack.

---

<a id="topic-docs-research-map-spatial-intelligence"></a>

## Spatial Intelligence

### Core question

> **How much of world understanding can be obtained by reconstructing and maintaining coherent geometry from vision?**

Spatial intelligence is broader than depth estimation. It includes camera/world geometry, consistent multi-view representation, reconstruction, scene completion and potentially simulation.

### Classical-to-learned transition

Traditional SfM/SLAM explicitly optimizes camera geometry and sparse/dense landmarks. Modern geometry foundation models increasingly infer camera and scene geometry directly with learned feed-forward systems.

This transition is important to Clover because it asks which parts of a world representation should be mathematically constrained and which should be learned from scale.

### VGGT

VGGT (CVPR 2025 Best Paper) is a feed-forward learned geometry model. The official repository describes direct inference of key 3D scene attributes including camera intrinsics/extrinsics, depth maps, point maps and 3D point tracks from one or many views.

Primary source:

- https://github.com/facebookresearch/vggt

#### Why Clover cares

VGGT demonstrates that a large learned visual model can collapse a traditionally multi-stage geometry pipeline into one learned inference system while still outputting explicit geometric quantities.

This creates a powerful hybrid precedent:

> **learned representation does not imply that the output world state must remain implicit.**

### VGGT-Ω

VGGT-Ω extends this line to larger-scale static and dynamic reconstruction. As of September 2026 the official repository exposes training code, reproduction checkpoints and data preparation material.

Primary sources:

- https://vggt-omega.github.io/
- https://github.com/facebookresearch/vggt-omega

#### Clover question

The project argues that reconstruction representations can transfer to broader spatial tasks. Clover should investigate the stronger proposition:

> **Is reconstruction sufficient as the spatial substrate of a persistent robot worldview, or does understanding require additional state for observability, object identity, dynamics, causality and task relevance?**

### DUSt3R / MASt3R family

These systems replace parts of classical multi-view correspondence and reconstruction with learned point-map style representations.

Reference:

- https://arxiv.org/abs/2312.14132

The relevant lesson is not to copy their architecture, but to understand why learned correspondences can outperform or simplify hand-engineered matching in difficult imagery.

### World Labs Atlas

World Labs introduced Atlas in September 2026 as an omni world model operating over text, images, video and 3D. Its stated scope includes generation, reconstruction, simulation and robot planning. The architecture is described as a multimodal autoregressive diffusion transformer with a shared spatial context.

Primary source:

- https://www.worldlabs.ai/blog/atlas

Atlas is not a pure-vision system, but it is a strong reference for a competing thesis:

> a generative spatial context may be enough to support multiple world functions without exposing a symbolic state.

### Key separations Clover must preserve during research

#### Geometry is not yet semantics

Accurate camera pose and point maps do not automatically supply object identity or type.

#### Reconstruction is not yet permanence

Reconstructing what was observed is different from representing what is currently unobserved but believed to persist.

#### Novel-view consistency is not yet causality

A coherent renderer may still lack intervention-sensitive dynamics.

#### 3D is not automatically the only useful space

Robots may need metric geometry, topological place structure, object-relative relations and task abstractions simultaneously.

### Open questions

1. Which world queries become trivial once strong geometry is available?
2. Does a 3D reconstruction remain stable under moving/deformable objects?
3. What is the minimum persistent spatial state required beyond a learned geometry encoder?
4. How should active camera motion update uncertainty and visibility?
5. Can explicit geometry reduce planning sample complexity compared with latent-only policies?

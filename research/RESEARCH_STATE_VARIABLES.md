# Stage 1 — World-State Variables & Observability Map

Last updated: 2026-10-14  
Freshness cutoff checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This file is a Stage-1 research inventory, not a Clover architecture specification.

Its purpose is to make the phrase **“understand the real world”** less vague by asking a more concrete question:

> Which world variables matter, and what evidence is currently known to constrain them?

The map deliberately separates what may be inferred from a static RGB image, passive temporal video, active visual exploration, physical action-response, and non-visual sensing.

It does **not** claim that the labels below are mathematical impossibility theorems. They are a working evidence map grounded in current literature and should be revised as stronger results appear.

---

## 1. Evidence routes

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

## 2. High-level observability map

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

## 3. Mass, density and scale

### 3.1 Single-image mass estimation is explicitly ill-posed

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

### 3.2 Real-object mass benchmark

**PhysQuantAgent / VisPhysQuant**  
Primary paper: https://arxiv.org/abs/2603.16958  
Evidence: `PRIMARY_PAPER`

VisPhysQuant contains multi-view RGB-D video with measured object masses. The method uses visual prompting, scale reasoning and inferred internal cross-sections to improve mass estimation.

Important Clover caveat:

RGB-D is outside strict `V0/V1` RGB-only observation. Use the benchmark as evidence about physical-quantity reasoning, but do not silently report it as a pure RGB result.

Stage-2 question:

> How much of mass estimation performance comes from geometry, material/world priors, metric scale, or memorized object-category statistics?

---

## 4. Friction is a strong example of interaction-limited knowledge

### 4.1 Visual + haptic friction mapping

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

### 4.2 Material-pair friction requires interaction structure

**Generalizable Friction Coefficient Estimation via Material Embedding and Proxy Interaction Modeling**  
Primary paper: https://arxiv.org/abs/2604.24188  
Evidence: `PRIMARY_PAPER`

The method predicts pairwise friction through measured interactions against a small fixed proxy-material set, rather than inferring friction directly from RGB appearance.

Stage-1 implication:

Friction is not merely an intrinsic property of one visible object. It is often a **pairwise interaction property** depending on two materials and contact conditions.

### 4.3 Behavior-grounded terrain/contact calibration

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

## 5. Articulation, function and physically usable object models

### 5.1 Active interaction can reveal unknown articulated structure

**DexSim2Real²**  
Primary paper: https://arxiv.org/abs/2409.08750  
Evidence: `PRIMARY_PAPER`

The system constructs an explicit digital twin of unseen articulated objects using the world state before and after an active one-step interaction.

This is valuable Stage-1 evidence that articulation may be partially observable from appearance, but precise manipulation benefits from **interaction that reveals kinematic structure**.

### 5.2 Physical function goes beyond visual asset quality

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

## 6. One state representation may need to span rigid, articulated and deformable objects

### PointCast

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

## 7. Deformation, cloth, rope and soft systems

### 7.1 Cloth world models

**Learning to Unfold Cloth: Scaling up World Models to Deformable Object Manipulation**  
Primary paper: https://arxiv.org/abs/2602.16675  
Evidence: `PRIMARY_PAPER`

The work modifies a Dreamer-style world model for cloth manipulation, including surface-normal input and changes to replay/data augmentation, and evaluates zero-shot physical-robot transfer.

Important protocol note:

Surface normals are stronger geometric evidence than raw monocular RGB and should be annotated accordingly when comparing to strict vision-only systems.

### 7.2 Contact-centric deformable dynamics

**WorldContact**  
Primary paper: https://arxiv.org/abs/2609.19600  
Evidence: `PRIMARY_PAPER`

WorldContact makes contact structure central for deformable manipulation and uses model-generated trajectories to expand policy data.

Stage-1 question:

> Does a general world model need an explicit contact representation, or can contact emerge reliably inside a distributed predictive state?

### 7.3 Soft robot embodiment itself is deformable state

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

## 8. Liquids and hidden physical properties

### Vision-Language Model-based Physical Reasoning for Robot Liquid Perception

Primary paper: https://arxiv.org/abs/2404.06904  
Evidence: `PRIMARY_PAPER`

The study evaluates common household liquids and reports that vision-only reasoning is substantially weaker than a setup where force/torque responses are converted into visual plots and jointly reasoned over.

The system estimates viscosity by using **interaction-derived non-visual evidence encoded visually**, so it must not be classified as proof that viscosity is recoverable from passive RGB.

Stage-1 implication:

For visually similar liquids, interaction response may be more informative than appearance.

Stage-2 question:

> Which fluid variables can be estimated from passive flow video, and which require known perturbations, metric calibration or force evidence?

---

## 9. Ego-motion and object-motion must be disentangled

### 4DVGGT-D

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

### DP-DeGauss

Primary paper: https://arxiv.org/abs/2604.07986  
Evidence: `PRIMARY_PAPER`

Egocentric 4D reconstruction explicitly decomposes background, hands and manipulated objects, showing that first-person scenes require component-aware motion separation under strong occlusion and camera movement.

---

## 10. Object permanence can be trained explicitly, not only measured

### WROP — Training Object Permanence in World Models

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

## 11. Active calibration can define the action/world interface

### SyncWorld

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

## 12. Robot-factored visual interfaces are another route to cross-embodiment transfer

### Robot-Factored World Models via Robot Rendering

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

## 13. 3D point-flow world models make a different claim about transferable physical state

### PointWorld

Primary paper: https://arxiv.org/abs/2601.03782  
Project: https://point-world.github.io/  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

PointWorld represents both action and predicted scene change as 3D point flow and reports one pretrained model across rigid pushing, deformable/articulated manipulation and tool use.

Important protocol caveat:

PointWorld takes RGB-D inputs, so it is not a strict `V0/V1` monocular RGB baseline.

Research value:

It is a strong comparator for the hypothesis that **shared 3D geometric action/state coordinates** can improve cross-embodiment world modeling.

---

## 14. Uncertainty must be decision-aware

### Decision-Aware Uncertainty Evaluation for Early Action Anticipation

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

## 15. Affordance is a distinct state variable from category and geometry

### RoboAfford++ / RoboAfford-Eval

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

## 16. A stronger working decomposition of “world state”

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

## 17. Key Stage-1 distinctions strengthened by this map

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

## 18. Priority Stage-2 reports implied by this map

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

## 19. Open collection gaps

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
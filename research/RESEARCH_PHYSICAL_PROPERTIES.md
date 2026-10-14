# Stage 1 — Hidden Physical Properties, Contact and Irreversible Change

Last updated: 2026-10-14  
Freshness cutoff checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research inventory. It does **not** propose a Clover architecture.

Its purpose is to deepen one part of [`RESEARCH_STATE_VARIABLES.md`](RESEARCH_STATE_VARIABLES.md): the real world contains important state that is only weakly visible, becomes informative only through temporal change or intervention, or changes irreversibly under contact.

The central questions are:

```text
Which physical properties are directly visible?
Which are only statistically predictable from appearance?
Which require observing dynamics?
Which become identifiable only through controlled interaction?
Which remain better measured through non-visual sensing?
How should a world model represent irreversible change?
```

Use the evidence-route notation from `RESEARCH_STATE_VARIABLES.md`:

```text
P0  static RGB
P1  passive temporal RGB/video
P2  active viewpoint changes while sensory evidence remains visual
P3  physical action-response observed visually
N   non-visual / privileged sensing or measured ground truth
```

---

## 1. Physical-property map

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

## 2. Inertial properties: mass, center of mass and inertia

### 2.1 Mass can be predicted visually without being visually identifiable

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

### 2.2 Physical-quantity benchmarks frequently rely on stronger sensing

**PhysQuantAgent / VisPhysQuant**  
Primary paper: https://arxiv.org/abs/2603.16958  
Evidence: `PRIMARY_PAPER`

VisPhysQuant provides multi-view RGB-D observations with measured object masses. It is useful for physical-quantity reasoning, but RGB-D is not a strict `V0/V1` observation protocol.

### 2.3 Inertial parameters are a long-standing interaction problem

**Estimation and Exploitation of Objects' Inertial Parameters in Robotic Grasping and Manipulation: A Survey**  
Primary paper: https://arxiv.org/abs/1911.04397  
Evidence: `BACKGROUND_REFERENCE`

The survey organizes inertial-parameter estimation by interaction level: purely visual, exploratory interaction and fixed-object identification. This remains useful background because it makes center of mass and inertia explicitly different from simple appearance recognition.

### Stage-1 gap

As of the current scan, we do **not** have a convincing modern general result showing that arbitrary real-object center of mass or moment of inertia is reliably identifiable from passive RGB alone.

Keep this as an explicit open problem rather than filling it with a category prior.

Stage-2 questions:

```text
How much inertial prediction comes from object-category memory?
Which controlled pushes/lifts/rotations most efficiently identify inertial parameters visually?
Should a robot maintain a probability distribution over inertial parameters until interaction reduces uncertainty?
```

---

## 3. Friction is an interaction property, not just an appearance label

### 3.1 Visual + haptic friction mapping

**Probabilistic Surface Friction Estimation Based on Visual and Haptic Measurements**  
Primary paper: https://arxiv.org/abs/2010.08277  
Evidence: `PRIMARY_PAPER`

The work explicitly argues that vision alone does not provide enough information for reliable friction estimation and combines visual correlation with limited haptic exploration.

### 3.2 Pairwise material interaction matters

**Generalizable Friction Coefficient Estimation via Material Embedding and Proxy Interaction Modeling**  
Primary paper: https://arxiv.org/abs/2604.24188  
Evidence: `PRIMARY_PAPER`

The method models friction through interactions between material pairs and measured proxy-material contacts instead of treating friction as a simple single-object image attribute.

### 3.3 Behavior-grounded friction/contact in a world model

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

## 4. Stiffness, compliance and tactile-grounded physical state

### 4.1 ViTacPhys

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

### 4.2 Tactile world models

**DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation**  
Primary paper: https://arxiv.org/abs/2609.20649  
Evidence: `PRIMARY_PAPER`

DexTouch-WM combines a pretrained video expert with tactile features and action conditioning, and scales human interaction data to improve robot-domain visual, geometric and contact prediction.

### 4.3 Tactile-grounded world-action policy

**TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation**  
Primary paper: https://arxiv.org/abs/2609.19613  
Evidence: `PRIMARY_PAPER`

TacSushi explicitly uses fingertip tactile features and predicts future visual/tactile/contact-related quantities during training.

Stage-1 implication:

Tactile-world-model results are useful **counterexamples** when defining a vision-only research goal: they reveal which difficult variables current researchers choose to measure through touch rather than infer from RGB.

---

## 5. Temperature is a clean example of a hidden state outside visible RGB

### HEARTH

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

## 6. Liquids and viscosity

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

## 7. Granular materials have hidden preparation state

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

## 8. Deformable objects and contact-rich state

### PointCast

Primary paper: https://arxiv.org/abs/2609.28393  
Project: https://pointcast-wm.github.io  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

PointCast uses persistent identity-bearing 3D point sets to model rigid objects, cloth, rope and articulated cabinets with one general representation family.

### WorldContact

Primary paper: https://arxiv.org/abs/2609.19600  
Evidence: `PRIMARY_PAPER`

WorldContact makes contact-centric state central for deformable manipulation.

### Learning to Unfold Cloth

Primary paper: https://arxiv.org/abs/2602.16675  
Evidence: `PRIMARY_PAPER`

Adapts a world-model approach to cloth manipulation and reports real-robot transfer, but uses surface normals in addition to ordinary RGB.

### ManiSoft

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

## 9. Irreversible topology change: cutting, splitting, tearing and breakage

Rigid-object tracking typically assumes that identity and topology survive action. Real manipulation violates that assumption.

### 9.1 DoughNet

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

### 9.2 CulinaryCut-VLAP

**CulinaryCut-VLAP: A Vision-Language-Action-Physics Framework for Food Cutting via a Force-Aware Material Point Method**  
Primary paper: https://arxiv.org/abs/2601.06451  
Evidence: `PRIMARY_PAPER`

The framework couples robotic manipulation with a Material Point Method simulator for deformable food cutting, where cuts produce large deformation, contact forces and topology changes. Its dataset includes multi-view visual observations plus force-torque/tool-pose labels.

Protocol warning:

This is not a pure vision-only learning setup; privileged physical simulation and force/tool-state labels are part of the training/evaluation infrastructure.

### 9.3 Sashimi-Bot

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

## 10. Counterfactual and intervention datasets are becoming much more explicit

### 10.1 What-If World

**What-If World: A Causal Benchmark for General World Models in Embodied Scenarios**  
Primary paper: https://arxiv.org/abs/2605.27589  
Evidence: `PRIMARY_PAPER`

The benchmark builds paired prompts from real nuScenes and DROID frames while varying one physical detail and evaluates whether generated futures change in the physically correct way.

This directly attacks a failure mode where two individually plausible videos do not respond correctly to an intervention.

### 10.2 CRONOS

**CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models**  
Primary paper: https://arxiv.org/abs/2605.23699  
Evidence: `PRIMARY_PAPER`

CRONOS systematically intervenes on viewpoint, scene, object category and appearance while holding the physical event type fixed.

It is useful for testing whether physical prediction is invariant to nuisance visual changes.

### 10.3 CausalPhys

**Causal Scaffolding for Physical Reasoning: A Benchmark for Causally-Informed Physical World Understanding in VLMs**  
Primary paper: https://arxiv.org/abs/2606.05966  
Evidence: `PRIMARY_PAPER`

CausalPhys contains image/video questions across perception, anticipation, intervention and goal-oriented reasoning together with expert-annotated causal graphs.

### 10.4 CG-World

**CG-World: A Large-Scale World-State Dataset and Protocol for World Models**  
Primary paper: https://arxiv.org/abs/2607.26452  
Evidence: `PRIMARY_PAPER`

CG-World explicitly records latent world state, geometry, skeletal/controller state, physics caches, contact events, render passes and branch metadata. Its branch structure includes observation, action and mechanism interventions plus counterfactual branches.

Critical protocol note:

CG-World is highly structured synthetic/CG supervision. It is valuable because it gives precise ground truth that real video usually lacks, but it is not evidence that such state is available from real RGB input.

### 10.5 Dream2Fix / counterfactual failure synthesis

**Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis**  
Primary paper: https://arxiv.org/abs/2603.13528  
Evidence: `PRIMARY_PAPER`

Dream2Fix perturbs actions inside a generative world model to synthesize paired failure/correction rollouts from successful real demonstrations and filters them for task validity, visual coherence and kinematic safety.

Why it matters:

Counterfactual data can be used not only for abstract causal QA but for **recovery behavior**.

---

## 11. Intervention-sensitive evaluation should become standard

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

## 12. What this means for “vision alone”

The current evidence suggests at least four qualitatively different cases.

### Case A — visually observable or strongly constrained

Examples:

```text
2D appearance
visible geometry
motion/correspondence
some articulation state
```

### Case B — visually predictable but prior-dependent

Examples:

```text
mass from category/material/shape
material semantics
affordance from familiar object appearance
some hidden geometry
```

### Case C — interaction reveals much stronger evidence

Examples:

```text
friction
stiffness/compliance
center of mass / inertia
action controllability
contact response
unknown articulation mechanism
```

### Case D — current strong systems commonly use non-visual sensing

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

## 13. Priority Stage-2 report queue from this file

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

## 14. Open gaps that Stage 1 should continue searching

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

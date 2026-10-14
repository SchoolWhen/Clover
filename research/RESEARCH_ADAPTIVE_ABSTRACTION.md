# Stage 1 — Adaptive Abstraction, State Granularity and Multi-Timescale Structure

Last updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study whether a robotic world representation should use one fixed state granularity, or adapt what it preserves according to task, timescale, uncertainty, embodiment and interaction phase.

---

## 1. Core problem

The physical world contains far more state than any robot can represent at maximum detail all the time.

A useful abstraction must therefore answer:

```text
What can be safely compressed?
What must remain explicit?
What should be coarse now but refined later?
Which distinctions matter only for the current task?
Which distinctions must survive because future tasks are unknown?
```

The central tension is:

```text
compression / efficiency
vs
preserving future-relevant distinctions.
```

---

## 2. Task-specific abstraction is not automatically universal understanding

### Causal Bisimulation Modeling

**Building Minimal and Reusable Causal State Abstractions for Reinforcement Learning**  
AAAI 2024: https://ojs.aaai.org/index.php/AAAI/article/view/29507  
Evidence: `PRIMARY_PAPER`

CBM learns causal dependencies in dynamics/rewards and derives minimal task-specific abstractions that keep variables needed for each task.

Why it matters:

It demonstrates a legitimate use of selective state:

```text
full environment state
→ task-conditioned subset
```

But it also exposes a Clover risk:

```text
minimal for current task
≠
sufficient for future unknown task.
```

---

## 3. State abstraction needs preservation guarantees

### Compositional Behavioral Semantics

**Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning**  
PMLR: https://proceedings.mlr.press/v306/zhang26dy.html  
ArXiv: https://arxiv.org/abs/2606.25357  
Evidence: `PRIMARY_PAPER`

This ICML 2026 work studies what behavioral structures are provably preserved when a concrete system is mapped into an abstraction.

Relevant preserved structures include:

```text
values
invariants
bisimulation-like relations
behavioral metrics
```

Stage-1 implication:

A representation should not be called “good abstraction” only because it is small or visually invariant. We need to specify **what property is promised to survive the abstraction**.

---

## 4. Multi-timescale state is a serious alternative to one-resolution state

### Temporally hierarchical active-inference world model

**Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model**  
Primary paper: https://arxiv.org/abs/2512.01924  
Evidence: `PRIMARY_PAPER`

The system models dynamics at slow and fast timescales and compresses action sequences into abstract actions. Its abstract world model predicts slower future states for tractable action selection.

Research question:

```text
Should fast contact/motion state
and slow task/world state
live at different temporal resolutions?
```

### S2-HWM

**S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation**  
Primary paper: https://arxiv.org/abs/2608.13103  
Evidence: `PRIMARY_PAPER`

S2-HWM learns sparse event evidence and separates event-level manager updates from primitive-step control. Event transitions have variable duration rather than a fixed clock rate.

Why it matters:

```text
physical time step
≠
meaningful world-state update event.
```

Some state should be updated continuously; other state may only need revision when a contact, subgoal, topology change or semantic event occurs.

---

## 5. Hierarchical world state can mix symbolic and perceptual levels

### H-WM

**H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model**  
Primary paper: https://arxiv.org/abs/2602.11291  
Evidence: `PRIMARY_PAPER`

H-WM jointly predicts high-level logical state transitions and low-level visual state transitions.

This provides a useful counter-hypothesis to a single homogeneous latent state:

```text
logical / relational state
+
visual / geometric state
```

may be maintained at different abstraction levels.

What it does **not** establish:

- that symbolic state is necessary for general robotics;
- that the chosen predicates are open-world sufficient;
- that one fixed hierarchy transfers to arbitrary tasks.

---

## 6. Hierarchical memory can be organized by operating timescale

### HiMe

**HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control**  
PMLR: https://proceedings.mlr.press/v306/ji26k.html  
Evidence: `PRIMARY_PAPER`

HiMe separates a high-frequency executor, a working-memory sentry and a long-term planner, and supports Add/Update/Delete memory operations.

Stage-1 relevance:

It suggests that **state access frequency** may itself be an abstraction variable:

```text
high-frequency motor-relevant state
working state
long-horizon episodic/semantic state
```

This is related to, but distinct from, representational granularity.

---

## 7. Structured equivariance can preserve detail without storing it naively

### Flow Equivariant World Models

**Flow Equivariant World Models: Structured Memory for Dynamic Environments**  
PMLR: https://proceedings.mlr.press/v306/lillemark26a.html  
Project: https://flowequivariantworldmodels.github.io/  
Evidence: `PRIMARY_PAPER`

This work builds latent memory that transforms equivariantly with self-motion and inferred object motion, so out-of-view information remains aligned as the observer/world moves.

Why it matters:

Adaptive abstraction is not only about deleting information. Another strategy is to encode known transformation structure so the same information can be maintained more efficiently and consistently.

---

## 8. Task semantics may determine which relations deserve explicit representation

### Semantically Rich World Models

**Beyond Instance Slots: Semantically Rich World Models for Physical Interaction Planning**  
Official project/publication page: https://www.max-robotics.com/en/research/publications/cmu42t6js00r9pd42avv37dcb  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

The method structures planning state around functional roles such as gripper, target, goal, relation and phase rather than only generic object identity.

Stage-1 implication:

```text
entity identity
alone may be too fine in one way
and too weak in another.
```

The abstraction required for planning may be role- and task-conditioned.

---

## 9. Hierarchy can also operate over subgoals

### ViGAR

**Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation**  
Primary paper: https://arxiv.org/abs/2610.02368  
Evidence: `PRIMARY_PAPER`

ViGAR separates a visual subgoal planner from a subgoal executor, using a shared pretrained world-model representation.

This is not necessarily a world-state hierarchy, but it matters because state granularity and action horizon are coupled:

```text
primitive action horizon
subtask horizon
full-task horizon
```

may require different state summaries.

---

## 10. Non-stationarity means a previously sufficient abstraction can become wrong

A world representation may be sufficient under one dynamics regime and fail after the robot, controller, environment or task distribution changes.

### ReDRAW

**Adapting World Models with Latent-State Dynamics Residuals**  
PMLR/L4DC 2026: https://proceedings.mlr.press/v331/lanier26a.html  
Evidence: `PRIMARY_PAPER`

ReDRAW pretrains a latent world model in simulation and adapts it to changed target dynamics by learning residual corrections in latent-state dynamics. It evaluates both vision-based control domains and a physical visual lane-following task.

Stage-1 relevance:

```text
same representation
+
changed transition law
```

can require adaptation even when observations remain visually similar.

### ROAM

**Adapt On-the-Go: Behavior Modulation for Single-Life Robot Deployment**  
PMLR/CoLLAs 2026: https://proceedings.mlr.press/v330/chen26a.html  
Evidence: `PRIMARY_PAPER`

ROAM adapts within one deployment episode to novel situations and changed dynamics using a repertoire of learned behaviors, including a real quadruped dynamics-shift demonstration.

This is useful evidence that open-world robotics requires **online recognition of regime mismatch**, not only offline robustness.

### WorMI

**World Model Implanting for Test-time Adaptation of Embodied Agents**  
PMLR/ICML 2025: https://proceedings.mlr.press/v267/yoo25a.html  
Evidence: `PRIMARY_PAPER`

WorMI retrieves and composes domain-specific world models at test time for unseen domains.

Research question:

```text
when should one world model be adapted,
when should another model be selected,
and when should the system conclude that no existing model is adequate?
```

---

## 11. Embodiment itself changes the meaning of state and action

### LAC-WM

**Cross-Embodiment Robot Foundation World Models with Latent Actions**  
PMLR/ICML 2026: https://proceedings.mlr.press/v306/huang26bv.html  
ArXiv: https://arxiv.org/abs/2610.10846  
Project: https://lacwm.github.io/  
Evidence: `PRIMARY_PAPER`

LAC-WM learns a unified latent action space across diverse robot embodiments and compares it with explicit action conditioning. The paper reports that explicit action spaces fragment across embodiments while the learned latent action representation transfers better to unseen robots.

Stage-1 implication:

```text
numerical action label
≠
embodiment-independent action meaning.
```

This strengthens the need to treat **self/embodiment state** as part of the world-model interface rather than a fixed external assumption.

### OSCAR

**OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics**  
Primary paper: https://arxiv.org/abs/2606.04463  
Evidence: `PRIMARY_PAPER`

OSCAR uses a 2D kinematic skeleton rendering as a common conditioning representation across robot arms and human hands. This is another candidate answer to cross-embodiment action semantics.

Neither result proves a universal embodiment representation; together they show that action/world abstraction depends strongly on how the robot body is represented.

---

## 12. Adaptive abstraction taxonomy

Stage 1 should distinguish at least:

### G1 — task-conditioned abstraction

Keep only distinctions needed for a specified objective.

### G2 — temporal abstraction

Represent fast and slow dynamics at different rates.

### G3 — event-conditioned abstraction

Refine/update state around semantically meaningful transitions rather than every frame.

### G4 — spatial abstraction

Use global coarse structure plus local high-resolution detail.

### G5 — entity/relation abstraction

Move between dense scene representation, entities, relations and functional roles.

### G6 — uncertainty-conditioned abstraction

Allocate more state/detail where uncertainty or decision sensitivity is high.

### G7 — embodiment-conditioned abstraction

Keep state variables relevant to the current robot/action interface.

### G8 — open-world reserve

Retain enough recoverable evidence so future tasks can reconstruct distinctions that were not important at the moment of compression.

### G9 — regime-conditioned abstraction

Change representation/model assumptions when dynamics, domain or environment regime changes.

This is especially important for Clover's long-term general-purpose goal.

---

## 13. Failure modes of abstraction

### Over-abstraction

```text
states that require different actions become merged
hidden changes are forgotten
a new task needs information that was discarded
```

### Under-abstraction

```text
state becomes unnecessarily large
planning becomes expensive
irrelevant visual variation dominates representation
memory grows without bound
```

### Wrong abstraction boundary

```text
correct object state but wrong task relation
correct visual detail but missing contact mode
correct short-term state but lost long-horizon event history
```

### Static abstraction under non-stationarity

```text
state was sufficient yesterday
but dynamics / embodiment / controller / task distribution changed today.
```

A general-purpose system therefore needs a way to detect when an abstraction/model is no longer adequate.

---

## 14. Representation reversibility is an under-studied requirement

Compression can discard information that later becomes useful.

For a general-purpose robot, Stage 1 should distinguish:

```text
lossy active state
vs
recoverable evidence store / provenance
```

A state may remain compact while preserving links to evidence from which omitted distinctions can later be reconstructed.

This is not a recommendation for any historical Clover replay mechanism; it is a generic research requirement:

> If the future task distribution is unknown, how much information should remain recoverable after abstraction?

This connects memory, provenance, abstraction and open-world optionality.

---

## 15. Candidate later diagnostics

### D-G1 — task-switch stress test

Train/compress for task A and test whether task B exposes irreversibly lost information.

### D-G2 — granularity-cost Pareto curve

Measure:

```text
state size / memory / compute
vs
prediction
control
planning
memory
causal reasoning
```

### D-G3 — local refinement test

Allow a coarse representation to request high-resolution local state only when needed; compare with always-fine and always-coarse baselines.

### D-G4 — timescale ablation

Compare one-rate memory/state against multi-timescale or event-driven state updates.

### D-G5 — unknown-future-task retention

Evaluate whether raw evidence/provenance allows reconstruction of information that the active abstraction omitted.

### D-G6 — regime-shift detection

Change dynamics, camera, controller or embodiment and measure:

```text
mismatch-detection latency
adaptation time
false alarms
catastrophic interference
recovery of calibrated prediction/control
```

### D-G7 — embodiment transfer

Keep task/environment fixed while changing robot morphology/action interface; test whether the state/action abstraction still preserves equivalent physical meaning.

---

## 16. Adjacent gaps discovered

The literature suggests these areas should remain visible during Stage 1:

```text
multi-timescale state
structured/equivariant memory
non-stationarity and test-time adaptation
task-semantic / functional-role state
self / embodiment model
representation reversibility
open-world model inadequacy detection
```

These are not separate Clover commitments. They are candidate dimensions along which future representations should be compared.

---

## 17. Stage-1 questions

```text
Should state granularity be fixed or adaptive?
Which variables require high-frequency update and which only event-level update?
Can task-conditioned abstractions remain reusable for unknown future tasks?
How much raw evidence must be retained to reverse an earlier abstraction decision?
Should uncertainty control representation resolution?
Can structured transformation laws replace brute-force memory?
How should global scene state and local manipulation state interact?
When does hierarchy genuinely improve sufficiency rather than merely add modules?
How should the system detect that its current dynamics/embodiment abstraction is stale?
Should action semantics be represented in robot-specific coordinates or a shared embodiment-invariant space?
When should a model be adapted, replaced, composed with another model, or rejected as inadequate?
```

---

## Current rule

Do not equate minimal state with general understanding.

Do not equate maximal-detail state with better intelligence.

The research target is **appropriate sufficiency at appropriate granularity, with explicit knowledge of what was discarded, whether it can be recovered, and whether the abstraction remains valid when the world or embodiment changes**.

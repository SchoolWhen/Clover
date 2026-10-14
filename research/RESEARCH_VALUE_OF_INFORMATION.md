# Stage 1 — Value of Information, Probing Actions and Active Evidence Acquisition

Last updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a core consequence of partial observability:

> When the current visual evidence is insufficient, what observation or action should the agent choose next in order to reduce uncertainty most efficiently?

This connects active perception, information gain, Bayesian experimental design, system identification, probing actions and embodied reasoning.

---

## 1. Core distinction

Most control formulations score actions mainly by task value:

```text
Which action moves me toward the goal?
```

But under uncertainty an action can also have epistemic value:

```text
Which action will teach me what world I am actually in?
```

The same physical action may therefore have two roles:

```text
instrumental action — changes the world to achieve the task
probing action      — changes viewpoint/world to reveal information
```

Some actions do both.

---

## 2. Value of information as belief change

A generic information-seeking objective compares the current belief

```text
p(x | history)
```

with the posterior expected after a candidate observation/action.

One common form is expected information gain:

```text
EIG(a)
= E_o [ KL( p(x | history, a, o) || p(x | history) ) ]
```

The hidden quantity `x` may represent:

```text
latent state
physical parameter
model parameter
causal structure
object identity
map hypothesis
possible task interpretation
```

This makes the target of information gathering explicit.

---

## 3. Active inference: information gain over states, parameters and model structure

### Active inference and artificial reasoning

Peer-reviewed article: https://www.nature.com/articles/s41467-026-77209-5  
Published: 2026-09-08  
Evidence: `PRIMARY_PAPER`

The paper extends expected information gain beyond uncertainty over latent state to include uncertainty over model parameters and model structure. Action/policy selection combines expected value with epistemic gain and is framed as a form of optimal experimental design.

The distinction is highly relevant to Clover:

```text
What is the current state?
What are the physical parameters?
Which causal/model structure is true?
```

are different uncertainty targets and may require different probes.

Important limitation:

The paper's numerical examples operate in discrete partially observed generative models. It does not demonstrate general visual robotics or pixel-level world-model learning.

Stage-1 question:

> Can visual embodied agents explicitly distinguish information gain about current state from information gain about hidden dynamics or causal structure?

---

## 4. Active perception resolves missing physical evidence

### Active Perception for Embodied Disambiguation

Primary paper: https://arxiv.org/abs/2608.13605  
Evidence: `PRIMARY_PAPER`

The work addresses ambiguity caused not only by language but by missing physical evidence: occlusion, restricted viewpoints, unreadable text and unobserved targets. The robot can continue observing, request clarification or finish selection based on accumulated evidence.

Stage-1 relevance:

It operationalizes:

```text
uncertain target
→ choose new observation
→ accumulate evidence
→ decide whether uncertainty is resolved
```

and shows that information acquisition policy can be separated from base representation quality.

---

## 5. Next-best-view is one form of epistemic action

Relevant Stage-1 sources:

- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810
- Classical Active Perception — https://ieeexplore.ieee.org/abstract/document/5968

These methods treat viewpoint selection as a decision variable.

Important distinction:

```text
move camera to see hidden geometry
```

is different from:

```text
push object to reveal friction/mass/dynamics.
```

The first changes observation geometry; the second intervenes on the physical system.

---

## 6. Active system identification: action can identify dynamics

### Sampling-based System Identification with Active Exploration for Legged Sim2Real Learning

CoRL/PMLR: https://proceedings.mlr.press/v305/sobanbabu25a.html  
Evidence: `PRIMARY_PAPER`

This work actively selects exploratory behavior to reduce uncertainty over real robot dynamics for sim-to-real adaptation, rather than relying only on passive logs or broad domain randomization.

Stage-1 relevance:

A probing trajectory can be valuable because it distinguishes competing dynamic hypotheses.

This connects directly to hidden physical properties such as:

```text
friction
actuator response
contact behavior
unknown load
dynamic parameters
```

and supports the broader principle:

```text
some world knowledge is acquired by experiments, not by passive seeing.
```

---

## 7. Behavior-grounded physics is already using this principle

### DR-WM

Primary paper: https://arxiv.org/abs/2610.17630  
Evidence: `PRIMARY_PAPER`

DR-WM obtains scene geometry from RGB but calibrates terrain/contact properties from real action-response evidence before simulating candidate consequences.

Although the probing policy itself is not the central contribution, the method provides a concrete example where action-response turns an underdetermined visual property into a better-constrained physical model.

---

## 8. Information gathering can target state, parameter or structure uncertainty

Stage 1 should distinguish:

### V1 — state information

Example:

```text
Is the cup behind the box or was it removed?
```

Potential probe:

```text
move camera
```

### V2 — parameter information

Example:

```text
How slippery is this surface?
```

Potential probe:

```text
small controlled slide/push
```

### V3 — mechanism information

Example:

```text
Is this drawer prismatic, hinged, latched or stuck?
```

Potential probe:

```text
small directional interaction
```

### V4 — causal-structure information

Example:

```text
Does this switch control this device?
```

Potential probe:

```text
intervention on switch
```

### V5 — task-interpretation information

Example:

```text
Which of two visually similar objects did the user mean?
```

Potential probe:

```text
new view / read label / ask user
```

---

## 9. Information gain is not automatically task value

A highly informative action can be expensive, risky or destructive.

A practical objective may need to trade:

```text
information gain
expected task reward
energy/time
risk
irreversibility
safety
opportunity cost
```

This is especially important in real robotics because some experiments cannot be undone.

Examples:

```text
push gently to estimate friction          — low cost
cut object to learn internal material     — irreversible
lift unknown heavy object                 — possible safety risk
open sealed package                       — changes world state
```

Stage 1 should therefore preserve the distinction:

```text
most informative action
≠
best action to execute.
```

---

## 10. Probing actions can change the thing being measured

This creates a subtle causal issue.

Example:

```text
measure deformability by squeezing
```

may itself alter the material state.

Therefore the agent may need to model:

```text
probe action
→ information gained
+
world change caused by the probe
```

This is particularly important for:

```text
soft objects
fragile objects
food
liquids
granular materials
adhesive/contact states
thermal systems
```

The epistemic process is part of the dynamics, not external to it.

---

## 11. A useful research loop

Without committing to a Clover mechanism, the literature supports studying this generic loop:

```text
current belief / hypotheses
        ↓
what uncertainty matters for the task?
        ↓
which candidate view/action would discriminate hypotheses?
        ↓
execute safe probe
        ↓
new visual evidence
        ↓
update belief / parameters / model structure
        ↓
stop when additional information is not worth its cost
```

This connects:

```text
active perception
system identification
causal intervention
uncertainty calibration
belief revision
planning
```

---

## 12. Candidate later diagnostics

### D-V1 — ambiguity-trigger test

Does the system seek evidence only when current belief is genuinely insufficient?

Measure unnecessary probes and failures to probe.

### D-V2 — expected-vs-realized information gain

Before action, estimate expected uncertainty reduction. After observation, measure realized reduction.

### D-V3 — cheapest discriminating action

Among actions that resolve the ambiguity, measure whether the system selects the lowest-cost / lowest-risk one.

### D-V4 — parameter identification efficiency

How many interactions are needed to reach a calibrated posterior over mass/friction/stiffness/dynamics?

### D-V5 — model-structure discrimination

Provide several causal/mechanism hypotheses that make identical passive predictions but diverge after intervention.

### D-V6 — stop-rule calibration

Does the system know when it has enough information to act rather than continuing to gather evidence indefinitely?

---

## 13. Adjacent gaps discovered

Value-of-information research reveals several additional Stage-1 areas:

```text
epistemic action safety
irreversible experimentation
experiment design under limited budgets
model-structure uncertainty
meta-reasoning over whether to think/look/ask/act
open-world hypothesis generation
```

The last item is especially important: classical Bayesian experimental design usually assumes a hypothesis/model class already exists. A general robot may first need to realize that **none of its current hypotheses explain the observation**.

That becomes an open-world discovery problem, not just uncertainty reduction inside a fixed model family.

---

## 14. Stage-1 questions

```text
What uncertainty is worth reducing before action?
Should the agent seek information about state, parameters or model structure?
How should information value be traded against time, energy, risk and irreversible change?
Which probes are valid under a strict vision-sensing goal?
How can expected information gain be estimated when the world model itself is wrong?
How should the agent detect that the current hypothesis set is incomplete?
When should it look, move, touch through action-response, ask, or simply remain uncertain?
```

---

## Current rule

Do not treat active perception as a camera-planning add-on.

Do not treat exploration as random data collection.

For Stage 1, the important concept is:

```text
an intelligent action can be valuable because of the evidence it is expected to produce.
```

This may be central to learning aspects of the real world that passive RGB cannot uniquely determine.

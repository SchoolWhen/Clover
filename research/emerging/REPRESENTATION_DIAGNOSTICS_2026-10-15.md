# Stage-1 Emerging Audit — Representation Diagnostics and Causal Use

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This is supporting methodology for Stage 1 / Stage 2. It does not define a Clover representation.

## Core problem

A representation may contain information that a downstream probe can decode even when the deployed policy does not actually use that information.

Keep three claims separate:

```text
information is decodable from latent state
≠
information is causally used by the model
≠
changing that information produces the expected closed-loop behavior
```

This distinction matters directly for claims such as:

```text
"the model represents mass"
"the model understands direction"
"the world model encodes object permanence"
"the policy uses causal state"
```

A linear probe alone cannot establish these stronger claims.

---

# 1. Current embodied mechanistic-interpretability evidence

## Do Vision-Language-Action Models Understand Instructions?

Paper: https://arxiv.org/abs/2610.10178  
Evidence: `PRIMARY_PAPER`

The paper studies `π0.5` and `GR00T N1.7` using activation patching and attribution patching under controlled instruction corruptions.

Important reported observations:

- directional language can produce large causal effects on action generation;
- the loci of causal sensitivity differ across the two model families;
- for GR00T N1.7, large causal effects can occur while representational geometry changes relatively little;
- attribution patching tracks activation patching differently across the two models.

Stage-1 lesson:

```text
representation similarity
≠
causal functional role
```

and interpretability methods themselves require validation per architecture.

---

## Mechanistic interpretability for steering VLAs

Paper: https://arxiv.org/abs/2509.00328  
Evidence: `PRIMARY_PAPER`

This work identifies internal semantic directions linked to action behavior and demonstrates activation steering on open-source VLA models in simulation and on a physical robot.

Research role:

```text
observe latent feature
→ intervene on latent feature
→ measure action change
```

is stronger evidence than probe accuracy alone.

But successful steering still does not prove that the steered concept is a complete or correctly grounded world variable.

---

# 2. Required representation-evidence ladder

For future Clover/Stage-2 claims, record the strongest evidence available.

```text
RD0 correlation / visualization
RD1 linear probe recoverability
RD2 nonlinear probe / controlled prediction
RD3 causal activation patch / ablation / mediation
RD4 targeted steering changes action in expected direction
RD5 closed-loop intervention changes physical outcome as predicted
RD6 OOD / counterfactual replication of the causal effect
```

Do not promote an `RD1` result into an `RD5` claim.

Example:

```text
mass can be linearly predicted from Z_t
```

only establishes decodability under the probe/data assumptions. It does not establish that the robot policy uses mass, that mass is identifiable from evidence, or that manipulating the mass coordinate changes action appropriately.

---

# 3. Probe controls that should be mandatory

When probing a latent variable, control for:

```text
probe capacity
sample size
class/category leakage
language-label leakage
viewpoint / camera identity
object identity shortcut
time-index shortcut
action-label shortcut
train/test environment overlap
frozen vs post-trained representation
```

Prefer counterfactual/minimal-pair datasets where the target physical variable changes while appearance/semantics are controlled as much as possible.

---

# 4. Representation quality should be multidimensional

For a candidate world state `Z_t`, evaluate separately:

```text
Decodable?          can a probe recover the variable?
Identifiable?       was enough evidence available to infer it?
Causally used?      does the model actually rely on it?
Intervenable?       can controlled latent change alter behavior predictably?
Persistent?         does it survive occlusion/time?
Revisable?          can contradictory evidence update it?
Action-sufficient?  does it support control/planning?
Open-world robust?  does the effect survive new objects/scenes/regimes?
```

This prevents `representation quality` from collapsing into one probe score.

---

# 5. Relation to JEPA / WAM / Foundation-model audits

This methodology is especially important for recent latent world models such as:

```text
V-JEPA / RoboJEPA
SpecWM
Identifiable World Models
ReWAM
LeWAM variants
LAC-WM
DELE-style future latents
```

Questions to ask:

```text
Does scaling reduce prediction loss while leaving critical state variables absent?
Does a frozen visual encoder create a hard information ceiling?
Are action-relevant variables merely decodable or causally used?
Does post-training re-route which layers/features actually control action?
Does quantization/token pruning preserve probe accuracy but alter causal use?
```

---

# 6. Current rule

Stage 2 must not equate:

```text
probe success
with
understanding.
```

For high-value world-state claims, aim to progress from:

```text
recoverability
→ causal attribution
→ intervention
→ closed-loop behavioral evidence
→ OOD/counterfactual validation.
```

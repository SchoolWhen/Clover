# R-E — Physical Understanding: Plausibility, Quantification and Relational Structure

Last updated: 2026-10-14  
Status: **BACKGROUND_RESEARCH**

## 1. Fundamental question

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

## 2. Intuitive physics

### IntPhys 2

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

## 3. Shortcut-resistant physical reasoning

### Minimal Video Pairs / MVPBench

- Paper: https://arxiv.org/abs/2506.09987
- Code/data reference: https://github.com/facebookresearch/minimal_video_pairs
- Meta physical-reasoning overview: https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/

MVP-style evaluation pairs videos that differ minimally but require opposite answers.

**Research value:** minimal pairs reduce the ability to solve a benchmark using background, language or coarse appearance shortcuts.

**Clover implication:** future physical-understanding claims should include paired intervention/perturbation controls, not only aggregate benchmark accuracy.

## 4. Quantitative physical reasoning

### QuantiPhy

- Paper: https://arxiv.org/abs/2512.19526

QuantiPhy evaluates numerical estimation of physical properties such as size, velocity and acceleration from video.

**Demonstrates:** qualitative verbal plausibility can remain strong while numerical physical estimates are poor; models may rely heavily on pretrained world knowledge rather than the actual provided evidence.

**Clover implication:** physical understanding should include machine-checkable quantities, not only natural-language explanations.

## 5. Relational physics without calibration dependence

### Principia

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

## 6. Physical variables can emerge in distributed representations

### Interpreting Physics in Video World Models

- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Paper: https://arxiv.org/abs/2602.07050

The study finds layerwise emergence of speed, acceleration and motion direction, with direction encoded as a high-dimensional population code.

**Implication:** a model can carry useful physical information without exposing a compact symbolic physics state.

Therefore:

```text
physical understanding
≠ automatically explicit physics variables
```

## 7. Physics as prediction is still not physics as execution

### RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

RoboPhys-3D evaluates world-model rollouts at multiple levels including pixel fidelity, 3D geometry consistency, state-level understanding and task-level completeness.

**Key lesson:** visually plausible generated video can still fail state- and execution-grounded metrics.

For Clover:

```text
plausible future video
≠ correct physical state
≠ executable consequence
```

## 8. Visually inferred physical properties must remain hypotheses

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

## 9. Operational research questions

1. Which physical laws are learnable from passive video alone?
2. Which physical variables require interaction to become identifiable?
3. Is relational physics more robust than absolute metric prediction under V0?
4. Does a predictive latent encode enough physics for action without explicit state?
5. How much physical accuracy is hidden by visually realistic generation metrics?
6. Can the system distinguish visually plausible but physically impossible rollouts?
7. Do explicit physical variables improve novel-object transfer and recovery?

## 10. Best baseline battery

| Capability | Baseline / benchmark | What it measures |
|---|---|---|
| Intuitive plausibility | IntPhys 2 | permanence, continuity, solidity, immutability |
| Shortcut resistance | MVPBench | minimal visual changes with answer flips |
| Quantitative kinematics | QuantiPhy | numerical size/velocity/acceleration |
| Relational laws | Principia | calibration-independent Newtonian consistency |
| Latent physical representation | V-JEPA 2/2.1 probing | decodability of physical information |
| Execution-grounded state | RoboPhys-3D | world-model state and task consequences |

## 11. Discriminating experiments

### T-E-01 — Qualitative vs quantitative split

Use the same video to ask:

```text
Will it fall?
How fast is it moving?
Which of two objects accelerates more?
What numerical acceleration is supported?
```

This separates language-level plausibility from quantitative grounding.

### T-E-02 — Relational invariance

Vary:

```text
camera scale
frame rate
viewpoint
object appearance
```

while preserving the physical relation.

Measure whether the model preserves the correct relation.

### T-E-03 — Appearance prior conflict

Construct objects whose visual appearance suggests one material/dynamics prior but whose observed motion supports another.

Measure whether the model follows actual visual dynamics or pretrained semantic expectation.

### T-E-04 — Passive vs action-conditioned physics

Compare the same base representation before and after action-conditioned experience.

Measure gains in:

- consequence prediction;
- affordance transfer;
- intervention sensitivity;
- quantitative dynamics.

### T-E-05 — State-grounded rollout

Evaluate generated/predicted futures by downstream reconstructed state and executable consequences, not by video quality alone.

## 12. Kill conditions

A proposed explicit physics mechanism should be removed if it does not outperform strong latent/video baselines on at least one of:

- quantitative prediction;
- relational invariance;
- intervention transfer;
- novel dynamics;
- planning/recovery;
- sample efficiency.

Likewise, a generative model should not be called physically grounded if its advantage exists only on perceptual/video metrics while state/action consequences are wrong.

## 13. Clover landing

Current conclusion:

> **Physical understanding should be treated as a layered empirical target—from plausibility through quantitative and relational constraints to intervention and action—not as a single score or a commitment to explicit physics variables.**

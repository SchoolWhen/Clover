# 02 — Explicit vs Distributed Representation

## Question

Must world understanding be stored in compact explicit variables, or can a high-dimensional distributed representation be the better substrate?

## Why this matters

Old Clover prototypes lean toward explicit machine-native state. Modern representation learning provides a serious counter-hypothesis: useful physical information may be distributed across large feature spaces and only become readable when needed.

## Evidence for distributed representations

DINOv2 shows that self-supervised training at scale can produce generic visual features transferable across many tasks.

V-JEPA 2/2.1 shows that predictive self-supervision can produce strong global and dense video features. V-JEPA 2.1 specifically adds dense predictive loss and deep self-supervision to improve spatially and temporally grounded features.

Meta's mechanistic work on physics in video world models reports that some physical variables become increasingly linearly accessible across network depth while other quantities can be represented by distributed population codes rather than a small set of dedicated units.

## Evidence for explicit outputs

Classical geometry remains compelling when the variable has a well-defined mathematical meaning: camera pose, projection, depth constraints and multi-view consistency are not arbitrary labels.

VGGT is important because it combines a learned network with explicit geometric outputs: camera parameters, depth, point maps and tracks.

## The real comparison

The right question is not `explicit vs neural`.

It is:

> Which information should remain distributed for flexibility, and which information should be materialized as explicit state because downstream reasoning, revision or control needs stable semantics?

A plausible hybrid is:

```text
learned distributed visual representation
        ↓
selective explicit state materialization
        ↓
planning / verification / interaction
```

But this remains a hypothesis.

## Clover implication

Clover should test whether explicit variables add value in:

- long-horizon persistence;
- belief revision;
- causal intervention;
- efficient planning;
- failure diagnosis;
- cross-task reuse.

If explicit state does not improve these, explicitness alone is not a contribution.

## Primary sources

- DINOv2: https://arxiv.org/abs/2304.07193
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- V-JEPA 2/2.1 code: https://github.com/facebookresearch/vjepa2
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- Slot Attention: https://arxiv.org/abs/2006.15055
- Meta — Interpreting Physics in Video World Models: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

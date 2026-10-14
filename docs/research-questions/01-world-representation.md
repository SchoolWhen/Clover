# 01 — What Is a World Representation?

## Question

What internal state must a machine maintain so that visual observations become a usable model of a persistent world rather than a stream of unrelated frames?

## Major prior answers

### Explicit geometric state

Classical SfM/SLAM represents cameras, landmarks and geometric constraints explicitly. ORB-SLAM3 demonstrates that a system can maintain and merge maps over long time spans and across revisits.

Strength: variables are interpretable and directly usable for localization and geometry.

Limit: geometry alone does not provide object identity, affordance, semantics, causal structure or broad open-world abstraction.

### Learned distributed state

DINOv2 and V-JEPA-style encoders learn feature spaces rather than hand-written geometric state. V-JEPA 2 extends this to video and shows that large-scale self-supervised video learning supports motion understanding, action anticipation and, after action-conditioned post-training, robot planning.

Strength: broad abstraction can emerge without manually defining every variable.

Limit: what constitutes the persistent world state is less explicit, and updating/revising a long-lived world model remains a separate question.

### Learned geometric state

VGGT directly predicts cameras, depth, point maps and 3D tracks with a feed-forward model. VGGT-Ω pushes this direction toward larger-scale, dynamic reconstruction and more transferable geometry-aware representations.

Strength: combines learned priors with explicit geometric outputs.

Limit: accurate reconstruction is not equivalent to physical, causal or task-level understanding.

### Generative/spatial world models

World Labs Atlas and NVIDIA Cosmos 3 represent another answer: train a large model to generate/reconstruct/simulate coherent worlds across modalities. These systems suggest that a world representation may be best judged by what coherent futures or spatial continuations it can generate.

Limit: generation quality can hide state inconsistency; persistent identity, observability and intervention structure require separate measurement.

## Current synthesis

A useful world representation likely needs to support at least four functions:

1. **state** — what currently exists and where;
2. **persistence** — what remains true when not currently visible;
3. **transition** — how the world can change;
4. **query/action interface** — what downstream decisions can reliably read.

No current route establishes that one representation family is sufficient for all four.

## Clover implication

Clover should not choose `field`, `object graph`, `3D map`, or `latent` by preference. The next representation hypothesis should be selected by whether it jointly supports persistence, revision, dynamics, queryability and action utility.

## Primary sources

- ORB-SLAM3 paper: https://arxiv.org/abs/2007.11898
- ORB-SLAM3 code: https://github.com/UZ-SLAMLab/ORB_SLAM3
- DINOv2 paper: https://arxiv.org/abs/2304.07193
- V-JEPA 2 paper: https://arxiv.org/abs/2506.09985
- V-JEPA 2 official code: https://github.com/facebookresearch/vjepa2
- VGGT paper: https://arxiv.org/abs/2503.11651
- VGGT code: https://github.com/facebookresearch/vggt
- VGGT-Ω paper: https://arxiv.org/abs/2605.15195
- VGGT-Ω code: https://github.com/facebookresearch/vggt-omega
- World Labs Atlas: https://www.worldlabs.ai/blog/atlas
- Cosmos 3 paper: https://arxiv.org/abs/2606.02800

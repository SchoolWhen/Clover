# Video Representation and World Models

## What problem does this area solve?

Learn temporal representations that support prediction, physical understanding and planning from large-scale video.

## Typical representation

Often a learned latent representation with temporal prediction or self-supervised objectives rather than an explicit symbolic world state.

## Representative work

### V-JEPA 2 / 2.1

- Publication: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- Code/models: https://github.com/facebookresearch/vjepa2

V-JEPA 2 is especially relevant because it connects action-free video self-supervision to physical understanding and action-conditioned planning.

### Mechanistic interpretation

Meta's 2026 work on interpreting physics in video world models is tracked because it challenges a strong Clover assumption: useful physical variables may be represented in distributed, high-dimensional population codes rather than a compact explicit state.

Source: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

## Open questions for Clover

- What does prediction learn that reconstruction does not?
- Are physical variables explicit, linearly readable, or deeply distributed?
- Does a latent representation support persistent world revision and intervention as well as an explicit state?
- How much passive video is sufficient before interaction becomes necessary?

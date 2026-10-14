# Object-Centric Representation

## What problem does this area solve?

Factor a scene into persistent, reusable entity-like components rather than representing everything as one dense feature tensor.

## Representative work

### Slot Attention

- Paper: https://arxiv.org/abs/2006.15055

The core idea is to aggregate perceptual features into exchangeable slots that can support compositional structure.

### SAM 2

- Code: https://github.com/facebookresearch/sam2

SAM 2 is not itself a world model, but its streaming video segmentation/memory provides a strong practical baseline for visual entity continuity.

## Clover questions

- Should objects be primitive or emergent?
- Do slots preserve identity under long occlusion and interaction?
- Can an object-centric representation express free space, regions, fields and continuous phenomena?
- Is a field-to-entity emergence model more general than object slots, or simply more complex?

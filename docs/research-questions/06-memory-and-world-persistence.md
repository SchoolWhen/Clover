# 06 — Memory and World Persistence

## Question

If the visual field changes every moment, what should persist inside the machine, for how long, and in what form?

## Different traditions answer differently

### SLAM

Persistent maps and keyframes preserve geometric information across time and revisits. ORB-SLAM3 is a strong example of reusing older map information and merging maps after tracking loss.

### Video models

Transformers and video encoders maintain temporal context inside a finite computation window. V-JEPA 2.1 targets temporally consistent dense features, but a feature's temporal stability is not yet equivalent to an indefinitely persistent world memory.

### Video segmentation

SAM 2 uses streaming memory for video segmentation, showing a practical architecture for carrying object-mask information through time.

### Robot policies

Long-horizon policies may use context, recurrence or hierarchical subtask structure without exposing a persistent external world state.

## Three memory problems must be separated

1. **perceptual continuity** — keep identity over nearby frames;
2. **world persistence** — retain facts while they are out of view;
3. **lifelong consolidation** — retain useful knowledge across long periods without storing all raw observations.

Treating all three as one `memory module` hides the real research problem.

## Belief revision is the hard test

Memory is not useful if it only accumulates. A world model must support:

```text
old belief
+ new contradictory visual evidence
→ corrected world state
```

The important capability is selective persistence plus revision.

## Clover implication

Future Clover work should measure memory by world-query stability and correction, not by context length alone.

## Primary sources

- ORB-SLAM3: https://arxiv.org/abs/2007.11898
- SAM 2: https://arxiv.org/abs/2408.00714
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- Ego4D dataset: https://ego4d-data.org/
- LIBERO lifelong robot learning benchmark: https://libero-project.github.io/main.html

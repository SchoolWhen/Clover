# R-C — Representation: Explicit, Distributed, Object-Centric or Hybrid?

Last updated: 2026-10-14  
Status: **BACKGROUND_RESEARCH**

## 1. Fundamental question

> **What internal representation is sufficient for stable visual world understanding and action?**

Candidate families include:

```text
explicit geometric/state variables
distributed latent representation
object-centric slots/entities
dense scene representation
continuous fields
generative latent state
hybrid / identifiable representations
```

No family is privileged by the Research Reset.

## 2. Static self-supervised representation

### DINOv3

- Paper: https://arxiv.org/abs/2508.10104
- Official research page: https://ai.meta.com/research/publications/dinov3/
- Code: https://github.com/facebookresearch/dinov3

DINOv3 is a strong current baseline for large-scale label-free visual representation and dense frozen features.

**Demonstrates:** a static visual encoder can learn broadly reusable object/part/shape/spatial features without task-specific labels.

**Does not establish:** persistent identity, world revision, temporal state, intervention sensitivity or action-conditioned dynamics.

**Clover question:** what world-understanding capability is genuinely missing once a strong static representation is already available?

## 3. Predictive video representation

### V-JEPA 2

- Paper: https://arxiv.org/abs/2506.09985
- Official page: https://ai.meta.com/vjepa/
- Research page: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- Code: https://github.com/facebookresearch/vjepa2

V-JEPA 2 combines large-scale action-free video pretraining with a relatively small amount of action-conditioned robot experience for planning.

**Demonstrates:** distributed predictive latent state can support motion understanding, anticipation and robot planning without a hand-designed explicit world language.

**Open contradiction:** does predictive latent state remain sufficient for long-horizon persistence, belief revision, auditability and unseen physical interventions?

### V-JEPA 2.1

- Paper: https://arxiv.org/abs/2603.14482

V-JEPA 2.1 strengthens dense, spatially structured and temporally consistent predictive features.

**Clover significance:** this is a serious alternative to a separately engineered `semantic + geometry + temporal` world representation.

## 4. Distributed physical variables are a real counterexample

### Interpreting Physics in Video World Models

- Official publication: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Paper: https://arxiv.org/abs/2602.07050

This mechanistic study finds that physical quantities such as speed, acceleration and direction become decodable at different depths, and that direction is represented using a high-dimensional population code rather than a small set of compact state coordinates.

**Research consequence:**

```text
useful physical information
≠ necessarily compact explicit variables
```

Historical Clover mechanisms therefore cannot justify explicit state by interpretability intuition alone.

## 5. Object-centric representation

### Slot Attention

- Paper: https://arxiv.org/abs/2006.15055

Slot Attention produces exchangeable object-like latent slots and demonstrated compositional generalization in controlled object-centric tasks.

**Potential advantage:** identity, relational structure and composition become easier to express.

**Open problem:** scalable object discovery in cluttered open-world video, dynamic topology, parts/fluids/deformables and ambiguous object boundaries.

### Visible entities are not persistent world entities

SAM 3.1 provides a strong modern video detection/segmentation/tracking baseline:

- Official: https://ai.meta.com/blog/segment-anything-model-3/
- Code: https://github.com/facebookresearch/sam3

But:

```text
mask / track while visible
≠ enduring entity after evidence disappears
```

This is a critical separator between perception and representation.

## 6. Hybrid and identifiable state

### Identifiable World Models from Pretrained Diffusion Representations

- Paper: https://arxiv.org/abs/2610.07028

This work asks whether a powerful distributed generative latent can be equipped with identifiable coordinates without retraining the generative backbone.

**Demonstrates in studied settings:** distributed world-model representations and interpretable/identifiable state coordinates need not be mutually exclusive.

**Clover significance:** the important comparison may not be `explicit vs latent`, but whether a hybrid can obtain the strengths of both with less cost than maintaining duplicate authorities.

## 7. Representation objectives preserve different information

Three major learning objectives should not be treated as synonyms:

```text
reconstruction → recover observed/spatial structure
prediction     → retain information useful for future state
 generation    → model a plausible conditional distribution
```

A representation that is excellent for one objective may discard information required by another.

Examples:

- VGGT / VGGT-Ω emphasize learned spatial reconstruction;
- V-JEPA emphasizes predictive latent state;
- Atlas / Cosmos emphasize generative/spatiotemporal simulation;
- VLA/WAM systems emphasize action-useful state.

## 8. Operational research questions

1. Does an explicit state offer measurable advantages in revision, querying or planning?
2. Can a distributed latent preserve object permanence and observability semantics without explicit variables?
3. Are object slots necessary, useful bias, or unnecessary restriction at open-world scale?
4. Can a hybrid representation avoid duplicate or inconsistent world authorities?
5. Which representation is most data-efficient for unseen dynamics?
6. Which representation transfers across camera and embodiment changes?
7. What information is lost by predictive compression?
8. What information is invented by generative completion?

## 9. Baseline families

| Family | Suggested comparator | Primary question |
|---|---|---|
| Static dense latent | DINOv3 | what can images alone encode? |
| Predictive video latent | V-JEPA 2/2.1 | can temporal prediction create sufficient world state? |
| Learned explicit geometry | VGGT / VGGT-Ω | is reconstruction enough for spatial understanding? |
| Object-centric | Slot Attention-style baseline | does factorized entity state improve composition/persistence? |
| Generative latent | Atlas/Cosmos-class evidence | does simulation imply usable state? |
| Hybrid identifiable | ConDA / identifiable world-model direction | can latent power coexist with interpretable coordinates? |
| Historical Clover | candidate explicit state | does it add independent measurable value? |

## 10. Discriminating experiment suite

### T-C-01 — Matched world-query probing

Use the same visual histories and probe each representation for:

```text
identity
object permanence
spatial relation
temporal order
observability
physical variables
world change
intervention consequence
```

Keep probe capacity controlled to avoid measuring probe power instead of representation quality.

### T-C-02 — Compression sufficiency

Compare representation sizes at matched query/task correctness.

Measure:

- representation bytes;
- answer coverage;
- correctness;
- long-occlusion degradation;
- new-query performance without retraining.

### T-C-03 — Revision locality

Introduce a local world change after a long history.

Measure whether the representation can update the affected world state without catastrophic or unnecessary global change.

### T-C-04 — Strong policy falsifier

```text
strong direct / recurrent policy
vs
same policy + candidate world representation
```

The world representation must improve at least one of:

- unseen-scene transfer;
- recovery;
- task success;
- planning cost;
- sample efficiency;
- unjustified action rate.

## 11. Kill conditions

A candidate representation should be rejected or simplified if:

- its advantages disappear with a stronger baseline;
- its benefit is only additional compute/memory;
- the same capability emerges in a simpler distributed state;
- explicit factors cannot be learned reliably from real visual data;
- hybrid state creates inconsistent duplicate authorities;
- representation quality does not translate to action or recovery.

## 12. Clover landing

Current conclusion:

> **Representation is still an open scientific variable. The strongest evidence argues against prematurely equating interpretability with correctness, while also leaving room for hybrid or identifiable state when it provides measurable revision, query, causal or action advantages.**

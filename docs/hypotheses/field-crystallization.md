# Hypothesis — Field Crystallization

**Status:** `RESEARCH_PROTOTYPE`

## Question

Can local visual evidence self-organize under a small set of dynamics into stable structures that correspond to useful world entities and relations?

## Intuition

The original Clover intuition combines puzzle fragments, charge-like local evidence and field/potential dynamics: fragmented evidence interacts and stabilizes into larger structures rather than relying exclusively on category-first detection.

## Current claim boundary

Existing implementation work shows that a field/crystallization mechanism can be constructed and used as part of a world prototype. It has **not** established that stable crystallization is equivalent to correct world structure or that this representation is superior to learned latent/object/geometry alternatives.

## Critical competing explanations

- ordinary connected components / tracking;
- object-centric slots;
- learned dense video representations;
- explicit learned geometry;
- segmentation + tracking pipelines.

## Falsifier

If field crystallization provides no independent gain in identity, relation, physical prediction, generalization or downstream decision under controlled complexity/compute, it should not remain a core mechanism merely because the analogy is elegant.

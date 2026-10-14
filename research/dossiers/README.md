# Clover Research Dossiers

Last updated: 2026-10-14  
Phase: **Background Research / Problem Reconstruction**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

These dossiers deepen the broad Survey into domain-specific research records. They are not architecture specifications. Each dossier is expected to answer:

```text
fundamental question
→ canonical foundations
→ strongest current approaches
→ exact primary / official / code URLs
→ demonstrated capability
→ limitation / confound
→ unresolved contradiction
→ best baseline
→ discriminating experiment
→ implication for Clover
```

## Dossiers

- [`R-A-observability-epistemology.md`](R-A-observability-epistemology.md) — partial observability, uncertainty, belief state, what pixels can and cannot identify.
- [`R-B-geometry.md`](R-B-geometry.md) — projective geometry, optical flow, SLAM, learned geometry and what is already solved.
- [`R-C-representation.md`](R-C-representation.md) — static SSL, predictive video, object-centric, explicit vs distributed vs hybrid state.
- [`R-D-memory-persistence.md`](R-D-memory-persistence.md) — object permanence, episodic memory, evidence retention, revision and forgetting.
- [`R-E-physics.md`](R-E-physics.md) — intuitive, relational and quantitative physical understanding.
- [`R-F-causality-interaction.md`](R-F-causality-interaction.md) — intervention, identifiability, counterfactual reasoning and causal representation.
- [`R-G-world-action.md`](R-G-world-action.md) — VLA, world-action models, planners and whether a persistent worldview adds measurable action value.
- [`R-H-active-perception-lifelong.md`](R-H-active-perception-lifelong.md) — information-seeking action, viewpoint selection, world growth and lifelong visual experience.

## Cross-domain contradictions

The dossiers should converge on evidence about six primary contradictions rather than on historical module names:

```text
C1 explicit state vs distributed latent vs hybrid / identifiable state
C2 reconstruction vs prediction vs generation
C3 object-centric vs dense scene representation
C4 passive observation vs interaction
C5 persistent world state vs long context / direct policy
C6 evidence-grounded belief vs plausible generative completion
```

## Source discipline

For durable claims, prefer in order:

1. peer-reviewed paper or primary preprint;
2. official project/model/research page;
3. official open-source repository/checkpoint;
4. official company/lab result, explicitly labeled `OFFICIAL_REPORTED_RESULT`;
5. secondary/news source only as `SURVEY_SIGNAL` until replaced by a primary source.

Every important source should also be mirrored into [`../survey/SOURCE_MAP.md`](../survey/SOURCE_MAP.md) when it materially constrains the project.

## Research order

```text
Background Research / Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
```

A dossier is mature when it makes a future baseline or falsifier clearer. It is not mature merely because it contains many papers.

# 11 — Language and the Vision-Only Question

## Question

How should Clover study systems that use language pretraining when the SSOT asks what can be understood through vision alone?

## Why the distinction matters

Modern embodied models often inherit enormous amounts of semantic and commonsense knowledge from language or vision-language pretraining. This can dramatically improve task generalization, but it complicates claims about what was learned from visual evidence.

RT-2 explicitly transfers web-scale vision-language knowledge into robot control. π0.5 mixes image observations, language, object detections, semantic subtasks, web data and robot actions. Gemini Robotics ER 2 is a vision-language model based on Gemini 3.5 Flash.

These systems are important capability references, but they are not pure tests of visual world formation.

## Proposed research separation

Clover should distinguish:

### Vision-only formation

What world structure can be learned from visual observations and visually observed interaction without language supervision?

### Language alignment

Once a world representation exists, can language efficiently name, query and compose the learned structures?

### Language prior

How much performance comes from knowledge imported through text rather than discovered from visual experience?

## Why this does not mean rejecting language

A general-purpose robot brain will likely need language. The research constraint is about causal attribution of capability, not banning useful interfaces.

Language can be a communication and task-specification channel while the scientific question remains: what world knowledge did vision itself provide?

## Clover implication

Future experiments should include vision-only and vision+language conditions when language knowledge could otherwise confound the central claim.

## Primary sources

- RT-2: https://arxiv.org/abs/2307.15818
- OpenVLA: https://arxiv.org/abs/2406.09246
- π0.5: https://arxiv.org/abs/2504.16054
- Gemini Robotics ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- V-JEPA 2: https://arxiv.org/abs/2506.09985

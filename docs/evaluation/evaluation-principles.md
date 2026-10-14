# Evaluation Principles

## 1. Benchmarks are instruments

A benchmark answers a narrow measurement question. It does not define Clover's research problem.

## 2. Capability before leaderboard position

Before asking whether Clover is first on a leaderboard, ask whether the protocol measures a capability required by a general-purpose visual robot brain.

## 3. Use real tasks at the top of the evidence hierarchy

Controlled benchmarks are essential for diagnosis, but the eventual claim must survive unfamiliar physical environments and embodied tasks.

## 4. Separate perception success from world-model success

Detection, segmentation, depth, flow, reconstruction and tracking can each be excellent while the system still lacks a persistent, revisable world model.

## 5. Separate prediction from causality

Future prediction is evidence of useful dynamics, not automatically causal understanding. Strong causal claims require intervention-sensitive or counterfactual protocols.

## 6. Separate answer accuracy from coverage

If a system can refuse or return Unknown, report at minimum:

- coverage;
- correctness conditional on answering;
- unjustified assertion rate;
- refusal/unknown rate.

A system cannot obtain an apparent scientific win by refusing almost everything.

## 7. Track privileged information

Every evaluation should document what enters the model:

- RGB only?
- camera calibration?
- multiple cameras?
- depth?
- language?
- actions/proprioception?
- ground-truth state?

Examiner truth must not leak into the model path.

## 8. Attack shortcuts

Where possible use minimal pairs, scene/background probes, temporal shuffle, crop-only and language-only controls.

## 9. Compare representations on downstream consequences

Representation quality should eventually be judged by what it enables:

- better generalization;
- more reliable world queries;
- faster recovery;
- less data;
- better planning;
- lower compute;
- more stable long-horizon behavior.

## 10. Report evidence provenance

Distinguish:

- independently reproduced result;
- peer-reviewed/public benchmark result;
- official project result;
- vendor-reported closed-system result;
- Clover internal result.

Do not present these as equivalent evidence.

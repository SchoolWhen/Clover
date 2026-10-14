# Benchmark and Dataset Map

This file records what each instrument measures before Clover decides which evaluations belong in a future paper.

| Instrument | Area | What it helps measure | Starting point |
|---|---|---|---|
| IntPhys 2 | intuitive physics | permanence, immutability, spatiotemporal continuity, solidity | https://github.com/facebookresearch/IntPhys2 |
| MVPBench | physical video QA | shortcut-resistant minimal-pair physical reasoning | https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/ |
| CausalVQA | causality | causal, hypothetical, counterfactual and anticipation reasoning | https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/ |
| Perception Test | video perception | tracking, memory, action localization and video QA | https://github.com/google-deepmind/perception_test |
| Ego4D | egocentric video | real human first-person activities and long visual context | https://ego4d-data.org/ |
| DROID | robot data | in-the-wild robot manipulation video/action data | https://droid-dataset.github.io/droid/ |
| Open X-Embodiment | robot data | multi-embodiment robot experience | https://github.com/google-deepmind/open_x_embodiment |
| LIBERO | robot learning | lifelong transfer and manipulation suites | https://github.com/Lifelong-Robot-Learning/LIBERO |
| CALVIN | robot learning | long-horizon language-conditioned manipulation | https://github.com/mees/calvin |
| RoboCasa | robot learning | diverse household manipulation tasks/scenes | https://robocasa.ai/ |

## Usage rule

Before adopting an instrument, document:

- exact capability under test;
- permitted inputs (especially what counts as vision alone);
- known shortcuts/leakage;
- metric limitations;
- whether success can occur without a persistent world model;
- relationship to a real embodied capability.

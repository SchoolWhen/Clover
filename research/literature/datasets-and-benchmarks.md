# Datasets, Benchmarks and Task Environments

Last verified: 2026-10-14

This file is a research-resource index. Dataset size and task counts are recorded from official project sources when available.

| Resource | Type | Relevant scale / scope | Why Clover cares | Primary source |
|---|---|---|---|---|
| IntPhys 2 | synthetic physics benchmark | permanence, immutability, continuity, solidity | controlled intuitive-physics diagnostic | https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ |
| MVPBench | physical video QA | 55K examples, minimal-pair design | shortcut-resistant physical reasoning | https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/ |
| CausalVQA | real-video causal QA | five causal/reasoning question families | counterfactual/anticipation diagnostic | https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/ |
| Perception Test | multimodal video benchmark | QA, object/point tracking, action/sound localization | memory/physics/tracking diagnostic | https://github.com/google-deepmind/perception_test |
| Ego4D | egocentric video | ~3,600+ hours daily-life video | long visual history, memory, object interaction, forecasting | https://ego4d-data.org/docs/ |
| DROID | robot interaction dataset | 76K trajectories / 350h / 564 scenes / 86 tasks | passive-video vs action-conditioned learning | https://droid-dataset.github.io/ |
| Open X-Embodiment | cross-robot dataset | 22 embodiments; >1M episodes reported | cross-embodiment abstraction and transfer | https://github.com/google-deepmind/open_x_embodiment |
| LIBERO | lifelong robot benchmark | multiple suites/tasks | knowledge transfer and continual learning | https://libero-project.github.io/main.html |
| CALVIN | simulated robot benchmark | long-horizon language-conditioned manipulation | downstream long-horizon planning/control | https://github.com/mees/calvin |
| RoboCasa365 | generalist robot simulation/benchmark | 365 tasks; 2,500+ kitchen scenes; 2,200+ hours demos reported | compositional generalization and long-horizon manipulation | https://robocasa.ai/ |

## Dataset-role discipline

Different data sources provide different evidence:

### Passive internet / human video

Good for visual diversity and natural physical regularities. Lacks direct knowledge of the observer's intervention/action variables.

### Egocentric human video

Closer to embodied visual experience and object interaction, but embodiment/action labels may not transfer directly to robots.

### Robot demonstrations

Provides actions and consequences, but is expensive and usually narrower in environment diversity.

### Simulation

Provides exact state/interventions and cheap scale, but creates a reality gap.

### Closed real-robot evaluations

Provide strong capability evidence, but may lack reproducibility and inspectability.

Clover should eventually exploit these roles deliberately rather than treating all video/robot data as interchangeable.

# Frontier Signals — Filtered 2026 Watchlist

Last updated: 2026-10-14

This is the screened successor to the internal `news(5).md` archive. A signal is kept when it changes how the central problem should be framed, reveals a competing approach, exposes an evaluation failure, or points to primary material worth deeper study.

A frontier signal is **not automatically a scientific result or a Clover design decision**.

Evidence labels: `PRIMARY_PAPER`, `OFFICIAL_PROJECT`, `OPEN_SOURCE`, `OFFICIAL_REPORTED_RESULT`, `SURVEY_SIGNAL`.

## S1 — World models are moving from visual fidelity toward task-relevant state

**ReWAM** — https://arxiv.org/abs/2609.38163 — `PRIMARY_PAPER`

Reconstruction fidelity and generic perceptual features do not necessarily produce policy-useful representation. Clover therefore cannot use “accurate reconstruction” as the sole world-state objective.

## S2 — Intended action and realized consequence are different

**HWAM** — https://arxiv.org/abs/2610.12026 — `PRIMARY_PAPER`

Reference action, executed motion and observed consequence should be modeled separately. This is a general robot-brain state-transition issue, not only a VLA detail.

## S3 — Passive video is a serious physical-representation route

**V-JEPA 2** — https://arxiv.org/abs/2506.09985 · https://ai.meta.com/vjepa/ · https://github.com/facebookresearch/vjepa2

**V-JEPA 2.1** — https://arxiv.org/abs/2603.14482

Large-scale action-free video can learn motion/anticipation structure and dense temporal features before robot interaction is introduced. Open question: what does interaction add that passive observation cannot?

## S4 — Physical variables may be distributed

**Interpreting Physics in Video World Models** — https://arxiv.org/abs/2602.07050 · https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Physical quantities need not appear as a small hand-designed state vector. This is direct counter-pressure against historical explicit-state assumptions.

## S5 — Memory architecture can unlock capability without changing weights

**VISTA** — https://arxiv.org/abs/2610.02200

Lossless visual memory + active retrieval/reorganization makes evidence memory itself a research variable distinct from model weights/world state.

## S6 — Evidence/view selection is a reasoning variable

**Vantage** — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage

View planning can improve spatial reasoning without changing the base VLM. This strengthens active-perception/evidence-scheduling research.

## S7 — Confidence is useful but is not truth

**SpatialCORE** — https://arxiv.org/abs/2609.38716 · https://github.com/rafiibnsultan/SpatialCORE

Grounding confidence can be a training/compute signal. It should not automatically become world authority.

## S8 — Hierarchical world representations remain a live response to long horizons

**H-WM** — https://arxiv.org/abs/2602.11291

High-level logical and low-level visual transitions directly target the tradeoff between long-horizon robustness and perceptual grounding.

## S9 — Identifiability may bridge latent and explicit state

**Identifiable World Models** — https://arxiv.org/abs/2610.07028

A small identifiable/interpretable coordinate layer may sit on top of a powerful distributed representation. Explicit-vs-latent need not be binary.

## S10 — Learned geometry is becoming foundation representation

**VGGT** — https://arxiv.org/abs/2503.11651 · https://github.com/facebookresearch/vggt

**VGGT-Ω** — https://arxiv.org/abs/2605.15195 · https://vggt-omega.github.io/ · https://github.com/facebookresearch/vggt-omega

Any future Clover spatial primitive must justify what it contributes beyond modern learned camera/depth/point-map/track reconstruction.

## S11 — Spatial world models merge reconstruction, generation and simulation

**Atlas** — https://www.worldlabs.ai/blog/atlas — `OFFICIAL_PROJECT`

A single learned spatial model can serve reconstruction, generation, simulation and robotics workflows. Important boundary: plausible hidden completion is not observed/justified truth.

## S12 — World foundation models merge reasoning, generation and action

**Cosmos 3** — https://arxiv.org/abs/2606.02800 · https://github.com/nvidia/cosmos

The boundaries between world model, reasoner, generator and action model are becoming less clean. Clover's modular decomposition must earn its value empirically.

## S13 — Robot foundation models are serious falsifiers for explicit-worldview claims

**Figure Helix 2.5** — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization — `OFFICIAL_REPORTED_RESULT`

**Skild S1** — https://skild.ai/blogs/s1 — `OFFICIAL_REPORTED_RESULT`

**Physical Self-Play** — https://skild.ai/blogs/physical-self-play

If broad learned policies can generalize/recover without exposed persistent state, Clover must prove exactly what a worldview adds.

## S14 — VLA remains a real competing route

- RT-2: https://arxiv.org/abs/2307.15818
- OpenVLA: https://arxiv.org/abs/2406.09246 · https://github.com/openvla/openvla
- π0.5: https://arxiv.org/abs/2504.16054

The Clover question is not “how to avoid VLA?” It is whether a world representation gives measurable benefits that strong direct/hierarchical policies do not obtain as reliably, generally or efficiently.

## S15 — World-Action Models are becoming a distinct category

**WAM survey** — https://arxiv.org/abs/2609.16074 · https://rcl-robotics.github.io/Awesome-World-Action-Models

Open challenges include world-action factorization, alignment, long-horizon memory and efficient inference.

**Being-M0.7** — https://arxiv.org/abs/2610.11283

Uses >10,000 hours of mixed human video/motion data to learn future-aware visual-motion priors before humanoid adaptation.

**Being-H0.7** — https://arxiv.org/abs/2605.00078

Uses latent future-aware reasoning with a training-only future branch, avoiding future-pixel rollout at inference.

## S16 — Physical consistency needs state/process supervision, not pretty rollouts

**EVEWorld** — https://arxiv.org/abs/2610.03374

Targets “model laziness”: visually plausible rollouts with poor object/evolution consistency.

**RoboPhys-3D** — https://arxiv.org/abs/2608.28718

Evaluation is moving toward reconstructed state and execution-grounded physics.

```text
plausible video ≠ correct world state ≠ useful action consequence
```

## S17 — Pixels-to-physics systems explicitly add interaction-grounded physical state

**DR-WM / From Pixels to Executable Physics** — https://arxiv.org/abs/2610.17630

Visual geometry is combined with terrain/contact priors and action-response calibration so the same command can produce terrain-dependent outcomes. This supports the hypothesis that some action-relevant physical variables require interaction rather than appearance alone.

## S18 — Sparse visual change can support high-rate computation

**Motion-aware Event Suppression** — https://arxiv.org/abs/2602.23204

The useful abstraction for Clover is “compute on informative change,” not necessarily “depend on event-camera hardware.”

## S19 — Tactile/force work defines a boundary condition for “vision alone”

The raw news archive repeatedly surfaced tactile hands/world models/contact-rich manipulation. The durable research distinction is:

```text
Can vision infer a useful hidden-property hypothesis?
vs
Can vision uniquely measure force/friction/internal contact state?
```

Clover must not silently turn non-identifiable quantities into observed facts. A future product can use more sensors while the scientific vision-only protocol remains explicit.

## S20 — The capability frontier is unfamiliar, long-horizon, closed-loop behavior

Across Figure, Skild, Google and other robotics programs, the durable signal is movement toward unseen environments, longer tasks, mobile/whole-body manipulation, active perception, world change/recovery and broad experience pretraining.

This supports Clover's evaluation hierarchy: diagnostics are necessary, but eventual validation is embodied capability.

## Not promoted to current conclusions

The raw news archive also contains funding/valuation reports, supply-chain announcements, secondary summaries, single demos, unclear benchmark numbers and old “this proves Clover is right” interpretations. These remain historical signals unless primary/official technical evidence becomes available.

## Future signal template

A durable signal should contain:

```text
name
primary/official URL
evidence class
what changed
what it does not prove
why the SSOT cares
research question affected
```

A frontier signal is a reason to investigate, not a reason to stack another framework into Clover.

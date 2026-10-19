# Stage-1 Frontier Sweep — 2026-10-16 → 2026-10-19

Last updated: **2026-10-19**
Freshness cutoff checked through: **2026-10-19**

> Mother question: **How can a machine understand the real world through vision alone?**

This sweep extends the Stage-1 frontier watch from the 2026-10-15 cutoff (`../RESEARCH_FRONTIER.md`) to 2026-10-19. It is supporting Stage-1 material: it does **not** freeze a representation, backbone or training recipe, and it does **not** promote any mechanism into Clover Innovation.

Raw discovery material for this window lives in the news archive edition [`../../news_2610192217.md`](../../news_2610192217.md) (`SURVEY_SIGNAL`). Items below were upgraded against primary or official sources on 2026-10-19 where a source is marked `PRIMARY_PAPER` / `OFFICIAL_*`; items still resting on secondary listings stay `SURVEY_SIGNAL`.

## Project context for this sweep

```text
CPU-only implementation track: frozen at current results (2026-10-19 decision).
Main line: embodied robotic-brain research on top of those results.
This sweep therefore weights decision/action usefulness (SSOT evidence axis A)
and deployment/runtime evidence more heavily than before,
without dropping the vision-only identifiability discipline (V0–V3, L0–L4).
```

---

## 1. Verified additions

| Date | Source | Evidence | What it demonstrates | Does **not** prove | Stage-1 landing |
|---|---|---|---|---|---|
| 2026-10-15 (listed 10-16) | **VLA-Δ: Learning Physical State Transition for VLA Models** — https://arxiv.org/abs/2610.21306 · code https://github.com/ZJU-OmniAI/VLA-Delta | `PRIMARY_PAPER` / `OPEN_SOURCE` | Supervising the **physical state transition** (Δ between current and future state) instead of only the action improves VLA policies; reported competitive on LIBERO/RoboTwin and **above π0.5 in real-robot experiments**, with zero added inference cost | a state-transition target is a sufficient *world state*, or that Δ-supervision transfers across embodiments without the pretraining mixture used | state-transition supervision · sufficient state (S-PRED vs S-CTRL) · training/post-training |
| 2026-10-16 | **HIJP: Hindsight Inverse JEPA Planning** — https://arxiv.org/abs/2610.23615 | `PRIMARY_PAPER` | Search-free latent planning: a goal-conditioned inverse model replaces test-time action search; hindsight goal relabeling shapes the visual representation; reported 86.8% success across four visual control tasks and 1.9–16.5× planning speedup over search-based planning | latent inverse planning preserves uncertainty/epistemic state, or scales to contact-rich manipulation | JEPA planning · runtime systems · sufficient state |
| 2026-06-30 (resurfaced 10-19) | **AdaJEPA: An Adaptive Latent World Model** — https://arxiv.org/abs/2606.32026 · project https://agenticlearning.ai/adajepa/ · code https://github.com/agentic-learning-ai-lab/adajepa | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE` | A latent world model need not stay frozen at deployment: test-time adaptation inside the MPC loop, using executed transitions as self-supervision, with as little as one gradient step per replan, improves planning under distribution shift | online adaptation is safe/monotonic in open worlds, or that adaptation preserves calibration and long-horizon memory (no forgetting analysis for embodied deployment) | deployment learning (TR10/TR11) · model invalidation (E6) · belief revision |
| 2026-10-14 (demo window 10-20→22) | **NEURA Robotics — Neuron AI (PLA)** — official: https://neura-robotics.com/neura-robotics-introduces-neuron-ai/ · model page https://neura-robotics.com/neuron-ai | `OFFICIAL_REPORTED_RESULT` | A vendor robotic brain claiming perception-language-action with 3D vision + touch + sound + proprioception + memory, on-robot local inference, and an 11-minute unattended laundry sequence on 4NE1 at GTC Berlin 2026 (Hall 3, Booth #3031, Oct 20–22) as its public test | any benchmark number: at launch NEURA published **no** success rates, no Time-to-Skill figures and no independent evaluation; multisensory fusion also means it is **not** a vision-alone (V0–V3/L0–L4-clean) result | robotic-brain competitor watch · persistent memory claims · EV ladder (public demo ≈ EV7 claim, unverified) |
| 2026-10-17→19 (statements) | **OpenAI humanoid program** — Altman statements (Sources podcast / Fortune), reported 2026-10-19: https://www.timesnownews.com/technology-science/openai-is-building-its-own-humanoid-robot-ceo-sam-altman-confirms-article-156365247 | `OFFICIAL_REPORTED_RESULT` (executive statements via press; no OpenAI technical page yet) | The largest foundation-model lab is becoming a full-stack robotic-brain competitor: own humanoid, "cool demo in 2027", and the explicit claim that **the brain matters more than the body design**; ~27 robotics roles open (motion control, whole-robot behaviour, manufacturing) | any capability: no model, data, benchmark or hardware detail has been published | industry structure · robotic-brain race · watch for technical disclosure in 2027 demo run-up |
| 2026-04-15 (rechecked 10-19) | **HY-World 2.0** — https://arxiv.org/abs/2604.14268 | `PRIMARY_PAPER` / `OPEN_SOURCE` | Generative 3D world route: reconstruct/generate/simulate editable 3D worlds (mesh / 3DGS / point cloud) from text/image/video, exportable to Unity/UE and embodied-sim pipelines | generated 3D plausibility = physically correct, queryable world state; it sharpens, but does not settle, the "world model" definition dispute (generation vs explicit queryable state) | world-model definition watch · 3D representation · simulation data engines |

## 2. Discovery signals still needing primary-source upgrade

From the 2026-10-15/16 daily-paper listings (Hugging Face / Robotica) and the 10-16→19 digests. Each stays `SURVEY_SIGNAL` until its arXiv page is read and recorded with the §26 contribution template.

```text
Velox: Spatial Memory Makes World Models Efficient (2026-10-15)
  → persistent spatial memory as an efficiency mechanism, not only a capability one
  → landing: memory / sufficient state / edge cost

Can World and Action Modeling Benefit Each Other under Unified Causal Training? (2026-10-15)
  → causal unification of WAM training; direct test of world↔action factorization assumptions
  → landing: WAM · causality

WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction (2026-10-13/15)
  → hybrid VLA+latent-prediction; compare against GreenWAM / LoopWAM already indexed
  → landing: VLA/WAM boundary

Towards Agentic Robots: Model, Data, Environment, and Harness (2026-10-14) — https://arxiv.org/abs/2610.20442 (html listing seen)
  → agentic-robot system decomposition; harness contribution accounting (AGENTS §21)
  → landing: foundation-model systems · harness

TacDyn-WAM (v1 2026-09-30, resurfaced 2026-10-17)
  → predict contact change, not every tactile pixel — boundary condition for vision-alone claims:
    which contact variables are identifiable from vision (V-protocol) vs require L4 evidence?
  → landing: physical properties · identifiability · provenance

HexaShell / CarryOn / CoDA (2026-10-15/16 listings)
  → harness-as-policy and data-engine co-evolution signals; keep in harness/RSI watch, not core survey
  → landing: foundation-model systems · training
```

## 3. Breadth check (is the survey still wide, not only frontier-chasing?)

Stage 1 requires coverage **before** commitment. This sweep re-checked the breadth axes of `../RESEARCH.md` against the 10-16→19 inflow; the inflow is heavily concentrated in VLA/WAM and industry brain announcements. The following breadth areas received **no** new material this window and remain standing collection obligations, to be filled from primary/canonical literature (not news) in the next sweep:

```text
classical geometry / SLAM / SfM baselines and their failure records
human & developmental visual cognition (object permanence, intuitive physics)
image formation & adverse visual conditions (observation physics)
POMDP / observability / identifiability theory (canonical, pre-2026 sources)
deformable / fluid / granular dynamics beyond rigid-body benchmarks
evaluation methodology: shortcut-resistant, examiner-isolated test design
```

Rule reinforced: frontier items may **not** narrow the survey. A sweep that only adds VLA/WAM papers is a failed sweep.

## 4. What changed in the comparison space

```text
state-transition (Δ) supervision
≠ world-state representation — but it is now a measured training signal
  a robotic brain can exploit without inference cost

frozen-at-deployment world model
≠ default assumption — AdaJEPA makes deployment-time adaptation
  a first-class design variable (with open safety/forgetting questions)

"robotic brain" is now an explicit industry product category
  (OpenAI full-stack entry; NEURA PLA; Figure/Skild class systems)
  → Clover's long-term goal statement is the contested ground itself;
    differentiation must come from evidence quality (identifiability,
    licence-style accounting, falsifiable claims), not from the slogan

public unattended long-sequence demos (NEURA laundry, 11 min)
  → becoming the industry's informal EV7 evidence; Clover's EV ladder
    remains the stricter accounting and should be applied to every such claim
```

## 5. Next checks (owners: research line, no deadline theatre)

1. Read VLA-Δ and HIJP in full; record both with the AGENTS §26 template in `../survey/SOURCE_MAP.md` and decide whether Δ-supervision deserves a Stage-2 one-method-one-report slot.
2. NEURA GTC Berlin (2026-10-20→22): collect independent reporting/video of the laundry sequence; score against the EV ladder and the memory/persistence claims; upgrade or downgrade the `OFFICIAL_REPORTED_RESULT` accordingly.
3. Upgrade §2 signals to primary sources in listing order; drop any that cannot be upgraded.
4. Next sweep must include at least one canonical/breadth source per §3 axis (pre-2026 primary literature counts).
5. Watch for OpenAI robotics technical disclosure (paper, system card, or demo protocol) rather than executive statements.

# SURVEY_BREADTH — Breadth Foundation for Stage-1 Research

**Created:** 2026-10-19 · **Place:** repository root (flat layout, next to [`NEWS.md`](NEWS.md) and [`STATUS.md`](STATUS.md))
**Companion:** [`research/emerging/FRONTIER_SWEEP_2026-10-19.md`](research/emerging/FRONTIER_SWEEP_2026-10-19.md) tracks the *frontier*; this file builds the *breadth* underneath it.

The 2026-10-19 frontier sweep found that recent intake was almost entirely VLA / world-action-model / industry-brain news, with **zero new material on six breadth axes**. Rule adopted there and kept here:

```text
a sweep with frontier but no breadth counts as failed
```

This file records verified anchor sources for those six axes, plus the standing tracking channels that keep both breadth and frontier current. Entries follow the AGENTS §4.4 record shape (problem / demonstrates / does-not-demonstrate / assumptions / counter-hypothesis) in compact form. Anchors were located and bibliographically verified on 2026-10-19; unless marked otherwise, status is **abstract/bibliographic level — full-text read is queued, not done**. No entry here is an architecture decision (§4.2, §26).

---

## 0. Standing tracking channels

| Channel | What it feeds | Cadence |
|---|---|---|
| arXiv listings cs.RO / cs.CV / cs.LG / cs.AI | frontier papers | daily digest |
| CoRL (2026: Austin, workshops 12 Nov 2026; CFP explicitly lists *video models and latent world models for robot learning* and *robot foundation models*) | top-venue robot learning | proceedings sweep at publication |
| RSS (2027: Athens, 6–11 Jul 2027; extended-abstract deadline 2026-12-04) | top-venue robotics | proceedings sweep |
| ICRA / IROS / CVPR / ICCV / NeurIPS / ICLR / ICML / AISTATS | method + theory anchors | proceedings sweep |
| Journals: T-RO, IJRR, Science Robotics, PNAS, Nature Machine Intelligence, Artificial Intelligence | durable results | monthly scan |
| Official industry sources only (NVIDIA, Google DeepMind, Physical Intelligence, Figure, NEURA, OpenAI, Tesla) | industry claims as `OFFICIAL_*` / `SURVEY_SIGNAL` | daily digest |

Company statements never become scientific fact silently (§4.5). News remains a discovery layer; durable conclusions must be upgraded to `PRIMARY_PAPER` / `OFFICIAL_*` and recorded in `research/survey/SOURCE_MAP.md` / `research/RESEARCH_FRONTIER.md`.

---

## 1. Axis A — Partial observability & identifiability theory

**Why this axis:** Clover's core promise is a *licensed* world state from vision alone. Whether a hidden variable is determined by visual evidence at all — and under what extra assumptions — is a theorem-level question, not an architecture preference (§7: predictability is not identifiability).

### A1. POMDP formalism — Kaelbling, Littman & Cassandra (1998)

- **Source:** *Planning and acting in partially observable stochastic domains*, Artificial Intelligence 101(1–2):99–134. DOI: https://doi.org/10.1016/S0004-3702(98)00023-X · `PRIMARY_PAPER` (bibliographic + abstract verified 2026-10-19)
- **Problem:** optimal action when the true state is never directly observed and both actions and observations are stochastic.
- **Demonstrates:** belief state (a distribution over world states) is a sufficient statistic for the observation history; exact solution is computationally hard even for small domains.
- **Does not demonstrate:** how to *learn* the model or the belief representation from raw pixels; assumes a given state space and observation model.
- **Landing for Clover:** the belief/licence discipline has a classical formal home — "unobserved ≠ free, unknown is a state" is POMDP orthodoxy, not a Clover invention. Any Clover state claim should name which POMDP assumption it keeps or drops.

### A2. Identifiability of learned latent state — Khemakhem et al. (2020)

- **Source:** *Variational Autoencoders and Nonlinear ICA: A Unifying Framework*, AISTATS 2020, PMLR 108:2207–2217. http://proceedings.mlr.press/v108/khemakhem20a.html · `PRIMARY_PAPER` (verified 2026-10-19)
- **Problem:** when is a learned latent representation *the* latent state, rather than one of infinitely many equivalent reparameterisations?
- **Demonstrates:** with an auxiliary variable conditioning the prior (iVAE), the latent model is identifiable up to simple transformations; plain VAEs / unconditional latent models are provably **non-identifiable**.
- **Does not demonstrate:** identifiability from raw video alone without auxiliary structure; the auxiliary variable is an added assumption, not a free lunch.
- **Landing for Clover:** pairs with *Identifiable World Models* (arXiv:2610.07028, already tracked in the frontier survey). Together they set the Stage-1 question precisely: *what auxiliary structure (temporal contrast, action, multi-view, intervention) makes a visual world state identifiable, and what equivalence class remains?* Any "learned world state" claim that cannot answer this is incomplete.

---

## 2. Axis B — Human & developmental visual cognition

**Why this axis:** infants solve a version of the mother question from vision with almost no language. Their constraint set — what is present early, what is absent — is evidence about what visual world understanding minimally requires, and the violation-of-expectation paradigm is a ready-made falsification instrument.

### B1. Core knowledge — Spelke et al. (1992)

- **Source:** *Origins of knowledge*, Psychological Review 99(4):605–632. DOI 10.1037/0033-295X.99.4.605 · PubMed: http://www.ncbi.nlm.nih.gov/pubmed/1454901 · `PRIMARY_PAPER` (abstract verified 2026-10-19)
- **Demonstrates:** early infant physical reasoning accords with **continuity** (objects move on connected paths) and **solidity** (no two objects in the same place at the same time).
- **Does not demonstrate — equally important:** early reasoning does **not** accord with **gravity** or **inertia**. The honest reading is a *partial* constraint set, not a full physics engine at birth.
- **Landing for Clover:** continuity + solidity are candidate Stage-1 test constraints (object permanence across occlusion); gravity/inertia must be treated as *learned or absent*, not assumed as priors. This also warns against importing a complete "core knowledge" checklist as an axiom set (§4.1).

### B2. Violation-of-expectation — Baillargeon (1985; Baillargeon & Graber 1987)

- **Source:** drawbridge experiments (1985) and tall/short-rabbit screen experiments (1987), Developmental Psychology / Cognition venues. Locator (secondary): https://simplypsychology.org/wp-content/uploads/cogDev_BaillargeonEssay.pdf · `BACKGROUND_REFERENCE` — primary full-text read queued.
- **Demonstrates:** infants as young as ~3.5–5 months look longer at physically *impossible* events (screen rotating through a hidden box; tall rabbit failing to appear in a window), i.e. they maintain occluded objects and expectations about them.
- **Does not demonstrate:** the internal representation format; looking time is an expectation signal, not a state readout. The paradigm's interpretation has known critiques (perceptual-novelty confounds), which any borrowing must record.
- **Landing for Clover:** VoE is a transferable *evaluation* design — possible vs impossible event pairs with matched perceptual novelty — directly usable as a shortcut-resistant test shape for object permanence (see Axis F).

### B3. Intuitive physics engine — Battaglia, Hamrick & Tenenbaum (2013)

- **Source:** *Simulation as an engine of physical scene understanding*, PNAS 110(45):18327–18332. DOI 10.1073/pnas.1306572110 · Open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC3831455/ · `PRIMARY_PAPER` (abstract verified 2026-10-19)
- **Demonstrates:** a single probabilistic-simulation model fits human judgments across five psychophysical tasks (stability, support, tearing, containment…), including human illusions and biases — humans appear to run *approximate, noisy* simulation, not exact physics.
- **Does not demonstrate:** that the brain literally contains a physics engine of this form, nor that simulation is the only route; it is a computational-level fit to adult judgments.
- **Landing for Clover:** a competing hypothesis to keep visible (§4.4): world understanding as *approximate simulation over an inferred scene* vs Clover-style *queryable state with licences*. The two make different predictions under occlusion and counterfactual queries — a discriminating test belongs in Stage 2.

---

## 3. Axis C — Classical geometry, SLAM & SfM

**Why this axis:** the geometry tradition is the strongest existing answer to "state from vision alone" and the baseline any learned world state must beat or honestly differ from. Its failure records are as valuable as its successes.

### C1. DROID-SLAM — Teed & Deng (2021)

- **Source:** *DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras*, NeurIPS 2021. https://arxiv.org/pdf/2108.10869 · Code: https://github.com/princeton-vl/DROID-SLAM · `PRIMARY_PAPER` + `OPEN_SOURCE` (abstract verified 2026-10-19)
- **Demonstrates:** learned recurrent updates + a **differentiable dense bundle-adjustment layer** achieve large accuracy gains and far fewer catastrophic failures than prior systems, generalising across camera setups.
- **Does not demonstrate:** object-level or physical world state; output is camera pose + per-pixel depth. Notably, the learned front-end did **not** replace geometric optimisation — the state is still produced by bundle adjustment.
- **Landing for Clover:** evidence that "end-to-end learned" claims in this space quietly keep a geometric solver at the core. Any Clover geometric claim must state its relation to BA-style global consistency explicitly. Observation protocol of DROID-SLAM training: `L1`/`L4`-adjacent (supervised depth/pose signals) — deployment input being RGB does not make it vision-alone learning (§5).

### C2. ORB-SLAM3 — Campos et al. (2021)

- **Source:** *ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multimap SLAM*, IEEE Transactions on Robotics 37(6):1874–1890, 2021 (bibliographic record via citing literature, verified 2026-10-19). `PRIMARY_PAPER` / `OPEN_SOURCE`
- **Demonstrates:** the mature classical stack (feature tracking, local mapping, loop closure, map merging, visual-inertial fusion) and its documented operating envelope.
- **Does not demonstrate:** robustness in low-texture, dynamic, or badly lit scenes — the classical failure triad that motivated learned methods.
- **Landing for Clover:** the reference failure catalogue for Axis D: classical geometry fails exactly where image formation stops cooperating. A vision-alone brain must degrade *licences*, not silently hallucinate state, in the same conditions.

---

## 4. Axis D — Image formation & adverse visual conditions (observation physics)

**Why this axis:** §6 — world-state ambiguity ≠ image-formation ambiguity ≠ sensor corruption. What the pixels *cannot* contain is set by optics and acquisition before any model runs.

### D1. Brightness constancy & the aperture problem — Horn & Schunck (1981)

- **Source:** *Determining Optical Flow*, Artificial Intelligence 17:185–203, 1981. Reprint locator: http://dev.ipol.im/git/?p=coco/ipol_phs.git;a=blob_plain;f=doc/ipol_horn_schunck_draft.pdf;h=dc931ccba98cafe3742ffeb819d161ac361e3cbb;hb=575a90230da4c38969a1674748b29c9bb5fedf70 · `PRIMARY_PAPER` (bibliographic verified 2026-10-19)
- **Demonstrates:** under brightness constancy, one pixel yields one equation for two unknowns (the aperture problem): local image evidence *provably underdetermines* motion; their smoothness prior is an added assumption that fills the gap — visibly, the field's first explicit "licence" for inferred state.
- **Does not demonstrate:** validity under illumination change, specularity, transparency or occlusion boundaries — exactly where brightness constancy breaks.
- **Landing for Clover:** the canonical template for every observation-physics entry: name the image-formation assumption, name what it licenses, name where it dies. Full assumption checklist lives in [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md); this axis queues its adverse-condition evidence (low light, fog/rain, specular/transparent materials, motion blur, rolling shutter) as Stage-1 reading, still **open** — no verified anchor yet, recorded as a gap rather than filled with news (§28.22).

---

## 5. Axis E — Deformable, fluid & granular dynamics

**Why this axis:** rigid-body benchmarks dominate the frontier intake; household worlds are cloth, dough, liquid, cables and piles. A brain claim scoped to rigid scenes must say so.

### E1. PlasticineLab — Huang et al. (2021)

- **Source:** *PlasticineLab: A Soft-Body Manipulation Benchmark with Differentiable Physics*, ICLR 2021. https://arxiv.org/pdf/2104.03311 · Project: http://plasticinelab.csail.mit.edu · `PRIMARY_PAPER` + `OPEN_SOURCE` (abstract verified 2026-10-19)
- **Demonstrates:** a differentiable elastoplastic simulator (DiffTaichi) with 10 soft-body manipulation tasks; gradient-based planning solves many tasks in tens of iterations where RL largely fails — **but gradient methods still fall short on multi-stage, long-horizon tasks**.
- **Does not demonstrate:** perception of deformable state from pixels (state is privileged simulator state, `L4`); no visual state estimation is evaluated.
- **Landing for Clover:** two open problems in one paper — (i) deformable world state from vision alone is essentially unmeasured; (ii) even with perfect state and gradients, long-horizon deformable planning is unsolved. Simulation evidence tier: `EV1` (§23) — not sim2real evidence.

### E2. DiffTaichi — Hu et al. (2020)

- **Source:** *DiffTaichi: Differentiable Programming for Physical Simulation*, ICLR 2020 (bibliographic record via PlasticineLab lineage, verified 2026-10-19). `PRIMARY_PAPER`
- **Landing:** the tooling layer under E1; relevant when Stage 2 needs differentiable-physics falsifiers. **Still missing on this axis:** fluid and granular anchors (SPH/MPM perception-side work) — recorded as an open gap, not filled (§28.22).

---

## 6. Axis F — Evaluation methodology (shortcut resistance, examiner isolation)

**Why this axis:** a world-understanding claim is only as strong as the test that could have refuted it. This axis is the methodological licence for every capability claim in the repository.

### F1. Shortcut learning — Geirhos et al. (2020)

- **Source:** *Shortcut Learning in Deep Neural Networks*, Nature Machine Intelligence 2:665–673, 2020. DOI 10.1038/s42256-020-00257-z · https://arxiv.org/abs/2004.07780 · `PRIMARY_PAPER` (abstract verified 2026-10-19)
- **Demonstrates:** many benchmark successes are decision rules that perform on the test distribution yet fail under modest distribution change; shortcut behaviour appears in biological learners too — it is a property of learning systems, not a DNN quirk.
- **Does not demonstrate:** a complete remedy; it offers benchmarking recommendations, not a certification procedure.
- **Landing for Clover:** mandatory audit shape for any internal result — (1) what is the cheapest cue that solves this test without the claimed capability? (2) does the test include a condition where that cue misleads? (3) is the examiner isolated from the system's inputs (pixels-only discipline)? VoE pairs (Axis B2) are one concrete anti-shortcut instrument. Internal precedent: the frozen CPU-track S0 audit recorded its own TaskSuite as *not pixels-only* (`FALSIFIED + OPEN`) — this axis exists so that class of error is caught by design, not by luck.

---

## 7. What this file changes, and the read queue

1. **Every Stage-1 surface now has at least one primary anchor or an explicitly recorded gap.** Axes A–F map to surfaces 3, 2/5, 1/7, 4, 5, and 11/15 respectively in [`STATUS.md`](STATUS.md).
2. **Full-text read queue (Stage-1 → Stage-2 dossiers):** Battaglia 2013 · Khemakhem 2020 · DROID-SLAM 2021 · Spelke 1992 · PlasticineLab 2021. Each read produces a §26 record in `research/survey/SOURCE_MAP.md` before it may support any durable conclusion.
3. **Open gaps (explicit, §28.22):** adverse-condition observation anchors (Axis D second half); fluid/granular perception anchors (Axis E); a modern identifiability-of-world-models synthesis beyond A2; evaluation-methodology anchors beyond F1 (benchmark leakage / contamination literature).
4. **Next frontier sweep obligation (unchanged):** include at least one *new primary source* per axis above, or state why the axis produced nothing — silence is not coverage.

*Update rule: this is a living root file. New anchors are appended per axis with the same record shape and verification date; superseded entries are marked `SUPERSEDED`, never silently deleted (§15).*

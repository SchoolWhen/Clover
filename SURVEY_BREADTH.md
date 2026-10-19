# SURVEY_BREADTH — Breadth Foundation for Stage-1 Research

**Created:** 2026-10-19 · **Place:** repository root (flat layout, next to [`NEWS.md`](NEWS.md) and [`STATUS.md`](STATUS.md))
**Companion:** [`research/emerging/FRONTIER_SWEEP_2026-10-19.md`](research/emerging/FRONTIER_SWEEP_2026-10-19.md) tracks the *frontier*; this file builds the *breadth* underneath it.

The 2026-10-19 frontier sweep found that recent intake was almost entirely VLA / world-action-model / industry-brain news, with **zero new material on six breadth axes**. Rule adopted there and kept here:

```text
a sweep with frontier but no breadth counts as failed
```

This file records verified anchor sources for those six axes, plus the standing tracking channels that keep both breadth and frontier current. Entries follow the AGENTS §4.4 record shape (problem / demonstrates / does-not-demonstrate / assumptions / counter-hypothesis) in compact form. Anchors were located and bibliographically verified on 2026-10-19; the same evening, six of them were read in full text and recorded into [`research/survey/SOURCE_MAP.md`](research/survey/SOURCE_MAP.md) (marked **FULL READ** below). Remaining entries are abstract/bibliographic level, labelled as such. No entry here is an architecture decision (§4.2, §26).

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

- **Source:** *Planning and acting in partially observable stochastic domains*, Artificial Intelligence 101(1–2):99–134. DOI: https://doi.org/10.1016/S0004-3702(98)00023-X · `PRIMARY_PAPER` · **FULL READ 2026-10-19** (witness algorithm; belief-MDP optimality; finite-memory controller extraction; the paper's own complexity warning — exact polynomial solving in all parameters would imply NP = RP)
- **Problem:** optimal action when the true state is never directly observed and both actions and observations are stochastic.
- **Demonstrates:** belief state (a distribution over world states) is a sufficient statistic for the observation history; exact solution is computationally hard even for small domains.
- **Does not demonstrate:** how to *learn* the model or the belief representation from raw pixels; assumes a given state space and observation model.
- **Landing for Clover:** the belief/licence discipline has a classical formal home — "unobserved ≠ free, unknown is a state" is POMDP orthodoxy, not a Clover invention. Any Clover state claim should name which POMDP assumption it keeps or drops.

### A2. Identifiability of learned latent state — Khemakhem et al. (2020)

- **Source:** *Variational Autoencoders and Nonlinear ICA: A Unifying Framework*, AISTATS 2020, PMLR 108:2207–2217. http://proceedings.mlr.press/v108/khemakhem20a.html · `PRIMARY_PAPER` · **FULL READ 2026-10-19** (main text incl. corrigendum; supplementary proofs not read)
- **Problem:** when is a learned latent representation *the* latent state, rather than one of infinitely many equivalent reparameterisations?
- **Demonstrates:** with an auxiliary variable conditioning the prior (iVAE), the latent model is identifiable up to simple transformations; plain VAEs / unconditional latent models are provably **non-identifiable**. Precision from the full read: identifiability needs the auxiliary variable's λ-differences to span the full space — a *stationary* world in u collapses it; with k = 1 and location-only change, orthogonal transforms remain indistinguishable (the authors' own Proposition 1); and the paper's discrete-observation claim was **retracted in a corrigendum**. Experiments are synthetic sources + fMRI — never real video.
- **Does not demonstrate:** identifiability from raw video alone without auxiliary structure; the auxiliary variable is an added assumption, not a free lunch.
- **Landing for Clover:** pairs with *Identifiable World Models* (arXiv:2610.07028, already tracked in the frontier survey). Together they set the Stage-1 question precisely: *what auxiliary structure (temporal contrast, action, multi-view, intervention) makes a visual world state identifiable, and what equivalence class remains?* Any "learned world state" claim that cannot answer this is incomplete.

---

## 2. Axis B — Human & developmental visual cognition

**Why this axis:** infants solve a version of the mother question from vision with almost no language. Their constraint set — what is present early, what is absent — is evidence about what visual world understanding minimally requires, and the violation-of-expectation paradigm is a ready-made falsification instrument.

### B1. Core knowledge — Spelke et al. (1992)

- **Source:** *Origins of knowledge*, Psychological Review 99(4):605–632. DOI 10.1037/0033-295X.99.4.605 · PubMed: http://www.ncbi.nlm.nih.gov/pubmed/1454901 · `PRIMARY_PAPER` (abstract verified 2026-10-19)
- **Demonstrates:** early infant physical reasoning accords with **continuity** (objects move on connected paths) and **solidity** (no two objects in the same place at the same time).
- **Does not demonstrate — equally important:** early reasoning does **not** accord with **gravity** or **inertia**. The honest reading is a *partial* constraint set, not a full physics engine at birth.
- **Full-read refinement (2026-10-20):** the 1992 full text remains paywalled (abstract-level here), but Spelke (1994), *Initial knowledge: six suggestions*, Cognition 50:431–445, was read in full: the object-domain principles are stated as **cohesion, continuity, contact**; gravity/inertia are excluded with the rationale that initial knowledge captures what is most *true*, not what is most obvious (unsupported objects do not always fall perceptibly, motion is not always smooth); and a task-specificity caveat — 6-month-olds' looking-time inferences follow continuity-not-inertia while their predictive *reaching* extrapolates along the line of motion. Looking knowledge ≠ acting knowledge.
- **Landing for Clover:** continuity + solidity are candidate Stage-1 test constraints (object permanence across occlusion); gravity/inertia must be treated as *learned or absent*, not assumed as priors. This also warns against importing a complete "core knowledge" checklist as an axiom set (§4.1).

### B2. Violation-of-expectation — Baillargeon (1985; Baillargeon & Graber 1987)

- **Source:** Baillargeon, Spelke & Wasserman (1985), *Object permanence in five-month-old infants*, Cognition 20:191–208, DOI 10.1016/0010-0277(85)90008-3; and the tall/short-rabbit screen experiments (Baillargeon & Graber 1987). · `BACKGROUND_REFERENCE` — **primary abstract read 2026-10-20; full text confirmed closed-access** (Semantic Scholar openAccessPdf: CLOSED), so this entry stays abstract-level by evidence, not by omission.
- **Demonstrates:** in the 1985 drawbridge study, 5-month-olds (n=21) looked longer at the impossible event (screen rotating through the space of a hidden box) than at the possible event (screen stopping at the box); a control experiment (n=22, box placed *beside* the screen) rules out a simple rotation-length preference. Infants maintain occluded objects and expectations about them.
- **Does not demonstrate:** the internal representation format; looking time is an expectation signal, not a state readout. The paradigm's interpretation has known critiques (perceptual-novelty confounds), which any borrowing must record.
- **Landing for Clover:** VoE is a transferable *evaluation* design — possible vs impossible event pairs with matched perceptual novelty — directly usable as a shortcut-resistant test shape for object permanence (see Axis F).

### B3. Intuitive physics engine — Battaglia, Hamrick & Tenenbaum (2013)

- **Source:** *Simulation as an engine of physical scene understanding*, PNAS 110(45):18327–18332. DOI 10.1073/pnas.1306572110 · Open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC3831455/ · `PRIMARY_PAPER` · **FULL READ 2026-10-19**
- **Demonstrates:** a single probabilistic-simulation model fits human judgments across five psychophysical tasks (stability, support, tearing, containment…), including human illusions and biases — humans appear to run *approximate, noisy* simulation, not exact physics. Full-read specifics: uncertainty lives in the *input* (geometry σ ≈ 20% of a block's shorter side, latent forces φ, mass ratio μ); human trial variance implies only ~3–7 stochastic samples; and the scene inputs were sampled from a distribution **based on ground truth** — no visual front end was built (listed as future work). A feature-heuristic alternative fared consistently worse.
- **Does not demonstrate:** that the brain literally contains a physics engine of this form, nor that simulation is the only route; it is a computational-level fit to adult judgments.
- **Landing for Clover:** a competing hypothesis to keep visible (§4.4): world understanding as *approximate simulation over an inferred scene* vs Clover-style *queryable state with licences*. The two make different predictions under occlusion and counterfactual queries — a discriminating test belongs in Stage 2.

---

## 3. Axis C — Classical geometry, SLAM & SfM

**Why this axis:** the geometry tradition is the strongest existing answer to "state from vision alone" and the baseline any learned world state must beat or honestly differ from. Its failure records are as valuable as its successes.

### C1. DROID-SLAM — Teed & Deng (2021)

- **Source:** *DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras*, NeurIPS 2021. https://arxiv.org/pdf/2108.10869 · Code: https://github.com/princeton-vl/DROID-SLAM · `PRIMARY_PAPER` + `OPEN_SOURCE` · **FULL READ 2026-10-19**
- **Demonstrates:** learned recurrent updates + a **differentiable dense bundle-adjustment layer** achieve large accuracy gains and far fewer catastrophic failures than prior systems, generalising across camera setups. Full-read specifics: zero tracking failures on TartanAir/EuRoC/TUM-RGBD; EuRoC mono ATE 2.2 cm (43% better than ORB-SLAM3); and the load-bearing ablation — training *without* the DBA layer in the loop makes the system unstable, so the geometric optimiser must be inside learning, not bolted on at inference.
- **Does not demonstrate:** object-level or physical world state; output is camera pose + per-pixel depth. Notably, the learned front-end did **not** replace geometric optimisation — the state is still produced by bundle adjustment.
- **Landing for Clover:** evidence that "end-to-end learned" claims in this space quietly keep a geometric solver at the core. Any Clover geometric claim must state its relation to BA-style global consistency explicitly. Training provenance is `L4`, full stop: a single model trained entirely on synthetic TartanAir video with ground-truth pose/depth supervision (pose + flow losses); stereo/RGB-D enter only at test time through the DBA objective. Deployment input being RGB does not make it vision-alone learning (§5). Pinhole intrinsics are assumed known (`V1`).

### C2. ORB-SLAM3 — Campos et al. (2021)

- **Source:** *ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multimap SLAM*, IEEE Transactions on Robotics 37(6):1874–1890, 2021. https://arxiv.org/abs/2007.11898 · `PRIMARY_PAPER` / `OPEN_SOURCE` · **FULL READ 2026-10-20**
- **Demonstrates:** the mature classical stack (feature tracking, local mapping, loop closure, map merging via the Atlas multi-map system, visual-inertial fusion) and its documented operating envelope. Full-read specifics: stereo-inertial EuRoC ATE ≈ 3.5 cm RMS, multi-session operation 2.6–3.2× better than VINS-Mono; the authors' own accuracy thesis is that exploiting short/mid/long-term **and multi-map** data association "overpowers" front-end choices.
- **Does not demonstrate:** robustness in low-texture, dynamic, or badly lit scenes — the classical failure triad that motivated learned methods. The full read names the frontier precisely: **low texture is the stated main failure case** (descriptor matching loses to photometric LK tracking on near-featureless dark sequences); dynamic objects exist only as outliers to reject; pure rotation blocks monocular depth; IMU initialisation needs gravity/roll-pitch excitation (a car on flat ground may never initialise); long outdoor runs drift 10–70 m in inertial parameters; far/sky points are discarded by hand rules. Calibrated intrinsics are a required input (`V1`-adjacent); monocular scale is unobservable.
- **Landing for Clover:** the reference failure catalogue for Axis D: classical geometry fails exactly where image formation stops cooperating. A vision-alone brain must degrade *licences*, not silently hallucinate state, in the same conditions.

---

## 4. Axis D — Image formation & adverse visual conditions (observation physics)

**Why this axis:** §6 — world-state ambiguity ≠ image-formation ambiguity ≠ sensor corruption. What the pixels *cannot* contain is set by optics and acquisition before any model runs.

### D1. Brightness constancy & the aperture problem — Horn & Schunck (1981)

- **Source:** *Determining Optical Flow*, Artificial Intelligence 17:185–203, 1981. Reprint locator: http://dev.ipol.im/git/?p=coco/ipol_phs.git;a=blob_plain;f=doc/ipol_horn_schunck_draft.pdf;h=dc931ccba98cafe3742ffeb819d161ac361e3cbb;hb=575a90230da4c38969a1674748b29c9bb5fedf70 · `PRIMARY_PAPER` (bibliographic verified 2026-10-19)
- **Demonstrates:** under brightness constancy, one pixel yields one equation for two unknowns (the aperture problem): local image evidence *provably underdetermines* motion; their smoothness prior is an added assumption that fills the gap — visibly, the field's first explicit "licence" for inferred state.
- **Does not demonstrate:** validity under illumination change, specularity, transparency or occlusion boundaries — exactly where brightness constancy breaks.
- **Landing for Clover:** the canonical template for every observation-physics entry: name the image-formation assumption, name what it licenses, name where it dies. Full assumption checklist lives in [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md).

### D2. Adverse-condition boundary — Bijelic et al. (2020) — *counter-anchor, not vision evidence*

- **Source:** *Seeing Through Fog Without Seeing Fog: Deep Multimodal Sensor Fusion in Unseen Adverse Weather*, CVPR 2020, pp. 11682–11692. https://openaccess.thecvf.com/content_CVPR_2020/html/Bijelic_Seeing_Through_Fog_Without_Seeing_Fog_Deep_Multimodal_Sensor_Fusion_CVPR_2020_paper.html · arXiv:1902.08913 (preprint under an earlier title) · `PRIMARY_PAPER` (bibliographic + abstract verified 2026-10-19)
- **Demonstrates:** on a 100k-label multimodal dataset (>10,000 km of northern-Europe driving plus a controlled fog chamber), RGB object detection degrades severely in fog/snow/rain while lidar, radar and gated NIR degrade *asymmetrically*; an entropy-driven fusion network trained on clean data survives adverse weather by leaning on the non-RGB sensors.
- **Does not demonstrate:** anything about vision-alone understanding — the paper is multimodal **by design**; its point is precisely that the camera stream fails. The gated camera is active sensing (backscatter gating), not passive vision.
- **Landing for Clover:** this is the honest boundary marker for Axis D. It documents *which* observation regimes defeat RGB-only perception and how other sensors compensate. Any Clover claim scoped to adverse conditions must state its observation-physics regime; this paper must never be cited as vision-alone support.

### D3. Low light, passive RGB — Chen, Chen, Xu & Koltun (2018)

- **Source:** *Learning to See in the Dark*, CVPR 2018. https://arxiv.org/abs/1805.01934 · `PRIMARY_PAPER` (verified 2026-10-20)
- **Demonstrates:** a fully-convolutional network operating directly on raw sensor data replaces the traditional ISP pipeline and restores clean, colourful images from extreme low-light (<0.1 lux) short exposures; introduces the SID dataset (5,094 raw short-exposure images paired with long-exposure references).
- **Does not demonstrate:** world-state estimation — this is image restoration. And the restoration is *supervised by a privileged pairing* (long-exposure references): it shows the photon-noise floor can be learned around with paired data, not that low-light RGB yields reliable state for free.
- **Landing for Clover:** the first genuinely passive-RGB adverse-condition anchor. Low-light claims inherit its condition: restoration quality is bought with paired supervision; without pairs, the noise floor is the honest limit.

### D4. Low-light detection benchmark — Loh & Chan (2019)

- **Source:** *Getting to know low-light images with the Exclusively Dark dataset*, Computer Vision and Image Understanding 178:30–42, 2019. DOI 10.1016/j.cviu.2018.10.010 · `PRIMARY_PAPER` (verified 2026-10-20)
- **Demonstrates:** ExDark — 7,363 low-light images captured in visible light only, 10 lighting conditions, bounding-box annotations over 12 object classes — and the finding that low-light corruption reaches far deeper into hand-crafted and learned features than "illumination invariance" fixes.
- **Landing for Clover:** passive-side corroboration of D2's lesson: degraded RGB corrupts features non-superficially, so adverse-condition capability claims need examiners that go beyond invariance assumptions. **Still open on this axis:** passive anchors for specular/transparent materials and motion blur (§28.22).

---

## 5. Axis E — Deformable, fluid & granular dynamics

**Why this axis:** rigid-body benchmarks dominate the frontier intake; household worlds are cloth, dough, liquid, cables and piles. A brain claim scoped to rigid scenes must say so.

### E1. PlasticineLab — Huang et al. (2021)

- **Source:** *PlasticineLab: A Soft-Body Manipulation Benchmark with Differentiable Physics*, ICLR 2021. https://arxiv.org/pdf/2104.03311 · Project: http://plasticinelab.csail.mit.edu · `PRIMARY_PAPER` + `OPEN_SOURCE` · **FULL READ 2026-10-19**
- **Demonstrates:** a differentiable elastoplastic simulator (DiffTaichi) with 10 soft-body manipulation tasks; gradient-based planning solves many tasks in tens of iterations where RL largely fails — **but gradient methods still fall short on multi-stage, long-horizon tasks**. Full-read specifics: agents observe a privileged downsampled particle-landmark state, never pixels; gradient winners are *open-loop* trajectory optimisations assuming full environment knowledge (e.g. RollingPin 0.93, Assembly 0.90 soft-IoU) while SAC/TD3 score ~0 on several tasks; the multi-stage failure mechanism is named precisely — gradients vanish at detachment/reattachment (Pinch, Writer).
- **Does not demonstrate:** perception of deformable state from pixels (state is privileged simulator state, `L4`); no visual state estimation is evaluated.
- **Landing for Clover:** two open problems in one paper — (i) deformable world state from vision alone is essentially unmeasured; (ii) even with perfect state and gradients, long-horizon deformable planning is unsolved. Simulation evidence tier: `EV1` (§23) — not sim2real evidence.

### E2. DiffTaichi — Hu et al. (2020)

- **Source:** *DiffTaichi: Differentiable Programming for Physical Simulation*, ICLR 2020 (bibliographic record via PlasticineLab lineage, verified 2026-10-19). `PRIMARY_PAPER`
- **Landing:** the tooling layer under E1; relevant when Stage 2 needs differentiable-physics falsifiers.

### E3. Learned fluid / granular / deformable dynamics — Sanchez-Gonzalez et al. (2020)

- **Source:** *Learning to Simulate Complex Physics with Graph Networks* (GNS), ICML 2020, PMLR 119:8459–8468. https://arxiv.org/abs/2002.09405 · `PRIMARY_PAPER` (bibliographic + abstract verified 2026-10-19)
- **Demonstrates:** a graph-network simulator over particle state generalises across fluids, rigid solids and deformable materials (Water/Sand/Goop domains from SPH/MPM simulators), rolling out thousands of timesteps with ~10× more particles at test time than in training.
- **Does not demonstrate:** perception — inputs are privileged particle positions, velocities and material properties (`L4`); there are no pixels anywhere in the paper.
- **Landing for Clover:** the dynamics-side anchor for this axis, and it sharpens the open problem by contrast: learned *dynamics from state* is demonstrated (E1, E3); *state from vision alone* for deformable/fluid/granular matter remains unmeasured. That perception-side gap stays **open** (§28.22).

### E4. Particle dynamics with real-world control — Li et al. (2019, DPI-Net)

- **Source:** *Learning Particle Dynamics for Manipulating Rigid Bodies, Deformable Objects, and Fluids*, ICLR 2019. https://arxiv.org/abs/1810.01566 · `PRIMARY_PAPER` (bibliographic + provenance verified 2026-10-20)
- **Demonstrates:** a learned graph-network particle simulator (dynamic graphs, hierarchical propagation) spanning fluids, rigid bodies and deformables; its dynamics plus MPC control real tasks (fluid shaking, foam/rice-grip moulding), beating PPO baselines on sample efficiency.
- **State provenance — the decisive audit:** `MIXED`, leaning privileged. Training is entirely in simulation against simulator ground truth; for the real-world task, particles are *randomly sampled inside a mesh reconstructed from a depth camera via TSDF fusion* — geometry arrives from a classical reconstruction pipeline, never from a learned pixel estimator; the dynamics model never consumes an image.
- **Landing for Clover:** sibling dynamics anchor to E3, and the provenance verdict is its value: even the flagship "learning particle dynamics" system gets its real-world state from depth-camera reconstruction. The perception half remains unbuilt here.

### E5. Perception-side deformable state — Shi et al. (2022, RoboCraft)

- **Source:** *RoboCraft: Learning to See, Simulate, and Shape Elasto-Plastic Objects with Graph Networks*, RSS 2022. DOI 10.15607/RSS.2022.XVIII.008 · https://www.roboticsproceedings.org/rss18/p008.html · `PRIMARY_PAPER` (bibliographic + provenance verified 2026-10-20)
- **Demonstrates:** a full perception→dynamics→planning loop for elasto-plastic objects: particles are sampled from an RGB-D point cloud / reconstructed mesh; the GNN dynamics model is trained **directly from raw visual data** (10 minutes of real-world interaction, distribution-based losses, no particle-to-particle temporal correspondence); MPC then shapes plasticine into target shapes — including unseen ones — at untrained-human level.
- **State provenance:** `PIXELS`, with two honest caveats: input is RGB-**D** (depth participates — outside the RGB-only `V0–V2` protocol), and particle sampling leans on classical mesh reconstruction (alpha shapes / ball pivoting) with shape-prior refinements, not an end-to-end learned pixel→state estimator.
- **Landing for Clover:** the first true perception-side anchor on this axis — the closest existing demonstration of the capability the mother question demands for deformable matter. Its boundary defines the successor's target: same loop, from RGB alone, without classical reconstruction in the middle. Fluid/granular perception-side anchors remain **open** (§28.22).

---

## 6. Axis F — Evaluation methodology (shortcut resistance, examiner isolation)

**Why this axis:** a world-understanding claim is only as strong as the test that could have refuted it. This axis is the methodological licence for every capability claim in the repository.

### F1. Shortcut learning — Geirhos et al. (2020)

- **Source:** *Shortcut Learning in Deep Neural Networks*, Nature Machine Intelligence 2:665–673, 2020. DOI 10.1038/s42256-020-00257-z · https://arxiv.org/abs/2004.07780 · `PRIMARY_PAPER` · **FULL READ 2026-10-19** (adds two cautions: a usable o.o.d. test must satisfy three non-trivial conditions — clear shift, a well-defined intended solution, current models actually struggling — and good o.o.d. tests *decay* as models improve, cf. Winograd schemas; the proposed "Morgan's Canon for ML" is a methodological norm, not a result)
- **Demonstrates:** many benchmark successes are decision rules that perform on the test distribution yet fail under modest distribution change; shortcut behaviour appears in biological learners too — it is a property of learning systems, not a DNN quirk.
- **Does not demonstrate:** a complete remedy; it offers benchmarking recommendations, not a certification procedure.
- **Landing for Clover:** mandatory audit shape for any internal result — (1) what is the cheapest cue that solves this test without the claimed capability? (2) does the test include a condition where that cue misleads? (3) is the examiner isolated from the system's inputs (pixels-only discipline)? VoE pairs (Axis B2) are one concrete anti-shortcut instrument. Internal precedent: the frozen CPU-track S0 audit recorded its own TaskSuite as *not pixels-only* (`FALSIFIED + OPEN`) — this axis exists so that class of error is caught by design, not by luck.

---

## 7. What this file changes, and the read queue

1. **Every Stage-1 surface now has at least one primary anchor or an explicitly recorded gap.** Axes A–F map to surfaces 3, 2/5, 1/7, 4, 5, and 11/15 respectively in [`STATUS.md`](STATUS.md).
2. **Full-text read queue — status 2026-10-20:** DONE and recorded in `research/survey/SOURCE_MAP.md`: Battaglia 2013 · Khemakhem 2020 · Kaelbling 1998 · DROID-SLAM 2021 · PlasticineLab 2021 · Geirhos 2020 · ORB-SLAM3 2021 · Spelke 1994 (companion to B1). Closed at abstract level by access, not by choice: Spelke 1992 and Baillargeon 1985 full texts are paywalled/closed (verified 2026-10-20); their entries carry the abstract-level label permanently until access changes.
3. **Open gaps (explicit, §28.22):** passive anchors for specular/transparent materials and motion blur (Axis D; low light now anchored by D3/D4, fog boundary by D2); fluid/granular *perception-side* anchors (Axis E — E5 covers elasto-plastic from RGB-D; DPI-Net E4 audited as privileged-state); RGB-alone (no depth) deformable state estimation; a modern identifiability-of-world-models synthesis beyond A2; evaluation-methodology anchors beyond F1 (benchmark leakage / contamination literature).
4. **Next frontier sweep obligation (unchanged):** include at least one *new primary source* per axis above, or state why the axis produced nothing — silence is not coverage.

*Update rule: this is a living root file. New anchors are appended per axis with the same record shape and verification date; superseded entries are marked `SUPERSEDED`, never silently deleted (§15).*

# Clover Understanding Battery — Working Design

**Status:** OPEN / design document  
**Purpose:** define what a future comprehensive evaluation would need to measure without turning any one benchmark into the project objective.

## 1. Principle

The battery must answer:

> **Does the system form and use a coherent world understanding from visual evidence?**

A future scientific result should combine controlled diagnostics, open-world visual data and embodied tasks.

## 2. Capability families

### U1 — Existence and observability

Questions:

- Is something present?
- Was it observed?
- Is it currently unobserved rather than absent?
- Is free space actually established or merely unseen?

Failure to distinguish these states is a fundamental worldview error.

### U2 — Identity and permanence

Questions:

- Is this the same entity after viewpoint change?
- Does the entity persist through occlusion?
- Can it reappear after leaving the field of view?
- Can the system handle split/merge/deformation without arbitrary ID continuity?

Potential instruments: EgoTracks, SAM 2-style tracking baselines, custom occlusion/reappearance sequences.

### U3 — Spatial structure

Questions:

- Where is an entity relative to the camera/world/other entities?
- Is A inside/on/behind/near B?
- What space is traversable?
- Does geometry remain coherent across views?

Potential instruments: geometry/reconstruction benchmarks, controlled multi-view tasks.

### U4 — Temporal structure and dynamics

Questions:

- What changed?
- What is moving, and how?
- Which state is stable?
- What happens next?

Potential instruments: Perception Test, Something-Something V2, controlled trajectory tasks.

### U5 — Intuitive physics

Questions:

- Can an object disappear without cause?
- Can solids interpenetrate?
- Is a trajectory physically continuous?
- Which events are possible/impossible?

Potential instrument: IntPhys 2.

### U6 — Causality and counterfactuals

Questions:

- Why did the state change?
- What would happen under a different intervention?
- What action would produce a requested world-state change?

Potential instruments: CausalVQA plus future intervention twins in simulation/robotics.

### U7 — Memory and revision

Questions:

- Can a fact survive outside the current context window?
- Can later evidence correct an earlier world belief?
- Can stable knowledge be consolidated without retaining every frame?

Potential instruments: Ego4D long-history subsets + custom long-duration visual tasks.

### U8 — Generalization

Hold out:

- objects;
- scenes;
- compositions;
- viewpoints;
- dynamics;
- robot environments.

The key is not only OOD accuracy but whether the system knows when the new case invalidates an existing assumption.

### U9 — Active perception

Task form:

Two or more world hypotheses remain indistinguishable from the current view. The robot must choose a visual action that resolves the ambiguity before committing to a downstream action.

This directly tests whether uncertainty can drive information-seeking behavior.

### U10 — Decision usefulness

Compare downstream agents with and without the candidate worldview while controlling the rest of the stack as much as possible.

Measure:

- task success;
- unnecessary actions;
- replanning;
- recovery from world changes;
- search/compute cost;
- unsafe/unjustified commitments.

## 3. Anti-shortcut requirements

Every core diagnostic should consider:

- minimal pairs;
- background-only probe;
- static-frame probe;
- temporal shuffle;
- crop/scene-ID leakage;
- near-duplicate audit;
- language-only baseline when language is involved.

## 4. Pure-vision protocol labels

Results should identify the sensory protocol explicitly:

- **V0:** monocular RGB + temporal ordering;
- **V1:** RGB + camera calibration;
- **V2:** calibrated multi-camera RGB;
- **V3:** embodied active vision where actions determine future views.

Do not collapse these into one 'vision-only' number.

## 5. Evidence levels

A claim can have different evidence levels:

1. **unit/mechanism evidence**;
2. **controlled scientific diagnostic**;
3. **public benchmark evidence**;
4. **real-world visual transfer**;
5. **embodied task evidence**;
6. **unseen real-environment evidence**.

A high score at a lower level does not imply the higher levels.

## 6. Current status

This battery is a map for future evaluation. The current project phase is not yet running the complete battery. Its immediate purpose is to stop research from collapsing onto one convenient metric.

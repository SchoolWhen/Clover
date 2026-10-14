# Authority Chain

**Status:** target engineering principle derived from current Clover research prototypes.

The intended direction is:

```text
visual evidence
→ world state / world assertions
→ public queries
→ optional authority/provenance envelope
→ decision premises
→ action selection
→ execution trace
→ new visual evidence
```

## Principles

1. **One world authority** — caches and derived views must not silently become competing truth stores.
2. **No downstream private-truth bypass** — Decision should not gain special access unavailable through the Worldview contract.
3. **Observation re-enters through perception** — execution feedback should not directly write world truth.
4. **Unknown is not free/absent** — lack of observation is an epistemic condition.
5. **Provenance is not confidence** — evidence lineage and uncertainty have different semantics.

The exact licence mechanism remains a hypothesis; these authority principles are broader than any current implementation.

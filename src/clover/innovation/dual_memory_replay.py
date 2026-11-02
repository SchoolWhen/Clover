"""Dual-memory replay with asymmetric gating (H1/H4/H5/H6; sequence 4.6).

Working state (fast, current) + persistent evidence cache (slow).
Write policy implements the sequence-2.3 asymmetric gating criterion:
  - persistent write requires label OBSERVED **and** confidence >=
    tau_write (high threshold);
  - generative completion / prediction never writes directly: it goes
    to the pending-verification queue;
  - on REFUTED evidence, a cascade rollback downgrades every assertion
    that (transitively) depends on the refuted one (H6 proof-carrying
    audit chain makes this mechanical);
  - conflict between working state and new evidence triggers a replay
    request listing the conflicting assertions (H5).
"""
from __future__ import annotations

from ..core import Assertion, EpistemicLabel


class DualMemoryReplay:
    def __init__(self, tau_write: float = 0.8, tau_suspend: float = 0.4):
        self.tau_write = tau_write
        self.tau_suspend = tau_suspend
        self.working: dict[str, Assertion] = {}
        self.persistent: dict[str, Assertion] = {}
        self.pending: list[Assertion] = []
        self.rollback_log: list[str] = []

    def observe(self, a: Assertion) -> str:
        """Returns the route taken: 'persistent' | 'working' | 'pending' | 'rejected'."""
        key = f"{a.subject}|{a.predicate}"
        existing = self.working.get(key)
        if existing is not None and existing.value != a.value and a.label == EpistemicLabel.OBSERVED:
            self._refute(existing)   # new observation contradicts stored belief
        if a.label == EpistemicLabel.OBSERVED and a.confidence >= self.tau_write:
            self.working[key] = a
            self.persistent[a.id] = a
            return "persistent"
        if a.label in (EpistemicLabel.PREDICTED, EpistemicLabel.ASSUMED) :
            self.pending.append(a)   # completion/prediction: never persistent directly
            return "pending"
        if a.confidence >= self.tau_suspend:
            self.working[key] = a
            return "working"
        return "rejected"

    def _refute(self, old: Assertion) -> None:
        old_key_assert = old.downgrade(EpistemicLabel.REFUTED)
        self.rollback_log.append(f"refuted: {old.id}")
        # cascade: downgrade dependents recorded in the persistent store
        queue = [old.id]
        while queue:
            cur = queue.pop()
            for aid, stored in list(self.persistent.items()):
                if cur in stored.depends_on and stored.label != EpistemicLabel.REFUTED:
                    self.persistent[aid] = stored.downgrade(EpistemicLabel.AMBIGUOUS)
                    self.rollback_log.append(f"cascade downgrade: {aid}")
                    queue.append(aid)

    def conflicts_for_replay(self) -> list[str]:
        """Assertions whose working value disagrees with a pending prediction
        (conflict-triggered replay candidates, H5)."""
        out = []
        for p in self.pending:
            key = f"{p.subject}|{p.predicate}"
            w = self.working.get(key)
            if w is not None and w.value != p.value:
                out.append(key)
        return out

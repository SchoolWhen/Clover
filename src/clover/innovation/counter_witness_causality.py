"""Counter-witness causality (H7; sequence 4.6).

Given a dependency graph over latent/physical variables and a set of
observed anomalies (nodes whose predicted value disagrees with
observation), locate the minimal set of 'broken' upstream variables
whose failure explains all anomalies -- the counter-witness set.
Greedy exact cover for small graphs; the output is a falsifiable
localisation claim, not an explanation narrative.
"""
from __future__ import annotations


class CounterWitnessCausality:
    def __init__(self, edges: list[tuple[str, str]]):
        """edges: (cause, effect)."""
        self.children: dict[str, set[str]] = {}
        self.nodes: set[str] = set()
        for c, e in edges:
            self.children.setdefault(c, set()).add(e)
            self.nodes.update((c, e))

    def reachable(self, node: str) -> set[str]:
        seen, stack = set(), [node]
        while stack:
            cur = stack.pop()
            for ch in self.children.get(cur, ()):  # descendants
                if ch not in seen:
                    seen.add(ch); stack.append(ch)
        return seen

    def explain(self, anomalies: set[str]) -> dict:
        """Minimal greedy set of upstream nodes covering all anomalies."""
        remaining = set(anomalies)
        witnesses: list[str] = []
        while remaining:
            best, best_cover = None, set()
            for n in self.nodes:
                cover = (self.reachable(n) | {n}) & remaining
                if len(cover) > len(best_cover):
                    best, best_cover = n, cover
            if not best_cover:
                break
            witnesses.append(best)
            remaining -= best_cover
        return {"witnesses": witnesses,
                "unexplained": sorted(remaining),
                "explained_fraction": 1.0 - len(remaining) / max(len(anomalies), 1)}

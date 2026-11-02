"""Unit tests for the clover codebase (unittest; pytest-compatible)."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from clover.benchmarks import (make_episode, make_pair, run_suite,
                               score_episode, score_predictions)
from clover.core import Assertion, EpistemicLabel, Frame
from clover.harness import (BudgetExceeded, EndToEndProfiler,
                            FairBudgetController, ResourceAuditor)
from clover.innovation import (AnytimeComputeScheduler, ComputeTask,
                               CounterWitnessCausality, DualMemoryReplay,
                               SparseEventIR, TransitionAffordance,
                               select_evidence_action)
from clover.models import PHASE_A, ModelUnavailable, SAM3, YOLO26n
from clover.probes import (FrozenLinearProbe, NonMarkovianityDetector,
                           ProbeBudget, ProbeCapacityError, ReversibilityProbe,
                           StateAliasingAuditor, ZeroShotKNNProbe)


def frame(v=0):
    return Frame(np.full((8, 8, 3), v, dtype=np.uint8), 0.0)


class TestCore(unittest.TestCase):
    def test_epistemic_gate(self):
        self.assertTrue(EpistemicLabel.OBSERVED.persistable)
        self.assertFalse(EpistemicLabel.ASSUMED.persistable)
        self.assertFalse(EpistemicLabel.PREDICTED.persistable)


class TestHarness(unittest.TestCase):
    def test_profiler_percentiles(self):
        p = EndToEndProfiler()
        for _ in range(3):
            with p.run():
                with p.segment("forward"):
                    pass
        rep = p.report()
        self.assertIn("total", rep)
        self.assertGreaterEqual(rep["total"]["p99_ms"], rep["total"]["p50_ms"])

    def test_byte_budget_drops_oldest_and_reports(self):
        c = FairBudgetController(max_state_bytes=200)
        kept = c.apply_byte_budget([frame(), frame(), frame()])
        self.assertEqual(len(kept), 1)
        self.assertTrue(c.events)

    def test_latency_strict_raises(self):
        c = FairBudgetController(deadline_ms=0.001, strict=True)
        with self.assertRaises(BudgetExceeded):
            c.run_with_deadline(lambda: sum(range(100000)))

    def test_joule_unavailable_without_sampler(self):
        self.assertEqual(ResourceAuditor().joule_per_frame(), "UNAVAILABLE")
        self.assertAlmostEqual(
            ResourceAuditor().joule_per_frame([10.0, 10.0], [0.1, 0.1]), 1.0)


class TestModels(unittest.TestCase):
    def test_phase_a_families(self):
        self.assertEqual(len(PHASE_A), 10)

    def test_int8_validation(self):
        YOLO26n(precision="int8")
        with self.assertRaises(ValueError):
            SAM3(precision="int8")

    def test_load_fails_closed(self):
        with self.assertRaises(ModelUnavailable):
            YOLO26n().load()

    def test_dry_run_is_stamped(self):
        out = YOLO26n().dry_run_infer([frame()])
        self.assertEqual(out["mode"], "SYNTHETIC_DRY_RUN")


class TestProbes(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(0)
        self.X = rng.normal(size=(200, 8))
        self.y = (self.X[:, 0] + self.X[:, 1] > 0).astype(int)

    def test_linear_probe_learns(self):
        p = FrozenLinearProbe().fit(self.X, self.y)
        self.assertGreater(p.score(self.X, self.y), 0.9)

    def test_capacity_cap_enforced(self):
        with self.assertRaises(ProbeCapacityError):
            FrozenLinearProbe(ProbeBudget(max_effective_dof=4)).fit(self.X, self.y)

    def test_knn_probe(self):
        self.assertGreater(ZeroShotKNNProbe().fit(self.X, self.y).score(self.X, self.y), 0.8)

    def test_nonmarkovianity_detects_planted_leak(self):
        rng = np.random.default_rng(1)
        z = rng.normal(size=(300, 2)); a = rng.integers(0, 2, size=(300, 1))
        hist = rng.normal(size=(300, 2))
        y_next = (hist[:, 0] > 0).astype(float)
        self.assertTrue(NonMarkovianityDetector().leak(z, a, hist, y_next)["leak_detected"])

    def test_aliasing_and_reversibility(self):
        aud = StateAliasingAuditor().audit(
            [(np.zeros(3), np.full(3, 0.01), "A1")], np.array([1.0, 1.1]))
        self.assertEqual(aud["collapse_rate"], 1.0)
        rev = ReversibilityProbe().recoverability(self.X, self.X[:, :2])
        self.assertGreater(rev["r2_mean"], 0.99)


class TestBenchmarks(unittest.TestCase):
    def test_minimal_pairs_identical_before_contact(self):
        for kind in ("friction_boundary", "restitution_cavity", "mass_eccentricity"):
            p = make_pair(kind, seed=2)
            self.assertTrue(np.array_equal(p.frames_a[:p.contact_index],
                                           p.frames_b[:p.contact_index]))

    def test_minimal_pair_scoring(self):
        p = make_pair("friction_boundary", seed=0)
        self.assertTrue(score_predictions(p, p.hidden_a, p.hidden_b)["ranking_correct"])
        self.assertTrue(score_predictions(p, None, None)["refused"])

    def test_occlusion_scorer_and_fp_penalty(self):
        ep = make_episode("unknown_vs_unobserved")
        good = score_episode(ep, {"bottom_right_region": EpistemicLabel.UNOBSERVED,
                                  "target": EpistemicLabel.OBSERVED})
        self.assertEqual(good["accuracy"], 1.0)
        bad = score_episode(ep, {"bottom_right_region": EpistemicLabel.OBSERVED,
                                 "target": EpistemicLabel.OBSERVED},
                            {"bottom_right_region": 0.95})
        self.assertEqual(bad["fp_writeback_count"], 1)

    def test_anti_shortcut_runs(self):
        ds = [(np.zeros((5, 8, 8, 3), dtype=np.uint8), 1)]
        out = run_suite(lambda fr: 1, ds)
        self.assertEqual(out["clean"], 1.0)


class TestInnovation(unittest.TestCase):
    def test_asymmetric_gating(self):
        m = DualMemoryReplay()
        obs = Assertion("cup", "pos", "left", EpistemicLabel.OBSERVED, 0.9)
        self.assertEqual(m.observe(obs), "persistent")
        pred = Assertion("cup", "pos", "right", EpistemicLabel.PREDICTED, 0.99)
        self.assertEqual(m.observe(pred), "pending")  # completion never persists directly
        self.assertIn("cup|pos", m.conflicts_for_replay())

    def test_refutation_cascade(self):
        m = DualMemoryReplay()
        a = Assertion("cup", "pos", "left", EpistemicLabel.OBSERVED, 0.9)
        m.observe(a)
        dep = Assertion("table", "state", "set", EpistemicLabel.INFERRED, 0.7,
                        depends_on=[a.id])
        m.persistent[dep.id] = dep
        m.observe(Assertion("cup", "pos", "right", EpistemicLabel.OBSERVED, 0.95))
        self.assertTrue(any("cascade" in s for s in m.rollback_log))

    def test_sparse_event_ir(self):
        frames = np.zeros((10, 16, 16, 3), dtype=np.uint8)
        frames[5:, 4:8, 4:8] = 200
        out = SparseEventIR().encode(frames)
        self.assertGreaterEqual(out["stats"]["n_events"], 2)
        self.assertLess(out["stats"]["sparsity_ratio"], 0.01)

    def test_counter_witness(self):
        cw = CounterWitnessCausality([("valve", "pressure"), ("pressure", "flow")])
        out = cw.explain({"flow"})
        self.assertEqual(out["explained_fraction"], 1.0)

    def test_scheduler_anytime_and_shedding(self):
        sch = AnytimeComputeScheduler(frame_budget_ms=10)
        plan = sch.plan([ComputeTask("a", 8, 1.0, 0.5), ComputeTask("b", 8, 0.1, 0.0)])
        self.assertTrue(plan["anytime_guarantee"])
        self.assertEqual(plan["execute_in_order"], ["a"])

    def test_affordance_and_evidence_policy(self):
        ta = TransitionAffordance()
        d = ta.delta_w({"g": 0.0, "t": 0.0}, {"g": 1.0, "t": 0.5}, {"g"})
        self.assertGreater(d["goal_fraction"], 0.5)
        pick = select_evidence_action([
            {"name": "look", "expected_gain": 1, "cost": 1},
            {"name": "smash", "expected_gain": 10, "cost": 1, "irreversible": True}])
        self.assertEqual(pick["name"], "look")


if __name__ == "__main__":
    unittest.main()

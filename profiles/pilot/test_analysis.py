# SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck.
"""Tests for the pilot analysis. Run: python3 -m unittest discover -s profiles -p "test_*.py" """
import random
import unittest

import analysis as a


class Statistics(unittest.TestCase):
    def test_pearson_of_a_perfect_line_is_1(self):
        self.assertAlmostEqual(a.pearson([1, 2, 3, 4], [2, 4, 6, 8]), 1.0)
        self.assertAlmostEqual(a.pearson([1, 2, 3, 4], [8, 6, 4, 2]), -1.0)

    def test_pearson_with_no_variation_is_none(self):
        self.assertIsNone(a.pearson([1, 2, 3], [5, 5, 5]))

    def test_alpha_of_identical_items_is_1(self):
        rows = [[v, v, v] for v in (1, 2, 3, 4, 5)]
        self.assertAlmostEqual(a.cronbach_alpha(rows), 1.0)

    def test_alpha_matches_a_hand_calculation(self):
        # Item variances 2.5, 2.5 and 1.0. Variance of the totals 15.5. alpha = 3/2 * (1 - 6/15.5).
        rows = [[1, 2, 3], [2, 1, 3], [3, 4, 4], [4, 3, 5], [5, 5, 5]]
        self.assertAlmostEqual(a.cronbach_alpha(rows), 1.5 * (1 - 6 / 15.5))

    def test_alpha_of_unrelated_items_is_near_zero(self):
        rng = random.Random(1)
        rows = [[rng.randint(1, 5) for _ in range(12)] for _ in range(2000)]
        self.assertLess(abs(a.cronbach_alpha(rows)), 0.1)

    def test_item_rest_correlation_finds_the_item_that_does_not_fit(self):
        rng = random.Random(2)
        rows = []
        for _ in range(500):
            trait = rng.gauss(0, 1)
            good = [trait + rng.gauss(0, 0.5) for _ in range(5)]
            rows.append(good + [rng.gauss(0, 1)])
        correlations = a.item_rest_correlations(rows)
        self.assertTrue(all(c > 0.6 for c in correlations[:5]))
        self.assertLess(abs(correlations[5]), 0.15)

    def test_cohens_d(self):
        self.assertAlmostEqual(a.cohens_d([2, 3, 4], [1, 2, 3]), 1.0)


class Analyse(unittest.TestCase):
    BANK = {"A1": ("Voice", "+"), "A2": ("Voice", "-"), "A3": ("Voice", "+"), "B1": ("Warmth", "+"), "B2": ("Warmth", "-")}

    def test_data_with_no_respondents_is_a_clear_error(self):
        with self.assertRaisesRegex(ValueError, "fewer than two"):
            a.analyse(self.BANK, [])

    def data(self, n=200, seed=3):
        rng = random.Random(seed)
        clamp = lambda x: str(min(5, max(1, round(x))))  # noqa: E731
        rows = []
        for i in range(n):
            voice, warmth = rng.gauss(3, 1), rng.gauss(3, 1)
            rows.append({"respondent": str(i), "site": "north" if i % 2 else "south",
                         "A1": clamp(voice + rng.gauss(0, 0.5)), "A2": clamp(6 - voice + rng.gauss(0, 0.5)),
                         "A3": clamp(voice + rng.gauss(0, 0.5)),
                         "B1": clamp(warmth + rng.gauss(0, 0.5)), "B2": clamp(6 - warmth + rng.gauss(0, 0.5))})
        return rows

    def test_report_for_simulated_data(self):
        report = a.analyse(self.BANK, self.data(), retest=self.data(), group="site")
        voice = report["scales"]["Voice"]
        self.assertEqual((voice["items"], voice["n"], voice["retest_n"]), (3, 200, 200))
        self.assertGreater(voice["alpha"], 0.7)  # the reversed item is keyed correctly
        self.assertEqual(voice["retest_r"], 1.0)
        self.assertEqual(set(voice["groups"]), {"north", "south"})
        self.assertLess(abs(voice["group_d"]["north - south"]), 0.4)
        self.assertLess(abs(report["correlations"]["Voice x Warmth"]), 0.3)

    def test_respondent_with_too_many_missing_answers_is_left_out(self):
        data = self.data(50)
        data[0]["A1"] = data[0]["A2"] = ""
        report = a.analyse(self.BANK, data)
        self.assertEqual(report["scales"]["Voice"]["n"], 49)
        self.assertEqual(report["scales"]["Warmth"]["n"], 50)

    def test_norms_have_the_form_that_the_scoring_code_reads(self):
        norms = a.norms_from(a.analyse(self.BANK, self.data()))
        self.assertEqual(set(norms["Voice"]), {"mean", "sd", "reliability"})


class Simulation(unittest.TestCase):
    def test_analysis_finds_the_structure_of_the_invented_data(self):
        import os
        import simulate_pilot
        from ol_scoring import load_item_bank
        here = os.path.dirname(os.path.abspath(__file__))
        bank = load_item_bank(os.path.join(here, "..", "behaviour-profile", "item-bank.csv"))
        rows = [{k: str(v) for k, v in row.items()} for row in simulate_pilot.simulate(bank, 300, 1)]
        report = a.analyse(bank, rows, group="group")
        self.assertEqual(set(report["scales"]), {"Voice", "Warmth", "Method", "Exploration"})
        for entry in report["scales"].values():
            self.assertGreater(entry["alpha"], 0.8)
            self.assertTrue(all(r > 0.3 for r in entry["item_rest"].values()))
        self.assertTrue(all(abs(r) < 0.2 for r in report["correlations"].values()))


if __name__ == "__main__":
    unittest.main()

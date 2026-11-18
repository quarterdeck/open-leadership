# SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck.
"""Tests for ol_scoring. Run: python3 -m unittest discover -s profiles -p "test_*.py" """
import csv
import os
import unittest

import ol_scoring as s

PROFILES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BANKS = {name: os.path.join(PROFILES, name, "item-bank.csv") for name in ("behaviour-profile", "preference-profile")}


def bank_of(n=12, scale="Voice"):
    half = n // 2
    return {f"X{i:02d}": (scale, "+" if i < half else "-") for i in range(n)}


class KeyedValue(unittest.TestCase):
    def test_plus_keyed_item_keeps_the_response(self):
        self.assertEqual(s.keyed_value(4, "+"), 4)

    def test_minus_keyed_item_is_reversed(self):
        self.assertEqual([s.keyed_value(r, "-") for r in (1, 2, 3, 4, 5)], [5, 4, 3, 2, 1])

    def test_response_out_of_range_is_an_error(self):
        for bad in (0, 6):
            with self.assertRaises(ValueError):
                s.keyed_value(bad, "+")


class ScoreProfile(unittest.TestCase):
    def test_all_answers_at_the_high_end_give_100(self):
        bank = bank_of()
        responses = {i: (5 if k == "+" else 1) for i, (_, k) in bank.items()}
        self.assertEqual(s.score_profile(bank, responses)["Voice"]["score"], 100.0)

    def test_all_answers_at_the_low_end_give_0(self):
        bank = bank_of()
        responses = {i: (1 if k == "+" else 5) for i, (_, k) in bank.items()}
        self.assertEqual(s.score_profile(bank, responses)["Voice"]["score"], 0.0)

    def test_the_same_answer_to_each_item_gives_50(self):
        # Half of the items are reversed, so a person who gives one answer to all items is in the middle.
        bank = bank_of()
        for answer in (1, 3, 5):
            result = s.score_profile(bank, {i: answer for i in bank})["Voice"]
            self.assertEqual(result["score"], 50.0)
            self.assertEqual(result["position"], "middle")

    def test_two_missing_answers_of_twelve_still_give_a_score(self):
        bank = bank_of()
        responses = {i: 4 if k == "+" else 2 for i, (_, k) in bank.items()}
        responses["X00"] = None
        del responses["X11"]
        result = s.score_profile(bank, responses)["Voice"]
        self.assertEqual(result["score"], 75.0)
        self.assertEqual(result["answered"], 10)

    def test_three_missing_answers_of_twelve_give_no_score(self):
        bank = bank_of()
        responses = {i: 4 for i in list(bank)[:9]}
        result = s.score_profile(bank, responses)["Voice"]
        self.assertIsNone(result["score"])
        self.assertIsNone(result["position"])

    def test_response_for_an_unknown_item_is_an_error(self):
        with self.assertRaises(ValueError):
            s.score_profile(bank_of(), {"ZZ99": 3})

    def test_scales_are_scored_separately(self):
        bank = {"A1": ("Voice", "+"), "A2": ("Voice", "-"), "B1": ("Warmth", "+"), "B2": ("Warmth", "-")}
        result = s.score_profile(bank, {"A1": 5, "A2": 1, "B1": 1, "B2": 5})
        self.assertEqual((result["Voice"]["score"], result["Warmth"]["score"]), (100.0, 0.0))


class Band(unittest.TestCase):
    def test_band_is_never_narrower_than_the_minimum(self):
        bank = bank_of()
        result = s.score_profile(bank, {i: 4 if k == "+" else 2 for i, (_, k) in bank.items()})["Voice"]
        self.assertEqual((result["low"], result["high"]), (70.0, 80.0))
        self.assertEqual(result["position"], "higher")

    def test_band_is_wider_when_the_answers_disagree(self):
        bank = bank_of()
        steady = s.score_profile(bank, {i: 4 if k == "+" else 2 for i, (_, k) in bank.items()})["Voice"]
        mixed = s.score_profile(bank, {i: (5 if n % 2 else 3) if k == "+" else (1 if n % 2 else 3)
                                       for n, (i, (_, k)) in enumerate(bank.items())})["Voice"]
        self.assertEqual(mixed["score"], steady["score"])
        self.assertGreater(mixed["high"] - mixed["low"], steady["high"] - steady["low"])

    def test_band_stays_inside_0_to_100(self):
        bank = bank_of()
        result = s.score_profile(bank, {i: (5 if k == "+" else 1) for i, (_, k) in bank.items()})["Voice"]
        self.assertEqual((result["low"], result["high"]), (95.0, 100.0))

    def test_band_that_crosses_a_cut_is_middle(self):
        self.assertEqual(s.position(55, 70), "middle")
        self.assertEqual(s.position(30, 45), "middle")
        self.assertEqual(s.position(61, 80), "higher")
        self.assertEqual(s.position(10, 39), "lower")


class Norms(unittest.TestCase):
    NORMS = {"Voice": {"mean": 3.4, "sd": 0.6, "reliability": 0.84}}

    def test_person_at_the_norm_mean_is_at_the_50th_percentile(self):
        result = s.score_scale([3.4] * 12, 12, self.NORMS["Voice"])
        self.assertEqual(result["score"], 50.0)

    def test_person_one_sd_above_the_mean_is_near_the_84th_percentile(self):
        result = s.score_scale([4.0] * 12, 12, self.NORMS["Voice"])
        self.assertAlmostEqual(result["score"], 84.1, places=1)

    def test_band_uses_the_standard_error_of_measurement(self):
        result = s.score_scale([3.4] * 12, 12, self.NORMS["Voice"])
        sem = 0.6 * (1 - 0.84) ** 0.5
        self.assertAlmostEqual(result["high"], s.normal_cdf(1.96 * sem / 0.6) * 100, places=1)
        self.assertAlmostEqual(result["low"] + result["high"], 100.0, places=1)


class TeamSummary(unittest.TestCase):
    def results(self, scores):
        return [{"Voice": {"score": x}} for x in scores]

    def test_summary_of_a_team(self):
        summary = s.team_summary(self.results([20.0, 50.0, 80.0, 60.0, 40.0]))["Voice"]
        self.assertEqual(summary, {"n": 5, "lowest": 20.0, "median": 50.0, "highest": 80.0, "spread": 60.0})

    def test_fewer_than_five_scores_give_no_summary(self):
        self.assertEqual(s.team_summary(self.results([20.0, None, 80.0, 50.0, 60.0]))["Voice"], {"n": 4})


class LoadItemBank(unittest.TestCase):
    def test_item_that_is_in_the_bank_two_times_is_an_error(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            f.write("id,order,text,scale,keyed,source\nA1,1,x,Voice,+,s\nA1,2,y,Voice,-,s\n")
        with self.assertRaises(ValueError):
            s.load_item_bank(f.name)
        os.unlink(f.name)


class ItemBanks(unittest.TestCase):
    """The published item banks obey the rules in the technical manuals."""

    def rows(self, name):
        with open(BANKS[name], newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def test_each_scale_has_twelve_items_or_more(self):
        expected = {"behaviour-profile": {"Voice", "Warmth", "Method", "Exploration"},
                    "preference-profile": {"Company", "Focus", "Decisions", "Planning", "Pressure"}}
        for name, scales in expected.items():
            counts = {}
            for row in self.rows(name):
                counts[row["scale"]] = counts.get(row["scale"], 0) + 1
            self.assertEqual(set(counts), scales)
            self.assertTrue(all(n >= 12 for n in counts.values()), counts)

    def test_each_scale_has_items_keyed_in_both_directions(self):
        for name in BANKS:
            keys = {}
            for row in self.rows(name):
                keys.setdefault(row["scale"], set()).add(row["keyed"])
            self.assertTrue(all(k == {"+", "-"} for k in keys.values()), keys)

    def test_no_item_text_is_used_twice_in_the_two_profiles(self):
        texts = [row["text"] for name in BANKS for row in self.rows(name)]
        self.assertEqual(len(texts), len(set(texts)))

    def test_ids_and_order_are_unique_and_complete(self):
        for name in BANKS:
            rows = self.rows(name)
            self.assertEqual(len({r["id"] for r in rows}), len(rows))
            self.assertEqual([int(r["order"]) for r in rows], list(range(1, len(rows) + 1)))

    def test_the_item_banks_load_and_score(self):
        for name in BANKS:
            bank = s.load_item_bank(BANKS[name])
            result = s.score_profile(bank, {i: 3 for i in bank})
            self.assertTrue(all(r["score"] == 50.0 for r in result.values()))


if __name__ == "__main__":
    unittest.main()

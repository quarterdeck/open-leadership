#!/usr/bin/env python3
# SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck.
"""Write test-vectors.json from the scoring code. Run it after a change to the scoring or to an item bank.

    python3 profiles/scoring/make_test_vectors.py
"""
import csv
import json
import os

import ol_scoring as s

HERE = os.path.dirname(os.path.abspath(__file__))


def cases_for(profile):
    folder = os.path.join(HERE, "..", profile)
    bank = s.load_item_bank(os.path.join(folder, "item-bank.csv"))
    with open(os.path.join(folder, "item-bank.csv"), newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    ids = [row["id"] for row in rows]
    first_scale = rows[0]["scale"]
    in_first = [row["id"] for row in rows if row["scale"] == first_scale]
    two_missing = {i: (n * 3) % 5 + 1 for n, i in enumerate(ids)}
    two_missing[in_first[0]] = two_missing[in_first[1]] = None
    three_missing = dict(two_missing)
    three_missing[in_first[2]] = None
    cases = {
        "each answer is 3": {i: 3 for i in ids},
        "each answer is 5": {i: 5 for i in ids},
        "mixed answers": {i: (n * 7) % 5 + 1 for n, i in enumerate(ids)},
        "the example file": s.load_responses(os.path.join(folder, "scoring", "example-responses.csv")),
        f"two answers of {first_scale} are missing": two_missing,
        f"three answers of {first_scale} are missing": three_missing,
    }
    if profile == "preference-profile":
        cases["the Pressure items are not answered"] = {
            i: (None if bank[i][0] == "Pressure" else (n * 7) % 5 + 1) for n, i in enumerate(ids)}
    return [{"profile": profile, "case": name, "responses": responses, "expected": s.score_profile(bank, responses)}
            for name, responses in cases.items()]


def main():
    cases = cases_for("behaviour-profile") + cases_for("preference-profile")
    team = [c["expected"] for c in cases if c["profile"] == "behaviour-profile"][:5]
    document = {
        "note": "Test vectors for an implementation of the Open Leadership profile scoring. ol_scoring.py made the "
                "expected values. Provisional scoring, with no norms. Compare scores with a tolerance of 0.1.",
        "licence": "MIT. Copyright (c) Quarterdeck.",
        "cases": cases,
        "team": {"note": "team_summary of the first five behaviour-profile cases", "expected": s.team_summary(team)},
    }
    with open(os.path.join(HERE, "test-vectors.json"), "w", encoding="utf-8") as f:
        json.dump(document, f, indent=1)


if __name__ == "__main__":
    main()

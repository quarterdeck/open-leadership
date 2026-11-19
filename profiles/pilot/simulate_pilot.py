#!/usr/bin/env python3
# SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck.
"""Write an invented pilot data set, to try the analysis scripts before real data exists.

    python3 profiles/pilot/simulate_pilot.py ITEM_BANK.csv OUTPUT.csv [--n 500] [--seed 1]

Each invented respondent has one value for each scale. Each answer is that value,
in the direction of the item, plus noise. The scales are independent. The data
says nothing about real people. Do not use it for norms.
"""
import argparse
import csv
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scoring"))
from ol_scoring import load_item_bank  # noqa: E402


def simulate(bank, n, seed):
    """Return a list of rows in the form that analysis.py reads."""
    rng = random.Random(seed)
    scales = sorted({scale for scale, _ in bank.values()})
    rows = []
    for number in range(1, n + 1):
        trait = {scale: rng.gauss(0, 1) for scale in scales}
        row = {"respondent": f"R{number:04d}", "group": rng.choice(["a", "b"])}
        for item_id, (scale, keyed) in bank.items():
            direction = 1 if keyed == "+" else -1
            answer = round(3 + direction * 0.9 * trait[scale] + rng.gauss(0, 0.9))
            row[item_id] = min(5, max(1, answer))
        rows.append(row)
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write an invented pilot data set.")
    parser.add_argument("item_bank")
    parser.add_argument("output")
    parser.add_argument("--n", type=int, default=500)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args(argv)
    rows = simulate(load_item_bank(args.item_bank), args.n, args.seed)
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()

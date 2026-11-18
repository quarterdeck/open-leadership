#!/usr/bin/env python3
# SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck.
"""Scoring for the OL Behaviour Profile and the OL Preference Profile.

Both profiles use the same rules. The item bank of a profile is the scoring key.

    python3 profiles/scoring/ol_scoring.py ITEM_BANK.csv RESPONSES.csv [NORMS.json]

RESPONSES.csv has the columns "id" and "response". A response is a whole number
from 1 (very inaccurate) to 5 (very accurate). An empty response is a missing answer.
The result is JSON on standard output.

The method is in the technical manual of each profile. Python 3.9 or later. No
packages are necessary.
"""
import csv
import json
import math
import sys

MIN_RESPONSE = 1
MAX_RESPONSE = 5
MAX_MISSING_SHARE = 1 / 6  # 2 items of 12
MIN_BAND_HALF_WIDTH = 5.0
BAND_Z = 1.96
LOWER_CUT = 40.0
UPPER_CUT = 60.0
MIN_TEAM_SIZE = 5


def load_item_bank(path):
    """Return {item id: (scale, keyed)} from an item bank file."""
    with open(path, newline="", encoding="utf-8") as f:
        bank = {}
        for row in csv.DictReader(f):
                        if row["id"] in bank:
                raise ValueError(f"Item {row['id']} is in the item bank more than one time")
            if row["keyed"] not in ("+", "-"):
                raise ValueError(f"Item {row['id']}: keyed must be + or -")
            bank[row["id"]] = (row["scale"], row["keyed"])
    return bank


def load_responses(path):
    """Return {item id: response or None} from a responses file."""
    with open(path, newline="", encoding="utf-8") as f:
        return {row["id"]: (int(row["response"]) if row["response"].strip() else None) for row in csv.DictReader(f)}


def keyed_value(response, keyed):
    """Return the response in the direction of the scale."""
    if not MIN_RESPONSE <= response <= MAX_RESPONSE:
        raise ValueError(f"Response {response} is not from {MIN_RESPONSE} to {MAX_RESPONSE}")
    return response if keyed == "+" else MIN_RESPONSE + MAX_RESPONSE - response


def to_hundred(mean):
    """Convert a mean item value (1 to 5) to the 0 to 100 scale."""
    return (mean - MIN_RESPONSE) / (MAX_RESPONSE - MIN_RESPONSE) * 100


def position(low, high):
    """Name the position of a band: lower, middle or higher.

    A band that crosses a cut is "middle", because the result does not show
    clearly on which side the person is.
    """
    if high < LOWER_CUT:
        return "lower"
    if low > UPPER_CUT:
        return "higher"
    return "middle"


def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def score_scale(values, n_items, norm=None):
    """Score one scale from the keyed values of the answered items.

    Without norms, the score is the mean item value on a 0 to 100 scale, and the
    band comes from the spread of the person's own answers. With norms (mean,
    sd and reliability of the mean item value in a reference group), the score
    is the percentile in that group, and the band comes from the standard error
    of measurement.
    """
    missing = n_items - len(values)
    if not values or missing / n_items > MAX_MISSING_SHARE:
        return {"score": None, "low": None, "high": None, "position": None, "answered": len(values), "items": n_items}
    mean = sum(values) / len(values)
    if norm:
        sem = norm["sd"] * math.sqrt(1 - norm["reliability"])
        score, low, high = (normal_cdf((m - norm["mean"]) / norm["sd"]) * 100 for m in (mean, mean - BAND_Z * sem, mean + BAND_Z * sem))
    else:
        score = to_hundred(mean)
        if len(values) > 1:
            variance = sum((v - mean) ** 2 for v in values) / (len(values) - 1)
            half = BAND_Z * math.sqrt(variance / len(values)) / (MAX_RESPONSE - MIN_RESPONSE) * 100
        else:
            half = 100.0
        half = max(half, MIN_BAND_HALF_WIDTH)
        low, high = max(0.0, score - half), min(100.0, score + half)
    return {"score": round(score, 1), "low": round(low, 1), "high": round(high, 1), "position": position(low, high),
            "answered": len(values), "items": n_items}


def score_profile(bank, responses, norms=None):
    """Return {scale: result} for one person."""
    unknown = set(responses) - set(bank)
    if unknown:
        raise ValueError(f"Responses for items that are not in the item bank: {sorted(unknown)}")
    values, counts = {}, {}
    for item_id, (scale, keyed) in bank.items():
        counts[scale] = counts.get(scale, 0) + 1
        values.setdefault(scale, [])
        response = responses.get(item_id)
        if response is not None:
            values[scale].append(keyed_value(response, keyed))
    return {scale: score_scale(values[scale], counts[scale], (norms or {}).get(scale)) for scale in counts}


def team_summary(results):
    """Summarise the results of a team: {scale: {n, lowest, median, highest, spread}}.

    `results` is a list of the outputs of score_profile. A scale with fewer than
    five scores gets no summary, so that one person's result cannot be worked out.
    """
    summary = {}
    for scale in results[0] if results else []:
        scores = sorted(r[scale]["score"] for r in results if r[scale]["score"] is not None)
        if len(scores) < MIN_TEAM_SIZE:
            summary[scale] = {"n": len(scores)}
            continue
        mid = len(scores) // 2
        median = scores[mid] if len(scores) % 2 else (scores[mid - 1] + scores[mid]) / 2
        summary[scale] = {"n": len(scores), "lowest": scores[0], "median": round(median, 1), "highest": scores[-1],
                          "spread": round(scores[-1] - scores[0], 1)}
    return summary


def main(argv):
    if len(argv) not in (3, 4):
        print(__doc__, file=sys.stderr)
        return 2
    norms = None
    if len(argv) == 4:
        with open(argv[3], encoding="utf-8") as f:
            norms = json.load(f)
    result = score_profile(load_item_bank(argv[1]), load_responses(argv[2]), norms)
    json.dump(result, sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

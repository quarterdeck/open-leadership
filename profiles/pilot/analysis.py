#!/usr/bin/env python3
# SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck.
"""Analysis of pilot data for the OL Behaviour Profile and the OL Preference Profile.

    python3 profiles/pilot/analysis.py ITEM_BANK.csv PILOT.csv [--retest RETEST.csv]
                                       [--group COLUMN] [--norms NORMS.json]

PILOT.csv has one row for each respondent: the column "respondent", one column
for each item id with a response from 1 to 5 (empty if missing), and optional
group columns. RETEST.csv has the same form, for the respondents who answered a
second time. --norms writes the norms file that ol_scoring.py reads.

The report is JSON on standard output. For each scale it gives the number of
respondents, the mean, the standard deviation, Cronbach's alpha, the corrected
item-total correlation of each item, the test-retest correlation and the
difference between groups. It also gives the correlations between scales.

This script does not do factor analysis or coefficient omega. The plan for
those is in data-collection-plan.md. Python 3.9 or later. No packages are
necessary.
"""
import argparse
import csv
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scoring"))
from ol_scoring import MAX_MISSING_SHARE, keyed_value, load_item_bank  # noqa: E402


def mean(xs):
    return sum(xs) / len(xs)


def variance(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1)


def sd(xs):
    return math.sqrt(variance(xs))


def pearson(xs, ys):
    """Pearson correlation of two lists of the same length. None if one list has no variation."""
    mx, my = mean(xs), mean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    if sxx == 0 or syy == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / math.sqrt(sxx * syy)


def cronbach_alpha(rows):
    """Cronbach's alpha. `rows` is a list of respondents, each a list of keyed item values with no missing value."""
    k = len(rows[0])
    total_variance = variance([sum(r) for r in rows])
    if k < 2 or total_variance == 0:
        return None
    item_variances = sum(variance([r[i] for r in rows]) for i in range(k))
    return k / (k - 1) * (1 - item_variances / total_variance)


def item_rest_correlations(rows):
    """Correlation of each item with the sum of the other items of the scale."""
    k = len(rows[0])
    return [pearson([r[i] for r in rows], [sum(r) - r[i] for r in rows]) for i in range(k)]


def cohens_d(a, b):
    """Standardised difference between the means of two groups."""
    pooled = math.sqrt(((len(a) - 1) * variance(a) + (len(b) - 1) * variance(b)) / (len(a) + len(b) - 2))
    return (mean(a) - mean(b)) / pooled if pooled else None


def load_data(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def keyed_rows(data, items, bank):
    """Return {respondent: [keyed value or None for each item]}."""
    out = {}
    for row in data:
        out[row["respondent"]] = [keyed_value(int(row[i]), bank[i][1]) if row.get(i, "").strip() else None for i in items]
    return out


def scale_means(keyed):
    """Mean item value for each respondent who answered enough items of the scale."""
    out = {}
    for respondent, values in keyed.items():
        answered = [v for v in values if v is not None]
        if answered and (len(values) - len(answered)) / len(values) <= MAX_MISSING_SHARE:
            out[respondent] = mean(answered)
    return out


def r3(x):
    return None if x is None else round(x, 3)


def analyse(bank, data, retest=None, group=None):
    scales = {}
    for item_id, (scale, _) in bank.items():
        scales.setdefault(scale, []).append(item_id)
    report, means = {"scales": {}, "correlations": {}}, {}
    for scale, items in scales.items():
        keyed = keyed_rows(data, items, bank)
        complete = [v for v in keyed.values() if None not in v]
        means[scale] = scale_means(keyed)
        values = list(means[scale].values())
        entry = {"items": len(items), "n": len(values), "n_complete": len(complete),
                 "mean": r3(mean(values)), "sd": r3(sd(values)),
                 "alpha": r3(cronbach_alpha(complete)),
                 "item_rest": dict(zip(items, map(r3, item_rest_correlations(complete))))}
        if retest is not None:
            second = scale_means(keyed_rows(retest, items, bank))
            both = [r for r in second if r in means[scale]]
            entry["retest_n"] = len(both)
            entry["retest_r"] = r3(pearson([means[scale][r] for r in both], [second[r] for r in both])) if len(both) > 2 else None
        if group:
            by_group = {}
            for row in data:
                if row["respondent"] in means[scale] and row.get(group, "").strip():
                    by_group.setdefault(row[group], []).append(means[scale][row["respondent"]])
            names = sorted(by_group)
            entry["groups"] = {g: {"n": len(v), "mean": r3(mean(v))} for g, v in by_group.items()}
            entry["group_d"] = {f"{a} - {b}": r3(cohens_d(by_group[a], by_group[b]))
                                for i, a in enumerate(names) for b in names[i + 1:]
                                if len(by_group[a]) > 1 and len(by_group[b]) > 1}
        report["scales"][scale] = entry
    names = list(scales)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            both = [r for r in means[a] if r in means[b]]
            report["correlations"][f"{a} x {b}"] = r3(pearson([means[a][r] for r in both], [means[b][r] for r in both]))
    return report


def norms_from(report):
        """Norms for ol_scoring.py. Alpha is the estimate of reliability. A scale with no alpha gets no norms."""
    return {scale: {"mean": e["mean"], "sd": e["sd"], "reliability": e["alpha"]}
            for scale, e in report["scales"].items() if e["alpha"] is not None and e["sd"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Analyse pilot data of an OL profile.")
    parser.add_argument("item_bank")
    parser.add_argument("pilot")
    parser.add_argument("--retest")
    parser.add_argument("--group")
    parser.add_argument("--norms")
    args = parser.parse_args(argv)
    report = analyse(load_item_bank(args.item_bank), load_data(args.pilot),
                     load_data(args.retest) if args.retest else None, args.group)
    if args.norms:
        with open(args.norms, "w", encoding="utf-8") as f:
            json.dump(norms_from(report), f, indent=2)
    json.dump(report, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()

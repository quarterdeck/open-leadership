<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->

# OL Preference Profile: scoring

The scoring code is shared by both profiles: [`../../scoring/ol_scoring.py`](../../scoring/ol_scoring.py).
The item bank is the scoring key. The method is in section 6 of the
[technical manual](../technical-manual.md).

Run it from the root of the repository:

```
python3 profiles/scoring/ol_scoring.py \
    profiles/preference-profile/item-bank.csv \
    profiles/preference-profile/scoring/example-responses.csv
```

[`example-responses.csv`](example-responses.csv) is an invented set of answers. The result for
each scale has:

| Field | Meaning |
|---|---|
| `score` | 0 to 100. `null` if too many answers are missing |
| `low`, `high` | The band of uncertainty |
| `position` | `lower`, `middle` or `higher` |
| `answered`, `items` | The number of items answered, and the number in the scale |

The position names the side of the scale:

| Scale | `lower` | `middle` | `higher` |
|---|---|---|---|
| Company | Alone | Balanced | With others |
| Focus | Practical | Balanced | Conceptual |
| Decisions | By criteria | Balanced | By people |
| Planning | Flexible | Balanced | Planned |
| Pressure | Steady | Balanced | Alert |

The Pressure scale is optional. If its items are empty or are not in the responses file, its
`score` is `null` and the other scales are scored as usual.

After the pilot, a third argument gives a norms file (`norms.json`), and the score is then a
percentile.

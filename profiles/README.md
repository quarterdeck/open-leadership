<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->

# The Open Leadership profiles

Version 0.1.0 (draft, before the pilot).

Open Leadership has two questionnaires that help people to talk about how they work.

| Profile | Question it answers | Scores | Items | Time |
|---|---|---|---|---|
| [OL Behaviour Profile](behaviour-profile/technical-manual.md) | How do I tend to act with people and tasks at work? | Voice, Warmth, Method, Exploration | 48 | About 8 minutes |
| [OL Preference Profile](preference-profile/technical-manual.md) | In which conditions do I do my best work? | Company, Focus, Decisions, Planning, Pressure | 60 | About 10 minutes |

## What you must know before you use them

- **They are for development and self-awareness.** They are not validated for recruitment,
  selection, promotion, pay or any other decision about a person. Do not use them for those
  purposes.
- **They are not tested yet.** No pilot has been done. There are no norms, and the reliability
  and validity of the scores are not known. Each result is provisional. The
  [pilot plan](pilot/data-collection-plan.md) says how the evidence will be collected.
- **A score is a position on a line.** There are no types, no colours and no categories of
  person. Each score has a band that shows its uncertainty.
- **They describe tendencies and preferences.** They do not measure ability, intelligence,
  health or values. A result is the start of a conversation, and the person can disagree with it.
- **Taking part is voluntary**, and the person owns their result. See
  [data protection](data-protection.md).

## How the two profiles differ

The behaviour profile describes what other people see a person do. The preference profile
describes what a person likes and needs. The two can differ: a person can prefer to work alone
and still speak up readily in a meeting.

Both use the same five-point scale and the same scoring code. Both take their items from the
International Personality Item Pool, which is in the public domain. No item is in both
profiles. Both draw on the same areas of personality research, so some scores will go together.
The pilot will measure how much. If two scores measure the same thing, one will be removed.

## Files

| File | Content |
|---|---|
| `behaviour-profile/`, `preference-profile/` | For each profile: `technical-manual.md`, `item-bank.csv`, `scoring/`, `reports/` and `facilitator-guide.md` |
| [`scoring/ol_scoring.py`](scoring/ol_scoring.py) | The scoring code for both profiles, with tests |
| [`pilot/data-collection-plan.md`](pilot/data-collection-plan.md) | The plan for the pilot |
| [`pilot/analysis.py`](pilot/analysis.py) | The analysis code for the pilot, with tests |
| [`data-protection.md`](data-protection.md) | The rules for personal data |

Run the tests from the root of the repository:

```
python3 -m unittest discover -s profiles/scoring -p "test_*.py"
python3 -m unittest discover -s profiles/pilot -p "test_*.py"
```

## Independent

Open Leadership wrote these profiles. They are independent of all commercial profiling tools,
and they use no items, scoring keys, models, names, graphics or report text from any of them.

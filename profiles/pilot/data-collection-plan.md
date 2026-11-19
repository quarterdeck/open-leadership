<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->

# Pilot: data-collection plan

Version 0.1.0 (draft). Nobody has collected data yet.

The pilot gives the first evidence about the two profiles: are the scores reliable, do the
items fit their scales, and are the scores fair across groups. It also gives the first norms.

## Sample

| Rule | Value |
|---|---|
| People | Adults of 18 or more who work in the UK, employed or self-employed |
| Size | 300 complete responses as a minimum. The target is 500 or more |
| Second response | 100 or more people answer again after 2 to 8 weeks |
| Spread | No one employer gives more than 20% of the sample. No one sector gives more than 30%. People with and without management responsibility are both present, each with 100 or more |

Recruit through employers in more than one sector, through open invitations, and through
training providers. Record how each person was recruited. A sample of volunteers is not
representative of UK working adults, and the technical manuals will say so.

## What each person does

1. Reads the notice (see [data protection](../data-protection.md)) and agrees.
2. Answers both profiles in one session: 108 items, about 20 minutes. Half of the people
   answer the behaviour profile first, and half answer the preference profile first.
3. Answers optional group questions, each with "prefer not to say": age group (18 to 29, 30
   to 44, 45 to 59, 60 or more), sex, management responsibility (yes or no), sector (broad
   list), and whether English is a first language.
4. Chooses whether to give a contact for the second response. The contact is stored apart
   from the answers and is deleted after the second response.
5. Gets their own provisional result.

No name, employer name or email address is stored with the answers. Until the contact for the
second response is deleted, the data is personal data and is protected as such.

## Data files

One row for each person. The analysis code reads this form.

| Column | Content |
|---|---|
| `respondent` | A random code |
| `BP01` to `BP48`, `PP01` to `PP60` | The response to each item, 1 to 5, or empty |
| group columns | For example `age_group`, `sex`, `manager`, `sector`, `english_first` |

Remove a response before analysis if the person answered in less than 4 minutes, gave the same
answer to 30 items in sequence, or left more than 10% of the items empty. Report how many were
removed and why.

## Analysis

`analysis.py` in this folder does rows 1 to 4 and row 6 of the table. Run it one time for
each profile:

```
python3 profiles/pilot/analysis.py profiles/behaviour-profile/item-bank.csv pilot.csv \
    --retest retest.csv --group sex --norms profiles/behaviour-profile/scoring/norms.json
```

`factor_analysis.R` does row 5:

```
Rscript profiles/pilot/factor_analysis.R profiles/behaviour-profile/item-bank.csv pilot.csv
```

`simulate_pilot.py` writes an invented data set, so that you can try both scripts before real
data exists. Both scripts were run on invented data only. The invented data says nothing about
real people.

```
python3 profiles/pilot/simulate_pilot.py profiles/behaviour-profile/item-bank.csv invented.csv
```

| Question | Method | What we look for |
|---|---|---|
| Is each score consistent? | Cronbach's alpha | 0.70 or more is adequate, 0.80 or more is good. These guide values follow the test review model of the European Federation of Psychologists' Associations |
| Does each item fit its scale? | Corrected item-total correlation | 0.30 or more. An item below 0.20 is a candidate for removal |
| Is each score stable? | Correlation of first and second response | 0.70 or more |
| Are the scores fair across groups? | Standardised difference between group means | A difference of more than 0.5 needs an explanation. Then a test of each item for different functioning across groups |
| Do the items form the intended scales? | Confirmatory factor analysis for ordered responses, and coefficient omega | Each item loads on its own scale. The fit is acceptable. `factor_analysis.R` does this. It needs R and the package lavaan |
| Do the two profiles measure different things? | Correlations between all nine scores | A correlation of more than 0.70 between two scores means that one of them is a candidate for removal |
| Do the scores relate to other measures as expected? | Correlations with a public-domain five-factor measure that a part of the sample also answers | The pattern that the technical manuals predict |

## Decisions after the pilot

- Remove or replace an item that does not fit. Keep 10 items or more in each scale. A scale needs answers to five sixths of its items
  for a score.
- Remove or merge a scale that is not reliable or that repeats another.
- Publish the results in the technical manuals, which includes the results that are not good.
- Publish the anonymous data set in this repository if no person can be identified from it.
- Write the norms file. Until then, the reports use the provisional scoring.

## Ethics

- The rules in [data protection](../data-protection.md) apply.
- A person can stop at any time, and their answers are then deleted.
- The organisation that runs the pilot gets an ethics review from a person or a group that is
  independent of the project, and records the result.

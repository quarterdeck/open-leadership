<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->

# Software specification for the profiles

Version 0.1.0 (draft).

This document tells a developer, or an AI agent, how to build software that gives the OL
Behaviour Profile and the OL Preference Profile to people. It states what the software must
do. It does not state how to build it: you choose the language, the framework and the hosting.

The words "must", "must not" and "can" are exact. "Must" is a requirement. "Can" is permitted.

## 1. What you build

An application in which:

1. a person reads a notice, agrees, and answers a questionnaire
2. the application scores the answers
3. the person gets an individual report
4. if five or more people agree, a facilitator gets a team report.

Both profiles use the same rules. Build one engine and load each profile as data.

Read these files first. They are the source of the rules, and this document does not repeat
all of their text.

| File | What it gives you |
|---|---|
| [`behaviour-profile/item-bank.csv`](behaviour-profile/item-bank.csv), [`preference-profile/item-bank.csv`](preference-profile/item-bank.csv) | The items and the scoring key |
| [`scoring/ol_scoring.py`](scoring/ol_scoring.py) | The reference implementation of the scoring |
| [`scoring/test-vectors.json`](scoring/test-vectors.json) | Answers and the expected results, to prove that your scoring is correct |
| [`behaviour-profile/reports/`](behaviour-profile/reports/individual-report.md), [`preference-profile/reports/`](preference-profile/reports/individual-report.md) | The report text |
| [`data-protection.md`](data-protection.md) | The data protection rules and the notice |
| The two technical manuals | The method and its limits |

## 2. What the software must never do

These rules come from the purpose of the profiles. They are requirements.

- It must not show a type, a letter code, a colour for a person, a wheel, a circle or
  quadrants. A result is a mark and a band on a straight line.
- It must not join the scores into one label for a person or for a team.
- It must not rank people, and it must not sort people into groups by score.
- It must not give a result to a line manager, to HR or to any other person without the
  agreement of the person who answered.
- It must not offer a feature for recruitment, selection, promotion, pay, redundancy or
  discipline. It must not export results to a system that has such a purpose.
- It must not use words from medicine or psychology that suggest a diagnosis.
- It must not claim that the profiles are validated, accredited or approved.
- It must not change the wording of an item, the response labels or the scoring.

## 3. Data model

These are the records that the application needs. Names are examples.

| Record | Fields | Notes |
|---|---|---|
| Profile | id, name, version of the item bank | Loaded from the repository, not edited by users |
| Item | id, order, text, scale, keyed (`+` or `-`) | From `item-bank.csv`. The `source` column is for documentation only |
| Person | id, display name, a contact (for example an email address) | No date of birth, no address, no job grade. A person can use the application with no account if the result is shown on the screen and not stored |
| Consent | person, profile, the text and version of the notice, date and time | One for each session. Without it, no answers are stored |
| Session | id, person, profile, started, completed, whether the Pressure items are included | |
| Response | session, item id, value 1 to 5 or empty | |
| Result | session, and for each scale: score, low, high, position, answered, items. Scoring version. Norms version, or none | Made by the scoring. Never typed by a user |
| Team | id, name, facilitator | |
| Team membership | team, person, agreement to be in the team report (yes or no), agreement to show the name (yes or no), date | Both agreements start as "no" |

## 4. The questionnaire

- Show the notice from `data-protection.md` before the first item, with the parts in brackets
  completed by the organisation. The person must take an action to agree. A box that is
  already ticked is not agreement.
- Show this instruction. Behaviour profile: "Describe yourself as you are at work now, not as
  you wish to be. For each statement, say how accurately it describes you. There are no right
  or wrong answers. Answer quickly. Your first answer is usually the best." Preference
  profile: the same text with "as you are now" in place of "as you are at work now".
- Show the items in the order of the `order` column. Do not show the scale of an item.
- Each item has five responses, with these labels and values: very inaccurate (1), moderately
  inaccurate (2), neither accurate nor inaccurate (3), moderately accurate (4), very accurate
  (5). No response is selected at the start.
- A person can leave an item empty. If items are empty at the end, tell the person the
  number and let them continue or go back. Do not force an answer.
- There is no time limit. A person can stop at any time. If they stop, delete the answers,
  unless the person chose to save and continue later.
- The Pressure scale of the preference profile is optional. The organisation sets whether its
  12 items are included. If they are included, tell the person before the first item that
  they can leave them empty. If they are not included, the questionnaire has 48 items.

## 5. Scoring

Your scoring must give the results in `scoring/test-vectors.json`. Scores, `low` and `high`
must agree within 0.1. Positions and counts must agree exactly.

For each scale of the profile:

1. Take the items of the scale that have an answer. Let `n` be their number, and `k` the
   number of items in the scale.
2. If `n` is 0, or if `(k - n) / k` is more than 1/6, the scale has no score. The fields
   `score`, `low`, `high` and `position` are empty. Stop for this scale.
3. Keyed value of an item: the response `r` if the item is keyed `+`, and `6 - r` if it is
   keyed `-`. A response that is not a whole number from 1 to 5 is an error.
4. `mean` is the mean of the keyed values.
5. **Provisional score (no norms).** `score = (mean - 1) / 4 × 100`.
6. **Provisional band.** `variance` is the sample variance of the keyed values (divide by
   `n - 1`). `half = t × sqrt(variance / n) / 4 × 100`, where `t` is the two-sided 95% value
   of Student's t for `n - 1` degrees of freedom (2.201 for 12 answers, 2.228 for 11, 2.262
   for 10; the full table is in the reference code). If `n` is 1, `half` is 100. If `half` is
   less than 5, use 5. `low = max(0, score - half)`. `high = min(100, score + half)`.
7. **Position.** If `high` is less than 40, the position is `lower`. If `low` is more than
   60, it is `higher`. In all other cases it is `middle`. Compare before you round.
8. Round `score`, `low` and `high` to one decimal place.

**With norms (after the pilot).** A norms file gives, for a scale, the `mean`, the `sd` and
the `reliability` of the mean item value in a reference group. Then:
`sem = sd × sqrt(1 - reliability)`. The score is `Φ((mean - norm mean) / sd) × 100`, where Φ
is the standard normal distribution function. `low` and `high` are the same function of
`mean - 1.96 × sem` and `mean + 1.96 × sem`. The position rule is the same. A scale that is
not in the norms file uses the provisional scoring. No norms file exists yet, so build this
path but do not switch it on.

**Team summary.** For each scale, take the scores of the people who agreed and who have a
score. If there are fewer than five, give only the number. If there are five or more, give
the number, the lowest, the median, the highest, and the spread (highest minus lowest).

Store the version of the scoring and of the item bank with each result. If either changes,
do not compare old and new results without a note to the reader.

## 6. Reports

- **Individual report.** Use the text of the report template of the profile. For each scale,
  show the paragraph for the person's position and leave out the other two. If a scale has no
  score, leave out its section and say why. Keep the section "Read this first" with no change.
- **Chart.** For each scale: a straight horizontal line from 0 to 100, a mark at the score,
  and a thicker part of the line from `low` to `high`. Shade the zone from 40 to 60. Use one
  neutral colour for all scales. Give the numbers as text also, for a person who cannot see
  the chart.
- **Preference profile.** Each scale has two named sides, which are in
  [`preference-profile/scoring/README.md`](preference-profile/scoring/README.md). Put the two
  names at the two ends of the line. The middle position is called "balanced".
- **Team report.** Use the text of the team report template. Show one mark for each person
  who agreed, and the median. Show a name only if that person agreed to it. Show no summary
  and no chart for a scale with fewer than five scores.
- The person can download the report in a format that they can keep (for example PDF or
  HTML).
- Each report states that the profile is a draft that is not yet tested, in the words of the
  template.

## 7. Who can see what

| Role | Can see | Cannot see |
|---|---|---|
| The person | Their own answers, results and reports. The list of people and teams that they shared a result with | The results of other people, apart from a team report that they are in |
| Facilitator | The team report of their team. The individual result of a person only if that person shared it with them | Answers and results that are not shared. A facilitator must not be the line manager of a person in the team |
| Administrator of the organisation | Who was invited, and who completed (yes or no) only if the person agreed to that | Answers, results and reports |
| Operator of the system | Only what support needs, with a record of each access | |

A person can take back a share at any time. From that moment the other person cannot open
the result, and the next team report does not include it.

## 8. Data protection requirements

Each row is a requirement that you can test. The rules are in `data-protection.md`.

| No. | Requirement |
|---|---|
| D1 | No answer is stored before a consent record exists for the session |
| D2 | The notice names the controller, the lawful basis, who sees the result, the retention period, the rights of the person and how to complain |
| D3 | The application collects no data about a person other than the fields in section 3 |
| D4 | A person can delete their answers, results and reports without help. The deletion is complete in the live system at once, and in backups within a stated period. The person gets a confirmation |
| D5 | A person can export their own data in a common format |
| D6 | The application deletes identified answers and results after the retention period that the organisation set. The period cannot be more than 12 months |
| D7 | No result is shared by default. Each share is an action by the person, for one named person or team |
| D8 | A team report is made only from the results of people who agreed, and only if there are five or more for the scale |
| D9 | Data is encrypted in transit and in storage. Access needs a login for each user. Access to results by operators is recorded |
| D10 | No answer or result goes to a third party for advertising, for sale, or to train a model. If the application uses an outside service to make a report, that service gets no name and no contact |
| D11 | The application has no report, export or interface that lists people by score |
| D12 | Data for research has a random code in place of the person. The contact for a second response is stored apart from the answers and is deleted after use |

## 9. Other requirements

- **Accessibility.** Meet WCAG 2.2 level AA. The questionnaire works with a keyboard only and
  with a screen reader. The charts do not depend on colour.
- **Devices.** The questionnaire works on a phone.
- **Language.** British English. The item wording is from the International Personality Item
  Pool and uses some American spelling. Do not change it. Do not translate the items without a
  new study of the translation.
- **Text from a language model.** If the application uses a language model to write any text
  for a person, that text must keep to section 2, must not add a claim about the person that
  the scores do not support, and must be marked as generated. The report text in the templates
  is the default, and it needs no model.
- **Licence.** The items are in the public domain. The rest of this repository is under the
  MIT licence. You can build open or closed software from it. You must not suggest that Open
  Leadership or Quarterdeck approved your software.
- **Name.** If you change the items, the scales or the scoring, do not call the result an "OL
  Behaviour Profile" or an "OL Preference Profile".

## 10. Acceptance tests

The software is complete when each of these is true.

1. Each case in `scoring/test-vectors.json` gives the expected result, and the team summary
   gives the expected numbers.
2. A scale with 2 of 12 answers missing has a score. A scale with 3 missing has none, and the
   report says why.
3. A response of 0, 6, 3.5 or text is refused.
4. The same answer to each item gives 50 on each scale.
5. With the Pressure items left out, the other four scales have scores and the report has no
   Pressure section.
6. A session with no consent record stores no answers.
7. A facilitator cannot open a result that is not shared. A share that is taken back stops
   access at once.
8. A team of four people with scores gets no summary and no chart. A team of five gets both.
9. A person deletes their data, and no query of the live system finds it.
10. No screen, report or export shows a type, a letter code, a colour for a person, a rank or
    a list of people by score.
11. Each report contains the "Read this first" text of its template.
12. An accessibility check of the questionnaire and of one report finds no failure at level
    AA.

## 11. Open points

- No norms exist. The provisional score compares a person with the middle of the response
  scale, not with other people. After the pilot, a norms file and a new version of this
  specification will follow.
- The pilot can remove or replace items. Load the item bank as data, so that a new version
  needs no change to the code.
- Where the application is hosted, and who operates it, is for each organisation to decide.

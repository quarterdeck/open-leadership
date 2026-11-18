<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->

# OL Preference Profile: technical manual

Version 0.1.0 (draft, before the pilot).

The sections follow the structure of the test review model of the European Federation of
Psychologists' Associations (EFPA), so that a reviewer can find what they expect.

## 1. Summary

| | |
|---|---|
| Name | OL Preference Profile |
| Purpose | To describe the working conditions in which a person does their best work, for conversations about roles, routines and team agreements |
| Use | Development and self-awareness, for adults at work |
| Not for | Recruitment, selection, promotion, pay or any decision about a person |
| Scores | Five two-sided scales: Company, Focus, Decisions, Planning, Pressure |
| Items | 60 statements, 12 for each scale |
| Response | Five points, from "very inaccurate" to "very accurate" |
| Time | About 10 minutes |
| Source of items | International Personality Item Pool (public domain) |
| Evidence | None yet. No pilot has been done |
| Licence | MIT |

## 2. Proper use

The profile helps a person to say what they need in order to work well, and helps a team to
agree how it works: meetings, quiet time, plans, decisions and deadlines. A result is a
suggestion from 60 answers. The person is the judge of whether it fits.

Do not use the profile:

- to select, promote, pay or dismiss a person, or to decide who gets a task
- to refuse a person a role because of a preference
- as a measure of ability, potential, health or character
- with a person who did not choose to take part

A preference is not a limit. People work outside their preferences every day. It costs them
more effort.

The profile uses no clinical or diagnostic ideas, and it gives no information about health.

## 3. The five scales

Each scale is a line with a description at each end and a balanced zone in the middle. A
person has a position on each of the five lines. The positions are independent in design.
There are no types, no colours and no letter codes, and no side is better than the other.

| Scale | One side (lower score) | Other side (higher score) |
|---|---|---|
| Company | **Alone.** Does the best work with quiet and privacy, and recovers alone | **With others.** Does the best work in a group, and gets energy from company |
| Focus | **Practical.** Prefers the concrete, the present and what can be used | **Conceptual.** Prefers ideas, reflection and the meaning behind things |
| Decisions | **By criteria.** Decides first by rules, logic and self-reliance | **By people.** Decides first by the effect on the people involved |
| Planning | **Flexible.** Prefers to keep options open and to act in the moment | **Planned.** Prefers to think first, settle the course and keep to it |
| Pressure | **Steady.** Stays calm, and is slow to see a threat | **Alert.** Notices risk early, and feels pressure sooner |

### Research base

The scales were chosen from published personality research, and then named in plain words.
Each is close to a part of one of the five factors of personality:

| Scale | Closest part of the five-factor model |
|---|---|
| Company | The sociable part of extraversion |
| Focus | The imagination and intellect parts of openness |
| Decisions | The sympathy part of agreeableness |
| Planning | The cautious, deliberate part of conscientiousness |
| Pressure | The anxiety and vulnerability parts of emotional stability, reversed |

The layout as five two-sided scales follows a public idea: the preference pairs that C. G. Jung
described in 1921 (the first four scales), with a fifth scale from the five-factor model. Many
commercial tools use the same public idea and sort people into categories. Published research
on personality scales finds that scores form one continuous spread, with no natural division
into two groups. For that reason this profile reports a position and a band, with a balanced
zone, and never a category. It uses no letters, colours or types.

These statements are hypotheses about this profile until the pilot tests them. A person must
read the published papers in full before a later version of this manual cites them.

### Cautions about the scales

- **One side of three scales is measured only by the absence of the other.** The items of
  Focus measure imagination and interest in ideas, so "practical" means a lower score on
  those. The items of Planning measure caution and impulse, so the scale is about how much a
  person thinks before they act, more than about plans. The report text for these sides goes
  further than the items. The pilot will show if these scales need new items or new names.
- **A provisional score is not a comparison with other people.** People agree with some kinds
  of statement more easily than with others. Many people will probably score on the "by
  people" side of Decisions and the "steady" side of Pressure. Norms will correct this.

- **Decisions.** The items measure attention to people directly. The "by criteria" side is
  measured only as the absence of that attention. The pilot will show if this side needs items
  of its own.
- **Pressure.** A higher score means that a person notices risk and feels pressure sooner. It
  is a normal difference between people, and it is useful to a team. It is not a statement
  about health, and a report must never present it as one.
- **Pressure is optional.** An organisation can leave the 12 Pressure items out of the
  questionnaire, which then has 48 items. If the organisation includes them, each person can
  still leave them empty. The scale then has no score, and the report leaves out its section.
  The other four scores do not change. An employer that holds a score about worry and
  pressure must have a clear reason to do so.

## 4. The items

All 60 items are in [`item-bank.csv`](item-bank.csv). Each row gives the item, its scale, the
direction in which it is keyed, and the scale of the International Personality Item Pool
(IPIP) from which it comes. An item keyed + counts towards the higher side.

- The wording of each item is the wording of the IPIP, with no change.
- The items come from two public IPIP scale sets: the 30-facet set and the 16-scale set.
- No item is also in the OL Behaviour Profile.
- Items were selected to fit the definition of the scale, to make sense at work, and to avoid
  any reference to health, belief or politics.

| Scale | Items | Keyed + | Keyed − | IPIP source scales |
|---|---|---|---|---|
| Company | 12 | 4 | 8 | Gregariousness (30-facet set), Introversion (16-scale set) |
| Focus | 12 | 6 | 6 | Imagination, Intellect (30-facet set), Complexity (16-scale set) |
| Decisions | 12 | 6 | 6 | Sympathy (30-facet set), Warmth, Sensitivity (16-scale set) |
| Planning | 12 | 6 | 6 | Cautiousness (30-facet set), Intellect, Imagination (16-scale set) |
| Pressure | 12 | 6 | 6 | Anxiety, Vulnerability (30-facet set) |

Company has more items keyed − than +, because the public items about company that fit a
workplace are mostly about being alone. A person who agrees with every statement gets a
Company score below the middle. The pilot will measure this effect.

The IPIP publishes reliability figures for its own scales. Those figures do not apply to the
scales of this profile, because each scale here is a new selection of items.

## 5. Administration

- The person reads the notice and agrees. See [data protection](../data-protection.md).
- Present the items in the order of the `order` column. The order mixes the scales.
- Instruction to the person: "Describe yourself as you are now, not as you wish to be. For
  each statement, say how accurately it describes you. There are no right or wrong answers.
  Answer quickly. Your first answer is usually the best."
- Response labels: 1 very inaccurate, 2 moderately inaccurate, 3 neither accurate nor
  inaccurate, 4 moderately accurate, 5 very accurate.
- The person can leave an item empty.
- The questionnaire works on paper or on a screen. No time limit applies.

## 6. Scoring

The code is [`../scoring/ol_scoring.py`](../scoring/ol_scoring.py), and
[`scoring/README.md`](scoring/README.md) shows how to run it. The rules are the same as for
the OL Behaviour Profile.

1. For an item keyed −, reverse the response: 6 minus the response.
2. The scale value is the mean of the answered items of the scale, from 1 to 5.
3. If more than 2 of the 12 items of a scale are empty, the scale has no score.
4. **Provisional score (now, with no norms).** Convert the scale value to 0 to 100: (value −
   1) ÷ 4 × 100. A score of 50 means that the person's answers balance between the two sides.
   It does not mean "average for working adults".
5. **Band.** The band shows the uncertainty of the score. With no norms, it is the score plus
   and minus about 2.2 standard errors of the person's own mean item value, and never less than
   5 points each way. The multiplier is the 95% value of Student's t for the number of answered
   items: 2.20 for 12 items and 2.26 for 10.
6. **Position.** If the whole band is below 40, the person is on the lower side. If the whole
   band is above 60, the person is on the higher side. In all other cases the result is
   "balanced" (the code calls it `middle`). The cuts at 40 and 60 are a convention for the
   provisional score. They have no evidence behind them yet.
7. **Normed score (after the pilot).** With a norms file, the score is the percentile of the
   person in the reference group, and the band comes from the standard error of measurement of
   the scale (1.96 standard errors each way). The cuts at 40 and 60 then apply to percentiles:
   the lower side is below the 40th percentile of the reference group.

## 7. Norms

There are none. The first norms will come from the pilot sample. See the
[pilot plan](../pilot/data-collection-plan.md).

## 8. Reliability

Not known. The pilot will report internal consistency (alpha and omega) and stability over 2
to 8 weeks. The aim for each scale is 0.70 or more, and 0.80 or more is preferred.

## 9. Validity

Not known. The plan:

| Question | Evidence planned |
|---|---|
| Do the items form five scales? | Factor analysis of the pilot data |
| Do the scores relate to the five personality factors as section 3 states? | Correlations with a public-domain five-factor measure |
| Does the profile differ from the OL Behaviour Profile? | Correlations between the nine scores. Expected overlaps: Company with Warmth, Focus with Exploration, Planning with Method, Decisions with Warmth. If a correlation is more than 0.70, one of the two scores is a candidate for removal |
| Do the scores match what people choose? | A later study that compares scores with the working conditions that people select when they have a choice |
| Is the profile useful? | Feedback from people and facilitators on whether the result led to a useful agreement or change |

No evidence connects the scores with job performance, and the profile makes no such claim.

## 10. Fairness

- Some IPIP items use American idioms. The pilot will show if an item works differently for
  people whose first language is not English.
- The pilot compares scores across age groups and sexes, and tests the items of a scale where
  a difference appears. Published research on the source factors finds average differences
  between women and men on scales like Decisions and Pressure. A report must never suggest
  that a side fits one group.
- A person who uses a screen reader, or who needs more time, can take the profile with no
  change to its meaning.

## 11. Known limits

- All evidence is still to be collected. Treat each result as provisional.
- A self-report shows how a person sees themselves.
- The provisional score is not compared with other people.
- Four of the five scales are expected to overlap with a score of the OL Behaviour Profile.
  The two profiles may tell a person less that is new than their names suggest.
- A preference changes with the task, the team and the stage of a career.

## 12. Sources

- International Personality Item Pool: a scientific collaboratory for the development of
  advanced measures of personality and other individual differences. https://ipip.ori.org/.
  The items and scales are in the public domain.
- Goldberg, L. R., Johnson, J. A., Eber, H. W., Hogan, R., Ashton, M. C., Cloninger, C. R., and
  Gough, H. G. (2006). The International Personality Item Pool and the future of public-domain
  personality measures. Journal of Research in Personality, 40, 84-96.
- EFPA Test Review Model (structure of this manual and guide values), CC BY-SA 4.0.
- The full list is in [SOURCES.md](../../SOURCES.md).

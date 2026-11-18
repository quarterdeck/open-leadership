<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->

# OL Behaviour Profile: technical manual

Version 0.1.0 (draft, before the pilot).

The sections follow the structure of the test review model of the European Federation of
Psychologists' Associations (EFPA), so that a reviewer can find what they expect.

## 1. Summary

| | |
|---|---|
| Name | OL Behaviour Profile |
| Purpose | To describe how a person tends to act with people and tasks at work, in words that a team can use |
| Use | Development and self-awareness, for adults at work |
| Not for | Recruitment, selection, promotion, pay or any decision about a person |
| Scores | Four: Voice, Warmth, Method, Exploration |
| Items | 48 statements, 12 for each score |
| Response | Five points, from "very inaccurate" to "very accurate" |
| Time | About 8 minutes |
| Source of items | International Personality Item Pool (public domain) |
| Evidence | None yet. No pilot has been done |
| Licence | MIT |

## 2. Proper use

The profile helps a person to see their habits at work, and helps a team to talk about its
differences. A result is a suggestion from 48 answers. The person is the judge of whether it
fits.

Do not use the profile:

- to select, promote, pay or dismiss a person, or to decide who gets a task
- to explain or excuse poor treatment of a person
- as a measure of ability, potential, health or character
- with a person who did not choose to take part

The profile uses no clinical or diagnostic ideas, and it gives no information about health.

## 3. The four dimensions

Each dimension is a line from lower to higher. A person has a position on each of the four
lines. The four positions are independent in design: a person can be higher or lower on any
combination. There are no types, and no position is better than another.

| Dimension | What it describes | Lower | Higher |
|---|---|---|---|
| Voice | How readily a person takes the lead and states a view | Waits, listens, lets others lead, keeps a view until asked | Takes charge, states a view early, tries to persuade |
| Warmth | How much a person attends to others and to relationships | Reserved, attends to the task before the people, keeps a distance | Approachable, notices what others need, gives time to people |
| Method | How much a person prefers plans, order and completion | Starts late or loosely, comfortable with disorder, works in bursts | Prepares, starts promptly, follows the plan, exact |
| Exploration | How much a person looks for new ideas and change | Prefers what is known and proven, values routine | Looks for variety, new ideas and new ways to do things |

### Research base

The dimensions were chosen from published personality research, and then named in plain words.

- Voice and Warmth follow the two themes that appear again and again in research on behaviour
  between people: agency (getting ahead, taking control) and communion (getting along, caring).
  In the five-factor model of personality, Voice is close to the assertiveness part of
  extraversion. Warmth draws on the friendliness part of extraversion and the caring part of
  agreeableness.
- Method is close to conscientiousness, mainly its orderliness and self-discipline parts.
- Exploration is close to openness to experience, mainly its preference for variety and for
  new ideas.

The profile does not report emotional stability. The OL Preference Profile has a related
scale (Pressure).

These statements about the research base are hypotheses about this profile until the pilot
tests them. A person must read the published papers in full before a later version of this
manual cites them.

## 4. The items

All 48 items are in [`item-bank.csv`](item-bank.csv). Each row gives the item, its scale, the
direction in which it is keyed, and the scale of the International Personality Item Pool
(IPIP) from which it comes.

- Each item is a short statement in the first person, such as "Take charge."
- The wording of each item is the wording of the IPIP, with no change.
- The items come from two public IPIP scale sets: the 30-facet set and the 16-scale set.
- Items were selected to fit the definition of the dimension, to make sense at work, and to
  avoid any reference to health, belief or politics.
- Each scale has items keyed in both directions, so that a person who agrees with every
  statement does not get a high score.

| Scale | Items | Keyed + | Keyed − | IPIP source scales |
|---|---|---|---|---|
| Voice | 12 | 6 | 6 | Assertiveness (30-facet set), Assertiveness (16-scale set) |
| Warmth | 12 | 6 | 6 | Altruism, Friendliness (30-facet set), Warmth (16-scale set) |
| Method | 12 | 6 | 6 | Orderliness, Self-discipline (30-facet set), Orderliness (16-scale set) |
| Exploration | 12 | 7 | 5 | Adventurousness, Intellect (30-facet set), Complexity (16-scale set) |

The IPIP publishes reliability figures for its own scales. Those figures do not apply to the
scales of this profile, because each scale here is a new selection of items.

## 5. Administration

- The person reads the notice and agrees. See [data protection](../data-protection.md).
- Present the items in the order of the `order` column. The order mixes the scales.
- Instruction to the person: "Describe yourself as you are at work now, not as you wish to be.
  For each statement, say how accurately it describes you. There are no right or wrong
  answers. Answer quickly. Your first answer is usually the best."
- Response labels: 1 very inaccurate, 2 moderately inaccurate, 3 neither accurate nor
  inaccurate, 4 moderately accurate, 5 very accurate.
- The person can leave an item empty.
- The questionnaire works on paper or on a screen. No time limit applies.

## 6. Scoring

The code is [`../scoring/ol_scoring.py`](../scoring/ol_scoring.py), and
[`scoring/README.md`](scoring/README.md) shows how to run it.

1. For an item keyed −, reverse the response: 6 minus the response.
2. The scale value is the mean of the answered items of the scale, from 1 to 5.
3. If more than 2 of the 12 items of a scale are empty, the scale has no score.
4. **Provisional score (now, with no norms).** Convert the scale value to 0 to 100: (value −
   1) ÷ 4 × 100. A score of 50 means that the person's answers balance at the middle of the
   response scale. It does not mean "average for working adults".
5. **Band.** The band shows the uncertainty of the score. With no norms, it is the score plus
   and minus 1.96 standard errors of the person's own mean item value, and never less than 5
   points each way. A person whose answers within a scale disagree gets a wider band.
6. **Position.** If the whole band is below 40, the position is "lower". If the whole band is
   above 60, it is "higher". In all other cases it is "middle". The cuts at 40 and 60 are a
   convention for the provisional score. They have no evidence behind them yet.
7. **Normed score (after the pilot).** With a norms file, the score is the percentile of the
   person in the reference group, and the band comes from the standard error of measurement of
   the scale.

## 7. Norms

There are none. The first norms will come from the pilot sample. See the
[pilot plan](../pilot/data-collection-plan.md). The manual will describe the sample and its
limits.

## 8. Reliability

Not known. The pilot will report internal consistency (alpha and omega) and stability over 2
to 8 weeks. The aim for each scale is 0.70 or more, and 0.80 or more is preferred.

## 9. Validity

Not known. The plan:

| Question | Evidence planned |
|---|---|
| Do the items form four scales? | Factor analysis of the pilot data |
| Do the scores relate to the five personality factors as section 3 states? | Correlations with a public-domain five-factor measure |
| Are the four scores different from each other? | Correlations between the scores. Expected: low to moderate |
| Do other people see the same behaviour? | A later study that compares self-ratings with ratings by colleagues |
| Is the profile useful? | Feedback from people and facilitators on whether the result led to a useful conversation or change |

No evidence connects the scores with job performance, and the profile makes no such claim.

## 10. Fairness

- The items avoid culture-specific activities where possible. Some IPIP items use American
  idioms. The pilot will show if an item works differently for people whose first language is
  not English.
- The pilot compares scores across age groups and sexes, and tests the items of a scale where
  a difference appears.
- A person who uses a screen reader, or who needs more time, can take the profile with no
  change to its meaning.

## 11. Known limits

- All evidence is still to be collected. Treat each result as provisional.
- A self-report shows how a person sees themselves. People can answer as they wish to be seen.
- The provisional score is not compared with other people.
- Behaviour changes with the situation. The profile describes a tendency.

## 12. Sources

- International Personality Item Pool: a scientific collaboratory for the development of
  advanced measures of personality and other individual differences. https://ipip.ori.org/.
  The items and scales are in the public domain.
- Goldberg, L. R., Johnson, J. A., Eber, H. W., Hogan, R., Ashton, M. C., Cloninger, C. R., and
  Gough, H. G. (2006). The International Personality Item Pool and the future of public-domain
  personality measures. Journal of Research in Personality, 40, 84-96.
- EFPA Test Review Model (structure of this manual and guide values), CC BY-SA 4.0.
- The full list is in [SOURCES.md](../../SOURCES.md).

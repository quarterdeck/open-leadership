<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->

# OL Preference Profile: team report template

Version 0.1.0 (draft). Text in `{braces}` is replaced for each team.

Rules:

- Each person agreed that their result is part of this report.
- The report shows no summary for a scale with fewer than five scores.
- A name appears only if that person agreed to it. The default is no names.
- The chart shows one mark for each person. Tell each person this before they agree, because
  colleagues can sometimes work out whose mark is whose.
- Do not label the team as a type. Do not rank people.

The function `team_summary` in the scoring code gives the numbers.

---

# OL Preference Profile: team report

**{team}**, {date}, {n} people

## Read this first

- This report shows the spread of the team's working preferences. Its purpose is a set of
  team agreements: how we meet, when we are quiet, how we plan and how we decide.
- It must not be used for any decision about a person.
- The profile is a draft that is not yet tested. The team decides if the picture is true.
- No side is better than the other.

## The team's spread

Each `o` is one person. `M` is the median.

```
                                 balanced
Alone          |--o------|-o--o----|::M::::::|--o------|--o------|   With others
Practical      |---------|--o--o-o-|:M::o::::|---------|-o-------|   Conceptual
By criteria    |---------|-----o---|::o:M:o::|--o------|---------|   By people
Flexible       |-o-------|---------|::o::M:::|-o--o----|---------|   Planned
Steady         |---o--o--|----M----|:::::::o:|---------|--o------|   Alert
```

| Scale | Lowest | Median | Highest | Spread |
|---|---|---|---|---|
| Company | {company.lowest} | {company.median} | {company.highest} | {company.spread} |
| Focus | {focus.lowest} | {focus.median} | {focus.highest} | {focus.spread} |
| Decisions | {decisions.lowest} | {decisions.median} | {decisions.highest} | {decisions.spread} |
| Planning | {planning.lowest} | {planning.median} | {planning.highest} | {planning.spread} |
| Pressure | {pressure.lowest} | {pressure.median} | {pressure.highest} | {pressure.spread} |

## What a spread means

**Most of the team is on one side.** The team's habits probably suit that side. Ask who pays
for that: the few people on the other side, a customer, or the work itself.

**The team is spread wide.** The team's habits cannot suit everybody at the same time. An
explicit agreement is necessary.

**The team is balanced.** The team can probably adapt, and the agreement can be simple.

## Questions and possible agreements

| Scale | Questions | Examples of agreements |
|---|---|---|
| Company | How much of our week is in meetings or open contact? Who needs more quiet, and who needs more contact? | Quiet hours with no messages. An agenda one day before a meeting. One shared working session each week |
| Focus | Do our discussions start with the idea or with the example? Who do we lose in each case? | Each proposal has one paragraph of "why" and one of "what we do on Monday" |
| Decisions | When we decide, do we look first at the criteria or at the people? What did that cost us last time? | For each large decision, name the criteria and name who is affected, in that order or the other |
| Planning | How late can a plan change here? Who pays for a late change? Who pays for a plan that is fixed too early? | A date after which a plan changes only for a stated reason. A review point in each plan |
| Pressure | Who sees our risks first? Do we listen? Who stays calm when things go wrong, and do we use that? | A risk question at the start of each project. A named steady person for an incident |

## Our agreements

| We noticed | We agree | Review date |
|---|---|---|
| | | |
| | | |
| | | |

## About this report

Results are provisional, because the profile has no norms yet. Open Leadership is an
independent, unregulated framework. The profile is not validated for recruitment or selection.
{organisation} keeps this report until {deletion date}.

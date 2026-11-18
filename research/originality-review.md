<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->

# Originality review

Date: 18 November 2026. This is Phase 5 of the specification: a check of all content against
the hard rules, with a list of each passage that a person must review.

## Method and its limit

1. A search of all files for the names of awarding bodies, professional bodies, test
   publishers and branded models, and for words that claim accreditation, regulation,
   endorsement, equivalence or validation.
2. Two independent reviews by AI reviewers that did not write the content. One read all 61
   units. The other read the profiles, the framework rules, the people practice documents, one
   full set of qualification documents and the top-level files.

**The limit.** No reviewer opened the material of an awarding body, a professional body or a
test publisher, because the project rules forbid it. Each statement that a passage "is close
to" such material comes from a reviewer's memory. A person must check each open item against
the public source before a decision.

## Result in short

- No copied or closely paraphrased text was found. No item, scoring key or report text of a
  commercial tool was found. No colour system, wheel, letter code or type was found.
- No document claims accreditation, regulation, endorsement, equivalence or validation.
- The risk is in names and structure. Some qualification titles are close to existing titles.
  Some well-known models were recognisable in plain words. The preference profile follows a
  well-known public idea. Some data protection promises were stronger than the design.
- 30 points were corrected. 14 decisions are open for a person.

## Open decisions for a person

| No. | Subject | Concern | Options |
|---|---|---|---|
| 1 | The titles of the people practice qualifications | "Level 3 Certificate in People Practice", the two Level 5 pathways and "Level 7 Diploma in Strategic People Practice" are close to the titles of the main UK HR body. "People practice" is that body's term. The specification itself set the family name | Keep, or rename the family (for example "HR and Learning Practice") |
| 2 | The titles of the coaching qualifications | "Level 7 Certificate in Executive Coaching and Mentoring" and "Level 5 Certificate in Coaching and Mentoring" may be the same as existing titles of another body | Check the Ofqual register, then keep or rename |
| 3 | Coaching practice hours | OL3-COA-02 (6 hours), OL5-COA-01 (12 hours) and OL7-COA-01 (20 hours) may be the same ladder as another body's coaching qualifications | Keep as public facts, or set different hours with our own reasons |
| 4 | The people practice unit set | The Level 5 and Level 7 units cover the same subjects as the units of the main UK HR body, almost one to one. The wording is our own. Titles still close: OL7-PPR-02 "Strategic employment relations and reward", OL7-PPR-03 "Organisation design and development" | Accept as "comparable in scope", or change the division of subjects |
| 5 | The competence framework | The split into general areas and specialist areas, and the names of the specialist areas, have the same form as the copyright map of the main UK HR body. The areas are also ordinary names of HR functions | Keep, or remove the split |
| 6 | The recognition scheme | A ladder of three grades on qualification plus experience, with yearly CPD, has the form of membership grades. "Associate" is a membership grade name elsewhere | Keep, rename the first grade, or remove the scheme |
| 7 | The OL Preference Profile model | The first four scales follow the public preference pairs of C. G. Jung, in the usual order, as several commercial tools do. The profile now says so. The scores are continuous, with no letters, colours or types. Some report phrases ("gets energy from company", "keep options open") are common in reports of such tools | Keep, or rebuild the profile directly on the five-factor model with one-sided scales |
| 8 | The Pressure scale | Its items are about worry and pressure, and its public source scales are named "Anxiety" and "Vulnerability". The report text avoids all health language. An employer still holds a score of this kind | Keep with the present cautions, make it optional, or remove it |
| 9 | The OL Behaviour Profile model | Four dimensions invite a comparison with four-style commercial tools. Voice and Method are near two of the well-known four styles. The straight-line chart is near the chart of another commercial four-factor tool that is not in the specification. The reviewer judged the distance adequate | Keep, or add a fifth dimension so that the count differs |
| 10 | Levels, sizes and badges | The titles use "Level", "Award", "Certificate" and "Diploma" with the regulated meanings, on purpose. A badge shows only "OPEN LEADERSHIP" and, for example, "LEVEL 5 DIPLOMA". A person who sees only a badge or a title does not see the word "unregulated" | Add "independent, unregulated" to the badge, or require the sentence next to each title |
| 11 | The comparisons in the level descriptors | "Comparable level of demand: A level / a foundation degree / a master's degree". The form is the permitted one, but a small unregulated diploma next to "a master's degree" implies much | Keep, or change to "the level at which A levels sit" |
| 12 | NOTICE | It names the six organisations to state that there is no connection. A reference by name needs a human review. Check the legal name of each. The reviewer thinks that the name given for one leadership body is not the name of the awarding brand | Review and correct |
| 13 | Retention of assessment records | "At least six years" has no upper limit and no stated reason, and the record holds personal data | Set a period and a reason |
| 14 | The public specification | `docs/agent-spec.md` describes each part as the "equivalent" of a named offering. It was published by decision | Keep, or edit the public copy |

Smaller points that stay open:

- Report text of the preference profile describes the "practical", "by criteria" and "flexible"
  sides more fully than the items measure. The technical manual now says so.
- The provisional band uses 1.96 standard errors. With 10 to 12 items, a larger multiplier
  (about 2.2) is more exact.
- With a norms file, the cuts at 40 and 60 apply to percentiles. The manuals do not yet say so.
- The scoring code gives an unhelpful error for a response such as "3.0", and the analysis
  code stops on an empty data set.
- Items to look at in the pilot: PP25 "Believe people should fend for themselves" (an attitude
  about society), PP02 "Rarely notice my emotional reactions" (not about decisions), BP39 "Like
  to visit new places" (not about work).
- The MIT licence permits a person to change a badge. The badge rules are a request.
- The manifesto criticises fee and licence schemes without names. Confirm the tone.
- "A certificate is valid if" suggests an authority that decides. No such authority exists.
- The technical manuals follow the structure of an openly licensed test review model. Check
  that its share-alike licence permits this under MIT, and that the wording does not suggest a
  review by its owner.
- SOURCES.md needs entries for the published academic work behind the general ideas in the
  units (see the list below), after a person reads each source.

## Corrected in this review

| Where | What was wrong | Correction |
|---|---|---|
| OL5-RES-02 | A definition of risk that is word for word that of a copyright international standard | Reworded |
| OL3-OPS-02 title | "Solving problems and making decisions", the same as an existing unit title at the same level | "Finding causes and deciding what to do" |
| OL5-PPR-06 title | "Learning in the flow of work", a phrase tied to one author | "Learning from work and from colleagues" |
| OL5-PPR-01 title and content | "Resourcing and talent", and "tight and loose labour markets" | "Recruitment, retention and succession", and reworded |
| OL3-COA-02 criterion 2.1 | Made a well-known four-stage coaching model compulsory | The learner uses stages that they can explain |
| OL5-COA-01 | "A recognised process" implies an outside authority | "A staged process" |
| OL5-PEO-01 | A criterion assumed a five-stage model of team development, and the content listed its stages | Reworded, with the limits of stage models |
| OL5-OPS-03 | A published four-source model of evidence was built into the evidence requirements | "More than one type of source" |
| OL5-PPR-04, OL7-PPR-04 | A branded four-level model of training evaluation, and a phrase of its owners | Reworded |
| OL7-OPS-01 criterion 2.1 | The perspectives of a branded scorecard, in its order | "Financial and non-financial measures" |
| OL7-PPR-03, OL7-PEO-01 | Lists that followed a branded organisation model and a published list of culture mechanisms | Reworded in our own terms |
| OL5-CHG-01 | Steps of a well-known change model in its order. A criterion stated a legal duty to consult too widely | Reordered and shortened. "Legal and contractual duties" |
| OL5-SLF-01, OL5-PEO-01 | The usual description of type preferences | "Preferences in how a person works" |
| OL7-SLF-01, OL7-COA-01, OL7-COA-02 | "The duty to be candid" and "fitness to practise" are terms of regulated sectors | Reworded |
| All 61 units and the unit bank page | A unit page read alone did not say that the levels and credits are our own | A statement in each unit |
| MANIFESTO.md, GOVERNANCE.md | "Every word is original" was not true: the items are public-domain wording, and the descriptors are adapted | Accurate statements |
| Credit and assessment rules | A comparison with an identifiable qualification. No attribution for the size thresholds | Removed. Attribution added |
| Level descriptors | The attribution was weak | "Adapted from", a link, Crown copyright, and a request to keep the attribution |
| Competence framework | It cited an L&D apprenticeship standard that is not in SOURCES.md | Corrected |
| profiles/README.md, preference manual | Said that no model came from elsewhere, and criticised other tools with no source | States the public origin of the ideas. The claim is narrower |
| Both individual reports | "A different day could put you anywhere in the band". The band does not measure that | Reworded |
| Preference profile | "Most results are in or near the balanced zone" had no data | Removed. A caution on raw scores added to both manuals |
| Profile pages and guides | "Describes what others see": the profile is a self-report | "How a person says that they act" |
| Data protection | "The person sees the result first" is not true when a facilitator scores | The person decides who sees it. The facilitator is never the line manager, and the person is told who scores |
| Data protection, team reports, code | A summary for three people shows each person's score | The minimum is five. People are told that the chart shows one mark for each person |
| Data protection, pilot plan | Pilot data was called anonymous while a link to a contact exists | Called personal data until the link is deleted |
| Data protection notice | No controller, lawful basis, rights or route to complain | Added |
| Data protection | An impact assessment was only "considered" | Required before a first use |
| Scoring code | An item that is in the bank two times gave a wrong count with no error | An error, with a test |
| Analysis code | Norms with no reliability value stopped the scoring code | Such a scale gets no norms |

## General ideas that remain in the units

These ideas are in the indicative content in plain words, with no name. Each comes from
published academic work or public sector material, or is in general use. The reviewer rated
each as low risk, apart from the last, which a person must confirm. A person can add the sources to SOURCES.md after reading them.

Stages of response to change. Kinds of waste in a process. Urgent and important tasks.
Repeated "why" questions and categories of cause. Specific, measurable and achievable
objectives. The employee life cycle. Forces for and against a change. Cheap tests of risky
assumptions. Cycles of reflection. The purposes of supervision. The critical path and the
responses to a risk. Fitness for purpose, the cost of quality, and plan, trial, check and
decide. Trust as ability, honesty and good intent. Leadership styles from directive to
delegating. Learning from work, from other people and from formal learning. A grid of interest
and power, and interests behind positions. Sources of pressure at work (from the public
standards of the UK health and safety regulator). Features of a good job. The unwritten
expectations between employer and worker, and three kinds of fairness. Reviews after action.
Headings for a scan of the external environment, and strengths and weaknesses. Levels of
culture. Exploring and exploiting. The chain of activities that creates value. Three layers of
control. Tests of a strategic option, resources that are hard to copy, and deliberate and
emergent strategy. Power, legitimacy and urgency of stakeholders. Organisation development as
planned change. Transitions between levels of leadership. The five responses to conflict.

## What was found clean

- No named body, product, author or trade mark in any unit, qualification document or profile
  document. Names are only in `NOTICE`, `SOURCES.md`, `research/` and the specification.
- No legal figure, time limit or section number in any unit.
- No learning outcome that starts with "understand" or "know". No em dash.
- Each of the 108 questionnaire items has the correct key, and no item is in both profiles.
- The badges contain nothing that resembles another organisation's badge.

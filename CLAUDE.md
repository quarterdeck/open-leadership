# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Open Leadership (OL) is an open, freely licensed framework of management, leadership and people
practice qualifications, with two profiling tools (a behaviour profile and a preference profile).
Quarterdeck commissions it. The readers are HR, L&D and line managers in UK organisations.

`MANIFESTO.md` states the mission: leadership knowledge and tools open to everybody, with no
gatekeepers. Keep published content consistent with it.

The full specification is `docs/agent-spec.md`. Read it before you write content. This file is a
summary of the rules that apply to every task.

OL is comparable with the proprietary offerings in structure, level, scope and usefulness. It is
independently authored. Every word of syllabus, handbook, assessment item and report text is
written fresh from public facts and primary sources.

## Hard rules

These rules override all other instructions. If a task needs to break one, stop and ask.

1. No copying. Do not reproduce, closely paraphrase or translate material from CMI, ILM, City &
   Guilds, CIPD, DiSC (Wiley) or Insights Discovery (Insights Group). This includes unit
   specifications, handbooks, items, questionnaires, scoring keys, report text and model diagrams,
   and leaked, scraped or archived copies.
2. No trade marks in product names. Do not use the incumbents' names, "Discovery" as a product
   name, or a colour-and-character naming system. A nominative reference in a comparison needs a
   human review before publication.
3. No false claims. Never state or imply that OL is accredited, endorsed, approved, recognised,
   regulated by Ofqual or "equivalent" to an incumbent. Write "comparable in level and scope",
   with the disclaimer that OL is an independent, unregulated framework.
4. No lookalike branding. Visual identity, colours, report layouts and graphics must differ
   visibly from the incumbents.
5. Open foundations only. Permitted inputs: Ofqual RQF level descriptors, UK National Occupational
   Standards, published academic literature, public-domain psychometric resources (IPIP), and the
   public structure of qualifications (levels, credits, titles, hours, assessment methods) as facts.
6. Data protection. A profiling tool that collects personal data is designed for UK GDPR by
   default: consent, minimal data, retention limits, no sale of data.
7. Record provenance. Add each source to `SOURCES.md`: the link, the facts taken, the licence.

The profiles are for development and self-awareness. They are not validated for recruitment or
selection. Use no clinical or diagnostic language.

## This repository is public

`quarterdeck/open-leadership` is a public GitHub repository. Each push to `main` publishes the
content on GitHub and on the site. Therefore:

- Do not write or push `comparison/positioning.md`, or any other comparison with an incumbent,
  before Kris reviews it.
- Do not add private data or internal business information.

## Licence

MIT for all content, documents and code (Kris's decision; it replaces the CC BY-SA default in
section 6 of the specification). Each file carries a licence header. In Markdown, put this
comment after the front matter or on the first line:

```
<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->
```

## Structure

All documents are Markdown. No Word files.

- `framework/`: level descriptors, credit and assessment rules, `unit-bank/` (one file per unit).
  Qualifications in all three families share units from this one bank.
- `qualifications/management/`, `leadership/`, `people-practice/`: one folder for each qualification, with
  `specification.md`, `unit-summaries.md`, `assessment-guide.md`, `centre-guide.md` and
  `learner-handbook.md`.
- `profiles/behaviour-profile/`, `profiles/preference-profile/`: `technical-manual.md`,
  `item-bank.csv`, `scoring/` (code with tests), `reports/`, `facilitator-guide.md`.
- `research/`: source notes, the name-clash report, the proposed framework architecture.
- `comparison/`: positioning (human review required).
- `docs/agent-spec.md`: the specification.

Qualification titles follow `OL Level [n] [Award | Certificate | Diploma] in [Subject]`.

## Process

The work has five phases (section 9 of the specification). Phases 1 and 2 end with a stop for
Kris's approval.

1. Research and plan. Done.
2. Framework core: level descriptors, credit rules, unit bank. Done.
3. Qualifications: management, then leadership, then people practice, with the unit overlap
   check (`research/unit-overlap-check.md`). Written.
4. Profiles: item banks, scoring, technical manuals, report templates.
5. Review: originality check against the hard rules.

Work on one workstream at a time. Commit after each unit of work with a clear message and push
to `main`.

## Decisions by Kris (18 November 2026)

- Open to anyone: any organisation can deliver, assess and certify, with no approval. This is
  intended. Do not add an approval or licensing step.
- Certificates: organisations issue their own. A certificate is valid if the process in
  `framework/credit-and-assessment-rules.md` was followed and the record is kept. The process
  ends with a panel review, like the oral examination of a research degree. This model is a
  first design and can change.
- Names: write "Open Leadership" in full in documentation. Use the prefix "OL" only in the
  names of qualifications and profiles, and in unit codes.
- Badges: `badges/` holds the badge files, made from Quarterdeck's own badge design with an
  "OL" rosette. A badge never says "accredited". There is a qualification badge for each level
  and size, and an Open Leadership CPD badge.
- The owner of the framework in the long term is not decided. Quarterdeck is the steward.

## How the framework fits together

- `framework/unit-bank/README.md` is the map: it lists each unit by domain and the core and
  optional units of each qualification. A qualification is only a list of units, so a change to
  a unit changes each qualification that uses it. Keep the map and the "Used in" table of each
  unit file in agreement.
- Unit size is fixed for each level (5, 6 and 10 credits at Levels 3, 5 and 7). The credits of a
  qualification are the number of units multiplied by the unit size.
- `python3 tools/build_qualifications.py .` writes the five documents of each of the 17
  qualifications, and `qualifications/README.md`, from the unit bank and its map. Do not edit
  those documents by hand. Change the unit, the map or the text in the script, then run it.
- `qualifications/people-practice/` also holds the competence framework and the recognition
  scheme. Both are written by hand.
- `research/framework-architecture.md` is the Phase 1 proposal. Where it differs from the files
  in `framework/`, the files in `framework/` are correct.

## Writing standards for the content

- British English. Plain, direct, short sentences.
- No em dashes. No filler words. No "not X but Y" constructions.
- Learning outcomes use measurable verbs (analyse, apply, evaluate, plan).
- Each unit includes a short, practical workplace scenario.

## Site

GitHub Pages builds the site from the root of `main` with its built-in Jekyll (`_config.yml`).
There is no build step and no workflow. The Markdown files are the pages, and `README.md` is the
home page. The address is https://quarterdeck.github.io/open-leadership/.

There are no lint or test commands until the scoring code exists (Phase 4).

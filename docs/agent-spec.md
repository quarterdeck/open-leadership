# Open Leadership (OL): Agent Specification

## 1. Mission

Build an open, freely licensed framework of qualifications and profiling tools that serve the same practical purpose as the following proprietary offerings:

| Proprietary offering | Open equivalent (working name) |
|---|---|
| CMI qualifications | OL Management Qualifications |
| ILM qualifications | OL Leadership Qualifications |
| CIPD accreditations | OL People Practice Qualifications |
| DiSC profiling | OL Behaviour Profile |
| Insights Discovery | OL Preference Profile |

The framework is branded **Open Leadership (OL)**.

The commissioning organisation is Quarterdeck (Harrogate, UK), a leadership and management development company. Quarterdeck will deliver and promote the framework. Readers are HR, L&D and line managers at UK mid-market and corporate organisations, so the output must look credible and be easy to compare with the incumbents.

## 2. Meaning of "clone"

A clone means **functionally comparable and independently authored**. It matches the incumbents on structure, level, scope and usefulness. It shares none of their text, items, scoring keys, models, names, branding or visual identity.

Every word of syllabus, handbook, assessment item and report text is written fresh by you, working from public factual information and primary sources.

## 3. Legal and IP guardrails (hard rules)

These override every other instruction in this document. If a task seems to need breaking one, stop and ask.

1. **No copying.** Do not reproduce, closely paraphrase or translate unit specifications, handbooks, assessment items, questionnaires, scoring algorithms, report text or model diagrams from CMI, ILM, CIPD, DiSC (Wiley / Everything DiSC and licensed distributors) or Insights Discovery (Insights Group). This applies to material found in leaked, scraped or archived form as well.
2. **No trademarks in product names.** Do not use CMI, ILM, City & Guilds, CIPD, DiSC, Insights, Insights Discovery, "Discovery" as a product name, or their colour-and-character naming systems. Nominative reference in a comparison table ("comparable in level to...") is acceptable once reviewed by a human.
3. **No false claims.** Never state or imply that OL is accredited, endorsed, approved, recognised, regulated by Ofqual, or "equivalent" to any incumbent. Use "comparable in level and scope" with a plain disclaimer that OL is an independent, unregulated framework.
4. **No lookalike branding.** Visual identity, colour schemes, report layouts and wheel/quadrant graphics must differ visibly from the incumbents.
5. **Public-domain and open foundations only.** Acceptable inputs: Ofqual RQF level descriptors, the UK National Occupational Standards for management and leadership, published academic literature, public-domain psychometric resources, and the publicly stated structure of qualifications (levels, credit values, titles, guided learning hours, assessment methods) treated as facts.
6. **Data protection.** Any profiling tool that collects personal data must be designed for UK GDPR compliance by default (consent, minimal data, retention limits, no sale of data).
7. **Record provenance.** Keep a `SOURCES.md` listing every source consulted, what was taken from it (facts only), and its licence.

## 4. Workstreams

### A. OL Management Qualifications (CMI equivalent)
- Research the public structure of CMI qualification families: levels 2 to 7, award / certificate / diploma sizes, credit and total qualification time, typical unit themes, assessment approaches (assignments, work-based evidence, professional discussion).
- Design an original ladder, for example: Level 3 Award in Management Practice, Level 5 Certificate and Diploma in Management Practice, Level 7 Diploma in Strategic Management.
- Per qualification: purpose, target learner, entry guidance, unit list with credit values, learning outcomes and assessment criteria, assessment methods, grading rules, evidence requirements.

### B. OL Leadership Qualifications (ILM equivalent)
- Same method as A, with the emphasis on leadership: first-line leader, middle manager, senior leader, coaching and mentoring pathway.
- Suggested ladder: Level 3 Award in Leadership Practice, Level 5 Certificate/Diploma in Leadership Practice, Level 7 Diploma in Strategic Leadership.
- Share units with workstream A where sensible, so the whole set forms one modular credit system.

### C. OL People Practice Qualifications (CIPD equivalent)
- Research the public structure of CIPD qualifications (foundation, associate, intermediate, advanced levels) and membership grades.
- Design an original pathway for HR and L&D practitioners with unit specifications, and a **membership-grade style recognition scheme** (for example Associate, Practitioner, Senior Practitioner) based on qualification plus evidenced experience.
- The CIPD Profession Map is copyrighted. Build the competency framework from the UK NOS for HR and L&D and from published research, and make it structurally different.

### D. OL Behaviour Profile (DiSC equivalent)
- Build an original four-dimension behavioural style questionnaire.
- Use the **International Personality Item Pool (IPIP)** (public domain) as the source of questionnaire items, and the Big Five literature as the scientific base. Do not reuse DiSC items, adjective checklists, scoring keys, the circular map or the letter model. Name the dimensions and the model afresh.
- Deliverables: item bank, administration instructions, scoring method (in code and in documentation), norm-group approach, individual report template, team report template, facilitator guide.

### E. OL Preference Profile (Insights Discovery equivalent)
- Build an original preference profile covering a small number of preference dimensions with a clear, plain-English model for non-specialists.
- Do not reuse the colour-energy names, the 72-type wheel, the Jungian presentation as Insights uses it, report wording or scoring. Choose a different visual language.
- Same deliverable set as D. Share the item pool and scoring engine with D where the science supports it, and state clearly where the two instruments differ in purpose.

## 5. Psychometric and quality requirements (D and E)

- Include a technical manual covering construct definitions, item selection, scoring, and a plan for reliability (Cronbach's alpha, test-retest) and validity evidence.
- Write the data-collection plan for a pilot of at least 300 respondents, including the analysis code.
- State plainly in all materials that the profiles are for development and self-awareness. They are not validated for recruitment or selection decisions until evidence supports that.
- Use no clinical or diagnostic language.

## 6. Open licensing

- Default licence: **CC BY-SA 4.0** for documents, **MIT** for code, unless Kris specifies otherwise.
- Every file carries a licence header. The repository carries a top-level `LICENSE`, `NOTICE` and `CONTRIBUTING.md`.
- Include a governance page: how changes are proposed, who approves them, how versions are numbered.

## 7. Naming

- Framework: **Open Leadership (OL)**.
- Qualification titles follow `OL Level [n] [Award | Certificate | Diploma] in [Subject]`.
- Run a name-clash check on "Open Leadership" and "OL" (UK IPO trade mark search, Companies House, web search, training-sector directories). Report findings with links. Propose three fallback names if there is a conflict.
- Propose product names for the two profiles (D and E). Avoid colour-character systems and single-letter acronyms that echo DiSC.

## 8. Deliverables and structure

Produce a Git repository with Markdown as the format for all documents. No Word files.

```
open-leadership/
  README.md
  LICENSE  NOTICE  CONTRIBUTING.md  SOURCES.md  GOVERNANCE.md
  framework/
    level-descriptors.md
    credit-and-assessment-rules.md
    unit-bank/            (one .md per unit)
  qualifications/
    management/  leadership/  people-practice/
  profiles/
    behaviour-profile/  preference-profile/
      technical-manual.md  item-bank.csv  scoring/  reports/  facilitator-guide.md
  comparison/
    positioning.md        (human-review required before publication)
  research/
    name-clash-report.md  source-notes.md
```

Each qualification folder contains: `specification.md`, `unit-summaries.md`, `assessment-guide.md`, `centre-guide.md`, `learner-handbook.md`.

## 9. Process

1. **Phase 1: Research and plan.** Public-source research, `SOURCES.md`, name-clash report, proposed framework architecture. **Stop and present for approval.**
2. **Phase 2: Framework core.** Level descriptors, credit rules, unit bank skeleton. **Stop for approval.**
3. **Phase 3: Qualifications (A, B, C).** Build in that order, then cross-check unit overlap.
4. **Phase 4: Profiles (D, E).** Item banks, scoring, technical manuals, report templates.
5. **Phase 5: Review.** Run an originality check on all content against the guardrails in section 3, and list any passage that might be too close to an incumbent so a human can review it.

Work one workstream at a time. Commit after each unit of work with a clear message.

## 10. Writing standards

- British English.
- Plain, direct, concise prose. Short sentences.
- No em dashes. No filler words. No "not X but Y" constructions.
- Learning outcomes use measurable verbs (analyse, apply, evaluate, plan).
- Every unit includes a short, practical workplace scenario so that assessment fits real managers, not only academic readers.

## 11. Acceptance criteria

- No text, item or model from an incumbent appears in any deliverable.
- No document claims accreditation, regulation or equivalence.
- Every qualification has a complete specification, assessment guide and unit set.
- Both profiles have a complete technical manual, item bank, scoring code with tests, and report templates.
- `SOURCES.md` is complete and each source's licence is recorded.
- The name-clash report is delivered.

## 12. Questions to raise with Kris before Phase 2

1. Should Quarterdeck act as the awarding body, or will a separate legal entity own the framework?
2. Is any route to Ofqual recognition wanted later, or does OL stay unregulated?
3. Which licence applies if Quarterdeck wants commercial exclusivity on delivery and certification?
4. Are the profile tools to be hosted by Quarterdeck, and on which platform?
5. Who signs off the human review of the comparison and positioning page?

#!/usr/bin/env python3
# SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck.
"""Builds the five documents of each qualification from the unit bank. Usage:
   python3 tools/build_qualifications.py . [family ...]"""
import re, sys, textwrap
from pathlib import Path

REPO = Path(sys.argv[1])
ONLY = set(sys.argv[2:])
BANK = REPO / "framework/unit-bank"
HDR = "<!-- SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck. -->\n\n"
VERSION = "0.2.0"
FAMILY = {"A. Management": "management", "B. Leadership": "leadership", "C. People practice": "people-practice"}
UNIT = {3: (5, 50, 20), 5: (6, 60, 21), 7: (10, 100, 25)}  # credits, TQT, GLH
CODE = re.compile(r"OL\d-[A-Z]{3}-\d\d")

# title -> (who it is for, purpose, progression)
INFO = {
 "OL Level 3 Award in Management Practice": (
  "A person who is about to start, or has recently started, a first job with responsibility for the work of other people.",
  "The first steps in management: the learner plans and organises the work of a small team and develops one other part of the first-line manager's job.",
  ["OL Level 3 Certificate in Management Practice. Both units count towards it.", "OL Level 3 Award in Leadership Practice."]),
 "OL Level 3 Certificate in Management Practice": (
  "A team leader, supervisor or first-line manager who wants to cover the whole of the job.",
  "The full job of a first-line manager: manage yourself, lead the team, organise the work, and two further areas that fit the learner's role.",
  ["OL Level 5 Certificate in Management Practice.", "OL Level 5 Diploma in Management Practice."]),
 "OL Level 5 Certificate in Management Practice": (
  "A middle manager, or an experienced first-line manager, who wants focused development and has limited time.",
  "The two central tasks of a middle manager, which are the performance of people and the delivery of operations, with one further area that the learner selects.",
  ["OL Level 5 Diploma in Management Practice. All three units count towards it."]),
 "OL Level 5 Diploma in Management Practice": (
  "A middle manager who is responsible for the results of a team, a function or a project, with people and a budget to manage.",
  "The full job of a middle manager: self, team, performance, operations, evidence and money, with one further area that the learner selects.",
  ["OL Level 5 Diploma in Leadership Practice. Three core units count towards it.", "OL Level 7 Certificate in Strategic Management.", "OL Level 7 Diploma in Strategic Management."]),
 "OL Level 7 Certificate in Strategic Management": (
  "A senior manager, or a manager who is moving into a senior role, who wants focused development in strategy.",
  "The development and execution of strategy, with either the operating model or the finance and risk of the organisation.",
  ["OL Level 7 Diploma in Strategic Management. Both units count towards it."]),
 "OL Level 7 Diploma in Strategic Management": (
  "A senior manager or a director who is responsible for a large part of an organisation, or all of it.",
  "The work of a senior manager: lead at senior level, set and execute strategy, and design how the organisation performs, with one further area that the learner selects.",
  ["OL Level 7 Diploma in Strategic Leadership. Two core units count towards it."]),
 "OL Level 3 Award in Leadership Practice": (
  "A person who leads a small team now, or will soon, and wants a short first qualification about people.",
  "The practice of leading a team, with one further area of leading people that the learner selects.",
  ["OL Level 3 Certificate in Management Practice. The core unit counts towards it.", "OL Level 3 Award in Workplace Coaching.", "OL Level 5 Certificate in Leadership Practice."]),
 "OL Level 5 Certificate in Leadership Practice": (
  "A middle manager, a project lead or a professional who leads people and wants focused development with limited time.",
  "Two central tasks of a leader at this level, which are to build a team and to influence people outside it, with one further area that the learner selects.",
  ["OL Level 5 Diploma in Leadership Practice. The two core units count towards it, and so does each optional unit that is in the diploma."]),
 "OL Level 5 Diploma in Leadership Practice": (
  "A middle manager or an experienced leader of people who is responsible for the results and the development of a team.",
  "The full practice of a leader at this level: self, team, performance, influence, change and coaching, with one further area that the learner selects.",
  ["OL Level 5 Diploma in Management Practice. Three core units count towards it.", "OL Level 5 Certificate in Coaching and Mentoring. One unit counts towards it.", "OL Level 7 Diploma in Strategic Leadership."]),
 "OL Level 7 Diploma in Strategic Leadership": (
  "A senior leader or a director who leads other leaders and shapes the direction and culture of an organisation.",
  "The work of a senior leader: lead at senior level, set and execute strategy, and lead leaders and culture, with one further area that the learner selects.",
  ["OL Level 7 Diploma in Strategic Management. Two core units count towards it.", "OL Level 7 Certificate in Senior Coaching and Mentoring."]),
 "OL Level 3 Award in Workplace Coaching": (
  "A manager, team leader or colleague who wants to coach people at work as part of their job.",
  "The skills of a coaching conversation, and supervised practice of coaching at work.",
  ["OL Level 5 Certificate in Coaching and Mentoring."]),
 "OL Level 5 Certificate in Coaching and Mentoring": (
  "A manager or a practitioner who coaches or mentors people regularly, inside one organisation or for clients.",
  "The practice of coaching and mentoring, the conditions that make coaching work in an organisation, and reflective practice.",
  ["OL Level 5 Diploma in Leadership Practice. One unit counts towards it.", "OL Level 7 Certificate in Senior Coaching and Mentoring."]),
 "OL Level 7 Certificate in Senior Coaching and Mentoring": (
  "An experienced coach or mentor who works with senior managers, and a senior leader who coaches other leaders.",
  "Coaching and mentoring at senior level, with supervision and ethics.",
  ["OL Level 7 Diploma in Strategic Leadership. One unit counts towards it."]),
 "OL Level 3 Certificate in People Practice": (
  "A person in a first HR or learning and development role, or a manager or administrator who does people work as part of another job.",
  "The foundations of people practice: what the function does through the employee life cycle, how to handle people records lawfully, and two further areas that fit the learner's role.",
  ["OL Level 5 Diploma in People Practice, in either pathway.", "The grade OL Foundation Practitioner in People Practice, with experience. See the [recognition scheme](../recognition-scheme.md)."]),
 "OL Level 5 Diploma in People Practice (people management pathway)": (
  "An HR adviser, an HR business partner or a people manager in a generalist role, who gives advice and makes decisions without close supervision.",
  "Professional people practice at operational level in resourcing, employee relations and reward, on a base of ethics, evidence and knowledge of organisations.",
  ["OL Level 5 Diploma in People Practice (learning and development pathway). The three shared core units count towards it.", "OL Level 7 Diploma in Strategic People Practice.", "The grade OL Practitioner in People Practice, with experience. See the [recognition scheme](../recognition-scheme.md)."]),
 "OL Level 5 Diploma in People Practice (learning and development pathway)": (
  "A learning and development adviser, designer, trainer or facilitator who plans and delivers learning without close supervision.",
  "Professional learning and development practice: design learning, facilitate it and support learning during work, on a base of ethics, evidence and knowledge of organisations.",
  ["OL Level 5 Diploma in People Practice (people management pathway). The three shared core units count towards it.", "OL Level 7 Diploma in Strategic People Practice.", "The grade OL Practitioner in People Practice, with experience. See the [recognition scheme](../recognition-scheme.md)."]),
 "OL Level 7 Diploma in Strategic People Practice": (
  "A head of people, a senior HR or learning and development manager, or a consultant who shapes people strategy.",
  "People practice at strategic level: lead at senior level, set people strategy and plan the workforce, carry out an applied investigation, and three specialist areas.",
  ["The grade OL Senior Practitioner in People Practice, with experience. See the [recognition scheme](../recognition-scheme.md).", "OL Level 7 Diploma in Strategic Leadership. One core unit counts towards it, and so does each shared optional unit."]),
}

PANEL_Q = {
 3: ["Tell us about one piece of work in your evidence. What did you do, and why did you do it that way?",
     "What did not go as you planned? What did you do then?",
     "Which rule or procedure of your organisation mattered most here? Why does it exist?",
     "What do you do differently now?"],
 5: ["Which decision in this evidence was the hardest? What were the options, and what evidence did you use?",
     "Who saw this situation differently from you? How did that change what you did?",
     "Which idea or model from your learning was useful, and where did it not fit?",
     "How do you know that the result was caused by your action?",
     "What would you do differently, and what will you do next?"],
 7: ["What was the strategic question, and why did it matter to the organisation?",
     "What evidence was missing or in conflict, and how did you decide without it?",
     "Whose interests lost in your decision? How did you deal with that?",
     "Which accepted idea in your field did your work lead you to doubt?",
     "What changed in the organisation because of your work, and how do you know?",
     "What would a critic of your approach say, and how do you answer?"],
}
LEVEL_ROLE = {3: "a team leader, a supervisor or a new first-line manager", 5: "a middle manager or an experienced first-line manager", 7: "a senior manager or a director"}
LEVEL_JUDGE = {
 3: "The learner works within plans and rules that other people set. Good evidence shows that the learner completed defined tasks, selected a suitable method, and can say what worked and what to change. Do not ask for the analysis of theory.",
 5: "The learner is responsible for results and makes decisions within a strategy that other people set. Good evidence shows analysis of a problem, a decision with evidence behind it, and an evaluation of the result with reasons. A description of what happened is not sufficient.",
 7: "The learner makes decisions that have an effect on a large part of the organisation, with incomplete information. Good evidence shows critical evaluation of ideas and data, original thought, and a judgement that the learner can defend. An analysis that only applies a standard model is not sufficient.",
}
PANEL_MIN = {3: 30, 5: 45, 7: 60}


def wrap(s):
    return "\n".join(textwrap.fill(p, 100, break_long_words=False, break_on_hyphens=False) if not p.lstrip().startswith(("|", "-", "#", "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.")) else p for p in s.split("\n"))


def bullets(items):
    out = []
    for i in items:
        out.append(textwrap.fill(i, 98, initial_indent="- ", subsequent_indent="  ", break_long_words=False, break_on_hyphens=False))
    return "\n".join(out)


def read_unit(code):
    t = (BANK / f"{code}.md").read_text()
    title = re.search(r"^# " + code + r": (.+)$", t, re.M).group(1)
    purpose = re.search(r"## Purpose\n\n(.+?)\n\n", t, re.S).group(1).replace("\n", " ")
    los = re.findall(r"^\| (\d\. .+?) \| (.+?) \|$", t, re.M)
    m = re.search(r"Suitable methods: (.+?)\n\n", t, re.S)
    methods = m.group(1).replace("\n", " ").rstrip(".") if m else ""
    assert los and methods, code
    return dict(code=code, title=title, purpose=purpose, los=los, methods=methods, level=int(code[2]))


def parse_map():
    quals, fam = [], None
    for line in (BANK / "README.md").read_text().splitlines():
        if line.startswith("### ") and line[4:] in FAMILY:
            fam = FAMILY[line[4:]]
        elif fam and line.startswith("| OL Level"):
            title, credits, core, opt = [c.strip() for c in line.strip("|").split("|")]
            n = re.match(r"(\d) from(.*?):", opt)
            quals.append(dict(title=title, family=fam, credits=int(credits), core=list(dict.fromkeys(CODE.findall(core))),
                              opt=list(dict.fromkeys(CODE.findall(opt))),
                              n_opt=int(n.group(1)) if n else 0,
                              opt_rule=n.group(2).strip(", ") if n else ""))
        elif line.startswith("## Shared"):
            fam = None
    return quals


def slug(title):
    s = title.replace("OL ", "").replace(" in ", " ").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def ulink(code):
    return f"[{code}](../../../framework/unit-bank/{code}.md)"


def months(tqt):
    lo, hi = round(tqt / 10 / 4.33), round(tqt / 6 / 4.33)
    return f"{lo} to {hi} months"


def build(q, units, allq):
    title = q["title"]
    level = int(re.search(r"Level (\d)", title).group(1))
    size = re.search(r"(Award|Certificate|Diploma)", title).group(1)
    ucred, utqt, uglh = UNIT[level]
    nunits = len(q["core"]) + q["n_opt"]
    assert nunits * ucred == q["credits"], title
    tqt, glh = nunits * utqt, nunits * uglh
    who, purpose, prog = INFO[title]
    purpose = "This qualification covers " + purpose[0].lower() + purpose[1:]
    panel = size != "Award"
    psize = {"Certificate": "two", "Diploma": "three"}.get(size)
    pmin = PANEL_MIN[level]
    badge = f"ol-level-{level}-{size.lower()}.svg"
    name = title.replace("OL ", "Open Leadership ", 1)
    core = [units[c] for c in q["core"]]
    opt = [units[c] for c in q["opt"]]
    rule = f"{q['n_opt']} optional unit{'s' if q['n_opt'] > 1 else ''}" + (f" ({q['opt_rule']})" if q["opt_rule"] else "")
    disclaimer = "Open Leadership is an independent, unregulated framework. This qualification is not regulated by Ofqual and is not on the Regulated Qualifications Framework."
    nav = "Documents for this qualification: [specification](specification.md), [unit summaries](unit-summaries.md), [assessment guide](assessment-guide.md), [centre guide](centre-guide.md), [learner handbook](learner-handbook.md)."
    rules = "../../../framework/credit-and-assessment-rules.md"

    def utable(us):
        return "| Code | Unit | Credits |\n|---|---|---|\n" + "\n".join(f"| {ulink(u['code'])} | {u['title']} | {ucred} |" for u in us)

    can = [re.sub(r"^This unit enables the learner to ", "", u["purpose"]).rstrip(".") for u in core]

    # ---------- specification
    spec = HDR + f"# {title}\n\n## Specification\n\n" + wrap(f"Version {VERSION} (draft). {nav}") + "\n\n"
    spec += f"""| | |
|---|---|
| Title | {title} |
| Level | {level} |
| Size | {size} |
| Credits | {q['credits']} |
| Total qualification time | {tqt} hours |
| Guide for guided learning | {glh} hours |
| Units | {nunits} ({len(core)} core, {q['n_opt']} optional) |
| Assessment | Evidence from work, judged against criteria. No examination |
| Result | Pass |

"""
    spec += wrap(disclaimer) + "\n\n## Purpose\n\n" + wrap(purpose) + "\n\n## Who it is for\n\n" + wrap(who) + "\n\n"
    spec += "A learner who completes the core units can:\n\n" + bullets(can) + "\n\n"
    spec += "## Entry guidance\n\n" + bullets([
        "There are no formal entry requirements.",
        f"The demand is that of Level {level}: the typical learner is {LEVEL_ROLE[level]}. See the [level descriptors](../../../framework/level-descriptors.md).",
        "The learner needs access to real work that can give evidence for each unit. A learner who is not in a suitable role can use a secondment, a project or voluntary work.",
        "The learner needs English at a level that lets them explain their work in writing and in discussion."]) + "\n\n"
    spec += "## Structure\n\n" + wrap(f"The learner completes {len(core)} core unit{'s' if len(core) > 1 else ''}" + (f" and {rule}." if q["n_opt"] else ".") + f" Each unit is {ucred} credits ({utqt} hours of total time, with a guide of {uglh} hours of guided learning).") + "\n\n### Core units\n\n" + utable(core) + "\n\n"
    if opt:
        spec += f"### Optional units\n\nSelect {rule}.\n\n" + utable(opt) + "\n\n"
    spec += wrap("The learning outcomes and assessment criteria of each unit are in its unit file. [Unit summaries](unit-summaries.md) gives a short view of all units.") + "\n\n"
    spec += "## Credit from other learning\n\n" + bullets([
        "A unit that the learner passed for another Open Leadership qualification counts here. The learner does not take it again.",
        "A centre can accept other evidence of prior learning for up to half of the credit. The centre records what it accepted and why."]) + "\n\n"
    spec += "## Assessment methods\n\n" + wrap("Each unit lists the methods that fit it. The centre selects from them. The methods in this qualification are: work-based assignment, portfolio of work evidence, observation at work, witness statement, professional discussion, reflective account, project report and presentation. There are no examinations. The [assessment guide](assessment-guide.md) gives the method for each unit.") + "\n\n"
    spec += "## Grading\n\n" + bullets([
        "Each unit is pass or refer. To pass a unit, the learner meets every assessment criterion.",
        "A referred learner submits more evidence for the criteria that are not met.",
        ("The qualification is passed when all units are passed and the panel review is passed." if panel else "The qualification is passed when both units are passed. An Award has no panel review."),
        "There are no grades above pass."]) + "\n\n"
    spec += "## Evidence requirements\n\n" + bullets([
        "Evidence comes from the learner's own work. Each unit states what evidence is necessary.",
        "The learner signs a statement that the evidence is their own.",
        "A person at work who saw the work, and who is not the assessor, confirms the main evidence.",
        "Records of real people are made anonymous.",
        "If the learner used an AI tool, they say where and how."]) + "\n\n"
    if panel:
        spec += "## Panel review\n\n" + wrap(f"After the units, the learner presents their work to a panel of {psize} people for about {pmin} minutes and answers questions. " + ("At least one member comes from outside the learner's organisation. " if level == 7 else "At least one member comes from outside the learner's team. ") + f"The rules are in section 6 of the [credit and assessment rules]({rules}).") + "\n\n"
    spec += "## Certificate\n\n" + wrap(f"Any organisation can issue the certificate if it followed the process in section 6 of the [credit and assessment rules]({rules}) and keeps the assessment record. The certificate states the version of this specification and this sentence: \"Issued by [organisation] against the Open Leadership specification. Open Leadership is an independent, unregulated framework.\" The holder can use the badge [`{badge}`](../../../badges/{badge}).") + "\n\n"
    spec += "## Progression\n\n" + bullets(prog) + "\n"

    # ---------- unit summaries
    us = HDR + f"# {title}\n\n## Unit summaries\n\n" + wrap(f"Version {VERSION} (draft). {nav}") + "\n\n" + wrap("This page is a short view. The unit file has the assessment criteria, the indicative content, a workplace scenario and the evidence requirements.") + "\n\n"
    for role, group in (("Core", core), ("Optional", opt)):
        if not group:
            continue
        us += f"## {role} units\n\n"
        for u in group:
            us += f"### {ulink(u['code'])}: {u['title']}\n\n{role} unit. {ucred} credits. {utqt} hours.\n\n" + wrap(u["purpose"]) + "\n\nLearning outcomes:\n\n" + "\n".join(textwrap.fill(lo, 98, subsequent_indent="   ", break_long_words=False, break_on_hyphens=False) for lo, _ in u["los"]) + "\n\n"
    us = us.rstrip() + "\n"

    # ---------- assessment guide
    ag = HDR + f"# {title}\n\n## Assessment guide\n\n" + wrap(f"Version {VERSION} (draft). {nav}") + "\n\n" + wrap(f"This guide is for assessors, for the person who makes the second check" + (" and for panel members" if panel else "") + f". It applies the [credit and assessment rules]({rules}) to this qualification. If this guide and the rules disagree, the rules are correct.") + "\n\n"
    ag += "## The standard\n\n" + wrap(f"This is a Level {level} qualification. {LEVEL_JUDGE[level]}") + "\n\n" + bullets([
        "Judge against the assessment criteria of the unit, and nothing else. Do not add requirements.",
        "The learner must meet every criterion. A strong answer to one criterion does not make up for a missing one.",
        "Good writing is not the standard. A plain account with strong work evidence passes. A polished essay with no work evidence does not."]) + "\n\n"
    ag += "## Plan the assessment\n\n" + bullets([
        "Agree an assessment plan with the learner at the start: which work will give evidence, for which units, and by when.",
        "One piece of work can give evidence for more than one unit. Ask the learner to show which criteria each item of evidence meets.",
        "Use the workplace scenario of a unit only if the learner cannot use a case from their own work. Record the reason.",
        "Keep the amount of evidence small. One clear item for each criterion is sufficient."]) + "\n\n"
    ag += "## Methods for each unit\n\n| Unit | Role | Suitable methods |\n|---|---|---|\n" + "\n".join(f"| {ulink(u['code'])} {u['title']} | {r} | {u['methods'][0].upper() + u['methods'][1:]} |" for r, g in (("Core", core), ("Optional", opt)) for u in g) + "\n\n"
    ag += "### How to use each method\n\n| Method | Use it for | Take care that |\n|---|---|---|\n" + "\n".join([
        "| Work-based assignment | A task from the learner's job, with a written account of what they did and why | The task is real, and the learner's own part is clear |",
        "| Portfolio of work evidence | Documents that the learner made at work: plans, records, reports, messages | Each item has a note that says which criterion it meets. Personal data is removed |",
        "| Observation at work | Skills that show in action, such as a meeting or a conversation | The people present agree. The observer records what they saw against the criteria |",
        "| Witness statement | Work that the assessor cannot see | The witness saw the work, states facts, and is not the assessor |",
        "| Professional discussion | Reasons, judgement and depth of knowledge | The assessor keeps a record or a recording, with the criteria that were met |",
        "| Reflective account | What the learner learned and what they will change | It refers to real events. General statements are not evidence |",
        "| Project report | A larger piece of work with a start, an end and a result | The scope fits the level and the learner's authority |",
        "| Presentation | Findings and recommendations to an audience | Questions follow, and the answers are recorded |"]) + "\n\n"
    ag += "## Decisions and feedback\n\n" + bullets([
        "Record a decision for each criterion: met, or not met with the reason.",
        "The unit result is pass or refer. For a refer, tell the learner which criteria are not met and what evidence would meet them.",
        "Give the result and the feedback in writing. We recommend a reply inside 15 working days.",
        "The assessor is not the learner's line manager and has no personal interest in the result."]) + "\n\n"
    ag += "## Authenticity\n\n" + bullets([
        "The learner signs a statement that the evidence is their own work.",
        "A person at work who saw the work confirms the main evidence.",
        "The learner says where and how they used an AI tool. The use of a tool to improve wording is acceptable. Evidence that the learner cannot explain is not acceptable.",
        "If you doubt that the work is the learner's own, hold a professional discussion about it before you decide."]) + "\n\n"
    ag += "## The second check\n\n" + wrap("A second person checks a sample of each assessor's decisions. The second person knows the subject and did not assess that learner.") + "\n\n" + bullets([
        "We recommend that the sample is the first three decisions of a new assessor, then one decision in five.",
        "Include pass and refer decisions, and each unit of the qualification during a year.",
        "If the second person disagrees, the two discuss the evidence against the criteria. If they still disagree, a third person decides. Record the result.",
        "A small organisation can ask a person from another organisation to make the second check."]) + "\n\n"
    if panel:
        ag += "## The panel review\n\n" + wrap(f"The learner presents their work to a panel when all units are passed. The purpose is to confirm that the learner owns the work, can explain their decisions and works at Level {level}. The panel does not mark the units again.") + "\n\n| Rule | For this qualification |\n|---|---|\n" + "\n".join([
            f"| Panel size | {psize.capitalize()} people |",
            "| Chair | A person who has not taught or assessed the learner |",
            "| Independent member | " + ("At least one member from outside the learner's organisation" if level == 7 else "At least one member from outside the learner's team") + " |",
            f"| Subject member | At least one member who practises at Level {level} or above |",
            f"| Length | About {pmin} minutes |",
            "| Decision | Pass or refer, by agreement, with written reasons |"]) + "\n\n"
        ag += "### Before the panel\n\n" + bullets([
            "Give the members the evidence index and the assessor's decisions one week before.",
            "Each member states in writing that they are independent as the rules require.",
            "Tell the learner the date, the members and the format. Ask about adjustments that the learner needs."]) + "\n\n"
        ag += "### During the panel\n\n" + wrap(f"The learner presents for about {pmin // 3} minutes. The panel then asks questions. Questions that fit this level:") + "\n\n" + bullets(PANEL_Q[level]) + "\n\n" + wrap("Ask about the learner's real work. Do not test recall of theory. Give the learner time to think.") + "\n\n"
        ag += "### The decision\n\nThe panel passes the learner if all of these are true:\n\n" + bullets([
            "The learner explains the work in the evidence in their own words.",
            "The learner gives reasons for their decisions.",
            f"The answers show the knowledge, skills and scope of Level {level}.",
            "The learner can say what they would do differently."]) + "\n\n" + wrap("If the panel refers the learner, it gives written reasons and says what the learner must show. The learner can return to a panel one time.") + "\n\n"
    ag += "## The assessment record\n\nKeep this record for each certificate for six years from the date of the certificate, then delete it:\n\n" + bullets([
        "the learner's name, the qualification title and the version of the specification",
        "the units, with the assessor's decision and date for each",
        "an index of the evidence",
        "the record of the second check, if the learner was in the sample"] + (["the names and roles of the panel members, with a statement of independence from each", "the panel's decision, reasons and date"] if panel else [])) + "\n\n" + wrap("Give the learner a copy.") + "\n"

    # ---------- centre guide
    cg = HDR + f"# {title}\n\n## Centre guide\n\n" + wrap(f"Version {VERSION} (draft). {nav}") + "\n\n" + wrap("A centre is an organisation that delivers or assesses this qualification: an employer, a training provider, a college, a charity or a group of practitioners. You do not need approval, and there is no fee. You are responsible for the quality of what you do and for the truth of what you say about it.") + "\n\n" + wrap(disclaimer) + "\n\n"
    people = ["A tutor, coach or facilitator who guides the learning.",
              f"An assessor who knows the subject and holds, or works at, Level {level} or above. The assessor is not the learner's line manager.",
              "A second person who checks a sample of the assessor's decisions."]
    if panel:
        people.append(f"A panel of {psize} people for each learner at the end. The chair has not taught or assessed the learner. " + ("One member comes from outside the learner's organisation." if level == 7 else "One member comes from outside the learner's team."))
    people.append("One person can have more than one of these roles for different learners. A small organisation can share assessors" + (", second checkers and panel members" if panel else " and second checkers") + " with another organisation.")
    cg += "## The people you need\n\n" + bullets(people) + "\n\n"
    cg += "## Time\n\n| | |\n|---|---|\n" + f"| Total qualification time | {tqt} hours |\n| Guide for guided learning | {glh} hours |\n| Typical duration | {months(tqt)}, at 6 to 10 hours each week |\n\n" + wrap("Total time includes guided learning, private study, practice at work and assessment. Much of it is work that the learner does in their job. The guide for guided learning is a guide. Use more or less if the learner can still meet the outcomes.") + "\n\n"
    seq = core + opt[: q["n_opt"]]
    cg += "## A delivery plan\n\n" + wrap("This plan is an example. Change the order to fit the learner's work.") + "\n\n| Step | Unit | Guided learning | Suggested form |\n|---|---|---|---|\n"
    cg += "| 1 | Start | 2 hours | Explain the qualification. Agree the assessment plan and the optional unit" + ("s" if q["n_opt"] > 1 else "") + " |\n" if q["n_opt"] else "| 1 | Start | 2 hours | Explain the qualification. Agree the assessment plan |\n"
    for i, u in enumerate(seq, 2):
        label = f"{u['code']} {u['title']}" if u in core else f"Optional unit (for example {u['code']} {u['title']})"
        cg += f"| {i} | {label} | {uglh} hours | Workshops or coaching sessions, practice at work between them, then assessment |\n"
    if panel:
        cg += f"| {len(seq) + 2} | Panel review | {pmin} minutes for each learner | See the assessment guide |\n"
    cg += "\n" + bullets([
        "Units can run one after the other or together. Start each unit with the work that will give the evidence.",
        "Guided learning can be in a room or online, in a group or one to one.",
        "Use the workplace scenario of each unit for discussion.",
        "All Open Leadership material is free to copy and adapt. You can add your own material."]) + "\n\n"
    cg += "## Support for learners\n\n" + bullets([
        "Check at the start that the learner's work can give the evidence. If it cannot, agree a project, a secondment or another source with the learner's manager.",
        "Ask the learner's manager to give time for the work and to be, or to name, a witness.",
        "Make reasonable adjustments so that a disabled learner is not at a disadvantage. Change the method of assessment, never the criteria. For example, replace a written account with a recorded discussion.",
        "Give each learner the [learner handbook](learner-handbook.md)."]) + "\n\n"
    cg += "## Assessment and quality\n\n" + wrap("Follow the [assessment guide](assessment-guide.md). In short:") + "\n\n" + bullets([
        "an assessor judges each unit against its criteria",
        "a second person checks a sample",
        (f"a panel of {psize} reviews each learner at the end" if panel else "there is no panel for an Award"),
        "you keep the assessment record for six years, then delete it"]) + "\n\n" + wrap("We recommend a simple appeal route: a learner who disagrees with a decision can ask for a review by a person who took no part in it. Tell learners about the route at the start.") + "\n\n"
    cg += "## Records and personal data\n\n" + bullets([
        "The assessment record contains personal data. You are the controller of that data under UK data protection law.",
        "Tell the learner what you keep, why, and for how long.",
        "Keep an index of the evidence. The evidence itself can stay with the learner or the employer.",
        "Show the record to a person who asks to verify a certificate only with the learner's permission."]) + "\n\n"
    cg += "## Certificates, badges and what you can say\n\n" + bullets([
        f"Issue the certificate in your own name. It states the learner's name, the full title \"{title}\", the version of the specification, the date, and this sentence: \"Issued by [organisation] against the Open Leadership specification. Open Leadership is an independent, unregulated framework.\"",
        f"The learner and your organisation can use the badge [`{badge}`](../../../badges/{badge}) with reference to that learner or that programme. Do not change the words on it.",
        "You can say that your programme \"leads to\" or \"is assessed against\" this qualification.",
        "Do not say or imply that the qualification, your programme or your organisation is accredited, regulated, endorsed or approved by a regulator, an awarding organisation, a professional body or Quarterdeck."]) + "\n\n"
    cg += "## Tell us what you learn\n\n" + wrap("If a unit, a criterion or this guide does not work in practice, open an issue in the repository. See [how to contribute](../../../CONTRIBUTING.md).") + "\n"

    # ---------- learner handbook
    lh = HDR + f"# {title}\n\n## Learner handbook\n\n" + wrap(f"Version {VERSION} (draft). {nav}") + "\n\n"
    lh += "## What this qualification is\n\n" + wrap(purpose) + "\n\n" + wrap(f"It is at Level {level}. That is the level of work of {LEVEL_ROLE[level]}. It has {nunits} units and {q['credits']} credits. One credit is 10 hours, so the total time is about {tqt} hours. A typical duration is {months(tqt)}.") + "\n\n"
    lh += "## What it is not\n\n" + wrap("Open Leadership is an independent, unregulated framework. This qualification is not regulated by Ofqual, and no awarding organisation or professional body accredits it. Its value comes from the work that you show and from the open standard that anyone can read. An employer can check exactly what you did to get it.") + "\n\n"
    lh += "## What you study\n\n" + wrap(f"You complete {len(core)} core unit{'s' if len(core) > 1 else ''}" + (f" and {rule}. Select the optional unit{'s' if q['n_opt'] > 1 else ''} with your tutor and your manager, to fit your job." if q["n_opt"] else ".")) + "\n\n| Unit | What you learn to do |\n|---|---|\n"
    for r, g in (("core", core), ("optional", opt)):
        for u in g:
            lh += f"| {ulink(u['code'])} {u['title']} ({r}) | " + re.sub(r"^This unit enables the learner to ", "", u["purpose"]).rstrip(".").replace("their own", "your own").replace("their development", "your development").replace("their growth", "your growth").replace("their area", "your area").replace("their organisation", "your organisation").replace("their team", "your team").capitalize() + " |\n"
    lh += "\n" + wrap("If you passed one of these units for another Open Leadership qualification, it counts. You do not take it again.") + "\n\n"
    lh += "## How you spend the time\n\n" + bullets([
        f"Guided learning: about {uglh} hours for each unit with a tutor, coach or facilitator.",
        "Private study: reading and thinking.",
        "Practice at work: you use what you learn in your job. This is the largest part.",
        "Assessment: you collect and explain your evidence."]) + "\n\n"
    lh += "## How you are assessed\n\n" + wrap("There are no examinations. You show each learning outcome with evidence from your own work. Each unit has assessment criteria, and you must meet every one.") + "\n\n" + bullets([
        "At the start, you agree an assessment plan with your assessor.",
        "You collect evidence: documents from your work, accounts of what you did, statements from people who saw your work, a discussion with your assessor.",
        "Your assessor decides pass or refer for each unit. Refer means that some criteria are not met yet. Your assessor tells you which, and you give more evidence.",
        "A second person checks some of the assessor's decisions, so that the standard is the same for everybody."]) + "\n\n"
    lh += "### Good evidence\n\n" + bullets([
        "It is about real work that you did. Say \"I\", and say what your part was.",
        "It shows the criterion. Write the number of the criterion next to each item.",
        "It is short. One clear item for each criterion is sufficient. One item can serve more than one criterion.",
        "It protects other people. Remove names and personal details.",
        "A person at work who saw the work confirms it."]) + "\n\n"
    lh += "### AI tools\n\n" + wrap("You can use an AI tool to help you write. Say where and how you used it. The work and the thinking must be yours. " + ("The panel will ask you to explain your work without notes from a tool." if panel else "Your assessor can ask you to explain any part of your evidence.")) + "\n\n"
    if panel:
        lh += "## The panel review\n\n" + wrap(f"When you have passed all units, you present your work to a panel of {psize} people. It takes about {pmin} minutes. The model is the oral examination of a research degree, at a smaller scale.") + "\n\n" + bullets([
            f"You speak for about {pmin // 3} minutes about what you did, why, and what you learned.",
            "The panel asks questions about your evidence, your decisions and what you would do differently.",
            "The panel does not test your memory of theory. It wants to hear that the work is yours and that you understand it.",
            "At least one member does not know you" + (" and comes from outside your organisation." if level == 7 else " from your daily work."),
            "The result is pass or refer, with written reasons. If you are referred, you can return one time.",
            "Tell your centre before the day if you need an adjustment."]) + "\n\n" + "Questions that you can expect:\n\n" + bullets(PANEL_Q[level]) + "\n\n"
    lh += "## Your certificate and badge\n\n" + bullets([
        "The organisation that assessed you issues your certificate. It states the title, the version and the date.",
        "You get a copy of your assessment record. Keep it. It is the proof behind your certificate.",
        f"You can show the badge [`{badge}`](../../../badges/{badge}) on your profile or your email signature.",
        "Write the title in full: \"" + title + "\". Do not describe it as accredited or regulated."]) + "\n\n"
    lh += "## If something goes wrong\n\n" + bullets([
        "If you disagree with a decision, ask your centre for a review by a person who took no part in it.",
        "If your job changes and you can no longer get evidence, tell your assessor. You can agree a project or another source.",
        "Units that you passed stay passed. You can stop and continue later."]) + "\n\n"
    lh += "## What next\n\n" + bullets(prog) + "\n"

    d = REPO / "qualifications" / q["family"] / slug(title)
    d.mkdir(parents=True, exist_ok=True)
    for fn, body in (("specification.md", spec), ("unit-summaries.md", us), ("assessment-guide.md", ag), ("centre-guide.md", cg), ("learner-handbook.md", lh)):
        assert "—" not in body and "–" not in body
        (d / fn).write_text(body)
    return d


quals = parse_map()
assert len(quals) == 17, len(quals)
units = {}
done = []
for q in quals:
    if ONLY and q["family"] not in ONLY:
        continue
    for c in q["core"] + q["opt"]:
        if c not in units:
            units[c] = read_unit(c)
    done.append((q, build(q, units, quals)))

# index (only the families that exist on disk)
idx = HDR + "# Qualifications\n\n" + wrap(f"Version {VERSION} (draft). Each qualification is a set of units from the [unit bank](../framework/unit-bank/README.md). Each has five documents: a specification, unit summaries, an assessment guide, a centre guide and a learner handbook. Open Leadership is an independent, unregulated framework.") + "\n\n"
names = {"management": "Management", "leadership": "Leadership", "people-practice": "People practice"}
for fam in names:
    rows = [q for q in quals if q["family"] == fam and (REPO / "qualifications" / fam / slug(q["title"])).exists()]
    if not rows:
        continue
    idx += f"## {names[fam]}\n\n| Qualification | Credits | Documents |\n|---|---|---|\n"
    for q in rows:
        p = f"{fam}/{slug(q['title'])}"
        idx += f"| {q['title']} | {q['credits']} | [Specification]({p}/specification.md), [units]({p}/unit-summaries.md), [assessment]({p}/assessment-guide.md), [centre]({p}/centre-guide.md), [learner]({p}/learner-handbook.md) |\n"
    idx += "\n"
    if fam == "people-practice" and (REPO / "qualifications/people-practice/recognition-scheme.md").exists():
        idx += "See also the [competence framework](people-practice/competence-framework.md) and the [recognition scheme](people-practice/recognition-scheme.md).\n\n"
(REPO / "qualifications/README.md").write_text(idx.rstrip() + "\n")
print("built", len(done))

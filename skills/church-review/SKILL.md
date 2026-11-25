---
name: church-review
description: Review a church's or Christian organisation's policies and practice - safeguarding, leadership and pastoral care, money, governance and accountability, complaints, and how it treats staff and volunteers - against the Christian Guidelines (the safeguarding, church leadership and work areas, and the general rules on the church, money, speech and justice). Produces a findings report in which every finding cites its rule ID and source, says what the church does well, and lists questions the churches answer differently without taking sides. Use when asked to review, audit or check a church's safeguarding policy, handbook, constitution, finance procedures, code of conduct or governance, or to prepare for an inspection or a new leader.
argument-hint: "[path | document | description]"
---

# Church review

Review the church or organisation against the guidelines. Every finding has to be traceable to a written rule and its source. This is a review against shared Christian guidelines, not a legal or regulatory audit: where something depends on the law, such as safeguarding law, charity law or employment law, name the area and recommend checking with the church's safeguarding adviser, its denomination or a lawyer.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. You need:

- `<root>/RULES.md`: every rule with its ID, score and main source
- `<root>/specific/safeguarding/README.md` (`SAFE`), `<root>/specific/church-leadership/README.md` (`LEAD`) and `<root>/specific/workplace/README.md` (`BIZ`, for employers)
- `<root>/general/church.md` (`CHURCH`), `money.md` (`MONEY`), `speech.md` (`SPEECH`), `justice.md` (`JUST`) and `work.md` (`WORK`)
- `<root>/traditions/<church>.md`: the page of the church's own tradition

## First: if a child or adult may be at risk now

If the material or the conversation shows that someone may be at risk of abuse now, or that an allegation hasn't been reported, stop the review and say so first: the concern must go to the church's safeguarding lead and to the statutory authorities (police or social services) at once, under `SAFE-1` and `CHURCH-6`. A review is no substitute for reporting.

## 1. Scope

Work out what to review from the request (`$ARGUMENTS` if given): a folder of policies, one document, a description of how the church works, or answers the person gives you. Ask once, briefly, for what is missing, for example: "Do you have a written safeguarding policy? Who counts the collection? Who oversees the minister?" Then state your assumptions and continue. Don't invent facts about the church; record what you don't know as a gap.

Note the church's tradition and size. A small congregation needs simple arrangements, not a large organisation's procedures; judge it by what is reasonable for its size, and say so.

## 2. Review

Go through the areas below, highest-scored rules first. For each, look for evidence in the documents, and quote the file and passage. Read each rule in its file, with its "How to apply" practices: their absence is often a finding.

| Area | Look for | Rules |
| --- | --- | --- |
| Safeguarding | A written policy, a named safeguarding lead, how concerns are reported (and to the authorities, not only internally), safer recruitment and training, two-adult and open working, online contact with children, care for survivors, agreements for people who may pose a risk | `SAFE-1` to `SAFE-7`, `CHURCH-6` |
| Leaders and pastoral care | A code of conduct, oversight of the minister and leaders, boundaries in pastoral relationships, confidentiality and its limits, support and rest for leaders, sharing of leadership | `LEAD-1` to `LEAD-7`, `CHURCH-4` |
| Money | Two unrelated people counting and recording gifts, separation of the church's money from leaders' own, approval of spending, published accounts, honest fundraising | `LEAD-5`, `MONEY-1`, `MONEY-6` |
| Complaints and disagreement | How members can raise a concern about a leader, how disputes are handled, protection for those who speak up | `SAFE-3`, `CHURCH-4`, `CHURCH-5`, `SPEECH-2` |
| Staff and volunteers | Fair pay and conditions, safe work, fair recruitment, rest | `WORK-2`, `WORK-4`, `BIZ-4`, `BIZ-5` |
| Welcome and justice | Welcome for strangers and people with disabilities, care for the poor | `JUST-1`, `JUST-2`, `JUST-4` |

Also:

- Note what the church does well, with the rule it meets. A review that only lists problems is less useful and less fair.
- If something seems wrong but no rule covers it, put it under "Not covered by the guidelines" as your own observation, without a rule ID.
- If a finding touches a question the churches answer differently, such as how the church is governed, who may be ordained or the seal of confession, don't decide it. List it under "Questions the churches answer differently", with the positions and the source from the open question, and judge the church by its own tradition's rules where that is the question.

## 3. Report

Every finding must include the rule's source link, copied exactly from the guideline file:

```markdown
## Church review: <church or document>

**Tradition and size:** <…> · **Reviewed:** <documents or information> · **Guidelines applied:** specific/safeguarding, specific/church-leadership, general/…

### Summary
<2–4 sentences: the main risks, especially to children and vulnerable adults, and what the church does well>

### Findings
| # | Priority | Finding | Evidence | Rule | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | High | <what is missing or wrong, and who could be harmed> | `safeguarding-policy.md`, section 3 | `SAFE-1` (9): "Report every concern…" | [<source title>](<source link>) |

### What the church does well
- <practice, with the rule it meets>

### Recommendations
1. <a concrete step, linked to finding numbers, using a practice from the area's "How to apply" section where one exists>

### Questions the churches answer differently
- <question>: <positions, neutrally> ([source](…))

### Not covered by the guidelines
- <observation (opinion, no rule ID)>
```

Priority starts from the rule's score: 9–10 usually High, 6–8 Medium, 1–5 Low. Raise it where children or vulnerable adults could be harmed, and say why when you move a finding up or down. Safeguarding gaps that could leave someone at risk are always High.

End by recommending that the church's leaders discuss the report with their safeguarding adviser or denomination, and that the review be repeated each year.

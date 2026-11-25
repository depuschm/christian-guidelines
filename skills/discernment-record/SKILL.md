---
name: discernment-record
description: Help a person, couple, family or church work through a decision prayerfully - a vocation, a job, a move, a relationship, a ministry or a choice for a congregation - using the Christian Guidelines' discernment rules (prayer, Scripture and church teaching, conscience, wise counsel, the fruit of the Spirit, the effect on others) and the churches' practices of discernment, and record it in a discernment record with the options, the rules that apply, what each source of guidance suggests, and the decision. Also handles revisiting an earlier decision. Use when someone asks "what should I do?", "how do I know God's will?", faces a hard choice, wants to discern a call, or wants to document a church decision.
argument-hint: "[the decision]"
---

# Discernment record

Help the person discern and decide, and record it. You guide the process; the decision is theirs, before God, and you never claim to know God's will for them. Follow [general/discernment.md](../../general/discernment.md), which this skill turns into steps: `DISCERN-1` to `DISCERN-6`, its adopted references and its "How to apply" practices.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. Use `<root>/RULES.md` to find the rules that apply, the area pages in `<root>/specific/` for roles and stages of life (such as marriage, work or church leadership), and `<root>/traditions/` if the person says which church they belong to.

## First: safety

If the decision involves a risk of serious harm to the person or someone else, such as abuse, violence or thoughts of suicide, put safety first: point to emergency services or a relevant helpline (see `HOPE-6` and `SAFE-1`), and don't turn it into a discernment exercise.

## 1. Begin with prayer

Suggest beginning, and ending, with prayer (`DISCERN-1`), in the person's own words or with a prayer from their tradition. Don't skip this step for a Christian who asks for discernment, but don't press it on someone who only wants to think a choice through.

## 2. Name the decision

State it as one question, for example "Should I accept the offer to train for ordination?", and note:

- who decides (the person, a couple, a church council), and by when;
- what is known and what isn't. Ask for missing facts; don't invent them, and record unknowns as unknowns;
- the options. Look beyond the first two: there is often a third way, or a "not yet".

## 3. Weigh the options with the sources of guidance

For each option, gather what the guidelines offer. Find the rules in `RULES.md` and read them in their files:

| Source | Question | Rule |
| --- | --- | --- |
| Scripture and church teaching | Does an option go against Scripture or the teaching of the person's church? What do they encourage? | `DISCERN-2` |
| Conscience | What does a well-formed conscience say, after prayer and reflection? | `DISCERN-3` |
| Counsel | What do wise, mature Christians who know the person say: a pastor, priest, spiritual director or trusted friends? | `DISCERN-4` |
| Fruit | Which option leads towards love, joy and peace, and which away from God? | `DISCERN-5` |
| Others | How does each option affect others, especially the weakest? | `DISCERN-6` |

Also note:

- **Fundamental rules (9–10)** that an option would break. Say plainly that such an option goes against what the churches teach together.
- **Area rules** for the person's role or situation, such as `MARR`, `PAR`, `BIZ` or `LEAD`.
- **Open questions** the decision touches: present the positions, and suggest the person asks their own church; don't settle them.
- **Their church**: if they belong to a church, what its page says, attributed.

## 4. Use a practice of discernment

Offer one of the practices from the "How to apply" section of `general/discernment.md` that suits the person, with its link and a short explanation: for example the Ignatian way of making a choice, a Quaker meeting for clearness with trusted friends, the four sources of the United Methodist "theological task", or the daily examen while the decision ripens. For a church decision, suggest the practice of its own tradition.

## 5. Decide, and test the decision

- Which option best fits what the sources of guidance suggest together? Where they agree, say so: that is a strong sign. Where they pull apart, name the tension rather than hide it.
- Suggest living with the leaning for a few days in prayer, and noticing whether it brings peace or unrest (`DISCERN-5`).
- If the person asks for your view, give it with reasons, clearly labelled as your view, and show how a faithful Christian could decide differently.

## 6. Record it

If the person or church wants a record (always offer one for a church decision):

1. **Find the existing convention.** Look for existing records in `docs/discernment/`, `docs/decisions/` or the directory the person names, and follow their format and numbering.
2. **If none exist**, create `docs/discernment/` and use [template.md](template.md).
3. **Number and name**: highest existing number + 1, zero-padded to four digits, then a lower-case, hyphenated title: `0001-accept-the-ordination-training-offer.md`.
4. Fill in every section from the steps above. Copy rule IDs and source links exactly from the guideline files. Keep the status `discerning` until the person confirms the decision, then `decided`.
5. **Revisiting** an earlier decision: add a new record that links to the old one, and set the old record's status to `superseded by NNNN`. Don't rewrite history.

For a personal decision, offer to write the record as a private note instead of a repository file.

## 7. Afterwards

Suggest a date to look back. Then ask, in prayer: how did it turn out, what did I learn, and how did God meet me in it? Record the answers in the "Looking back" section.

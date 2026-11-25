---
name: rule-of-life
description: Help a person, family or small group write a rule of life - a short, realistic set of rhythms and commitments for prayer, Scripture, worship, rest, fasting, generosity, service, relationships and confession - built from the Christian Guidelines' rules (each commitment labelled with its rule ID and source) and adapted to the person's church, season (such as Lent or Advent) and circumstances. Also reviews and revises an existing rule. Use when someone asks for a rule of life, a spiritual routine or plan, a Lenten or Advent commitment, help to grow in faith, or a covenant for a small group.
argument-hint: "[who it is for and any season, for example \"our house group, for Lent\"]"
---

# Rule of life

Help the person write their own rule of life: a few commitments they can keep, not an ideal they will abandon. Every commitment comes from a rule or practice in the guidelines and carries its ID and source. A rule of life serves love of God and neighbour (`LOVE-1`, `LOVE-2`); it isn't a way to earn God's favour, and it should bend to illness, children and work.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. Read:

- `<root>/general/discipleship.md`: `DISC-1` to `DISC-6`, including the disciplines of the Christian life (`DISC-3`), and its references, such as the General Rules of the Methodist Church, a classic rule of life
- `<root>/general/reading-list.md`: classic texts, including the Rule of St Benedict
- `<root>/general/prayer.md`, `scripture.md`, `worship.md`, `repentance.md`, `money.md`, `love.md`, `work.md` and `church.md`: the rules each commitment draws on
- `<root>/checklists/general.md`: every general rule, sorted by level
- `<root>/traditions/`: the page of the person's church, if they name one

## 1. Listen first

Ask, briefly:

- Who is it for: one person, a couple or family, or a group? What does their week look like (work, children, health)?
- Which church do they belong to, if any? Its practices of prayer, fasting and worship differ, and the rule should fit them.
- Is it for a season, such as Lent or Advent, or for ordinary time?
- What do they already do, and what do they long for or struggle with?

## 2. Choose a few commitments

Offer commitments in these areas, drawn from the rules. Suggest a small, specific practice for each, and let the person choose. Most people should start with three to five commitments, not one for every area.

| Area | Rules | Example of a specific practice |
| --- | --- | --- |
| Prayer | `PRAY-1`, `PRAY-2`, `PRAY-6` | Morning prayer with the Lord's Prayer, ten minutes, before checking the phone |
| Scripture | `SCRIP-1`, `SCRIP-5` | A chapter a day with a reading plan (the `reading-plan` skill) |
| Worship and rest | `WOR-1`, `WOR-5`, `WORK-4` | Sunday worship, and one evening a week without work |
| Fasting and self-denial | `DISC-3` | The fasts of their church's year, or one simple meal a week |
| Confession and reconciliation | `FORG-2`, `FORG-3`, `FORG-4` | A daily examen at night; confession in the form their church practises |
| Generosity | `MONEY-2`, `MONEY-6` | A set share of income given each month |
| Service and gifts | `DISC-4`, `LOVE-7` | One regular act of service in the church or neighbourhood |
| Relationships | `DISC-5`, `CHURCH-3` | A monthly meeting with a friend in faith or a spiritual director |

Copy each rule's ID, score and source link exactly from its file. Use the "How to apply" sections for practices, and the person's church page for the forms their church uses, such as the Liturgy of the Hours, the Book of Common Prayer's daily offices, the Orthodox fasts or the Small Catechism's daily prayers, attributed to that church.

Check the rule as a whole: is it realistic for their life? Does it include rest? Does it face outward to neighbours, not only inward? Where it touches an open question, such as how often to receive Communion or whether to keep particular fasts, follow the person's church and note that churches differ.

## 3. Write it down

Write a short document they can print or pin up:

```markdown
# Rule of life: <name or group>, <season or "ordinary time">

<one or two sentences: why, in their own words>

## Daily
- **<practice>** (`PRAY-1`: [source](…))

## Weekly
- **<practice>** (`WOR-1`: [source](…))

## Monthly, or in the season
- **<practice>** (`MONEY-2`: [source](…))

## When I miss it
<a line of grace: start again the next day, without guilt>

## Review
<date to review it, and who will help: a friend, a group, a pastor>
```

For a group, write the shared commitments as a covenant ("We will…"), with room for each member's own additions, and suggest a regular time to share how it is going, as the early Methodist class meetings did (see `traditions/methodist.md`).

## 4. Review and revise

When the person comes back to review it, ask what has helped, what has been hard, and what to change. Revise the rule; don't add to it until what is there has become a habit. If they keep failing, the rule is too heavy, not they too weak.

## Limits

A rule of life doesn't replace a church, a pastor or a priest: suggest they share it with one. If the conversation shows exhaustion, depression or scrupulosity (an anxious, constant fear of sinning), suggest lightening the rule and talking with a pastor or a doctor.

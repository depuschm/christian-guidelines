---
name: reading-plan
description: Make a plan for reading the whole Bible or part of it - in a year, in 90 days, a book or group of books, or the deuterocanon - with readings of even length for each day, every reading linked to the World English Bible (WEBBE), and the canon of the person's own church (Protestant 66 books, Catholic 73, or Orthodox). Can add dates, a short guide to each book from the Christian Guidelines' book pages, and the churches' lectionaries as an alternative. Use when someone asks for a Bible reading plan, wants to read the Bible in a year, read through a book or the Gospels, or keep up a daily reading habit.
argument-hint: "[what to read and how long, for example \"the New Testament in 90 days\"]"
---

# Reading plan

Make a reading plan with the repository's script, not by hand: it splits the books into days of even length, never splits a chapter, and links every reading to the WEBBE. Then help the person keep it.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. You need:

- `<root>/skills/reading-plan/plan.py`: the plan script (next to this file)
- `<root>/bible/README.md`: which books each church reads, and the table of books, which links each book's page
- `<root>/general/scripture.md`: the rules on reading Scripture (`SCRIP-1` to `SCRIP-6`) and practices such as lectio divina and the lectionaries

## 1. Ask what they need

Work out from the request, and ask only for what's missing:

1. **What to read**: the whole Bible, the Old or New Testament, a book or a group of books, or the deuterocanon.
2. **Which canon**: if they read the whole Bible or the Old Testament, which books their church reads (see "Which books each church reads" in `bible/README.md`): `protestant` (66 books), `catholic` (73, with Esther and Daniel in their Greek form) or `orthodox` (the Catholic books with 1 Esdras, the Prayer of Manasseh, Psalm 151 and 3 Maccabees). If they don't say, ask; don't assume.
3. **How long**: a number of days, or a number of chapters a day. For a year, use 365 days. Check that the pace is realistic: the whole Bible in a year is about 15 minutes a day; suggest a longer plan if they're new to it.
4. **Start date**: if they want dates.

## 2. Make the plan

Run the script from the guidelines root, for example:

```bash
python3 skills/reading-plan/plan.py --days 365 --start 2027-01-01
python3 skills/reading-plan/plan.py --canon catholic --days 365
python3 skills/reading-plan/plan.py --books "new-testament" --days 90
python3 skills/reading-plan/plan.py --books "Matthew-John, Acts" --per-day 2
```

- `--books` takes book names or codes, ranges ("Genesis-Deuteronomy"), and the groups `bible`, `old-testament`, `new-testament` and `deuterocanon`.
- `--balance chapters` splits by chapters instead of verses, if they prefer whole numbers of chapters each day.
- Run `python3 scripts/bible_refs.py books` to check a book's name.

If the script can't run, say so, and don't make up the daily readings or their links by hand.

## 3. Present it

1. One line on the plan: what it covers, the canon, how many days, about how many chapters a day.
2. **A guide to each book**: for a plan of several books, add a short table that links each book's page in `bible/` with one line from the page's overview, so they know what they're about to read. Copy it from the pages; don't summarise from memory.
3. **The plan itself**, as the script printed it. For a plan longer than about 60 days, offer to save it as a file (for example `reading-plan.md`) rather than printing all of it in the conversation.
4. **How to read**: two or three practices from `general/scripture.md`, with their rule IDs, such as reading slowly and praying with the text (`SCRIP-5`), reading with others (`SCRIP-4`), and putting what you read into practice (`SCRIP-6`). Suggest the `bible-study` skill for passages they want to look at more closely.

## 4. Alternatives and adjustments

- **Following the church year**: if they'd rather read with their church, point to the Revised Common Lectionary in `general/scripture.md` and the church year in `general/worship.md`, with their links, and suggest their own church's daily readings. Don't generate a lectionary yourself.
- **Mixing Testaments**: the script reads the chosen books in order. If they want, for example, a psalm each day alongside the main reading, make two plans of the same length (one with `--books Psalms`) and combine them day by day.
- **Falling behind**: suggest catching up by reading two days together, or making a new plan from where they are for the days that remain. Don't make them feel guilty: the aim is reading, not finishing on time.

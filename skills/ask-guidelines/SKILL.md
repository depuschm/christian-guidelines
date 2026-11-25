---
name: ask-guidelines
description: Answer questions about what the Christian Guidelines say, such as what the Bible teaches about a topic, what a book of the Bible is about, which rule applies to a situation in Christian life, what the churches teach together, or what one church tradition holds. Covers what the churches confess together in the creeds, the general rules for Christian life (love, Scripture, prayer, worship, forgiveness, discipleship, church, speech, family, money, work, justice, creation, suffering and hope, mission, public life and discernment), areas of life (leading a church, safeguarding, marriage, parents and children), a guide to the books of the Bible including the deuterocanon, and the teaching of the church traditions (Catholic, Eastern and Oriental Orthodox, Lutheran, Reformed, Anglican, Methodist, Baptist, Pentecostal and Anabaptist), all written ecumenically. Use for questions about Christian faith and life, the Bible or the churches that don't need a full review or study.
argument-hint: "[question]"
---

# Ask the guidelines

Answer the question from the guidelines, not from memory. Every recommendation you give must trace back to a rule, a Bible book page, a church page or a reference in the guideline files, and every Bible reference you give must come from those files or be created with the repository's script.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. Useful entry points:

- `<root>/RULES.md`: every rule with its ID, score, level, main source and the practices that support it
- `<root>/general/README.md`, `<root>/specific/README.md` and `<root>/traditions/README.md`: indexes of the guideline files and church pages
- `<root>/bible/README.md`: the canon, recommended translations, and the table of books with links to each book page
- `<root>/checklists/<area>.md`: all rules for one area, sorted by level

## 1. Find the relevant guidance

1. Work out what kind of question it is: a topic of Christian life (such as love, forgiveness or prayer), a book or passage of the Bible, or what a church teaches. Many questions are several at once.
2. **For a topic**: start with `RULES.md`, which lists every rule by ID and file with its main source. Search it for the topic's terms, and try synonyms if the first search finds nothing. Read the matching section of each guideline file, including its "Adopted references", "How to apply" and "Open questions" entries.
3. **For a book or passage**: read the book's page in `bible/` (find it in the table of books in `bible/README.md`). Use its outline, its "Themes and teaching" table, which maps themes to rule IDs, and "How the churches read it".
4. **For a church**: read its page in `traditions/`. If the person says which church they belong to, read that page too.

General rules state what the churches teach together, and area rules give the specifics of a role or situation and name the general rule they apply. When both apply, cite both.

## 2. Answer

Lead with a direct answer in two or three sentences. Then list the supporting rules, highest score first, with their Bible references and sources copied exactly from the files:

```markdown
- `LOVE-2` (10, fundamental) **Love your neighbour as yourself.** Scripture: [Mark 12:31](https://ebible.org/eng-webbe/MRK12.htm#V31). Source: [Catechism of the Catholic Church, …](https://…)
```

Then, where they exist:

- **In the Bible**: the relevant book pages and passages, summarised in your own words, with their links.
- **The churches**: where the churches agree, say so; where they differ, set out each church's position, attributed ("The Catechism of the Catholic Church teaches…", "Lutheran confessions hold…"), with the source from the church page or the open question. Never present one church's teaching as the Christian answer.
- **Read next**: the one or two highest-scored adopted references for the topic.
- **Put it into practice**: practices from the "How to apply" section that support these rules.

Copy rule IDs, scores and links exactly from the files. Use the score to say how firmly a rule applies: 9–10 fundamental, 6–8 recommended, 1–5 situational. Never score or rank books of the Bible, passages or churches.

If you need a Bible reference that the files don't contain, create its link with `python3 <root>/scripts/bible_refs.py link "Book 1:2-3"` (where the script can run), and say that it doesn't come from the guidelines. Don't write Bible links by hand.

## 3. Open and uncovered questions

- **If the question is listed under "Open questions"**, or the churches differ on it, say so plainly, set out the main positions fairly with the listed sources, and don't pick a side. Suggest the person also asks their own church.
- **If no guideline covers it**, say so plainly. You may add general thoughts, but label them as your own and don't attach rule IDs to them. Suggest adding a guideline (maintainers can use the `add-guideline` skill in the guidelines repository).
- **If the question is personal or pastoral**, such as grief, guilt, doubt or a decision about one's own life, answer with care, and suggest talking with a pastor, priest or trusted member of their church. The guidelines don't replace them.
- **If the question needs another professional**, such as a lawyer or a doctor, say so: the guidelines aren't legal or medical advice.
- **If someone may be in danger**, including from abuse in a church, put their safety first: point them to emergency services or a relevant helpline before anything else.

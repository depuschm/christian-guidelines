---
name: bible-study
description: Lead a study of a Bible passage, for one person or a small group, from the Christian Guidelines' book pages - the passage in the context of its book, what it says, how the churches read it, the rules for Christian life it bears on, the questions the churches or scholars leave open, and questions for discussion and prayer. Works for every book of the Old and New Testaments and the deuterocanon, with every Bible reference linked to the World English Bible (WEBBE). Use when someone asks to study, prepare, lead or understand a passage or chapter in depth ("help me study Luke 15", "a Bible study on the Good Samaritan for my small group", "what does Romans 8 mean?"), or wants a study guide, sermon background or lectio divina on a passage.
argument-hint: "[passage, for example \"Luke 15:11-32\"]"
---

# Bible study

Prepare a study of the passage from the guidelines, not from memory. Everything you say about the book, its setting, its themes and how the churches read it must come from the book's page and the files it links to. You help the person read the passage for themselves: give them the text, the context and good questions, and don't preach a conclusion.

## Locate the guidelines

The guidelines root is `${CLAUDE_PLUGIN_ROOT}`. If that placeholder wasn't replaced with a path, the root is two directories above this `SKILL.md`. You need:

- `<root>/bible/README.md`: the canon, the recommended translations, and the table of books, which links each book's page
- `<root>/bible/<group>/<book>.md`: the book page: overview, outline, "Themes and teaching" (with rule IDs), "How the churches read it" and "Open questions"
- `<root>/RULES.md`: every rule with its ID, score and source
- `<root>/general/scripture.md`: how the churches read Scripture, including lectio divina

## 1. Pin down the passage

1. Work out the passage from the request (`$ARGUMENTS` if given). If the person names a story or a saying ("the prodigal son"), find its reference in the book page's outline or themes table; if it isn't there, ask.
2. Make its link with `python3 <root>/scripts/bible_refs.py link "Luke 15:11-32"`. If the script can't run, take the link from the book page, or write the reference without a link and say so. Never write a WEBBE link by hand.
3. If the passage is long (more than a chapter or two), suggest studying it in parts, and offer a plan with the `reading-plan` skill.

## 2. Read the book page

Find the book in the table of books in `bible/README.md` and read its page in full. From it, take:

- **Context**: what kind of book it is, its setting, author and date as the page states them (attributed, as the page attributes them), and where the passage falls in the outline. If the book is in the deuterocanon, say which churches read it, from the page's canon paragraph.
- **What the passage says**: the outline row and the themes rows that cover it, with their Bible links.
- **The rules it bears on**: the rule IDs in those themes rows. Look each one up in `RULES.md`.
- **How the churches read it**: every entry in "How the churches read it" that concerns the passage, attributed exactly as the page attributes it.
- **Open questions**: any that concern the passage, with their positions and sources.

If the passage quotes or is quoted by another book (for example, an Old Testament text quoted in the Gospels), read that book's page too, and use the cross-references the pages give.

## 3. Write the study

Use this structure, in this order. Keep it to what a person or group can use in an hour:

```markdown
## <Passage> (<link>)

**Context**: <two or three sentences: the book, its setting, and where the passage falls in it>

### Read the passage
<the WEBBE link, and a suggestion to read it aloud, slowly, twice. Quote key verses only, exactly as in the WEBBE.>

### What it says
<three to five short points, each with its verse links, from the outline and themes>

### How the churches read it
- <church or tradition>: <reading, attributed> ([source](…))
<Where the churches agree, say so. Where they differ, set out each reading; never present one as the Christian reading.>

### For Christian life
- `<ID>` (<score>) **<rule>**: <how the passage bears on it>

### Questions for discussion
1. <an observation question: what does the text say?>
2. <an interpretation question: what did it mean for its first readers?>
3. <an application question: what does it ask of us?>
<four to six questions in all, open rather than leading; one may draw on an open question, presenting its positions>

### Pray with it
<a short suggestion from general/scripture.md, such as reading it by lectio divina, or a prayer drawn from the passage's own words>

### Go further
<the book page's highest-scored tutorial or further reading, and the related book pages>
```

Copy rule IDs, scores, quotations and links exactly from the files. Use only sources the files cite.

## 4. Adapt it

- **For a group leader**, add a short note on timing and on handling disagreement: where the churches differ, let each person speak for their own church, and point to the open question.
- **For one person**, write the questions in the second person and leave room for their own notes.
- **If the person says which church they belong to**, read that church's page in `traditions/` and add how their church reads the passage, attributed, without dropping the others.
- **For sermon preparation**, add the passage's place in the lectionaries where the book page names it.

## 5. Limits

- If a question goes beyond the book page, say so, and answer only from other guideline files, or label your own thoughts as your own.
- If the study raises a personal or pastoral matter, such as grief, guilt or doubt, answer with care, and suggest talking with a pastor, priest or trusted member of their church.
- If someone may be in danger, put their safety first and point to emergency services or a helpline.

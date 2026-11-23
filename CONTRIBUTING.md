# Contributing

## 1. Reference first

Before writing anything, look for an existing source that covers the topic. Prefer sources in this order:

1. **Scripture**, linked to the World English Bible British Edition with Deuterocanon (WEBBE) as described in [Bible references](#bible-references) below
2. **Texts the churches share**: the creeds of the early church, the decisions of the ecumenical councils, texts of the World Council of Churches' Faith and Order Commission, and agreements between churches, such as the Joint Declaration on the Doctrine of Justification
3. **The churches' own teaching documents**: catechisms, confessions of faith, and statements adopted by a church's teaching office, synods or conferences, from their official websites
4. **Scholarly reference works**, such as the [St Andrews Encyclopaedia of Theology](https://www.saet.ac.uk/) and the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/), and introductions and commentaries by recognised scholars
5. **Well-maintained educational resources**, such as [BibleProject](https://bibleproject.com/)

If such a source exists, **add it under "Adopted references"** with one line saying what it covers and when to use it. Don't restate its content.

Write your own rule under "Key rules" only when:

- no single source covers the point, or several sources need to be combined, or
- the sources leave a practical choice open that readers need help with.

Even then, the rule must link to the sources that support it.

**Agreement, not sides.** A rule states what the churches broadly agree on ([ADR-0006](docs/decisions/0006-write-rules-only-where-the-churches-agree.md)). Every key rule cites:

- **Scripture**: at least one Bible passage that teaches it, and
- **the churches' agreement**: either an ecumenical text (a creed, a Faith and Order text or an agreement between churches), or the teaching documents of at least two church families, one of them Catholic or Orthodox and one Protestant.

If the churches disagree, for example on the baptism of infants, the ordination of women or divorce and remarriage, don't write a rule. Add an entry under "Open questions" that names the question, links a source that sets out the positions or a source for each church's position, and summarises them in a sentence or two without taking a side.

**General rule or area rule?** Check [RULES.md](RULES.md) before adding a rule. If a general rule already states the principle, an area rule should add only what the area adds (the practice, the guidance the churches give for that area, the specific situation) and name the general rule's ID, not restate it. When three or more area files need the same principle, add it to `general/` and keep the area rules to their specifics.

## 2. File formats

### General topics and areas of life

Every guideline file in `general/` and `specific/` uses these sections. Leave out any section that would be empty.

```markdown
<!-- rule-prefix: TOPIC -->
# Topic

One or two sentences on scope.

> Entries are sorted by score from 1 to 10 ([criteria](../RANKING.md)): … (added by rank.py fix)

## Adopted references

- `9` [Title](https://…): what it covers and when to use it.

## Key rules

### Subsection

- `8` `TOPIC-1` **Short imperative rule.** One or two sentences of explanation. ([Book 1:2–3](https://ebible.org/eng-webbe/…), [Catechism of the Catholic Church, 1234](https://…), [Westminster Larger Catechism, Q. 99](https://…))

## How to apply

- `7` [Practice or tool](https://…): what it is and how it helps. Supports `TOPIC-1`.

## Open questions

- `8` [Source that sets out the positions](https://…): the question, and each church's position in one or two neutral sentences.

## Tutorials and further reading

- `6` [Title](https://…): what you will learn.
```

Rules:

- **Every list item must contain a link.** A parent item whose sub-items each have a link is fine. Prose paragraphs give context only. Don't put rules in them.
- **Every reference entry and key rule starts with its score** in backticks. **Key rules also have an ID.** See [Scores, IDs and freshness](#4-scores-ids-and-freshness) below.
- **"How to apply"** lists practices, methods and tools that help people follow the rules: a way of praying, a rule of life, the works of mercy, a safeguarding policy template. Name the rule IDs each one supports.
- Link to the most specific page that supports the statement, not to a site's home page. For catechisms and confessions, name the paragraph, question or article in the link text, for example `[Catechism of the Catholic Church, 2055](…)` or `[Heidelberg Catechism, Q&A 4](…)`.
- Keep rules short. If a rule needs more than two sentences, the source probably deserves an "Adopted references" entry instead.
- Write rules as advice to the reader ("Forgive…", "Pray…", "Care for…"), in plain words. Explain theological terms the first time you use them.
- Don't paste large excerpts from sources. Summarise in your own words and link. Short quotations are fine when the exact wording matters, such as the words of the two great commandments.
- If you use an abbreviation that readers may not know, add it to [GLOSSARY.md](GLOSSARY.md). The website shows its meaning as a tooltip wherever it appears.
- This repository gives guidance drawn from Scripture and the churches' teaching. It doesn't replace a church, a pastor or a priest, and it isn't legal, medical or financial advice. When a rule touches the law, for example in safeguarding, say which law and where it applies, and recommend checking with the people responsible.

### Bible book pages

Pages in `bible/` describe one book of the Bible each ([ADR-0008](docs/decisions/0008-one-descriptive-page-per-bible-book.md)). They have no key rules and no rule prefix, and they never score the book or its passages. Copy [`bible/_template.md`](bible/_template.md) to the path that `python3 scripts/bible_refs.py books` lists for the book. It uses these sections:

- **Overview** (prose): the book's genre and subject, its setting, what the church has traditionally held and what scholars hold about its author and date, each attributed and sourced, and which churches include it.
- **Adopted references**: the book's text in the WEBBE, with a link to read it in the NRSVUE, and scholarly introductions.
- **Outline**: a table of the book's parts in order, each with its passage.
- **Themes and teaching**: a table with one row per theme, in the order the book develops it: what the book says, the related rule IDs in `general/` and `specific/`, and the passages.
- **How the churches read it**: reference entries on where the churches, or their interpreters, read the book differently, or where it has shaped their teaching and practice.
- **Open questions**: questions of authorship, date or meaning on which the churches or scholars disagree.
- **Tutorials and further reading.**

### Church pages

Pages in `traditions/` describe what a church or family of churches teaches and how it lives ([ADR-0007](docs/decisions/0007-describe-churches-on-their-own-terms.md)). They have no key rules and no rule prefix. Copy [`traditions/_template.md`](traditions/_template.md), which uses these sections:

- **Overview** (prose): which churches belong to the tradition, how it began, and what holds authority in it.
- **Adopted references**: its catechisms and confessions in their official text, the teaching documents of its governing bodies, and scholarly overviews.
- **Teaching**: a table with one row per teaching: the teaching, what the tradition holds, the related rule IDs, and the source. Order the rows as the tradition itself presents them, not by score.
- **Differences within the tradition**: where churches or movements within the tradition differ, each with a source.
- **Tutorials and further reading.**

### Writing about Scripture and the churches

Write about every church, and about Scripture, in the same neutral voice:

- **Attribute every teaching**: "The Catechism of the Catholic Church teaches…", "The Westminster Confession holds…", "The letter presents itself as…", "Most scholars date…". State as plain fact only what the text says ("Jesus tells the parable of the Good Samaritan") and what is undisputed. Never state a church's distinctive teaching as the Christian view, and never call it wrong.
- **Give both tradition and scholarship** where they differ, for example on who wrote a book and when, each with a source.
- **Use neutral names, or name each church's term.** Where churches use different words for the same thing, give them together the first time, for example "the Lord's Supper, also called the Eucharist or Holy Communion". Call the books the deuterocanon, and note that many Protestants call them the Apocrypha. Use the book names that `scripts/bible_refs.py books` lists.
- **Cite each church's own documents** for what it teaches, from its official website where possible, and scholarly reference works for how it is understood.
- **Respect sites' terms.** Don't script sites that forbid automated access; cite another reliable edition instead.
- **Prefer sources the churches or scholars recognise.** Don't cite devotional blogs, or polemical sites written to attack another church or another faith.
- **Show the churches' diversity.** Don't present one church's or one movement's view as the whole tradition's.
- **Map, don't merge.** In the "Related rules" column, link a teaching to the general rules it matches, but don't change a general rule to fit one church.

### Bible references

Every Bible reference is a link to the passage in the [World English Bible British Edition with Deuterocanon](https://ebible.org/eng-webbe/) (WEBBE), a public domain translation ([ADR-0009](docs/decisions/0009-quote-and-link-one-public-domain-translation.md)). The link text is the reference, and the link goes to the chapter and the first verse:

```markdown
[Matthew 22:34–40](https://ebible.org/eng-webbe/MAT22.htm#V34)
```

Don't write these links by hand. Create them with the script, which checks that the chapter and verses exist:

```bash
python3 scripts/bible_refs.py link "Matthew 22:34-40" "Jude 3" "Psalm 23"
```

- One passage per link. Use an en dash in ranges (`22:34–40`); the script converts hyphens.
- One-chapter books are cited by verse alone: "Jude 3", "Philemon 4–7".
- A whole chapter is "Psalm 23"; a whole book is its name alone, linked to the book's page.
- Quote the WEBBE, and only where the exact words matter. Otherwise summarise in your own words.
- The Greek forms of Esther and Daniel are cited as "Esther (Greek)" and "Daniel (Greek)", with the WEBBE's chapter and verse numbers.

## 3. Writing style

- British spelling in our own text (organisation, recognise, behaviour, neighbour). Keep titles of sources as they are written.
- Short sentences and common words. Readers include people who read English as a second language, and AI agents.
- Respectful, non-judgemental language about people, churches, other faiths and those with none.
- Dates as BC and AD.

## 4. Scores, IDs and freshness

**Scores.** Every source and every key rule has a score from 1 to 10. [RANKING.md](RANKING.md) defines the criteria and levels.

- **Sources**: the score lives in [sources.csv](sources.csv), one row per URL. A reference entry shows the score of its first link.
- **Bible passages** aren't in `sources.csv`. Each counts as a source with score 7, applied automatically.
- **Key rules**: the score is written at the start of the rule, for example `` `9` `LOVE-3` **Rule.** ``.

**Rule IDs.** Every key rule has a stable ID, made of the file's prefix and a number, such as `LOVE-3`. The prefix is declared on the file's first line as `<!-- rule-prefix: LOVE -->`.

- New rules get the next free number automatically. Don't pick numbers yourself.
- A rule keeps its ID when it's reworded, re-scored or re-sorted.
- When a rule is removed, its ID is retired in [rules.csv](rules.csv) and never reused. To move a rule to another file, remove it and add it as a new rule there.
- [RULES.md](RULES.md) lists every rule by ID. Every rule ID that a file names, for example in a "Related rules" column, must exist.

**Freshness.** Each source has a `verified` date in `sources.csv`, the last time someone confirmed the page still says what the guidelines cite it for.

- New links get today's date. You must have verified them (see [AGENTS.md](AGENTS.md)).
- Sources older than a year show up in the CI summary. Re-verify them with the `reverify-sources` project skill, or by hand: read the page, then update the date or fix the rule.

After adding or changing entries, run:

```bash
python3 scripts/rank.py fix
```

The command:

- adds new links to `sources.csv` with an empty score and removes unused ones,
- copies scores into the reference entries and gives new rules an ID,
- sorts every list by score,
- regenerates [SOURCES.md](SOURCES.md), [RULES.md](RULES.md), the checklists and the table of books in [bible/README.md](bible/README.md).

Fill in the empty scores, then run it again. Lists must be tight (no blank lines between items) to be sorted.

## 5. Adding an area of life, a church tradition or a Bible book page

**An area of life** (a role, a stage of life or a field of work):

1. Copy `specific/_template/` to `specific/<area>/` (lower-case, hyphenated).
2. Fill in `README.md`, and set a new, unique rule prefix in its first line. Split into more files only when the README gets long. Give each new file with key rules its own prefix, except when you split an existing README: then keep its prefix in every new file, so that the rule IDs don't change.
3. Add the area to [specific/README.md](specific/README.md) and the root [README.md](README.md).
4. Give it a sidebar icon for the website in `NAV_ICONS` in [scripts/build_site.py](scripts/build_site.py), from the Lucide set that Zensical bundles.

**A church tradition**:

1. Copy [`traditions/_template.md`](traditions/_template.md) to `traditions/<tradition>.md`.
2. Fill it in following [Church pages](#church-pages) above.
3. Add it to [traditions/README.md](traditions/README.md) and the root [README.md](README.md).

**A Bible book page**:

1. Find the book's path with `python3 scripts/bible_refs.py books`, and copy [`bible/_template.md`](bible/_template.md) there.
2. Fill it in following [Bible book pages](#bible-book-pages) above.
3. Run `python3 scripts/rank.py fix`, which links the page from the table of books in [bible/README.md](bible/README.md). The website lists it in the order of the canon.

## 6. Checks

Run these before opening a pull request:

```bash
python3 scripts/check_citations.py                     # every list item and table row has a link
python3 scripts/rank.py check                          # scores, IDs, sort order and the generated files
python3 scripts/bible_refs.py check                    # every Bible reference links to the right chapter and verse
python3 scripts/verify_sources.py                      # no broken or retired sources (needs network)
python3 scripts/verify_sources.py --stale              # sources not verified in the last year
lychee --config lychee.toml './**/*.md'                # links resolve (https://lychee.cli.rs/)
claude plugin validate .                               # plugin and marketplace manifests are valid
zizmor .                                               # workflow security audit (https://docs.zizmor.sh/)
```

To preview the website, install the generator once and build or serve it:

```bash
pip install -r requirements.txt
python3 scripts/build_site.py            # builds build/site/ in strict mode, like CI
python3 scripts/build_site.py --serve    # live preview at http://localhost:8000
```

The script stages the Markdown and generates the navigation from the indexes, so a new file, area or church page appears on the site once it's linked from its index, and a new Bible book page appears in the order of the canon. Links to files that aren't part of the site, such as CSV files and scripts, point to GitHub.

CI runs the same checks on every push and pull request, and weekly to catch link rot and retired pages. `verify_sources.py` catches pages that still answer HTTP 200 but redirect to a home, 404 or "deprecated" page, or that serve an empty page marked `noindex`, which a plain link checker misses.

### Sites that block automated link checks

Some sites return `403` to bots even when the page exists. They are listed in [`lychee.toml`](lychee.toml) under `exclude`. Check those links by hand, and only add a domain to the list after confirming in a browser that the page works.

### Pages that move or disappear

When a source breaks, first check whether the page, or its whole site, just moved: that's much more common than a page being retired. Look for a redirect or a move notice on the site, check whether other links to the same site broke too, and search for the page's title. If it moved, update the link and read the new page, because a redirect can lead to a less specific page. `verify_sources.py` lists permanent redirects (HTTP 301 and 308) as MOVED: the old link still works, so they don't fail CI, but they go stale.

Only if you find no new address: replace a page that was clearly retired with its successor or an equivalent current source. Otherwise don't remove it. If it may come back, keep it cited and park its exact URL in the "Temporarily unavailable" part of `exclude` in [`lychee.toml`](lychee.toml), with the date and the reason. Ask the repository owner before removing a source that has no replacement.

## 7. Licensing of contributions

By contributing, you agree that guideline content is licensed under [CC BY 4.0](LICENSE), and code and skills under [MIT](LICENSE-CODE), as described in the [README](README.md#license). Quotations from sources remain under their own licenses; Bible quotations come from the public domain WEBBE.

## 8. Changing the skills

Skills live in `skills/<name>/SKILL.md` ([Agent Skills format](https://agentskills.io/specification)). Keep the `name` field equal to the folder name. Keep `description` under 1024 characters and lead with what the skill does and when to use it. Skills must cite guideline files and their sources, must not invent rules, links or Bible references, and must not take sides on open questions. After changing a skill, run its evals (see [evals/README.md](evals/README.md)), and add a case when you add a skill.

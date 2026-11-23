---
name: add-guideline
description: Add or update a guideline, Bible book page or church page in this Christian Guidelines repository, the reference-first, ecumenical way. Finds and adopts existing creeds, church teaching documents, ecumenical agreements and reference works before writing new rules, keeps rules to what the churches broadly agree on, creates and checks Bible references, verifies every link, keeps the file format, updates the indexes, and runs the checks. Use when asked to add a topic, rule, source, open question, tutorial, area of life, Bible book page or church page (for example "add the page on Romans", "add guidelines for parents" or "add a rule about prayer").
argument-hint: "[topic, area, Bible book or church]"
---

# Add a guideline

Follow [CONTRIBUTING.md](../../../CONTRIBUTING.md). This skill turns it into steps.

## 1. Place it

- Christian life for everyone → a file in `general/`. Extend an existing file before creating a new one.
- A role, a stage of life or a field of work → `specific/<area>/`. For a new area, copy `specific/_template/README.md` to `specific/<area>/README.md`.
- A book of the Bible → the path `python3 scripts/bible_refs.py books` lists for it, from `bible/_template.md`.
- What a church tradition teaches → `traditions/<tradition>.md`, from `traditions/_template.md`.

## 2. Find existing guidance first

Search for authoritative sources, in this order: Scripture; texts the churches share (the creeds, the ecumenical councils, World Council of Churches Faith and Order texts, agreements between churches); the churches' own teaching documents (catechisms, confessions, statements of their teaching office, synods or conferences); scholarly reference works and introductions; then well-maintained educational resources.

- **If a source covers the topic well**, add it under **Adopted references** with a one-line description. Don't restate it.
- **Write a Key rule only if** no single source covers the point, several need combining, or the sources leave a practical choice open. Every rule cites at least one Bible passage and shows that the churches agree: an ecumenical text, or the teaching documents of at least two church families, one Catholic or Orthodox and one Protestant ([ADR-0006](../../../docs/decisions/0006-write-rules-only-where-the-churches-agree.md)).
- **If the churches disagree**, don't write a rule: add an **Open questions** entry with sources for the positions and a neutral summary.
- **Bible book and church pages have no key rules.** They describe, and link their teaching to rule IDs that exist in `RULES.md`.

## 3. Bible references

Create every Bible reference with the script, never by hand:

```bash
python3 scripts/bible_refs.py link "Romans 12:9-21" "Jude 3"
```

It prints Markdown links to the WEBBE with en dashes, and refuses chapters and verses that don't exist. Before citing a passage, read it (follow the link) and make sure it says what you attach to it. Quote the WEBBE only where the exact words matter.

## 4. Verify every other link

For each URL you add:

1. Fetch it and confirm it loads (HTTP 200 after redirects). Watch for soft 404s: the site redirects to its home page or to a "deprecated" or "no longer available" page, or it shows a "not found" page with status 200. Compare the final URL with the one you requested.
2. Confirm the page actually supports the statement you attach to it. Quote it to yourself before writing the rule. For catechisms and confessions, find the exact paragraph, question or article, and name it in the link text.
3. If the URL permanently redirects, use the final, canonical URL.
4. Link to the most specific page, not a site's home page.

Never add a URL from memory without fetching it.

## 5. Write it in the house format

```markdown
- `8` **Short imperative rule.** One sentence of explanation. ([Book 1:2](https://ebible.org/eng-webbe/…), [Church document, section](https://…), [Another church's document, section](https://…))
```

Every list item and table row in `general/`, `specific/`, `traditions/` and `bible/` needs at least one link. Keep rules to one or two sentences. On Bible book and church pages, attribute every teaching and every claim about authorship, date or meaning, and show where the churches or scholars differ ([ADR-0007](../../../docs/decisions/0007-describe-churches-on-their-own-terms.md), [ADR-0008](../../../docs/decisions/0008-one-descriptive-page-per-bible-book.md)).

## 6. Score it

Score every new source and rule from 1 to 10 using the criteria tables in [RANKING.md](../../../RANKING.md). Don't guess: name the criteria behind each score in your summary.

- **Rules**: write the score at the start of the rule, for example `` `8` **Rule.** ``. Don't write an ID: `fix` assigns the next free one for the file's prefix (`<!-- rule-prefix: … -->` on line 1).
- **Sources**: run `python3 scripts/rank.py fix`. It adds new links to `sources.csv` with an empty score and today's `verified` date. Fill in the `score` column (and tidy the `title` if the link text was generic), then run `fix` again. It copies the scores into the entries, sorts the lists and regenerates SOURCES.md, RULES.md, the checklists and the table of books in `bible/README.md`.
- **Bible passages** aren't scored by hand: they count as score 7 automatically.
- **Practices**: if a practice, template or tool helps people follow the rule, add it under "How to apply" with the rule IDs it supports.

## 7. Update the indexes (new files, areas or churches)

- `README.md`: the general, areas or church traditions table or list.
- `general/README.md`, `specific/README.md` or `traditions/README.md`.
- For a new area: an icon in `NAV_ICONS` in `scripts/build_site.py`.
- Bible book pages need no manual index update: `rank.py fix` links them from `bible/README.md`.
- New abbreviations: `GLOSSARY.md`.

## 8. Check

```bash
python3 scripts/check_citations.py
python3 scripts/rank.py check
python3 scripts/bible_refs.py check
lychee --config lychee.toml './**/*.md'   # if lychee is installed
```

Fix any failures. Then summarise what you added and list every new source URL.

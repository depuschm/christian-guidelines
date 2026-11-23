# Instructions for AI agents

This repository is a curated, source-linked collection of guidelines for Christian faith and life, written ecumenically: rules where the churches agree, a descriptive page for every book of the Bible, descriptions of what each church tradition teaches, and AI skills that apply them.

## Using the guidelines (in other projects and conversations)

- Guidelines live in `general/` (Christian life for everyone), `specific/<area>/` (roles, stages of life and fields of work), `bible/` (one page per book of the Bible) and `traditions/` (what each church tradition teaches).
- When you apply or cite a guideline, use the rule's ID (for example `LOVE-1`, listed in [RULES.md](RULES.md)) and include the rule's source links, including its Bible references.
- Every source and rule has a score from 1 to 10 ([RANKING.md](RANKING.md)), and lists are sorted by it. Read the highest-scored entries first. Use rule scores to weigh how firmly a rule applies: 9–10 fundamental, 6–8 recommended, 1–5 situational. Bible books, passages and churches are never scored.
- Don't invent rules, links or Bible references. If no guideline covers a question, say so.
- Don't take sides on questions the guidelines list under "Open questions", or between the churches. Present each position with its sources.
- Describe churches and their teaching in their own terms, attributed ("The Catechism of the Catholic Church teaches…", "Lutheran confessions hold…"), and never treat one church's teaching as the Christian view.
- This guidance doesn't replace a church, a pastor or a priest, and it isn't legal, medical or financial advice. Point people to their own church for personal and pastoral questions, and to emergency services or a helpline when someone may be in danger.
- Skills in `skills/` show the intended workflows.

## Editing this repository

Follow [CONTRIBUTING.md](CONTRIBUTING.md). The rules that matter most:

1. **Reference first.** If an authoritative source exists, such as a creed, a church's catechism or an ecumenical agreement, add it under "Adopted references" instead of rewriting it.
2. **Every list item and table row in `general/`, `specific/`, `traditions/` and `bible/` must contain a link** to a source that supports it. Prose paragraphs are for context only.
3. **Verify every link you add** by fetching it. Make sure it loads and actually supports the statement. Never add a URL from memory without checking it.
4. **Agreement, not sides.** Write rules only where the churches broadly agree: every key rule cites Scripture and either an ecumenical text or at least two church families, one Catholic or Orthodox and one Protestant. Contested questions go under "Open questions" ([ADR-0006](docs/decisions/0006-write-rules-only-where-the-churches-agree.md)).
5. **Bible references** link to the WEBBE. Create them with `python3 scripts/bible_refs.py link "John 3:16"`; never write them by hand ([ADR-0009](docs/decisions/0009-quote-and-link-one-public-domain-translation.md)).
6. **Score every new entry** following [RANKING.md](RANKING.md): sources in `sources.csv`, rules inline. Then run `python3 scripts/rank.py fix`, which assigns rule IDs. Never edit or reuse rule IDs by hand.
7. Run `python3 scripts/check_citations.py`, `python3 scripts/rank.py check` and `python3 scripts/bible_refs.py check` after editing guideline files.
8. When adding an area folder, update the indexes in `README.md` and `specific/README.md`. When adding a church page, update `traditions/README.md` and `README.md`. A new Bible book page is linked from `bible/README.md` by `rank.py fix`.

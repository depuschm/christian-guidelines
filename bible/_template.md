# <Book>

<!--
Copy this file to bible/<group>/<slug>.md, where <group> and <slug> are the ones `python3 scripts/bible_refs.py books`
lists for the book, and replace every placeholder. Book pages describe the book; they have no key rules and no rule
prefix, and they never score the book or its passages (ADR-0008). Their teaching links to rule IDs in general/ and
specific/ instead.

- Attribute what you report: "The letter presents itself as…", "Most scholars date…", "Catholic teaching reads this
  passage as…". Never state a disputed claim about authorship, date or meaning as plain fact. Where tradition and
  modern scholarship differ, give both, each with a source.
- Every Bible reference is a link to the WEBBE, made with `python3 scripts/bible_refs.py link "James 2:14–26"`.
  Quote the WEBBE, sparingly; summarise in your own words otherwise (ADR-0009).
- Every list item and table row must contain a link. Reference entries start with their score (from sources.csv,
  added by `python3 scripts/rank.py fix`). Outline and themes are tables, so they are never ranked.
- Order the outline and themes as the book itself runs, not by importance.
Delete this comment when done.
-->

<Two or three short paragraphs. What kind of book it is (a gospel, a letter, a collection of psalms, a history,
prophecy, wisdom) and what it is about. Its setting. Who it names as its author, what the church traditionally held
about its author and date, and what scholars hold today, each attributed and sourced. Where it stands in the canon:
which churches include it, and in which group.>

## Adopted references

- `7` [<Book>](https://example.com/text) in the World English Bible British Edition: the full text, which the references on this page link to. Read it also in the [NRSVUE](https://example.com/nrsvue) and other translations.
- `8` [Scholarly introduction to the book](https://example.com/intro): what it covers.

## Outline

The book's structure, in its own order.

| Passage | Contents |
| --- | --- |
| [<Book 1:1–18>](https://example.com/text#V1) | <What happens or what the passage says, in one sentence> |

## Themes and teaching

What the book teaches about God, faith and life, in the order the book develops it. *Related rules* are the rules in `general/` and `specific/` that the theme matches; leave the cell empty where none does yet.

| Theme | What the book says | Related rules | Passages |
| --- | --- | --- | --- |
| <Theme> | <One or two sentences, attributed to the book> | `LOVE-1` | [<Book 2:8>](https://example.com/text#V8) |

## How the churches read it

Where the churches, or their interpreters, read the book differently, or where it has played a part in their history. Each entry starts with its source's score.

- `7` [Source](https://example.com/reading): which church or interpreters, what they hold, and on which passage.

## Open questions

Questions on which the churches or scholars disagree, for example about the book's authorship or the meaning of a passage. These guidelines don't pick a side.

- `8` [Source that sets out the positions](https://example.com/debate): the question, and the main positions in one or two neutral sentences.

## Tutorials and further reading

- `6` [Overview video or introduction](https://example.com/overview): what you will learn.

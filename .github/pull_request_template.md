## What changes

<!-- One or two sentences. Name the rule IDs, Bible book pages or church pages you added or changed. -->

## Checklist

- [ ] Reference first: I adopted an existing text (a creed, a church's teaching document, an ecumenical agreement or a reference work) where one exists, rather than rewriting it.
- [ ] Every new list item and table row links to a source, and I opened each new link and confirmed it supports the statement.
- [ ] Every new rule cites Scripture and either an ecumenical text or at least two church families, one Catholic or Orthodox and one Protestant (docs/decisions/0006). Contested questions go under "Open questions".
- [ ] Teaching on Bible book and church pages is attributed, and no church's teaching is presented as the Christian view or judged.
- [ ] Bible references were created with `python3 scripts/bible_refs.py link`.
- [ ] New sources and rules are scored following RANKING.md, and I ran `python3 scripts/rank.py fix`.
- [ ] `python3 scripts/check_citations.py`, `python3 scripts/rank.py check` and `python3 scripts/bible_refs.py check` pass.
- [ ] For a new area or church page: the indexes are updated.

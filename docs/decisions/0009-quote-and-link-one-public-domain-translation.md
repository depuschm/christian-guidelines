---
status: accepted
date: 2026-11-23
decision-makers: depuschm
---

# Quote and link one public domain translation of the Bible

## Context and Problem Statement

The rules and the book pages cite Scripture constantly: across about 80 book pages and the topic files, the guidelines will link thousands of passages and quote some of them. Readers should be able to open each passage with one click. Modern translations are copyrighted, and their publishers allow quotation without permission only up to a limit: the NRSVUE needs written approval for more than 500 verses ([Bible Gateway, NRSVUE](https://www.biblegateway.com/versions/New-Revised-Standard-Version-Updated-Edition-NRSVUE-Bible/)), the NIV allows up to 500 verses that are less than a quarter of the work ([Bible Gateway, NIV](https://www.biblegateway.com/versions/New-International-Version-NIV-Bible/)), and the ESV's allowance excludes quotations "in a commentary or other biblical reference work" ([Crossway, Permissions](https://www.crossway.org/permissions/)), which is what the book pages are. Translations also differ in which books they include. Which translation should the guidelines quote and link to?

## Decision Drivers

* Freedom to quote: the guidelines are licensed CC BY 4.0 ([ADR-0005](0005-license-content-and-code-separately.md)), and their quotations shouldn't need permission or count against a limit.
* Completeness: the translation must include the deuterocanon ([ADR-0008](0008-one-descriptive-page-per-bible-book.md)).
* Stable links to a chapter and verse, which a script can check.
* Acceptability across the churches: readers of every church should find the text usable.

## Considered Options

* A scholarly committee translation, such as the New Revised Standard Version Updated Edition (NRSVUE), linked on Bible Gateway
* The King James Version, which is in the public domain outside the United Kingdom
* The World English Bible Classic edition, in the public domain, with the deuterocanon, which renders God's name in the Old Testament as "Yahweh"
* The World English Bible British Edition with Deuterocanon (WEBBE), in the public domain, with the deuterocanon, in British English, which renders God's name as "the LORD"

## Decision Outcome

Chosen option: "the WEBBE", on [ebible.org](https://ebible.org/eng-webbe/). It is in the public domain, it includes the deuterocanon and the further books of the Orthodox churches, its British spelling matches this repository's style, and it follows the common practice of rendering God's name as "the LORD". Every Bible reference is a link to the chapter in the WEBBE and the first verse of the passage, with the reference as the link text, for example `[Matthew 22:34–40](https://ebible.org/eng-webbe/MAT22.htm#V34)`.

The guidelines still recommend scholarly translations for reading and study, such as the NRSVUE and the translations the churches use, under "Adopted references" in [bible/README.md](../../bible/README.md). Pages summarise Scripture in their own words, and quote the WEBBE only where the exact words matter.

Bible passages are not entries in `sources.csv`. Each counts as a source with the same score, as a link to one section of a text, so no book or passage is ranked above another ([RANKING.md](../../RANKING.md)).

### Consequences

* Good, because quotations need no permission and carry no limit.
* Good, because every reference has the same form, so `scripts/bible_refs.py` checks offline that each one links to a chapter and verse that exist, and creates new links. If the site ever changes its addresses, the same script can rewrite every link from its reference.
* Bad, because the WEBBE is not a scholarly committee translation like the NRSVUE, and its wording differs from the translations many readers know. Readers who need precision are pointed to the scholarly translations, and quotations are kept short.
* Neutral, because the WEBBE prints the Greek forms of Esther and Daniel as whole books, so references to their additions use the WEBBE's chapter and verse numbers, which may differ from editions that print the additions separately.

### Confirmation

`scripts/bible_refs.py check` runs in CI and fails on any reference that doesn't link to the WEBBE, or that links to the wrong chapter or verse, or to one that doesn't exist.

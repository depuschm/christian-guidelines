---
status: accepted
date: 2026-11-23
decision-makers: depuschm
---

# Reference existing texts and teaching first, and back every written rule with a source

## Context and Problem Statement

We want one place for guidance on Christian faith and life: what the Bible says, book by book, what the churches teach, and how Christians can live it out in everyday life and in specific roles. Most of this already exists in Scripture, the creeds, the churches' catechisms and confessions, ecumenical agreements and scholarly reference works. How much should we write ourselves, and how do we keep what we write trustworthy?

This repository follows the approach of its sister projects, the [Architecture Guidelines](https://github.com/depuschm/architecture-guidelines) and the [Moral Guidelines](https://github.com/depuschm/moral-guidelines), which made the same decision for software architecture and for ethics.

## Decision Drivers

* Trust: readers and AI agents must be able to check every statement, which matters even more for claims about faith than for technical ones.
* Legitimacy: guidance that comes from Scripture and from the churches' own teaching carries weight that our own opinions don't.
* Maintenance: a small team can't keep a large self-written handbook current.
* Usefulness: readers need a curated path, not a pile of links.

## Considered Options

* Write our own complete handbook of Christian living
* Curate links only, like an awesome list
* Reference first: adopt existing texts and teaching, and write short rules only where needed, each with a source

## Decision Outcome

Chosen option: "Reference first", because it leaves the details to Scripture, the churches and scholarship while still giving readers our curated choices and short, actionable rules.

### Consequences

* Good, because every rule links to Scripture and to the churches' teaching, so statements can be checked.
* Good, because the churches maintain their own teaching documents; we only track whether our links still hold.
* Bad, because our content depends on external pages that move or change. Verified dates on every source, `scripts/verify_sources.py` and the `reverify-sources` skill address that.

### Confirmation

* `scripts/check_citations.py` fails CI if any list item or table row in `general/`, `specific/`, `traditions/` or `bible/` lacks a link.
* `scripts/bible_refs.py check` fails CI if a Bible reference doesn't link to the right chapter and verse.
* Link checks (lychee) and `scripts/verify_sources.py` catch broken and retired sources.

## More Information

The rules for contributors are in [CONTRIBUTING.md](../../CONTRIBUTING.md).

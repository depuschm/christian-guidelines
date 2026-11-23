---
status: accepted
date: 2026-11-23
decision-makers: depuschm
---

# Score every source and rule from 1 to 10, grouped into three named levels

## Context and Problem Statement

The collection will have hundreds of sources and rules. Readers need to know what to read first and which rules matter most, and reviews need a sense of severity. Rules differ greatly in weight: "love your neighbour as yourself" and "keep a regular time for prayer" are both good counsel, but not of the same importance. How should entries be ranked, without ranking Scripture or the churches?

## Decision Drivers

* Readers should see the most important entries first.
* Ranking should be consistent across contributors.
* Reviews need a severity signal.
* Scores must not rank books of the Bible, passages, churches or people.

## Considered Options

* No ranking, ordered by topic only
* Named levels only, such as "must", "should" and "may"
* Numeric scores from 1 to 10 only
* Scores from 1 to 10, grouped into named levels

## Decision Outcome

Chosen option: "Scores from 1 to 10, grouped into named levels": fundamental (9–10), recommended (6–8) and situational (1–5). Scores give a fine-grained sort order, and the levels tell readers how firmly to follow a rule. The criteria for rules are their weight in Scripture, the agreement of the churches, how central they are to the Christian life and how much harm neglecting them does, and their breadth. Agreement across every major church family counts most.

### Consequences

* Good, because every list puts the most important entries first, and [SOURCES.md](../../SOURCES.md) ranks all sources in one place.
* Good, because skills can use rule scores to say how firmly a rule applies.
* Bad, because scores are judgements and can drift between contributors. [RANKING.md](../../RANKING.md) defines the criteria, and blind second opinions calibrate them.
* Neutral, because Bible book pages and church pages have no scored rules ([ADR-0007](0007-describe-churches-on-their-own-terms.md), [ADR-0008](0008-one-descriptive-page-per-bible-book.md)), and every Bible passage counts as a source with the same score ([ADR-0009](0009-quote-and-link-one-public-domain-translation.md)). So no book, passage or church is ranked against another.

### Confirmation

`scripts/rank.py check` fails CI if any entry is unscored or any list is unsorted.

## More Information

The criteria and levels are in [RANKING.md](../../RANKING.md).

---
status: accepted
date: 2026-11-23
decision-makers: depuschm
---

# Describe the churches on their own terms, without ranking them

## Context and Problem Statement

The general rules state what the churches teach together ([ADR-0006](0006-write-rules-only-where-the-churches-agree.md)). But much of what matters to Christians is what their own church teaches and practises: how it reads Scripture, what it holds about the sacraments and ministry, and how it answers the questions on which the churches differ. Readers also want to understand churches other than their own. How should the guidelines cover the churches without judging between them?

## Decision Drivers

* Respect for every church, and for readers who belong to none.
* Accuracy: what a church teaches should be traceable to its own teaching documents and to scholarship.
* Usefulness: readers should see where the churches agree with each other and with the general rules, and where they differ.

## Considered Options

* Leave the churches out, and cover only what they share
* Merge the churches' distinctive teachings into the general rules
* Describe each church tradition on its own page, attributed and sourced, and map its teachings to the general rules without scoring them

## Decision Outcome

Chosen option: "Describe each church tradition on its own page". Each page in `traditions/` sets out what a church or family of churches (for example the Catholic Church, the Eastern Orthodox churches or the Lutheran churches) teaches and how it lives, attributed to that church and cited to its own teaching documents and to scholarly reference works. It shows the diversity within the tradition, and maps each teaching to the general rules it matches. Church pages have no key rules and no scores for teachings, so the repository never ranks one church's teaching above another's.

The folder keeps the name `traditions/`, as in the sister project [Moral Guidelines](https://github.com/depuschm/moral-guidelines), so that the tooling and skills work the same way in both. The text and the website call them church traditions.

### Consequences

* Good, because readers can see what each church teaches in its own words, and where the churches agree.
* Good, because the agreement between the churches is the evidence for the general rules.
* Bad, because a short page can't do justice to a church. Pages link to the church's own documents and to fuller scholarly treatments, and their "Differences within the tradition" sections make the simplification visible.
* Bad, because the first set of pages will leave many churches out. The index says so, and invites contributions.

### Confirmation

`scripts/check_citations.py` requires a source link in every list item and table row on church pages. `scripts/rank.py check` fails if a church page has key rules, or names a rule ID that doesn't exist.

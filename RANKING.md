# Ranking criteria

Every source and every key rule in this repository has a score from 1 to 10. Scores decide the order of each list (highest first). They group entries into three levels, and they give reviews a severity hint.

A score says how central a rule is to the Christian life, how firmly Scripture grounds it, and how broadly the churches agree on it. It isn't a verdict on people, and it never ranks Scripture or the churches:

- **Bible books and passages have no scores.** The [Bible book pages](bible/README.md) have no key rules, and every link to a passage counts the same as a source (see [Scoring sources](#scoring-sources)), whichever book it comes from ([ADR-0008](docs/decisions/0008-one-descriptive-page-per-bible-book.md)).
- **Churches have no scores.** The [church pages](traditions/README.md) have no key rules, and their sources are scored only on the source criteria below ([ADR-0007](docs/decisions/0007-describe-churches-on-their-own-terms.md)).

## Levels

| Score | Sources | Key rules |
| --- | --- | --- |
| 9–10 | **Start here**: read these first | **Fundamental**: at the heart of the Christian life; the churches teach them for every Christian, always |
| 6–8 | **Recommended**: read when working on the topic | **Recommended**: follow in most situations |
| 1–5 | **Further reading**: for depth or special cases | **Situational**: follow when the situation calls for it |

## Scoring sources

Judge each source on five criteria:

1. **Authority**: is it Scripture in a reliable edition, a creed or the decision of an ecumenical council, an official teaching document of a church (a catechism, a confession of faith, a statement adopted by a church's governing body), an ecumenical agreement that churches have adopted or that their joint commissions have published, the leading scholarly reference work, or the work of the person who defined the idea?
2. **Coverage**: does it cover the whole topic, or one detail of it?
3. **Currency**: is it in force, maintained and up to date? For Scripture, creeds and other ancient texts, currency means a reliable current edition or translation. For a church's teaching, it means the text the church holds today.
4. **Access**: is the full content freely available online?
5. **Actionability**: does it give concrete guidance that changes what people do, or does it survey a debate?

Then pick the score whose description fits best:

| Score | The source is… | Examples |
| --- | --- | --- |
| 10 | The definitive text for a whole area, shared across the churches, which this repository adopts as the baseline | a creed in a church's official text; an agreement such as the Joint Declaration on the Doctrine of Justification, for its topic |
| 9 | An essential primary source: the main catechism or confession of a church family, a foundational ecumenical text, or the Bible in a scholarly edition | the Catechism of the Catholic Church, the Westminster Confession of Faith, a scholarly translation's edition page |
| 8 | A highly authoritative source on an important sub-topic | a St Andrews Encyclopaedia of Theology entry, a church's official guidance on one area, a pope's encyclical or a synod's statement on one topic |
| 7 | Authoritative but narrower or less current | one section of a catechism or confession, one Bible passage, an official page on one topic, a respected book that isn't freely available |
| 6 | Good supporting material that overlaps with higher-ranked sources | a clear explanation, an introduction to a book of the Bible, a teaching video |
| 5 | Useful in specific contexts, or a secondary explanation of something covered better elsewhere | a toolkit's home page, a community guide |
| 4 | Narrow or limited in scope | |
| 3 | Dated or only partly relevant | a guide that predates the church's current teaching or current law |
| 1–2 | Kept for completeness only: archived, superseded or hard to access | |

A reference entry (in "Adopted references", "Open questions", "How the churches read it", "Tutorials and further reading" or the reading list) shows the score of its **first link**.

**Bible passages.** Every Bible reference links to the same public domain edition, the World English Bible British Edition with Deuterocanon ([ADR-0009](docs/decisions/0009-quote-and-link-one-public-domain-translation.md)). Passages aren't listed in [sources.csv](sources.csv): each counts as a source with score **7**, a link to one section of a text, whatever the book. `scripts/rank.py` applies that score, and `scripts/bible_refs.py check` checks that each reference links to the right chapter and verse.

Rules of thumb, adopted from the [architecture guidelines'](https://depuschm.github.io/architecture-guidelines/RANKING/) calibration rounds:

- A link to one section of a page usually scores at most 7, even when the page as a whole scores higher.
- An index or home page scores at most 9. A 10 is for a document that itself covers the whole topic.
- A St Andrews Encyclopaedia of Theology or Stanford Encyclopedia of Philosophy entry usually scores 8: authoritative and current, but an overview of a debate rather than guidance.

## Scoring key rules

Judge each rule on four criteria:

1. **Weight in Scripture**: did Jesus or the apostles command it, and is it taught across both Testaments, or does it rest on a few passages?
2. **Agreement across the churches**: do the creeds, the teaching documents of the Catholic, Orthodox and Protestant churches, and ecumenical agreements all teach it? Agreement across every major church family counts most ([ADR-0006](docs/decisions/0006-write-rules-only-where-the-churches-agree.md)).
3. **Centrality and harm**: is it at the heart of Christian faith and life, and does neglecting it do serious or lasting harm to people, to the church's witness or to a person's faith, or only miss a good?
4. **Breadth**: does it apply to every Christian in almost every situation, or only in some roles, such as parents or church leaders, or situations?

| Score | The rule… |
| --- | --- |
| 10 | Is at the centre of the Christian life, as Jesus named the two great commandments, or protects against grave, irreversible harm to people, and is taught throughout Scripture and by every church |
| 9 | Is a core duty for every Christian, commanded in Scripture and taught by all the major churches' catechisms and confessions |
| 8 | Is important in most situations: taught by the churches, and neglecting it does significant harm, or damage to trust, that is hard to repair |
| 7 | Is recommended in most situations, with a clear basis in Scripture and wide agreement among the churches, and a clear benefit at modest cost |
| 6 | Helps Christian life and practice, but neglecting it is easy to recover from |
| 5 | Is valuable in common but not universal situations, for example in one role, at a certain stage of life or in one kind of relationship |
| 3–4 | Applies only in specific circumstances |
| 1–2 | Is niche |

Within a topic subsection, rules are sorted by score. Rules with the same score keep their written order.

Rules exist only where the churches broadly agree ([ADR-0006](docs/decisions/0006-write-rules-only-where-the-churches-agree.md)). Questions on which the churches disagree, such as the baptism of infants or the ordination of women, aren't scored as rules. They are listed under "Open questions", with sources that set out each church's position.

## How scores are used

- **Ordering**: every list of ranked entries is sorted by score, highest first.
- **Overview**: [SOURCES.md](SOURCES.md) lists every source in one place, grouped by level.
- **Answers and reviews**: the [`ask-guidelines`](skills/ask-guidelines/SKILL.md) skill uses rule scores to say how firmly a rule applies. Future review skills use them as a severity hint: neglecting a 9–10 rule is usually *High*, 6–8 *Medium* and 1–5 *Low*, adjusted for the actual harm.

## Calibration

Scores are judgements, so they are checked with blind second opinions: someone scores a sample of rules and sources against this file without seeing the existing scores, and any band where the two disagree systematically is re-checked. The results of each round will be recorded here. No round has been run yet.

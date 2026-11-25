# Christian Guidelines

Christian faith and life, written ecumenically: source-linked guidelines where the churches agree, a guide to every book of the Bible, what each church tradition teaches, and AI skills that apply them.

**Read it as a website:** [depuschm.github.io/christian-guidelines](https://depuschm.github.io/christian-guidelines/), with search, dark mode and a link to every rule.

The repo is **reference-first**, like its sister projects, the [Architecture Guidelines](https://github.com/depuschm/architecture-guidelines) and the [Moral Guidelines](https://github.com/depuschm/moral-guidelines). Where a good source already exists (Scripture, the creeds, a church's catechism or confession, an agreement between churches, or a scholarly reference work), we link to it and adopt it. We only write our own short rules where nothing suitable exists, and every rule we write links to its sources.

The guidelines are **ecumenical**: they are written for Christians of every church, and for anyone who wants to understand Christianity. Rules state **what the churches broadly agree on**, and every rule cites Scripture and the teaching of more than one church family. Where the churches disagree, for example on the baptism of infants or the ordination of women, the guidelines don't take a side: they list the question under "Open questions", with each church's position and its sources ([ADR-0006](docs/decisions/0006-write-rules-only-where-the-churches-agree.md)). The [church pages](traditions/README.md) describe what each church teaches in its own terms.

**Every book of the Bible** gets a page: the 39 books of the Old Testament, the 27 of the New Testament, and the deuterocanon, the further books that the Catholic and Orthodox churches read in their Old Testament. Each page describes the book, its structure and themes, and how the churches read it, and links its teaching to the rules ([ADR-0008](docs/decisions/0008-one-descriptive-page-per-bible-book.md)). Every Bible reference links to the passage in the public domain [World English Bible British Edition](https://ebible.org/eng-webbe/) ([ADR-0009](docs/decisions/0009-quote-and-link-one-public-domain-translation.md)).

Every source and every rule has a **score from 1 to 10**, and lists are sorted by it, so the most important entries come first. Books of the Bible, passages and churches are never scored.

| Score | Sources | Rules |
| --- | --- | --- |
| 9–10 | Start here | Fundamental |
| 6–8 | Recommended | Recommended |
| 1–5 | Further reading | Situational |

[RANKING.md](RANKING.md) explains the criteria, and [SOURCES.md](SOURCES.md) lists every source in one place, ranked, with the date each was last verified.

Every rule also has a **stable ID**, such as `LOVE-1`, so studies, reviews and discussions can cite it. [RULES.md](RULES.md) lists all rules by ID. On the website, `https://depuschm.github.io/christian-guidelines/RULES/#LOVE-1` is a permanent link to a rule. Where a practice helps people follow a rule, the guideline file names it under **How to apply**.

These guidelines draw on Scripture and the churches' teaching. They don't replace a church, a pastor or a priest, and they aren't legal, medical or financial advice.

## Structure

```
general/            Christian life for everyone: the creeds, love, Scripture, prayer, worship, forgiveness, family, justice, …
bible/              One page per book of the Bible: Old Testament, deuterocanon, New Testament
bible/_template.md  Starting point for a book page
specific/<area>     One folder per role, stage of life or field of work (planned)
specific/_template  Starting point for a new area folder
traditions/         What each church tradition teaches, in its own terms
skills/             AI skills (Agent Skills format) that apply these guidelines
checklists/         One checklist per area, for reflection, studies and reviews (generated)
docs/decisions/     Decision records for this repository
RANKING.md          How sources and rules are scored from 1 to 10
SOURCES.md          Every linked source, ranked (generated from sources.csv)
RULES.md            Every rule by ID (generated)
GLOSSARY.md         Abbreviations and their meanings
sources.csv         Score and last-verified date of every source
rules.csv           Registry of rule IDs, including retired ones (never reused)
.claude-plugin/     Makes this repo installable as a Claude Code plugin and marketplace
scripts/            Repository checks (citations, scores, IDs, Bible references, source freshness) and tooling
zensical.toml       Website configuration, built by scripts/build_site.py
```

## General guidelines

| Topic | What it covers |
| --- | --- |
| [What the churches confess together](general/beliefs.md) | The faith of the Nicene and Apostles' Creeds, article by article, and where the churches differ |
| [Love of God and neighbour](general/love.md) | The two great commandments, the Golden Rule, who my neighbour is, love of enemies, love in deeds |
| [Reading Scripture](general/scripture.md) | Reading the Bible regularly, in context and as a whole, with others and in prayer, and doing what it says |
| [Prayer](general/prayer.md) | Praying every day, the Lord's Prayer, praying for others, thanksgiving, lament, praying together and humbly |
| [Worship and the sacraments](general/worship.md) | The Lord's Day, baptism, the Lord's Supper and preparing for it, a day of rest, worship with your whole life |
| [Repentance and forgiveness](general/repentance.md) | Repenting and confessing sin, forgiving others, reconciliation, no revenge, helping those who fall |
| [Growing as a disciple](general/discipleship.md) | Following Jesus, the fruit of the Spirit, spiritual disciplines, using your gifts, mentors, perseverance |
| [Belonging to a church](general/church.md) | The local church, unity, serving and giving, leaders and accountability, disagreements, safeguarding |
| [Honest and kind speech](general/speech.md) | Truthfulness, no gossip or slander, words that build up, the tongue and anger, keeping your word, confidences |
| [Marriage, family and singleness](general/family.md) | Parents, faithfulness, children, self-giving love, singleness, no abuse at home |
| [Money, possessions and generosity](general/money.md) | Honesty, generosity, greed, contentment, debts, stewardship |
| [Work and rest](general/work.md) | Working well, fair wages, dignity of work, rest for workers, vocation |
| [Justice and the poor](general/justice.md) | The poor and the stranger, equal dignity, honest justice, migrants, just structures, prisoners |
| [Care for creation](general/creation.md) | Caring for the earth, simple living, pollution, animals, praise, future generations |
| [Suffering, death and hope](general/suffering.md) | Trust in suffering, comfort, care for the sick and dying, hope in the resurrection, suicide |
| [Sharing the faith](general/mission.md) | Witness in word and deed, no coercion, integrity, respect for other faiths, service, mission |
| [Public life and citizenship](general/public-life.md) | Authorities, laws and taxes, obeying God first, peace, religious freedom, the common good |
| [Discernment and decisions](general/discernment.md) | Prayer, Scripture and church teaching, conscience, wise advice, fruit, care for others |
| [Reading list](general/reading-list.md) | Complete guides, Bible introductions, courses, classics and church history |


## The Bible

The [Bible section](bible/README.md) explains which books each church reads, recommends translations for reading and study, and lists every book with its page:

[Old Testament](bible/README.md#old-testament) · [Deuterocanon](bible/README.md#deuterocanon) · [New Testament](bible/README.md#new-testament)

The Old Testament and the New Testament are complete: all 66 books have a page, listed in the [table of books](bible/README.md#books). The 15 books and additions of the deuterocanon come next.

## Areas of life

Planned, with their own guidance and rules: church leadership and safeguarding, marriage, parents and children, work and business, online life and technology, healthcare and the end of life, politics and public life. See [specific/README.md](specific/README.md).

## Church traditions

Each church tradition is described in its own terms, from its own teaching documents ([ADR-0007](docs/decisions/0007-describe-churches-on-their-own-terms.md)):

[The Catholic Church](traditions/catholic.md) · [The Eastern Orthodox churches](traditions/eastern-orthodox.md) · [The Oriental Orthodox churches](traditions/oriental-orthodox.md) · [The Lutheran churches](traditions/lutheran.md) · [The Reformed and Presbyterian churches](traditions/reformed.md) · [The Anglican churches](traditions/anglican.md) · [The Methodist churches](traditions/methodist.md) · [The Baptist churches](traditions/baptist.md) · [The Pentecostal and charismatic churches](traditions/pentecostal.md) · [The Anabaptist churches](traditions/anabaptist.md)

Many other churches still need pages. See [traditions/README.md](traditions/README.md).

## Checklists

Every rule of an area in one list, grouped by level and sorted by score, with the practices that support each rule. Use one for personal reflection, in a small group, or to review a church's life and practice:

[General](checklists/general.md)

## AI skills

The [`skills/`](skills) folder uses the [Agent Skills](https://agentskills.io/specification) format (a folder with a `SKILL.md`), which Claude Code and other agent tools can load.

| Skill | Use it to |
| --- | --- |
| [`ask-guidelines`](skills/ask-guidelines/SKILL.md) | Answer "what does the Bible say about X?", "what is this book about?" or "what do the churches teach?" with rule IDs, Bible references and sources, and each church's position where they differ |

Planned: `bible-study` (study a passage in its context, with how the churches read it), `reading-plan` (plans for reading the whole Bible or part of it), `discernment-record` (work through a decision with Scripture, tradition, reason and experience), `rule-of-life` (build a personal or small-group rule of life, labelled with rule IDs) and `church-review` (review a church's safeguarding, finance and governance against the guidelines).

The skills come with [evals](evals/README.md) that compare runs with and without the plugin. They haven't been run against real models yet: start the **Skill evals** workflow once the repository has an `ANTHROPIC_API_KEY` secret.

Maintainers also get two project skills: [`add-guideline`](.claude/skills/add-guideline/SKILL.md) adds guidelines, Bible book pages and church pages the reference-first way, and [`reverify-sources`](.claude/skills/reverify-sources/SKILL.md) re-checks stale or retired sources.

### Install in Claude Code

The repo is a [Claude Code plugin](https://code.claude.com/docs/en/plugins) and its own marketplace:

```bash
claude plugin marketplace add depuschm/christian-guidelines
claude plugin install christian-guidelines@christian-guidelines
```

The skills then run as `/christian-guidelines:ask-guidelines` and so on. Claude also loads them on its own when a request matches.

The plugin has no fixed version, so every commit to `main` is a new release. To receive updates automatically, open `/plugin`, go to **Marketplaces**, select `christian-guidelines` and choose **Enable auto-update**. Otherwise, update by hand with `claude plugin update christian-guidelines@christian-guidelines`. To try the plugin from a local clone without installing it, run `claude --plugin-dir ./christian-guidelines`.

### Use with other agents

Tools that read [`AGENTS.md`](AGENTS.md) or support Agent Skills can use the `skills/` folders directly. The skills find the guideline files relative to their own location (`../../general`, `../../bible`, `../../traditions`), so keep the repo layout intact.

## Roadmap

1. **Foundations** (done): the repository's decisions, scoring criteria, templates, checks and website, the Bible reference tooling, and one page of each kind to prove the format: [Love of God and neighbour](general/love.md) and [James](bible/new-testament/james.md).
2. **General topics and church pages** (done): eighteen topics, from the creeds to discernment, with 106 rules, a reading list, and ten church pages (Catholic, Eastern Orthodox, Oriental Orthodox, Lutheran, Reformed, Anglican, Methodist, Baptist, Pentecostal, Anabaptist).
3. **Bible book pages** (in progress): the Old Testament and the New Testament are done, all 66 books. Next: the deuterocanon.
4. **Areas of life, more skills and evals.**

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). The short version:

1. **Reference first.** Link to Scripture, a creed, a church's teaching document or an ecumenical agreement before writing a new rule.
2. **Agreement, not sides.** Every rule cites Scripture and either an ecumenical text or at least two church families. Contested questions go under "Open questions", with each church's position.
3. **Every statement has a source.** Each list item and table row in `general/`, `specific/`, `traditions/` and `bible/` must contain a link. CI enforces this with [`scripts/check_citations.py`](scripts/check_citations.py).
4. **Bible references are created, not typed.** `python3 scripts/bible_refs.py link "John 3:16"` creates a link to the WEBBE, and [`scripts/bible_refs.py`](scripts/bible_refs.py) checks every reference in CI.
5. **Every entry has a score.** Score sources in `sources.csv` and rules inline, following [RANKING.md](RANKING.md). Then run `python3 scripts/rank.py fix`, which also gives new rules their ID, sorts the lists and updates SOURCES.md, RULES.md, the checklists and the table of books.
6. **Links must work and stay current.** CI runs [lychee](https://lychee.cli.rs/) and [`scripts/verify_sources.py`](scripts/verify_sources.py) on every push and once a week. The script also catches retired pages, and the job summary lists sources not verified in the last year.

### Automation

| What runs | When | Where |
| --- | --- | --- |
| Citation, score, rule ID and Bible reference checks | Every push and pull request | [`checks.yml`](.github/workflows/checks.yml) |
| Workflow security audit with [zizmor](https://docs.zizmor.sh/) | Every push and pull request | [`checks.yml`](.github/workflows/checks.yml) |
| Plugin and marketplace manifest validation | Every push and pull request | [`checks.yml`](.github/workflows/checks.yml) |
| Link check and retired-page detection | Every push and pull request, and weekly | [`checks.yml`](.github/workflows/checks.yml) |
| Sources not verified for a year fail the weekly run, and a failed weekly run opens (or updates) an issue | Weekly | [`checks.yml`](.github/workflows/checks.yml) |
| Website build in strict mode (broken links fail it), deployed to GitHub Pages | Pull requests build it, pushes to `main` deploy it | [`site.yml`](.github/workflows/site.yml) |
| Update pull requests for GitHub Actions and the site generator | Weekly | [`dependabot.yml`](.github/dependabot.yml) |
| Skill evals against real models | When started by hand (needs an `ANTHROPIC_API_KEY` secret) | [`evals.yml`](.github/workflows/evals.yml) |

Issue templates cover suggesting a source, disputing a score, reporting an outdated source and requesting a new area, church or Bible book page. The decisions behind how this repository works are recorded in [docs/decisions](docs/decisions/README.md).

## License

- **Guideline content and documentation** (`general/`, `specific/`, `traditions/`, `bible/` and the Markdown files at the root) is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). Bible quotations come from the World English Bible British Edition, which is in the public domain. Other short quotations from sources remain under their own terms.
- **Code and AI skills** (`scripts/`, `skills/`, `.claude/`, `.claude-plugin/`, `.github/` and config files) are licensed under the [MIT License](LICENSE-CODE).
- Linked third-party sources keep their own licenses. This repository links to them and summarises them. It doesn't copy them.

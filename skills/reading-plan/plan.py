#!/usr/bin/env python3
"""Make a Bible reading plan with links to the WEBBE, as a Markdown table.

The plan splits the chosen books into days of about the same length, counted in verses (or in
chapters), and never splits a chapter. Every reading links to the World English Bible British
Edition with Deuterocanon (WEBBE) on ebible.org, made with scripts/bible_refs.py (ADR-0009).

Which books a church reads differs (see bible/README.md, "Which books each church reads"), so the
plan asks for a canon:

  protestant  the 39 books of the Old Testament and the 27 of the New Testament
  catholic    the same, with Tobit, Judith, 1 and 2 Maccabees, Wisdom, Sirach and Baruch, and Esther
              and Daniel in their Greek form, in the order of the New American Bible
  orthodox    the Catholic list, with 1 Esdras, the Prayer of Manasseh, Psalm 151 and 3 Maccabees.
              The plan keeps the order of English Bibles and puts these books next to the books they
              belong with; Orthodox Bibles that follow the Septuagint order the books differently.

Usage:
  python3 plan.py --days 365
  python3 plan.py --canon catholic --days 365 --start 2027-01-01
  python3 plan.py --books "Matthew-John" --days 30
  python3 plan.py --books "new-testament, Psalms" --per-day 3
  python3 plan.py --books "Genesis, Exodus" --days 40 --balance chapters

  --books    comma-separated: book names or codes (for example "Psalms", "1 Samuel", "SIR"), ranges
             ("Genesis-Deuteronomy", in the order of the chosen canon), or the groups "bible" (the
             whole canon, the default), "old-testament" and "new-testament" (the canon's part of
             the Bible), and "deuterocanon" (the canon's books beyond the 39 and 27).
  --days N / --per-day K   split into N days, or into days of K chapters
  --start DATE             add a date column, starting on DATE (YYYY-MM-DD)
  --balance verses|chapters   split by verse count (default) or by chapter count
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
import bible_refs  # noqa: E402

OT = [code for code, *_rest in bible_refs.BOOKS if bible_refs.BY_CODE[code][2] == "old-testament"]
NT = [code for code, *_rest in bible_refs.BOOKS if bible_refs.BY_CODE[code][2] == "new-testament"]
CATHOLIC_OT = (
    "GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH EZR NEH TOB JDT ESG 1MA 2MA "
    "JOB PSA PRO ECC SNG WIS SIR ISA JER LAM BAR EZK DAG HOS JOL AMO OBA JON MIC NAM HAB ZEP HAG ZEC MAL"
).split()


# The Catholic list, with the Prayer of Manasseh after 2 Chronicles, 1 Esdras before Ezra, Psalm 151
# after the Psalms and 3 Maccabees after 2 Maccabees.
ORTHODOX_OT = (
    "GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH MAN 1ES EZR NEH TOB JDT ESG 1MA 2MA 3MA "
    "JOB PSA PS2 PRO ECC SNG WIS SIR ISA JER LAM BAR EZK DAG HOS JOL AMO OBA JON MIC NAM HAB ZEP HAG ZEC MAL"
).split()

CANONS = {
    "protestant": (OT, NT),
    "catholic": (CATHOLIC_OT, NT),
    "orthodox": (ORTHODOX_OT, NT),
}


def book_code(label):
    label = label.strip()
    if label.upper() in bible_refs.BY_CODE:
        return label.upper()
    code = bible_refs.NAMES.get(label.lower())
    if code is None:
        raise SystemExit(f"Unknown book: {label!r}. Run `python3 scripts/bible_refs.py books` for the names.")
    return code


def select(spec, canon):
    old, new = CANONS[canon]
    order = old + new
    extra = [code for code in old if bible_refs.BY_CODE[code][2] == "deuterocanon"]
    chosen = []
    for item in [part.strip() for part in spec.split(",") if part.strip()]:
        key = item.lower()
        if key in ("bible", "all"):
            chosen += order
        elif key in ("old-testament", "ot"):
            chosen += old
        elif key in ("new-testament", "nt"):
            chosen += new
        elif key == "deuterocanon":
            if not extra:
                raise SystemExit("The protestant canon has no deuterocanon: choose --canon catholic or orthodox.")
            chosen += extra
        elif re.search(r"\s*(?:[–-]| to )\s*", item) and not bible_refs.NAMES.get(key):
            first, last = re.split(r"\s*(?:[–-]| to )\s*", item, maxsplit=1)
            a, b = book_code(first), book_code(last)
            if a not in order or b not in order:
                raise SystemExit(f"{item!r}: both books must be in the {canon} canon to make a range.")
            i, j = order.index(a), order.index(b)
            if i > j:
                raise SystemExit(f"{item!r}: {first} comes after {last} in the {canon} canon.")
            chosen += order[i:j + 1]
        else:
            chosen.append(book_code(item))
    seen = set()
    return [code for code in chosen if not (code in seen or seen.add(code))]


def chapters(codes, data):
    result = []
    for code in codes:
        for number, verses in sorted(data[code]["chapters"].items(), key=lambda item: int(item[0])):
            if int(number) > 0:
                result.append((code, int(number), verses))
    return result


def split(items, days, balance):
    weights = [verses if balance == "verses" else 1 for _, _, verses in items]
    total = sum(weights)
    days = min(days, len(items))
    plan, current, done = [], [], 0
    for index, (item, weight) in enumerate(zip(items, weights)):
        current.append(item)
        done += weight
        left_items = len(items) - index - 1
        left_days = days - len(plan) - 1
        target = total * (len(plan) + 1) / days
        if left_days > 0 and (done >= target or left_items == left_days):
            plan.append(current)
            current = []
    if current:
        plan.append(current)
    return plan


def reading(day, data):
    """The day's chapters as Markdown links, one per run of chapters in the same book."""
    parts = []
    run = [day[0]]
    for item in day[1:] + [None]:
        if item is not None and item[0] == run[-1][0] and item[1] == run[-1][1] + 1:
            run.append(item)
            continue
        code = run[0][0]
        name = bible_refs.BY_CODE[code][0]
        if len(data[code]["chapters"]) == 1:
            text = name
        elif len(run) == 1:
            text = f"{name} {run[0][1]}"
        else:
            text = f"{name} {run[0][1]}–{run[-1][1]}"
        ref = bible_refs.parse(text, data)
        parts.append(f"[{text}]({bible_refs.url_for(ref, data)})")
        if item is not None:
            run = [item]
    return " · ".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--canon", choices=sorted(CANONS), default="protestant")
    parser.add_argument("--books", default="bible")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--days", type=int)
    group.add_argument("--per-day", type=int)
    parser.add_argument("--start", type=datetime.date.fromisoformat)
    parser.add_argument("--balance", choices=["verses", "chapters"], default="verses")
    args = parser.parse_args()

    data = bible_refs.load()
    codes = select(args.books, args.canon)
    items = chapters(codes, data)
    if args.per_day:
        if args.per_day < 1:
            raise SystemExit("--per-day must be at least 1.")
        plan = [items[i:i + args.per_day] for i in range(0, len(items), args.per_day)]
    else:
        if args.days < 1:
            raise SystemExit("--days must be at least 1.")
        plan = split(items, args.days, args.balance)

    names = [bible_refs.BY_CODE[code][0] for code in codes]
    if len(names) <= 6:
        scope = ", ".join(names)
    else:
        scope = f"{names[0]} to {names[-1]}, {len(names)} books"
    print(f"Reading plan: {scope} ({args.canon} canon), {len(items)} chapters in {len(plan)} days. "
          "Links go to the World English Bible British Edition with Deuterocanon (WEBBE).\n")
    if args.start:
        print("| Day | Date | Reading | Done |\n| --- | --- | --- | --- |")
    else:
        print("| Day | Reading | Done |\n| --- | --- | --- |")
    for number, day in enumerate(plan, 1):
        if args.start:
            date = args.start + datetime.timedelta(days=number - 1)
            print(f"| {number} | {date.isoformat()} | {reading(day, data)} | ☐ |")
        else:
            print(f"| {number} | {reading(day, data)} | ☐ |")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        sys.exit(0)

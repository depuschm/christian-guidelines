#!/usr/bin/env python3
"""Check and create links to Bible passages.

Every Bible reference in this repository links to the same passage in the World English Bible British
Edition with Deuterocanon (WEBBE) on ebible.org, a public domain translation (ADR-0009). The link text is
the reference, and the link goes to the chapter page and the first verse:

    [Matthew 22:34–40](https://ebible.org/eng-webbe/MAT22.htm#V34)

The script knows every book, chapter and verse of the WEBBE from scripts/bible_books.json, which
`build-data` generates from the edition's own HTML files, so it can check references offline.

Usage:
  python3 scripts/bible_refs.py check [FILE ...]   Check every link to ebible.org in the Markdown files: the
                                                  link text must be a valid reference (book, chapter, verses,
                                                  with an en dash in ranges), and the URL must go to that
                                                  chapter and verse of the WEBBE. Exit code 1 on problems.
  python3 scripts/bible_refs.py link REF [REF ...] Print Markdown links, for example:
                                                  python3 scripts/bible_refs.py link "Romans 13:8-10" "Jude 3"
  python3 scripts/bible_refs.py books             List the books with their names, codes, groups and chapters.
  python3 scripts/bible_refs.py build-data [ZIP]  Regenerate scripts/bible_books.json from eng-webbe_html.zip
                                                  (downloaded from ebible.org when no file is given).

Reference forms: "John 3:16", "Matthew 22:34–40", "Matthew 5:1–7:29", "Psalm 23", "Isaiah 52–53",
"Jude 3" and "Philemon 4–7" (one-chapter books may leave out the chapter), "Psalm 151:4", and a whole
book by its name alone, linked to the book's page (https://ebible.org/eng-webbe/JAS.htm).
"""

import io
import json
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(__file__).resolve().parent / "bible_books.json"
EDITION = "eng-webbe"
BASE = f"https://ebible.org/{EDITION}/"
ZIP_URL = f"https://ebible.org/Scriptures/{EDITION}_html.zip"
SKIP_DIRS = {".git", "build", "node_modules"}

# (code, name used in references and page titles, other names accepted in references, group, page slug, section)
# Groups and order follow bible/README.md. Names follow the NRSVUE where it differs from the WEBBE,
# except for the Greek forms of Esther and Daniel, which the WEBBE prints as whole books.
BOOKS = [
    ("GEN", "Genesis", [], "old-testament", "genesis", "Law (Pentateuch)"),
    ("EXO", "Exodus", [], "old-testament", "exodus", "Law (Pentateuch)"),
    ("LEV", "Leviticus", [], "old-testament", "leviticus", "Law (Pentateuch)"),
    ("NUM", "Numbers", [], "old-testament", "numbers", "Law (Pentateuch)"),
    ("DEU", "Deuteronomy", [], "old-testament", "deuteronomy", "Law (Pentateuch)"),
    ("JOS", "Joshua", [], "old-testament", "joshua", "History"),
    ("JDG", "Judges", [], "old-testament", "judges", "History"),
    ("RUT", "Ruth", [], "old-testament", "ruth", "History"),
    ("1SA", "1 Samuel", [], "old-testament", "1-samuel", "History"),
    ("2SA", "2 Samuel", [], "old-testament", "2-samuel", "History"),
    ("1KI", "1 Kings", [], "old-testament", "1-kings", "History"),
    ("2KI", "2 Kings", [], "old-testament", "2-kings", "History"),
    ("1CH", "1 Chronicles", [], "old-testament", "1-chronicles", "History"),
    ("2CH", "2 Chronicles", [], "old-testament", "2-chronicles", "History"),
    ("EZR", "Ezra", [], "old-testament", "ezra", "History"),
    ("NEH", "Nehemiah", [], "old-testament", "nehemiah", "History"),
    ("EST", "Esther", [], "old-testament", "esther", "History"),
    ("JOB", "Job", [], "old-testament", "job", "Wisdom and poetry"),
    ("PSA", "Psalms", ["Psalm"], "old-testament", "psalms", "Wisdom and poetry"),
    ("PRO", "Proverbs", [], "old-testament", "proverbs", "Wisdom and poetry"),
    ("ECC", "Ecclesiastes", [], "old-testament", "ecclesiastes", "Wisdom and poetry"),
    ("SNG", "Song of Songs", ["Song of Solomon"], "old-testament", "song-of-songs", "Wisdom and poetry"),
    ("ISA", "Isaiah", [], "old-testament", "isaiah", "Major prophets"),
    ("JER", "Jeremiah", [], "old-testament", "jeremiah", "Major prophets"),
    ("LAM", "Lamentations", [], "old-testament", "lamentations", "Major prophets"),
    ("EZK", "Ezekiel", [], "old-testament", "ezekiel", "Major prophets"),
    ("DAN", "Daniel", [], "old-testament", "daniel", "Major prophets"),
    ("HOS", "Hosea", [], "old-testament", "hosea", "Minor prophets"),
    ("JOL", "Joel", [], "old-testament", "joel", "Minor prophets"),
    ("AMO", "Amos", [], "old-testament", "amos", "Minor prophets"),
    ("OBA", "Obadiah", [], "old-testament", "obadiah", "Minor prophets"),
    ("JON", "Jonah", [], "old-testament", "jonah", "Minor prophets"),
    ("MIC", "Micah", [], "old-testament", "micah", "Minor prophets"),
    ("NAM", "Nahum", [], "old-testament", "nahum", "Minor prophets"),
    ("HAB", "Habakkuk", [], "old-testament", "habakkuk", "Minor prophets"),
    ("ZEP", "Zephaniah", [], "old-testament", "zephaniah", "Minor prophets"),
    ("HAG", "Haggai", [], "old-testament", "haggai", "Minor prophets"),
    ("ZEC", "Zechariah", [], "old-testament", "zechariah", "Minor prophets"),
    ("MAL", "Malachi", [], "old-testament", "malachi", "Minor prophets"),
    ("TOB", "Tobit", [], "deuterocanon", "tobit", "In Catholic and Orthodox Bibles"),
    ("JDT", "Judith", [], "deuterocanon", "judith", "In Catholic and Orthodox Bibles"),
    ("ESG", "Esther (Greek)", ["Greek Esther"], "deuterocanon", "esther-greek", "In Catholic and Orthodox Bibles"),
    ("WIS", "Wisdom of Solomon", ["Wisdom"], "deuterocanon", "wisdom-of-solomon", "In Catholic and Orthodox Bibles"),
    ("SIR", "Sirach", ["Ecclesiasticus"], "deuterocanon", "sirach", "In Catholic and Orthodox Bibles"),
    ("BAR", "Baruch", [], "deuterocanon", "baruch", "In Catholic and Orthodox Bibles"),
    ("1MA", "1 Maccabees", [], "deuterocanon", "1-maccabees", "In Catholic and Orthodox Bibles"),
    ("2MA", "2 Maccabees", [], "deuterocanon", "2-maccabees", "In Catholic and Orthodox Bibles"),
    ("DAG", "Daniel (Greek)", ["Greek Daniel"], "deuterocanon", "daniel-greek", "In Catholic and Orthodox Bibles"),
    ("1ES", "1 Esdras", [], "deuterocanon", "1-esdras", "In Orthodox Bibles"),
    ("MAN", "Prayer of Manasseh", ["Prayer of Manasses"], "deuterocanon", "prayer-of-manasseh", "In Orthodox Bibles"),
    ("PS2", "Psalm 151", [], "deuterocanon", "psalm-151", "In Orthodox Bibles"),
    ("3MA", "3 Maccabees", [], "deuterocanon", "3-maccabees", "In Orthodox Bibles"),
    ("2ES", "2 Esdras", [], "deuterocanon", "2-esdras", "In some Orthodox Bibles"),
    ("4MA", "4 Maccabees", [], "deuterocanon", "4-maccabees", "In some Orthodox Bibles"),
    ("MAT", "Matthew", [], "new-testament", "matthew", "Gospels"),
    ("MRK", "Mark", [], "new-testament", "mark", "Gospels"),
    ("LUK", "Luke", [], "new-testament", "luke", "Gospels"),
    ("JHN", "John", [], "new-testament", "john", "Gospels"),
    ("ACT", "Acts", [], "new-testament", "acts", "Acts"),
    ("ROM", "Romans", [], "new-testament", "romans", "Letters of Paul"),
    ("1CO", "1 Corinthians", [], "new-testament", "1-corinthians", "Letters of Paul"),
    ("2CO", "2 Corinthians", [], "new-testament", "2-corinthians", "Letters of Paul"),
    ("GAL", "Galatians", [], "new-testament", "galatians", "Letters of Paul"),
    ("EPH", "Ephesians", [], "new-testament", "ephesians", "Letters of Paul"),
    ("PHP", "Philippians", [], "new-testament", "philippians", "Letters of Paul"),
    ("COL", "Colossians", [], "new-testament", "colossians", "Letters of Paul"),
    ("1TH", "1 Thessalonians", [], "new-testament", "1-thessalonians", "Letters of Paul"),
    ("2TH", "2 Thessalonians", [], "new-testament", "2-thessalonians", "Letters of Paul"),
    ("1TI", "1 Timothy", [], "new-testament", "1-timothy", "Letters of Paul"),
    ("2TI", "2 Timothy", [], "new-testament", "2-timothy", "Letters of Paul"),
    ("TIT", "Titus", [], "new-testament", "titus", "Letters of Paul"),
    ("PHM", "Philemon", [], "new-testament", "philemon", "Letters of Paul"),
    ("HEB", "Hebrews", [], "new-testament", "hebrews", "Hebrews and the general letters"),
    ("JAS", "James", [], "new-testament", "james", "Hebrews and the general letters"),
    ("1PE", "1 Peter", [], "new-testament", "1-peter", "Hebrews and the general letters"),
    ("2PE", "2 Peter", [], "new-testament", "2-peter", "Hebrews and the general letters"),
    ("1JN", "1 John", [], "new-testament", "1-john", "Hebrews and the general letters"),
    ("2JN", "2 John", [], "new-testament", "2-john", "Hebrews and the general letters"),
    ("3JN", "3 John", [], "new-testament", "3-john", "Hebrews and the general letters"),
    ("JUD", "Jude", [], "new-testament", "jude", "Hebrews and the general letters"),
    ("REV", "Revelation", [], "new-testament", "revelation", "Revelation"),
]

BY_CODE = {code: (name, aliases, group, slug) for code, name, aliases, group, slug, _ in BOOKS}
NAMES = {}
for _code, _name, _aliases, _group, _slug, _section in BOOKS:
    for _label in [_name, *_aliases]:
        NAMES[_label.lower()] = _code

URL = re.compile(rf"^{re.escape(BASE)}(?:(?P<book>[A-Z0-9]{{3}})\.htm|(?P<code>[A-Z0-9]{{3}})(?P<chapter>\d{{2,3}})\.htm(?:#V(?P<verse>\d+))?)$")
EBIBLE = re.compile(r"https?://(?:www\.)?ebible\.org/[^)\s>]*", re.IGNORECASE)
MD_LINK = re.compile(r"\[([^\]]+)\]\((https?://(?:www\.)?ebible\.org/[^)\s]+)\)", re.IGNORECASE)
FENCE = re.compile(r"^\s*(```|~~~)")
# "Book 3", "Book 3:16", "Book 3:16–18", "Book 3:16–4:2", "Book 3–4"; the book name may start with a digit.
REFERENCE = re.compile(
    r"^(?P<book>(?:[1-4] )?[A-Za-z][A-Za-z ()]*?)(?: (?P<c1>\d+)(?::(?P<v1>\d+))?"
    r"(?:(?P<dash>[–-])(?:(?P<c2>\d+):(?P<v2a>\d+)|(?P<n2>\d+)))?)?$"
)


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))["books"]


def chapter_file(code, chapter, data):
    digits = data[code]["digits"]
    return f"{code}{chapter:0{digits}d}.htm"


def parse(text, data):
    """Parse a reference. Returns (code, chapter, verse, end chapter, end verse) or raises ValueError.
    chapter is None for a whole book; verse is None for whole chapters."""
    text = text.strip()
    if text.lower().startswith("psalm 151"):
        # Psalm 151 is a book of one psalm: "Psalm 151:4" means its verse 4.
        rest = text[len("psalm 151"):]
        if rest == "":
            return ("PS2", None, None, None, None)
        match = re.fullmatch(r":(\d+)(?:([–-])(\d+))?", rest)
        if not match:
            raise ValueError("write Psalm 151 references as \"Psalm 151:4\" or \"Psalm 151:1–7\"")
        if match.group(2) == "-":
            raise ValueError("use an en dash (–) in verse ranges, not a hyphen")
        start = int(match.group(1))
        return ("PS2", 1, start, 1, int(match.group(3)) if match.group(3) else start)
    match = REFERENCE.match(text)
    if not match:
        raise ValueError("not a Bible reference such as \"John 3:16\" or \"Matthew 22:34–40\"")
    code = NAMES.get(match.group("book").strip().lower())
    if code is None:
        raise ValueError(f"unknown book \"{match.group('book').strip()}\" (see `bible_refs.py books`)")
    if match.group("dash") == "-":
        raise ValueError("use an en dash (–) in ranges, not a hyphen")
    chapters = data[code]["chapters"]
    if match.group("c1") is None:
        return (code, None, None, None, None)
    c1 = int(match.group("c1"))
    v1 = int(match.group("v1")) if match.group("v1") else None
    c2 = int(match.group("c2")) if match.group("c2") else None
    v2 = int(match.group("v2a")) if match.group("v2a") else None
    n2 = int(match.group("n2")) if match.group("n2") else None
    if len(chapters) == 1 and v1 is None and c1 is not None:
        # One-chapter books are cited by verse: "Jude 3", "Philemon 4–7".
        v1, c1 = c1, 1
        if n2 is not None:
            v2, c2, n2 = n2, 1, None
    if v1 is None:
        # Whole chapters: "Psalm 23", "Isaiah 52–53".
        end = n2 if n2 is not None else c1
        return (code, c1, None, end, None)
    if n2 is not None:
        c2, v2 = c1, n2
    if c2 is None:
        c2, v2 = c1, v1
    return (code, c1, v1, c2, v2)


def validate(ref, data):
    """Return a problem with the parsed reference's chapters and verses, or None."""
    code, c1, v1, c2, v2 = ref
    if c1 is None:
        return None
    chapters = data[code]["chapters"]
    name = BY_CODE[code][0]
    for chapter in (c1, c2):
        if str(chapter) not in chapters:
            return f"{name} has no chapter {chapter} in the WEBBE (chapters {min(map(int, chapters))}–{max(map(int, chapters))})"
    if (c2, v2 or 0) < (c1, v1 or 0):
        return "the range ends before it starts"
    for chapter, verse in ((c1, v1), (c2, v2)):
        if verse is not None and not 1 <= verse <= chapters[str(chapter)]:
            label = name if len(chapters) == 1 else f"{name} {chapter}"
            return f"{label} has verses 1–{chapters[str(chapter)]} in the WEBBE"
    return None


def url_for(ref, data):
    code, c1, v1, _, _ = ref
    if c1 is None:
        return f"{BASE}{code}.htm"
    anchor = f"#V{v1}" if v1 is not None else ""
    return f"{BASE}{chapter_file(code, c1, data)}{anchor}"


def normalise(text):
    """The reference with en dashes, for `link`."""
    return re.sub(r"(?<=\d)-(?=\d)", "–", text.strip())


def markdown_files(paths):
    if paths:
        return [Path(p).resolve() for p in paths]
    return [p for p in sorted(ROOT.rglob("*.md")) if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts)]


def check(paths):
    data = load()
    problems, links = [], 0
    for path in markdown_files(paths):
        relative = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        in_fence = False
        for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), start=1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            found = MD_LINK.findall(line)
            bare = len(EBIBLE.findall(line)) - len(found)
            if bare > 0:
                problems.append(f"{relative}:{number}: ebible.org address outside a Markdown link")
            for text, url in found:
                links += 1
                where = f"{relative}:{number}: [{text}]"
                if not url.startswith(BASE):
                    problems.append(f"{where}: link the {EDITION} edition ({BASE}), not {url}")
                    continue
                if url in (BASE, f"{BASE}index.htm"):
                    continue  # a link to the edition itself
                try:
                    ref = parse(text, data)
                except ValueError as error:
                    problems.append(f"{where}: {error}")
                    continue
                problem = validate(ref, data)
                if problem:
                    problems.append(f"{where}: {problem}")
                    continue
                expected = url_for(ref, data)
                if url != expected:
                    problems.append(f"{where}: links {url}, expected {expected}")
    for problem in problems:
        print(problem)
    if problems:
        print(f"\n{len(problems)} problem(s) in Bible references. Create links with: python3 scripts/bible_refs.py link \"John 3:16\"")
        return 1
    print(f"OK: {links} Bible references checked against the WEBBE.")
    return 0


def link(references):
    data = load()
    status = 0
    for text in references:
        text = normalise(text)
        try:
            ref = parse(text, data)
            problem = validate(ref, data)
        except ValueError as error:
            problem = str(error)
        if problem:
            print(f"{text}: {problem}", file=sys.stderr)
            status = 1
            continue
        print(f"[{text}]({url_for(ref, data)})")
    return status


def books():
    data = load()
    current = None
    for code, name, aliases, group, slug, section in BOOKS:
        if group != current:
            current = group
            print(f"\n{group}")
        chapters = data[code]["chapters"]
        also = f" (also: {', '.join(aliases)})" if aliases else ""
        print(f"  {code}  {name}{also}: {len(chapters)} chapter(s), {section}, page bible/{group}/{slug}.md")
    return 0


def build_data(source):
    if source:
        raw = Path(source).read_bytes()
    else:
        request = urllib.request.Request(ZIP_URL, headers={"User-Agent": "christian-guidelines bible_refs.py"})
        with urllib.request.urlopen(request, timeout=120) as response:
            raw = response.read()
    archive = zipfile.ZipFile(io.BytesIO(raw))
    chapter_name = re.compile(r"^(?:.*/)?([A-Z0-9]{3})(\d{2,3})\.htm$")
    verse_id = re.compile(r'id="V(\d+)"')
    result = {}
    for info in archive.infolist():
        match = chapter_name.match(info.filename)
        if not match or match.group(1) not in BY_CODE:
            continue
        code, number = match.group(1), match.group(2)
        verses = [int(v) for v in verse_id.findall(archive.read(info).decode("utf-8", "replace"))]
        verses = [v for v in verses if v > 0]
        book = result.setdefault(code, {"digits": len(number), "chapters": {}})
        if verses and int(number) > 0:
            book["chapters"][str(int(number))] = max(verses)
    missing = [code for code in BY_CODE if code not in result or not result[code]["chapters"]]
    if missing:
        sys.exit(f"The archive has no chapters for: {', '.join(missing)}")
    ordered = {code: {"digits": result[code]["digits"],
                      "chapters": dict(sorted(result[code]["chapters"].items(), key=lambda kv: int(kv[0])))}
               for code in BY_CODE}
    payload = {"edition": EDITION, "base": BASE, "source": ZIP_URL, "books": ordered}
    DATA.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    chapters = sum(len(book["chapters"]) for book in ordered.values())
    print(f"wrote {DATA.relative_to(ROOT)}: {len(ordered)} books, {chapters} chapters")
    return 0


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("check", "link", "books", "build-data"):
        print(__doc__)
        return 2
    command, args = sys.argv[1], sys.argv[2:]
    if command == "check":
        return check(args)
    if command == "link":
        return link(args) if args else (print(__doc__), 2)[1]
    if command == "books":
        return books()
    return build_data(args[0] if args else None)


if __name__ == "__main__":
    sys.exit(main())

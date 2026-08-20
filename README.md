# veritastimmy

Wikipedia editing tools and legal-exhibit tooling.

## Quickstart

    ./setup_venv.sh
    source venv/bin/activate

### Conda Setup + Aliases

If you prefer Conda, run:

    ./setup_conda.sh [env_name] [python_version]

This will create/activate a Conda environment and install `requirements.txt`.

## Project Structure

    bin/        # CLI scripts (wiki editing, PDF comparison)
    lib/        # Local Python packages (pdf_utils)
    docs/       # Project notes (TODO, ACJ exhibits inventory)
    scripts/    # Exhibit markdown generation helpers
    tpl/        # Templates for generated exhibit docs
    tests/      # Tests + fixtures (wiki samples, case documents)
    setup_venv.sh    # venv environment setup
    setup_conda.sh   # Conda environment setup
    requirements.txt

## Wiki Utilities

- `bin/wiki_lang_pick.py` — list a page's available language versions and
  print the selected version's raw wikitext for analysis or comparison; can
  also post a note to the article's talk page.

  Examples:
  - List language versions:
    `python3 bin/wiki_lang_pick.py "Tim Ballard" --list`
  - Pick a version and output raw wikitext:
    `python3 bin/wiki_lang_pick.py "Tim Ballard" --pick 2 --raw`
  - Post a note to the talk page (requires credentials JSON):
    `python3 bin/wiki_lang_pick.py "Tim Ballard" --pick 0 --post-talk "Note for editors" --credentials tests/inputs/wiki_credentials.json`

- `bin/wiki_replace_edit.py` — make a single, exact-match text replacement on
  a live page. The safe, targeted way to make a small change: it fetches the
  page itself at edit time, requires the `--old` string to match exactly
  once, and rejects the save (editconflict) if anyone else edited the page
  in between rather than clobbering their change. Supports `--dry-run` to
  preview the diff before posting.

  Example:
  `python3 bin/wiki_replace_edit.py "Tim Ballard" --old "..." --new "..." --summary "..." --credentials tests/inputs/wiki_credentials.json --dry-run`

- `bin/wiki_page_edit.py` — edit a page's full contents (optionally
  `--append` instead of replace), with an optional talk-page note. Without
  `--append`, this **replaces the entire page** with no find/replace and no
  edit-conflict protection — prefer `wiki_replace_edit.py` for targeted
  changes; use this only when you genuinely intend to replace/seed a whole
  page.

  Example:
  `python3 bin/wiki_page_edit.py "Sandbox" --message-file tests/inputs/wiki_page_edit_sample.txt --summary "Update sandbox" --append --talk-message-file tests/inputs/wiki_talk_sample.txt --talk-summary "Note to editors" --credentials tests/inputs/wiki_credentials.json`

Credentials format (JSON):
```json
{
  "username": "YourBotUsername",
  "password": "YourBotPassword"
}
```

To avoid committing secrets, copy `tests/inputs/wiki_credentials.json.example` to
`tests/inputs/wiki_credentials.json` and fill in your real credentials (the
real file is gitignored).

## Exhibit Markdown Generation

`scripts/new_exhibit.sh` fills `tpl/exhibit.md.tpl` and writes a markdown
exhibit doc (plus a run log) to a target directory:

    ./scripts/new_exhibit.sh [run_dir] [doc_basename] [title] [author] [date]
    # e.g. ./scripts/new_exhibit.sh exhibits/sourcing_1 ex1 "Source Provenance" "" "August 2026"

`scripts/exif2table.sh` builds a markdown "EXIF-Verified Provenance" table
from one or more image files (requires `exiftool`):

    ./scripts/exif2table.sh path/to/*.jpg >> exhibits/sourcing_1/ex1.md

Ported from `joderswar`'s exhibit tooling; kept output to `.md` only (no
pandoc/PDF build step here).

## Case Exhibit Archive

`tests/inputs/ballard/` holds primary-source court filings and related
documents for the Ballard civil suits. `tests/inputs/ballard/acj/` holds
documents pulled from American Crime Journal's ("ACJ") O.U.R./Ballard
investigative archive; see `ACJ_HOLDINGS.md` in that directory for the full
inventory and provenance notes.

## PDF Comparison

`bin/compare_pdfs.py` compares two PDFs (checksum, `pdfinfo` metadata, and a
`pdftotext` content diff) and writes a markdown report. Requires
poppler-utils (`pdfinfo`, `pdftotext`) on PATH:

    python3 bin/compare_pdfs.py file_a.pdf file_b.pdf \
        --label-a "PACER" --label-b "ACJ" \
        --out tests/outputs/pdf_compare/report.md

Core logic lives in `lib/pdf_utils.py`. Used to check duplicate/near-duplicate
exhibits between the PACER-sourced case files and the ACJ archive above.

## Instagram Watch

`bin/ig_watch_ballard.py` checks the `tim_ballard89` Instagram profile once
per run for video posts made *today* that haven't been seen before, and
appends each one as a link (URL, shortcode, timestamp, caption) to
`data/dlwm_input_queue.jsonl` — a queue for downstream processing elsewhere.
It only identifies and queues; it never downloads media, comments, or
engagement data.

    python3 bin/ig_watch_ballard.py

Auth reuses Netscape-format `cookies.txt` files (as exported by yt-dlp)
rather than an interactive login. It tries `conf/instagram.cookies.txt`,
then `conf/instagram.cookies.2.txt`, in order, verifying each is actually
logged in before trusting it and falling through on failure. `conf/` is
gitignored — cookies never get committed. To convert a cookie file into a
standalone instaloader session file instead (e.g. for reuse by another
instaloader-based tool), use `bin/ig_cookie_bridge.py conf/some.cookies.txt`.

Every run also updates `data/ig_watch_state.json` (dedup so a rerun never
double-queues a post) and appends one line to `data/ig_watch_wakeup.log`
summarizing what happened — meant to be the signal a downstream consumer
checks to know whether the queue has anything new. Cron (2am daily example):

    0 2 * * * cd /path/to/veritastimmy && \
        /path/to/venv/bin/python3 bin/ig_watch_ballard.py \
        >> data/ig_watch_cron.log 2>&1

Don't increase the polling frequency without checking first — running it
more often risks the logged-in account getting flagged.

## Requirements

- Python 3.9+
- `requests`, `pytest`, `instaloader` (`pip install -r requirements.txt`)
- poppler-utils (`pdfinfo`, `pdftotext`) for `bin/compare_pdfs.py`
- `exiftool` for `scripts/exif2table.sh`

## Credits

Developed by BG Bear Guards – March 2025 (renamed 2026-08-05 at project owner's request; the
prior name was an inside joke that didn't read well out of context, so it's retired.)

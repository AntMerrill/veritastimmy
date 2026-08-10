#!/usr/bin/env python3
"""
Make a single, exact-match text replacement on a live MediaWiki page — the
targeted alternative to wiki_page_edit.py's full-page --message/--message-file
replace, which has no find/replace and no edit-conflict protection (it just
overwrites whatever `text=` you hand it).

This script:
  - fetches the CURRENT page text and revision timestamp itself (never takes
    a locally-cached copy as input), along with the server's current time
  - requires the --old string to appear in that text EXACTLY ONCE (refuses to
    run on 0 or >1 matches, so it can't guess wrong)
  - submits the edit with basetimestamp/starttimestamp so MediaWiki rejects
    the save (editconflict) if anyone else edited the page in between,
    instead of silently clobbering their change
  - supports --dry-run to print the unified diff without posting anything

Examples:
  python3 wiki_replace_edit.py "Tim Ballard" \
    --old "''Hidden War'' (2025)" \
    --new "''[[Hidden War (film)|Hidden War]]'' (2025)" \
    --summary "Wikilink Hidden War to the new article" \
    --credentials tests/inputs/wiki_credentials.json --dry-run

  # drop --dry-run once the diff looks right, to actually post it
"""

from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path
from typing import Dict, Optional, Tuple

import requests


def mw_get(session: requests.Session, api: str, **params) -> dict:
    params = {"format": "json", **params}
    r = session.get(api, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def mw_post(session: requests.Session, api: str, **params) -> dict:
    params = {"format": "json", **params}
    r = session.post(api, data=params, timeout=30)
    r.raise_for_status()
    return r.json()


def load_credentials(path: Path) -> Dict[str, str]:
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ValueError("Credentials file must contain a JSON object.")
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        raise ValueError("Credentials must include 'username' and 'password'.")
    return {"username": username, "password": password}


def login(session: requests.Session, api: str, username: str, password: str) -> None:
    token_res = mw_get(session, api, action="query", meta="tokens", type="login")
    token = token_res["query"]["tokens"]["logintoken"]
    login_res = mw_post(
        session,
        api,
        action="login",
        lgname=username,
        lgpassword=password,
        lgtoken=token,
    )
    result = login_res.get("login", {}).get("result")
    if result != "Success":
        raise RuntimeError(f"Login failed: {result}")


def fetch_csrf_token(session: requests.Session, api: str) -> str:
    token_res = mw_get(session, api, action="query", meta="tokens")
    return token_res["query"]["tokens"]["csrftoken"]


def fetch_current_page(session: requests.Session, api: str, title: str) -> Tuple[str, str, str]:
    """Return (content, basetimestamp, starttimestamp) for the live page, right now."""
    res = mw_get(
        session,
        api,
        action="query",
        titles=title,
        prop="revisions",
        rvslots="main",
        rvprop="content|timestamp",
        curtimestamp=1,
        formatversion=2,
    )
    pages = res["query"]["pages"]
    if not pages or pages[0].get("missing"):
        raise RuntimeError(f"Page {title!r} does not exist.")
    page = pages[0]
    rev = page["revisions"][0]
    content = rev["slots"]["main"]["content"]
    basetimestamp = rev["timestamp"]
    starttimestamp = res["curtimestamp"]
    return content, basetimestamp, starttimestamp


def apply_replacement(content: str, old: str, new: str) -> str:
    count = content.count(old)
    if count == 0:
        raise RuntimeError(
            "--old text not found in the current page — it may have already "
            "changed since you last looked. Re-check before retrying."
        )
    if count > 1:
        raise RuntimeError(
            f"--old text is not unique ({count} occurrences) — refusing an "
            "ambiguous replacement. Give more surrounding context in --old."
        )
    return content.replace(old, new)


def edit_page_conflict_safe(
    session: requests.Session,
    api: str,
    title: str,
    new_text: str,
    summary: str,
    basetimestamp: str,
    starttimestamp: str,
) -> str:
    token = fetch_csrf_token(session, api)
    params = {
        "action": "edit",
        "title": title,
        "summary": summary,
        "token": token,
        "bot": True,
        "nocreate": True,
        "text": new_text,
        "basetimestamp": basetimestamp,
        "starttimestamp": starttimestamp,
    }
    res = mw_post(session, api, **params)
    if "error" in res:
        code = res["error"].get("code")
        if code == "editconflict":
            raise RuntimeError(
                "Edit conflict: the page changed after it was fetched. "
                "Nothing was overwritten — re-run to pick up the latest text."
            )
        raise RuntimeError(f"Edit failed: {res['error']}")
    edit = res.get("edit", {})
    if edit.get("result") != "Success":
        raise RuntimeError(f"Edit failed: {res}")
    return edit.get("newrevid", "")


def read_text_arg(value: Optional[str], value_file: Optional[str], label: str) -> str:
    if value and value_file:
        raise SystemExit(f"Use only one of --{label} or --{label}-file.")
    if not value and not value_file:
        raise SystemExit(f"--{label} or --{label}-file is required.")
    return value if value is not None else Path(value_file).read_text()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("title", help="Wikipedia title (for example: Tim Ballard)")
    ap.add_argument(
        "--api",
        default="https://en.wikipedia.org/w/api.php",
        help="MediaWiki API endpoint.",
    )
    ap.add_argument("--old", help="Exact existing text to find (must be unique on the page).")
    ap.add_argument("--old-file", help="File containing the exact existing text to find.")
    ap.add_argument("--new", help="Replacement text.")
    ap.add_argument("--new-file", help="File containing the replacement text.")
    ap.add_argument(
        "--summary",
        default="Targeted edit from wiki_replace_edit.py",
        help="Edit summary when updating the page.",
    )
    ap.add_argument(
        "--credentials",
        required=True,
        help="Path to JSON credentials file with username/password for posting.",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch the live page, show the diff, and stop without posting anything.",
    )
    ap.add_argument("--stdout", action="store_true", help="Print success details to STDOUT.")
    args = ap.parse_args()

    old = read_text_arg(args.old, args.old_file, "old")
    new = read_text_arg(args.new, args.new_file, "new")
    creds = load_credentials(Path(args.credentials))

    with requests.Session() as s:
        s.headers.update({"User-Agent": "AntMerrillWikiTool/0.4 (targeted edit; automation)"})

        # Fetching is unauthenticated-safe, but logging in first means the
        # basetimestamp we grab is as close as possible to the edit itself.
        login(s, args.api, creds["username"], creds["password"])

        content, basetimestamp, starttimestamp = fetch_current_page(s, args.api, args.title)
        new_content = apply_replacement(content, old, new)

        diff = "".join(
            difflib.unified_diff(
                content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=f"{args.title} (live)",
                tofile=f"{args.title} (proposed)",
            )
        )
        print(diff)

        if args.dry_run:
            print("--dry-run: nothing posted.")
            return 0

        new_rev = edit_page_conflict_safe(
            s,
            args.api,
            args.title,
            new_content,
            args.summary,
            basetimestamp,
            starttimestamp,
        )
        if args.stdout:
            print(f"Updated page {args.title} (rev {new_rev}).", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Anonymous MediaWiki fetcher with numbered language selection.

What it does:
1) Lists language versions (langlinks) for an EN page, numbered.
2) You pick a number (via --pick N or interactive prompt).
3) Prints the chosen page's full wikitext body to STDOUT.

New:
- --raw : print ONLY the wikitext body (no numbered list, no BEGIN/END markers)

Examples:
  # list versions
  python3 wiki_lang_pick.py "Tim Ballard" --list

  # pick version #2 and print body to STDOUT
  python3 wiki_lang_pick.py "Tim Ballard" --pick 2

  # interactive: list then ask for number
  python3 wiki_lang_pick.py "Tim Ballard"

  # save output (with markers)
  python3 wiki_lang_pick.py "Tim Ballard" --pick 2 > out.wikitext

  # save output (raw body only)
  python3 wiki_lang_pick.py "Tim Ballard" --pick 2 --raw > out.wikitext
"""

from __future__ import annotations

import argparse
from typing import Dict, List, Optional, Tuple

import requests


EN_API = "https://en.wikipedia.org/w/api.php"


def api_for_lang(lang: str) -> str:
    return f"https://{lang}.wikipedia.org/w/api.php"


def mw_get(session: requests.Session, api: str, **params) -> dict:
    params = {"format": "json", **params}
    r = session.get(api, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def get_langlinks(session: requests.Session, en_title: str) -> Dict[str, str]:
    """
    Return dict: lang_code -> localized title
    """
    langlinks: Dict[str, str] = {}
    llcontinue = None

    while True:
        params = dict(
            action="query",
            titles=en_title,
            prop="langlinks",
            lllimit="max",
        )
        if llcontinue:
            params["llcontinue"] = llcontinue

        res = mw_get(session, EN_API, **params)
        pages = res.get("query", {}).get("pages", {})
        page = next(iter(pages.values()))
        for ll in page.get("langlinks", []) or []:
            langlinks[ll["lang"]] = ll["*"]

        cont = res.get("continue", {})
        if "llcontinue" not in cont:
            break
        llcontinue = cont["llcontinue"]

    return dict(sorted(langlinks.items(), key=lambda kv: kv[0]))


def fetch_wikitext(session: requests.Session, api: str, title: str) -> Optional[str]:
    res = mw_get(
        session,
        api,
        action="query",
        prop="revisions",
        titles=title,
        rvprop="content|timestamp|ids",
        rvslots="main",
    )
    pages = res.get("query", {}).get("pages", {})
    page = next(iter(pages.values()))
    if "missing" in page:
        return None
    rev = page["revisions"][0]
    slot = rev.get("slots", {}).get("main", {})
    text = slot.get("*") or rev.get("*")
    return text


def build_numbered_versions(en_title: str, langlinks: Dict[str, str]) -> List[Tuple[str, str]]:
    """
    Returns a list of (lang_code, title) including EN at index 0.
    """
    versions: List[Tuple[str, str]] = [("en", en_title)]
    for lang, title in langlinks.items():
        versions.append((lang, title))
    return versions


def print_versions(versions: List[Tuple[str, str]]) -> None:
    for i, (lang, title) in enumerate(versions):
        print(f"{i}: {lang}\t{title}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("title", nargs="?", default="Tim Ballard", help="EN Wikipedia title (default: Tim Ballard)")
    ap.add_argument("--list", action="store_true", help="List numbered language versions and exit")
    ap.add_argument("--pick", type=int, help="Pick a numbered version and print its wikitext to STDOUT")
    ap.add_argument("--raw", action="store_true", help="Print ONLY the wikitext body (no list/markers)")
    args = ap.parse_args()

    en_title = args.title

    with requests.Session() as s:
        s.headers.update(
            {"User-Agent": "AntMerrillWikiTool/0.4 (anonymous; lang pick; research)"}
        )

        langlinks = get_langlinks(s, en_title)
        versions = build_numbered_versions(en_title, langlinks)

        # If --raw: do NOT print the numbered list (clean output for piping)
        if not args.raw:
            print_versions(versions)

        if args.list:
            return 0

        pick = args.pick
        if pick is None:
            # If --raw and interactive, we still need to ask for a number.
            # But we should not have printed the list, so prompt is on stdin.
            try:
                pick_str = input("\nPick a number: ").strip()
                pick = int(pick_str)
            except Exception:
                if not args.raw:
                    print("Invalid selection.", flush=True)
                return 2

        if pick < 0 or pick >= len(versions):
            if not args.raw:
                print(f"Pick must be between 0 and {len(versions)-1}.", flush=True)
            return 2

        lang, title = versions[pick]
        api = api_for_lang(lang)

        text = fetch_wikitext(s, api, title)
        if text is None:
            if not args.raw:
                print(f"Could not fetch wikitext for {lang}:{title}", flush=True)
            return 3

        if args.raw:
            # Body only, perfect for piping/redirection
            print(text, end="" if text.endswith("\n") else "\n")
        else:
            print("\n---BEGIN_WIKITEXT---")
            print(text, end="" if text.endswith("\n") else "\n")
            print("---END_WIKITEXT---")

        return 0


if __name__ == "__main__":
    raise SystemExit(main())


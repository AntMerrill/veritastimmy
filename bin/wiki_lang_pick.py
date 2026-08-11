#!/usr/bin/env python3
"""
Anonymous MediaWiki fetcher with numbered language selection.

What it does:
1) Lists language versions (langlinks) for an EN page, numbered.
2) You pick a number (via --pick N or interactive prompt).
3) Writes the chosen page's full wikitext body to a file in tests/ by default.

New:
- --raw : print ONLY the wikitext body (no numbered list, no BEGIN/END markers)
- --json : write JSON output with wikitext + sections
- --post-talk / --post-talk-file : append a note to the selected talk page

Examples:
  # list versions
  python3 wiki_lang_pick.py "Tim Ballard" --list

  # pick version #2 and write to tests/
  python3 wiki_lang_pick.py "Tim Ballard" --pick 2

  # interactive: list then ask for number
  python3 wiki_lang_pick.py "Tim Ballard"

  # save output elsewhere (with markers)
  python3 wiki_lang_pick.py "Tim Ballard" --pick 2 --out-dir ./exports

  # save output (raw body only)
  python3 wiki_lang_pick.py "Tim Ballard" --pick 2 --raw --out-dir ./exports

  # print output to STDOUT instead of writing a file
  python3 wiki_lang_pick.py "Tim Ballard" --pick 2 --stdout

  # append a message to the talk page (credentials required)
  python3 wiki_lang_pick.py "Tim Ballard" --pick 0 --post-talk "Note" --credentials tests/inputs/wiki_credentials.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
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


def mw_post(session: requests.Session, api: str, **params) -> dict:
    params = {"format": "json", **params}
    r = session.post(api, data=params, timeout=30)
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


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = value.strip("_")
    return value or "untitled"


def split_wikitext_sections(text: str) -> List[dict]:
    sections: List[dict] = []
    current = {"title": None, "content": []}
    for line in text.splitlines():
        match = re.match(r"^(=+)\s*(.*?)\s*\1\s*$", line)
        if match:
            sections.append(
                {
                    "title": current["title"],
                    "content": "\n".join(current["content"]).rstrip(),
                }
            )
            current = {"title": match.group(2), "content": []}
            continue
        current["content"].append(line)
    sections.append(
        {
            "title": current["title"],
            "content": "\n".join(current["content"]).rstrip(),
        }
    )
    return sections


def load_credentials(path: Path) -> Dict[str, str]:
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ValueError("Credentials file must contain a JSON object.")
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        raise ValueError("Credentials must include 'username' and 'password'.")
    return {"username": username, "password": password}


def build_talk_title(title: str) -> str:
    if title.lower().startswith("talk:"):
        return title
    return f"Talk:{title}"


def extract_heading(message: str) -> Tuple[Optional[str], str]:
    """
    If `message` opens with a MediaWiki section heading (== Title ==),
    split it into (title, remainder-without-heading). Otherwise (None, message).
    """
    stripped = message.lstrip("\n")
    match = re.match(r"^==\s*(.*?)\s*==[ \t]*\n?", stripped)
    if not match:
        return None, message
    return match.group(1), stripped[match.end():]


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


def post_talk_page(
    session: requests.Session,
    api: str,
    title: str,
    message: str,
    summary: str,
) -> str:
    talk_title = build_talk_title(title)
    token = fetch_csrf_token(session, api)

    params = dict(action="edit", title=talk_title, summary=summary, token=token, bot=True)
    section_title, body = extract_heading(message)
    if section_title:
        # Native "new section" edit: MediaWiki generates the heading and
        # surrounding blank lines itself, so this can never run into
        # whatever the previous section happens to end with (the bug that
        # bit us with plain appendtext: no guaranteed separator, so a
        # heading with no leading blank line merges into the prior thread).
        params.update(section="new", sectiontitle=section_title, text=body)
    else:
        # No heading in the message: append, but force separation from
        # whatever's already there.
        params["appendtext"] = "\n\n" + message.lstrip("\n")

    res = mw_post(session, api, **params)
    edit = res.get("edit", {})
    if edit.get("result") != "Success":
        raise RuntimeError(f"Edit failed: {edit}")
    return edit.get("newrevid", "")


def build_output_path(out_dir: Path, lang: str, title: str, suffix: str) -> Path:
    slug = slugify(f"{lang}_{title}")
    return out_dir / f"{slug}{suffix}"


def write_output(
    out_dir: Path,
    lang: str,
    title: str,
    text: str,
    raw: bool,
    json_output: bool,
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    if json_output:
        payload = {
            "language": lang,
            "title": title,
            "wikitext": text,
            "sections": split_wikitext_sections(text),
        }
        path = build_output_path(out_dir, lang, title, ".json")
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        return path

    path = build_output_path(out_dir, lang, title, ".wikitext")
    if raw:
        body = text
    else:
        body = "\n".join(
            [
                "---BEGIN_WIKITEXT---",
                text.rstrip(),
                "---END_WIKITEXT---",
                "",
            ]
        )
    path.write_text(body)
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("title", nargs="?", default="Tim Ballard", help="EN Wikipedia title (default: Tim Ballard)")
    ap.add_argument("--list", action="store_true", help="List numbered language versions and exit")
    ap.add_argument("--pick", type=int, help="Pick a numbered version and print its wikitext to STDOUT")
    ap.add_argument("--raw", action="store_true", help="Print ONLY the wikitext body (no list/markers)")
    ap.add_argument("--json", action="store_true", help="Write JSON output with wikitext and sections")
    ap.add_argument(
        "--out-dir",
        default="tests",
        help="Directory to write output files (default: tests)",
    )
    ap.add_argument(
        "--stdout",
        action="store_true",
        help="Print output to STDOUT instead of writing to a file",
    )
    ap.add_argument(
        "--post-talk",
        help="Append a message to the selected page's talk page (requires --credentials).",
    )
    ap.add_argument(
        "--post-talk-file",
        help="Append a message from a file to the selected page's talk page (requires --credentials).",
    )
    ap.add_argument(
        "--talk-summary",
        default="Automated note from wiki_lang_pick.py",
        help="Edit summary when posting to the talk page.",
    )
    ap.add_argument(
        "--credentials",
        help="Path to JSON credentials file with username/password for posting.",
    )
    args = ap.parse_args()

    en_title = args.title
    out_dir = Path(args.out_dir)

    with requests.Session() as s:
        s.headers.update(
            {"User-Agent": "AntMerrillWikiTool/0.4 (anonymous; lang pick; research)"}
        )

        langlinks = get_langlinks(s, en_title)
        versions = build_numbered_versions(en_title, langlinks)

        should_print_list = args.list or args.pick is None
        if should_print_list:
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
                if args.stdout:
                    print("Invalid selection.", flush=True)
                return 2

        if pick < 0 or pick >= len(versions):
            if args.stdout:
                print(f"Pick must be between 0 and {len(versions)-1}.", flush=True)
            return 2

        lang, title = versions[pick]
        api = api_for_lang(lang)

        text = fetch_wikitext(s, api, title)
        if text is None:
            if args.stdout:
                print(f"Could not fetch wikitext for {lang}:{title}", flush=True)
            return 3

        if args.stdout:
            if args.json:
                payload = {
                    "language": lang,
                    "title": title,
                    "wikitext": text,
                    "sections": split_wikitext_sections(text),
                }
                print(json.dumps(payload, ensure_ascii=False, indent=2))
            elif args.raw:
                print(text, end="" if text.endswith("\n") else "\n")
            else:
                print("\n---BEGIN_WIKITEXT---")
                print(text, end="" if text.endswith("\n") else "\n")
                print("---END_WIKITEXT---")
        else:
            output_path = write_output(out_dir, lang, title, text, args.raw, args.json)
            print(f"Wrote output to {output_path}", flush=True)

        post_message = None
        if args.post_talk:
            post_message = args.post_talk
        elif args.post_talk_file:
            post_message = Path(args.post_talk_file).read_text()

        if post_message:
            if not args.credentials:
                raise SystemExit("--credentials is required when posting to talk pages.")
            creds = load_credentials(Path(args.credentials))
            login(s, api, creds["username"], creds["password"])
            new_rev = post_talk_page(
                s,
                api,
                title,
                post_message,
                args.talk_summary,
            )
            if args.stdout:
                print(f"Posted to talk page (rev {new_rev}).", flush=True)

        return 0


if __name__ == "__main__":
    raise SystemExit(main())

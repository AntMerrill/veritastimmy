#!/usr/bin/env python3
"""
Edit the contents of a MediaWiki page, with optional talk-page note.

Examples:
  python3 wiki_page_edit.py "Sandbox" --message "Hello" --summary "Update sandbox" \
    --credentials tests/inputs/wiki_credentials.json
  python3 wiki_page_edit.py "Sandbox" --message-file tests/inputs/wiki_page_edit_sample.txt \
    --summary "Update sandbox" --append --credentials tests/inputs/wiki_credentials.json
  python3 wiki_page_edit.py "Sandbox" --message-file tests/inputs/wiki_page_edit_sample.txt \
    --summary "Update sandbox" --append \
    --talk-message-file tests/inputs/wiki_talk_sample.txt \
    --talk-summary "Note to editors" \
    --credentials tests/inputs/wiki_credentials.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Optional

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


def build_talk_title(title: str) -> str:
    if title.lower().startswith("talk:"):
        return title
    return f"Talk:{title}"


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


def edit_page(
    session: requests.Session,
    api: str,
    title: str,
    message: str,
    summary: str,
    append: bool,
) -> str:
    token = fetch_csrf_token(session, api)
    params = {
        "action": "edit",
        "title": title,
        "summary": summary,
        "token": token,
        "bot": True,
    }
    if append:
        params["appendtext"] = message
    else:
        params["text"] = message
    res = mw_post(session, api, **params)
    edit = res.get("edit", {})
    if edit.get("result") != "Success":
        raise RuntimeError(f"Edit failed: {edit}")
    return edit.get("newrevid", "")


def post_talk_page(
    session: requests.Session,
    api: str,
    title: str,
    message: str,
    summary: str,
) -> str:
    talk_title = build_talk_title(title)
    token = fetch_csrf_token(session, api)
    res = mw_post(
        session,
        api,
        action="edit",
        title=talk_title,
        appendtext=message,
        summary=summary,
        token=token,
        bot=True,
    )
    edit = res.get("edit", {})
    if edit.get("result") != "Success":
        raise RuntimeError(f"Edit failed: {edit}")
    return edit.get("newrevid", "")


def read_message(message: Optional[str], message_file: Optional[str]) -> str:
    if message and message_file:
        raise SystemExit("Use only one of --message or --message-file.")
    if not message and not message_file:
        raise SystemExit("--message or --message-file is required.")
    return message or Path(message_file).read_text()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("title", help="Wikipedia title (for example: Sandbox)")
    ap.add_argument(
        "--api",
        default="https://en.wikipedia.org/w/api.php",
        help="MediaWiki API endpoint.",
    )
    ap.add_argument("--message", help="Message to write to the page.")
    ap.add_argument("--message-file", help="File containing the message to write.")
    ap.add_argument(
        "--summary",
        default="Automated edit from wiki_page_edit.py",
        help="Edit summary when updating the page.",
    )
    ap.add_argument(
        "--append",
        action="store_true",
        help="Append to the page instead of replacing it.",
    )
    ap.add_argument(
        "--talk-message",
        help="Append a message to the page's talk page (requires credentials).",
    )
    ap.add_argument(
        "--talk-message-file",
        help="Append a message from a file to the talk page (requires credentials).",
    )
    ap.add_argument(
        "--talk-summary",
        default="Automated note from wiki_page_edit.py",
        help="Edit summary when posting to the talk page.",
    )
    ap.add_argument(
        "--credentials",
        required=True,
        help="Path to JSON credentials file with username/password for posting.",
    )
    ap.add_argument(
        "--stdout",
        action="store_true",
        help="Print success details to STDOUT.",
    )
    args = ap.parse_args()

    message = read_message(args.message, args.message_file)

    talk_message = None
    if args.talk_message:
        talk_message = args.talk_message
    elif args.talk_message_file:
        talk_message = Path(args.talk_message_file).read_text()

    creds = load_credentials(Path(args.credentials))

    with requests.Session() as s:
        s.headers.update(
            {"User-Agent": "AntMerrillWikiTool/0.4 (page edit; automation)"}
        )
        login(s, args.api, creds["username"], creds["password"])
        new_rev = edit_page(
            s,
            args.api,
            args.title,
            message,
            args.summary,
            args.append,
        )
        if args.stdout:
            print(f"Updated page {args.title} (rev {new_rev}).", flush=True)

        if talk_message:
            talk_rev = post_talk_page(
                s,
                args.api,
                args.title,
                talk_message,
                args.talk_summary,
            )
            if args.stdout:
                print(f"Posted to talk page (rev {talk_rev}).", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Overwrite the contents of a MediaWiki user page.

Examples:
  python3 wiki_user_put.py "ExampleUser" --message "Hello!" --credentials tests/inputs/wiki_credentials.json
  python3 wiki_user_put.py "User:ExampleUser" --message-file ./note.txt --summary "Replace content" --credentials tests/inputs/wiki_credentials.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict

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


def build_user_title(username: str) -> str:
    if username.lower().startswith("user:"):
        return username
    return f"User:{username}"


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


def put_user_page(
    session: requests.Session,
    api: str,
    username: str,
    message: str,
    summary: str,
) -> str:
    user_title = build_user_title(username)
    token = fetch_csrf_token(session, api)
    res = mw_post(
        session,
        api,
        action="edit",
        title=user_title,
        text=message,
        summary=summary,
        token=token,
        bot=True,
    )
    edit = res.get("edit", {})
    if edit.get("result") != "Success":
        raise RuntimeError(f"Edit failed: {edit}")
    return edit.get("newrevid", "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("username", help="Username (with or without User: prefix).")
    ap.add_argument(
        "--api",
        default="https://en.wikipedia.org/w/api.php",
        help="MediaWiki API endpoint.",
    )
    ap.add_argument("--message", help="Message to set as the user page contents.")
    ap.add_argument("--message-file", help="File containing the message to set.")
    ap.add_argument(
        "--summary",
        default="Automated overwrite from wiki_user_put.py",
        help="Edit summary when posting to the user page.",
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

    if args.message and args.message_file:
        raise SystemExit("Use only one of --message or --message-file.")
    if not args.message and not args.message_file:
        raise SystemExit("--message or --message-file is required.")

    message = args.message or Path(args.message_file).read_text()
    creds = load_credentials(Path(args.credentials))

    with requests.Session() as s:
        s.headers.update(
            {"User-Agent": "AntMerrillWikiTool/0.4 (user put; automation)"}
        )
        login(s, args.api, creds["username"], creds["password"])
        new_rev = put_user_page(s, args.api, args.username, message, args.summary)
        if args.stdout:
            print(f"Updated user page (rev {new_rev}).", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

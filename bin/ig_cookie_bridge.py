#!/usr/bin/env python3
"""
ig_cookie_bridge.py

Converts a Netscape-format cookies.txt (as exported by yt-dlp) into an
instaloader session file, so scripts using instaloader's session mechanism
can reuse an already-authenticated cookie jar without an interactive
`instaloader --login` prompt.

Verifies the cookies actually belong to a logged-in user (via test_login())
before saving, and refuses to save an anonymous/expired cookie jar.

USAGE:
    python3 bin/ig_cookie_bridge.py conf/instagram.cookies.txt
"""

import argparse
import http.cookiejar
import sys
from pathlib import Path

import instaloader


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("cookie_file", help="Netscape-format cookies.txt to convert")
    args = parser.parse_args()

    cookie_path = Path(args.cookie_file)
    if not cookie_path.exists():
        sys.exit(f"Cookie file not found: {cookie_path}")

    jar = http.cookiejar.MozillaCookieJar(str(cookie_path))
    jar.load(ignore_discard=True, ignore_expires=True)

    loader = instaloader.Instaloader(quiet=True)
    loader.context.update_cookies(jar)

    username = loader.test_login()
    if not username:
        sys.exit(
            f"{cookie_path}: cookies are not an authenticated session "
            f"(no logged-in user found). Not saving."
        )

    loader.context.username = username
    loader.save_session_to_file()
    print(f"{cookie_path}: logged in as '{username}'. Session saved to "
          f"~/.config/instaloader/session-{username}")


if __name__ == "__main__":
    main()

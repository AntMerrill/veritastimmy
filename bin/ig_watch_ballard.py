#!/usr/bin/env python3
"""
ig_watch_ballard.py

Watches a target Instagram profile (default: tim_ballard89) for new video
posts made "today," and queues them for downstream processing by dl_wm.

AUTH:
    Reuses Netscape-format cookies.txt files (e.g. exported by yt-dlp) rather
    than an interactive instaloader login. Tries each file in
    --cookie-file order (default: conf/instagram.cookies.txt, then
    conf/instagram.cookies.2.txt), verifying login via test_login() before
    accepting it, and falls through to the next file on failure. No
    open-ended retrying beyond the given list.

USAGE:
    python3 bin/ig_watch_ballard.py
    python3 bin/ig_watch_ballard.py --cookie-file conf/other.cookies.txt --cookie-file conf/backup.cookies.txt

CRON (2am daily example):
    0 2 * * * cd /path/to/veritastimmy && \
        /path/to/venv/bin/python3 bin/ig_watch_ballard.py \
        >> data/ig_watch_cron.log 2>&1

OUTPUTS:
    - Queue file (JSON lines): each new video hit gets one line:
          {"url": ..., "shortcode": ..., "timestamp": ..., "caption": ...,
           "status": "new", "queued_at": ...}
      dl_wm's intake step should read this file, process entries, and can
      mark them (e.g. rewrite the file with status "done") once consumed.

    - State file (JSON): tracks which shortcodes have already been queued,
      so re-running the script (e.g. multiple cron fires, manual reruns)
      never double-queues the same post.

    - Log file (plain text, append-only): one line per run summarizing what
      happened ("2026-08-19T02:00:03 checked tim_ballard89: 1 new video
      queued" or "... 0 new"). This is the file dl_wm reads on wake-up to
      know whether there's anything in its inbox.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import instaloader
except ImportError:
    sys.exit(
        "Missing dependency: instaloader.\n"
        "Install it with: pip install instaloader"
    )


def load_state(state_file: Path) -> dict:
    if state_file.exists():
        try:
            return json.loads(state_file.read_text())
        except json.JSONDecodeError:
            print(f"WARNING: {state_file} was unreadable/corrupt, starting fresh state.", file=sys.stderr)
    return {"queued_shortcodes": []}


def save_state(state_file: Path, state: dict) -> None:
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, indent=2))


def append_queue_entry(queue_file: Path, entry: dict) -> None:
    queue_file.parent.mkdir(parents=True, exist_ok=True)
    with queue_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def append_log(log_file: Path, message: str) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"{ts} {message}\n")


def get_loader(cookie_files: list) -> "instaloader.Instaloader":
    """
    Try each Netscape-format cookie file in order (as exported by yt-dlp),
    verifying login via test_login() before accepting it. Falls through to
    the next file on failure; exits if none authenticate. No open-ended
    retrying beyond the given list.
    """
    import http.cookiejar

    for cookie_file in cookie_files:
        cookie_path = Path(cookie_file)
        if not cookie_path.exists():
            print(f"WARNING: cookie file not found, skipping: {cookie_path}", file=sys.stderr)
            continue

        loader = instaloader.Instaloader(
            download_pictures=False,
            download_videos=False,
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            compress_json=False,
            quiet=True,
            fatal_status_codes=[429],
        )
        jar = http.cookiejar.MozillaCookieJar(str(cookie_path))
        jar.load(ignore_discard=True, ignore_expires=True)
        loader.context.update_cookies(jar)

        username = loader.context.test_login()
        if username:
            loader.context.username = username
            print(f"Authenticated as '{username}' via {cookie_path}")
            return loader
        print(f"WARNING: {cookie_path} did not authenticate, trying next.", file=sys.stderr)

    sys.exit(
        "No cookie file in the fallback list authenticated. "
        "Refresh the cookies (or their session) and try again."
    )


def find_todays_new_videos(loader, target_username: str, state: dict, max_posts_checked: int = 30):
    """
    Walk the target profile's posts (newest first). Stop once we hit a post
    older than today, since Instagram returns posts in reverse chronological
    order. Yield only video posts from today not already in state.
    """
    profile = instaloader.Profile.from_username(loader.context, target_username)
    today = datetime.now().astimezone().date()
    already_queued = set(state.get("queued_shortcodes", []))

    checked = 0
    for post in profile.get_posts():
        checked += 1
        if checked > max_posts_checked:
            break

        post_date = post.date_local.date()
        if post_date < today:
            break  # older than today; nothing further back matters
        if post_date > today:
            continue  # shouldn't happen, but skip just in case

        if not post.is_video:
            continue
        if post.shortcode in already_queued:
            continue

        yield post


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--target-username", default="tim_ballard89", help="IG account to watch")
    parser.add_argument(
        "--cookie-file", dest="cookie_files", action="append",
        default=None,
        help="Netscape-format cookies.txt to try (repeatable, in fallback order). "
             "Defaults to conf/instagram.cookies.txt, conf/instagram.cookies.2.txt",
    )
    parser.add_argument("--queue-file", default="data/dlwm_input_queue.jsonl", help="Path to dl_wm input queue (JSON lines)")
    parser.add_argument("--state-file", default="data/ig_watch_state.json", help="Path to dedup state file")
    parser.add_argument("--log-file", default="data/ig_watch_wakeup.log", help="Path to wake-up log dl_wm reads")
    args = parser.parse_args()

    cookie_files = args.cookie_files or ["conf/instagram.cookies.txt", "conf/instagram.cookies.2.txt"]
    queue_file = Path(args.queue_file)
    state_file = Path(args.state_file)
    log_file = Path(args.log_file)

    state = load_state(state_file)
    loader = get_loader(cookie_files)

    new_count = 0
    try:
        for post in find_todays_new_videos(loader, args.target_username, state):
            entry = {
                "url": f"https://www.instagram.com/p/{post.shortcode}/",
                "shortcode": post.shortcode,
                "timestamp": post.date_local.isoformat(),
                "caption": (post.caption or "")[:280],
                "status": "new",
                "queued_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
            append_queue_entry(queue_file, entry)
            state.setdefault("queued_shortcodes", []).append(post.shortcode)
            new_count += 1
            print(f"Queued: {entry['url']}")
    except (instaloader.exceptions.ConnectionException,
            instaloader.exceptions.AbortDownloadException) as e:
        append_log(log_file, f"checked {args.target_username}: ERROR (connection/rate-limit) - {e}")
        sys.exit(f"Connection/rate-limit error talking to Instagram: {e}")
    except instaloader.exceptions.LoginRequiredException:
        append_log(log_file, f"checked {args.target_username}: ERROR (session expired)")
        sys.exit("Session expired or invalid. Refresh conf/instagram.cookies*.txt from a logged-in browser/yt-dlp export.")

    save_state(state_file, state)

    if new_count:
        append_log(log_file, f"checked {args.target_username}: {new_count} new video(s) queued")
    else:
        append_log(log_file, f"checked {args.target_username}: 0 new")

    print(f"Done. {new_count} new video(s) queued to {queue_file}")


if __name__ == "__main__":
    main()

# TODO

- [ ] `JustinR1970` wiki bot account is inaccessible — plain password login
      via `action=login` fails (`Login failed: Failed`) against
      `en.wikipedia.org`. Likely needs a Bot Password
      (`Username@AppName` + generated password from `Special:BotPasswords`)
      rather than the account's regular password — but that requires being
      logged into the account itself first, which we don't currently have.
      Any write operation (`wiki_page_edit.py`, `wiki_replace_edit.py`,
      `wiki_lang_pick.py --post-talk`) is blocked until this is resolved.
      Read-only operations (`--list`, `--raw`, `--dry-run`) are unaffected.

- [ ] `bin/ig_watch_ballard.py` (Instagram Watch, see README) is built,
      committed, and covered by an offline test suite (`tests/test_ig_watch_ballard.py`,
      12/12 passing) — but has never had a successful live run against
      Instagram. Cookie auth itself works (confirmed: authenticates as
      `merrillp.jensen` via `conf/instagram.cookies.txt`), but every live
      profile query since has hit `429 Too Many Requests`, most likely
      residual from an early test that let instaloader's default retry
      loop run for ~11 minutes before being killed. Confirmed via a second
      target account (`pickleballandpitty`) that this is an
      account/session-level throttle, not specific to `tim_ballard89`.
      Remaining before this is actually done:
      - [ ] get one clean live run (needs real cooldown time first)
      - [ ] verify idempotency against real data (second run queues 0 new)
      - [ ] set up the cron entry (README has the example line)
      Explicitly not in scope: any `dl_wm`-side intake code — this repo only
      produces the queue file, per project-owner decision to leave `dl_wm`
      alone.

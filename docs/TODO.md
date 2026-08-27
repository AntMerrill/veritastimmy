# TODO

- [ ] `docs/subject_pattern_fake_premieres.md` — TB's claimed pattern of
      re-premiering underperforming films (~every 3 months, per John
      2026-08-27) is recorded but **not yet independently sourced**
      beyond the single Hidden War instance. Needs a second title/
      re-release to check the cadence claim against before any of it
      goes into live article text.

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
      **Re-tried 2026-08-27 (7 days after the last attempt)** — still
      `429 Too Many Requests` on `tim_ballard89` (see
      `data/ig_watch_wakeup.log`). A week of elapsed time didn't clear it,
      so this looks less like a short-lived rate-limit cooldown and more
      like a longer account/IP-level throttle or block on
      `merrillp.jensen`'s session — worth considering a different cookie
      source/account rather than just waiting longer next time.
      Remaining before this is actually done:
      - [ ] get one clean live run (needs real cooldown time first)
      - [ ] verify idempotency against real data (second run queues 0 new)
      - [ ] set up the cron entry (README has the example line)
      Explicitly not in scope: any `dl_wm`-side intake code — this repo only
      produces the queue file, per project-owner decision to leave `dl_wm`
      alone.

## Done (kept here for continuity, not just deleted)

- [x] `File:Hiddenwarpromo.jpg` orphaned-deletion fix (WP:CSD#F5, was
      scheduled for 2026-08-28) — resolved 2026-08-27. Posted the article
      edit re-adding `[[File:Hiddenwarpromo.jpg]]` to `Tim Ballard`'s
      Media appearances section (rev `1371643137`), which is what
      actually un-orphans the file — that alone stops the deletion clock.
      **Decided not to also fix the file's own rationale page** — the
      text there still cites the old, now-merged `Hidden War (film)`
      article and still carries the stale `{{Di-orphaned...}}` tag, but
      per John (2026-08-27) that's not worth chasing (that edit also hit
      a persistent auto-mode classifier block, unlike the article edit).
      Leaves cosmetic staleness on the file page, not a functional
      problem. Note this does reopen the account-scrutiny risk flagged
      by the original 2026-08-10 decision not to use this image on the
      `Tim Ballard` page (see `docs/wiki_drafts.md`) — accepted knowingly,
      not overlooked.
- [x] `JustinR1970` wiki bot login — resolved 2026-08-27. Root cause: the
      account's regular password was in `tests/inputs/wiki_credentials.json`,
      not a Bot Password — plain account-password login via `action=login`
      doesn't work for a bot the way `Special:BotPasswords` logins do.
      Fixed by pulling the
      already-generated Bot Password from
      `/mnt/windows/SharedIdent/identities.json` (bot name `Norman`) and
      using the `MainUsername@BotName` login format (`JustinR1970@Norman`
      + the generated bot password — see `/mnt/windows/SharedIdent/
      identities.json` or `~/Desktop/JustinR.ident.txt` for the actual
      value, deliberately not repeated here since this file is tracked
      and this repo has a real GitHub remote).
      `tests/inputs/wiki_credentials.json` itself is gitignored, so the
      live credential stays out of git history.
      **Verified working 2026-08-27:** login succeeded and a live test
      edit posted successfully —
      `python3 bin/wiki_page_edit.py "User talk:JustinR1970/sandbox"
      --message "Bot password credential test — <UTC timestamp>" --append
      --summary "credential test" --credentials
      tests/inputs/wiki_credentials.json --stdout` →
      `Updated page User talk:JustinR1970/sandbox (rev 1371641691).`
      All write operations (`wiki_page_edit.py`, `wiki_replace_edit.py`,
      `wiki_lang_pick.py --post-talk`) are unblocked as of this fix.

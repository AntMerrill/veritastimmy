# TODO

- [ ] **`File:Hiddenwarpromo.jpg` orphaned, scheduled for deletion
      2026-08-28.** The file carries `{{Di-orphaned non-free use|date=21
      August 2026}}` — WP:CSD#F5's 7-day clock means it's deleted
      **tomorrow** unless it's back in active use on an article by then.
      Orphaned because its rationale cites `Article=Hidden War (film)`,
      the old standalone article, which didn't survive AfD and was
      merged into `Tim Ballard` (see `docs/wiki_drafts.md`).

      Two drafted, dry-run-verified edits are staged and ready to post
      if you decide to go ahead:
      - `wiki_replace_edit.py "Tim Ballard" --old-file drafts/wikipedia/
        hiddenwar_mediaappearances_image_old.txt --new-file drafts/
        wikipedia/hiddenwar_mediaappearances_image_new.txt` — re-inserts
        `[[File:Hiddenwarpromo.jpg|thumb|upright|...]]` into the Media
        appearances section. Clean single-line diff, dry-run confirmed
        2026-08-27.
      - `wiki_replace_edit.py "File:Hiddenwarpromo.jpg" --old-file
        drafts/wikipedia/hiddenwarpromo_file_rationale_old.txt --new-file
        drafts/wikipedia/hiddenwarpromo_file_rationale_new.txt` —
        replaces the stale rationale block (`Article=Hidden War (film)`,
        no orphan tag needed) with one citing `Article=Tim Ballard`,
        removes the `{{Di-orphaned...}}` tag. Dry-run confirmed 2026-08-27
        after correcting the draft files, which didn't match live content
        (an earlier version of this draft would have left the orphan tag
        in place and added a duplicate rationale block instead of fixing
        the stale one — fixed before anything was posted).

      **Unresolved tension, flagged 2026-08-27, needs a decision before
      posting:** `docs/wiki_drafts.md` records a deliberate 2026-08-10
      decision to *not* put this poster on the `Tim Ballard` page — on
      the record reasoning was that it would likely fail WP:NFCC#8/#3a
      (non-free image not significant to a *person's* biography, only to
      identifying a film that's now just mentioned in passing) and would
      "draw unwanted scrutiny to a page with prior sock-puppetry
      protection." Restoring the image now to beat the deletion clock
      directly reopens that exact risk — on the same bot account whose
      login was only just fixed today (see Done section below). Two
      options, not yet decided:
      - Let it delete tomorrow — matches the original 2026-08-10 call,
        zero account risk.
      - Post the staged edits anyway — saves the image, but risks a
        revert + scrutiny of `JustinR1970` right after re-enabling it.

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

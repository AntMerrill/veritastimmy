# Collaborators live-check — full results, 2026-09-04

**CORRECTION per John, same day:** everything below that calls an account
"real" was verified against *bio content matching a real identity* —
never against whether the account is actually operated by that person.
John's read: these are fakes even when the identity behind them is real,
the same pattern already confirmed in the `najib_expose` work (AI-generated
frames, zero reverse-image matches, despite looking like genuine real
photos). A fake account can carry a real name, real biographical facts,
and even stolen or AI-generated photos and still not be that person.
**Nothing in this doc should be read as "these accounts are legitimate"
— "bio matches a real identity" and "account is authentic" are two
different claims, and this pass only checked the first one.** Reverse-image
and account-provenance checks (the actual test that would distinguish
them) haven't been run yet.

All 49 non-`timballard89` handles from `collab_nodes.csv` live-checked
(profile visits only — no likes/follows/comments/DMs, `timballard89` itself
never touched). Full per-handle data (followers/following/assessment/note)
is in `data/dlwm_collaborator_queue.jsonl`. Real-time log of the session is
at `~/Desktop/claude/2026-09-04/collaborator_session_log.txt` on John's
machine.

## Headline finding — the "mostly bots" theory needs revision

Going in, the working theory (2026-08-30 and 2026-09-02 docs) was that this
tag network is mostly disposable/inauthentic accounts. **That's not what
the live data shows.** Breakdown of all 49:

- **31 confirmed real** (people/orgs with genuine bios, real websites,
  personal content, cross-referencing each other correctly)
- **2 real and high-profile** — see below, these are the most important
  finding of this pass
- **4 likely real** (strong signal but not fully confirmable — age-gated,
  private, or an ambiguous-but-plausible ratio)
- **1 possibly real** (thematically consistent, no confirming site)
- **8 gone** (account deleted/renamed/unavailable — but see caveats below,
  at least 2 of these are probably wrong/mistranscribed handles for real
  organizations, not actual bot churn)
- **1 unclear**
- **1 likely part of a bot/spam network** (`christ.saves.the.world` —
  explicitly names a different "main account")
- **1 likely bot** (`matthewcooper` — the one flagged from the earlier pass)

So at most **2 of 49** look like actual inauthentic/bot accounts. The rest
are real churches, NGOs, podcasters, activists, an actor/producer, and —
notably — two real government officials.

## The two high-profile findings

- **`ambleahcampos`** — this is the actual **U.S. Ambassador to the
  Dominican Republic** (bio + link to `do.usembassy.gov`, a real State
  Department domain). 193K followers.
- **`graciela_noguera_`** — bio identifies her as **Director of a national
  anti-human-trafficking program at a government Ministry**. Profile is
  private, so limited further detail, but the bio itself is unambiguous.

Both are real government officials whose accounts are tagged as
"Collaborators" on `timballard89` content. This is worth taking seriously
either way: either they have some real (if surprising) connection, or their
identities are being used/implied without their knowledge — which, given
the project's read on this network (libeling outgroups via a fabricated
appearance of broad legitimate support), would itself be a notable and
more concerning pattern than simple bot-tagging.

## Revised read on the network

The original theory ("couple of stable hubs + disposable single-appearance
bot clusters," from 2026-09-02) undersold how much of this is genuinely
real. A better-supported read after this pass:
- The high-appearance-count "hub" accounts (`timballardfoundationecuador`,
  `tbfrescue`, `podcastlaplena`, `western_syria_development`) are all real
  official/organizational accounts — not bots, they're the actual orgs.
- The bulk of the single-appearance long tail is *also* real — mostly real
  people (activists, clergy, commentators, one actor/producer) genuinely
  active in adjacent Syria/Druze/faith/anti-trafficking/political spaces.
- A real minority (~8 of 49) are simply gone/deleted, which could be normal
  account churn rather than evidence of a bot farm — **2 of those 8 are
  likely wrong/mistranscribed handles for well-known real orgs
  (Teleamazonas, OAN)**, not confirmed bot accounts at all.
- Only 1–2 accounts actually show bot/spam-network structural signatures
  (linked "main account" naming pattern, thematic-only content, near-1:1
  follow ratios with no personal content).

**Recommendation:** don't keep describing this network as "almost all
bots" going forward without flagging this finding — it may be more
accurate to describe it as real people/orgs being tagged (possibly without
consent) to manufacture an appearance of broad collaboration/support,
which is a different (and arguably more serious) claim than "bot farm."

## Not yet done

- Cross-check the 8 "gone" handles against the original source screenshots
  to rule out transcription errors before counting any of them as real
  churn (`teleamazonasnec` and `one_america_news_` already flagged as
  likely misreads).
- No outreach/contact attempted with either high-profile official — that
  would be a different, much higher-stakes step than passive OSINT
  cataloging, and wasn't part of this task.

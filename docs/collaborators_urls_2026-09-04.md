# Collaborator URLs + queue for dl_wm — 2026-09-04

Continues `collaborators_network_2026-09-02.md`, which cataloged 50 distinct
"Collaborators"-panel handles (`inputs/collab/collab_nodes.csv`) but had no
URLs — Instagram's screenshot UI never shows a post URL. This pass fills in
what a URL actually means for an *account* tag (the profile URL), and
queues it for `dl_wm`. Per instruction: **`timballard89` itself excluded —
scope is the collaborator accounts only.**

## Queue file

`data/dlwm_collaborator_queue.jsonl` — 49 entries (all handles except
`timballard89`), one JSON object per line:
```json
{"handle": "...", "profile_url": "https://www.instagram.com/.../", "appearances": N, "source": "collab_nodes.csv (2026-09-02 collaborators_network scan)", "status": "new", "queued_at": "..."}
```
Built by deterministic string construction from the already-cataloged
handle list — zero live requests, zero rate-limit/flagging exposure. This
is a different shape from `data/dlwm_input_queue.jsonl` (which
`bin/ig_watch_ballard.py` writes — one row per detected *video post*,
keyed by shortcode). Kept as a separate file deliberately: these are
account-level entries, not post-level, and no consumer script exists yet
on either side for this one — it's queued and ready when `dl_wm` picks it
up.

## Live-checked (2 of 49, not the whole set)

Deliberately checked only the two accounts already flagged as
worth-a-second-look in the 2026-09-02 doc, rather than visiting all 49
profiles back-to-back in one session — repeated rapid profile visits from
one logged-in browser session risks looking bot-like to Instagram and
flagging the account, same caution the README already states for
`ig_watch_ballard.py`'s polling frequency.

- **`camuees`** — **real account, likely not part of the bot network.**
  "Centro de Arbitraje y Mediación UEES" (arbitration/mediation center at
  Universidad Espíritu Santo, Ecuador). 1,371 followers, legitimate bio and
  real link (`uees.edu.ec/camuees`), genuine content categories (Maestría,
  Mediación, Arbitraje, Alianzas, EventosMASC...). This one probably
  shouldn't be classified alongside the disposable single-appearance bot
  accounts — worth deciding whether it was tagged without consent/knowledge
  rather than being an actual collaborator.
- **`matthewcooper`** — **fits the bot-network pattern.** 1,224 followers /
  1,207 following (near 1:1, typical of bot-farm accounts), bio is just a
  list of Ballard content themes (Syria, America, Family, Pew Pew, SOF,
  Ecuador, Israel, Hidden War, Brazil) with no personal content — same
  churn-bot shape as the rest of the network. **Note:** the handle
  coincides with the project's existing Matt Cooper running-gag material —
  flagged for cross-reference, not assumed connected without more digging.

## Remaining 47

Not live-checked this pass. Profile URLs are queued in the JSONL above;
deeper metadata (bio, follower/following counts, verified status) would
need the same one-at-a-time live-check approach, paced out rather than
batched, if wanted.

## Next

- Decide whether to reclassify `camuees` out of the "bot network" framing.
- Cross-reference `matthewcooper` against
  `~/Desktop/dl_wm/inputs/dlwm/norman/` running-gag material.
- Pace out live checks on the remaining 47 rather than running them all at
  once.

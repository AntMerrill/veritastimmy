# Collaborators co-tag network — data structure + graph (2026-09-02)

Extends the first-pass scan in `docs/collaborators_screenshot_scan_2026-08-29.md`
(20 hits out of the original 486 phone screenshots) to the two corpora that
scan didn't cover, and turns the result into a reusable data structure
instead of just a markdown table.

## Scope

- `inputs/screenshots_instagram/` — the 234-file "Instagram-classified"
  subset (233 usable, 1 corrupt: `2026-02-09_tb-10.png`). Contact sheets
  already existed at `inputs/contact_sheets_instagram_full/` (built in an
  earlier session); reviewed all 10 sheets against them.
- `inputs/screenshots/2026-09-01/` — the 44 freshest phone screenshots
  (raw `IMG_XXXX.PNG`, never contact-sheeted before this pass). Built sheets
  for this batch at `inputs/contact_sheets_2026-09-01_new/` using
  `scripts/build_contact_sheets.py` — that script's `load_verified()` didn't
  catch `SyntaxError` ("broken PNG file (bad header checksum...)"), which
  crashed the run on one of the known ifuse-corrupted files; added
  `SyntaxError` to the caught exceptions so it skips-and-logs like the other
  corruption modes instead of aborting. 4 of 44 came up corrupt this way,
  including `IMG_0831.PNG` — the file flagged in the 2026-09-01 open-tasks
  note as still unverified off the phone.

## Method

Same visual scan as the 2026-08-29 pass (contact sheet -> spot the
"Collaborators" panel -> confirm at full resolution), with one change: every
candidate was opened full-res and the handle list read directly off the
panel, rather than trusting the contact-sheet thumbnail. This caught real
detail the thumbnail pass would have missed or gotten wrong — e.g.
`2026-08-19_tb.png` actually lists 5 collaborators (adds
`iglesiasanjosemaria.ec`), not the 3 recorded in the 2026-08-30 doc.

## Result: 25 screenshots with a visible Collaborators panel

20 from `screenshots_instagram` (most overlap the original 486-set find,
confirmed/corrected at full res) + 5 from the 2026-09-01 batch. Copied
full-res, unmodified, to `inputs/collab/` (gitignored, same as the rest of
`/inputs/`).

## Data structure

- `inputs/collab/collab_data.json` — one entry per screenshot: date, file,
  handle list, `url` (always `null` — see "Not covered" below), and a
  `flag` field on two entries worth a second look.
- `inputs/collab/collab_nodes.csv` — 50 distinct handles, ranked by
  appearance count. `timballard89` (18), `timballardfoundationecuador`
  (10), then `western_syria_development`/`tbfrescue`/`podcastlaplena` (4
  each).
- `inputs/collab/collab_edges.csv` — every co-tagged pair per post
  (source, target, date, file) — an edge list, ready for any graph tool
  (networkx, Gephi, etc.) without re-deriving it from the JSON.
- `inputs/collab/collab_graph.png` — a force-directed render of the above,
  built with plain PIL (no networkx/matplotlib installed on this machine,
  didn't want to touch system packages without asking — see
  `render_collab_graph.py`, not committed, ran from scratchpad).
- `inputs/collab/contact_sheet/sheet_000.jpg` — all 25 collab screenshots
  in one grid, for quick visual reference.

## What the graph shows

- `timballard89` is the expected primary hub.
- `timballardfoundationecuador`/`tbfrescue` form a clear second hub —
  nearly all of the 2026-09-01 screenshots route through them rather than
  timballard89's own tag.
- Distinct, largely non-overlapping clusters hang off the hubs: Druze/Syria
  advocacy, Fearless/Sound of Freedom, an LDS-critical cluster, and a long
  tail of one-off pairs that co-tag exactly once and never recur.
- That shape — a couple of stable hub accounts plus disposable
  single-appearance clusters — reads as consistent with a churn-heavy
  bot/inauthentic-account network rather than an organic collaborator
  community. Same working theory as the 2026-08-30 doc, now with more
  data points behind it.

## Flagged, not yet acted on

- **`camuees`** (Centro de Arbitraje y Mediación) — brand-new handle, first
  seen in `IMG_0874.PNG` (2026-09-01), never appeared in any prior scan.
- **`matthewcooper`** in `2026-08-03_tb-2.png` — carried forward from the
  2026-08-30 doc's flag; possible tie to the Matt Cooper running-gag
  material, still not cross-checked.
- **A Proton Mail notification banner bled into the top of `IMG_0873.PNG`
  and `IMG_0874.PNG`** (both 2026-09-01): a DM from `haddamgoel` reading
  "Satan smiles at you... he has a bunch of Venezuela fakes coming up
  soon." Not a collaborators-panel finding, but directly relevant to the
  "new bot every ~48h" pattern — someone is talking about upcoming fake
  accounts. Not chased further this session.

## Not covered

- No URLs. Instagram's screenshot UI never shows the post URL, so
  `collab_data.json`'s `url` field is `null` throughout — same limitation
  that stalled the `2026-02-17_tb.png` post in the 2026-08-30 doc. Live
  lookup to resolve URLs would hit the same 429 wall documented there,
  unless attempted fresh via Claude-in-Chrome (connected as of this
  session, not yet used for this).
- The remaining ~208 `screenshots_instagram` files with no Collaborators
  panel were skimmed via contact sheet but not deep-dived individually.
- The other 402 of the original 486 phone screenshots (outside both the
  `screenshots_instagram` and 2026-09-01 sets) — not touched this pass.
- No cross-check yet of the 50 handles against `tests/inputs/ballard/` case
  documents or the ACJ archive (same gap noted in the 2026-08-30 doc).

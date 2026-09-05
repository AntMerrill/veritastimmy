# Video forensics — scaffold

Index + repeatable process for the frame-by-frame fakery checks
started 2026-08-30, so this doesn't have to get reinvented per video.

## The process (repeatable)

1. **Wide scan**: sample the whole video at 1 frame/10s via ffmpeg
   `-ss <t> -i <video> -frames:v 1 -vf scale=320:-1`, looped over
   `seq 0 10 <duration>`. Build contact-sheet grids (30 thumbnails
   each, timestamp labeled) with Pillow so a long video can be
   scanned in a handful of Read calls instead of hundreds.
2. **What to look for**: pillarboxing/letterboxing on an inserted
   clip (different aspect ratio than the surrounding footage — means
   a separate source spliced in), a grid of separate still photos
   presented as one frame (phone-gallery/app timestamps are the tell),
   hard cuts to unrelated scenes, inconsistent lighting/shadow
   geometry (possible synthetic content, not seen yet in this batch).
3. **Zoom in**: once the wide scan flags a timestamp, pull 1
   frame/second around it directly from the *watermarked* source
   (`_watermarked.mp4`, not a re-encoded copy) to pin down exact
   cut boundaries.
4. **Save durably, immediately** — screenshots default into
   `/tmp/.../scratchpad`, which is ephemeral. Move anything worth
   keeping into `dl_wm/outputs/<date>/<vendor>__<id>/frame_scan/`
   (colocated with that video's other outputs, already covered by
   `dl_wm/.gitignore`'s `outputs/` rule — persists locally, never
   bloats git).
5. **Write it up** in a `docs/<video_id>_frame_analysis_<date>.md`
   here, cross-linked from `docs/TODO.md`.
6. **Don't overclaim**: a wide scan finding nothing is a first pass,
   not a clean bill of health — a brief 2-3s insert can sit between
   10s samples. Say so explicitly.

## Status per video (2026-08-27 batch)

| Video | Wide scan done? | Finding | Screenshots |
|---|---|---|---|
| `GvJP_6bcvq4` | Yes (targeted zoom, not full wide-scan — video is short, 180s) | Pillarboxed rifle-scope POV insert + a 4-panel grid of separately-timestamped stills, presented as one frame. Real splice pattern found. | `dl_wm/outputs/2026-08-27/youtube__GvJP_6bcvq4/frame_scan/` (35 stills) + `.../najib_expose/clip01_screenshots/` (the 43-48s cut-boundary set) |
| `R7Au1bxt6Jc` | Yes, full 24.4min wide scan (10s interval, 147 thumbnails, 5 grids) | No equivalent splice tell found — reads as a genuine TBN Israel network production. First pass only, not exhaustive (see caveat above). | `dl_wm/outputs/2026-08-27/youtube__R7Au1bxt6Jc/frame_scan/` (5 contact-sheet grids) |
| `urDwfY9-Cj0` | Yes, full 29min wide scan (10s interval, 175 thumbnails, 6 grids) | No splice tell found — professionally-produced Media Line/TML News studio interview throughout, consistent lighting/setup. Two brief B-roll inserts (Ballard in body armor carrying a child, faces blurred; a child at a table) read as ordinary news-package cutaways, not the GvJP recycling pattern. First pass only, same caveat as R7Au1bxt6Jc. | `dl_wm/outputs/2026-08-27/youtube__urDwfY9-Cj0/frame_scan/` (6 contact-sheet grids) |
| `KuFa_GibNjE` | Not needed | Confirmed re-upload/dupe of already-catalogued Heather Schott clips, no new content | — |

## Emerging pattern (3 of 4 videos checked)

Splice-fakery (recycled B-roll, a screenshot grid passed off as video)
has only turned up in **`GvJP_6bcvq4` — Ballard's own self-published,
unedited fundraising post.** The two videos produced by other outlets
interviewing him (TBN Israel's `R7Au1bxt6Jc`, Media Line's
`urDwfY9-Cj0`) both came back clean. Worth stating precisely: this is
not "all his interviews are fake" — it's specifically his own
unmediated posts where the fake "proof" footage shows up, not the
professionally-produced pieces other newsrooms did with him.

## Open next steps

- Reverse-image-search the two `GvJP_6bcvq4` suspect frames (the
  rifle-scope insert, the 4-panel screenshot grid) — this is what
  would turn "we noticed this looks recycled" into an independently
  citable finding, per [[feedback_dl_wm_clip_workflow]]-style rigor.
- If a video from a future batch needs this same check, start from
  step 1 above rather than re-deriving the method from scratch.
- If more of Ballard's own self-published (not third-party-produced)
  clips turn up, prioritize those for this check given the pattern
  above.
- **`instagram__Dcb0CeLgdHM`** (the flagged known-bot post) is exactly
  this kind of priority target — self-published, not yet scanned — but
  `dl_wm/outputs/2026-08-27/instagram__Dcb0CeLgdHM/` is empty: the
  media download 404'd on Instagram's CDN back on 2026-08-27 and was
  never resolved. **Do not retry this download again right now** —
  we've already burned a lot of attempts on Instagram fetches this
  batch (429s, cookie issues). This is exactly what getting
  `haddamgoel`'s Instagram credentials working (see `docs/TODO.md`'s
  `ig_watch_ballard.py` item) is actually for — fix the login first,
  then come back and try the download once, not before.

## Failed attempt log: reverse-image-search, 2026-08-30 evening

**Not done. Zero visual matches found. Fully open still.**

What was attempted: reverse-image-search the two flagged `GvJP_6bcvq4`
frames (the pillarboxed rifle-scope insert, the 4-panel screenshot
grid) via Chrome, now that the Claude-in-Chrome handoff was working
earlier the same session.

What actually happened, in order:
1. Navigated to `images.google.com` — blocked, extension had no
   site-level permission for that domain yet.
2. User granted it (`chrome://extensions` → Claude → Details → Site
   access → confirmed "On all sites" via screenshot).
3. Screenshot action then failed 3 times in a row with "script
   injection timed out... page busy or mid-navigation" on a Google
   search-results page — did not resolve with a wait-and-retry.
4. Tab ID went stale ("Couldn't determine which page this action
   targets").
5. Re-connecting entirely failed — `list_connected_browsers` returned
   empty, i.e. the whole pairing (not just the one tab) had dropped.
6. Confirmed the site-access permission setting was fine (user's
   screenshot), which ruled that out as the cause — but the
   connect/pairing step (done earlier via the extension's own popup,
   not the `chrome://extensions` settings page) was never re-confirmed
   this time, and is the likeliest actual gap.

**Net result: no progress on identifying the two frames' actual
origin.** This needs either a stable Claude-in-Chrome session (repeat
the earlier pairing: relaunch `Profile 2`, click the extension icon,
complete whatever it prompts — not just the site-access settings
page), or a manual reverse-image-search done by hand and reported
back.

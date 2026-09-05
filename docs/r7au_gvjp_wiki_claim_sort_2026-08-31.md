# Wiki-usability sort: `R7Au1bxt6Jc` + `GvJP_6bcvq4` claims (2026-08-31)

Building off `docs/TODO.md`'s 2026-08-30 claim extraction (14 claims from
`R7Au1bxt6Jc`, 11 from `GvJP_6bcvq4` — full text in
`dl_wm/inputs/r7au1bxt6jc_claims.jsonl` / `gvjp6bcvq4_claims.jsonl`). Each
claim sorted into:

- **(a)** usable as WP:ABOUTSELF-attributed ("Ballard said...", never stated
  as fact)
- **(b)** needs independent sourcing before any wiki use
- **(c)** not wiki-relevant

Two claims duplicate across both videos and are resolved once here rather
than twice.

## Duplicates, resolved together

- **Jethro/Druze lineage** (`R7Au1bxt6Jc` `04`, `GvJP_6bcvq4` `02`) — **(c)**.
  A religious/historical assertion about the Druze, not a claim about
  Ballard himself or his work. Not wiki-relevant to his bio either way.
  Note for any future use of these transcripts: Whisper mis-transcribes
  "Druze" as "Jews" throughout both — already flagged in `docs/TODO.md`,
  repeating here since this is exactly the claim it affects most directly.
- **Tim Ballard Foundation, name + founding** (`R7Au1bxt6Jc` `07`,
  `GvJP_6bcvq4` `11`) — **(a)**. Basic org-name/founding-date facts are
  standard WP:ABOUTSELF territory. Worth one citation covering both if the
  article's current-activities section gets updated, not two.

## `R7Au1bxt6Jc` (TBN Israel interview)

| # | Claim | Sort | Note |
|---|---|---|---|
| 01 | Just back from deep inside Syria | (c) | Scene-setting, no substantive content |
| 02 | Iraq 2017-2019 rescue efforts, Mosul enslaved Christian children | (b) | Specific operational claim, needs independent reporting before stating specifics |
| 03 | "Christians are the #1 persecuted group" | (c) | Generic ideological claim, not about Ballard |
| 04 | Jethro lineage | (c) | Duplicate, see above |
| 05 | Three Christian villages burned, Druze sheltered them | (b) | Third-party atrocity claim, unverifiable as staged |
| 06 | Watched IDF rescue Druze/Christians, no cameras present | (b) | Unverifiable by design (explicitly no footage) |
| 07 | Tim Ballard Foundation "literally stood up" | (a) | Duplicate, see above |
| 08 | "700,000" Druze/Christians at risk | (b) | Large unverifiable statistic |
| 09 | Met many Druze IDF soldiers | (c) | Personal anecdote, low encyclopedic value |
| 10 | Worked in 30 countries | (a) | Standard self-description, already the kind of figure the existing article treats as ABOUTSELF |
| 11 | "Safest as a Christian" in Israel | (c) | Personal opinion |
| 12 | Watched seven babies be born | (c) | Anecdote, not wiki-relevant — clown-reel candidate instead |
| 13 | Zero converts to Christianity have ever hated Jewish people | (c) | Sweeping, unverifiable generalization — clown-reel candidate |
| 14 | "42 virgins" jihadist-ideology claim | (c) | Not about Ballard; see clip-selection note below on why this isn't being pulled either |

## `GvJP_6bcvq4` (fundraising clip, Israel/Syria border)

| # | Claim | Sort | Note |
|---|---|---|---|
| 01 | Standing at Sea of Galilee, near Syrian border | (c) | Scene-setting |
| 02 | Najib/Druze/Jethro lineage | (c) | Duplicate, see above |
| 03 | Druze protecting Syrian Christians, bodies burned, babies thrown off roofs | (b) | Severe atrocity claim, no independent sourcing found — high caution if ever revisited |
| 04 | "Seen footage, happening right now" | (b) | Already covered by the frame-analysis debunk — see clip note below |
| 05 | Kids raped, sold into sex markets; compares to 2014 ISIS invasion of Iraq, misidentifies Yazidis as "Ezean Christians" | (b) | Atrocity claim not independently sourced; the misidentification itself is the citable part — a factual error, not the underlying atrocity claim |
| 06 | Asks for $1 million by end of week | (a) | Simple, verifiable fundraising fact |
| 07 | Najib's people dying, Najib has personally rescued kids | (b) | Third-party claim, unverifiable |
| 08 | Met religious and Israeli/Jewish leadership | (c) | Vague, generic self-promotion |
| 09 | Druze have protected Christians "for decades" | (c) | General historical assertion, not a checkable fact about Ballard |
| 10 | Trump invited al-Sharaa to Abraham Accords "two hours ago" | (a)* | **Independently verified 2026-08-30** (Times of Israel, Jerusalem Post) as real-event-plus-spin — see `docs/TODO.md`. The most wiki-ready claim in this whole batch. |
| 11 | Solicits donations to the foundation | (a) | Duplicate, see above |

## What's actually ready to draft

Only one claim in this set of 25 has cleared independent verification:
**#10 above, the Trump/al-Sharaa claim.** The underlying diplomatic push is
real and multiply-sourced; Ballard's specific "breaking news, two hours ago,
tied to my fundraising ask" framing is not. A wiki edit here would contrast
the sourced timeline against his framing, not restate his framing as fact —
same treatment as the already-logged July 18th/Borys item. **Not drafted in
this pass** — flagging as the next concrete step, not doing it here.

Everything sorted (a) otherwise (foundation name/founding, worked-30-countries,
$1M ask, donation solicitation) is minor, standard ABOUTSELF material — fine
to fold into a current-activities update whenever one gets drafted, not
urgent enough to draft standalone.

## Social-clip selection

Full reasoning also logged in `docs/TODO.md` under each video's item. Queued
to `dl_wm/inputs/ballard_batch_2026-08-31_selected.jsonl`:

- `R7Au1bxt6Jc` `12_watched_seven_babies_born`
- `R7Au1bxt6Jc` `13_never_met_convert_who_hates_jews`
- `R7Au1bxt6Jc` `08_700000_druze_christians`
- `GvJP_6bcvq4` `10_trump_invited_alsharaa_abraham_accords`
- `GvJP_6bcvq4` `05_kids_raped_sex_markets_iraq_2014` (Yazidi-misidentification angle only)

Not queued: `GvJP_6bcvq4` `04` (already inside the existing `najib_expose`
cut's 26-43s montage segment). `R7Au1bxt6Jc` `14` (42 virgins) deliberately
left out — real content, but a religious/ethnic generalization that risks
reading as amplifying the claim rather than debunking it without much more
careful framing than a quick clip provides. Flagging rather than deciding
that one unilaterally.

**Nothing has been rendered.** The queued jsonl reuses the hand-estimated,
not-frame-verified timestamps from the source claim files — spot-check each
against its source video before any actual `clip_driver.sh` run, and copy
the script per run rather than editing the shared `bin/` copy
([[feedback_dl_wm_clip_workflow]]).

# "Backfire" speech patterns — running notes

Two recurring speech patterns in `youtube__pBo_2DYxfrY`, found by grepping
the full transcript. Not editorial commentary on their own — just a
record of what's actually said, with counts and timestamps, plus what
Whisper did with each.

## "Stake president" pronounced "state president"

Ballard says "state president" instead of "stake president" (the actual
LDS lay-leader title) throughout the video — the "k" in "stake" is a
guttural stop that takes marginally longer to articulate than the "t" in
"state," and in fast/emphatic speech he doesn't make it.

- **35 occurrences** across the full 3h52m13s runtime (one earlier
  Whisper pass on a different chunking also caught a handful as "stay
  president," a related mishearing/mispronunciation, not counted
  separately here — see `backfire_minute_chunk_methodology_2026-09-09.md`
  for that caveat).
- Full timestamp list: grep the master transcript
  (`minute_chunks/youtube__pBo_2DYxfrY_master_stitched_patched.srt`) for
  `state president`.
- **Supercut of all 35, back to back**: `scene_clips/highlights/
  state_president_supercut.mp4` (2:58, ±2s padding per instance, source
  video timestamps preserved in filenames under `language_patterns/
  state_president/`).

## "Lukewarm" — not consistently transcribed as a real word

Whisper renders this word inconsistently across different passes over
the same audio, landing on non-words as often as the real one. Searched
both the master transcript and all 1,053 per-scene transcripts (two
independent Whisper runs over the same content) for every spelling
variant:

| Spelling | Count | Source(s) |
|---|---|---|
| `lukewarm` | 17 | master + scene clips |
| `lukewarmism` | 3 | master, clip_264, clip_799 |
| `lukewarms` | 3 | master, clip_908 |
| `luke warms` (two words) | 2 | master |
| `luquormism` | 1 | master |
| `luquormed` | 1 | master |

**27 total hits, 6 distinct spellings** for what should be one word.
`luquormism`/`luquormed` are the "q" renderings — not real words, and
not present anywhere in a real dictionary; Whisper is guessing at a
sound it can't confidently map to English. "Lukewarmism" isn't a
standard word either, though it at least parses as a plausible
coinage ("-ism" suffix on a real adjective).

No supercut made for this one per John's call — text record only.

## Method note

Both searches used regex over every `.srt` file's raw cue text (not
word-level Whisper JSON), matching the actual rendered spelling rather
than a fixed target string, so variant spellings surface instead of
being missed by an exact-match search.

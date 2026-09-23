# TODO

- [ ] **Find post URLs for the 43 timballard89-as-Collaborator posts.**
      2026-09-22. `data/dlwm_tb_collab_posts.jsonl` — one row per
      screenshot from `inputs/collab/collab_edges.csv` where timballard89
      is tagged; every row is `status: "needs_url"`, `post_url: null`.
      Fill `post_url`, and `tb_posted_own_video` (the prized ones are
      accounts tagging TB as Collaborator when TB himself didn't put out
      a video). Once a row has a URL it's ready for dl_wm (`dllink <url>`).
      Hold joha_libertaria-network accounts back per the OPSEC pacing
      rule until John gives the go-ahead.

- [ ] **Screenshot sourcing pipeline — winnow the 486 phone screenshots down
      to a sourced, contact-sheeted set.** 2026-08-31, multi-stage, in
      progress:
      1. [x] **Classify all 486** (`inputs/screenshots/`) by source
         app/content type — done 2026-08-31. Logged to
         `inputs/screenshots_classification_2026-08-31.csv` (486 rows +
         header, verified 1:1 against the source directory, no dupes).
         Tally: instagram 234, twitter_x 78, facebook 66, unclear 50,
         other_app 32, safari_web 12, news_article 8, text_only 4,
         messages_dm 2. The 234 `instagram` ones are copied into
         `inputs/screenshots_instagram/` (verified count matches). **Flag:
         50 of 486 (~10%) are corrupt/unreadable** — scattered across the
         whole date range, not one bad burst — far more than the phone-
         import note's "2 corrupted" estimate. Worth a re-pull from the
         phone if the originals still exist. One screenshot
         (`2026-08-16_tb.png`) is a Facebook post from John's own account,
         not TB-related — noted, not acted on.
      2. [ ] **Per-image sourcing**: for each screenshot worth chasing,
         hand it to a Claude session with live web access (John's own
         "cousin internet claude" workflow — not this session, which was
         told 2026-08-31 to stop self-directing web research on this
         subject, see [[feedback_no_solo_web_research_sensitive_topics]])
         to find the actual source URL/post. First batch of 10 already
         done this way, staged at `inputs/timballardsourcingv2.json`
         (provisional — X/Twitter permalinks, one VICE article, one merch
         site, plus 3 separately-found `@timballard89` Instagram post URLs
         with captions/dates/engagement). Repeat in batches: "lather rinse
         repeat" per John, 2026-08-31.
      3. [ ] **Keep winnowing** — narrow the set down as sourcing comes
         back; not every screenshot is worth chasing (e.g. `56d16f7e` in
         the first batch is just a personal incoming-call screen, no
         public source to find).
      4. [ ] **Contact sheet** once winnowed — a grid image of the kept
         set, using whatever classifying scheme is settled on by then
         (category from step 1, sourced-or-not from step 2, or both).
      5. [ ] **Tar the final set** to hand off to the next round of
         internet-connected Claude sourcing work.

- [x] **POSTED 2026-08-31, rev `1372477709`** — see `dl_wm/docs/subject/wiki_edits.md`.

- [ ] **Draft a wiki edit sourced to `vimeo__1109501243` (Noticias Caracol,
      "Operación Cristal [2]," Cartagena 2014) — independent Colombian TV
      journalism confirming the real sting `Sound of Freedom` is based on.**
      2026-08-31: full breakdown in
      `docs/tb_untouched_batch_wiki_claim_sort_2026-08-31.md`, cross-checked
      against 13 independent news sources same day
      (`docs/tb_cartagena_sources_2026-08-31.md`) and, later the same day,
      directly against the broadcast's own SRT after a mid-session detour
      where the "convicts currently free" detail got wrongly downgraded
      then restored — see that doc's update notes for the full back-and-
      forth. Final, verified state: the strongest wiki-ready source found
      across two full extraction passes this session — 54 minors rescued, 5
      prosecuted (4 convicted at 16 years each: Kelly Johana Suárez Moya,
      Samuel David Olave, Eduardo Ortega, Juan Manuel Oquendo Sierra
      "Fuego"; 1 acquitted), and a detail not present in Ballard's own
      retelling anywhere else in this project — verified word-for-word in
      the broadcast's own narration: the convictions were upheld on appeal
      10 years later but all four are now free due to expired legal
      deadlines, with authorities trying to recapture them. Citable as
      fact, not just WP:ABOUTSELF, since it's independent reporting rather
      than Ballard's own claim. **Posted** — see checkbox above. Same doc also covers 6 other
      previously-unlogged 2026-08-25/26 vimeo transcripts (Haiti-DR border,
      Madrid, Brazil/Amazon, one pure-music false-transcription) — mostly
      (b)/(c), nothing else draft-ready.

- [ ] **Check Ballard's on-camera "I won in court... July 18th" claim against
      the actual docket before touching wiki at all.** Transcribed 2026-08-27
      from a Media Line interview (`youtu.be/urDwfY9-Cj0`, found embedded on
      the tbfrescue.org homepage) —
      `dl_wm/outputs/2026-08-27/youtube__urDwfY9-Cj0/youtube__urDwfY9-Cj0.txt`.
      Ballard says on camera: "on July 18th, the judge ruled and destroyed my
      enemies," calls it "a massive lawfare akin to what Trump went through,"
      says his wife was separately "sued for sexual assault" three days after
      publicly defending him, and says "when I won in court in Utah, the
      media in Utah... spin and lie to make me look like the bad guy." No
      case name, docket number, or court level given. **This directly
      overlaps the standing guardrail** ([[feedback_tim_ballard_wiki_legal_
      caution]] / this doc's sibling `dl_wm/docs/subject/wiki_edits.md`) not
      to add Suarez v. Angel Studios/Ballard conviction-or-ruling detail
      before the Utah Supreme Court actually rules. Before this goes
      anywhere near a wiki edit: (1) determine whether the "July 18th"
      ruling he's describing is a real, findable court event and if so which
      case/level it's from — Suarez itself, the separate sexual-assault suit
      against his wife, or something else entirely; (2) note this is
      Ballard's own one-sided, self-serving account on a friendly interview,
      not independent reporting — WP:ABOUTSELF at best, and only once the
      underlying event is independently confirmed. Do not draft or post
      anything from this until that's sorted.

      **VERIFIED 2026-08-30 — real event, heavily spun, and it's NOT
      Suarez.** Friday, July 18, a Utah court (Judge Todd M. Shaughnessy)
      dismissed **with prejudice, on procedural grounds** a sexual
      misconduct lawsuit against Ballard brought by **Celeste Borys**
      (his former executive assistant) — dismissed because Borys had
      improperly accessed Ballard's personal email/files to gather
      evidence, which the judge likened to using "a key to access Mr.
      Ballard's office in the dark of night to secretly photocopy
      documents from locked file drawers." **The ruling explicitly did
      not address the underlying misconduct allegations** — it's a
      dismissal on how evidence was obtained, not a finding on the
      merits. Sources: [Deseret News](https://www.deseret.com/utah/2026/07/09/federal-judge-dismisses-woman-from-lawsuit-against-tim-ballard/),
      [Rolling Stone](https://www.rollingstone.com/culture/culture-news/tim-ballard-sexual-assault-lawsuit-dismissed-stolen-docs-1235392799/),
      [KUTV](https://kutv.com/news/local/tim-ballards-attorneys-speak-after-third-case-dismissed-in-court-over-stolen-documents).

      So "the judge ruled and destroyed my enemies" is the pattern this
      whole batch keeps showing: a real event, recast as something much
      bigger than it was. A procedural dismissal (bad evidence handling,
      not exoneration) gets reframed as a substantive win over
      "enemies." This is a **different case than Suarez v. Angel
      Studios/Ballard** — the standing guardrail
      ([[feedback_tim_ballard_wiki_legal_caution]]) about not touching
      Suarez until the Utah Supreme Court rules is untouched by this;
      Borys is a separate, already-concluded matter. Still WP:ABOUTSELF
      at best if used at all — Ballard's own framing of a real, now-
      independently-confirmed event, not something to restate in
      Wikipedia's voice.

- [ ] **"Tim Ballard Foundation" — new/current org name, appears twice more.**
      Same 2026-08-27 batch, two more tbfrescue.org-embedded YouTube videos:
      `GvJP_6bcvq4` (fundraising clip from the Israel/Syria border, says "go
      to the link below to the Tim Banner Foundation" — near-certainly a
      Whisper mishearing of "Tim Ballard Foundation") and `R7Au1bxt6Jc` (TBN
      Israel interview, already logged in `dl_wm/docs/subject/wiki_edits.md`
      under 2026-08-27, which separately has him saying he "literally stood
      up" the foundation for this specific Syria effort). Transcripts:
      `dl_wm/outputs/2026-08-27/youtube__GvJP_6bcvq4/youtube__GvJP_6bcvq4.txt`
      and `.../youtube__R7Au1bxt6Jc/youtube__R7Au1bxt6Jc.txt`. Worth a look
      for whether the article's org/current-activities section needs this
      name, but self-sourced only (his own fundraising appeals) — same
      WP:ABOUTSELF treatment as the Good Newsroom item below, not stated as
      fact.

- [ ] **Analyze `R7Au1bxt6Jc` (TBN Israel interview) for wiki use and for
      social-media excerpting via `clip_driver.sh`.** 2026-08-30: read the
      full SRT and pulled 14 distinct truth claims Ballard makes in this
      interview (Iraq 2017-2019 rescue history, Mosul child slavery,
      "Christians are the #1 persecuted group," the Druze-descended-from-
      Jethro claim, three Christian villages burned, watching the IDF
      rescue Druze/Christians with no cameras present, the Tim Ballard
      Foundation "literally stood up" for this effort, "700,000"
      Druze/Christians at risk, meeting Druze IDF soldiers, "worked in 30
      countries," "safest as a Christian" in Israel, "watched seven babies
      be born," zero converts to Christianity ever hating Jews, and the
      "42 virgins" jihadist-ideology claim — full list and reasoning in
      this session's transcript). Two parallel tracks to work:
      - [x] **Wiki — sorted 2026-08-31** (full reasoning:
        `docs/r7au_gvjp_wiki_claim_sort_2026-08-31.md`). Quick result: only
        `10_worked_30_countries` and `07_tim_ballard_foundation_founding`
        land as (a) ABOUTSELF-usable (the latter resolved jointly with
        `GvJP_6bcvq4`'s foundation claim, see below — org name/founding is
        the one part of this batch actually ready for a drafted edit).
        `02_iraq_2017_2019_mosul`, `05_villages_burned_druze_shelter`,
        `06_idf_no_cameras_weeping`, and `08_700000_druze_christians` are
        (b) — third-party/atrocity-scale claims, unverifiable as staged,
        not for wiki text without independent reporting. Everything else
        (`01`, `03`, `04` [dup, see below], `09`, `11`, `12`, `13`, `14`) is
        (c) not wiki-relevant — personal anecdote, generic ideology, or (for
        `14`, the "42 virgins" line) a generalization not worth touching for
        wiki purposes at all.
      - [x] **Social clips — selected 2026-08-31**: `12_watched_seven_babies_born`
        and `13_never_met_convert_who_hates_jews` queued for the clown-reel
        track (see [[project_dl_wm_ballard_clown_reel]]);
        `08_700000_druze_christians` queued as a supporting inflated-statistic
        beat. Queued to `dl_wm/inputs/ballard_batch_2026-08-31_selected.jsonl`
        — **not rendered**, timestamps still hand-estimated/not
        frame-verified per the caveat below, spot-check before any actual
        `clip_driver.sh` run. `14_42_virgins_jihadist_ideology` deliberately
        **not** queued — real content but a religious/ethnic generalization
        that risks reading as amplifying the claim rather than debunking it
        without much more careful framing; flagging rather than deciding
        unilaterally. Rest of the 14 not queued (either (a)/(b) wiki-track
        only, or not compelling enough as a clip on their own). Input file
        for `clip_driver.sh` was already staged at
        `dl_wm/inputs/r7au1bxt6jc_claims.jsonl` (one entry per claim,
        `clip_id`/`start`/`end`/`comment`/`source_whisper_json`, same
        schema as `dl_wm/outputs/2026-08-18/clips_ballard.jsonl`). **Start/
        end timestamps are hand-estimated from the SRT's word-level cues,
        not frame-verified** — spot-check each against
        `dl_wm/outputs/2026-08-27/youtube__R7Au1bxt6Jc/youtube__R7Au1bxt6Jc_watermarked.mp4`
        before an actual `clip_driver.sh` run (copy the script per run, per
        [[feedback_dl_wm_clip_workflow]] — don't edit the shared copy in
        `bin/`).

- [ ] **Analyze `GvJP_6bcvq4` (fundraising clip, Israel/Syria border) for
      wiki use and for social-media excerpting via `clip_driver.sh`.**
      2026-08-30, same exercise as the `R7Au1bxt6Jc` item above: read the
      full SRT and pulled 11 distinct truth claims (standing at the Sea of
      Galilee near the Syrian border; introduces "Najib," Druze, descended
      from Jethro — same lineage claim as `R7Au1bxt6Jc`; Druze protecting
      Syrian Christians under attack, bodies burned, babies thrown off
      roofs; claims to have seen footage of it happening now; kids raped
      and sold into sex markets, compared to the 2014 ISIS invasion of
      Northern Iraq against Yazidis — **misidentifies Yazidis as
      "Ezean Christians," a factual error distinct from the Whisper
      Druze/Jews mistranscription, worth flagging on its own**; asks for
      $1 million by end of week; claims Najib's people are dying and that
      Najib has personally rescued kids; claims to have met with religious
      leadership and Israeli/Jewish leadership; claims Druze have
      protected Christians for decades; claims Trump invited Syria's
      President al-Sharaa to join the Abraham Accords "two hours ago";
      solicits tax-deductible donations to the foundation). Same two
      tracks as the item above:
      - [x] **Wiki — sorted 2026-08-31** (full reasoning:
        `docs/r7au_gvjp_wiki_claim_sort_2026-08-31.md`). Result:
        `06_million_dollars_by_week_end` and `11_donate_tim_ballard_foundation`
        are (a) ABOUTSELF-usable (the latter resolved jointly with
        `R7Au1bxt6Jc`'s `07_tim_ballard_foundation_founding` — same
        underlying fact, cite once). **`10_trump_invited_alsharaa_abraham_accords`
        is the standout of this whole batch: independently verified 2026-08-30
        (see the item two above this one) as real-event-plus-spin — this is
        the one claim in 25 across both videos that's actually ready to turn
        into drafted wiki text**, contrasting Ballard's "two hours ago"
        fundraising framing against the sourced Times of Israel/JPost
        timeline. Not drafted yet — next step, not done here. `03`, `05`
        (needs independent sourcing; `05` also carries the standalone
        Yazidi/"Ezean Christians" misidentification flag, kept separate from
        the general Druze/Jews mistranscription caveat), and `04`/`07` are
        (b) — third-party atrocity and eyewitness claims, no independent
        sourcing found. `01`, `02` (dup of `R7Au1bxt6Jc`'s `04`, same
        Jethro/lineage claim — not wiki-relevant either way), `08`, `09` are
        (c) not wiki-relevant.
      - [x] **Social clips — selected 2026-08-31**: `10_trump_invited_alsharaa_abraham_accords`
        queued as an exposé-style debunk (same real-event-plus-spin pattern
        as the July 18th cut) — the strongest new clip candidate from either
        video, now that it's independently verified. `05_kids_raped_sex_markets_iraq_2014`
        queued narrowly for the Yazidi-misidentification angle specifically
        (a citable factual error, not the atrocity claim itself). `04_seen_footage_happening_now`
        **not separately queued** — its 31.26-33.68s range already falls
        inside the 26-43s "recycled montage" segment already cut into
        `najib_expose/final_video.mp4`. Both new picks queued to
        `dl_wm/inputs/ballard_batch_2026-08-31_selected.jsonl` alongside the
        `R7Au1bxt6Jc` picks above — not rendered, spot-check timestamps
        first. Input file staged at `dl_wm/inputs/gvjp6bcvq4_claims.jsonl`,
        same schema as the `r7au1bxt6jc_claims.jsonl` file above.
        **Timestamps are hand-estimated from the SRT, not frame-verified**
        — spot-check against the source video before running
        `clip_driver.sh` (copied per run, not edited in place).

      **VERIFIED 2026-08-30 — the Trump/al-Sharaa Abraham Accords claim,
      same pattern as the July 18th item above: real event, wrong
      framing.** Trump did publicly urge Syria's President al-Sharaa to
      join the Abraham Accords — real, independently reported across
      multiple outlets (first at their May 2025 Riyadh meeting, Trump:
      "I hope you're going to join [the Abraham Accords]... he said
      yes"). But al-Sharaa's actual, most recent public stance (their
      November 2025 White House meeting) is a hedge, not agreement: "We
      are not going to enter into a negotiation directly, right now."
      As of this fundraising clip, Syria has not joined and there's no
      confirmed same-day event matching Ballard's specific "two hours
      ago" framing — the underlying diplomatic push is real, the
      "breaking news, right now, tied to my fundraising ask" packaging
      is not independently confirmed. Sources:
      [Times of Israel](https://www.timesofisrael.com/trump-urges-syrias-al-sharaa-to-join-abraham-accords-with-israel/),
      [Jerusalem Post](https://www.jpost.com/middle-east/article-873445).

      **Both verified claims in this batch (this one and the July 18th
      ruling in the item above) follow the same tactic: take a real,
      independently-confirmable event and recast it — bigger, more
      final, more current, or more personally vindicating than the
      actual record supports.** Worth keeping that framing in mind for
      any claim in this batch still unverified — the pattern isn't
      outright fabrication, it's real-event-plus-heavy-spin, which
      changes what a correction needs to say.

- [x] **First exposé cut made from `GvJP_6bcvq4`** — 2026-08-30, done.
      Frame-by-frame review (see `docs/gvjp6bcvq4_frame_analysis_2026-08-30.md`)
      found the presenter shots (Ballard + "Najib") look like genuine,
      continuously-shot footage — but the "proof" B-roll spliced in
      right after is a rapid montage of multiple distinct, unrelated
      clips: at least one pillarboxed video insert (a rifle-scope POV
      over a body) and, more damning, **a 4-panel grid of separate still
      photos, each individually timestamped "9:28 AM"** (phone gallery/
      messaging-app screenshots composited into one frame, not video at
      all) — presented as live proof of the claimed event. Cut a 43.7s
      short from this: `dl_wm/outputs/2026-08-27/youtube__GvJP_6bcvq4/najib_expose/final_video.mp4`,
      titled "Why would this Syrian, 'Najib,' be in Israel?" — title
      card → Najib/Druze/Jethro intro (8.8-21.9s of source) → card →
      the recycled montage (26-43s of source) → card → Ballard back on
      the hillside pleading over it (43-48.5s of source). Built via
      `bin/clip_driver.sh`, copied per-run to
      `outputs/2026-08-30/najib_expose/clip_driver_najib.sh` (per
      [[feedback_dl_wm_clip_workflow]]); input jsonl at
      `outputs/2026-08-27/youtube__GvJP_6bcvq4/najib_expose_clips.jsonl`;
      title card image at `outputs/2026-08-30/najib_expose/title.png`.
      Source video's own watermark (`Official Tim Ballard`, upload date
      `20250808`) survives into the cut, which is useful provenance if
      this ever gets shared.
      Still open:
      - [ ] Reverse-image-search the two suspect frames (the rifle-scope
        POV insert and the 4-panel screenshot grid) to identify their
        actual origin — this is what would turn "we noticed this looks
        recycled" into an independently citable debunk.
      - [x] `R7Au1bxt6Jc` checked 2026-08-30 — different picture. Scanned
        the full ~24.4 min video at 10s intervals (147 thumbnails, 5
        contact-sheet grids). This is a full TBN Israel network
        production (café interview + refugee-camp B-roll + a Syrian
        opposition speech + a French diplomatic meeting + embedded IDF
        combat footage + a memorial-candle scene + a protest/flag-burning
        segment + standard YouTube outro), not a solo Ballard splice job.
        B-roll throughout reads as genuine professional broadcast
        footage (consistent quality, blurred child/civilian faces —
        standard journalistic privacy practice, not a tell). **No
        pillarboxed inserts or timestamped-screenshot grids like
        `GvJP_6bcvq4` turned up at this sampling resolution** — but a
        10s interval could still miss a brief 2-3s insert, so this isn't
        a clean bill of health, just a first pass. Worth a denser
        second pass around 02:30 (a pixelated/blurred frame) and the
        combat-footage segments at 06:00-06:30 and 20:00-20:30 if this
        video specifically becomes important.
      - [ ] The other 2026-08-27 batch videos (`GvJP_6bcvq4` done,
        `R7Au1bxt6Jc` done, `KuFa_GibNjE` is a known non-issue re-upload)
        haven't been frame-checked this way.

- [ ] **Data-quality note for both items above (and any future Syria/Druze
      content from this batch): this is not a Whisper mishearing.**
      **Corrected 2026-09-01, per John: Ballard himself always mixes up
      Druze and Jewish — he says "Dru-ish,"** a blend of the two words, on
      camera. Whisper is transcribing what he actually says; it just has no
      spelling for the blend, so it lands on the nearest real word ("Jews")
      instead. Confirmed by context in both `urDwfY9-Cj0` and `R7Au1bxt6Jc`
      (Jethro/Shuaib lineage claims, "Christian Drues," Druze IDF soldiers
      described as "Jews soldiers" one sentence after being correctly
      called Druze). **"Dru-ish" is the correct rendering** for this —
      when correcting these raw transcripts for quotation, render Ballard's
      actual word as "Dru-ish," not silently normalized to "Druze" (which
      would erase what he actually said) and not left as Whisper's "Jews"
      (which misattributes the claim to Jewish people). Don't quote these
      raw transcripts without that fix first.

- [ ] **`KuFa_GibNjE` is not a new find** — checked 2026-08-27, it's a
      re-upload/clip compilation of quotes already catalogued from the
      Heather Schott "Holy Disruption" podcast interview (the Brazil
      "mayhem/systematic rape" line, ROI-on-slavery line, movie-inaccuracy
      admission, "total coward" line, Jesus-texts line, "13 or 14...
      pregnant" line — see [[project_dl_wm_ballard_clown_reel]]). No new
      wiki-relevant content, just noting so a future session doesn't
      re-transcribe/re-check it.

- [ ] **Wanted, not currently possible: download a specific flagged
      Instagram post (e.g. a known-bot account's post — see
      `dl_wm/inputs/instagram_known_bots.jsonl`, started 2026-08-27) on
      demand via `dl_wm`.** Tried 2026-08-27 against
      `https://www.instagram.com/p/Dcb0CeLgdHM/` using the new
      `haddamgoel` account/session (see the ig_watch_ballard.py entry
      below for how that got set up) — two separate, still-unresolved
      problems stacked on top of each other:
      1. Reading a *specific post's* metadata (`instaloader.Post.from_shortcode`)
         did NOT hit the 429 that profile-level queries
         (`web_profile_info`) keep hitting — so post-level reads may not
         be blocked the same way. Not confirmed as reliable, just this
         one instance.
      2. Once metadata loaded fine, actually downloading the media
         404'd on Instagram's CDN (`scontent-sea1-1.cdninstagram.com`)
         for the first entry of what's a multi-item carousel post.
         Not root-caused — could be a stale/mismatched sidecar media
         URL from Instaloader, not a login or rate-limit issue. Other
         carousel entries untried.
      Config change made in the process, still in place: `dl_wm/conf/app_config.json`
      now has `"instagram": {"username": "haddamgoel"}` (previously
      absent — downloader was running fully anonymous before this).
      Uses the instaloader session at `~/.config/instaloader/session-haddamgoel`
      (created via `veritastimmy/bin/ig_cookie_bridge.py`, same account
      as `conf/instagram.cookies.goelhaddam.txt` below). Revert that
      config if `merrillp.jensen`'s session is preferred as the default
      again.

- [ ] **Decide what (if anything) to do with the Good Newsroom video
      transcript.** Transcribed 2026-08-27 — turned out NOT to be an
      empty puff piece like the article text. Real, quotable claims from
      Ballard on camera: an origin story (wife's Ukraine foundation →
      "aerial recovery" claiming 3,000 children/people rescued across 6
      countries), an explicit self-comparison to Sound of Freedom ("one
      country, Colombia... this is six countries"), and a specific
      unverified statistic ("80% of kids who disappear... recruited from
      their own cell phones"). Full transcript:
      `dl_wm/outputs/2026-08-27/vimeo__1139346138/vimeo__1139346138.txt`;
      summary with caveats: `~/Desktop/hidden_war_video_transcript_
      2026-08-27.txt`. Usable only as WP:ABOUTSELF-attributed claims
      ("Ballard said..."), never stated as fact — deliberately not
      drafted into article text without John weighing in first, given
      how claim-heavy it turned out to be.

- [ ] **Process the 486 phone screenshots staged in `inputs/screenshots/`
      (2026-08-29).** Pulled from iPhone via `ifuse`, renamed to
      `YYYY-MM-DD_tb.png` (chronological `-2`, `-3`, ... suffix for
      same-day duplicates; 4 files with no usable EXIF date fell back to
      file mtime instead — not their real capture date). Gitignored
      (`/inputs/`), not committed. Nobody has looked through them yet to
      say which are actually case-relevant — needs a pass to sort
      relevant vs. not, and likely `scripts/exif2table.sh` run over
      whatever's kept for an EXIF-provenance table before anything goes
      into an exhibit doc.

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
      loop run for ~11 minutes before being killed.
      **Re-tried 2026-08-27 (7 days after the last attempt)** — still
      `429 Too Many Requests` on `tim_ballard89` (see
      `data/ig_watch_wakeup.log`). A week of elapsed time didn't clear it.
      **Account-rotation theory ruled out, 2026-08-27:** got a genuinely
      new account working — `conf/instagram.cookies.goelhaddam.txt`
      (account `haddamgoel`), authenticated via desktop Chrome login +
      `yt-dlp --cookies-from-browser` export, verified live by
      `bin/ig_cookie_bridge.py` (`test_login()` succeeded) and now the
      third entry in `ig_watch_ballard.py`'s `--cookie-file` fallback
      list. First-ever live query on this brand-new account/session
      still hit `429 Too Many Requests` — tested against both
      `tim_ballard89` and `pickleballandpitty` (different target,
      isolates the target from the block). Same 429 both times, on a
      session that had never talked to Instagram before. **This means
      the block isn't account/session-level — it's most likely an
      IP-level block on this machine's connection to Instagram.**
      Swapping cookie files further won't help; would need a different
      network path (VPN, different connection) to actually test that.

      **IP-block theory ruled out, 2026-08-30:** re-tested a fixed target
      (the `kaheakamauu` reel, `C2n3N5VvHYl` — see
      `docs/collaborators_screenshot_scan_2026-08-29.md`'s Kahea Kamauu
      thread) from a phone hotspot on a different carrier network
      entirely (T-Mobile cellular IP `172.56.205.213`, vs. the Spectrum
      home connection). Same two failures on both networks, byte-for-byte
      identical error text:
      - anonymous `yt-dlp`: `Requested content is not available,
        rate-limit reached or login required` — both networks.
      - `--cookies conf/instagram.cookies.txt` (`merrillp.jensen`):
        `HTTP Error 400: Bad Request` — both networks, **not** a 429.

      Identical failures across two unrelated networks/ISPs means this
      is not network/IP-level. Re-reads as two separate, more mundane
      causes: (1) Instagram's standard wall for any non-browser,
      unauthenticated client — expected, not evidence of a targeted
      block; (2) the `merrillp.jensen` cookie jar is most likely stale,
      malformed, or the wrong format for what's being asked of it (a
      plain HTTP 400 is a request-format/auth problem, not a rate-limit
      response — and `downloaders/instagram.py` already notes instaloader
      wants a session file, not a Netscape cookie jar, which is what
      `--cookies` handed to raw `yt-dlp` actually is).

      **Suggested next step is a login refresh, not a network workaround:**
      generate a fresh instaloader session the same way
      `bin/ig_cookie_bridge.py`/the `haddamgoel` account was set up on
      2026-08-27 — either `instaloader --login=<username>` interactively,
      or a fresh `yt-dlp --cookies-from-browser` export from a real,
      currently-logged-in browser session — and retest with that,
      through `ig_watch_ballard.py`'s own instaloader-based path rather
      than raw `yt-dlp --cookies`. If a *freshly*-authenticated session
      still comes back 429 on first use (like the `haddamgoel` test did
      2026-08-27), that's the actual signal worth escalating on — not
      this 400.

      Remaining before this is actually done:
      - [x] test from a different IP/network to confirm the IP-block theory — ruled out 2026-08-30, see above
      - [ ] get haddam's insta creds
      - [ ] regenerate a fresh, valid instaloader session/cookie export and retest
      - [ ] get one clean live run once that's sorted
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

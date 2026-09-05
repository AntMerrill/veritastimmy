# Wiki-usability sort: untouched 2026-08-25/26 vimeo batch (2026-08-31)

Seven `dl_wm` transcripts, downloaded 2026-08-25/26, never claim-extracted or
referenced in any doc before this pass (confirmed via grep across both
repos' `docs/*.md`). Unlike the `R7Au1bxt6Jc`/`GvJP_6bcvq4` batch
(`docs/r7au_gvjp_wiki_claim_sort_2026-08-31.md`, same sort framework used
here), `source_url` is `null` in every one of these manifests — no known
provenance beyond the vimeo ID and download date. Read each `.srt` in full
(not the flattened `.txt`, which loses speaker/paragraph structure).

Sort key: **(a)** usable WP:ABOUTSELF-attributed / **(b)** needs independent
sourcing / **(c)** not wiki-relevant.

## Headline finding

**`vimeo__1109501243` is Noticias Caracol (Colombian TV network) news
coverage of "Operación Cristal 2," the actual 2014 Cartagena sting Sound of
Freedom is based on — genuine independent journalism, not Ballard
self-report, and by far the most wiki-valuable item in this whole batch.**
See its own section below.

## Data-quality summary

| File | Speaker | Usable? |
|---|---|---|
| `vimeo__1109193765` | None — gospel/hymn song ("Go tell that long tongue liar... God's gonna come down") | **No.** Whisper picked up music, not speech. Interspersed Portuguese fragments are transcription noise, not real content. Zero claims extractable. |
| `vimeo__1109252893` | Ballard + an unnamed colleague ("Matt") | Yes — real content |
| `vimeo__1109253570` | Ballard | Yes but thin — 25s, one paragraph |
| `vimeo__1109254647` | Ballard | Yes — real content |
| `vimeo__1109254777` | Mixed: hymn-style music (garbled) + a Brazilian government minister + an unidentified Amazon/Indigenous Brazilian woman | Partially — real dialogue exists but is spliced between music and multiple speakers; treat speaker attribution as uncertain |
| `vimeo__1109255041` | Ballard (presumed, first-person plural "we") | Marginal — 33s, entirely religious framing, no factual claims |
| `vimeo__1109501243` | Noticias Caracol narrator + Tim Ballard (quoted/interviewed) + on-scene audio | **Yes — independent journalism, the strongest source in this batch** |

One aside, out of scope for this doc: `vimeo__1109252893` has an unnamed
colleague addressed as "Matt" who describes his own undercover work — if
that's relevant to [[project_matt_cooper_running_gag]], flagging for
whoever owns that thread; not pursued here.

## `vimeo__1109252893` (Haitian-Dominican border)

| Claim | Sort | Note |
|---|---|---|
| "One of the most horrific child slavery scenes in the world and no one knows it" (Haiti-DR border) | (b) | Sweeping claim, unverified |
| Estimated 400,000+ children in the border region, "disposable... for sex, for labor, for organ harvesting" | (b) | Large unverifiable statistic; organ-harvesting claims specifically are a recurring, rarely-substantiated trope in anti-trafficking rhetoric generally — worth treating with extra skepticism if ever cited |
| "We've been doing since 2014" (border operations) | (a) | Simple self-described operational timeline |
| Matt (colleague): describes undercover work, says they've "rescued many" at a "resort town," references organ-harvesting reports | (b) | Third-party corroborating anecdote, same sourcing bar as Ballard's own claims |

## `vimeo__1109253570` (Madrid)

Single claim: meeting anti-trafficking orgs to build a Spain/Latin
America intel network. **(c)** — PR-clip scene-setting, no substantive
content to sort.

## `vimeo__1109254647` (Brazil/Amazon)

| Claim | Sort | Note |
|---|---|---|
| US teens lured via social media by traffickers, end up on "yachts, boats" | (b) | Unverified, non-specific |
| "80,000 people disappeared [in Brazil] in '23," many children, most "up the Amazon" | (b) | Large, specific statistic — checkable against Brazilian missing-persons data if this is ever pursued, not independently confirmed here |
| Children moved down the Amazon by boat into Europe for "labor, sex slave, organ harvesting," organ markets "in the Middle East" | (b) | Serious unverified claim, same organ-harvesting caveat as above |
| Working with Brazilian federal/state police and military, flying in "a military plane" | (a) | Operational self-description |

## `vimeo__1109254777` (Brazil, mixed)

Structurally the messiest file — hymn-style music bookends, a brief
exchange with what's described as a former "minister of culture" who
"made [the Sound of Freedom poster] viral" in Brazil, then an unidentified
Amazon/Indigenous Brazilian woman's speech about "MAPA," a human-trafficking
route, describing a specific case: a 7-year-old girl "married, strangled,
sexually abused, and raped," found "outside a tent."

**(b)** if used at all — this is third-party testimony from an unnamed
speaker, not Ballard's own claim, describing a specific, extremely serious
individual case with no corroborating detail (no name, date, or location
beyond "the route"). Flagging rather than sorting further: speaker identity
itself needs to be established before this could go anywhere near wiki
text, independent of the sourcing bar for the content.

## `vimeo__1109255041` (pre-op religious framing)

33 seconds, entirely religious ("we can go through crazy things in the
Amazon... he will send angels to fill the Amazon until we rescue everyone
of these children"). **(c)** — no factual claim to sort, though the
messianic self-framing of operations is consistent with the pattern noted
elsewhere in this project's transcripts.

## `vimeo__1109501243` — Noticias Caracol, "Operación Cristal [2]" (Cartagena, 2014)

**2026-08-31 update: found and checked the actual Noticias Caracol article
online** (`noticiascaracol.com/colombia/asi-fue-como-un-agente-del-fbi-logro-burlar-y-desmantelar-a-proxenetas-en-cartagena-rg10`),
plus corroborating pieces from El País and Infobae. Two corrections to the
Whisper-derived version below — **do not use the uncorrected version for
anything**:

1. **Name was wrong.** The pageant-contestant defendant is
   **Kelly Johana Suárez Moya**, not "Liliana Suárez Mulla" — that was a bad
   reconstruction from garbled audio, not a close call.
2. **RESTORED 2026-08-31, second pass: the "convicts currently free" detail
   is real — verified word-for-word against the video's own SRT, not
   Whisper noise.** Earlier the same day this was downgraded to
   "unconfirmed" because three written news articles (Noticias Caracol's
   own site, El País, Infobae) don't mention it. That was checking the
   wrong layer — those are short recap pieces; the ~18-minute broadcast
   itself says it explicitly, right after the conviction/sentencing recap:
   *"...todos están libres por vencimiento de términos. Y ahora la misión
   de la justicia es recapturarlos para que cumplan con su pena."* ("...all
   of them are free due to expired legal deadlines. And now the mission of
   justice is to recapture them so they can serve their sentence.") This is
   the broadcast's own narration, not Ballard's framing, not a
   transcription artifact — **independently reported by Noticias Caracol,
   citable as fact.** The written articles simply omit a detail the video
   includes; their silence isn't a contradiction. Apologies for the
   whiplash — this is now the confirmed version, restored to (a).
   (Separately: the same passage has the broadcast's own narrator calling
   Ballard "exagente, el FBI" — the video's own claim is FBI, not Homeland
   Security, for what that's worth against the timballard.org/Infobae
   "Homeland Security" framing noted elsewhere.)

Original Whisper-derived summary follows, flagged as needing this
correction rather than rewritten from scratch:

Spanish-language broadcast. Whisper's Spanish transcription is rougher than
its English output — proper names below are **best-effort reconstructions**
(e.g. "peroxenitas" → *proxenetas*, "pimps"; peripheral names like "Yllonas
Suares mollas" / "el Ijuana Suárez Mulla" turned out to be a garbled
**Kelly Johana Suárez Moya**, confirmed above, not the "Liliana Suárez
Mulla" first guessed) — verify against an actual Noticias Caracol transcript
or news archive before quoting any name in wiki text.

**This is independent Colombian television journalism, not Ballard
self-report** — the strongest sourcing tier of anything found across either
batch this session. Content, paraphrased:

- Oct 11, 2014: a child-sexual-abuse/child-prostitution sting was uncovered
  in Cartagena, Colombia — "Operación Cristal [2]," which the report states
  **explicitly inspired the film *Sound of Freedom*.**
- Tim Ballard is named directly as one of the infiltrated agents ("uno de
  los agentes infiltrados en la operación"), posing as "el jefe gringo."
  Identified in the report as an ex-FBI agent who had spent recent years
  infiltrating trafficking organizations in Latin America.
- Operation involved Colombia's Fiscalía (prosecutor's office), the Armada
  Nacional (Navy), Migración Colombia, ICBF (the child-welfare agency), and
  "la ONG de Tim Balar" (his NGO, i.e. O.U.R.) working together.
- A fake modeling agency was used as cover; traffickers offered children to
  purported foreign buyers, including a specific line from a trafficker
  ("Fuego," Juan Manuel Oquendo Sierra) offering his "12-year-old virgin
  sister" for $1,000.
- **54 minors were rescued** in the operation.
- **5 traffickers were captured**; convicted and sentenced to **16 years'
  imprisonment each**, one acquitted.
- **10 years later (i.e. this broadcast, ~2024): the Superior Tribunal of
  Cartagena confirmed the sentences on appeal — but the report states all
  convicts are currently free due to "vencimiento de términos" (expiration
  of statutory/procedural deadlines), and that authorities' current mission
  is to recapture them.** This is a substantive nuance not present in
  Ballard's own framing of this or similar operations elsewhere in this
  project's transcripts.
- Official Colombian figures cited: ~400 children induced into prostitution
  nationally "in the last four years" (as of ~2014), with authorities
  saying the real, unreported figure is likely higher.
- The report previews a follow-up segment: testimony from "Pedro" (likely a
  pseudonym), one of the rescued minors, now in exile due to threats
  received for speaking out.

### Sort

| Claim | Sort | Note |
|---|---|---|
| Operación Cristal happened, Oct 2014, Cartagena — sting inspired Sound of Freedom | **(a)** | Independently reported by Colombian TV news, not Ballard's own claim — this is citable as fact, not just ABOUTSELF; corroborated 2026-08-31 against the live Noticias Caracol article |
| Ballard was one of the infiltrated agents, posed as "jefe gringo" | **(a)** | Independently reported, corroborated |
| 54 minors rescued, 4 traffickers convicted (Kelly Johana Suárez Moya, Samuel David Olave, Eduardo Ortega, Juan Manuel Oquendo Sierra "Fuego"), 16-year sentences, 1 acquitted | **(a)** | Corroborated 2026-08-31 against El País and Noticias Caracol — corrects the earlier Whisper-derived count/name (see update note above) |
| "Convictions confirmed on appeal 10 years later, all convicts currently free, authorities trying to recapture them" | **(a)** | **RESTORED** — verified verbatim in the broadcast's own SRT (see update note above), not just the written recap articles. Citable as fact. |
| ~400 children nationally induced into prostitution over 4 years (official Colombian figures, as of ~2014) | **(b)** | Attributed to Colombian authorities in the report, but a third-party statistic about the country generally, not specifically verified here |
| Specific dialogue/pricing detail (the "12-year-old virgin sister" offer, per-child pricing) | **(b)** | Real per the broadcast's own recorded audio, but graphic operational detail — high caution if ever excerpted, and exact names/spellings need independent verification first |

**Note for anyone using this later:** "Suárez Moya" (corrected name), a
trafficking-ring member named in this 2014 Colombian criminal case, is
**unrelated** to *Suárez v. Angel Studios/Ballard* (the separate, ongoing
civil defamation suit covered by the standing wiki caution — see
[[feedback_tim_ballard_wiki_legal_caution]]). Same surname, different
person, different case, different decade. Not touching the guarded topic
here; flagging only so the name coincidence doesn't cause confusion later.

## What's actually ready to draft

**The full `vimeo__1109501243`/Noticias Caracol picture is corroborated and
wiki-ready, including the standout detail: the operation happening,
Ballard's role, 54 minors rescued, the four names, 16-year sentences, one
acquittal, AND that all four are currently free on expired legal deadlines
while authorities try to recapture them** — that last part verified
directly against the broadcast's own SRT (see update note above), not just
Whisper output or the shorter written recap articles. This is a solid,
citable origin-story source (independent Colombian journalism > Ballard's
own retelling) with real narrative weight: a "case closed, justice served"
framing the rest of this project's Ballard-sourced material implies is
actually undercut by the broadcast's own reporting. **Not drafted here** —
flagging as the next concrete step, same treatment as the al-Sharaa item in
the sibling doc.

Everything else in this batch is either not wiki-relevant, thin, or stuck
at (b) pending sourcing this session didn't chase down.

## Not queued for clips

Nothing from this batch queued to `dl_wm/inputs/` — that decision was
scoped to the earlier `R7Au1bxt6Jc`/`GvJP_6bcvq4` batch and not asked for
here. Flagging that the Operación Cristal footage could make a strong
factual explainer clip (real names, sentences, the release-on-technicality
detail) if that's ever wanted, but that's a call for whoever picks this up
next, not decided in this pass.

# Phone screenshot scan: Instagram "Collaborators" panels

First pass at triaging the 486 phone screenshots imported 2026-08-29 into
`inputs/screenshots/` (see `CLAUDE.md`'s "Phone screenshot import" section
and the `docs/TODO.md` entry). Scope of this pass: find every screenshot
that captures Instagram's "Collaborators" UI — the panel Instagram shows
when a post has more than one tagged co-author — on a `timballard89` post.
Not a full relevance triage of all 486; see "Not covered" below.

## Method

- Built 17 contact-sheet grids (30 thumbnails each, filename under each
  frame) from all 486 files with a scratch Pillow script, saved to
  `inputs/contact_sheets/` for reference.
- Read each sheet, visually scanning for the "Collaborators" list UI
  (a header labeled "Collaborators" followed by avatar/handle/"Follow"
  rows).
- Copied the 20 matching source screenshots (full-res, unmodified) to
  `inputs/collaborators/`.

Both `inputs/contact_sheets/` and `inputs/collaborators/` fall under the
existing `/inputs/` gitignore — not committed, same as the source
screenshots.

## Result: 20 screenshots, dated 2026-01-27 through 2026-08-19

| Screenshot | Collaborator handles listed |
|---|---|
| `2026-01-27_tb-3.png` | timballardfoundationecuador, estamananate, teleamazonasnec |
| `2026-02-07_tb-9.png` | freddydice, sandrabronzina, francoisevenspaul, actualidadconsoledad |
| `2026-02-11_tb-2.png` | druze_nexus, savedruze, banim3rouf, western_syria_development |
| `2026-02-13_tb.png` | danaalexatv, one_america_news_ |
| `2026-02-15_tb.png` | banim3rouf, druze_nexus, stopalawitegenocide, western_syria_development |
| `2026-02-24_tb-3.png` | christ.saves.the.world, western_syria_development |
| `2026-03-27_tb-2.png` | christ.saves.the.world, western_syria_development |
| `2026-04-12_tb-4.png` | scottythekid, patriotketopop, 337_pure_blood |
| `2026-04-12_tb-7.png` | latterdaychad, nauvoolegion, transcendental_mormon_my..., mount_of_olivesids, latterdayavenger |
| `2026-04-15_tb-6.png` | mansor_ashkar, joanofjudea, ali_the_lor, keidardoron |
| `2026-04-20_tb-3.png` | tbfrescue, paolafelixdiaz |
| `2026-04-20_tb-5.png` | andres.fearless, soundoffreedommovie, fearless.brothers, eduardoverastegui |
| `2026-04-20_tb-8.png` | fearless.brothers, karim.fearless, gabriel.unbound, andres.fearless |
| `2026-04-20_tb.png` | tbfrescue, eduardoverastegui |
| `2026-04-22_tb-9.png` | soundoffreedommovie, ambleahcampos, eduardoverastegui |
| `2026-04-24_tb-7.png` | andres.fearless, encounterministries_mexico, fearless.brothers |
| `2026-07-26_tb-2.png` | thelight8011, brokenshepherds, nathan_appfel, religionbusiness |
| `2026-07-30_tb-9.png` | podcastlaplena, emilia_maldonadojaramillo, timballardfoundationecuador |
| `2026-08-03_tb-2.png` | graciela_noguera_, matthewcooper, denisromeroroa |
| `2026-08-19_tb-6.png` | timballardfoundationec..., p.juancarlosv, podcastlaplena |

(`timballard89` itself is a co-author on most of these and is omitted
above where it's just the account being viewed.)

**Working theory (John, 2026-08-30): these are bot/inauthentic
accounts, not real people or an actual collaborative team.** Treat
everything below as an account/bot-network mapping exercise, not a
social or friendship graph — language like "team" or "cluster" below
refers to accounts that co-appear, not to a group of humans who know
each other.

## Handles grouped by apparent affiliation

- **Sound of Freedom / Fearless cluster**: `eduardoverastegui` (Eduardo
  Verástegui — matches the "Eduardo" named in the standalone
  `2026-02-17_tb.png` post about SOF 2 & 3), `soundoffreedommovie`,
  `fearless.brothers`, `andres.fearless`, `karim.fearless`,
  `gabriel.unbound`
- **Ecuador foundation**: `timballardfoundationecuador`, `tbfrescue`,
  `podcastlaplena`, `paolafelixdiaz`, `emilia_maldonadojaramillo`,
  `p.juancarlosv`
- **Druze/Syria advocacy**: `druze_nexus`, `savedruze`, `banim3rouf`,
  `western_syria_development`, `stopalawitegenocide`
- **LDS-adjacent/critical accounts**: `christ.saves.the.world`,
  `scottythekid`, `337_pure_blood`, `latterdaychad`, `nauvoolegion`,
  `mount_of_olivesids`, `latterdayavenger`, `mansor_ashkar`, `joanofjudea`,
  `ali_the_lor`, `keidardoron`
- **Other / unclustered**: `danaalexatv`, `one_america_news_`,
  `thelight8011`, `brokenshepherds`, `nathan_appfel`, `religionbusiness`,
  `ambleahcampos`, `encounterministries_mexico`, `graciela_noguera_`,
  `matthewcooper`, `denisromeroroa`, `freddydice`, `sandrabronzina`,
  `francoisevenspaul`, `actualidadconsoledad`

**Flagged**: `matthewcooper` appears in `2026-08-03_tb-2.png` alongside
`graciela_noguera_` and `denisromeroroa`. Possible connection to the Matt
Cooper running-gag material — not yet checked against that thread.

## Co-occurrence network analysis (2026-08-30)

The "grouped by apparent affiliation" section above was eyeballed from
context. This section instead derives clusters and tie-strength directly
from which handles are *actually co-tagged together on the same post*
(`timballard89` excluded as the hub present on nearly all of them) — 40
distinct handles across the 20 screenshots.

**Recurring ties** — co-tagged together on 2+ separate posts (the
closest thing to a repeat-pairing signal for these accounts):

| Pair | Posts together |
|---|---|
| `andres.fearless` ↔ `fearless.brothers` | 3 |
| `eduardoverastegui` ↔ `soundoffreedommovie` | 2 |
| `banim3rouf` ↔ `druze_nexus` | 2 |
| `banim3rouf` ↔ `western_syria_development` | 2 |
| `druze_nexus` ↔ `western_syria_development` | 2 |
| `christ.saves.the.world` ↔ `western_syria_development` | 2 |

**Most-connected handles** (distinct co-tagged partners): `andres.fearless`
and `fearless.brothers` (6 each), `western_syria_development` and
`eduardoverastegui` (5 each), then `timballardfoundationecuador`,
`banim3rouf`, `druze_nexus`, and the whole single-post `2026-04-12_tb-7`
group (4 each, but from only one shared post — see caveat below).

**Connected-component clusters** (handles chained together by shared
posts, not just affiliation guesswork):

1. **Sound of Freedom / Fearless cluster** (10 accounts, densest cluster,
   3 internal posts): `eduardoverastegui`, `soundoffreedommovie`,
   `fearless.brothers`, `andres.fearless`, `karim.fearless`,
   `gabriel.unbound`, `tbfrescue`, `paolafelixdiaz`, `ambleahcampos`,
   `encounterministries_mexico`
2. **Ecuador foundation** (7 handles, 2 internal posts):
   `timballardfoundationecuador`, `podcastlaplena`, `p.juancarlosv`,
   `emilia_maldonadojaramillo`, `estamananate`, `teleamazonasnec`,
   `timballardfoundationec...`
3. **Druze/Syria advocacy** (6 handles, 4 internal posts,
   `western_syria_development` is the hub): `druze_nexus`, `banim3rouf`,
   `savedruze`, `stopalawitegenocide`, `christ.saves.the.world`
4. **LDS-critical cluster A** (5 handles, single post
   `2026-04-12_tb-7` only): `latterdaychad`, `nauvoolegion`,
   `mount_of_olivesids`, `latterdayavenger`, `transcendental_mormon_my...`
5. **LDS-critical cluster B** (4 handles, single post
   `2026-04-15_tb-6` only): `mansor_ashkar`, `joanofjudea`, `ali_the_lor`,
   `keidardoron`
6. Four more clusters confirmed only within one post each: Feb-07 group
   (`freddydice`, `sandrabronzina`, `francoisevenspaul`,
   `actualidadconsoledad`), Jul-26 group (`thelight8011`,
   `brokenshepherds`, `nathan_appfel`, `religionbusiness`), Apr-12 group
   (`scottythekid`, `patriotketopop`, `337_pure_blood`), and the flagged
   Aug-03 group (`matthewcooper`, `graciela_noguera_`, `denisromeroroa`)
7. `danaalexatv` ↔ `one_america_news_` (single post)

**Caveats — this is a bot/account network, not a social graph:**
- This measures Instagram co-authorship *tags* between accounts
  believed to be bots/inauthentic, not friendship, human collaboration,
  or even mutual follows. Don't describe any of it as people knowing
  each other.
- Most single-occurrence pairs (clusters 4-7 above) have exactly one
  data point — can't distinguish a recurring pairing from two accounts
  tagged on one joint post.
- No live-IG verification (follows, mutuals, bios) has been possible —
  both cookie sessions are hitting 429s, attributed to an IP-level
  throttle on this machine, not the accounts (see below).

None of this has been verified against the live Instagram accounts
(display names, follower counts, bios) — the table above only records
what each screenshot's UI shows. Two IG cookie sessions
(`merrillp.jensen`, `haddamgoel`) hit 429 Too Many Requests on
2026-08-29 while trying to look up an unrelated post (see below), which
points to an IP-level throttle on this machine — account verification
against live IG was not attempted for these 20 handles as a result.

## Related, unresolved: the `2026-02-17_tb.png` post

Separately from this scan, `2026-02-17_tb.png` (single screenshot, no
same-day duplicates) shows a `timballard89` video post captioned "Thank
you, Eduardo, for speaking out" about Sound of Freedom 2 & 3, naming David
Jacobs, Krista Kacey, Celeste Borys, and Kelly Suarez as
antagonists/subjects. Intended to stage this post's URL into `dl_wm`'s
`data/dlwm_input_queue.jsonl` (per `bin/ig_watch_ballard.py`'s queue
format) for downstream processing, but the post URL isn't visible in the
screenshot itself. Attempted to find it via `instaloader` using the
existing cookie sessions; both `instagram.cookies.txt`
(`merrillp.jensen`) and `instagram.cookies.goelhaddam.txt`
(`haddamgoel`) returned 429 on the very first profile lookup, suggesting
an IP-level block rather than an account-level one. Not staged. Still
open.

## Not covered by this pass

- The other ~466 screenshots have not been triaged for general
  case-relevance (the broader `docs/TODO.md` item).
- 20 or so screenshots across the set are corrupted/unreadable (contact
  sheets render them as red "ERR" tiles — truncated files, broken PNG
  chunks, or unrecognized data streams). Not enumerated exhaustively
  here; visible directly in `inputs/contact_sheets/`.
- No `scripts/exif2table.sh` provenance pass has been run over the 20
  collaborator screenshots yet — still just copied as-is.
- None of the 40-ish distinct handles above have been cross-checked
  against `tests/inputs/ballard/` case documents or the ACJ archive.

# Collaborators co-tag network — 2026-09-21 update

Extends `docs/collaborators_network_2026-09-02.md` with a full manual
review of a new corpus, and finally populates the Portuguese/Brazil
cluster that doc left empty.

## Scope

`inputs/icloud_pngs_2026-09-21/` — 218 screenshots (212 PNG + 6 JPEG)
pulled via an iCloud Photos web export from the "Justin Riggs" persona
account, ISO-date-prefixed and reviewed in full, one by one.

Criteria, per John's explicit instruction ("let's just keep it narrow
now"): **only** the Instagram "Collaborators" post-tag feature counts as
a match — either the full Collaborators sheet or a feed byline
("AccountA and AccountB" / "AccountA and N others"). Story reposts
(one account resharing another's story) do **not** count, even though
they show attribution to another account.

## Method

Read every file at full resolution (no contact-sheet/thumbnail pass this
time), chunked into ~20-image checkpoints reported back as the review
went. Near-duplicate frames of an already-logged post (adjacent video
frames, different scroll positions of the same post) were identified and
silently skipped rather than logged as separate matches. Bylines that
were cut off mid-name ("and 2 others" with no full sheet, or a truncated
handle) were treated as evidence for the manifest but **not** turned into
graph edges — only pairs/sets where every handle was actually legible
went into the edge list, same conservative philosophy the render script
already uses for cluster classification.

## Result: 43 screenshots with a visible Collaborators pattern

Copied full-res, unmodified, to
`inputs/icloud_pngs_2026-09-21/selected/`, tracked in
`selected/selection_manifest.json` (one entry per file, with a `why`
field quoting the exact byline/sheet text). Of those 43, 33 posts had a
fully resolvable handle set and were turned into graph edges (below);
the other 10 are real evidence in the manifest but contribute no edges
(unresolved "and N others").

## Graph update

`scripts/render_collab_graph_clusters.py`'s dataset
(`inputs/collab/collab_edges.csv` + `collab_nodes.csv`) was extended:

- **88 new edge rows** from 33 posts (all-pairs per post where the full
  set was legible, single edge for byline-only pairs).
- **39 brand-new handles**, `timballard89` 22 -> 43 appearances,
  `sandrabronzina` newly tracked at 14.
- **PORTUGUESE cluster populated for the first time** (was empty as of
  2026-09-05) — 10 confirmed Brazil/Portuguese-language nodes:
  `ageisianefreitas`, `danipinheirodosreis`, `diegojjacome`,
  `herbertesmahan`, `ibelacamargo`, `larinoar`, `maaydelara`,
  `professordiegocientista`, `rebecadecastrobatista`, `ritamariamatias`.
- **`sandrabronzina` is now dual-cluster** (Original Four + Portuguese,
  drawn as a split wedge) — she has a real, distinct body of Brazil-
  language Collaborators edges now, separate from the old 2026-02-07
  co-tag island.
- New SPANISH-cluster nodes, mostly Ecuador/Chile: `piedradetoqueec`,
  `filguayaquil`, `fabriciolara.ec`, `freechildhoodec`, `chemalibreria`,
  `ecuavisatv`/`ecuavisanoticias`, `expofamily.cl`, `margaritarojoc`,
  `dramariajosemancino`, `cuerpodextoenlacruz`, `argueta.virginia`,
  `femineidadvirtuosa`, `dra.carmenpeguero`, `cambioglobalparadesarrollo_`.
- `ldsabuseonx` added to LDS_CRITICAL (explicit framing, co-tagged
  directly with `latterdaychad`/`transcendental_mormon_myths`).

Rendered: `inputs/collab/collab_graph_clusters_2026-09-21.png` (full
network) and `inputs/collab/collab_graph_brazil_cluster_2026-09-21.png`
(new sub-render, just the Portuguese/Brazil cluster + its direct hub
ties — 16 nodes, 25 edges, via new companion script
`scripts/render_collab_graph_brazil.py`).

## Notable finds

- **`timballard89` himself is a Collaborator, not just pictured**, on
  two separate postings of an "Expo Family 2026" event flyer (Santiago,
  Chile, Oct 17) — alongside Margarita Rojo, Padre Javier Olivera Ravasi,
  María José Mancino, Agustín Laje, and Sandra Bronzina
  (`IMG_1159`/`1160` and `IMG_1182`/`1183`, different collaborator-count
  variants of the same flyer).
- A cluster of Brazil's Câmara dos Deputados content (`silviawaiapi`,
  `diegojjacome`/`professordiegocientista`, `danipinheirodosreis`)
  showing Tim Ballard testifying about child trafficking in the Amazon.
- A Vatican meeting with Pope Leo XIV (`IMG_1119`, byline
  "timballardfoundationecuador and 4 others" — byline-only, not a graph
  edge since the 4 others were never fully legible).
- `aerialrecoverygroup` confirmed as a real Collaborators node (not just
  a co-mention), tied to the Aerial Recovery Group "Operation Safe
  Return" trafficking-rescue content.

## Forensic backup

`inputs/collab/sha256sums_2026-09-21.txt` — SHA-256 manifest of the 43
curated screenshots + `selection_manifest.json` (44 lines). Scoped to
just the curated set, not the full 218 raw pulls or the CSV/graph
outputs, per John's direction.

An OpenTimestamps stamp of that manifest was tried and then explicitly
backed out ("let's not do bitcoin") — tooling (a throwaway venv at
`~/.local/venvs/ots`) and the resulting `.ots` proof file were both
removed. The hash manifest alone still proves tampering later; it just
lacks an independent third-party timestamp.

## Not covered

- The 10 evidence entries in `selection_manifest.json` with unresolved
  "and N others" bylines — real matches, not graph edges. Worth another
  pass if the full Collaborators sheet for any of those ever surfaces
  (e.g. `IMG_1002`, `IMG_1020`, `IMG_1075`, `IMG_1083`, `IMG_1095`,
  `IMG_1102`, `IMG_1114`, `IMG_1119`, `IMG_1123`).
- No distribution package built yet — held off per John's explicit
  "let's hold off" pending a decision on destination/scope (backup-only
  vs. an external recipient).
- `inputs/collab/collab_edges.csv.bak-2026-09-21` and
  `collab_nodes.csv.bak-2026-09-21` left in place as a pre-update
  rollback snapshot (that directory is a symlink out to the E769-0C67
  USB drive, not tracked in git either way).

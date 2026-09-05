# tbfrescue.org — prior-session findings (2026-08-31 cross-reference)

Found two things neither this session nor today's work had touched: a JSON
from an earlier Claude session, and a whole separate archival repo.

## `dl_wm/inputs/tbfrescue_vimeo.json`

Sources for all 7 vimeo videos referenced throughout today's work, all
from tbfrescue.org:

- **6 from `/recent-rescue-updates/`**, sectioned:
  - `1109252893` — Haitian-Dominican Border
  - `1109193765` — Brazil
  - `1109254777` — Brazil
  - `1109255041` — Brazil
  - `1109254647` — Brazil
  - `1109253570` — Recent Rescue Updates (Madrid clip)
- **1 from `/in-the-news/`**: `1109501243`, captioned on the page itself as
  **"Noticias caracol: Colombia"** — independently confirms today's own
  finding (via live web search) that this is genuine Noticias Caracol
  broadcast content, from a completely different session and method.

## `tbfrescue-mirror` repo (separate from `dl_wm` and `veritastimmy`)

A forensically-oriented WARC archive of tbfrescue.org — chain-of-custody
notes, SHA256 checksums, robots.txt-respecting rate-limited crawl. Local-
only, no GitHub remote (John's call, same as `joderswar`).

**Same spam-compromise pattern as timballard.org, worse:** 6,094 of 6,101
sitemap URLs on tbfrescue.org are injected gambling/casino spam (dated
2025-12-12). Only `/about/`, `/in-the-news/`, `/recent-rescue-updates/`,
`/donate-today/` carry genuine Tim Ballard Foundation content (DBA Red Rock
Foundation Inc, EIN 99-1999715). Sample spam pages and a full URL catalog
(CSV/JSONL/MD) already exist in `tbfrescue-mirror/findings/`.

**Conclusion: both Ballard-affiliated domains checked so far
(timballard.org today, tbfrescue.org in this earlier session) are
compromised WordPress installs**, not an isolated one-off on either site.

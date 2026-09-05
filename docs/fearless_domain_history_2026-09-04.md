# "Fearless" domain history — findings, 2026-09-04

Prepared per John's request to document, with citable sources, how old the
"Fearless"/"Fearless Brothers"/"Fearless Congress" web presence actually is
(Fearless Congress 2026, Guadalajara, featuring Tim Ballard and Eduardo
Verástegui — see `collaborators_urls_2026-09-04.md` and
`collaborators_live_check_2026-09-04.md` for how this thread started).

**Method note, for the record:** all findings below come from two public,
third-party sources — the Internet Archive's Wayback Machine
(`web.archive.org`) and a public WHOIS lookup (`who.is`) — accessed via
browser on 2026-09-04. Exact URLs queried and timestamps returned are
recorded below so each finding can be independently reproduced. Screenshots
are saved as exhibits in `docs/evidence/2026-09-04_fearless_domain_history/`.
Nothing below is inference from social-media bio text (see the same-day
correction in `collaborators_live_check_2026-09-04.md` about that
distinction) — these are domain-registration and web-archive records, a
different and more independently verifiable category of evidence.

## Claim under examination

`fearlessbrothers.com`'s own site states the movement "began... in 2015."
The question: does independent, third-party record of the domains'
history support a multi-year history, or a much shorter one?

## Finding 1 — `fearlessbrothers.com`: registered May 1, 2026

**Source:** WHOIS lookup via `who.is/whois/fearlessbrothers.com`, queried
2026-09-04.
```
Registrar: NameCheap, Inc.
Created:   May 1, 2026
Updated:   June 13, 2026
Expires:   May 1, 2027
Registrant: Redacted for Privacy Purposes (WithheldForPrivacy LLC)
```
**Source:** Wayback Machine, `https://web.archive.org/web/*/fearlessbrothers.com/*`,
queried 2026-09-04 — result: **"No URL has been captured for this URL
prefix."** Zero archived snapshots, ever, at any date.

Both records agree: this domain is roughly **4 months old** as of this
writing, consistent with never having been crawled by the Internet
Archive. (Caveat: a domain can also block archive crawlers via
`robots.txt`, which would also produce zero snapshots — that alternative
explanation was not separately ruled out, but the very recent WHOIS
creation date is independent of and consistent with the Wayback result
either way.)

## Finding 2 — `fearlessmasculinity.com`: previously an Andrew Tate affiliate redirect, not "Fearless" content

**Source:** Wayback Machine CDX API,
`https://web.archive.org/cdx/search/cdx?url=fearlessmasculinity.com&output=text&fl=timestamp,statuscode&limit=30&matchType=exact`,
queried 2026-09-04. Full result (25 total captures on record, Nov 8 2022 –
Jun 7 2026):
```
20221108215515 301
20230225191245 -
20231006070530 301
20250220113354 301
20250220113355 200
20250220131505 200
20250220204742 301
20250220204743 301
20250221032832 301
20250221232226 200
20250222000421 301
20250222000421 -
20250222020614 301
20250222022241 301
20250405090224 301
20250405090224 200
20250406184432 200
20250407030722 301
20250408015414 301
20260204031910 200
20260407102337 200
20260408162718 200
20260512093259 200
20260519225213 200
20260607110430 200
```

**Earliest capture, Nov 8 2022 21:55:15 UTC** — the archived page shows an
HTTP 301 redirect to:
```
https://therealworld.ai/?a=nttpbwzpn8
```
`therealworld.ai` is Andrew Tate's "The Real World" platform; the `?a=`
parameter is a referral/affiliate tracking code. Screenshot:
`docs/evidence/2026-09-04_fearless_domain_history/2022-11-08_fearlessmasculinity-com_redirects-to-therealworld-ai.jpg`.
Same redirect status (301) recurs at the Oct 6 2023 capture per the CDX
record above (the rendered page for that specific timestamp did not load
independently in this session — the browser fell back to displaying the
Nov 2022 capture — so the Oct 2023 finding rests on the CDX status-code
record alone, not a second rendered screenshot; flagged here rather than
glossed over).

**By Feb 21 2025 23:22:26 UTC, the domain serves real "Fearless
Masculinity" content** — page text: "FEARLESS MASCULINITY — BECOME THE MAN
GOD CREATED YOU TO BE," listing 2025 retreat dates (Puebla Mar 7-9, Dallas
Apr 11-13, Querétaro May 2-4, Guadalajara May 30-Jun 1, CDMX Oct 24-26).
Screenshot:
`docs/evidence/2026-09-04_fearless_domain_history/2025-02-21_fearlessmasculinity-com_live-fearless-content.jpg`.

**No captures exist between Oct 6 2023 and Feb 20 2025** — a ~16-month gap
with no Wayback coverage, so the exact switchover date can't be pinned
further with this source alone.

## Finding 3 — WHOIS "Created" date for `fearlessmasculinity.com` (Oct 21, 2024) and how it fits with Finding 2

**Source:** WHOIS lookup via `who.is/whois/fearlessmasculinity.com`,
queried 2026-09-04.
```
Registrar: GoDaddy.com, LLC
Created:   October 21, 2024
Updated:   January 26, 2026
Expires:   October 21, 2026
Nameservers: ns1.dns-parking.com / ns2.dns-parking.com (GoDaddy parking NS)
```
This "Created" date is *later* than the Nov 2022/Oct 2023 Wayback captures
of the same domain — not a contradiction: WHOIS "Created" reflects the
**current registration**, and resets whenever a domain lapses/expires and
is re-registered by a new owner. Read together, Findings 2 and 3 support:
the domain previously belonged to whoever ran the Tate-affiliate redirect
(captured live in 2022 and 2023), then **lapsed and was re-registered by
the current owner on Oct 21, 2024**, with the "Fearless Masculinity" site
built out and live by Feb 2025.

(Note: current nameservers point to GoDaddy's parking service, not an
active host — possibly stale WHOIS caching, possibly the record not
reflecting current production DNS. Not resolved this pass; flagged as an
open thread if it matters later.)

## Bottom line

Independent domain-registration and web-archive records — not site
copy, not social-media bios — show:
- `fearlessbrothers.com`: **~4 months old** (registered May 2026), never
  archived.
- `fearlessmasculinity.com`: real "Fearless" content only verifiably
  begins **Feb 2025**; before that, the same domain was redirecting to an
  Andrew Tate affiliate link as recently as **Oct 2023**.

Neither domain has any independently verifiable web presence supporting
the "since 2015" origin claim. That claim currently rests entirely on the
organization's own copy, not on anything third-party-checkable found this
pass.

## Not done this pass

- No registrant identity was recoverable — both domains use WHOIS privacy
  redaction.
- Did not check for a *different* historical domain (e.g. an older
  `.mx`, a Facebook page, or a differently-spelled domain) that might
  independently corroborate an earlier "Fearless" presence than these two
  domains show — the "since 2015" claim could theoretically be true under
  a different web address not checked here.
- Did not attempt the live-Instagram volunteer-account angle that started
  this thread — that's still open, separate from this domain-history
  finding.

# ACJ Remaining Sub-Archives — Crawl Report

**Date:** 2026-08-10
**Scope:** the 5 sub-archives on American Crime Journal's "Derailed: Operation
Underground Railroad" hub that were left uncrawled after the 2026-08-09 pull
(see `ACJ_HOLDINGS.md` and memory `project_acj_holdings_pull`).
**Archive hub:** https://americancrimejournal.com/acj-investigates/operation-underground-railroad-o-u-r/

## TL;DR

- **Downloaded this session: zero files.** All three sub-archives that turned
  out to be live contain no PDFs or downloadable documents at all — they're
  narrative journalism/article indexes, not document repositories like Legal
  Archive and Financial Archive.
- Two of the five originally-listed sub-archives (**People**, **Organizations
  & Network**) aren't actually published/linked on ACJ's site — their
  "Explore" buttons have no working link. Worth flagging to Damion.
- The repo's ACJ holdings are unchanged from 2026-08-09: still the same 45
  PDFs in `tests/inputs/ballard/acj/`. Only documentation (`ACJ_HOLDINGS.md`)
  was updated, not source files.
- `ACJ_HOLDINGS.md` now fully accounts for all 7 sections listed on the hub
  page — nothing left to crawl there unless ACJ publishes new content.

## Methodology

For each sub-archive URL:

1. Downloaded the raw page HTML with `curl` (not just the WebFetch
   AI-summarized view, which can silently drop content).
2. Grepped the raw HTML for `href="..."` .pdf` links — a hard, mechanical
   check independent of what any summary might miss.
3. Where zero PDFs were found, extracted the actual `<h3>`/`<h4>` heading
   structure and `<li><a>` article links directly from the HTML to build an
   accurate section-by-section article inventory (rather than trusting a
   possibly-truncated AI summary).
4. Logged findings into `tests/inputs/ballard/acj/ACJ_HOLDINGS.md`, in the
   same style as the existing Legal/Financial Archive entries, and committed
   to `my-new-branch` (not `main`, consistent with how the original ACJ pull
   was handled).

## Findings by sub-archive

### 1. Public Claims & Narratives

**URL:** `.../public-claims-narratives/`
**Result:** 0 PDFs. Pure narrative/commentary section.

Categories: Sound of Freedom & Media Narratives · Rescue Claims & Mission
Narratives · Trafficking Statistics & Public Messaging · Faith, Mission, and
Divine Calling · Fundraising Narratives · Media, Influencers & Celebrity
Support.

17 linked articles logged by title in `ACJ_HOLDINGS.md` (not pulled — hosted
directly on americancrimejournal.com). Two of them ("The Arrest of Earl
Venton Buchanan" and the LVMPD task force piece) duplicate titles already
logged elsewhere on the hub — same article, cross-linked from multiple
sections, not a distinct document.

### 2. Accountability & Scrutiny

**URL:** `.../accountability-scrutiny/`
**Result:** 0 PDFs. Pure narrative/commentary section.

Seven categories, ~38 linked articles total, all logged by title and
category in `ACJ_HOLDINGS.md`:

- Internal Complaints & Whistleblowers (7 articles)
- Organizational Conduct & Leadership (9 articles)
- Sexual Misconduct & Survivor Allegations (6 articles)
- Institutional & Partner Responses (5 articles)
- Law Enforcement & Expert Concerns (5 articles)
- LDS Church Response (5 articles)
- Media Investigations & Public Scrutiny (6 articles)

Several titles overlap with Legal Archive's, Financial Archive's, and Public
Claims & Narratives' "not pulled" lists (e.g. the LDS Church denouncement
piece, the VICE/"Liliana" piece) — same articles cross-referenced from
multiple sub-archives, not new documents.

### 3. The Whiteboard Meeting

**URL:** `.../the-whiteboard-meeting/`
**Result:** 0 PDFs. Single long-form narrative piece by Lynn Packer.

Reconstructs (in prose, not as a scanned/photographed original) a whiteboard
diagram Ballard allegedly drew at a private August 2019 meeting, describing
non-profit/for-profit money flows, LDS-influence plans, and the Foyer de
Sion orphanage (Haiti) angle. No image of the actual whiteboard is
embedded or linked on the page.

Named entities extracted for cross-referencing (not independently verified):

- **Slave Stealers, LLC** (for-profit) — partners: Brian Norton, Tim
  Ballard, M. Russell Ballard (silent partner)
- Ballard-controlled non-profits: Operation Underground Railroad, The
  Nazarene Fund, Children Need Families (Katherine Ballard), Liberty and
  Light Equity Trust, Mercury One (Glenn Beck), Foyer de Sion orphanage
- Foyer de Sion staff named: Brad Damon (CEO), Hada Vanessa (Executive),
  Kahea (advisor)

A "Resources & Further Reading" section links 6 **external** (off-ACJ)
sources — Wikipedia, CharityWatch, Child Liberation Foundation's own site,
Looper, Vice, Vanity Fair — logged for reference but not archived locally
since they're off-site.

### 4 & 5. People / Organizations & Network — not actually live

**Result:** no working link exists for either.

The hub page (`.../operation-underground-railroad-o-u-r/`) has headings,
descriptive text, and bullet lists for both:

- **People** — "Profiles of key individuals connected to O.U.R.,
  investigations, litigation, and related organizations," naming Tim
  Ballard, Sean Reyes, Paul Hutchinson, Dave Lopez, Jon Lines, Carlos
  Rodriguez, M. Russell Ballard.
- **Organizations & Network** — "Examining the broader ecosystem
  surrounding O.U.R.," naming Operation Underground Railroad, Aerial
  Recovery, Child Liberation Foundation, Nazarene Fund, Mercury One, Angel
  Studios.

Each is followed by an `[Explore People]` / `[Explore Organizations]`
button — but checking the raw page HTML directly, those two buttons are
plain `<h4>` text with **no `<a href>` wrapper at all**, unlike every other
section's "Explore" button (e.g. `[Explore The Whiteboard Meeting]`, which
does have a working link to its page). This isn't a crawl failure on my
end — the pages are not published/linked anywhere on the site as of
2026-08-10. **This is the item worth telling Damion about.**

## Current state of `tests/inputs/ballard/acj/`

Unchanged from the 2026-08-09 pull: 45 PDFs (Legal Archive + Financial
Archive), plus `ACJ_HOLDINGS.md` and `acj_downloads_manifest.json`. No files
added this session — only `ACJ_HOLDINGS.md` was edited, to add the three new
"crawled, nothing to pull" sections and the "People/Orgs not live" note.

## Git

Committed to `my-new-branch` (not pushed to `main`, matching the original
pull):

```
869ba58 Document ACJ Public Claims, Accountability, and Whiteboard Meeting sub-archives
 1 file changed, 177 insertions(+), 13 deletions(-)
```

## Open items

- If Damion publishes the People / Organizations & Network pages later,
  those still need crawling.
- No other gaps identified — all 7 sections listed on the ACJ hub are now
  accounted for in `ACJ_HOLDINGS.md`.

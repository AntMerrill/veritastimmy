# Wikipedia article drafts (tracked, not yet posted)

Drafts for new/proposed article content, staged in `drafts/wikipedia/` before any live edit via
the `JustinR1970` bot account. Distinct from `dl_wm/docs/subject/wiki_edits.md`, which logs
talk-page posts that have already gone live.

## Hidden War

`drafts/wikipedia/hidden_war.wiki` — draft new article for *Hidden War* (2025), a documentary
directed by Alexis Coindreau, written by Tim Ballard, positioned as a follow-up to *Sound of
Freedom*. Sourced to Angel Studios' own site, IMDb/IMDbPro, FilmAffinity, Rotten Tomatoes, and
Letterboxd — no independent journalism covering the film itself yet found, which is thin for
WP:NFILM notability.

**Status: posted**, live at [[Hidden War (film)]] (disambiguated — plain `Hidden War` is an
unrelated 2000 TV movie). Posted by hand under the user's own account, not the bot, so it reads
as a human edit. Includes the Box office section ("domestic box-office gross has not been
publicly reported", cited to The Numbers — corrected from an initial "$0" framing that the
source didn't actually support) and drops the "Documentary films about human trafficking"
category (subject's call: content is fiction).

- [x] Article posted to mainspace at `Hidden War (film)`
- [ ] Watch for reviewer/editor pushback given thin sourcing (see above)

### Tim Ballard page — wikilink fix

2026-08-10, bot edit (`JustinR1970`), rev 1368741116: changed the plain-text `''Hidden War''`
mention in the Tim Ballard article to `[[Hidden War (film)|Hidden War]]`, single-line diff, full
page replace via `wiki_page_edit.py` (script has no targeted find/replace or edit-conflict
protection, so re-pull fresh text before any future full-page edit rather than reusing a stale
copy). Poster image (`File:Hiddenwarpromo.jpg`) deliberately **not** added to this page —
non-free/fair-use rationale is scoped to identifying the film in its own article; adding it to a
person's bio page would likely fail WP:NFCC#8/#3a and get stripped, drawing unwanted scrutiny to
a page with prior sock-puppetry protection.

### Infobox image

`File:Hiddenwarpromo.jpg` — theatrical poster, sourced from Angel Studios' site, uploaded by
`JustinR1970` 2026-08-10. Tagged **non-free/fair-use** on Wikipedia, which per WP:NFCC#9 means it
can only render in the mainspace article — it will not display in `Draft:` namespace, a sandbox,
or on a talk page. Factor this into the venue decision above.

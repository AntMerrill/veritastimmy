# "Backfire" claim check: "Wikipedia removed articles... same day" — false, per Wikipedia's own public edit history

## The claim

From `youtube__GvJP_6bcvq4` (~00:29:35, per the transcript, also referenced
in `veritastimmy/docs/TODO.md`): Ballard says Wikipedia "has now removed
articles promoting Tim Ballard and the nonprofit he founded, Operation
Underground Railroad," and that this happened "on the same day the
Church released" its November 6, 2025 statement (the statement's date is
independently confirmed by the live article's own citation — see below).

## The check

Wikipedia's revision history is public, timestamped, and permanent —
every edit to every article is independently checkable by anyone via
`Special:History` or the API, no login or special access needed. Checked
the three articles most plausibly meant by "articles promoting Tim
Ballard and O.U.R.": **Tim Ballard**, **Operation Underground Railroad**,
and **Sound of Freedom (film)**.

**None of the three have a single edit anywhere near November 6, 2025:**

| Article | Last edit before Nov 6, 2025 | Next edit after |
|---|---|---|
| [Tim Ballard](https://en.wikipedia.org/wiki/Tim_Ballard) | [Sep 26, 2025](https://en.wikipedia.org/w/index.php?title=Tim_Ballard&oldid=1313467240) | [Nov 13, 2025](https://en.wikipedia.org/w/index.php?title=Tim_Ballard&oldid=1321888391) — **7-week gap spanning the claimed date** |
| [Operation Underground Railroad](https://en.wikipedia.org/wiki/Operation_Underground_Railroad) | [May 2, 2025](https://en.wikipedia.org/w/index.php?title=Operation_Underground_Railroad&oldid=1288434177) | none found through Nov 20, 2025 — **6+ month gap** |
| [Sound of Freedom (film)](https://en.wikipedia.org/wiki/Sound_of_Freedom_(film)) | [Oct 21, 2025](https://en.wikipedia.org/w/index.php?title=Sound_of_Freedom_(film)&oldid=1317980869) | [Nov 20, 2025](https://en.wikipedia.org/w/index.php?title=Sound_of_Freedom_(film)&oldid=1323168425) — **4-week gap spanning the claimed date** |

Every cell in that table is a direct permalink to a specific, timestamped
revision — reproducible by anyone, not dependent on us.

## Conclusion

The claim doesn't hold up against the record it's about. Not "real event,
recast with spin" (the pattern found in the two earlier-verified claims
in this project — the July 18 court ruling and the Trump/al-Sharaa
Abraham Accords claim) — here, the specific, checkable event ("Wikipedia
removed articles... same day") appears not to have happened at all, on
any of the three most obviously-relevant articles, across windows
ranging from four weeks to over six months surrounding the date in
question.

Two important limits on this finding, stated plainly:

- This checks the **English Wikipedia article history only**. If
  Ballard means a different language Wikipedia, a different specific
  page, a Wikimedia Commons page, or something else entirely by
  "Wikipedia," this check doesn't cover that — the claim is vague
  enough ("articles," no specific page named) that we can't rule out
  every possible referent, only the three most obvious ones.
- The Church's own statement date (November 6, 2025) is itself sourced
  to the Wikipedia article's own citation (Salt Lake Tribune), not
  independently re-verified here — if that date is wrong, the whole
  comparison shifts. Worth a quick independent confirmation of the
  Nov 6 date before using this anywhere public.

## Method note

All data pulled live via the public MediaWiki API
(`en.wikipedia.org/w/api.php`, `action=query&prop=revisions`), no
credentials or special access — anyone can reproduce this exact check.

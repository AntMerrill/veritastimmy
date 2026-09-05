# timballard.org mirror (2026-08-31)

**Location:** `inputs/timballard_org_mirror_2026-08-31/` (gitignored, not in
the public repo — same treatment as the other raw-archive material).
**Method:** `wget --mirror --page-requisites --convert-links -e robots=off`
against `https://timballard.org/`, rate-limited (`--wait=1 --random-wait`),
no `-H`/span-hosts, `--no-parent`. Ran in two passes (first got killed by a
timeout, resumed with `-c`), then manually stripped of spam — see
`tb_org_lawfare_page_2026-08-31.md`'s site-security note for why the domain
had ~240 spam directories in the first place.

## What's captured (97 files, 4.7M, verified no zero-byte/partial files)

- `lawfare-updates/`, `about/`, `donate/`, `events/`, `contact/`, homepage
  — full HTML, all confirmed complete
- `wp-content/` — theme assets + real uploaded images (Ballard's actual
  logo/photo files, e.g. `uploads/2023/05/Tim_Ballard_OUR.jpg`)
- `wp-includes/`, `feed/` — WordPress infrastructure, needed for the pages
  to render if opened locally, not content in their own right

## Links present on the page that were NOT fetched (deliberately, by scope)

The mirror only followed links within `timballard.org` itself. Everything
below was seen on the `lawfare-updates` page but not downloaded:

**7 PDF exhibits, all hosted on a *different subdomain*
(`old140826.timballard.org`, not the mirrored `timballard.org`) — this is
why plain `--no-parent` wget didn't get them, not an oversight:**
- Bree-Righter-Case-Dismissal-2024.06.27.pdf
- Celeste-Borys-Termination-Order-Findings-of-Fact-Conclusions-of-Law-and-Order.pdf
- Complaint-and-Jury-Demand-6-Women-1.pdf
- Complaint-and-Jury-Demand-Davis.pdf
- Kyra-Lynch-Protective-Order-Against-Ballard-Dismissed-2024.08.22.pdf
- Order-Dismissing-Righter-Complaint.pdf
- Righter_UGA-Order.pdf

**12 Google Drive folder links** — the "More Details and Evidence" /
"Full Complaint Document" / "Video Evidence" links for each accuser
section. Not fetched (external host, and Drive folders aren't
wget-mirrorable anyway).

**1 YouTube video** (`youtu.be/36o24dTeoIU`) — almost certainly "Hear
directly from Tim about the Couples Ruse." Not downloaded.

**Social/other external links, not fetched:** facebook.com/officialtimballard,
twitter.com/timballard, instagram.com/timballard89, tbfrescue.org (the
donation-focused sister site, separate from this one).

**~240 spam directories** (`/2025/09/08/...`, casino/gambling SEO
injection) — were fetched initially (that's what made the mirror balloon
to 46M/1,321 files and get killed twice), then deliberately deleted after
the fact. Not part of the kept mirror.

## Not done here

None of the PDFs, Drive folders, or the YouTube video have been fetched or
reviewed. If any of that evidence matters later, it needs its own explicit
pull — this mirror only covers the page text and images already extracted
into `tb_org_lawfare_page_2026-08-31.md`.

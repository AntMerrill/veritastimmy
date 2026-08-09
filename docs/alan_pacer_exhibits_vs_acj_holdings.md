# Alan's PACER Exhibits vs ACJ Holdings

Compares the 13 PDFs supplied by plaintiffs' counsel Alan W. Mortensen
(Mortensen & Milne) — filed as exhibits to the Second Amended Complaint,
Case `2:24-cv-00794-RJS-JCB`, Doc 57 — against American Crime Journal's
independently-pulled O.U.R./Ballard archive (`tests/inputs/ballard/acj/`).
Each matched pair was run through `bin/compare_pdfs.py` (md5 + pdfinfo +
`pdftotext` content diff); full per-pair reports are in
`tests/outputs/pdf_compare/alan_vs_acj/` (gitignored, local only).

## Summary

- **13** PDFs from Alan
- **12** have an ACJ counterpart
- **11 of 12** matches are byte-identical (md5 match, 100% text similarity)
- **1 of 12** differs — Jon Lines Deposition — but only in PACER page-stamp
  boilerplate (doc number, filed date, PageID), not transcript content; see
  [`jon_lines_depo_pacer_vs_acj_summary.md`](jon_lines_depo_pacer_vs_acj_summary.md)
- **1** has no ACJ counterpart at all: `master_timeline_2021_2023_no_ukraine.pdf`

## Matched exhibits

| Alan/PACER file | ACJ file | Result |
|---|---|---|
| Doc 57 Second Amended Complaint for Anti-Trafficking.pdf | Second Amended TVPRA Complaint - Ballard OUR Aerial Recovery.pdf | Identical |
| Doc 57-2 Exh B — Declaration of Aaron Asay.pdf | Declaration of Aaron Asay.pdf | Identical |
| Doc 57-4 Exh D — Declaration of Greg Rogers.pdf | Declaration of Greg Rogers.pdf | Identical |
| Doc 57-5 Exh E — Jon Lines Depo (Redacted).pdf | Jon Lines Deposition.pdf | **Differs** — page-stamp boilerplate only (0.8798 text similarity) |
| Doc 57-3 Exh C — Dr. Dawn Hughes Report.pdf | Dr Dawn Hughes Report.pdf | Identical |
| Doc 57-6 Exh F — JJ Texts (Redacted).pdf | Exhibit F - Text Messages Between Tim Ballard and JJ (Redacted).pdf | Identical |
| Doc 57-12 Exh L — Celeste Borys Statement.pdf | Statement of Celeste Borys.pdf | Identical |
| Doc 57-13 Exh M — Mary Hall Statement.pdf | Statement of Mary Hall.pdf | Identical |
| Doc 57-14 Exh N — Sasha Hightower Statement.pdf | Statement of Sashleigha Hightower.pdf | Identical |
| Doc 57-15 Exh O — Krista Kacey Statement.pdf | Statement of Krista Kacey.pdf | Identical |
| Doc 57-16 Exh P — Kira Lynch Statement.pdf | Statement of Kira Lynch.pdf | Identical |
| Righter-v.-Ballard.pdf | Righter v. Ballard, OUR and Matthew Cooper - Lawsuit.pdf | Identical |

Note: `Statement of Krista Kacey.pdf` was matched, not ACJ's separate
`Declaration of Krista Kacey.pdf` — they're different documents from the
same person; only the Statement has an Alan-side counterpart.

## Unmatched (Alan-only, no ACJ holding)

| File | Notes |
|---|---|
| `master_timeline_2021_2023_no_ukraine.pdf` | No equivalent title in ACJ's Legal or Financial archives; ACJ's five other thematic sub-archives are unreviewed (see `ACJ_HOLDINGS.md`), so this could still surface there later. |

## Bottom line

Alan's exhibit set and the ACJ archive overlap almost completely for the
documents ACJ has pulled so far — 11 of 12 matched files are exact
duplicates, and the 12th (Jon Lines depo) is the same transcript refiled
under a different docket entry. Only the master timeline PDF is unique to
Alan's set within what's been compared.

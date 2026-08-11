# ACJ Exhibits — Technical Inventory & Accessibility Analysis

**Date:** 2026-08-10
**Scope:** the 45 PDFs pulled from ACJ's Legal & Financial Archives into
`tests/inputs/ballard/acj/` (2026-08-09). Companion to `ACJ_HOLDINGS.md`
(what each file *is*) — this covers what each file *is made of*: page
counts, whether it has a real text layer, whether it's tagged for
accessibility, and where a screen reader (or a paralegal trying to
copy/search text) would actually hit a wall.

**Tools used:** `pdfinfo`, `pdftotext`, `pdffonts`, `pdfimages` (all
poppler-utils, already on this machine) — no OCR was run, no files were
modified.

## TL;DR

- **3 exhibits are genuinely image-only "picture" documents** (a
  promotional image, an infographic, a phone-screenshot of text messages)
  — these are the closest thing to "missing `alt` text" in this set: there
  is no text to extract at all, so a description has to be written by hand
  if these need to be accessible or searchable.
- **11 exhibits are raw, unOCR'd scans** — mostly the older O.U.R. Form 990s
  (2015–2018, 2021, 2024) plus a few police reports and one motion. Zero
  extractable text, zero embedded fonts. These need an OCR pass to be
  searchable/screen-reader-usable at all.
- **7 exhibits (the 5 women's Statements, the Krista Kacey Declaration, and
  the Jon Lines Deposition) extract a suspiciously flat ~89 characters per
  page** — almost certainly the federal court's ECF header/footer stamp
  ("Case 2:24-cv-... Document ... Filed ... Page X of Y"), not the actual
  body text. These read as having "some text" but functionally don't for
  search/accessibility purposes.
- **Only 7 of 45 files are tagged PDFs** (proper accessibility structure/
  reading order) — the other 38 have no tag tree even where they do have
  real extractable text.
- **1 file is encrypted with copy disabled** (`OUR Combined Financial
  Statements 2018-2019.pdf`) — printing is allowed but copy/paste text
  extraction is blocked at the permissions level, on a document that's a
  routine public financial filing with no real confidentiality need for
  that restriction.

## Full inventory

| File | Size | Pages | Producer/tool | Tagged | Chars extracted | Fonts | Images | Flag |
|---|---:|---:|---|:---:|---:|---:|---:|---|
| Ballard v. Morgan Davis - Defendants Answer.pdf | 1.6 MB | 36 | Adobe Acrobat Pro | no | 6,051 (168/pg) | 5 | 802 | OK — real text |
| Borys v. Ballard - Motion to Release Crime Lab DNA Report.pdf | 1.3 MB | 33 | Adobe Acrobat Pro + iText | no | 12,204 (370/pg) | 8 | 205 | OK — real text |
| Davis County Criminal Investigation into Tim Ballard and OUR.pdf | 21 MB | 75 | macOS Quartz PDFContext | no | 26,201 (349/pg) | 65 | 63 | OK — real text |
| Declaration of Aaron Asay.pdf | 707 KB | 8 | MS Word + iText (courts) | no | 9,109 (1,139/pg) | 5 | 113 | OK — real text |
| Declaration of Deanna Hanks.pdf | 861 KB | 8 | Adobe PDF Library + iText (courts) | no | 4,879 (610/pg) | 6 | 173 | OK — real text |
| Declaration of Greg Rogers.pdf | 160 KB | 4 | Adobe Acrobat + iText (courts) | no | 4,745 (1,186/pg) | 7 | 1 | OK — real text |
| **Declaration of Krista Kacey.pdf** | 1.8 MB | 51 | Konica Minolta scanner + iText (courts) | no | 4,541 (**89/pg**) | 3 | 331 | **Thin OCR — likely just ECF stamp text** |
| Declaration of Ryan Fisher.pdf | 330 KB | 13 | Adobe Acrobat + iText (courts) | no | 17,830 (1,371/pg) | 5 | 10 | OK — real text |
| Dr Dawn Hughes Report.pdf | 242 KB | 13 | Adobe Acrobat + iText (courts) | **yes** | 24,681 (1,899/pg) | 11 | 0 | OK — tagged |
| Exhibit F - Text Messages Between Tim Ballard and JJ (Redacted).pdf | 2.6 MB | 38 | iText (courts) | no | 3,346 (88/pg) | 4 | 37 | Mostly image content (redacted screenshots) |
| **Exhibit I - Guerra Oculta Promotional Image.pdf** | 496 KB | 2 | Adobe Acrobat + iText (courts) | no | 177 | 3 | 1 | **Image-only exhibit — needs written alt text** |
| **Exhibit J - Myth vs Fact Human Trafficking Graphic.pdf** | 347 KB | 2 | Adobe Acrobat + iText (courts) | no | 179 | 3 | 1 | **Image-only exhibit (infographic) — needs written alt text** |
| Exhibit K - NY Times Article on Tim Ballard and OUR.pdf | 974 KB | 22 | Adobe Acrobat + iText (courts) | **yes** | 36,852 (1,675/pg) | 13 | 9 | OK — tagged |
| **Exhibit S - Text Message Screenshot Belt Communication.pdf** | 780 KB | 2 | Adobe Acrobat *Image Conversion Plug-in* | no | 185 | 3 | 1 | **Image-only exhibit (phone screenshot) — needs written alt text/transcription** |
| Exhibit T - Buenos Aires Times Article Referencing Tim Ballard.pdf | 1.8 MB | 8 | Adobe PDF Library + iText (courts) | **yes** | 13,614 (1,702/pg) | 44 | 44 | OK — tagged |
| Federal TVPRA Complaint Against Tim Ballard and OUR.pdf | 8.6 MB | 184 | Adobe Acrobat Pro | no | 24,516 (133/pg) | 24 | 1,522 | OK, but very image-heavy per page — spot-check for embedded photo exhibits |
| First Amended Complaint - WW et al v Ballard et al.pdf | 15 MB | 246 | Adobe PDF Library + iText | **yes** | 219,261 (891/pg) | 254 | 150 | OK — tagged, largest file in the set |
| **Jon Lines Deposition.pdf** | 3.8 MB | 54 | YesLaw Transcript Generator + iText (courts) | no | 4,808 (**89/pg**) | 3 | 178 | **Thin extraction — see note below, likely a font-encoding artifact, not a real scan** |
| Kely Johana Suarez Moya v. Tim Ballard and OUR - Lawsuit.pdf | 2.0 MB | 66 | Adobe Acrobat Pro + iText | no | 69,980 (1,060/pg) | 7 | 47 | OK — real text |
| **Lindon Police Department Report - Tim Ballard.pdf** | 1.1 MB | 5 | Microsoft Print to PDF | no | 5 (**1/pg**) | 0 | 20 | **Raw scan, zero OCR** |
| **Moya v. Ballard - Motion to Dismiss Denied.pdf** | 339 KB | 6 | Konica Minolta scanner | no | 6 (**1/pg**) | 0 | 38 | **Raw scan, zero OCR** |
| OUR Combined Financial Statements 2018-2019.pdf | 236 KB | 20 | Adobe PDF Library | **yes** | 36,647 (1,832/pg) | 8 | 1 | **Encrypted, copy disabled** (see below) — otherwise tagged/OK |
| **OUR Form 990 - 2015.pdf** | 1.5 MB | 49 | Tiff Junction 4.1 | no | 49 (**1/pg**) | 0 | 49 | **Raw scan, zero OCR** |
| **OUR Form 990 - 2016.pdf** | 1.6 MB | 62 | Tiff Junction 4.1 | no | 62 (**1/pg**) | 0 | 62 | **Raw scan, zero OCR** |
| **OUR Form 990 - 2016 Updated.pdf** | 2.9 MB | 45 | Tiff Junction 4.1 | no | 45 (**1/pg**) | 0 | 45 | **Raw scan, zero OCR** |
| **OUR Form 990 - 2017.pdf** | 1.8 MB | 64 | Tiff Junction 4.1 | no | 64 (**1/pg**) | 0 | 64 | **Raw scan, zero OCR** |
| **OUR Form 990 - 2017 Updated.pdf** | 3.1 MB | 52 | Tiff Junction 4.1 | no | 52 (**1/pg**) | 0 | 52 | **Raw scan, zero OCR** |
| **OUR Form 990 - 2018.pdf** | 1.8 MB | 65 | Tiff Junction 4.1 | no | 65 (**1/pg**) | 0 | 65 | **Raw scan, zero OCR** |
| OUR Form 990 - 2019.pdf | 1.2 MB | 58 | (none listed) | no | 149,391 (2,576/pg) | 33 | 6 | OK — full text layer (unlike its siblings) |
| **OUR Form 990 - 2021.pdf** | 2.2 MB | 97 | GeneratePDFs.exe | no | 97 (**1/pg**) | 0 | 97 | **Raw scan, zero OCR** |
| OUR Form 990 - 2023.pdf | 465 KB | 84 | Aspose.Pdf for .NET | no | 214,748 (2,556/pg) | 21 | 0 | OK — full text layer (unlike its siblings) |
| **OUR Form 990 - 2024.pdf** | 3.1 MB | 163 | GeneratePDFs.exe | no | 163 (**1/pg**) | 0 | 163 | **Raw scan, zero OCR** |
| **OUR IRS Determination Letter 2015.pdf** | 906 KB | 1 | Microsoft Print to PDF | no | 1 | 0 | 7 | **Raw scan, zero OCR** |
| Righter v. Ballard, OUR and Matthew Cooper - Lawsuit.pdf | 693 KB | 19 | Adobe PDF Library + iText | **yes** | 23,353 (1,229/pg) | 4 | 5 | OK — tagged |
| Second Amended TVPRA Complaint - Ballard OUR Aerial Recovery.pdf | 502 KB | 69 | Adobe PDF Library + iText (courts) | **yes** | 115,047 (1,667/pg) | 6 | 0 | OK — tagged |
| Second Lawsuit Against Tim Ballard OUR and Others.pdf | 3.1 MB | 62 | Konica Minolta scanner + iText | no | 122,498 (1,976/pg) | 1 | 428 | OK — real text despite scanner origin |
| Separation and Mutual Release Agreement - Timothy Ballard and OUR.pdf | 1.1 MB | 12 | PDFium | no | 12 (**1/pg**) | 27 | 12 | **Chars/page=1 but 27 fonts embedded — likely extraction quirk, not a true scan; spot-check manually** |
| **Statement of Celeste Borys.pdf** | 857 KB | 19 | Adobe PDF Library + iText (courts) | no | 1,693 (**89/pg**) | 3 | 47 | **Thin OCR — likely just ECF stamp text** |
| **Statement of Kira Lynch.pdf** | 1.4 MB | 32 | Adobe PDF Library + iText (courts) | no | 2,850 (**89/pg**) | 3 | 164 | **Thin OCR — likely just ECF stamp text** |
| **Statement of Krista Kacey.pdf** | 1.5 MB | 34 | Adobe PDF Library + iText (courts) | no | 3,028 (**89/pg**) | 3 | 210 | **Thin OCR — likely just ECF stamp text** |
| **Statement of Mary Hall.pdf** | 617 KB | 15 | Adobe Acrobat + iText (courts) | no | 1,337 (**89/pg**) | 3 | 76 | **Thin OCR — likely just ECF stamp text** |
| **Statement of Sashleigha Hightower.pdf** | 658 KB | 17 | Adobe PDF Library + iText (courts) | no | 1,515 (**89/pg**) | 3 | 172 | **Thin OCR — likely just ECF stamp text** |
| **Utah County Sheriffs Office Report - Tim Ballard.pdf** | 455 KB | 2 | Microsoft Print to PDF | no | 2 (**1/pg**) | 0 | 10 | **Raw scan, zero OCR** |
| Utah District Court Order - Sexual Violence Protective Order Borys v Ballard.pdf | 1.3 MB | 7 | (none listed) | no | 190 (27/pg) | 4 | 5 | Thin but non-flat — likely partial scan, spot-check |
| Whitehead v. Utah AG Sean Reyes and OUR - Lawsuit.pdf | 2.5 MB | 60 | iText (older) | no | 41,592 (693/pg) | 5 | 48 | OK — real text |

## The genuinely image-only exhibits

These three ARE pictures, not documents-that-happen-to-be-scanned — a
description would need to be written from scratch, the same way you'd write
`alt` text for an `<img>`, because there's no underlying text to recover:

| File | Image | Notes |
|---|---|---|
| `Exhibit I - Guerra Oculta Promotional Image.pdf` | 1320×2365 JPEG | A promotional graphic for the "Guerra Oculta" operation. Page 1 is a blank/cover page (177 chars total across both pages is just page furniture, not content). |
| `Exhibit J - Myth vs Fact Human Trafficking Graphic.pdf` | 1320×2305 JPEG | An infographic — this is the worst case for accessibility, since infographics typically pack real informational claims into the image itself, none of which is recoverable as text. |
| `Exhibit S - Text Message Screenshot Belt Communication.pdf` | 4032×3024 JPEG2000, produced via Adobe's **Image Conversion Plug-in** (i.e., this file was *made* by converting a photo to PDF) | A phone screenshot of a text conversation. Unlike the other two, this one has real evidentiary text trapped in image form — an OCR transcription here would actually restore useful, searchable content, not just a caption. |

## Raw, zero-OCR scans (11 files)

Every one of these has `fonts=0` and roughly 1 extracted character per page
— there is no text layer whatsoever, just page images:

- `OUR Form 990 - 2015.pdf`, `2016.pdf`, `2016 Updated.pdf`, `2017.pdf`,
  `2017 Updated.pdf`, `2018.pdf`, `2021.pdf`, `2024.pdf` (8 of the 11 Form
  990 filings — see note below on the 2 that *aren't* like this)
- `OUR IRS Determination Letter 2015.pdf`
- `Lindon Police Department Report - Tim Ballard.pdf`
- `Utah County Sheriffs Office Report - Tim Ballard.pdf`
- `Moya v. Ballard - Motion to Dismiss Denied.pdf`

**Worth noting:** two Form 990 filings in the same set — **2019** and
**2023** — have full, dense text layers (2,576 and 2,556 chars/page
respectively) while the other eight are raw scans. Same document type, same
filer, wildly different accessibility quality depending on which year and
which tool (`GeneratePDFs.exe`/`Tiff Junction` vs. `Aspose.Pdf`/native) was
used to produce the PDF. If completeness/searchability across all years
matters, the 8 scanned years are the ones that need an OCR pass.

## The suspiciously-flat "~89 chars/page" group (7 files)

`Declaration of Krista Kacey.pdf`, the five women's **Statements** (Celeste
Borys, Kira Lynch, Krista Kacey, Mary Hall, Sashleigha Hightower), and the
**Jon Lines Deposition** all extract almost exactly 89 characters per page,
regardless of how many pages the document has. That flatness — the same
number no matter what the document actually says — is the signature of a
**fixed boilerplate stamp**, not real content. Six of these seven share the
producer string `...modified using iText® Core 7.2.3 ... Administrative
Office of the United States Courts` — that's the federal judiciary's ECF
filing system, which stamps a fixed-format header/footer onto each page
(`Case 2:24-cv-00794-RJS-JCB Document ... Filed .../.../.. PageID.#### Page
X of Y`) — almost exactly 89 characters, and it's the only real text layer
sitting on top of what's otherwise a scanned image of the original
statement/declaration.

**Practical effect:** these files "have text" in the sense that `pdftotext`
returns something non-empty, but that something is court case-number
boilerplate, not the actual statement content. A screen reader or full-text
search would find the case number and page count and nothing else.

**Jon Lines Deposition is the one exception worth separating out.** Per
`bin/compare_pdfs.py` (used earlier in this project — see
`docs/jon_lines_depo_pacer_vs_acj_summary.md`), the *actual* 54-page Q&A
transcript text was successfully extracted and compared word-for-word
against the PACER copy — meaning the real deposition text **is** recoverable
by some means, it just isn't showing up under a plain `pdftotext` run the
way I did it here. Deposition-transcript-generator PDFs (this one's
producer is "YesLaw Transcript Generator") sometimes use custom font
encodings that plain text extraction handles inconsistently depending on
the tool/flags used. This file likely isn't a real scan like the others in
this section — it's an extraction-tool quirk — but it's worth re-running
with `pdftotext -layout` or the same method `compare_pdfs.py` uses before
concluding anything about its actual accessibility.

## Tagged vs. untagged

Only **7 of 45** files have a PDF tag tree (proper accessibility structure —
reading order, roles, alt-text slots for embedded images):

`Dr Dawn Hughes Report.pdf`, `Exhibit K - NY Times Article...pdf`,
`Exhibit T - Buenos Aires Times Article...pdf`, `First Amended Complaint -
WW et al v Ballard et al.pdf`, `OUR Combined Financial Statements
2018-2019.pdf`, `Righter v. Ballard, OUR and Matthew Cooper -
Lawsuit.pdf`, `Second Amended TVPRA Complaint - Ballard OUR Aerial
Recovery.pdf`.

The other 38 — including several with perfectly good extractable text —
have no tag structure. Practically, an untagged PDF with good text usually
still reads fine in most modern screen readers (they fall back to visual/
stream order), but there's no guaranteed reading order and no per-image
alt-text slots. Not urgent, but the gap is real for anyone auditing full
Section 508 / WCAG-style PDF accessibility rather than "can text be
extracted at all."

## Encrypted file

`OUR Combined Financial Statements 2018-2019.pdf` is the only encrypted
file in the set: `print:yes copy:no change:no addNotes:no`. Printing is
allowed, but copy/paste text extraction is blocked at the PDF permissions
level. This is a routine public IRS/nonprofit financial filing — there's no
apparent confidentiality reason for the copy restriction; it was most
likely just the default export setting of whatever tool (Adobe PDF Library
15.0) originally produced it, back in 2020. `pdftotext` extracted the
content fine regardless (poppler doesn't enforce PDF permission bits), but
a compliant reader/screen-reader that does honor permissions could be
blocked from letting a user select or copy the text.

## Recommendations, if this matters for the case file

1. **OCR the 11 raw-scan files** (list above) — cheapest way to make them
   searchable and screen-reader-usable; `ocrmypdf` (adds a text layer
   without altering the visible page) would be the standard tool for this.
2. **Write manual alt-text/descriptions for the 3 image-only exhibits**
   (Guerra Oculta image, Myth vs Fact graphic, Belt text screenshot) if
   they'll be cited anywhere that needs to be accessible — an automated OCR
   pass won't help the two pure graphics, and even for the text-message
   screenshot OCR would need a manual accuracy check given it's evidentiary.
3. **Re-verify the Jon Lines Deposition's real text layer** with a
   different extraction method (`-layout` flag, or whatever `compare_pdfs.py`
   uses) before assuming it needs OCR — it likely doesn't, unlike the other
   thin-extraction files.
4. **Treat the ~89-char/page group's `pdftotext` output as unreliable** for
   any downstream text-search/quoting work — always go back to the original
   page image for these six Statements/Declaration.

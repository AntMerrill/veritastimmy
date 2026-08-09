#!/usr/bin/env python3
"""
Compare two PDFs: md5 checksum, pdfinfo metadata, and pdftotext content diff.
Writes a markdown report.

Requires poppler-utils (`pdfinfo`, `pdftotext`) on PATH.

Examples:
  # write report to tests/outputs/pdf_compare/<a-stem>_vs_<b-stem>.md
  python3 bin/compare_pdfs.py file_a.pdf file_b.pdf

  # custom labels + output path
  python3 bin/compare_pdfs.py file_a.pdf file_b.pdf \\
      --label-a "PACER" --label-b "ACJ" \\
      --out tests/outputs/pdf_compare/jon_lines_depo.md

  # print report to stdout instead of writing a file
  python3 bin/compare_pdfs.py file_a.pdf file_b.pdf --stdout
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "lib"))

from pdf_utils import PdfToolError, compare_pdfs, render_markdown_report  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("pdf_a", help="Path to the first PDF")
    parser.add_argument("pdf_b", help="Path to the second PDF")
    parser.add_argument("--label-a", default=None, help="Friendly name for A (default: filename)")
    parser.add_argument("--label-b", default=None, help="Friendly name for B (default: filename)")
    parser.add_argument(
        "--out",
        default=None,
        help="Output .md path (default: tests/outputs/pdf_compare/<a-stem>_vs_<b-stem>.md)",
    )
    parser.add_argument(
        "--stdout", action="store_true", help="Print the report to stdout instead of writing a file"
    )
    parser.add_argument(
        "--diff-limit", type=int, default=200, help="Max diff lines to embed in the report (default 200)"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_a, pdf_b = Path(args.pdf_a), Path(args.pdf_b)

    try:
        result = compare_pdfs(pdf_a, pdf_b, args.label_a, args.label_b)
    except PdfToolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

    report = render_markdown_report(result, diff_limit=args.diff_limit)

    if args.stdout:
        print(report)
        return

    out_path = (
        Path(args.out)
        if args.out
        else Path("tests/outputs/pdf_compare") / f"{pdf_a.stem}_vs_{pdf_b.stem}.md"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report)
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()

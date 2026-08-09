"""PDF comparison helpers: checksums, pdfinfo metadata, and pdftotext content diff.

Shells out to poppler-utils (`pdfinfo`, `pdftotext`) rather than adding a PDF
parsing dependency to requirements.txt — both are already present on this
machine.
"""

from __future__ import annotations

import difflib
import hashlib
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional


class PdfToolError(RuntimeError):
    pass


def _require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise PdfToolError(
            f"'{name}' not found on PATH (poppler-utils). Install it, e.g. "
            f"'sudo apt install poppler-utils'."
        )


def md5sum(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def pdf_info(path: Path) -> Dict[str, str]:
    _require_tool("pdfinfo")
    out = subprocess.run(
        ["pdfinfo", str(path)], capture_output=True, text=True, check=True
    ).stdout
    info: Dict[str, str] = {}
    for line in out.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            info[key.strip()] = value.strip()
    return info


def pdf_text(path: Path) -> str:
    _require_tool("pdftotext")
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        capture_output=True, text=True, check=True,
    ).stdout


def compare_pdfs(
    path_a: Path,
    path_b: Path,
    label_a: Optional[str] = None,
    label_b: Optional[str] = None,
) -> Dict:
    path_a, path_b = Path(path_a), Path(path_b)
    label_a = label_a or path_a.name
    label_b = label_b or path_b.name

    md5_a, md5_b = md5sum(path_a), md5sum(path_b)
    info_a, info_b = pdf_info(path_a), pdf_info(path_b)
    text_a, text_b = pdf_text(path_a), pdf_text(path_b)
    lines_a, lines_b = text_a.splitlines(), text_b.splitlines()

    diff = list(
        difflib.unified_diff(lines_a, lines_b, fromfile=label_a, tofile=label_b, lineterm="")
    )

    return {
        "path_a": path_a,
        "path_b": path_b,
        "label_a": label_a,
        "label_b": label_b,
        "size_a": path_a.stat().st_size,
        "size_b": path_b.stat().st_size,
        "md5_a": md5_a,
        "md5_b": md5_b,
        "identical": md5_a == md5_b,
        "info_a": info_a,
        "info_b": info_b,
        "text_similarity": difflib.SequenceMatcher(None, text_a, text_b).ratio(),
        "diff_lines": diff,
    }


_METADATA_FIELDS = ["Pages", "Producer", "Creator", "CreationDate", "ModDate", "PDF version"]


def render_markdown_report(result: Dict, diff_limit: int = 200) -> str:
    a, b = result["label_a"], result["label_b"]
    lines: List[str] = []

    lines.append(f"# PDF Comparison: {a} vs {b}")
    lines.append("")
    lines.append(f"- **A:** `{result['path_a']}`")
    lines.append(f"- **B:** `{result['path_b']}`")
    lines.append("")
    lines.append(f"**Verdict:** {'IDENTICAL (md5 match)' if result['identical'] else 'NOT identical'}"
                 f" — text similarity {result['text_similarity']:.4f}")
    lines.append("")

    lines.append("## Files")
    lines.append("")
    lines.append("| | A | B |")
    lines.append("|---|---|---|")
    lines.append(f"| Size (bytes) | {result['size_a']:,} | {result['size_b']:,} |")
    lines.append(f"| md5 | `{result['md5_a']}` | `{result['md5_b']}` |")
    lines.append("")

    lines.append("## Metadata (pdfinfo)")
    lines.append("")
    lines.append("| Field | A | B | Match |")
    lines.append("|---|---|---|---|")
    info_a, info_b = result["info_a"], result["info_b"]
    for field in _METADATA_FIELDS:
        va, vb = info_a.get(field, ""), info_b.get(field, "")
        mark = "✓" if va == vb else "✗"
        lines.append(f"| {field} | {va} | {vb} | {mark} |")
    lines.append("")

    lines.append("## Text Diff (pdftotext -layout)")
    lines.append("")
    diff_lines = result["diff_lines"]
    if not diff_lines:
        lines.append("No text differences.")
    else:
        shown = diff_lines[:diff_limit]
        lines.append("```diff")
        lines.extend(shown)
        lines.append("```")
        if len(diff_lines) > diff_limit:
            lines.append("")
            lines.append(
                f"_Truncated: {len(diff_lines)} diff lines total, showing first {diff_limit}._"
            )
    lines.append("")

    return "\n".join(lines)

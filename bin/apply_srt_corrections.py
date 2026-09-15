#!/usr/bin/env python3
"""Apply hand-verified corrections to the Backfire master SRT and show the diff.

Corrections are logged in docs/srt_corrections.json, one entry per fix, each
naming the exact cue (by start timestamp) and its exact original text. This
script never guesses: if a correction's cue_original doesn't match the master
SRT exactly, it errors instead of applying a partial/wrong fix.

Output: a corrected copy of the SRT (never touches the master), plus a
unified diff of every change applied so far.
"""
import difflib
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MASTER_SRT = Path(
    "/run/media/hogan/E769-0C67/boner_vault/dl_wm_outputs/2026-09-07/"
    "youtube__pBo_2DYxfrY/minute_chunks/youtube__pBo_2DYxfrY_master_stitched_patched.srt"
)
CORRECTIONS_JSON = REPO / "docs" / "srt_corrections.json"
OUTPUT_SRT = REPO / "corrections" / "youtube__pBo_2DYxfrY_master_corrected.srt"
DIFF_OUT = REPO / "corrections" / "srt_corrections_diff.txt"

CUE_RE = re.compile(r"^(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)$")


def parse_srt(path):
    """Return list of [index_line, timing_line, text_line, ...] blocks, each a list of raw lines."""
    text = path.read_text(encoding="utf-8")
    blocks = text.strip("\n").split("\n\n")
    return [b.split("\n") for b in blocks]


def main():
    if not MASTER_SRT.exists():
        sys.exit(f"master SRT not found: {MASTER_SRT}")

    corrections = json.loads(CORRECTIONS_JSON.read_text(encoding="utf-8"))
    blocks = parse_srt(MASTER_SRT)

    applied = 0
    for c in corrections:
        match = None
        for block in blocks:
            if len(block) < 3:
                continue
            m = CUE_RE.match(block[1])
            if not m:
                continue
            if m.group(1) == c["timestamp"] and block[2] == c["cue_original"]:
                match = block
                break
        if match is None:
            sys.exit(
                f"correction id={c['id']} did not match: "
                f"timestamp={c['timestamp']!r} original={c['cue_original']!r} "
                f"-- master SRT text differs or timestamp not found, refusing to apply"
            )
        match[2] = c["cue_corrected"]
        applied += 1

    OUTPUT_SRT.parent.mkdir(parents=True, exist_ok=True)
    corrected_text = "\n\n".join("\n".join(b) for b in blocks) + "\n"
    OUTPUT_SRT.write_text(corrected_text, encoding="utf-8")

    original_lines = MASTER_SRT.read_text(encoding="utf-8").splitlines(keepends=True)
    corrected_lines = corrected_text.splitlines(keepends=True)
    diff = difflib.unified_diff(
        original_lines, corrected_lines,
        fromfile=str(MASTER_SRT), tofile=str(OUTPUT_SRT),
    )
    diff_text = "".join(diff)
    DIFF_OUT.write_text(diff_text or "(no differences)\n", encoding="utf-8")

    print(f"applied {applied}/{len(corrections)} correction(s)")
    print(f"corrected SRT: {OUTPUT_SRT}")
    print(f"diff: {DIFF_OUT}")


if __name__ == "__main__":
    main()

#!/bin/bash
set -euo pipefail

# Generates a markdown exhibit doc from tpl/exhibit.md.tpl.
#
# Usage: new_exhibit.sh [run_dir] [doc_basename] [title] [author] [date]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

RUN_DIR="${1:-exhibits}"
DOC_BASENAME="${2:-exhibit}"
TITLE="${3:-Exhibit}"
AUTHOR="${4:-}"
DATESTR="${5:-$(date +"%B %Y")}"

OUT_MD="$RUN_DIR/${DOC_BASENAME}.md"
LOG_DIR="$RUN_DIR/_logs"
LOG_FILE="$LOG_DIR/new_exhibit.log"

mkdir -p "$RUN_DIR" "$LOG_DIR"

export VAR_TITLE="$TITLE"
export VAR_AUTHOR="$AUTHOR"
export VAR_DATE="$DATESTR"
export VAR_SLUG="$DOC_BASENAME"

envsubst < "$REPO_ROOT/tpl/exhibit.md.tpl" > "$OUT_MD"

{
  echo "---- $(date -u +"%Y-%m-%dT%H:%M:%SZ") ----"
  echo "run_dir=$RUN_DIR"
  echo "doc_basename=$DOC_BASENAME"
  echo "output_md=$OUT_MD"
  echo "title=$TITLE"
  echo "author=$AUTHOR"
  echo "date=$DATESTR"
} >> "$LOG_FILE"

echo "[new_exhibit] Wrote: $OUT_MD"
echo "[new_exhibit] Logged: $LOG_FILE"

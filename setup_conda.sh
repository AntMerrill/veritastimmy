#!/bin/bash
set -euo pipefail

ENV_NAME="${1:-veritastimmy}"
PYTHON_VERSION="${2:-}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ALIAS_SOURCE_FILE="$REPO_ROOT/conf/aliases.sh"
TARGET_ALIAS_FILE="$HOME/.veritastimmy_aliases"

if ! command -v conda >/dev/null 2>&1; then
  echo "❌ Conda not found. Install Miniconda/Anaconda and re-run this script." >&2
  exit 1
fi

CONDA_BASE="$(conda info --base)"
# shellcheck disable=SC1090
source "$CONDA_BASE/etc/profile.d/conda.sh"

if conda env list | awk '{print $1}' | grep -qx "$ENV_NAME"; then
  echo "✅ Conda env '$ENV_NAME' already exists."
else
  if [[ -n "$PYTHON_VERSION" ]]; then
    conda create -y -n "$ENV_NAME" "python=$PYTHON_VERSION"
  else
    conda create -y -n "$ENV_NAME" python
  fi
fi

conda activate "$ENV_NAME"

if [[ -f "$REPO_ROOT/requirements.txt" ]]; then
  pip install --upgrade pip
  pip install -r "$REPO_ROOT/requirements.txt"
else
  echo "⚠️ requirements.txt not found; skipping pip install."
fi

if [[ -f "$ALIAS_SOURCE_FILE" ]]; then
  if [[ -f "$TARGET_ALIAS_FILE" ]] && ! cmp -s "$ALIAS_SOURCE_FILE" "$TARGET_ALIAS_FILE"; then
    BACKUP_FILE="$TARGET_ALIAS_FILE.bak.$(date +%Y%m%d%H%M%S)"
    cp "$TARGET_ALIAS_FILE" "$BACKUP_FILE"
    echo "✅ Backed up existing aliases to $BACKUP_FILE"
  fi
  cp "$ALIAS_SOURCE_FILE" "$TARGET_ALIAS_FILE"
  echo "✅ Aliases written to $TARGET_ALIAS_FILE"
else
  echo "⚠️ Alias source file not found at $ALIAS_SOURCE_FILE"
fi

for SHELL_RC in "$HOME/.bashrc" "$HOME/.zshrc"; do
  if [[ -f "$SHELL_RC" ]]; then
    if ! grep -Fq "# veritastimmy aliases" "$SHELL_RC"; then
      {
        echo ""
        echo "# veritastimmy aliases"
        echo "if [ -f \"$TARGET_ALIAS_FILE\" ]; then"
        echo "  # shellcheck disable=SC1090"
        echo "  source \"$TARGET_ALIAS_FILE\""
        echo "fi"
      } >> "$SHELL_RC"
      echo "✅ Updated $SHELL_RC to source aliases"
    else
      echo "✅ $SHELL_RC already sources aliases"
    fi
  fi
done

echo "✅ Conda environment '$ENV_NAME' is ready."
echo "➡️ Restart your shell or run: source $TARGET_ALIAS_FILE"

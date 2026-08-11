# TODO

- [ ] Finish `bin/continue_tasks.py` — line ~62 has a stub (`# TODO: Replace
      this with actual task function`); it currently just logs "Simulated
      running task" instead of executing `perform_download` /
      `apply_watermark` / `generate_captions` / `post_process`. Wire up real
      task execution.
- [ ] Decide fate of the legacy transcription pipeline (`bin/call_*.py` +
      `lib/*_utils.py`) — flagged in the local (gitignored) `CLAUDE.md` as
      largely superseded by the separate `dl_wm` project but still
      functional. Check `dl_wm` overlap and decide whether to prune.

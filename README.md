# Mimesis – Audio Transcription + Source Comparison Toolkit

## Quickstart

1. Set up environment:
    ./setup_venv.sh

2. Run full transcription:
    ./run.sh data/original.mp4

Outputs:
- Full transcript (.txt)
- Per-minute JSON
- Captions (.srt, .vtt)
- Source article scrape

## Project Structure

bin/        # Scripts (transcribe, captions, etc.)
conf/       # Configs
data/       # Media input
lib/        # Local Python packages
run.sh      # Run the pipeline
setup_venv.sh   # One-line environment setup
requirements.txt

## Wiki Utilities

Use `bin/wiki_lang_pick.py` to list a page's available language versions and
print the selected version's raw wikitext for analysis or comparison.

Examples:
- List language versions:
  `python3 bin/wiki_lang_pick.py "Tim Ballard" --list`
- Pick a version and output raw wikitext:
  `python3 bin/wiki_lang_pick.py "Tim Ballard" --pick 2 --raw`
- Post a note to the talk page (requires credentials JSON):
  `python3 bin/wiki_lang_pick.py "Tim Ballard" --pick 0 --post-talk "Note for editors" --credentials tests/inputs/wiki_credentials.json`
- Post a note to a user's page (requires credentials JSON):
  `python3 bin/wiki_user_post.py "ExampleUser" --message "Hello!" --credentials tests/inputs/wiki_credentials.json`
- Replace a user's page contents (requires credentials JSON):
  `python3 bin/wiki_user_put.py "ExampleUser" --message "Updated content" --credentials tests/inputs/wiki_credentials.json`

Credentials format (JSON):
```json
{
  "username": "YourBotUsername",
  "password": "YourBotPassword"
}
```

To avoid committing secrets, copy `tests/inputs/wiki_credentials.json.example` to
`tests/inputs/wiki_credentials.json` and fill in your real credentials (the
real file is gitignored).

## Configuration

Application defaults live in `conf/app_config.json`.  At runtime
`load_app_config()` also looks for optional per-OS overrides in
`conf/config.json` keyed by the value of `platform.system()`.  When
present, those settings are merged into the base configuration.
The base config now includes a `target_usb` path which download
scripts use as the default mount point for removable storage.

## Requirements

- Python 3.9+
- ffmpeg
- OpenAI Whisper:
    pip install git+https://github.com/openai/whisper.git
- Others:
    pip install -r requirements.txt

## Credits

Developed by BG Bear Guards – March 2025

mimesis/
├── bin/               # CLI scripts
├── conf/              # Configs
├── data/              # Media input
├── lib/
│   └── mimesis/       # Consolidated helper package
├── README.md          # ✔️ Exists
├── requirements.txt   # ✔️ Exists



## Further Reading

For ideas on simplifying the internal modules, see
[`docs/library_consolidation.md`](docs/library_consolidation.md).

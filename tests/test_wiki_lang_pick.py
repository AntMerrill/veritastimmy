from datetime import datetime
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "bin"))

import wiki_lang_pick


def make_persistent_output_dir() -> Path:
    outputs_root = Path(__file__).resolve().parent / "outputs"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = outputs_root / f"run-{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def test_split_wikitext_sections():
    text = "\n".join(
        [
            "Intro line.",
            "",
            "== Heading One ==",
            "Content A",
            "=== Subheading ===",
            "Content B",
        ]
    )
    sections = wiki_lang_pick.split_wikitext_sections(text)
    assert sections[0]["title"] is None
    assert "Intro line." in sections[0]["content"]
    assert sections[1]["title"] == "Heading One"
    assert "Content A" in sections[1]["content"]
    assert sections[2]["title"] == "Subheading"
    assert "Content B" in sections[2]["content"]


def test_write_output_json():
    output_dir = make_persistent_output_dir()
    output_path = wiki_lang_pick.write_output(
        out_dir=output_dir,
        lang="en",
        title="Sample Page",
        text="Lead line\n== Section ==\nBody",
        raw=True,
        json_output=True,
    )
    assert output_path.exists()
    assert output_path.suffix == ".json"
    contents = output_path.read_text()
    assert '"sections"' in contents


def test_main_reports_output_path(monkeypatch, capsys):
    def fake_get_langlinks(session, en_title):
        return {}

    def fake_fetch_wikitext(session, api, title):
        return "Lead line\n== Section ==\nBody"

    monkeypatch.setattr(wiki_lang_pick, "get_langlinks", fake_get_langlinks)
    monkeypatch.setattr(wiki_lang_pick, "fetch_wikitext", fake_fetch_wikitext)
    output_dir = make_persistent_output_dir()
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "wiki_lang_pick.py",
            "Tim Ballard",
            "--pick",
            "0",
            "--json",
            "--out-dir",
            str(output_dir),
        ],
    )

    exit_code = wiki_lang_pick.main()
    captured = capsys.readouterr()

    expected_path = output_dir / "en_tim_ballard.json"
    assert exit_code == 0
    assert captured.out == f"Wrote output to {expected_path}\n"
    assert expected_path.exists()

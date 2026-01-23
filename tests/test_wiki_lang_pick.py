from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "bin"))

import wiki_lang_pick


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


def test_write_output_json(tmp_path):
    output_path = wiki_lang_pick.write_output(
        out_dir=tmp_path,
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

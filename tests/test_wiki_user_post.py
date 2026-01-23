from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "bin"))

import wiki_user_post


def test_build_user_title():
    assert wiki_user_post.build_user_title("ExampleUser") == "User:ExampleUser"
    assert wiki_user_post.build_user_title("User:Sandbox") == "User:Sandbox"


def test_load_credentials(tmp_path):
    creds_path = tmp_path / "creds.json"
    creds_path.write_text('{"username": "bot", "password": "secret"}')
    creds = wiki_user_post.load_credentials(creds_path)
    assert creds["username"] == "bot"
    assert creds["password"] == "secret"

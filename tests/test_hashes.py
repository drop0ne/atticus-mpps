from pathlib import Path

from mpps.packet.hashes import sha256_file


def test_hash_changes_when_file_changes(tmp_path: Path):
    p = tmp_path / "sample.txt"
    p.write_text("a", encoding="utf-8")
    h1 = sha256_file(p)
    p.write_text("b", encoding="utf-8")
    h2 = sha256_file(p)
    assert h1 != h2

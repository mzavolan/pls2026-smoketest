import subprocess, sys
from pathlib import Path

def test_total_is_twelve(tmp_path):
    subprocess.run([sys.executable, "run.py", "--out-dir", str(tmp_path)], check=True)
    assert (tmp_path / "total.txt").read_text().strip() == "12"

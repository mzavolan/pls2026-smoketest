"""Stub project: read a CSV, sum a column, write a result and its provenance."""
import argparse, csv, json, sys
from pathlib import Path

def main(argv=None):
    p = argparse.ArgumentParser(description="Sum the counts column of a tiny dataset.")
    p.add_argument("--data-dir", default="data/raw")
    p.add_argument("--out-dir", default="results")
    a = p.parse_args(argv)
    rows = list(csv.DictReader(open(Path(a.data_dir) / "counts.csv")))
    total = sum(int(r["count"]) for r in rows)
    out = Path(a.out_dir); out.mkdir(parents=True, exist_ok=True)
    (out / "total.txt").write_text(f"{total}\n")
    (out / "run_metadata.json").write_text(json.dumps({"n_rows": len(rows), "total": total}) + "\n")
    print("total:", total)

if __name__ == "__main__":
    main()

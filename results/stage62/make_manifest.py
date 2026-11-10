#!/usr/bin/env python3
"""Create or check deterministic SHA-256 provenance for Stage 62 deliverables."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MANIFEST = HERE / "verification_manifest.json"
FILES = (
    "report.md",
    "summary.md",
    "verify_singular_series.py",
    "verify_singular_series_sage.py",
    "finite_examples.json",
    "sage_verification.json",
    "stage62_verification.json",
    "make_manifest.py",
)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def expected_manifest():
    branch = subprocess.check_output(
        ["git", "-C", str(ROOT), "branch", "--show-current"], text=True
    ).strip()
    base_commit = subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
    ).strip()
    return {
        "stage": 62,
        "branch": branch,
        "base_commit_before_stage62_commit": base_commit,
        "algorithm": "SHA-256 over exact saved file bytes",
        "files": {name: sha256(HERE / name) for name in FILES},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = expected_manifest()
    if args.check:
        actual = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if actual != expected:
            raise SystemExit("verification manifest mismatch")
        print("verification manifest: all listed SHA-256 hashes match")
    else:
        MANIFEST.write_text(json.dumps(expected, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {MANIFEST}")


if __name__ == "__main__":
    main()

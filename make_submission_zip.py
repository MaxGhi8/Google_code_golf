#!/usr/bin/env python3
"""Create a submission.zip from all Python tasks in finals/.

- Collects all files matching finals/*.py
- Writes them into submission.zip at the repository root (overwrite if exists)
- Ensures deterministic ordering (sorted by filename)

Usage:
  python make_submission_zip.py                 # writes submission.zip
  python make_submission_zip.py --output path   # custom output path
  python make_submission_zip.py --dry-run       # show which files would be zipped
"""
from __future__ import annotations

import argparse
import os
import sys
import zipfile
from glob import glob

DEFAULT_OUTPUT = "submission.zip"
FINALS_DIR = "finals"


def list_final_files() -> list[str]:
    pattern = os.path.join(FINALS_DIR, "*.py")
    files = sorted(glob(pattern))
    return files


def make_zip(files: list[str], out_path: str) -> None:
    # Write zip at out_path, storing files with arcname stripped of leading finals/
    with zipfile.ZipFile(out_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for fp in files:
            arcname = os.path.basename(fp)
            zf.write(fp, arcname)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", "-o", default=DEFAULT_OUTPUT, help="Output zip path (default: submission.zip)")
    ap.add_argument("--dry-run", action="store_true", help="Only list the files that would be added")
    args = ap.parse_args()

    if not os.path.isdir(FINALS_DIR):
        print(f"Error: '{FINALS_DIR}/' directory not found.", file=sys.stderr)
        return 1

    files = list_final_files()
    if not files:
        print(f"No Python files found in '{FINALS_DIR}/'. Creating empty zip: {args.output}")
        if not args.dry_run:
            # create empty zip
            with zipfile.ZipFile(args.output, mode="w", compression=zipfile.ZIP_DEFLATED):
                pass
        return 0

    if args.dry_run:
        print("Would create:", args.output)
        print("With files:")
        for f in files:
            print(" -", f)
        return 0

    # Ensure parent directory of output exists
    out_parent = os.path.dirname(os.path.abspath(args.output))
    if out_parent and not os.path.isdir(out_parent):
        os.makedirs(out_parent, exist_ok=True)

    make_zip(files, args.output)
    print(f"Wrote {args.output} with {len(files)} files from '{FINALS_DIR}/'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

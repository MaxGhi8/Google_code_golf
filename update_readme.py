#!/usr/bin/env python3
"""
Wrapper to update README:
- Updates the Bytes column via update_readme_bytes.py
- Updates the Status column via update_readme_status.py

Usage:
  python update_readme_all.py            # run both updates
  python update_readme_all.py --bytes    # only bytes update
  python update_readme_all.py --status   # only status update
  python update_readme_all.py --dry-run  # dry-run for bytes update only (status currently always writes)

Notes:
- --dry-run applies to the bytes updater only (mirrors existing support).
- Order: bytes first, then status.
"""
from __future__ import annotations

import sys


def run_bytes(dry: bool) -> int:
    from update_readme_bytes import process as update_bytes
    print("[1/2] Updating README bytes…", file=sys.stderr)
    rc = update_bytes(dry)
    return rc


def run_status() -> int:
    import update_readme_status as urs
    print("[2/2] Updating README statuses…", file=sys.stderr)
    try:
        best = urs.fetch_best_bytes()
    except Exception as e:
        print(f"Failed to fetch best bytes: {e}", file=sys.stderr)
        return 2
    changed = urs.update_readme_statuses(best)
    print(f"Status updated rows: {changed}", file=sys.stderr)
    return 0


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv
    only_bytes = "--bytes" in argv
    only_status = "--status" in argv

    if only_bytes and only_status:
        print("Cannot use --bytes and --status together", file=sys.stderr)
        return 2

    rc = 0
    if only_status:
        rc = run_status()
    elif only_bytes:
        rc = run_bytes(dry)
    else:
        # default: run bytes then status
        rc = run_bytes(dry)
        if rc == 0:
            rc = run_status()
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

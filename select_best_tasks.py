#!/usr/bin/env python3
"""Select best (shortest in bytes) task implementations.

For every task number 001..400 this script:
    * Looks for compressed/taskNNN.py and tasks/taskNNN.py (if they exist)
    * Chooses the shorter file (byte size). If only one exists, uses it.
    * Copies it to finals/taskNNN.py (overwrites existing).

Tie-breaking:
  * If both exist and have identical byte size, preference order can be
    configured (default: keep existing finals version if present, else prefer
    compressed/, else tasks/). This avoids unnecessary overwrites.

Usage:
  python select_best_tasks.py            # normal run
  python select_best_tasks.py --dry-run  # show decisions only
  python select_best_tasks.py --force    # overwrite even on ties

Exit code is 0 unless an unexpected exception occurs.
"""
from __future__ import annotations

import argparse
import os
import shutil
from dataclasses import dataclass

TASK_RANGE = range(1, 401)
# Candidate source directories in preference order for tie-breaking when --force
FILES_PER_DIR = ["tasks", "compressed", "submission"] # "submission"
# Destination folder containing the chosen best versions
FINALS_DIR = "finals"

@dataclass
class Candidate:
    path: str
    size: int
    source_dir: str


def gather_candidates(task_num: int) -> list[Candidate]:
    name = f"task{task_num:03d}.py"
    out: list[Candidate] = []
    for d in FILES_PER_DIR:
        p = os.path.join(d, name)
        if os.path.isfile(p):
            out.append(Candidate(p, os.path.getsize(p), d))
    return out


def choose_best(cands: list[Candidate], existing_finals: str | None, force: bool) -> Candidate | None:
    if not cands:
        return None
    # Sort primarily by size
    cands_sorted = sorted(cands, key=lambda c: c.size)
    smallest = [c for c in cands_sorted if c.size == cands_sorted[0].size]
    if len(smallest) == 1:
        return smallest[0]

    # Tie handling
    if force:
        # Deterministic: follow FILES_PER_DIR order already implicit in gather order
        for pref in FILES_PER_DIR:
            for c in smallest:
                if c.source_dir == pref:
                    return c
    else:
        # If finals file exists and matches one of the tied candidates' content, keep it
        if existing_finals and os.path.isfile(existing_finals):
            try:
                finals_size = os.path.getsize(existing_finals)
                # If size differs we must pick something anyway (shouldn't happen if tie)
                if finals_size == smallest[0].size:
                    return None  # signal: keep existing finals (no copy)
            except OSError:
                pass
        # Prefer compressed version among ties, else tasks
        for pref in ("compressed", "tasks"):
            for c in smallest:
                if c.source_dir == pref:
                    return c
    # Fallback
    return smallest[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Do not copy, only report decisions")
    ap.add_argument("--force", action="store_true", help="On size ties always pick a source instead of keeping finals")
    args = ap.parse_args()

    copied = 0
    skipped_missing = 0
    kept_ties = 0
    total_considered = 0

    for n in TASK_RANGE:
        name = f"task{n:03d}.py"
        finals_path = os.path.join(FINALS_DIR, name)
        cands = gather_candidates(n)
        if not cands:
            skipped_missing += 1
            print(f"{name}: no source found (skipped)")
            continue
        total_considered += 1
        best = choose_best(cands, finals_path, args.force)
        if best is None:
            kept_ties += 1
            print(f"{name}: tie on size ({cands[0].size} bytes); keeping existing finals")
            continue
        action = "COPY" if not args.dry_run else "WOULD_COPY"
        dst = finals_path
        src = best.path
        # Avoid copying a file onto itself (can happen if destination equals source)
        if os.path.realpath(src) == os.path.realpath(dst):
            print(f"{name}: SKIP (source and destination are the same: {src})")
        else:
            if not args.dry_run:
                os.makedirs(FINALS_DIR, exist_ok=True)
                shutil.copyfile(src, dst)
            copied += 1
            print(f"{name}: {action} from {src} ({best.size} bytes)")
        # If identical path, treat as kept (no change to copied counter)

    print("\nSummary:")
    print(f"Sources with at least one candidate: {total_considered}")
    print(f"Copied / updated finals: {copied}")
    print(f"Kept existing finals on tie: {kept_ties}")
    print(f"Missing entirely: {skipped_missing}")

if __name__ == "__main__":
    main()

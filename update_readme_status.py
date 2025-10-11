#!/usr/bin/env python3
"""
Update README task statuses based on byte counts vs best-known solutions.

Rules:
- "💎 GGWP" if our solution has fewer bytes than the best one
- "🏆 Optimized" if equal to the best one
- "✅ Completed" if at most 50 bytes more than the best
- "👀 Need Review" if more than 50 bytes over the best

Best byte counts are fetched from a published Google Sheet, identical to findiffs.sh.
"""
from __future__ import annotations

import os
import re
import sys
import urllib.request
from html.parser import HTMLParser
import csv
from typing import Dict, List, Optional, Tuple

# Constants
SHEET_URL = (
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pubhtml/sheet?headers=false&gid=1427788625"
)
SHEET_CSV_URL = (
    "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pub?gid=1427788625&single=true&output=csv"
)
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
FINALS_DIR = os.path.join(REPO_ROOT, "finals")
README_PATH = os.path.join(REPO_ROOT, "README.md")
DEFAULT_SIZE_IF_MISSING = 2500
TASK_COUNT = 400

STATUS_GGWP = "💎 GGWP"
STATUS_OPTIMIZED = "🏆 Optimized"
STATUS_COMPLETED = "✅ Completed"
STATUS_REVIEW = "👀 Need Review"


class WaffleThirdColumnParser(HTMLParser):
    """Extract text content of the 3rd <td> of each <tr> in table.waffle.

    Note: Retained for debugging; production path uses CSV export to obtain the
    correct 'BEST' byte counts (2nd column) per task.
    """

    def __init__(self) -> None:
        super().__init__()
        self._in_waffle_stack: List[bool] = []  # track nested tables; True if waffle
        self._in_tr: bool = False
        self._td_index: int = 0
        self._capture: bool = False
        self._buf: List[str] = []
        self.values: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]):
        if tag == "table":
            classes = None
            for k, v in attrs:
                if k == "class":
                    classes = v or ""
                    break
            is_waffle = classes is not None and "waffle" in classes.split()
            self._in_waffle_stack.append(is_waffle)
        elif tag == "tr" and self._in_waffle():
            self._in_tr = True
            self._td_index = 0
        elif tag == "td" and self._in_tr and self._in_waffle():
            self._td_index += 1
            self._capture = self._td_index == 3
            if self._capture:
                self._buf.clear()

    def handle_endtag(self, tag: str):
        if tag == "td" and self._capture:
            self._capture = False
            text = "".join(self._buf).strip()
            self.values.append(text)
            self._buf.clear()
        elif tag == "tr" and self._in_tr:
            self._in_tr = False
            self._td_index = 0
        elif tag == "table":
            if self._in_waffle_stack:
                self._in_waffle_stack.pop()

    def handle_data(self, data: str):
        if self._capture:
            self._buf.append(data)

    def _in_waffle(self) -> bool:
        return any(self._in_waffle_stack) and (self._in_waffle_stack[-1] is True)


def fetch_best_bytes(url_csv: str = SHEET_CSV_URL) -> Dict[int, int]:
    """Fetch best byte counts for tasks 1..TASK_COUNT via CSV export.

    The CSV has rows like: [TASK, BEST, SCORE, ...]. We want BEST (bytes).
    Returns a dict mapping task number -> best byte count.
    """
    with urllib.request.urlopen(url_csv) as resp:
        data = resp.read().decode("utf-8", errors="ignore")
    reader = csv.reader(data.splitlines())
    best: Dict[int, int] = {}
    for row in reader:
        if not row:
            continue
        task_cell = row[0].strip() if len(row) > 0 else ""
        best_cell = row[1].strip() if len(row) > 1 else ""
        # Identify task rows by a 3-digit task number in the first column
        if re.fullmatch(r"\d{3}", task_cell):
            try:
                t = int(task_cell)
            except ValueError:
                continue
            # BEST may include formatting; extract first integer
            m = re.search(r"\d+", best_cell.replace(",", ""))
            if not m:
                continue
            best[t] = int(m.group(0))
    # Ensure we only return known tasks 1..TASK_COUNT
    return {k: v for k, v in best.items() if 1 <= k <= TASK_COUNT}


def solution_size(task_no: int) -> int:
    path = os.path.join(FINALS_DIR, f"task{task_no:03d}.py")
    if os.path.isfile(path):
        try:
            with open(path, "rb") as f:
                return len(f.read())
        except OSError:
            return DEFAULT_SIZE_IF_MISSING
    return DEFAULT_SIZE_IF_MISSING


def status_for(size: int, best: int) -> str:
    if size < best:
        return STATUS_GGWP
    if size == best:
        return STATUS_OPTIMIZED
    if size <= best + 50:
        return STATUS_COMPLETED
    return STATUS_REVIEW


def update_readme_statuses(best_map: Dict[int, int], readme_path: str = README_PATH) -> int:
    """Update README.md status column for each task row.

    Returns number of rows changed.
    """
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"README not found at {readme_path}", file=sys.stderr)
        return 0

    changed = 0
    out_lines: List[str] = []

    # Match markdown rows that start with a task link, e.g.:
    # | [task001.py](task001.py) | ...
    # Capture the three-digit task number once and allow any three digits in the href
    task_row_re = re.compile(r"^\|\s*\[task(\d{3})\.py\]\(task\d{3}\.py\)\s*\|")

    for line in lines:
        m = task_row_re.match(line)
        if not m:
            out_lines.append(line)
            continue
        task_no = int(m.group(1))
        best = best_map.get(task_no)
        if best is None:
            # If no best available, leave line unchanged
            out_lines.append(line)
            continue

        size = solution_size(task_no)
        new_status = status_for(size, best)

        # Split markdown row by '|' and replace the status cell (index 2 in split list)
        parts = line.rstrip("\n").split("|")
        # Ensure we have at least the 5 columns + edges
        if len(parts) < 7:
            out_lines.append(line)
            continue

        # parts example: ['', ' [task001.py](task001.py) ', ' ✅ Completed ', ' 61 ', ' Max, Ale ', '  ', '']
        old_status = parts[2]
        parts[2] = f" {new_status} "
        new_line = "|".join(parts) + "\n"
        if new_line != line:
            changed += 1
        out_lines.append(new_line)

    if changed:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.writelines(out_lines)
    return changed


def main(argv: List[str]) -> int:
    print("Fetching best byte counts from sheet…", file=sys.stderr)
    try:
        best_map = fetch_best_bytes()
    except Exception as e:
        print(f"Failed to fetch or parse sheet: {e}", file=sys.stderr)
        return 2

    print("Updating README statuses…", file=sys.stderr)
    changed = update_readme_statuses(best_map)
    print(f"Done. Updated {changed} task row(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

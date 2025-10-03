#!/usr/bin/env python3
"""Update the Bytes column in README.md for tasks 001-400.

Rules:
- For each taskNNN.py (NNN zero-padded 001..400) present in finals/ directory, compute its size in bytes (raw file byte length).
- In README.md table lines of the form:
  | [taskNNN.py](taskNNN.py) | <status> | <bytes> | ... |
  replace the third column with the current byte length.
- Leave every other part of the README unchanged.
- If a task file is missing, leave that line untouched.

Usage:
  python update_readme_bytes.py            # updates in place
  python update_readme_bytes.py --dry-run  # show planned changes only
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
README=ROOT/"README.md"
FINALS=ROOT/"finals"
TASK_RE=re.compile(r"^\| \[task(\d{3})\.py\]\(task\1\.py\) ")

def task_file(n:str)->Path:
    return FINALS/f"task{n}.py"

def compute_size(p:Path)->int:
    return len(p.read_bytes())

def process(dry:bool=False)->int:
    if not README.exists():
        print("README.md not found",file=sys.stderr);return 1
    lines=README.read_text(encoding='utf-8').splitlines()
    changed=0
    new_lines=[]
    for line in lines:
        m=TASK_RE.match(line)
        if not m:
            new_lines.append(line);continue
        n=m.group(1)
        tf=task_file(n)
        if not tf.exists():
            new_lines.append(line);continue
        # Split markdown table row into columns (strip leading/trailing pipe)
        parts=[p.strip() for p in line.strip().strip('|').split('|')]
        if len(parts)<3:
            new_lines.append(line);continue
        size=compute_size(tf)
        old=parts[2]
        new=str(size)
        if old!=new:
            parts[2]=new
            changed+=1
            outline='| '+' | '.join(parts)+' |'
            if dry:
                print(f"UPDATE task{n}: {old} -> {new}")
            new_lines.append(outline if not dry else line)
        else:
            new_lines.append(line)
    if not dry and changed:
        README.write_text('\n'.join(new_lines)+"\n",encoding='utf-8')
    if dry:
        print(f"Planned updates: {changed}")
    else:
        print(f"Updated rows: {changed}")
    return 0

if __name__=="__main__":
    sys.exit(process('--dry-run' in sys.argv))

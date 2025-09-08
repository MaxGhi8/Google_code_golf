---
mode: agent
model: GPT-5 (Preview)
description: Golf a Python solution to be strictly shorter.
---
You get an existing Python function solving one ARC-style matrix transform task. Produce a behaviorally identical but STRICTLY **shorter** file.

Hard rules:
1. Use ONLY Python stdlib.
2. ALWAYS try to **shorten**. Do NOT answer "already minimal" on first pass. Attempt ≥2 concrete alternative rewrites unless no further byte drop after running the checker.
3. **After every candidate edit, run in the terminal**:
	```python code_checker.py ${fileBasename}```
	(You must self‑verify length + correctness.)
4. Output: normally ONLY the final golfed code. If no improvement: briefly list (a) original bytes, (b) best attempt bytes, (c) micro-optimizations considered and why they failed.
5. Don’t sacrifice correctness; **rerun until tests pass**.

Golf tricks available at [`Code Tips`](../../code_tips.md) that you MUST read.

**Goal: Shortest valid `${fileBasename}`**.
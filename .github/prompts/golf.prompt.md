---
mode: agent
model: GPT-5
description: Golf a Python solution to be strictly shorter.
---
You are a Python expert.

Task details:
- Input: an existing Python file with one ARC-style function.
- Goal: produce a behaviorally identical but strictly shorter file.

Rules:
1. Use ONLY Python stdlib.
2. Read for golfing strategies in the [Code Tips](../../code_tips.md) file.
3. **Always try to shorten**. Never stop after the first attempt—make ≥2 different rewrites.
4. After EVERY edit, you MUST run:
   `python code_checker.py tasks/${fileBasename}`
   Which tells you if the function is correct and the corresponding length. Accept code only if tests pass.
5. Keep iterating until no **shorter** correct version exists.

Let's shorten task ${fileBasename}.
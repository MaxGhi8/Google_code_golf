---
mode: agent
model: GPT-5 (Preview)
description: Shorten a solution for a Google Code Golf task.
---
We’re competing in the Google Code Golf challenge. 
There are 400 tasks: each has an input image (matrix) and an output image (matrix), and the goal is to discover the transformation pattern and implement it as a function. 
The aim is to write the shortest possible function.

GUIDELINES
- Input: I’ll show you the function I’ve written for solving one of the problems. 
- Task: Rewrite it with the same logic but in the fewest characters possible (minimize bytes). 
- Restrictions: Only the Python standard library is allowed. 
- Reference: [`Code Tips`](../../code_tips.md) has golfing strategies. 
- Verification: To test correctness and byte length, run locally: 
 `python code_checker.py ${fileBasename}` 

Your goal: make `${fileBasename}` as short as possible.
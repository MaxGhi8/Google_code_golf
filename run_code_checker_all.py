#! /usr/bin/env python
import os
import subprocess

# Path to the compressed folder
compressed_folder = "./finals"

# Path to the code_checker script
code_checker_script = "./code_checker.py"

# Iterate through all files in the compressed folder
for file_name in os.listdir(compressed_folder):
    if file_name.endswith(".py"):
        file_path = os.path.join(compressed_folder, file_name)
        print(f"Running code_checker for {file_name}...")
        subprocess.run(["python3", code_checker_script, file_path])
        print("\n")

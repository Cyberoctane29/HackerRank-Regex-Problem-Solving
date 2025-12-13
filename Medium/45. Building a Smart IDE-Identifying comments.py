# Problem: Identifying Comments in C / C++ / Java Programs  
# Difficulty: Medium  
# Skills: Python, Regular Expressions (re module), Text Parsing

# Problem Statement:
# You are given the source code of a program written in C, C++, or Java (up to 200 lines).  
# Your job is to extract **only the comments** from the code.
#
# Types of comments to detect:
#
# 1. **Single-line comments**
#       // comment text
#       x = 1; // comment after code
#
# 2. **Multi-line comments**
#       /* comment text */
#       /* This is a multi-line
#          comment example */
#
# Notes and Restrictions:
# - You do NOT need to handle:
#       * nested comments  
#       * multi-line comments inside single-line comments  
#       * single-line comments inside multi-line comments  
# - Preserve the exact line structure of multi-line comments.
# - Remove all leading whitespace before comments.
# - For multi-line comments, remove leading whitespace from *each* line.
#
# Input Format:
# - Entire input is the raw source code (multiple lines).
#
# Output Format:
# - Print each extracted comment in the order they appear.
# - Multi-line comments must retain their internal line structure.
# - No leading or trailing spaces should appear.

# Example:
# Input:
# // hello
# code...
# /* test
#    block */
#
# Output:
# // hello
# /*test
# block */


# Solution

import sys
import re

text = ''.join(sys.stdin)

# Regex matches:
#   //...            (single-line comment)
#   /* ... */        (multi-line comment, non-greedy, spanning across lines)
pattern = r'//.*|/\*[\s\S]*?\*/'
comments = re.findall(pattern, text)

result = []

for c in comments:
    if c.startswith("/*"):
        # Multi-line: remove leading whitespace from each line
        lines = c.split("\n")
        cleaned = "\n".join(line.lstrip() for line in lines)
        result.append(cleaned)
    else:
        # Single-line: remove leading whitespace from the line
        result.append(c.lstrip())

print("\n".join(result))

# Intuition:
# - Use a single regex to capture both comment types:
#       //.*         → everything after '//' until end of line
#       /\*...?\*/   → multi-line comments, non-greedy, spanning across lines
#
# - Multi-line comments may contain indentation, so we remove leading whitespace on each line.
# - Single-line comments only need left-strip.
# - Comments must appear in original order, so we process them sequentially.
#
# Explanation:
# 1. Read all input as a single text block so multi-line comment regex can match across lines.
# 2. Regex finds all comment blocks in the order they appear.
# 3. For each:
#       - If it begins with "/*", treat it as multi-line:
#             - split into lines
#             - left-strip each line
#             - rejoin them with newline (`\n`)
#       - Else treat it as single-line with simple lstrip()
# 4. Print each cleaned comment on its own line (multi-line blocks preserved).

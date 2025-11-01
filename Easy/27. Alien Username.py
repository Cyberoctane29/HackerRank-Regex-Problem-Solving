# Problem: Alien Username  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), Pattern Matching  

# Problem Statement:
# On a distant planet, computer usernames must follow a specific format:
#
# 1. It must begin with **either an underscore (_) or a period (.)**.
# 2. This must be immediately followed by **one or more digits (0–9)**.
# 3. After the digits, there may be **zero or more English letters (a–z or A–Z)**.
# 4. It may optionally end with an underscore (_).  
#    If it doesn’t end with an underscore, no characters may appear after the letters.
#
# Task:
# Given `n` usernames, determine whether each is **VALID** or **INVALID** according to the rules above.
#
# Input Format:
# - First line: integer `n` (number of usernames)
# - Next `n` lines: each contains a single username string
#
# Output Format:
# - For each username:
#     - Print `VALID` if it matches the alien username rules
#     - Print `INVALID` otherwise
#
# Constraints:
# - 1 < n ≤ 100
#
# Example:
# Input:
# 3
# _0898989811abced_
# _abce
# _09090909abcDO
#
# Output:
# VALID
# INVALID
# INVALID
#
# Explanation:
# - `_0898989811abced_` → ✅ valid (starts with '_', digits, letters, optional underscore)
# - `_abce` → ❌ invalid (no digits immediately after '_')
# - `_09090909abcDO` → ❌ invalid (ends with letters but followed by uppercase — which is okay — 
#     but must not be followed by any extra digits or symbols)

# Solution

import re

n = int(input())
pattern = r'^(?:_|\.)[0-9]+[a-zA-Z]*_?$'  # Start (_ or .), then digits, optional letters, optional underscore at end

for _ in range(n):
    if bool(re.search(pattern, input())):
        print("VALID")
    else:
        print("INVALID")

# Intuition:
# - ^ and $ → ensure the pattern matches the **entire** string
# - (?:_|\.) → non-capturing group: matches either '_' or '.'
# - [0-9]+ → one or more digits (must follow immediately)
# - [a-zA-Z]* → zero or more letters (optional)
# - _? → optional underscore at the end
#
# Explanation:
# - re.search() checks whether the pattern appears in the whole string.
# - bool() converts match object to True/False.
# - Based on this, print VALID or INVALID.

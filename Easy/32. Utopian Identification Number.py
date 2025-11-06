# Problem: Utopian Identification Number  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), Pattern Matching  

# Problem Statement:
# Every citizen of Utopia is assigned a unique identification number that follows a specific format.
# You must determine whether a given identification number is valid or not.
#
# The format rules are:
# 1. The string must begin with **0 to 3 lowercase letters** (a–z).
# 2. Immediately after the lowercase letters, there must be a **sequence of digits (0–9)**.
#    - The length of this digit segment must be **between 2 and 8 inclusive**.
# 3. Immediately following the digits, there must be **at least 3 uppercase letters** (A–Z).
#
# Input Format:
# - The first line contains an integer N (number of identification numbers).
# - The next N lines each contain a string representing an identification number.
#
# Output Format:
# - For each identification number:
#     - Print "VALID" if the ID matches the format.
#     - Print "INVALID" otherwise.
#
# Constraints:
# - 1 ≤ N ≤ 100
#
# Example:
# Input:
# 2
# abc012333ABCDEEEE
# 0123AB
#
# Output:
# VALID
# INVALID
#
# Explanation:
# - `abc012333ABCDEEEE` is valid because:
#     - Starts with 3 lowercase letters (`abc`)
#     - Followed by 6 digits (`012333`)
#     - Ends with 7 uppercase letters (`ABCDEEEE`)
# - `0123AB` is invalid because it only has 2 uppercase letters (needs at least 3).


# Solution

import re

n = int(input())
pattern = r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$'  # Matches full pattern with end anchor

for _ in range(n):
    if bool(re.search(pattern, input())):
        print("VALID")
    else:
        print("INVALID")

# Intuition:
# - Use regex anchors `^` and `$` to ensure the entire string matches the required structure.
# - The regex is built step-by-step based on the problem’s format rules.

# Explanation of the Regex:
# 1. `^` → Start of the string.
# 2. `[a-z]{0,3}` → Matches 0 to 3 lowercase letters.
# 3. `[0-9]{2,8}` → Matches 2 to 8 digits.
# 4. `[A-Z]{3,}` → Matches at least 3 uppercase letters.
# 5. `$` → End of the string (ensures no extra characters beyond valid format).
#
# The regex ensures the identification number strictly adheres to the Utopian ID pattern.

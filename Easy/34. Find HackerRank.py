# Problem: Find HackerRank  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Pattern Matching  

# Problem Statement:
# At HackerRank, we want to analyze our popularity by scanning conversations from various websites.
# Each line represents a conversation that may contain the word "hackerrank" (all lowercase).
# You need to determine if "hackerrank" appears:
#
# 1. At the **start** of the line.  
# 2. At the **end** of the line.  
# 3. Both at the **start and end** (i.e., the line is exactly "hackerrank").  
# 4. Or **neither**.
#
# Input Format:
# - The first line contains an integer N (number of conversations).
# - The next N lines each contain one conversation (string of lowercase words separated by spaces).
#
# Output Format:
# For each conversation:
# - Print `1`  → if it starts with "hackerrank"
# - Print `2`  → if it ends with "hackerrank"
# - Print `0`  → if it both starts and ends with "hackerrank"
# - Print `-1` → if none of the above
#
# Constraints:
# - 1 ≤ N ≤ 10
# - 1 ≤ W ≤ 100 (number of words per line)
# - 1 ≤ C ≤ 20 (characters per word)
# - All characters are lowercase English letters.
#
# Example:
# Input:
# 4
# i love hackerrank
# hackerrank is an awesome place for programmers
# hackerrank
# i think hackerrank is a great place to hangout
#
# Output:
# 2
# 1
# 0
# -1
#
# Explanation:
# - Line 1 ends with "hackerrank" → Output `2`
# - Line 2 starts with "hackerrank" → Output `1`
# - Line 3 starts and ends with "hackerrank" (only one word) → Output `0`
# - Line 4 neither starts nor ends with "hackerrank" → Output `-1`


# Solution

import re

n = int(input())
pattern_start = r'^hackerrank\s'   # Matches if line starts with "hackerrank"
pattern_end = r'\shackerrank$'     # Matches if line ends with "hackerrank"
pattern_exact = r'^hackerrank$'    # Matches if line is exactly "hackerrank"

for _ in range(n):
    s = input().strip()
    if bool(re.search(pattern_exact, s)):
        print(0)
    elif bool(re.search(pattern_start, s)):
        print(1)
    elif bool(re.search(pattern_end, s)):
        print(2)
    else:
        print(-1)

# Intuition:
# - We use three regex patterns to check whether the word “hackerrank” is at the beginning,
#   at the end, or is the only word in the line.
#
# Explanation of the Regex:
# 1. `^hackerrank\s` → Matches "hackerrank" at the **start** of the line, followed by a space.
# 2. `\shackerrank$` → Matches "hackerrank" at the **end** of the line, preceded by a space.
# 3. `^hackerrank$` → Matches if the entire string is exactly "hackerrank".
#
# - The order of checking matters:
#   - First, check if it’s both start and end (exact match).
#   - Then check if it starts with.
#   - Then check if it ends with.
#   - Otherwise, return -1.

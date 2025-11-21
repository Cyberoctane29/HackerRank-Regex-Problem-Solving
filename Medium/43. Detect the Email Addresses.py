# Problem: Extract Unique E-mail Addresses  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), Text Processing

# Problem Statement:
# You are given up to 100 lines of text. Your task is to extract all unique e-mail addresses
# that appear in the text and print them in lexicographical order, separated by semicolons.
#
# Simplified e-mail rules for this challenge:
# - Before the '@': one or more strings separated by dots
#   allowed characters → a–z, A–Z, 0–9, underscore (_), dot (.), %, +, -
# - After the '@': similar allowed strings separated by dots
# - Must end with a valid domain suffix: at least 2 letters (e.g., .com, .in, .org)
#
# Input:
# - First line: integer N (number of text lines, N ≤ 100)
# - Next N lines: the text to scan
#
# Output:
# - One line containing unique e-mail addresses sorted lexicographically
# - Separate each address with a semicolon `;`
#
# Example:
# Input:
# hackers@hackerrank.com  
# product@hackerrank.com  
#
# Output:
# hackers@hackerrank.com;product@hackerrank.com

# Solution 1

import re

n = int(input())
text = '\n'.join(input() for _ in range(n))

# General e-mail pattern matching sequences of allowed chars.
pattern = r'\b[A-Za-z0-9_.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

ans = set(re.findall(pattern, text))   # unique emails

print(';'.join(sorted(ans)))

# Intuition:
# - Use a strict but simplified regex for e-mail extraction.
# - `\b` ensures matching at word boundaries.
# - `[A-Za-z0-9_.%+-]+` matches local part before '@'.
# - `[A-Za-z0-9.-]+` matches domain name.
# - `\.[A-Za-z]{2,}` enforces a valid top-level domain.
# - Convert to set for uniqueness, sort, and print.

# Explanation:
# 1. Combine all lines into one text block for easier searching.
# 2. Use re.findall() to extract all substrings matching the email pattern.
# 3. Convert to a set to remove duplicates.
# 4. Sort lexicographically and print with semicolon separators.


# Solution 2 (using \w shorthand)

import re

n = int(input())
text = '\n'.join(input() for _ in range(n))

# \w includes A-Z, a-z, 0-9, _
pattern = r'\b[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}\b'

ans = set(re.findall(pattern, text))

print(';'.join(sorted(ans)))

# Intuition:
# - Same logic as Solution 1, but uses \w for convenience.
# - Slightly shorter and still satisfies the constraints of the challenge.

# Explanation:
# - Both regex patterns correctly detect valid e-mail addresses under the simplified rules.
# - Sorting ensures deterministic output.

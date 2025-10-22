# Problem: Backreferences to Optional Groups  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches S under the following rules:
# - S consists of exactly 8 digits.
# - S may optionally include a "-" separator between every 2 digits,
#   dividing the string into 4 parts of 2 digits each (e.g., 12-34-56-78 or 12345678).
#
# This is a regex-only challenge; no additional code logic is required.

# Explanation of backreferences to optional groups:
# - `(pattern)?` defines a capturing group that may match zero or one occurrence.
# - `\1` refers to the first capturing group.
# - If the group captured nothing, `\1` also matches nothing, allowing the regex to adapt.
# - This is particularly useful for matching strings that may or may not include a separator consistently.

# Example:
# Test Strings:
#   12345678 ✅ match
#   12-34-56-78 ✅ match
#   12-3456-78 ❌ no match
#   1234-5678 ❌ no match

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r"^\d{2}(-?)\d{2}\1\d{2}\1\d{2}$"  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used a capturing group `(-?)` to optionally match the "-" separator.
# The backreference `\1` ensures that the same separator (or absence of it) is repeated
# between all 2-digit segments. This guarantees consistency in formatting.

# Explanation:
# - `\d{2}` → matches exactly 2 digits.
# - `(-?)` → optional capturing group that matches "-" or nothing.
# - `\1` → backreference to the first group; enforces the same separator pattern.
# - `^` and `$` → anchor the pattern to match the entire string from start to end.
# Using this pattern, both "12345678" and "12-34-56-78" are valid matches.

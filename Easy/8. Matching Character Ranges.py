# Problem: Character Classes & Ranges  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches the following rules:
# - The length of the string must be at least 5.
# - 1st character: must be a lowercase English letter (a–z).
# - 2nd character: must be a positive digit (1–9). (0 is not considered positive.)
# - 3rd character: must not be a lowercase English letter.
# - 4th character: must not be an uppercase English letter.
# - 5th character: must be an uppercase English letter (A–Z).
#
# This is a regex-only challenge. No additional code logic is required.

# Example:
# Test String:   x5$gK
# Pattern:       ^[a-z][1-9][^a-z][^A-Z][A-Z]
# Match:         x5$gK
#
# - `[a-z]` matches any lowercase English letter.
# - `[1-9]` matches any positive digit.
# - `[^a-z]` matches any character that is NOT a lowercase English letter.
# - `[^A-Z]` matches any character that is NOT an uppercase English letter.
# - `[A-Z]` matches any uppercase English letter.
# - `^` ensures the match starts at the beginning of the string.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used character classes to strictly define the allowed or disallowed character sets at each position.
# By combining ranges, negated character classes, and anchors, the pattern enforces the required structure.

# Explanation:
# - `^[a-z]` ensures the first character is a lowercase English letter.
# - `[1-9]` ensures the second character is a positive digit.
# - `[^a-z]` ensures the third character is not a lowercase English letter.
# - `[^A-Z]` ensures the fourth character is not an uppercase English letter.
# - `[A-Z]` ensures the fifth character is an uppercase English letter.
# The `^` anchor ensures matching starts at the beginning of the string, and since length is ≥ 5, the pattern works as intended.

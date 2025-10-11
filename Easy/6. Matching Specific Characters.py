# Problem: Matching Specific Characters with Character Classes
# Difficulty: Easy
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S of length 6, match it using the following conditions:
# - 1st character: 1, 2, or 3
# - 2nd character: 1, 2, or 0
# - 3rd character: x, s, or 0
# - 4th character: 3, 0, A, or a
# - 5th character: x, s, or u
# - 6th character: . or ,
# Use a regex pattern to validate the string exactly. This is a regex-only challenge.

# Example:
# Test String:  12x3xu.
# Pattern:      ^[123][120][xs0][30Aa][xsu][.,]$
# Match:        Valid string according to given rules.

# Explanation of Character Classes:
# - `[123]` matches any one of 1, 2, or 3.
# - `[xs0]` matches any one of x, s, or 0.
# - `[30Aa]` matches 3, 0, A, or a.
# - `[xsu]` matches x, s, or u.
# - `[.,]` matches a literal dot or comma.
# - `^` and `$` anchor the pattern to the start and end of the string to enforce exact length and sequence.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower()


# Solution

Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used character classes `[ ]` to specify allowed characters at each position.
# Anchors `^` and `$` ensure the string is exactly 6 characters long and follows the specified order.

# Explanation:
# - The pattern checks each character individually using `[ ]`.
# - `^` and `$` ensure no extra characters before or after.
# - re.search() returns True only if the string exactly matches the pattern.

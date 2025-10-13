# Problem: Exact Repetitions with {x}  
# Difficulty: Medium  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches the following rules:
# - The string length must be exactly 45.
# - The first 40 characters must be letters (both lowercase and uppercase) or even digits (0,2,4,6,8).
# - The last 5 characters must be odd digits (1,3,5,7,9) or whitespace characters.
#
# This is a regex-only challenge. No additional code logic is required.

# Example:
# Test String:   Aa2Bb4Cc6...<40 chars>  1 3 5 7 9
# Pattern:       ^[a-zA-Z02468]{40}[13579\s]{5}$
# Match:         matches the string if it satisfies the above conditions

# Explanation of {x}:
# - `{n}` matches exactly n repetitions of the preceding character or character class.
# - `[a-zA-Z02468]{40}` matches 40 characters consisting of letters or even digits.
# - `[13579\s]{5}` matches 5 characters consisting of odd digits or whitespace.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower()


# Solution

Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used exact repetition `{n}` to ensure the first 40 characters and last 5 characters
# follow the specified character sets strictly.

# Explanation:
# - `^[a-zA-Z02468]{40}` ensures the first 40 characters are letters or even digits.
# - `[13579\s]{5}$` ensures the last 5 characters are odd digits or whitespace.
# - `^` and `$` anchors ensure the string matches the pattern from start to end.
# - re.search() returns True if the string satisfies all these rules.

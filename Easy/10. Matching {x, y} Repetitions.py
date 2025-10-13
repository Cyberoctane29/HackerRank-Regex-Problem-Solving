# Problem: Repetitions with {x,y}  
# Difficulty: Medium  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches the following rules:
# - S must begin with 1 or 2 digits.
# - After that, S must have 3 or more letters (both lowercase and uppercase).
# - Finally, S may end with 0 to 3 period symbols (.), inclusively.
#
# This is a regex-only challenge. No additional code logic is required.

# Example:
# Test String:   12Hack...
# Pattern:       ^\d{1,2}[a-zA-Z]{3,}\.{0,3}$
# Match:         matches the string if it satisfies the above conditions

# Explanation of {x,y}:
# - `{m,n}` matches between m and n repetitions (inclusive) of the preceding character/class/group.
# - `\d{1,2}` matches 1 or 2 digits.
# - `[a-zA-Z]{3,}` matches 3 or more letters.
# - `\.{0,3}` matches 0 to 3 periods at the end of the string.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower()


# Solution

Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used {x,y} to specify exact ranges of repetitions for each segment of the string:
# - 1–2 digits at the start, 3 or more letters in the middle, and up to 3 periods at the end.

# Explanation:
# - `^\d{1,2}` ensures the string starts with 1 or 2 digits.
# - `[a-zA-Z]{3,}` ensures the middle part contains at least 3 letters.
# - `\.{0,3}$` allows up to 3 periods at the end (including the possibility of none).
# - `^` and `$` anchors ensure the pattern matches the entire string from start to end.
# - re.search() returns True if the input string satisfies all these rules.

# Problem: Repetitions with *  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex pattern that satisfies the following:
# - S must begin with 2 or more digits.
# - Then, it may contain zero or more lowercase letters.
# - Finally, it may end with zero or more uppercase letters.
#
# This is a regex-only challenge. No extra logic is required.

# Example:
# Test String:   12abcXYZ
# Pattern:       ^\d{2,}[a-z]*[A-Z]*$
# Match:         matches the string if it satisfies the above rules

# Explanation of *:
# - `*` matches zero or more occurrences of the preceding character/class/group.
# - `\d{2,}` ensures at least 2 digits at the beginning.
# - `[a-z]*` allows any number of lowercase letters (including none).
# - `[A-Z]*` allows any number of uppercase letters (including none).

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used `*` after lowercase and uppercase letter classes to allow them to appear any number of times or not at all.
# The digits part is fixed with `{2,}` to ensure at least 2 digits at the beginning.

# Explanation:
# - `^\d{2,}` matches 2 or more digits at the start of the string.
# - `[a-z]*` matches zero or more lowercase letters.
# - `[A-Z]*$` matches zero or more uppercase letters at the end of the string.
# - The `^` and `$` anchors make sure the whole string follows this exact structure.
# - re.search() returns True if the input matches the pattern fully.

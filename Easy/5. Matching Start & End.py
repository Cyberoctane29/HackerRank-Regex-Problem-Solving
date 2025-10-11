# Problem: Matching Start & End Patterns  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, match a pattern of exactly 6 characters where:
# - The first character is a digit (`\d`)
# - The next 4 characters are word characters (`\w`)
# - The last character is a dot (`.`)
# - The string must **start** with the digit and **end** with the dot.
#
# This is a regex-only challenge; you only need to fill in the regex pattern.

# Example:
# Test String:  1abcde.
# Pattern:      ^\d\w{4}\.$
# Match:        1abcd.

# Explanation of Anchors:
# - `^` asserts the start of the string.
# - `$` asserts the end of the string.
# - `\d` matches a single digit.
# - `\w{4}` matches exactly 4 word characters (letters, digits, or underscore).
# - `\.` matches the literal dot character at the end.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r"^\d\w{4}\.$"  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used `^` and `$` to ensure the pattern matches the **entire string** exactly 6 characters long.
# The first character is constrained to a digit, the next four are word characters, and the last is a dot.

# Explanation:
# - `^` ensures the match starts at the beginning of the string.
# - `\d` matches the first digit.
# - `\w{4}` matches the next four word characters.
# - `\.` matches the final dot.
# - `$` ensures the match ends at the last character of the string.
# - re.search() returns True if this exact structure is found, False otherwise.

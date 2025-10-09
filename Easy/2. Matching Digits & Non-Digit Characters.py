# Problem: Matching Digits & Non-Digit Characters  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, match the pattern xxXxxXxxxx  
# where:
#   - x = a digit character (\d)
#   - X = a non-digit character (\D)
# This is a regex-only challenge, meaning I only needed to complete the regex pattern, not write logic.

# Example:
# Test String:  06-11-2015
# Pattern:      \d{2}\D\d{2}\D\d{4}
# Match:        06-11-2015
#
# The pattern looks for:
# - 2 digits
# - 1 non-digit
# - 2 digits
# - 1 non-digit
# - 4 digits

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution 1

Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used quantifiers to match the exact number of digits and non-digits as required by the pattern (xxXxxXxxxx).

# Explanation:
# - `\d{2}` matches exactly 2 digits (e.g., 06).
# - `\D` matches a single non-digit character (e.g., - or /).
# - `\d{2}` matches another 2 digits.
# - `\D` matches another non-digit.
# - `\d{4}` matches 4 digits (e.g., 2015).
# re.search() returns True if the pattern is found, otherwise False.


# Solution 2

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# Instead of using quantifiers, I wrote out each digit and non-digit explicitly,
# which achieves the same match as Solution 1.

# Explanation:
# - `\d\d` matches two digits.
# - `\D` matches a single non-digit.
# - `\d\d` matches another two digits.
# - `\D` matches another single non-digit.
# - `\d\d\d\d` matches four digits.
# This is a more verbose version of Solution 1, but it works identically.
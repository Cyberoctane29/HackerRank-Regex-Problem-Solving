# Problem: Matching Whitespace & Non-Whitespace Characters  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, match the pattern XXXXXXX  
# where:
#   - X = non-whitespace character (\S)
#   - & = whitespace character (\s)
# Specifically:
# - 2 non-whitespace characters
# - 1 whitespace character
# - 2 non-whitespace characters
# - 1 whitespace character
# - 2 non-whitespace characters
#
# This is a regex-only challenge, so I only needed to complete the regex pattern.

# Example:
# Test String:  AB CD EF
# Pattern:      \S{2}\s\S{2}\s\S{2}
# Match:        AB CD EF
#
# \S matches any non-whitespace character (letters, digits, symbols, etc.)
# \s matches any whitespace character (spaces, tabs, newlines, etc.)

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution 1

Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used quantifiers `{2}` to match exactly two non-whitespace characters,
# and `\s` for the single whitespace in between.

# Explanation:
# - `\S{2}` matches exactly 2 non-whitespace characters (e.g., AB).
# - `\s` matches a single whitespace character (e.g., space).
# - `\S{2}` matches the next 2 non-whitespace characters (e.g., CD).
# - `\s` matches another whitespace character.
# - `\S{2}` matches the last 2 non-whitespace characters (e.g., EF).
# re.search() returns True if the pattern is matched, else False.


# Solution 2

Regex_Pattern = r"\S\S\s\S\S\s\S\S"  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# Instead of quantifiers, I wrote the pattern explicitly using repeated `\S` for each non-whitespace character.

# Explanation:
# - `\S\S` matches two non-whitespace characters.
# - `\s` matches a whitespace.
# - `\S\S` matches another two non-whitespace characters.
# - `\s` matches another whitespace.
# - `\S\S` matches the last two non-whitespace characters.
# This gives the same match result as Solution 1, but in a more explicit form.

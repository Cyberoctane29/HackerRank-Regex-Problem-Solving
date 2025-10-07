# Problem: Matching Specific String
# Difficulty: Easy
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, match the specific string "hackerrank".
# The match must be case-sensitive.
# I was required to complete the regex pattern only (no logic modification needed),
# as this is a regex-only challenge on HackerRank.

# Example:
# Test String:  https://en.wikipedia.org/
# Pattern:      wikipedia
# Match:        https://en.**wikipedia**.org/
#
# In this challenge, my task was to match occurrences of the word "hackerrank" in the given input.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# Test_String = input()
# match = re.findall(Regex_Pattern, Test_String)
# print("Number of matches :", len(match))

# Solution:
Regex_Pattern = r'hackerrank'  # Do not delete 'r'.

import re

Test_String = input()  # Note: Input is automatically provided by HackerRank test cases.
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# - My goal was to identify all exact matches of the string "hackerrank".
# - Since the problem specifies a case-sensitive match, I used the pattern exactly as given.
# - re.findall() conveniently returns all matches in a list, so len() gives the total count.

# Explanation:
# 1. Regex_Pattern = r'hackerrank' matches every literal occurrence of "hackerrank".
# 2. The raw string prefix (r'') ensures no escape sequences interfere with matching.
# 3. re.findall() searches the entire input for all non-overlapping matches.
# 4. len(match) outputs the total number of matched occurrences.

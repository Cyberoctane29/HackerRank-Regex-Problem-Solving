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

# Solution 1

Regex_Pattern = r'hackerrank'  # Do not delete 'r'.

import re

Test_String = input()  # Note: Input is automatically provided by HackerRank test cases.
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# My goal was to identify all exact matches of the string "hackerrank".
# Since the problem specifies a case-sensitive match, I used the pattern exactly as given.
# re.findall() conveniently returns all matches in a list, so len() gives the total count.

# Explanation:
# Regex_Pattern = r'hackerrank' matches every literal occurrence of "hackerrank".
# The raw string prefix (r'') ensures no escape sequences interfere with matching.
# re.findall() searches the entire input for all non-overlapping matches.
# len(match) outputs the total number of matched occurrences.


# Solution 2

Regex_Pattern = r'( |)hackerrank(| )'  # Do not delete 'r'.

import re

Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# I slightly modified the pattern to account for potential spaces before or after the word "hackerrank".
# This helps capture cases where the word might appear with surrounding spaces in the input string.

# Explanation:
# The pattern `( |)hackerrank(| )` allows an optional space before or after the target word.
# The parentheses create capture groups for these optional spaces.
# re.findall() still returns all matches, but since groups are used, it returns tuples of matched parts.
# len(match) gives the number of such matches found, regardless of spacing.

# Solution 3

Regex_Pattern = r'(?: |\b)hackerrank(?:\b| )'  # Do not delete 'r'.

import re

Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# I used non-capturing groups and word boundaries to match "hackerrank" as a complete word,
# while also allowing for optional spaces around it.
# This is a cleaner and more precise approach than using capturing groups.

# Explanation:
# The pattern `(?: |\b)hackerrank(?:\b| )`:
# - `(?: ...)` denotes a non-capturing group, so re.findall() returns only the matched word.
# - `\b` ensures word boundaries, so partial words like "hackerranking" won't be matched.
# - The space or boundary on either side allows flexibility with surrounding characters.
# This approach improves accuracy while keeping the output simple.
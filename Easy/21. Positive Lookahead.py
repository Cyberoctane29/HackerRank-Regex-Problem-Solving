# Problem: Positive Lookahead `( ?= )`  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches **all occurrences of 'o'**
# that are **immediately followed by 'oo'**.
# 
# You must use a **positive lookahead** `( ?= )`.
# 
# The lookahead only asserts a condition — it does not consume characters from the match.

# Example:
# Pattern:  o(?=oo)
# Test String:  gooooo!
# Matches: ✅ 'o' at positions where it’s followed by "oo"
# Output:  Number of matches : 3

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# Test_String = input()
# match = re.findall(Regex_Pattern, Test_String)
# print("Number of matches :", len(match))


# Solution

Regex_Pattern = r'o(?=oo)'  # Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# - We want to find every 'o' that’s directly followed by 'oo'.
# - The '(?=oo)' lookahead checks for 'oo' immediately after 'o' but doesn't include it in the match.

# Explanation:
# - `o` → matches the character 'o'.
# - `(?=oo)` → positive lookahead that asserts the next two characters are 'oo'.
# - `re.findall()` returns all non-overlapping matches of 'o' that satisfy this condition.

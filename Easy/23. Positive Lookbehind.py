# Problem: Positive Lookbehind `( ?<= )`  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches **all digits which are immediately
# preceded by an odd digit**.
# 
# You must use a **positive lookbehind** `( ?<= )`.
# 
# The lookbehind only asserts a condition — it does not consume characters from the match.

# Example:
# Pattern:  (?<=[13579])\d
# Test String:  123467
# Matches: ✅ '2', '4', and '6' (because they are immediately after 1, 3, and 5 respectively)
# Output:  Number of matches : 3

# Note:
# JavaScript does not support lookbehind assertions.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# Test_String = input()
# match = re.findall(Regex_Pattern, Test_String)
# print("Number of matches :", len(match))


# Solution

Regex_Pattern = r"(?<=[13579])\d"  # Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# - We want to find every digit that is immediately preceded by an **odd digit** (1, 3, 5, 7, 9).
# - The positive lookbehind `(?<=...)` checks the character before the current one without including it.

# Explanation:
# - `(?<=[13579])` → positive lookbehind that asserts the previous character is an odd digit.
# - `\d` → matches any digit (0–9).
# - Together, it matches digits that follow odd digits directly.
# - `re.findall()` returns all such matches.

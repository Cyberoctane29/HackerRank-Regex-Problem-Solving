# Problem: Negative Lookbehind `( ?<! )`  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches **all characters which are not
# immediately preceded by a vowel** (a, e, i, o, u, A, E, I, O, U).
# 
# You must use a **negative lookbehind** `( ?<! )`.
# 
# The lookbehind only asserts a condition — it does not consume characters from the match.

# Example:
# Pattern:  (?<![aeiouAEIOU]).
# Test String:  he1o
# Matches: ✅ 'h', 'e', '1', 'o'  (because none of them are preceded by vowels)
# Output:  Number of matches : 4

# Note:
# JavaScript does not support lookbehind assertions.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# Test_String = input()
# match = re.findall(Regex_Pattern, Test_String)
# print("Number of matches :", len(match))


# Solution

Regex_Pattern = r"(?<![aeiouAEIOU])."  # Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# - We want to find every character that is **not preceded by a vowel**.
# - The negative lookbehind `(?<!...)` checks the character before the current one without including it.

# Explanation:
# - `(?<![aeiouAEIOU])` → negative lookbehind that asserts the previous character is **not** a vowel.
# - `.` → matches any character (except newline).
# - This ensures we only match characters that are not immediately preceded by vowels.
# - `re.findall()` returns all such matches.

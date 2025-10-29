# Problem: Negative Lookahead `( ?! )`  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches **all characters which are not
# immediately followed by the same character**.
# 
# You must use a **negative lookahead** `( ?! )`.
# 
# The lookahead only asserts a condition — it does not consume characters from the match.

# Example:
# Pattern:  (\w)(?!\1)
# Test String:  goooo
# Matches: ✅ 'g' and the last 'o'
# Output:  Number of matches : 2

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# Test_String = input()
# match = re.findall(Regex_Pattern, Test_String)
# print("Number of matches :", len(match))


# Solution

Regex_Pattern = r"(\w)(?!\1)"  # Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# - We want to find every word character that is **not** followed by the same character.
# - The negative lookahead `(?!\1)` ensures the next character is different from the one matched.

# Explanation:
# - `(\w)` → captures any word character (letter, digit, or underscore).
# - `(?!\1)` → negative lookahead that asserts the next character is **not** the same as the captured one.
# - This way, only characters without identical consecutive duplicates are matched.
# - `re.findall()` returns all such matching characters.

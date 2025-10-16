# Problem: Backreferences with `\group_number`  
# Difficulty: Hard  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex that matches S under the following rules:
# - S must be of **length 20**.
# - 1st character: lowercase letter.
# - 2nd character: word character.
# - 3rd character: whitespace character.
# - 4th character: non-word character.
# - 5th character: digit.
# - 6th character: non-digit.
# - 7th character: uppercase letter.
# - 8th character: any letter (lowercase or uppercase).
# - 9th character: vowel (a, e, i, o, u, A, E, I, O, U).
# - 10th character: non-whitespace character.
# - 11th–20th characters: must be exact **backreferences** of the 1st–10th characters respectively.

# Explanation of `\n`:
# - `\1` refers to the text matched by the **first** capturing group `(...)`.
# - `\2` refers to the text matched by the **second** capturing group, and so on.
# - These allow you to match the same text again without rewriting the pattern.

# Example:
# Pattern:  ^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$
# Test String:  a_\$5zBaiea_\$5zBaie
# Match: ✅ a_\$5zBaiea_\$5zBaie

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# ✅ Solution

Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used capturing groups for the first 10 required characters and then used backreferences
# to ensure that the next 10 characters are exactly the same in order.

# Explanation:
# - `([a-z])` → lowercase letter, group 1
# - `(\w)` → word character, group 2
# - `(\s)` → whitespace character, group 3
# - `(\W)` → non-word character, group 4
# - `(\d)` → digit, group 5
# - `(\D)` → non-digit, group 6
# - `([A-Z])` → uppercase letter, group 7
# - `([a-zA-Z])` → any letter, group 8
# - `([aeiouAEIOU])` → vowel, group 9
# - `(\S)` → non-whitespace character, group 10
# - `\1\2\3\4\5\6\7\8\9\10` → exact backreference sequence of groups 1–10
# - `^` and `$` anchor the pattern to match the entire string from start to end.

# Problem: `$` Boundary Matcher  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# You need to write a regex pattern to match a test string `S` such that:
# - The string consists of only uppercase and lowercase English letters.
# - The string must end with the character `s`.
#
# This is a regex-only challenge. No extra logic is required.

# Example:
# Test String:   Hints
# Pattern:       ^[a-zA-Z]*s$
# Match:         ✅ Matches because it has only letters and ends with 's'.

# Explanation of `$`:
# - `$` asserts that the match must occur at the **end of the line**.
# - `^[a-zA-Z]*` allows zero or more letters at the start.
# - `s$` ensures the string ends with the character 's'.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r'^[a-zA-Z]*s$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used `^[a-zA-Z]*` to allow any number of letters and `$` after `s`
# to ensure that the string strictly ends with the lowercase letter 's'.

# Explanation:
# - `^` anchors the match at the start of the string.
# - `[a-zA-Z]*` matches zero or more alphabetic characters.
# - `s$` ensures the string ends with the character 's'.
# - This pattern guarantees no digits or symbols are allowed, and 's' is the last character.

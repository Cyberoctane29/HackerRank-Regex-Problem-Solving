# Problem: Repetitions with +  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex pattern that satisfies the following:
# - S should begin with 1 or more digits.
# - Then, it should have 1 or more uppercase letters.
# - Finally, it should end with 1 or more lowercase letters.
#
# This is a regex-only challenge. No extra logic is required.

# Example:
# Test String:   123ABCxyz
# Pattern:       ^\d+[A-Z]+[a-z]+$
# Match:         matches the string if it satisfies the above rules

# Explanation of +:
# - `+` matches one or more occurrences of the preceding character/class/group.
# - `\d+` ensures at least 1 digit at the beginning.
# - `[A-Z]+` ensures at least 1 uppercase letter.
# - `[a-z]+` ensures at least 1 lowercase letter at the end.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used `+` after each character class to ensure the presence of at least one digit,
# one uppercase letter, and one lowercase letter in that specific order.

# Explanation:
# - `^\d+` matches 1 or more digits at the start of the string.
# - `[A-Z]+` matches 1 or more uppercase letters.
# - `[a-z]+$` matches 1 or more lowercase letters at the end of the string.
# - The `^` and `$` anchors ensure that the entire string strictly follows this structure.
# - re.search() validates if the input fully matches the pattern.

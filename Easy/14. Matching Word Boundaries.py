# Problem: Word Boundary and Vowel Start  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex pattern to match words that:
# - Start with a vowel (a, e, i, o, u or A, E, I, O, U)
# - Contain only letters (lowercase or uppercase)
# - Are of any length
# - Begin and end at a word boundary (`\b`)
#
# This is a regex-only challenge. No additional code logic is required.

# Example:
# Test String:   An apple is on the tree
# Pattern:       \b[aeiouAEIOU][a-zA-Z]*\b
# Matches:       "An", "apple", "is", "on"

# Explanation of \b:
# - `\b` ensures matching at word boundaries so partial words are not matched.
# - `[aeiouAEIOU]` matches the first character being a vowel.
# - `[a-zA-Z]*` matches zero or more letters following the vowel.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used a word boundary `\b` to ensure the match is an entire word.
# The first letter is constrained to vowels using `[aeiouAEIOU]`.
# Following letters, if any, are letters only `[a-zA-Z]*`.

# Explanation:
# - `\b` at the start ensures the word starts at a word boundary.
# - `[aeiouAEIOU]` ensures the first character is a vowel.
# - `[a-zA-Z]*` allows the rest of the word to be any combination of letters.
# - `\b` at the end ensures the word ends at a word boundary.
# - re.search() checks if any word in the input string matches the pattern.

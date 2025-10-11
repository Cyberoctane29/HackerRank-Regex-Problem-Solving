# Problem: Matching Word & Non-Word Characters  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, match the pattern:
#    xxxXxxxxxxxxxxXxxx
# where:
#   - x = any word character (letter, digit, or underscore) → `\w`
#   - X = any non-word character (not a letter, digit, or underscore) → `\W`
#
# Specifically, the pattern represents:
# - 3 word characters
# - 1 non-word character
# - 10 word characters
# - 1 non-word character
# - 3 word characters
#
# This is a regex-only challenge, so only the regex pattern was required.

# Example:
# Test String:   abc#helloworld$xyz
# Pattern:       \w{3}\W\w{10}\W\w{3}
# Match:         abc#helloworld$xyz
#
# Here:
# - `abc`, `helloworld`, and `xyz` are word sequences.
# - `#` and `$` are non-word characters separating them.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution 1

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used quantifiers `{3}` and `{10}` for precise counts of word characters
# and inserted `\W` to represent the required non-word characters in between.

# Explanation:
# - `\w{3}` matches exactly 3 word characters.
# - `\W` matches a single non-word character.
# - `\w{10}` matches exactly 10 word characters.
# - Another `\W` matches the next non-word character.
# - Finally, `\w{3}` matches 3 more word characters.
# re.search() checks if this exact pattern exists in the input string.


# Solution 2

Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# This version explicitly writes each character position
# instead of using quantifiers like `{3}` or `{10}`.
# It’s longer but functionally equivalent to Solution 1.

# Explanation:
# - The pattern repeats `\w` for each word character and `\W` for each non-word character.
# - The sequence exactly follows the required structure: 3 word chars, 1 non-word, 10 word chars, 1 non-word, 3 word chars.
# - re.search() returns True if this exact structure appears anywhere in the input.
# While verbose, this form helps beginners understand explicit repetition instead of using `{}` quantifiers.

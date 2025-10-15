# Problem: Grouping with () and Non-Capturing Groups (?: )  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex pattern that satisfies the following:
# - S should have **3 or more consecutive repetitions** of the substring `ok`.
#
# Note: 
# - Parentheses `()` group parts of a regex together, allowing us to apply quantifiers to the entire group.
# - `(?: )` creates a non-capturing group — this groups the pattern but doesn’t store the matched text for backreferences.

# Example:
# Test String:   okokok
# Pattern:       (?:ok){3,}
# Match:         ✅ okokok

# Explanation of (?: ):
# - `(ok)` groups the substring `ok`.
# - `(?:ok)` is a non-capturing group — useful when we don’t need backreferences.
# - `{3,}` ensures the group repeats at least 3 times consecutively.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r'(?:ok){3,}'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I wrapped "ok" in a non-capturing group to apply the repetition quantifier `{3,}` directly on it.
# This allows matching "ok" repeated three or more times without storing unnecessary capturing groups.

# Explanation:
# - `(?:ok)` groups the substring `ok` without capturing it.
# - `{3,}` means three or more repetitions of that group.
# - re.search() checks if the test string contains such a sequence anywhere.

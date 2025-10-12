# Problem: Negated Character Classes  
# Difficulty: Easy
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, match the pattern with the following conditions:
# - The length of S must be exactly 6 characters.
# - 1st character should not be a digit (0–9).
# - 2nd character should not be a lowercase vowel (a, e, i, o, u).
# - 3rd character should not be b, c, D, or F.
# - 4th character should not be a whitespace character (\r, \n, \t, \f, or space).
# - 5th character should not be an uppercase vowel (A, E, I, O, U).
# - 6th character should not be `.` or `,`.
#
# This is a regex-only challenge. You are not required to write any additional code.

# Example:
# Test String:   ZxgkLp
# Pattern:       ^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$
# Match:         ZxgkLp
#
# - `[^ ]` represents a **negated character class** — it matches any character not listed inside the brackets.
# - Anchors `^` and `$` ensure that the pattern applies to the entire string.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution 1

Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used negated character classes `[^ ]` to disallow specific sets of characters at each position
# while still allowing everything else. This ensures only valid characters can appear at each spot.

# Explanation:
# - `[^\d]` matches any character except digits.
# - `[^aeiou]` matches any character except lowercase vowels.
# - `[^bcDF]` matches any character except b, c, D, F.
# - `[^\s]` matches any character except whitespace.
# - `[^AEIOU]` matches any character except uppercase vowels.
# - `[^.,]` matches any character except `.` or `,`.
# The pattern is anchored with `^` and `$` to enforce the 6-character length and exact order.


# Solution 2

Regex_Pattern = r'^[\D][^aeiou][^bcDF][\S][^AEIOU][^.,]$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I replaced some negated character classes with shorthand notations like `\D` (non-digit) and `\S` (non-whitespace),
# making the regex more concise without changing its meaning.

# Explanation:
# - `\D` matches any non-digit character (equivalent to `[^\d]`).
# - `[^aeiou]` excludes lowercase vowels.
# - `[^bcDF]` excludes specific letters (b, c, D, F).
# - `\S` matches any non-whitespace character (equivalent to `[^\s]`).
# - `[^AEIOU]` excludes uppercase vowels.
# - `[^.,]` excludes `.` and `,`.
# The result is a cleaner, functionally equivalent pattern.

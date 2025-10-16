# Problem: Alternations with |  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# Given a test string S, write a regex pattern that satisfies the following:
# - S must start with one of the titles: `Mr.`, `Mrs.`, `Ms.`, `Dr.`, or `Er.`.
# - After the title, the rest of the string must contain **only English alphabetic letters** (both uppercase and lowercase) and at least one character.
#
# Note:
# - Alternation `|` acts as an OR operator inside a group `()`.
# - Anchors `^` and `$` ensure that the match spans the entire string from start to end.

# Example:
# Test String:   Dr.John
# Pattern:       ^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$
# Match:         ✅ Dr.John

# Explanation of ( ... | ... ):
# - `(Mr|Mrs|Ms|Dr|Er)` matches exactly one of the titles.
# - `\.` matches the literal dot after the title.
# - `[a-zA-Z]+` matches one or more letters following the title.
# - Anchors `^` and `$` ensure the full string matches this pattern.

# Boilerplate provided by HackerRank:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# print(str(bool(re.search(Regex_Pattern, input()))).lower())


# Solution

Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'  # Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Intuition:
# I used a capturing group with alternation to list all allowed prefixes.
# The literal `\.` ensures the dot after the title is matched.
# `[a-zA-Z]+` ensures the rest of the string contains only letters, at least one.

# Explanation:
# - `(Mr|Mrs|Ms|Dr|Er)` matches any one of the specified titles.
# - `\.` matches the required dot literally.
# - `[a-zA-Z]+` matches the name after the title.
# - `^` and `$` ensure that the entire input string follows this exact pattern.

# Problem: Find a Word  
# Difficulty: Medium  
# Skills: Python, Regular Expressions (re module), Word Boundary Matching

# Problem Statement:
# A *word* is defined as a maximal sequence of characters consisting only of:
#   - lowercase letters a–z
#   - uppercase letters A–Z
#   - digits 0–9
#   - underscore '_'
#
# A word occurs only when:
#   - It is preceded by a non-word character (or start of sentence)
#   - It is followed by a non-word character (or end of sentence)
#
# You are given N sentences and then T query words.  
# For each query word, count how many times it occurs as a whole word in all sentences.

# Notes:
# - WORD characters = `[A-Za-z0-9_]`
# - Word boundaries `\b` detect transitions between word and non-word characters.
# - Words like "foo-bar" count as two words: "foo" and "bar".
# - Words like "foo_bar" are a single word → "foo" inside it does NOT count.
# - Punctuation such as '.', ',', '-', '(', ')', ''' all break words.

# Example:
# Input:
# foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.
# Query: foo
#
# Output: 6

# Solution

import re

n = int(input())
text = ' '.join(input() for _ in range(n))   # merge all lines into one searchable text

t = int(input())

for _ in range(t):
    query = input().strip()
    pattern = rf'\b{query}\b'     # match whole word only
    ans = len(re.findall(pattern, text))
    print(ans)

# Intuition:
# - We must match only whole-word occurrences.
# - Python’s \b matches boundaries between word-chars and non-word-chars.
# - Since valid word-chars include letters, digits and underscore, this aligns perfectly.

# Explanation:
# 1. Combine all sentences into one string for easier searching.
# 2. For each query word:
#    - Build a regex using:  \bword\b
#    - \b ensures word boundary on both sides.
#    - re.findall returns all matches; count them.
# 3. Print the count for each query.

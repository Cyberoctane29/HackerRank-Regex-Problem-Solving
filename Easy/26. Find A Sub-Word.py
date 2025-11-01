# Problem: Find A Sub-Word  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Processing  

# Problem Statement:
# We define:
# - A **word character** as any of the following:
#     - English alphabetic letter (a–z, A–Z)
#     - Decimal digit (0–9)
#     - Underscore (_)
#
# - A **word** is a contiguous sequence of one or more word characters
#   that is **preceded and succeeded by one or more non-word characters or line terminators**.
#
# - A **sub-word** is a sequence of word characters that:
#     - Appears **inside another word** (as a contiguous substring)
#     - Is **preceded and succeeded by word characters only**
#
# Task:
# Given `n` sentences, and `q` queries, count how many times each query string `s`
# occurs as a **sub-word** (not a standalone word) in all `n` sentences.
#
# Input Format:
# - First line: integer `n` (number of sentences)
# - Next `n` lines: each a sentence consisting of words separated by non-word characters
# - Next line: integer `q` (number of queries)
# - Next `q` lines: each containing a query string `s`
#
# Output Format:
# - For each query, print the total number of sub-word occurrences across all sentences
#
# Example:
# Input:
# 1
# existing pessimist optimist this is
# 1
# is
#
# Output:
# 3
#
# Explanation:
# - "is" occurs inside:
#     - existing → 1 time
#     - pessimist → 1 time
#     - optimist → 1 time
# - "this" and "is" (standalone) are ignored because "is" is not surrounded by word characters.
# - Total = 3

# Boilerplate provided by HackerRank:
# import re
# n = int(input())
# sentences = [input().strip() for _ in range(n)]
# q = int(input())
# queries = [input().strip() for _ in range(q)]
# for query in queries:
#     total = 0
#     pattern = r"________"
#     for sentence in sentences:
#         total += len(re.findall(pattern, sentence))
#     print(total)


# Solution

import re

n = int(input())
sentences = [input().strip() for _ in range(n)]

q = int(input())
queries = [input().strip() for _ in range(q)]

for query in queries:
    total = 0
    pattern = rf"\B{re.escape(query)}\B"  # Matches 'query' only when surrounded by word characters
    for sentence in sentences:
        total += len(re.findall(pattern, sentence))
    print(total)

# Intuition:
# - `\B` matches a position **not** at a word boundary, meaning it’s surrounded by word characters.
# - So `\Bword\B` ensures the substring is **inside** a word, not at its start or end.
# - `re.escape(query)` safely escapes any special regex characters in the query string.
#
# Explanation:
# - For each query:
#     - We build a regex pattern like r"\Bis\B"
#     - Use re.findall() to count all matches per sentence
#     - Sum all occurrences across sentences
# - Finally, print the total count for each query.

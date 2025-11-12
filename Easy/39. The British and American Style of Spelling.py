# Problem: The British and American Style of Spelling  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Pattern Matching  

# Problem Statement:
# American English and British English often differ in their spellings.  
# A common difference is that words ending in **-ze** in American English  
# often end in **-se** in British English (e.g., "analyze" → "analyse").  
#
# Given the American-English spelling of a word ending with "ze",  
# find the **total occurrences** of both its American and British variants  
# across a given set of text lines.
#
# Input Format:
# - The first line: integer N (number of text lines)
# - Next N lines: each line contains a sequence of words separated by spaces
# - Next line: integer T (number of test cases)
# - Next T lines: each contains a word W' (American spelling ending with "ze")
#
# Output Format:
# - For each test case, print the total count of both variants (ending in "ze" and "se")
#
# Constraints:
# - 1 ≤ N ≤ 10
# - Each line ≤ 10 words
# - Each word contains only lowercase letters (a–z)
# - 1 ≤ T ≤ 10
# - 1 ≤ length(W or W') ≤ 20
# - Every test word W' ends with "ze"
#
# Example:
# Input:
# 2
# the organization will organize a meeting
# in british english they organise differently
# 1
# organize
#
# Output:
# 2
#
# Explanation:
# - "organize" appears once.
# - "organise" (UK variant) appears once.
# - Total = 2.


# Solution

import re

n = int(input())
lines = [input() for _ in range(n)]

t = int(input())
for _ in range(t):
    test_word = input()  # American spelling (ends in 'ze')
    uk_word = test_word.replace('ze', 'se')  # Convert to British spelling

    # Match either American (-ze) or British (-se) variants as whole words
    pattern = rf'\b({test_word}|{uk_word})\b'

    ans = 0
    for line in lines:
        ans += len(re.findall(pattern, line))
    print(ans)

# Intuition:
# - The task requires counting both forms of the word: one ending in "ze" (US) and one ending in "se" (UK).
# - The regex pattern `\b` ensures we only match **whole words**, not substrings.
# - Using an alternation `|` allows matching either variant in one pass.
#
# Explanation:
# 1. For a test word like "organize":
#     - British variant becomes "organise".
#     - The regex becomes `\b(organize|organise)\b`.
# 2. `re.findall()` counts all appearances of both spellings across the given lines.
# 3. The total occurrences are printed for each test word.
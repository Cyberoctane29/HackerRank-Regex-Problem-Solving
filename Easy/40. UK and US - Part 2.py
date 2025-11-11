# Problem: UK and US Spelling Variations  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Processing  

# Problem Statement:
# British and American English often differ in spelling — one common difference is the use of **"our"** in UK words 
# (like "colour", "odour") versus **"or"** in US words ("color", "odor").  
#
# Given a set of sentences and a list of UK-style words, you must count how many times both the **UK** and **US** variants 
# appear in the sentences combined.
#
# Input Format:
# - The first line: integer N (number of text lines)
# - Next N lines: contain sentences with words separated by spaces
# - Next line: integer T (number of test cases)
# - Next T lines: each contains a UK-formatted word (with “our”)
#
# Output Format:
# - For each test word, print the total number of times **both UK and US** variants appear in all N lines.
#
# Constraints:
# - 1 ≤ N ≤ 10
# - Each line ≤ 10 words
# - Each word only contains lowercase English letters
# - 1 ≤ T ≤ 10
# - 1 ≤ length(W or W') ≤ 20
# - Every test word contains “our” as a substring.
#
# Example:
# Input:
# 2
# the odour coming out of the left over food was intolerable
# ammonia has a very pungent odor
# 1
# odour
#
# Output:
# 2
#
# Explanation:
# - “odour” (UK) appears once.
# - “odor” (US) appears once.
# - Total count = 2.


# Solution

import re

n = int(input())
lines = [input() for _ in range(n)]  # Read all input lines

t = int(input())

for _ in range(t):
    test_word = input()  # UK word containing 'our'
    us_word = test_word.replace("our", "or")  # Create US variant

    # Pattern matches either UK or US spelling as a whole word
    pattern = rf'\b(?:{test_word}|{us_word})\b'

    ans = 0
    for line in lines:
        ans += len(re.findall(pattern, line))
    print(ans)

# Intuition:
# - Each UK word with “our” (like odour) has a US variant with “or” (odor).
# - Using regex `\b` ensures we match full words only, not substrings within other words.
# - The pattern `(odour|odor)` matches both variants simultaneously.
#
# Explanation:
# 1. `us_word = test_word.replace("our", "or")`
#    - Generates the US spelling version automatically.
# 2. `pattern = rf'\b({test_word}|{us_word})\b'`
#    - Matches either the UK or US spelling as a complete word.
# 3. For each line, `re.findall()` counts all matches.
# 4. The total count is printed for each test word.

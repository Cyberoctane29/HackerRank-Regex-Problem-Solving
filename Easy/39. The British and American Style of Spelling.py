# Problem: British and American Style of Spelling  
# Difficulty: Easy  
# Skills: Python, Regular Expressions, String Processing  

# Problem Statement:
# American English words ending in **-ze** (e.g., analyze, recognize) often end in **-se** 
# in British English (analyse, recognise).
#
# Given the **American** spelling of a word ending in "ze", count how many times **both the 
# American and British** variants occur in a set of sentences.
#
# Input:
# - First line: integer N (number of lines)
# - Next N lines: sequences of lowercase words
# - Next line: integer T (number of test queries)
# - Next T lines: each contains an American English word ending in "ze"
#
# Output:
# For each test word, print the total number of occurrences of both:
#   - American spelling (ending in "ze")
#   - British spelling (same word but ending in "se")
#
# Constraints:
# - 1 ≤ N ≤ 10
# - Each line ≤ 10 words
# - All words are lowercase alphabets
# - 1 ≤ T ≤ 10
# - Word length ≤ 20
# - Test word always ends with "ze"
#
# Example:
# Input:
# 2
# he will analyze the data
# she must analyse it properly
# 1
# analyze
#
# Output:
# 2


# Solution

import re

n = int(input())
lines = [input() for _ in range(n)]  # Store all lines

t = int(input())

for _ in range(t):
    american = input()             # Word ending in "ze"
    british = american[:-2] + "se" # Replace trailing "ze" with "se"

    # Match whole-word American OR British spelling
    pattern = rf'\b(?:{american}|{british})\b'

    total = 0
    for line in lines:
        total += len(re.findall(pattern, line))
    print(total)

# Intuition:
# - US version ends with "ze"
# - UK version ends with "se"
# - We simply replace the final "ze" → "se" to form the British version
#
# Explanation:
# 1. british = american[:-2] + "se"
#    - Cuts off "ze", appends "se".
# 2. pattern = r'\b(?:american|british)\b'
#    - Matches either variant as a whole word.
# 3. re.findall() counts occurrences in every sentence.
# 4. Sum all counts and print.

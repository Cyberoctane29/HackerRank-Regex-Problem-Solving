# Problem: Saying Hi  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Filtering  

# Problem Statement:
# Given a set of sentences, identify and print those that satisfy the following pattern:
#
# 1. The **first character** must be 'H' or 'h'.
# 2. The **second character** must be 'I' or 'i'.
# 3. The **third character** must be a space (`\s`).
# 4. The **fourth character** must **not** be 'D' or 'd'.
#
# Essentially, a sentence should start with "Hi " or "hi " followed by a word that does **not**
# begin with 'D' or 'd'.
#
# Input Format:
# - The first line contains an integer `n`, the number of sentences.
# - The next `n` lines each contain one sentence `s`.
#
# Output Format:
# - Print each sentence that matches the described pattern.
#
# Constraints:
# - 1 < n ≤ 10
# - Each sentence contains 1 to 10 words.
# - Words consist only of uppercase and lowercase English letters.
#
# Example:
# Input:
# 5
# Hi Alex how are you doing
# hI dave how are you doing
# Good by Alex
# hidden agenda
# Alex greeted Martha by saying Hi Martha
#
# Output:
# Hi Alex how are you doing
#
# Explanation:
# - Sentence 1: ✅ Matches → starts with "Hi " and next letter ('A') is not D/d.
# - Sentence 2: ❌ Fails → next letter is 'd' after "Hi ".
# - Sentence 3: ❌ Fails → doesn’t start with 'H' or 'h'.
# - Sentence 4: ❌ Fails → doesn’t start with 'Hi '.
# - Sentence 5: ❌ Fails → “Hi” appears later, not at start.


# Solution

import re

n = int(input())
pattern = r'^[Hh][Ii]\s[^Dd]'  # Start with "Hi " or "hi ", followed by a non-D/d character

for _ in range(n):
    s = input()
    if bool(re.search(pattern, s)):
        print(s)

# Intuition:
# - We use anchors (^) to ensure the sentence starts with the desired pattern.
# - `[Hh]` → matches 'H' or 'h' (case-insensitive first letter).
# - `[Ii]` → matches 'I' or 'i' (case-insensitive second letter).
# - `\s` → ensures a space follows.
# - `[^Dd]` → ensures the next character after the space is NOT 'D' or 'd'.

# Explanation of Regex:
# 1. `^` → start of the line.
# 2. `[Hh]` → matches 'H' or 'h'.
# 3. `[Ii]` → matches 'I' or 'i'.
# 4. `\s` → matches a single whitespace character (the space).
# 5. `[^Dd]` → matches any character that is NOT 'D' or 'd'.
#
# Together, it ensures the sentence starts exactly with "Hi " (case-insensitive)
# and that the next word doesn’t begin with D/d.

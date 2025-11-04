# Problem: Detect Tweets Containing “hackerrank”  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Matching  

# Problem Statement:
# The popularity of HackerRank can be seen in tweets such as:
# - "I love #hackerrank"
# - "I just scored 27 points in the Picking Cards challenge on #HackerRank"
# - "I just signed up for summer cup @hackerrank"
#
# Given a set of tweets, your task is to determine how many of them contain the string
# **"hackerrank"** (case-insensitive).
#
# Input Format:
# - The first line contains an integer N (number of tweets).
# - The next N lines each contain a valid tweet.
#
# Output Format:
# - Print the total number of tweets that contain "hackerrank" (case-insensitive).
#
# Constraints:
# - 1 ≤ N ≤ 10
# - Each character of a tweet is a valid ASCII character.
#
# Example:
# Input:
# 4
# I love #hackerrank
# I just scored 27 points in the Picking Cards challenge on #HackerRank
# I just signed up for summer cup @hackerrank
# interesting talk by hari, co-founder of hackerrank
#
# Output:
# 4
#
# Explanation:
# All 4 tweets contain the word "hackerrank" in some form (with or without #/@ and in mixed case).
# Hence, the answer is 4.


# Solution 1

import re

n = int(input())
pattern = r'[#@]?[hH][aA][cC][kK][eE][rR]{2}[aA][nN][kK]'
ans = 0

for _ in range(n):
    if bool(re.search(pattern, input())):
        ans += 1
print(ans)

# Intuition:
# - We manually match all possible case combinations of "hackerrank" by writing a case-insensitive pattern.
# - `[#@]?` allows an optional '#' or '@' prefix (like in hashtags or mentions).
#
# Explanation of the Regex:
# - `[#@]?` → matches an optional '#' or '@'
# - `[hH][aA][cC][kK][eE][rR]{2}[aA][nN][kK]` → explicitly matches each letter of "hackerrank" in both cases.
# - re.search() finds if "hackerrank" appears anywhere in the tweet.


# Solution 2

import re

n = int(input())
pattern = r'[#@]?[hackerrankHACKERRANK]{10}'
ans = 0

for _ in range(n):
    if bool(re.search(pattern, input())):
        ans += 1
print(ans)

# Intuition:
# - This pattern tries to detect "hackerrank" by checking a sequence of 10 letters that belong to the set of
#   all upper and lowercase letters in "hackerrank".
#
# Explanation:
# - `[#@]?` → optional '#' or '@'
# - `[hackerrankHACKERRANK]{10}` → matches any 10-letter sequence using only these characters.
# - While functional for simple cases, this approach may overmatch (it doesn't ensure exact order),
#   but it demonstrates another valid regex style.


# Solution 3 (Recommended)

import re

n = int(input())
pattern = r'[#@]?hackerrank'
ans = 0

for _ in range(n):
    if bool(re.search(pattern, input(), re.IGNORECASE)):
        ans += 1
print(ans)

# Intuition:
# - This is the cleanest and most Pythonic approach.
# - Instead of writing out letter cases manually, we use the `re.IGNORECASE` flag to make matching case-insensitive.
#
# Explanation of the Regex:
# 1. `[#@]?` → matches an optional '#' or '@' prefix.
# 2. `hackerrank` → matches the word itself in any case combination.
# 3. `re.IGNORECASE` → ensures the regex engine ignores case when matching.
# 4. The counter increments whenever a tweet contains this substring.

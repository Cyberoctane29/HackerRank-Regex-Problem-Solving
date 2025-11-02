# Problem: IP Address Validation  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Pattern Matching  

# Problem Statement:
# You are given N lines of text that may contain potential IP addresses.
# For each line, determine whether it is:
#   - An IPv4 address
#   - An IPv6 address
#   - Neither of these
#
# IPv4 Format:
# - Four decimal numbers (A.B.C.D)
# - Each number is between 0 and 255 (inclusive)
# - Numbers are separated by dots (.)
#
# IPv6 Format:
# - Eight groups of hexadecimal values (0–9, a–f, A–F)
# - Each group can contain 1 to 4 hexadecimal digits
# - Groups are separated by colons (:)
#
# Input:
# - The first line: integer N (number of potential IP addresses)
# - The next N lines: each contains a string that may be IPv4, IPv6, or neither
#
# Output:
# - For each string:
#     - Print "IPv4" if it’s a valid IPv4 address
#     - Print "IPv6" if it’s a valid IPv6 address
#     - Print "Neither" otherwise
#
# Constraints:
# - N ≤ 50
# - Each input line ≤ 500 characters
#
# Example:
# Input:
# 3
# This line has junk text.
# 121.18.19.20
# 2001:0db8:0000:0000:0000:ff00:0042:8329
#
# Output:
# Neither
# IPv4
# IPv6
#
# Explanation:
# - The first line does not match either format → Neither
# - The second line has 4 valid numbers (121,18,19,20) within 0–255 → IPv4
# - The third line has 8 groups of 1–4 hexadecimal digits → IPv6

# Solution

import re

n = int(input())

# IPv4 pattern: exactly 4 groups of 0–255 separated by dots
ipv4pattern = (
    r'^(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
    r'(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$'
)

# IPv6 pattern: exactly 8 groups of 1–4 hexadecimal digits separated by colons
ipv6pattern = r'^[0-9A-Fa-f]{1,4}(?::[0-9A-Fa-f]{1,4}){7}$'

for _ in range(n):
    s = input().strip()
    if bool(re.search(ipv4pattern, s)):
        print("IPv4")
    elif bool(re.search(ipv6pattern, s)):
        print("IPv6")
    else:
        print("Neither")

# Intuition:
# - The `^` and `$` anchors ensure the entire line must match the pattern (no extra spaces or characters).
# - For IPv4:
#     - Each group represents a valid number between 0 and 255.
#     - The pattern uses alternation to handle different number ranges:
#         - 25[0-5] → matches 250–255
#         - 2[0-4][0-9] → matches 200–249
#         - 1[0-9]{2} → matches 100–199
#         - [1-9]?[0-9] → matches 0–99
#     - The non-capturing group `(?: ... ){3}` ensures 3 additional groups after the first one.
#
# - For IPv6:
#     - `[0-9A-Fa-f]{1,4}` matches 1 to 4 hexadecimal digits per group.
#     - `(?::[0-9A-Fa-f]{1,4}){7}` ensures there are exactly 8 groups separated by colons.
#
# Explanation:
# - `re.search()` is used to test each input line against both patterns.
# - If a line matches the IPv4 regex, print "IPv4".
# - If it matches the IPv6 regex, print "IPv6".
# - If neither matches, print "Neither".
# - The regex ensures strict validation—partial matches or malformed inputs are rejected.

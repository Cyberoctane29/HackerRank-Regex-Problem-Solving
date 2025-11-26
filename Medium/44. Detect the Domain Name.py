# Problem: Detect the Domain Name  
# Difficulty: Medium  
# Skills: Python, Regular Expressions (re module), String Extraction  

# Problem Statement:
# You are given N lines of an HTML fragment. Your task is to extract **unique domain names**
# appearing inside any HTTP/HTTPS URLs in the markup.
#
# Rules:
# - A domain may have multiple levels:  
#       xyz.com  
#       abc.xyz.com  
#       abcd.xyz.com  
#   All must be treated as unique.
#
# - If the URL begins with "www." or "ww2.", these prefixes must be removed.
#
# - URL formats:
#       http://domain/...  
#       https://domain/...  
#
# - Extract only the domain part (not the path).
#
# Input Format:
# - First line: integer N (number of lines)
# - Next N lines: HTML content containing URLs
#
# Output Format:
# - Print unique domain names in **lexicographical order**, separated by semicolons `;`
#
# Example:
# Input:
# http://www.hackerrank.com/contest  
#
# Output:
# hackerrank.com
#
# Constraints:
# - N ≤ 100
# - HTML content length ≤ 10000 chars


# Solution

import re

n = int(input())
text = '\n'.join(input() for _ in range(n))

# Regex: capture domain after http:// or https://
# (?:www\.)? removes optional www.
# Group captures domain with multiple dots, e.g., abc.xyz.com
pattern = r'https?://(?:www\.|ww2\.)?([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)'

ans = set(re.findall(pattern, text))

print(';'.join(sorted(ans)))

# Intuition:
# - Use a capturing group to extract the domain from any HTTP/HTTPS link.
# - Remove optional prefixes: "www." or "ww2.".
# - Allow multi-level domains using: ([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)
# - Store in a set for uniqueness, then sort lexicographically.

# Explanation of Regex:
# 1. `https?://`  
#       Matches either "http://" or "https://".
# 2. `(?:www\.|ww2\.)?`  
#       Non-capturing group; optionally matches "www." or "ww2." at the start.
# 3. `([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)`  
#       - Captures domain name containing labels separated by dots  
#       - Ensures at least one dot → domain.tld  
#       - Supports multi-level domains like "abc.xyz.com"
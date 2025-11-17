# Problem: HTML Link Extractor  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), HTML Parsing

# Problem Statement:
# Given HTML fragments, extract:
#   1. The URL inside each <a href="..."> tag  
#   2. The visible text associated with the link  
#
# The visible text may contain nested tags:
#     <a href="link"><b><i>Text</i></b></a>
# In such cases, strip all tags to get only the pure text.
#
# Input:
# - First line: integer N (number of HTML lines)
# - Next N lines: HTML content
#
# Output:
# For each link:
#   link,text
# (no extra spaces, text is stripped)
#
# Example:
# Input:
# <a href="abc">Hello</a>
# <a href="xyz"><b>Click</b> here</a>
#
# Output:
# abc,Hello
# xyz,Click here


# Solution 1

import re

pattern = r'href="([^"]*)"[^>]*>(.*?)</a>'   # Captures link and inner HTML
remove_tags = r'<[^>]+>'                     # Removes nested tags

n = int(input())
for _ in range(n):
    html = input()

    for link, inner in re.findall(pattern, html):
        text = re.sub(remove_tags, '', inner).strip()
        print(f"{link},{text}")

# Intuition:
# - Find all <a ... href="URL">inner HTML</a> blocks.
# - Extract the link with group(1).
# - Remove all nested tags inside inner HTML using remove_tags.
# - Strip extra spaces and print.


# Explanation:
# 1. pattern:
#    - href="([^"]*)" → captures URL inside quotes.
#    - (.*?)</a>      → captures everything until closing </a> (non-greedy).
#
# 2. remove_tags:
#    - Matches any <...> HTML tag and removes it, leaving only visible text.
#
# 3. Strip whitespace and print "URL,text".


# Solution 2 (compiled regex for efficiency)

import re

pattern = r'href="([^"]*)"[^>]*>(.*?)</a>'
remove_tags = re.compile(r'<[^>]+>')   # Precompiled tag remover

n = int(input())
for _ in range(n):
    html = input()

    for link, inner in re.findall(pattern, html):
        text = remove_tags.sub('', inner).strip()
        print(f"{link},{text}")

# Intuition:
# - Same as Solution 1, but compiled regex speeds up repeated substitution.

# Explanation:
# - re.findall locates all <a href="...">...</a> occurrences.
# - remove_tags.sub removes nested HTML tags efficiently.
# - Output matches required "link,text" format.

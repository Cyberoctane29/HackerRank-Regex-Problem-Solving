# Problem: Detect HTML Tags  
# Difficulty: Medium  
# Skills: Python, Regular Expressions (re module), String Manipulation

# Problem Statement:
# Given N lines of HTML fragments, find all **unique HTML tag names** (ignore attributes)
# and print them as **semicolon-separated values** in **lexicographical order**.
#
# A tag can be:
# - Opening tag: <tag>
# - Closing tag: </tag>
# - Self-closing tag: <tag/>
# - Tags may include spaces or attributes, e.g. < a href="..."> or <div class="...">
#
# Examples of valid tag names:
# - <p>This is a paragraph</p> → tag: p
# - <a href="https://example.com">Link</a> → tag: a
# - <p/> → tag: p
#
# Input:
# - The first line: integer N (number of HTML fragments)
# - Next N lines: HTML fragments
#
# Output:
# - A single line of semicolon-separated unique tag names in lexicographic order.
#
# Constraints:
# - 1 < N ≤ 100
# - Each fragment contains < 10,000 ASCII characters.

# Example:
# Input:
# 2
# <p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
# <div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
#
# Output:
# a;div;p
#
# Explanation:
# - First line has tags: p, a
# - Second line has tags: div, a
# - Unique tags: {a, div, p}
# - Sorted lexicographically: a;div;p

# Boilerplate provided by HackerRank:
# import re
# n = int(input())
# pattern = r"_________"
# matches = []
# for _ in range(n):
#     line = input()
#     matches += re.findall(pattern, line)
# unique = sorted(set(matches))
# print(";".join(unique))


# Solution 1

import re

n = int(input())
pattern = r'<\s*([a-zA-Z0-9]+)'  # Capture tag names, ignoring attributes and closing slashes
matches = []
for _ in range(n):
    line = input()
    matches += re.findall(pattern, line)

unique = sorted(set(matches))
print(";".join(unique))

# Intuition:
# - HTML tags start with '<' and contain the tag name before any space, '>', or '/'.
# - The regex `<\s*([a-z0-9]+)` captures this tag name:
#     - `<\s*` → allows optional spaces after '<'
#     - `([a-z0-9]+)` → captures one or more lowercase letters or digits (the tag name)
#
# Explanation:
# - re.findall() returns all matches of tag names per line.
# - We accumulate matches in a list.
# - Convert to a set to remove duplicates.
# - Sort lexicographically.
# - Join with ';' to print in the required format.

# Solution 2 (Alternative approach using sys.stdin)

import sys, re

data = sys.stdin.read()  
pattern = r'<\s*([a-zA-Z0-9]+)'  # Supports both lowercase and uppercase tag names
matches = re.findall(pattern, data)
unique = sorted(set(matches))
print(";".join(unique))

# Intuition:
# - Instead of reading N line by line, we read all input at once using sys.stdin.read().
# - The regex allows both uppercase and lowercase letters in tag names.
#
# Explanation:
# - `re.findall()` extracts all tag names from the entire HTML input.
# - We use `set()` to remove duplicates and `sorted()` for lexicographic order.
# - Output is printed as semicolon-separated unique tag names.
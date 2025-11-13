# Problem: Detect HTML Attributes  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), HTML Parsing  

# Problem Statement:
# Given an HTML fragment, extract:
#   1. Every HTML tag name  
#   2. All attributes belonging to that tag  
#
# Requirements:
# - Print each unique tag in **lexicographic order**.
# - For each tag, print its attributes (if any) also in **lexicographic order**.
# - If a tag has no attributes, print just:  tag:
# - Attributes consist only of lowercase letters.
#
# Input:
# - First line: integer N (number of HTML lines)
# - Next N lines: HTML fragment (from Wikipedia-like markup)
#
# Output Format:
# tag1:attrA,attrB,attrC
# tag2:attrA
# tag3:
# ...
#
# Example:
# Input:
# 2
# <p><a href="...">Example</a></p>
# <div class="box"><a href="...">More</a></div>
#
# Output:
# a:href
# div:class
# p:

# Solution

import re

tags = {}
n = int(input())
html = '\n'.join(input() for _ in range(n))

# Pattern to capture:
#   group(1) → tag name  
#   group(2) → everything inside tag after tag name
tags_pattern = r"<([a-z0-9]+)([^>]*)>"

# Pattern to extract attribute names (lowercase only)
attr_pattern = r"\s([a-z]+)="

# Extract tags and their raw attribute sections
for tag, attrs in re.findall(tags_pattern, html):
    tags.setdefault(tag, set())  # ensure tag exists in dictionary
    for attr in re.findall(attr_pattern, attrs):
        tags[tag].add(attr)

# Print output sorted lexicographically
for tag in sorted(tags):
    print(f"{tag}:{','.join(sorted(tags[tag]))}")

# Intuition:
# - We scan HTML for `<tag ...>` patterns.
# - For each found tag, extract the substring containing the attributes.
# - Then extract attribute names using the `attr_pattern`.
# - Use a dictionary of sets to de-duplicate attributes for each tag.

# Explanation:
# 1. tags_pattern:
#    - `<([a-z0-9]+)` captures the tag name.
#    - `([^>]*)>` captures everything until closing ">",
#      which may include attributes.
#
# 2. attr_pattern:
#    - `\s([a-z]+)=` finds attributes of the form `attr=`.
#      Attribute names must be lowercase alphabetic.
#
# 3. Store attributes in sets to avoid duplicates.
# 4. Sort tags and attribute lists before printing to satisfy lexicographic order.

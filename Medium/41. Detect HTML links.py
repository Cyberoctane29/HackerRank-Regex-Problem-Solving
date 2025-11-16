# Problem: Detect HTML Links and Text Names  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), HTML Parsing  

# Problem Statement:
# Charlie must extract:
#   1. The hyperlink URL from each <a href="..."> tag.
#   2. The visible text associated with the link.
#
# Important:
# - The text may be nested inside multiple inner HTML tags.
#   Example:
#       <a href="..."><h1><b>HackerRank</b></h1></a>
#   The visible text is: HackerRank
#
# Input:
# - First line: integer N (number of lines)
# - Next N lines: HTML fragment
#
# Output:
# - One line per hyperlink found:
#       link,text
#   The link and the text must have no surrounding spaces.
# - Order of output must match the order links appear in the HTML.
#
# Notes:
# - Some links may have empty or missing text → print: link,
# - Nested tags inside the link text must be removed.
# - Input size ≤ 10000 characters.

# Solution

import re

# Pattern:
#   href="URL" ... > inner HTML text </a>
pattern = r'href="([^"]*)"[^>]*>(.*?)</a>'

# Pattern to remove all inner HTML tags to extract visible text
remove_tags = re.compile(r'<[^>]+>')

n = int(input())

for _ in range(n):
    html = input()

    # Find each hyperlink (URL + inner HTML content)
    for link, inner in re.findall(pattern, html):
        # Remove nesting tags inside the inner text
        text = remove_tags.sub('', inner).strip()
        print(f"{link},{text}")

# Intuition:
# - The outer regex extracts:
#     group(1): the URL inside href=""
#     group(2): everything between > and </a> (may include nested tags)
# - We then remove all inner tags (e.g., <b>, <h1>, <span>…) using another regex.
# - Strip extra spaces.
#
# Explanation of the Regex:
# 1. href="([^"]*)"
#       - Captures any URL inside the href attribute.
# 2. [^>]*>
#       - Allows other optional attributes before closing '>'.
# 3. (.*?)
#       - Non-greedy capture of the text inside the <a>...</a>.
# 4. </a>
#       - Ensures we match until closing tag.
#
# The extracted inner text may still contain tags, so:
#   remove_tags = re.compile(r'<[^>]+>')
#   removes all <...> occurrences, leaving visible text only.

# Problem: Build a Stack Exchange Scraper  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), HTML Parsing  

# Problem Statement:
# Stack Exchange hosts countless question libraries covering a wide range of topics.
# Given an HTML fragment representing a Stack Exchange question listing page,  
# your task is to **extract and print details for each question** in the order they appear.
#
# For each question, extract the following:
# 1. **Identifier** – the unique question ID (from `id="question-summary-XXXX"`)
# 2. **Question text** – the question title (inside the hyperlink with class `question-hyperlink`)
# 3. **Time** – the relative time the question was asked (inside `<span class="relativetime">...</span>`)
#
# Input Format:
# - The input is a block of HTML (read via standard input).
#
# Output Format:
# - Each output line contains:
#     ```
#     ID;Question Text;Time
#     ```
#   with each field separated by a semicolon `;`,  
#   and no leading or trailing spaces in each field.
#
# Constraints:
# - The markup will be similar to the example fragment (possibly with 100 questions max).
# - The input will be valid HTML markup.
#
# Example:
# Input (truncated HTML fragment):
#   <div class="question-summary" id="question-summary-80407">
#       ...
#       <h3><a href="/questions/80407/about-power-supply-of-operational-amplifier" class="question-hyperlink">
#           about power supply of operational amplifier
#       </a></h3>
#       ...
#       <span class="relativetime">11 hours ago</span>
#   </div>
#
#   <div class="question-summary" id="question-summary-80405">
#       ...
#       <h3><a href="/questions/80405/5v-regulator-power-dissipation" class="question-hyperlink">
#           5V Regulator Power Dissipation
#       </a></h3>
#       ...
#       <span class="relativetime">11 hours ago</span>
#   </div>
#
# Output:
# 80407;about power supply of operational amplifier;11 hours ago  
# 80405;5V Regulator Power Dissipation;11 hours ago
#
# Explanation:
# - Extracted the question ID (80407, 80405)
# - Extracted the corresponding question title text from the hyperlink
# - Extracted the relative time (e.g., “11 hours ago”)
# - Output matches the sequence of questions in the original markup.


# Solution

import re
import sys

pattern = (
    r'id="question-summary-(\d+)".*?'               # Capture the numeric ID
    r'class="question-hyperlink"[^>]*>([^<]+)</a>.*?'  # Capture question title text
    r'class="relativetime"[^>]*>([^<]+)</span>'     # Capture time string
)

html = sys.stdin.read()  # Read the entire input HTML
matches = re.findall(pattern, html, re.DOTALL)  # Use DOTALL to match across newlines

for match in matches:
    print(';'.join(match))

# Intuition:
# - The HTML for each question follows a consistent structure:
#   ID → title link → time span.
# - We can use a single regex to capture all three parts together.
#
# Explanation of the Regex:
# 1. `id="question-summary-(\d+)"`  
#    → Captures the numeric identifier after `question-summary-`.
# 2. `.*?class="question-hyperlink"[^>]*>([^<]+)</a>`  
#    → Captures the visible question text between `<a>` and `</a>`.
# 3. `.*?class="relativetime"[^>]*>([^<]+)</span>`  
#    → Captures the time string displayed inside the `<span>` tag.
# - `.*?` → non-greedy wildcard to handle variable HTML spacing/newlines.
# - `re.DOTALL` → allows `.` to also match newlines since the markup may span multiple lines.
#
# The script then prints the extracted data in the required `ID;Question;Time` format,
# preserving the order in which questions appear in the HTML.

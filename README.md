# 🧠 HackerRank Regex Problem Solving

Welcome to my **HackerRank Regex Problem Solving** repository!

This repository contains my **Python Regular Expressions (Regex)** problem-solving approach and solutions to HackerRank challenges, systematically categorized by difficulty level:

- **Easy**
- **Medium**

Each problem has its own dedicated Python file, which includes:

- **Problem Explanation** – A brief overview of the problem statement.
- **Solution Intuition** – The thought process and reasoning behind the regex pattern used.
- **Regex Pattern** – The final working pattern to match the required conditions.
- **Python Code** – A clean and structured implementation.
- **Alternative Patterns** (if applicable) – Other possible solutions or variations for better understanding.

## Why This Repository?

This collection serves as a structured reference for:

- Learning **Regex fundamentals** through real-world problem statements.
- Understanding how different **regex tokens and boundaries** work in practice.
- Exploring **pattern optimizations** and alternative approaches.
- Building strong **regex problem-solving intuition** for interviews and assessments.

## Repository Structure

```python
# HackerRank-Regex-Solutions/
# │── Easy/
# │   ├── problem_name_1.py
# │   ├── problem_name_2.py
# │── Medium/
# │   ├── problem_name_3.py
# │   ├── problem_name_4.py
```
## Example Solution Format

```python
# Problem: [Problem Title]
# Difficulty: [Easy/Medium]
# Skills: Python, Regular Expressions (re module)

# Problem Statement:
# [Provide a brief description of the problem. Include requirements such as case-sensitivity, 
# whole word matching, boundaries, optional spaces, etc.]

# Example:
# Test String:  [example input string]
# Pattern:      [example regex pattern]
# Match:        [highlighted matches in the input]

# Boilerplate Provided:
# Regex_Pattern = r"_________"  # Do not delete 'r'.
# import re
# Test_String = input()
# match = re.findall(Regex_Pattern, Test_String)
# print("Number of matches :", len(match))

# Solution

Regex_Pattern = r'[your_pattern_here]'  # Do not delete 'r'.

import re

Test_String = input()  # Input comes from HackerRank test cases
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

# Intuition:
# [Explain the thought process behind the chosen regex pattern.
# Mention why it captures the required matches and how it handles different input cases.]

# Explanation:
# [Break down the regex pattern and explain how each part works.
# Describe how re.findall() collects all non-overlapping matches.
# Explain why len(match) gives the correct count or result.]
```

I hope this repository helps you build a strong understanding of **Python regular expressions** and enhances your pattern-matching problem-solving skills.  

Let’s learn and grow together! 🚀 Happy coding! 🎯

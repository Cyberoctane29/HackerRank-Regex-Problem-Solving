# 🧠 HackerRank Regex Problem Solving

Welcome to my **HackerRank Regex Problem Solving** repository!

This repository contains my **Regular Expressions (Regex)** problem-solving approach and solutions to HackerRank challenges, systematically categorized by difficulty level:

- **Easy**
- **Medium**

Each problem has its own dedicated Python or Java file, which includes:

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

```python or java
# HackerRank-Regex-Solutions/
# │── Easy/
# │   ├── problem_name_1.py
# │   ├── problem_name_2.java
# │── Medium/
# │   ├── problem_name_3.py
# │   ├── problem_name_4.java
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

Regex_Pattern = r'[your_regex_here]'  # Do not delete 'r'.

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
```java
// Problem: [Problem Title]
// Difficulty: [Easy/Medium/Hard]
// Skills: Java, Regular Expressions (Pattern & Matcher classes)

// Problem Statement:
// [Provide a concise description of what the regex should match or validate. 
// Include the core rules, constraints, and required structure. 
// Mention whether the regex should match the entire string or just specific parts. 
// Also note any case sensitivity or repetition requirements.]

// Example:
// Test String:  [example input string]
// Pattern:      [example regex pattern]
// Match:        [show what the regex should match or validate]

// Boilerplate Provided:
// import java.io.*;
// import java.util.*;
// import java.util.regex.*;
//
// public class Solution {
//     public static void main(String[] args) {
//         Scanner in = new Scanner(System.in);
//         String testString = in.nextLine();
//         Pattern pattern = Pattern.compile("__________");  // Fill your regex here
//         Matcher matcher = pattern.matcher(testString);
//         System.out.println(matcher.find());  // or matcher.matches(), depending on the problem
//     }
// }

// Solution

import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String testString = scanner.nextLine();
        Pattern pattern = Pattern.compile("[your_regex_here]");
        Matcher matcher = pattern.matcher(testString);

        if (matcher.find()) {  // Use matcher.matches() for full-string validation
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}

// Intuition:
// The goal of this regex is to validate strings that follow a specific structure or format.
// Each component of the regex enforces a particular rule — for instance, numeric ranges,
// fixed-length groups, or consistent separators.
//
// Non-capturing groups `(?:...)` are used for grouping without backreferencing, 
// while capturing groups `(...)` are used when the same pattern must repeat (via backreferences).
// Anchors (^ and $) ensure the regex matches the entire string, not just a substring.
//
// In Java, regex patterns must use double backslashes (e.g., `\\d`, `\\w`, `\\.`) 
// since backslashes are also escape characters in Java string literals.
//
// Backreferences (`\\1`, `\\2`, etc.) enforce consistency by ensuring previously matched 
// separators or groups are repeated identically throughout the string.

// Explanation:
// Here’s what each part of the sample regex does:
//
// ^\\d{2}                   → Ensures the string starts (^) with exactly two digits.
// ((?:---)|-|\\.|:)         → Captures one of the valid separators (---, -, ., or :) as Group 1.
// \\d{2}                    → Matches another pair of digits.
// \\1\\d{2}\\1\\d{2}        → Uses backreference \1 to repeat the same separator consistently 
//                             between all remaining groups of digits.
// $                         → End of string anchor, ensuring nothing extra appears after.
//
// Overall, this pattern ensures that:
// - The string is divided into four two-digit parts.
// - All separators between parts are the same type.
// - Anchors guarantee full-string validation without partial matches.
```

I hope this repository helps you build a strong understanding of **regular expressions** and enhances your pattern-matching problem-solving skills.  

Let’s learn and grow together! 🚀 Happy coding! 🎯

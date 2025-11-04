# Problem: Detecting Valid Latitude and Longitude Pairs
# Difficulty: Easy 
# Skills: Python, Regular Expressions (re module), Pattern Validation  

# Problem Statement:
# You are given N lines of text that may contain coordinates in the form of (X, Y).
# Using regular expressions, determine whether each line contains a valid pair of latitude and longitude.
#
# Format of Coordinates:
# - Always in the form: (X, Y)
# - X → Latitude  → must be in range -90 ≤ X ≤ +90
# - Y → Longitude → must be in range -180 ≤ Y ≤ +180
#
# Additional Rules:
# - X and Y may have a '+' or '-' sign.
# - A single space will exist **after the comma**, but not before or after the parentheses.
# - No unnecessary leading zeros allowed (e.g., -090.00 is invalid).
# - No trailing decimal points allowed (e.g., 90. or 180. are invalid).
# - Decimal points and fractional parts are allowed (e.g., 45.123, -0.0001).
# - No symbols for degrees or directions (N/S/E/W).
#
# Input Format:
# - First line: integer N (number of coordinate lines)
# - Next N lines: each line may contain a potential coordinate pair
#
# Output Format:
# - For each line:
#     - Print "Valid" if the line contains a valid (latitude, longitude) pair
#     - Print "Invalid" otherwise
#
# Constraints:
# - 1 ≤ N ≤ 100
#
# Example:
# Input:
# 12
# (75, 180)
# (+90.0, -147.45)
# (77.11112223331, 149.99999999)
# (+90, +180)
# (90, 180)
# (-90.00000, -180.0000)
# (75, 280)
# (+190.0, -147.45)
# (77.11112223331, 249.99999999)
# (+90, +180.2)
# (90., 180.)
# (-090.00000, -180.0000)
#
# Output:
# Valid
# Valid
# Valid
# Valid
# Valid
# Valid
# Invalid
# Invalid
# Invalid
# Invalid
# Invalid
# Invalid
#
# Explanation:
# - The first 6 inputs are valid because:
#     - They follow the correct syntax `(X, Y)`
#     - X and Y are within their valid numeric ranges
# - The next 6 are invalid due to:
#     - Out-of-range numbers (e.g., 280, 190, 249.99)
#     - Trailing dots (e.g., 90., 180.)
#     - Leading zeros before 90 or 180 (e.g., -090)


# Solution 1

import re

n = int(input())
pattern = (
    r'^\([+-]?(?:90(?:\.0+)?|(?:[1-8][0-9]|[0-9])(?:\.\d+)?),'
    r'\s[+-]?(?:180(?:\.0+)?|(?:1[0-7][0-9]|[1-9]?[0-9])(?:\.\d+)?)\)$'
)

for _ in range(n):
    if bool(re.search(pattern, input())):
        print("Valid")
    else:
        print("Invalid")

# Intuition:
# - This regex checks the structure `(latitude, longitude)` and verifies each number falls in range.
# - It ensures proper syntax and spacing (comma followed by a single space).
#
# Explanation of the Regex:
# 1. `^\(` and `\)$` → Enforces parentheses around the pair.
# 2. `[+-]?` → Optional sign for both latitude and longitude.
# 3. Latitude (X):
#     - `90(?:\.0+)?` → Matches 90 or 90.0 or 90.0000 etc.
#     - `(?:[1-8][0-9]|[0-9])(?:\.\d+)?` → Matches 0–89.999...
# 4. `,\s` → Enforces comma followed by a single space.
# 5. Longitude (Y):
#     - `180(?:\.0+)?` → Matches 180 or 180.0 or 180.0000 etc.
#     - `(?:1[0-7][0-9]|[1-9]?[0-9])(?:\.\d+)?` → Matches 0–179.999...
# - The pattern is strict, disallowing invalid formats like extra dots or leading zeros.


# Solution 2

import re

n = int(input())
pattern = (
    r'^\([+-]?(?:90(?:\.0+)?|[1-8]?\d(?:\.\d+)?),\s'
    r'[+-]?(?:180(?:\.0+)?|(?:1[0-7]\d|[1-9]?\d)(?:\.\d+)?)\)$'
)

for _ in range(n):
    if bool(re.search(pattern, input())):
        print("Valid")
    else:
        print("Invalid")

# Intuition:
# - This version simplifies and slightly optimizes the earlier regex, while keeping the same logic.
# - It matches valid latitude and longitude pairs within required ranges and format constraints.
#
# Explanation of the Regex:
# 1. `^\(` and `\)$` → Ensures coordinates are enclosed in parentheses.
# 2. `[+-]?` → Optional plus or minus sign.
# 3. Latitude (X):
#     - `90(?:\.0+)?` → Allows 90 or 90.0 etc.
#     - `[1-8]?\d(?:\.\d+)?` → Covers 0–89.999... range.
# 4. `,\s` → Exactly one comma followed by a space.
# 5. Longitude (Y):
#     - `180(?:\.0+)?` → Matches 180 or 180.0 etc.
#     - `(?:1[0-7]\d|[1-9]?\d)(?:\.\d+)?` → Matches 0–179.999...
# - The pattern ensures precise control over valid latitude-longitude formatting and range compliance.

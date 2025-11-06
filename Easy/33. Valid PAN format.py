# Problem: Valid PAN Format  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Validation  

# Problem Statement:
# The Permanent Account Number (PAN) is a unique 10-character alphanumeric identifier issued in India.  
# The valid format of a PAN number is as follows:
# <char><char><char><char><char><digit><digit><digit><digit><char>
#
# Rules for a valid PAN:
# 1. The first 5 characters must be uppercase English letters (A–Z).
# 2. The next 4 characters must be digits (0–9).
# 3. The last character must be an uppercase English letter (A–Z).
# 4. The PAN must contain exactly 10 characters — no more, no less.
#
# Input Format:
# - The first line contains an integer N (number of PAN numbers to check).
# - The next N lines each contain one PAN number.
#
# Output Format:
# - For each PAN number:
#     - Print "YES" if it is valid.
#     - Print "NO" otherwise.
#
# Constraints:
# - 1 < N ≤ 10
# - Each PAN number length = 10
# - Characters are alphanumeric (A–Z, 0–9)
#
# Example:
# Input:
# 3
# ABCDS1234Y
# ABAB12345Y
# avCDS1234Y
#
# Output:
# YES
# NO
# NO
#
# Explanation:
# - "ABCDS1234Y" → ✅ Valid (5 uppercase letters, 4 digits, 1 uppercase letter)
# - "ABAB12345Y" → ❌ Invalid (5th character is a digit, not a letter)
# - "avCDS1234Y" → ❌ Invalid (contains lowercase letters)


# Solution 1

import re

n = int(input())
pattern = r'^[A-Z]{5}\d{4}[A-Z]$'  # Strict format: 5 uppercase letters, 4 digits, 1 uppercase letter

for _ in range(n):
    if bool(re.search(pattern, input())):
        print("YES")
    else:
        print("NO")

# Intuition:
# - Use regex anchors ^ and $ to ensure the full PAN number matches exactly 10 characters.
# - [A-Z]{5} → first 5 uppercase letters.
# - \d{4} → next 4 digits.
# - [A-Z] → last uppercase letter.
#
# Explanation:
# - re.search() checks if the string matches the full PAN structure.
# - bool() converts the match result to True or False.
# - Prints "YES" for valid, "NO" for invalid formats.


# Solution 2

import re

n = int(input())
pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'  # Alternative: same logic but uses [0-9] instead of \d

for _ in range(n):
    if bool(re.search(pattern, input())):
        print("YES")
    else:
        print("NO")

# Intuition:
# - [0-9] explicitly matches digits 0 through 9 (equivalent to \d but more readable in some contexts).
#
# Explanation:
# - The regex enforces uppercase letters and digit positions exactly as per PAN rules.
# - Anchors ^ and $ ensure there are no extra or missing characters.
# - Both patterns produce identical results — the difference is stylistic preference.

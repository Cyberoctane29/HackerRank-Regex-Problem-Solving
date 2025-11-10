# Problem: Split the Phone Numbers  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), Group Capturing  

# Problem Statement:
# You are given a list of valid phone numbers in a specific format.  
# Your task is to extract and print the **Country Code**, **Local Area Code**, and **Number** from each phone number.
#
# Phone Number Format:
# [Country code]-[Local Area Code]-[Number]
#
# Rules:
# - Segments may be separated by either a hyphen `-` or a space ` `.
# - Country code: 1–3 digits.
# - Local area code: 1–3 digits.
# - Number: 4–10 digits.
#
# Input Format:
# - First line: integer N (number of phone numbers)
# - Next N lines: each contains a phone number in one of the valid formats
#
# Output Format:
# - For each phone number, print:
#   CountryCode=[Country Code],LocalAreaCode=[Local Area Code],Number=[Number]
#
# Constraints:
# - 1 ≤ N ≤ 20
#
# Example:
# Input:
# 2
# 1 877 2638277
# 91-011-23413627
#
# Output:
# CountryCode=1,LocalAreaCode=877,Number=2638277
# CountryCode=91,LocalAreaCode=011,Number=23413627
#
# Explanation:
# - The regex separates the input into three groups:
#   - Group 1 → Country code
#   - Group 2 → Local area code
#   - Group 3 → Number
# - It correctly handles both spaces and hyphens between segments.


# Solution 1

import re

n = int(input())
pattern = r'^(\d{1,3})(?:-|\s)(\d{1,3})(?:-|\s)(\d{4,10})$'

for _ in range(n):
    s = input()
    s1 = re.search(pattern, s).group(1)
    s2 = re.search(pattern, s).group(2)
    s3 = re.search(pattern, s).group(3)
    print(f"CountryCode={s1},LocalAreaCode={s2},Number={s3}")

# Intuition:
# - The regex `(\d{1,3})` captures 1–3 digits for the first two groups (country and area codes).
# - `(\d{4,10})` captures 4–10 digits for the phone number.
# - `(?:-|\s)` is a non-capturing group that allows either a hyphen or a space as a separator.
#
# Explanation:
# - re.search(pattern, s) finds the pattern in each input line.
# - group(1), group(2), and group(3) correspond to the respective parts of the number.
# - The formatted output prints the extracted segments.


# Solution 2

import re

n = int(input())
pattern = r'^(\d{1,3})(?:-|\s)(\d{1,3})(?:-|\s)(\d{4,10})$'

for _ in range(n):
    match = re.search(pattern, input())
    s1, s2, s3 = match.groups()
    print(f"CountryCode={s1},LocalAreaCode={s2},Number={s3}")

# Intuition:
# - Instead of calling re.search() multiple times, we call it once per line.
# - `.groups()` returns a tuple of all captured groups in the match (country, area, number).
#
# Explanation:
# - This version is cleaner and more efficient.
# - Both versions yield identical output, but this one avoids redundant regex lookups.

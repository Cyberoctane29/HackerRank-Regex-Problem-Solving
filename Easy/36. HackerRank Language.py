# Problem: Valid Programming Language Field  
# Difficulty: Easy  
# Skills: Python, Regular Expressions (re module), String Validation  

# Problem Statement:
# Every submission at HackerRank includes a "language" field indicating the programming language 
# used by the hacker. However, sometimes API requests contain invalid or misspelled language fields.
# You must determine whether a given API request contains a valid language field.
#
# The valid languages (case-sensitive) are:
# C, CPP, JAVA, PYTHON, PERL, PHP, RUBY, CSHARP, HASKELL, CLOJURE, BASH, SCALA,
# ERLANG, CLISP, LUA, BRAINFUCK, JAVASCRIPT, GO, D, OCAML, R, PASCAL, SBCL, DART,
# GROOVY, OBJECTIVEC
#
# Input Format:
# - The first line contains an integer N (number of API requests).
# - The next N lines each contain:
#     api_id language
#   where `api_id` is an integer (10^4 ≤ api_id < 10^5) 
#   and `language` is a string indicating the language.
#
# Output Format:
# - For each API request:
#     - Print "VALID" if the language field is valid.
#     - Print "INVALID" otherwise.
#
# Constraints:
# - 1 ≤ N ≤ 100
# - 10000 ≤ api_id < 100000
#
# Example:
# Input:
# 3
# 11011 LUA
# 11022 BRAINFUCK
# 11044 X
#
# Output:
# VALID
# VALID
# INVALID
#
# Explanation:
# - LUA and BRAINFUCK are valid languages as per the list.
# - X is not in the valid list, so it’s invalid.


# Solution 1

import re

n = int(input())

# Regex pattern containing all valid languages (case-sensitive)
valid_pattern = (
    r'^(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|'
    r'ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|'
    r'GROOVY|OBJECTIVEC)$'
)

# Extract language part from the line (the word after the space)
line_pattern = r'\s([A-Z]+)$'

for _ in range(n):
    s = input()
    lang = re.search(line_pattern, s)
    if lang:
        language = lang.group(1)
        if re.search(valid_pattern, language):
            print("VALID")
        else:
            print("INVALID")
    else:
        print("INVALID")

# Intuition:
# - Each line has an `api_id` followed by a language name.
# - We extract the last word (language) using `line_pattern`.
# - Then, we check if it matches one of the predefined valid languages in `valid_pattern`.
#
# Explanation:
# 1. `line_pattern = r'\s([A-Z]+)$'`
#    - `\s` → Matches the space before the language.
#    - `([A-Z]+)` → Captures one or more uppercase letters (the language name).
#    - `$` → Ensures it’s at the end of the line.
#
# 2. `valid_pattern` → Matches any of the valid language names listed.
#    - Uses alternation `|` inside parentheses to define valid options.
#    - Anchored with `^` and `$` to ensure full string match.
#
# The script checks each line, extracts the language, and prints "VALID" or "INVALID" accordingly.


# Solution 2

import re

n = int(input())
valid_pattern = (
    r'^(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|'
    r'ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|'
    r'GROOVY|OBJECTIVEC)$'
)

for _ in range(n):
    api_id, s = input().split()
    if re.search(valid_pattern, s):
        print("VALID")
    else:
        print("INVALID")

# Intuition:
# - This approach splits each line into two parts directly: `api_id` and `language`.
# - It eliminates the need for an additional regex to extract the language.
#
# Explanation:
# - The language part (`s`) is directly matched against the `valid_pattern`.
# - If it matches one of the valid listed languages → print "VALID".
# - Otherwise → print "INVALID".
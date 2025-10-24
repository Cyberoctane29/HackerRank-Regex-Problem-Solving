// Problem: Branch Reset Groups  
// Difficulty: Easy  
// Skills: Regular Expressions (Advanced Grouping)

// Problem Statement:
// Given a test string `S`, write a regex that matches `S` under the following rules:
// - `S` consists of **8 digits**.
// - It must contain a separator that can be **“---”**, **“-”**, **“.”**, or **“:”**.
// - The string must be divided into **4 parts**, each having exactly **2 digits**.
// - The string must use **only one type** of separator throughout.
// - Separators must have digits on both sides (no separator at start or end).
//
// Valid examples:
// - `12-34-56-78`
// - `12:34:56:78`
// - `12---34---56---78`
// - `12.34.56.78`
//
// Invalid examples:
// - `1-234-56-78` → first part not 2 digits
// - `12-45.78:10` → mixed separators
//
// This is a regex-only challenge; no additional code logic is required.

// Example:
// Pattern:  ^\d{2}((?:---)|-|.|:)\d{2}\1\d{2}\1\d{2}$
// Test String:  12-34-56-78
// Match: ✅ 12-34-56-78

// Explanation of `(?:---)|-|.|:`:
// - `(?:...)` creates a **non-capturing group**, meaning it groups without capturing.
// - The alternation `|` allows choosing between multiple separator options.
// - The entire group `((?:---)|-|.|:)` is captured as **Group 1**.
// - The backreference `\1` ensures that **the same separator** repeats consistently.
//
// Anchors:
// - `^` → start of the string.
// - `$` → end of the string, ensuring full-string match.

// Boilerplate provided by HackerRank (Java):

import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        Pattern pattern = Pattern.compile("^\\d{2}((?:---)|-|.|:)\\d{2}\\1\\d{2}\\1\\d{2}$");
        Matcher matcher = pattern.matcher(s);
        if (matcher.matches()) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}

// ✅ Intuition:
// The goal is to ensure the string contains only one kind of separator between fixed-length numeric parts.
// To achieve this:
// - I used `((?:---)|-|.|:)` to match any one of the allowed separators.
// - The backreference `\1` guarantees the same separator repeats between all numeric pairs.

// ✅ Explanation:
// - `^\d{2}` → two digits at the start.
// - `((?:---)|-|.|:)` → captures one of the allowed separators as Group 1.
// - `\d{2}` → next two digits.
// - `\1` → ensures the same separator appears again.
// - `\d{2}\1\d{2}` → repeats the pattern two more times for all four parts.
// - `$` → end of string anchor ensuring the match spans the entire string.
//
// Thus, it matches valid strings like:
// - `12-34-56-78`
// - `12.34.56.78`
// and rejects invalid ones with inconsistent or misplaced separators.

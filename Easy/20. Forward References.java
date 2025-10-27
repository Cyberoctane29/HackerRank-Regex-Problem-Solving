// Problem: Forward References  
// Difficulty: Hard  
// Skills: Regular Expressions (Advanced Backreferences and Lookaheads)

// Problem Statement:
// Given a test string `S`, write a regex that matches `S` under the following rules:
// - `S` consists of the words **tic** or **tac** only.
// - The word **tic** cannot be an immediate neighbour of itself (i.e., no consecutive `tictic`).
// - The **first** occurrence of `tic` must appear **only after** at least two `tac` occurrences.
//
// Valid examples:
// - ✅ `tactactic`
// - ✅ `tactactictactic`
//
// Invalid examples:
// - ❌ `tactactictactictictac` → multiple consecutive `tic` or misplaced `tic`
// - ❌ `tactictac` → first `tic` occurs before two `tac`
//
// Example:  
// Pattern → `(\2amigo|(go!))+`  
// Test String → `go!go!amigo`  
// Here, the regex uses a **forward reference** `\2` before group (2) is defined.

// ─────────────────────────────────────────────────────────────

// ✅ Solution 1 — Using Forward Reference

import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        Pattern pattern = Pattern.compile("^(\\2tic|(tac))+$");
        Matcher matcher = pattern.matcher(s);
        if (matcher.matches()) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}

// ✅ Intuition (Solution 1):
// - `(\2tic|(tac))` → this uses a **forward reference**.
// - `\2` refers to the **second capturing group**, even though it appears later.
// - The pattern ensures that `tic` only appears *after* `tac` has been matched (since `\2` refers to `(tac)`).
// - `+` repeats the pattern, allowing multiple `tac` and occasional `tic` only after conditions are met.
// - The forward reference mechanism enforces sequencing without explicit counters.

// ✅ Explanation:
// - `^` and `$` → anchors ensure the pattern matches the entire string.
// - `(tac)` → Group 2, matches “tac”.
// - `(\2tic|(tac))` → Group 1, matches either:
//   - `\2tic` → “tactic” (allowed only after `tac` has occurred at least twice)
//   - `(tac)` → “tac”
// - The use of forward reference `\2` guarantees order dependency between `tac` and `tic`.

// ─────────────────────────────────────────────────────────────

// ✅ Solution 2 — Using Quantifiers and Lookaheads (Alternative Logic)

import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        Pattern pattern = Pattern.compile("^(tac){2,}(tic(?!tic)|tac)*$");
        Matcher matcher = pattern.matcher(s);
        if (matcher.matches()) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}

// ✅ Intuition (Solution 2):
// - `(tac){2,}` → ensures at least two “tac” before anything else (satisfying the first condition).
// - `(tic(?!tic)|tac)*` → allows repeating “tac” or “tic”, but prevents “tictic” (due to `(?!tic)` lookahead).
// - This approach avoids forward references by using logical ordering and negative lookaheads.

// ✅ Explanation:
// - `^` → start of string.
// - `(tac){2,}` → must start with two or more “tac” sequences.
// - `(tic(?!tic)|tac)*` → after that, any number of “tac” or isolated “tic” (not followed by another “tic”).
// - `$` → end of string.
// - This satisfies all problem conditions without relying on advanced forward-reference behavior.

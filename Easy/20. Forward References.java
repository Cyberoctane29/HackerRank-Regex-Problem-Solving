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
// - tactactic
// - tactactictactic
//
// Invalid examples:
// - tactactictactictictac → multiple consecutive “tic” or misplaced “tic”
// - tactictac → first “tic” occurs before two “tac”
//
// Example:
// Pattern:  (\2amigo|(go!))+  
// Test String:  go!go!amigo  
// Here, the regex uses a forward reference `\2` before group (2) is defined.

// ─────────────────────────────────────────────────────────────

// Solution 1 — Using Forward Reference

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

// Intuition (Solution 1):
// - (\2tic|(tac)) uses a forward reference.
// - \2 refers to the second capturing group (tac), even though it appears later.
// - Ensures “tic” appears only after “tac” has already been matched.
// - The + quantifier repeats the pattern, allowing multiple “tac” and occasional “tic”.
// - Forward reference enforces sequencing without counters.

// Explanation:
// - ^ and $ anchor the match to the full string.
// - (tac) is Group 2.
// - (\2tic|(tac)) is Group 1, matching either “tactic” or “tac”.
// - The forward reference \2 guarantees order dependency between “tac” and “tic”.

// ─────────────────────────────────────────────────────────────

// Solution 2 — Using Quantifiers and Lookaheads (Alternative Logic)

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

// Intuition (Solution 2):
// - (tac){2,} ensures at least two “tac” before anything else.
// - (tic(?!tic)|tac)* allows “tac” or isolated “tic”, but prevents “tictic” using a negative lookahead.
// - This method avoids forward references entirely and uses logical ordering.

// Explanation:
// - ^ → start anchor.
// - (tac){2,} → requires two or more “tac” at the start.
// - (tic(?!tic)|tac)* → repeats “tac” or single “tic”.
// - $ → end anchor.
// - Fulfills all problem conditions with a simpler, more portable pattern.

// ─────────────────────────────────────────────────────────────

// Solution 3 — Simplified Pattern Logic

import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        Pattern pattern = Pattern.compile("^(tac)(tactic|tac)+$");
        Matcher matcher = pattern.matcher(s);
        if (matcher.matches()) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}

// Intuition (Solution 3):
// - Starts with one “tac” to ensure the sequence begins correctly.
// - (tactic|tac)+ repeats either “tactic” or “tac” for the rest of the string.
// - This indirectly ensures that “tic” appears only after “tac” has occurred at least once before.

// Explanation:
// - ^ and $ → match the full string.
// - (tac) → ensures the string starts with “tac”.
// - (tactic|tac)+ → repeats valid “tac” or “tactic” segments.
// - Though simpler, it still maintains proper sequencing and avoids consecutive “tic”.

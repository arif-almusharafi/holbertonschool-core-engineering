# Offline Guide — Control Flow

No solutions are included here. Focus on conditions, loop boundaries, and exact formatting. Project rules also forbid functions and imports unless the task explicitly supplies the random-import line.

## Task 0 — Positive, Zero, or Negative

**Concept:** `if / elif / else` chooses exactly one branch. Compare the supplied random `number` against zero and print the matching description.

**Think about:** The three cases are mutually exclusive: greater than zero, equal to zero, and less than zero. Preserve the supplied random line exactly.

**Check:** Run the script many times because the value changes. Verify positive, negative, and zero formatting when those cases appear.

## Task 1 — The Last Digit

**Concept:** You need both digit extraction and conditional classification. Python's behavior with negative numbers deserves special attention because the expected last digit for a negative number is negative.

**Think about:** Work out examples on paper for positive and negative values before coding. After obtaining the correct signed last digit, classify it as greater than 5, equal to 0, or less than 6 and not 0.

**Check:** Test representative positive, negative, and zero-ending numbers. Exact wording matters.

## Task 2 — Alphabet Game

**Concept:** Iterate through character codes and skip unwanted characters using a condition. `ord()` converts a character to its numeric code and `chr()` converts a code back to a character.

**Constraints to watch:** Only one `print` call may appear in your code. Output must remain on one continuous line until the final newline.

**Think about:** A loop can visit the lowercase alphabet range while a condition decides whether the current character should be emitted.

## Task 3 — Hexadecimal Printing

**Concept:** One loop can generate the sequence 0 through 98. Python string formatting can display the same integer in decimal and hexadecimal.

**Useful idea:** Learn the format specifier for hexadecimal rather than manually converting numbers.

**Constraints:** One loop, one `print` function using string formatting, and no storing numbers or strings in variables.

**Check:** Pay special attention to the first value, values around 9/10 and 15/16, and the final value 98.

## Task 4 — 00...99

**Concept:** Fixed-width numeric formatting can add a leading zero. The main formatting challenge is printing separators between values without leaving a comma after the final value.

**Think about:** Your loop needs to distinguish the last iteration from earlier iterations, or otherwise control the `end` behavior of `print`.

**Constraints:** One loop, no more than two formatted `print` calls, no storing numbers or strings in variables.

**Check:** The output begins with two-digit values, uses exactly comma + one space between entries, ends at 99, has no trailing comma, and finishes with a newline.

## Task 5 — Combinations of Two Digits

**Concept:** This is a nested-loop problem. To avoid duplicates such as both 01 and 10, reason about the relationship between the first and second digit.

**Think about:** If the second digit is always later/larger than the first, identical digits and reversed duplicates disappear naturally. You still need special handling for the separator after the final combination.

**Constraints:** At most two loops and three formatted `print` calls.

**Check:** Confirm 00 and 11 never appear, 10 does not appear after 01, ordering is ascending, 89 is last, and there is no trailing comma.

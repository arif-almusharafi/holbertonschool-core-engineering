# Offline Guide — Functions & Modules

These notes explain the reasoning without giving final implementations.

## Task 0 — islower

**Concept:** ASCII character codes allow you to determine whether a character belongs to the lowercase-letter range. `ord(c)` gives the integer code for a character.

**Think about:** A lowercase character must satisfy both a lower boundary and an upper boundary. Return the result as a Boolean; do not print it.

**Check:** Try lowercase letters, uppercase letters, digits, and boundary letters.

## Task 1 — To Uppercase

**Concept:** Uppercase and lowercase ASCII letters have a predictable numeric relationship. Use `ord()` to inspect a character and `chr()` to create the converted character.

**Think about:** Only lowercase letters should be converted; other characters should remain unchanged. The function prints the final characters and ends with a newline. It does not return a useful value.

**Check:** Test lowercase, uppercase, spaces, digits, and mixed strings. Do not use `.upper()`.

## Task 2 — Print Last Digit

**Concept:** Separate two requirements: compute a last digit that is always non-negative, then both print and return that same value.

**Think about:** Negative inputs are the important edge case. Verify your arithmetic manually before writing code.

**Check:** Test positive, negative, zero, and numbers ending in zero. Confirm the printed value has no extra text and the returned value matches it.

## Task 3 — a ^ b

**Concept:** Exponentiation can be understood as repeated multiplication. A loop maintains an accumulated result.

**Think about:** The exponent-zero case is important: ask what value multiplication should start from so that raising a number to zero produces the expected result.

**Constraints:** No `**` and no imports.

**Check:** Test exponent 0, exponent 1, and several positive exponents.

## Task 5 — Import a Simple Function

**Concept:** A module can expose a function that another file imports. Also understand the difference between code that runs during import and code that runs only when the file is executed directly.

**Useful concept:** `__name__` has a special value when a file is the entry-point script. Use the standard main guard to protect executable code.

**Check:** Run `./add.py`, then separately import `add` from a Python session and make sure the script's normal output does not run automatically.

## Task 6 — My First Toolbox

**Concept:** Import several named functions from `calculator_1.py` and call each with the required values. Do not use wildcard imports.

**Think about:** Keep imports explicit and place executable behavior behind the main guard so importing `calculation.py` has no side effects.

**Check:** Verify addition, subtraction, multiplication, and division each appear on their own line and match the required formatting.

## Task 7 — Everything Can Be Imported

**Concept:** Modules can export data as well as functions. Import the named variable from `variable_load_5.py` and display it.

**Constraints:** No wildcard import, and the program must stay silent when imported as a module.

**Check:** Execute the file normally, then import it from another Python session to verify the main guard behavior.

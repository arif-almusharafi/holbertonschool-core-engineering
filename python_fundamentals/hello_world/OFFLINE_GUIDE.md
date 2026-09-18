# Offline Guide — Hello World

Use this guide while solving the task yourself. It explains the concepts and checks, but intentionally does not contain the final solution.

## Task 1 — Deterministic Script Output (`structured_output.py`)

**What to understand:** A Python script can be executed directly when it has the required shebang and executable permission. The task also checks numeric types, Boolean expressions, f-strings, and exact output formatting.

**Approach:** Store the needed values using appropriate Python types. Produce the Boolean from a real comparison rather than writing `True` directly. For the decimal value, use fixed-point formatting so exactly two digits appear after the decimal point. Use formatted string interpolation on at least one line.

**Useful syntax:** Review `print()`, f-strings such as `f"...{value}..."`, comparison operators such as `>`, `<`, and `==`, and float formatting with `.2f`.

**Check yourself:** Run `./structured_output.py` and `python3 structured_output.py`. Confirm there are exactly four lines, no extra spaces or debug text, the file ends with a newline, and the file is executable. You can use `python3 -m py_compile structured_output.py` for syntax and `pycodestyle structured_output.py` if pycodestyle 2.7.x is installed.

**Common mistakes:** Hardcoding the decimal as text, hardcoding the Boolean, forgetting the shebang or executable bit, or producing output that differs by one character.

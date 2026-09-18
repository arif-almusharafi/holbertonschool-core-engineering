# Offline Guide — Core Data Structures

These notes are hints and test ideas, not solutions.

## Task 0 — Print a List of Integers

**Concept:** Iterate through a list and print each element on its own line. The checker specifically expects integer formatting with `:d`.

**Think about:** You do not need to transform the list. Each iteration handles one integer.

**Check:** Test a normal list, a one-item list, negative integers, and an empty list.

## Task 1 — Safe Access to a List Element

**Concept:** Python normally allows negative indexes, but this task explicitly forbids them. Validate the index before accessing the list.

**Think about:** There are two invalid regions: below zero and at/above the list length. Invalid indexes return `None`.

**Check:** Test index 0, the last valid index, -1, exactly `len(my_list)`, and a much larger index.

## Task 2 — Replace an Element in a List

**Concept:** Lists are mutable. A valid index changes the existing list, while an invalid index leaves it unchanged.

**Think about:** Validate before assignment so Python's negative-index behavior does not accidentally modify the wrong element.

**Check:** Test first/last valid positions, negative index, and out-of-range index. Confirm the returned object contains the expected mutation.

## Task 3 — Print a Matrix of Integers

**Concept:** A matrix is a list of rows, so nested iteration is natural: one level chooses the row and another handles its values.

**Formatting challenge:** Values within a row need one space between them, but no unwanted trailing spacing. Each row ends with a newline.

**Check:** Test a 3×3 matrix, a one-row matrix, and empty rows.

## Task 4 — Tuple Addition

**Concept:** Tuples are immutable, so return a new two-item tuple. Inputs may contain fewer than two items, in which case missing positions behave as zero; extra positions are ignored.

**Think about:** Normalize each input conceptually to two usable values before adding corresponding positions.

**Check:** Test two full tuples, one-item tuples, empty tuples, and tuples with more than two values.

## Task 5 — Common Elements in Two Sets

**Concept:** Set intersection represents values that occur in both sets. The result should be a new set.

**Think about:** Python has a set operation designed specifically for intersection. Repeated values are not a concern because sets already enforce uniqueness.

**Check:** Test overlapping sets, disjoint sets, identical sets, and empty sets.

## Task 6 — Update or Add a Dictionary Entry

**Concept:** Dictionary assignment using a key works for both cases: updating an existing key and creating a missing key.

**Think about:** The task expects the dictionary to be updated and returned.

**Check:** First update an existing key, then add a new key, and inspect the returned dictionary after each call.

## Task 7 — Best Score

**Concept:** Dictionaries let you iterate over key/value relationships. Track which key is associated with the largest integer value.

**Think about:** Handle `None` and an empty dictionary before searching. Since values are guaranteed to be different, tie handling is unnecessary.

**Check:** Test a normal score dictionary, one entry, an empty dictionary, and `None`.

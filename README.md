# TextWise Solutions – Recursive String Reversal

## Problem
Implement a function to reverse a string **using recursion** as part of a technical interview exercise.

---

## Clarifying Questions
1. Should non-string inputs be allowed? (Assumed no)
2. Should Unicode characters be supported? (Yes)
3. Should whitespace and punctuation be preserved? (Yes)

---

## Approach
We use recursion with:
- A **base case** for strings of length 0 or 1
- A **recursive case** that reverses the substring excluding the first character

---

## Example
Input: `"abcd"`

Call stack:
- reverse("abcd") → reverse("bcd") + "a"
- reverse("bcd") → reverse("cd") + "b"
- reverse("cd") → reverse("d") + "c"
- reverse("d") → "d"

Output: `"dcba"`

---

## Time & Space Complexity

Let `n` be the length of the string.

- Time Complexity: **O(n²)**  
  Due to string slicing (`s[1:]`) at each recursive call.
- Space Complexity: **O(n)**  
  Due to recursion call stack.

---

## Tests
Tests are written using **pytest** and include:
- 3 normal cases
- 3+ edge cases

Run tests:
```bash
pip install pytest
pytest

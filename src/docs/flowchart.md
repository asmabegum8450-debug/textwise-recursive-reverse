# Recursive String Reversal – Flowchart

Example: "abcd"

reverse("abcd")
→ reverse("bcd") + "a"
→ reverse("cd") + "b" + "a"
→ reverse("d") + "c" + "b" + "a"
→ reverse("") + "d" + "c" + "b" + "a"
→ ""

## Base Case
- Empty string or length 1 → return string

## Recursive Case
- Reverse substring starting at index 1
- Append first character at the end

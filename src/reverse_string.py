def reverse_string_recursive(s: str) -> str:
    """
    Reverse a string using recursion.

    Args:
        s (str): input string

    Returns:
        str: reversed string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Base case
    if len(s) <= 1:
        return s

    # Recursive case
    return reverse_string_recursive(s[1:]) + s[0]

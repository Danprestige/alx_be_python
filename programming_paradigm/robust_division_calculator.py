# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Attempts to divide numerator by denominator.
    Returns:
      - A float result if successful
      - A string error message for invalid input or division by zero
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except (TypeError, ValueError):
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"

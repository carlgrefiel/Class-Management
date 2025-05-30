# arithmetic_operations.py

def validate_number(value):
    """
    Validates that the input is a number (int or float).
    Returns the number if valid, or None if invalid.
    """
    if isinstance(value, (int, float)):
        return value
    print("Error: Invalid input. Only numbers (int or float) are allowed.\n")
    return None

def add(x, y):
    x = validate_number(x)
    y = validate_number(y)
    if x is None or y is None:
        return None
    return x + y

def subtract(x, y):
    x = validate_number(x)
    y = validate_number(y)
    if x is None or y is None:
        return None
    return x - y

def multiply(x, y):
    x = validate_number(x)
    y = validate_number(y)
    if x is None or y is None:
        return None
    return x * y

def divide(x, y):
    x = validate_number(x)
    y = validate_number(y)
    if x is None or y is None:
        return None
    if y == 0:
        print("Error: Cannot divide by zero.\n")
        return None
    return x / y

def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Subtract y from x."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y

def divide(x: float, y: float) -> float:
    """Divide x by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y 
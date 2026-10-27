from collections.abc import Callable

def factorial(n: int | float) -> int | float:
    if n == 0:
        return 1
    elif n == float(n):
        raise ValueError("Input cannot have a decimal.")
    elif n < 0:
        raise ValueError("Input needs to be a nonnegative integer.")
    else:
        return n * factorial(n - 1)

factorial(2.5)
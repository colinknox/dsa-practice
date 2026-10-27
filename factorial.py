def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Input needs to be a nonnegative integer.")
    else:
        return n * factorial(n - 1)
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Input cannot be a negative number.")
    elif n == 0: 
        return 1
    else:
        return n * factorial(n - 1)


assert factorial(5) == 120
assert factorial(3) == 6
assert factorial(1) == 1
assert factorial(-2) == 1
print("Factorial runs beautifully!")
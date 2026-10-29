def factorial(n):
    if n < 0:
        raise ValueError("Input cannot be a negative number.")
    elif n == 0: 
        return 1
    else:
        return n * factorial(n - 1)



print(factorial(5))
print(factorial(3))
print(factorial(0))
print(factorial(-1))

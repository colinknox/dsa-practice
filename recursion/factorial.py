def factorial(num):
    if num < 0:
        raise ValueError("Input cannot be a negative number. Must be 0 or above.")
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# assert factorial(5) == 120
# assert factorial(4) == 24
# assert factorial(2) == 2
# assert factorial(1) == 1
# assert factorial(0) == 1
print(factorial(0))
print("Factorial function tests successful.")
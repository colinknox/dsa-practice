def countup(n):
    if n <= 0:
        return
    countup(n - 1)
    print(n)



countup(5)
countup(3)
countup(0)
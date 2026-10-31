def countup(n: int) -> int | None:
    if n <= 0:
        return
    countup(n - 1)
    print(n)


countup(5)
countup(3)
countup(0)
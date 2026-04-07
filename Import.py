def sanash(n):
    if n == 0:
        return
    print(n)
    sanash(n - 1)

sanash(5)
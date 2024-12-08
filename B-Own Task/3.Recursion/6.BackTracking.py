def ascendingOrder(i):
    if i <= 0:
        return
    ascendingOrder(i - 1)
    print(i)

def descendingOrder(i):
    if i >= 3:
        return
    descendingOrder(i + 1)
    print(i)

descendingOrder(0)



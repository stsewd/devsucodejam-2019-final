def rabbits(n):
    if n < 0:
        return -1
    prev = 2
    current = 2
    for _ in range(n - 1):
        prev, current = current, prev + current
    return current//2

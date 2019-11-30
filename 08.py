def operations(n1, n2):
    steps = 0
    r = 0
    while True:
        if n1 + n2 == 0:
            break
        a = n1 % 10
        b = n2 % 10
        if a + b + r >= 10:
            steps += 1
            r = 1
        else:
            r = 0
        n1 = (n1 - a) // 10
        n2 = (n2 - b) // 10
    return steps

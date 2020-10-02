import math

def get_top(n):
    i = 1
    r = 0
    while i <= n:
        i += 2
        r += 1
    return r


def triangles(n):
    if not n:
        return -1
    if n <= 0:
        return -1
    if n == 1:
        return 1
    if n == 2:
        return 4
    up = False
    all_cols = [1, 3]
    for _ in range(3, n + 1):
        col_up = all_cols[0]
        col_down = all_cols[-1]
        for i in range(len(all_cols)):
            all_cols[i] += 2

        if up:
            all_cols.insert(0, get_top(col_up))
            all_cols[-1] += col_down - 1
            up = False
        else:
            all_cols.append(get_top(col_down))
            all_cols[0] += col_up - 1
            up = True
    return sum(all_cols)

n = int(input())
print(triangles(n))

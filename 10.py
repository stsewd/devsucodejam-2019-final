# FIXME: Check what number to add exactly when up is True or False

import math

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
        for i in range(len(all_cols)):
            if all_cols[i] % 2 == 1:
                all_cols[i] += 2
            else:
                all_cols[i] += 3
    if up:
        all_cols.insert(0, math.ceil(all_cols[0]/2))
        up = False
    else:
        all_cols.append(math.ceil(all_cols[-1]/2))
        up = True
    return sum(all_cols)

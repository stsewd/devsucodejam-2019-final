import itertools

def natural(n, m):
    if not (0 < m < 10):
        return -1
    allowed = '0' + str(m)
    i = 1
    while True:
        for posible in itertools.product(allowed, repeat=i):
            c = int(''.join(posible))
            if c > 0 and c % n == 0:
                return c
        i += 1

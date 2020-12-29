n = 5
start = 0

def xorOperation(n, start):

    k = 1
    s = start
    while k != n:
        start ^= s + 2*k
        k += 1
    return start


def xorOperation(n, start):
    import functools
    b = [start + 2*i for i in range(n)]
    return functools.reduce(lambda a, b: a ^ b, b)


print(xorOperation(n, start))

print(xorOperation(n, start))

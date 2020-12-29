n = 234

def subtractProductAndSum(n):
    import functools
    n = list(map(int, str(n)))
    return functools.reduce(lambda x, y: x * y, n)

print(subtractProductAndSum(n))
res_mul = 1
res_sum = 0
while n > 0:
    r = n % 10
    res_mul *= r
    res_sum += r
    n //= 10
return res_mul - res_sum
def subtractProductAndSum(n):


print(subtractProductAndSum(n))
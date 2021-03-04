#F(0) = 0, F(1) = 1
#F(n) = F(n - 1) + F(n - 2), for n > 1.


def fib(self, n: int) -> int:
    f1 = 0
    f2 = 1
    def fibo(n):
        if n ==0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibo(n-1) + fibo(n-2)
    return  fibo(n)



def fib(n: int) -> int:
    f1 = 0
    f2 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n - 2):
            f1, f2 = f2, f1 + f2
        return  f1 + f2

print(fib(4))



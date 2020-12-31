def maximum69Number (num: int) -> int:
    ans = num
    counter = 0
    last6 = 0
    while num != 0:
        counter += 1
        if num % 10 == 6:
            last6 = counter
        num //= 10
    if last6 != 0:
        return ans + 3 * (10 ** (last6 -1))
    return ans

print(maximum69Number(9999))
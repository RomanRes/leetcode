n = 5

def sumZero(n: int):
    ans = [i for i in range(1, int(n / 2) + 1)]
    ans2 = [-i for i in range(1, int(n / 2) + 1)]

    #if the number is odd
    if n%2 == 1:
        ans.append(0)
    ans.extend(ans2)
    return ans

print(sumZero(n))
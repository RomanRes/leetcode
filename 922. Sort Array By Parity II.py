A = [4,2,5,7]

def sortArrayByParityII(A):
    odd = [a for a in A if a % 2 == 1]
    even = [a for a in A if a % 2 == 0]
    ans = []
    while odd:
        ans.append(even.pop())
        ans.append(odd.pop())
    return ans

def sortArrayByParityII(A):
    ans = [None] * len(A)
    k = 0
    t = 1
    for i in A:
        if i % 2 == 0:
            ans[k] = i
            k += 2
        else:
            ans[t] = i
            t += 2
    return ans

print(sortArrayByParityII(A))
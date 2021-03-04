def diStringMatch(S):
    n = len(S)
    low = 1
    ans = []
    for i in S:
        if i == "I":
            ans.append(low)
            low += 1
        else:
            ans.append(n)
            n -= 1
    ans.append(0)
    return ans

S = "III"
print(diStringMatch(S))
def getMaximumGenerated(n):
    if n == 0:
        return 0
    result = [0, 1]
    for i in range(1, n // 2 + 1):
            result.append(result[i])
            result.append((result[i]) + result[i + 1])

    print(result)
    if len(result) == n + 1:
        return max(result)
    else:
        result.pop()

        return max(result)




        print(i)
    return result
print(getMaximumGenerated(3))
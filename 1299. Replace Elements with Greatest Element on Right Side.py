arr = [17,18,5,4,6,1]
def replaceElements(arr):
    m = arr[-1]
    result = [-1]
    for i in range(1, len(arr)):
        result.append(m)
        m = max(arr[~i], m)
    return result[::-1]

print(replaceElements(arr))
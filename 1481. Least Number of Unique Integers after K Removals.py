def findLeastNumOfUniqueInts(arr, k):
    d = dict()
    for number in arr:
        d[number] = d.get(number, 0) + 1
    values = sorted(d.values(), reverse=True)
    print(values)
    result = len(values)
    while k > 0:
        k -= values.pop()
        result -= 1
    if k == 0:
        return  result
    else:
        return result + 1

arr = [4,3,1,1,3,3,2]
k = 3
print(findLeastNumOfUniqueInts(arr, k))
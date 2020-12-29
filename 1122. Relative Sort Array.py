def relativeSortArray(arr1, arr2):

    d = dict()
    for i in arr1:
        d[i] = d.get(i, 0) + 1
    res = []

    for number in arr2:
        res.extend([number] * d[number])

    temp = list(set(arr1) - set(arr2))
    temp.sort()
    for number in temp:
        res.extend([number] * d[number])


    return res


arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]

arr2 = [2,42,38,0,43,21]
print(relativeSortArray(arr1, arr2))

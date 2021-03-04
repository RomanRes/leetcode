arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

def uniqueOccurrences(arr):
    d =  {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    if len(set(d.values())) == len(d.values()):
        return True
    return False


print(uniqueOccurrences(arr))
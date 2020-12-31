groupSizes = [3,3,3,3,3,1,3]
from collections import defaultdict
def groupThePeople(groupSizes):
    d = defaultdict(list)
    result = []
    for i, size in enumerate(groupSizes):
        d[size].append(i)
        if len(d[size]) == size:
            result.append(d[size])
            d[size] = []
    return result


print(groupThePeople(groupSizes))
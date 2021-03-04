from typing import List

arr = [4, 1, 2, 3]
def arrayRankTransform(arr: List[int]) -> List[int]:
    d = dict()
    for i, num in enumerate(sorted(list(set(arr))), 1):
        d[num] = i
    return [d[num] for num in arr]

print(arrayRankTransform(arr))

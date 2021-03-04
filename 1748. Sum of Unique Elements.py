from typing import List

def sumOfUnique(nums: List[int]) -> int:
    h = dict()
    for num in nums:
        h[num] = h.get(num, 0) + 1
    res = 0
    for key, val in h.items():
        if val == 1:
            res += key

    return res

assert sumOfUnique([1,1,1,1,1]) == 0, "0"
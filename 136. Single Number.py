from collections import defaultdict

nums = [4,1,2,1,2]
def singleNumber(nums):
    h = defaultdict(int)
    for num in nums:
        h[num] += 1

    return list(h.keys())[list(h.values()).index(1)]

print(singleNumber(nums))
nums = [4,1,2,1,2]

from functools import reduce
from operator import xor
def singleNumber(nums):
    return reduce(xor, nums)

print(singleNumber(nums))


nums = [4,1,2,1,2]


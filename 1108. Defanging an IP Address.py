nums = [1,2,3,1,1,3]
import itertools
import math
def numIdenticalPairs(nums):
    import itertools
    import math
    d = {}
    for number in nums:
        d[number] = d.get(number, 0) + 1
    result = 0
    for value in d.values():
        result += math.comb(value, 2)
    print(result)

numIdenticalPairs(nums)
nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    result = []
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [i, d[target - n]]
        else:
            d[n] = i
print(twoSum(nums, target))
def twoSum(nums, target):
    result = []
    for a in range(len(nums)):
        for b in range(len(nums)):
            if target - nums[a] == nums[b] and a != b:
                result.append(a)
                result.append(b)
                return result


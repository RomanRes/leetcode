nums = [6,2,6,5,1,2]

def arrayPairSum(nums) -> int:
    nums.sort()
    return sum(nums[::2])

print(arrayPairSum(nums))


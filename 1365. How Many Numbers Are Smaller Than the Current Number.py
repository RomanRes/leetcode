nums = [8,1,2,2,3]
def smallerNumbersThanCurrent(nums):
    temp = nums.copy()
    temp.sort()
    print(temp)
    return [temp.index(i) for i in nums]






print(smallerNumbersThanCurrent(nums))
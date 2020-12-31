nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 0
    for i in range(1, len(nums)):
        if nums[slow] != nums[i]:
            slow

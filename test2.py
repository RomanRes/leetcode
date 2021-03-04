def findKthLargest(nums, k):
        nums = sorted(nums)
        print(nums)
        return nums[-k]

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))
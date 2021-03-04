nums = [-4,-1,0,3,10]

def sortedSquares(nums):
    ans = []
    low = 0
    high = len(nums) - 1
    while low <= high:
        if nums[low] ** 2 <= nums[high] ** 2:
            ans.append(nums[low] ** 2)
            low += 1
        else:
            ans.append(nums[high] ** 2)
            high -= 1
    return ans[::-1]

print(sortedSquares(nums))

def sortedSquares(nums):
    ans = [n * n for n in nums]
    ans.sort()
    return ans
print(sortedSquares(nums))
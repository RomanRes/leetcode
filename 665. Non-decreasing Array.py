nums = [5, 7, 1, 8]
def checkPossibility(nums):
    counter = 0
    first = -1
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            counter += 1
            first = i
    if counter == 0:
        return True
    elif counter == 1 and first == 0:
        return True
    elif counter == 1 and nums[first - 1] <= nums[first + 1]:
        return True
    elif counter == 1 and first + 2 == len(nums):
        return True
    elif counter == 1 and nums[first] <= nums[first + 2]:
        return True
    return False

print(checkPossibility(nums))

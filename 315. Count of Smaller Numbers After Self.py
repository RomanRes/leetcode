nums = [5,2,6,1]

def countSmaller(nums):
    result = []
    for i in range(len(nums)):
        number = nums[i]
        counter = 0
        for j in range(i + 1, len(nums)):
            if nums[j] < number:
                counter += 1
        result.append(counter)
        counter = 0
    return result
print(countSmaller(nums))
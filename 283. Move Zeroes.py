
def moveZeroes(nums):
    zero = 0
    numbers = 0
    while zero != (len(nums) - 1) and numbers != len(nums):
        if nums[zero] != 0:
            zero += 1
        else:
            numbers = zero + 1
            while nums[numbers] == 0 and numbers != (len(nums) - 1):
                numbers += 1
            nums[zero], nums[numbers] = nums[numbers], nums[zero]
            zero += 1
    return nums

nums = [0, 1, 0, 0, 5, 6]
def moveZeroes(nums):
    zeroPoint = 0
    for secondPoint, num in enumerate(nums):
        print(secondPoint, num)
        if nums[zeroPoint] == 0:
            nums[zeroPoint], nums[secondPoint] = nums[secondPoint], nums[zeroPoint]
        if num != 0:
            zeroPoint += 1



    return nums

print(moveZeroes(nums))


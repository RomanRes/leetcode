nums = [3,4,5,2]

def maxProduct(nums):
    nums.sort()
    if (nums[0]-1)*(nums[1]-1) > (nums[-1]-1)*(nums[-2]-1):
        return (nums[i]-1)*(nums[j]-1)
    return (nums[-1]-1)*(nums[-2]-1)
print(maxProduct(nums))


#bruteforce
def maxProduct(nums):
    m = (nums[0]-1)*(nums[1]-1)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                m = max(m, (nums[i]-1)*(nums[j]-1))
    return m
print(maxProduct(nums))

#------------------
#best solution
def maxProduct(nums):
    m1 = max(nums)
    nums.remove(m1)
    return (m1-1)*(max(nums)-1)

print(maxProduct(nums))


def maxProduct(nums):
    max1, max2 = sorted(nums[:2])
    for i in range(2, len(nums)):
        max1 = max(max1, nums[i])
        max2 = max(max1, max2)
    return (max1 - 1) * (max2 - 1)


print(maxProduct(nums))
nums = [3,4,5,2]
a, b = sorted(nums[:2])
print(a, b)


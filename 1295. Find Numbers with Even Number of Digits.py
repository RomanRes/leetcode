nums = [12,345,2,6,7896]

def findNumbers(nums):
    counter = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            counter += 1
    return counter


def findNumbers(nums):
    ans = 0
    for num in nums:
        if num > 9:
            counter = 0
            while num != 0:
                num //= 10
                counter += 1
            if counter % 2 == 0:
                ans += 1

    return ans

print(findNumbers(nums))

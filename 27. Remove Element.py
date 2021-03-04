from typing import List


def removeElement(nums: List[int], val: int) -> int:
    for i in range(nums.count(val)):
        nums.remove(val)
    return nums


def removeElement(nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except:
                return len(nums)


print(removeElement([1, 2, 3, 3, 4], 3))


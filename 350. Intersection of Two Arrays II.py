nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

from typing import List
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    hMap = dict()
    hMap_2 = dict()
    for num in nums1:
        hMap[num] = hMap.get(num, 0) + 1
    for num in nums2:
        hMap_2[num] = hMap_2.get(num, 0) + 1
    result = []
    if len(hMap) < len(hMap_2):
        for item in hMap:
            temp = min(hMap.get(item, 0), hMap_2.get(item, 0))
            result.extend([item] * temp)
    else:
        for item in hMap_2:
            temp = min(hMap.get(item, 0), hMap_2.get(item, 0))
            result.extend([item] * temp)

    return  result


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    hMap = dict()
    for num in nums1:
        hMap[num] = hMap.get(num, 0) + 1
    result = []
    for num in nums2:
        if hMap.get(num):
            result.append(num)
            hMap[num] -= 1


    return  result


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    return [num for num in set(nums1) & set(nums2)
            for i in range(min(nums1.count(num), nums2.count(num)))]


    return  result

assert intersect(nums1, nums2) == [2, 2],  "must [2, 2]"
assert intersect([4,9,5], [9,4,9,8,4]) == [4, 9] or [9, 4],  "must [9, 4]"

from typing import List

# ez solution
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return set(nums1) & set(nums2)

# set solution
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return set.intersection(set(nums1), set(nums2))

print(intersection([2,3, 4], [4, 5, 6]))






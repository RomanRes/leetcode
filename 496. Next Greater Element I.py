nums1 = [2, 4]
nums2 = [1,2,3,4]

def nextGreaterElement(A, B):
    stack = []
    d = {}
    for i, num in enumerate(nums2):
        while stack and stack[-1]  < num:
            d[stack.pop()] = num
        stack.append(num)
    return [d[i] if i in d else -1 for i in nums1]








print(nextGreaterElement(nums1, nums2))
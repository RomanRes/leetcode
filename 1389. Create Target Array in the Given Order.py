nums = [0,1,2,3,4]
index = [0,1,2,2,1]

def createTargetArray(nums, index):
    res = []
    for i in range(len(index)):
        res.insert(index[i], nums[i])
    return res

createTargetArray(nums, index)
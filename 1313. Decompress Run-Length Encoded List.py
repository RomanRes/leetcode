nums = [1, 2, 3, 4]

def decompressRLElist(nums):
    result = []
    for first in range(0, len(nums), 2):
        freq = nums[first]
        val = nums[first + 1]
        result.extend([val] *  freq)
    print(result)
    return result
decompressRLElist(nums)
def decompressRLElist(nums):
    output_list = []
    for i in range(len(nums) // 2):
        output_list += ([nums[2 * i + 1]] * nums[2 * i])
    print(output_list)
    return output_list

def decompressRLElist(nums):
    result = []
    for first in range(0, len(nums), 2):
        for i in range(nums[first]):
            result.append(nums[first + 1])
    return result





decompressRLElist(nums)
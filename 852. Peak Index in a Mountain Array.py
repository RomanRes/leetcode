arr = [24,69,100,99,79,78,67,36,26,19]

def peakIndexInMountainArray(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i + 1]:
            return i

print(peakIndexInMountainArray(arr))


def peakIndexInMountainArray(arr):
    return arr.index(max(arr))

print(peakIndexInMountainArray(arr))
arr = [1,2]


def sumOddLengthSubarrays(arr):
    ans = 0
    for i in range(1, len(arr) + 1, 2):
        for j in range(0, len(arr) - i + 1):
            deb = arr[j:j+i]
            ans += sum(arr[j:j+i])
    return ans



print(sumOddLengthSubarrays(arr))


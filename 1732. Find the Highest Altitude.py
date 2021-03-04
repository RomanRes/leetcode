from typing import List

def largestAltitude(gain: List[int]) -> int:
    """
    Runtime: 24 ms, faster than 99.49% of Python3 online submissions for Find the Highest Altitude.
    Memory Usage: 14.2 MB, less than 45.47% of Python3 online submissions for Find the Highest Altitude.
    """
    m = 0
    last = 0
    for g in gain:
        last += g
        if m < last:
            m = last
    return m

assert largestAltitude([-5,1,5,0,-7]) == 1, "1"
assert largestAltitude([0,-4,-7,-9,-10,-6,-3,-1]) == 0, "0"





def minimumSwap(s1: str, s2: str):
    """
    Runtime: 28 ms, faster than 87.35% of Python3 online submissions for Minimum Swaps to Make Strings Equal.
    Memory Usage: 14.1 MB, less than 85.88% of Python3 online submissions for Minimum Swaps to Make Strings Equal.
    """
    countX = 0
    countY = 0
    for a, b in zip(s1, s2):
        if a != b:
            if a == "x":
                countX += 1
            else:
                countY += 1

    if (countX + countY) % 2 == 1:
        return -1
    return countX // 2 + countX % 2 + countY // 2 + countY % 2


assert minimumSwap("xy", "yx") == 2, "2"


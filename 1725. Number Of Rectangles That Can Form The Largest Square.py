from typing import List

def countGoodRectangles(rectangles: List[List[int]]) -> int:
    temp = sorted([min(a, b) for a, b in rectangles])
    return temp.count(temp[-1])

assert countGoodRectangles([[2,3],[3,7],[4,3],[3,7]]) == 3, "3"
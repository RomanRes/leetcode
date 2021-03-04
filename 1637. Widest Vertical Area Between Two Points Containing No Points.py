def maxWidthOfVerticalArea(points):
    points.sort(key=lambda p: p[0])
    result = 0
    for i in range(len(points) - 1):
        result = max(result, points[i+1][0] - points[i][0])

    return result

assert maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]) == 1, "shuld be 1"
assert maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]) == 3, "shuld be 3"


def maxWidthOfVerticalArea(points):
    """
    Runtime: 792 ms, faster than 97.98% of Python3 online submissions
    for Widest Vertical Area Between Two Points Containing No Points.

    Memory Usage: 55.4 MB, less than 18.79% of Python3 online submissions
    for Widest Vertical Area Between Two Points Containing No Points.
    """

    points = sorted([val[0] for val in points])
    points.sort()
    result = 0
    for i in range(len(points) - 1):
        if points[i+1] - points[i] > result:
            result = points[i+1] - points[i]

    return result

assert maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]) == 1, "shuld be 1"
assert maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]) == 3, "shuld be 3"
assert maxWidthOfVerticalArea([[1,5],[1,70],[3,1000],[55,700],[999876789,53],
                               [987853567,12]]) == 987853512, "shuld be 987853512"
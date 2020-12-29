points = [[3,2],[-2,2]]

def minTimeToVisitAllPoints(points):
    ans = 0
    for i in range(0, len(points) - 1):
        x, y = abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1])
        ans += max(x, y)

    return ans

print(minTimeToVisitAllPoints(points))

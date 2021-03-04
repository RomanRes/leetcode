grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]


def maxIncreaseKeepingSkyline(grid):
    top = []
    left = []
    for row in grid:
        left.append(max(row))


    for col in zip(*grid):
        top.append(max(col))
    #top.append(max([grid[row][col] for row in range(len(grid))]))

    ans = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            ans += min(top[col], left[row]) - grid[row][col]

    return ans

print(maxIncreaseKeepingSkyline(grid))



grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]





def islandPerimeter(grid):
    n = len(grid)
    m = len(grid[0])

    s = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1:
                if not n - 1 >= (row - 1) >= 0:
                    s += 1
                else:
                    if grid[row - 1][col] == 0:
                        s += 1
                if not n - 1 >= (row + 1) >= 0:
                    s += 1
                else:
                    if grid[row + 1][col] == 0:
                        s += 1
                if not m - 1 >= (col - 1) >= 0:
                    s += 1
                else:
                    if grid[row][col -1] == 0:
                        s += 1
                if not m - 1 >= (col + 1) >= 0:

                    s+= 1
                else:
                    if grid[row][col + 1] == 0:
                        s += 1
    return s

islandPerimeter(grid)


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

# looking from left to right
''''
def countNegatives(grid):
    counter = 0
    for row in grid:
        while row:
            if row.pop() < 0:
                counter += 1
            else:
                break
    return counter

print(countNegatives(grid))

'''
#Binary Search Solution
def countNegatives(grid):
    def bin_search(lst):
        low = 0
        high = len(lst) - 1
        while low <= high:
            middle = int(low + (high - low) / 2)
            if lst[middle] < 0:
                high = middle - 1
            else:
                low = middle + 1
        return len(lst[low:])

    counter = 0
    for row in grid:
        counter += bin_search(row)
    return counter

print(countNegatives(grid))
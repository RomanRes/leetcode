heights = [5,1,2,3,4]
def heightChecker(heights):
    s_heights = sorted(heights)
    counter = 0
    for i in range(len(heights)):
        if heights[i] != s_heights[i]:
            counter += 1
    return counter
print(heightChecker(heights))


def heightChecker(heights):
    s_heights = sorted(heights)
    counter = 0
    for i, j in zip(heights, s_heights):
        if i != j:
            counter +=1
    return counter
print(heightChecker(heights))
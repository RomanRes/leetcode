s = "1+(2*3)/(2-1)"

def maxDepth(s):
    max = 0
    counter = 0
    for i in s:
        if i == "(":
            counter += 1
        if i == ")":
            if counter > max:
                max = counter
            counter -= 1
    return max

print(maxDepth(s))
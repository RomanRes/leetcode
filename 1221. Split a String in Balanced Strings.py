s = "RLRRRLLRLL"
def balancedStringSplit(s):
    dif = 0
    counter = 0
    for i in s:
        if i == "R":
            dif += 1
        else:
            dif -= 1
        if dif == 0:
            counter += 1
    return counter




print(balancedStringSplit(s))
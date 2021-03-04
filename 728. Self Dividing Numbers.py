left = 1
right = 22

def selfDividingNumbers(left: int, right: int) :
    ans = []
    for number in range(left, right + 1):
        temp = list(str(number))
        if '0' in temp:
            continue
        for i in temp:
            if number % int(i) != 0:
                break
        else:
            ans.append(number)
    return ans

print(selfDividingNumbers(left, right))
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

def addTwoNumbers(l1, l2):
    if len(l1) < len(l2):
        l1[::-1], l2[::-1] = l2, l1
    result = []
    rest = 0
    for i in range(len(l1)):
        if i < len(l2) - 1:
            temp = l1.pop() + l2.pop() + rest
            result.append(temp % 10)
            rest = temp // 10
        else:
            temp = l1.pop() + rest
            result.append(temp % 10)
            rest = temp // 10
    return result
print(addTwoNumbers(l1, l2))


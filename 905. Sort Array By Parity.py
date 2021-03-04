a = [3,1,2,4]

def sortArrayByParity(A):
    first = [a for a in A if a % 2 == 0]
    second = [a for a in A if a % 2 == 1]
    first.extend(second)
    return first

print(sortArrayByParity(a))

def sortArrayByParity(A):
    first = []
    second = []
    for number in A:
        if number % 2 == 0:
            first.append(number)
        else:
            second.append(number)
    first.extend(second)
    return first

print(sortArrayByParity(a))

def sortArrayByParity(A):
    A.sort(key = lambda a: a % 2)
    return A

print(sortArrayByParity(a))
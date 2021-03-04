lst = [5,1,5,2,5,3,5,4]

def repeatedNTimes(A):
    for i in A:
        if A.count(i) == len(A) / 2:
            return i

print(repeatedNTimes(lst))


def repeatedNTimes(A):
    temp = set()
    for i in A:
        if i not in temp:
            temp.add(i)
        else:
            return i

print(repeatedNTimes(lst))
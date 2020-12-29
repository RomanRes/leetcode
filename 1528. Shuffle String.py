s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

def restoreString(s, indices):
    temp = list(zip(s, indices))
    temp.sort(key = lambda a: a[1])
    return ''.join([letter[0] for letter in temp])
    print(temp)


print(restoreString(s, indices))
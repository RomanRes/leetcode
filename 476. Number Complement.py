num = 5

def findComplement(num: int) -> int:
    res = []
    for i in bin(num)[2:]:
        if i == "0":
            res.append("1")
        else:
            res.append("0")
    return int(''.join(res), 2)

def findComplement(num: int) -> int:
    res = []
    for i in bin(num)[2:]:
        res.append(str(int(not int(i))))
    return int(''.join(res), 2)

def findComplement(num: int) -> int:
    return num ^ int("1"*len(bin(num)[2:]), 2)

print(findComplement(num))

#return num^
#
# int(

# (
# len(str(
# bin(num)
#
# )) - 2)*"1",
# 2)
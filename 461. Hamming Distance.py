a = 1
b = 4

def hammingDistance(x: int, y: int) -> int:
    return str(bin(x ^ y)).count("1")

print(hammingDistance(a, b))

def hammingDistance(x: int, y: int) -> int:
    return str(bin(x ^ y))[2:].count("1")

print(hammingDistance(a, b))

print(2 >> 1)
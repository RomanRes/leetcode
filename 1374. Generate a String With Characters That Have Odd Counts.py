def generateTheString(n: int) -> str:
    if n % 2 == 1:
        return "a"*(n)
    return "a"*(n - 1) +  "b"

print(generateTheString(3))
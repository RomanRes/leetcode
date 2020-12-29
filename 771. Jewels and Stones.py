import time
jewels = "aA"
stones = "aAAbbbb"

start = time.time()
for _ in range(2000):
    def numJewelsInStones(jewels, stones):
        result = 0
        for stone in jewels:
            result += stones.count(stone)
        return result

print(numJewelsInStones(jewels, stones))
end = time.time()

elapsed = end - start
print(elapsed, "1")
result = 0
#way faster


def numJewelsInStones(jewels, stones):
    j_Dict = {}
    for stone in stones:
        j_Dict[stone] = j_Dict.get(stone, 0) + 1
    result = 0
    for jewel in jewels:
        result += j_Dict[jewel]
    return result

print(numJewelsInStones(jewels, stones))


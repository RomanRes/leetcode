import time
import collections

start = time.time()
target = [1,2,3,4]
arr = [2,4,1,3]
for _ in range(200000):
    def canBeEqual(target, arr):
        if sorted(target) == sorted(arr):
            return True
        return False

canBeEqual(target, arr)
end = time.time()

elapsed = end - start
print(elapsed, "1")


start = time.time()
for _ in range(200000):
    def canBeEqual(target, arr):
        if collections.Counter(target) == collections.Counter(arr):
            return True
        return False
canBeEqual(target, arr)
end = time.time()

elapsed = end - start
print(elapsed)

start = time.time()
for _ in range(200000):
    def canBeEqual(target, arr):
        temp = [x for x in target + arr if x not in target or x not in arr]
        if not temp:
            return True
        return False


print(canBeEqual(target, arr))

end = time.time()

elapsed = end - start
print(elapsed)
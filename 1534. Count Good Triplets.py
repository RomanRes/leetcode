arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

def countGoodTriplets( arr, a, b, c):
    d = {num: arr.index(num) for num in arr}
    print(d)
    import itertools
    temp = itertools.permutations(arr, 3)
    ans = [tup for tup in temp if d[tup[0]] <= d[tup[1]] <= d[tup[2]] and abs(tup[0] - tup[1]) <= a
        and abs(tup[0] - tup[2]) <= c and abs(tup[1] - tup[2]) <= b]
    print(ans)


countGoodTriplets(arr, a, b, c)
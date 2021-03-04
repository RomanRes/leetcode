encoded = [6,2,7,3]
first = 4
def decode(encoded, first):
    ans = [first]
    for i in encoded:
        ans.append(ans[-1] ^ i)
    return ans

print(decode(encoded, first))


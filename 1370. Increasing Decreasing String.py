s = "aaaabbbbccc"

def sortString(s):
    # make hashmap
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1

    #
    keys = sorted(d.keys())
    r_keys = keys[::-1]
    print(keys, r_keys)
    couter = len(s)
    result = []
    while couter > 0:
        for key in keys:
            if d.get(key) > 0:
                result.append(key)
                d[key] -= 1
                couter -= 1
        for key in r_keys:
            if d.get(key) > 0:
                result.append(key)
                d[key] -= 1
                couter -= 1
    return ''.join(result)


print(sortString(s))


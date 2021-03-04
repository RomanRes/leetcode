a = ["9001 discuss.leetcode.com"]


for i in range(len(a)):
    print(a[i:])

def subdomainVisits(cpdomains):
    hashMap = {}
    for i in cpdomains:
        val, dom = i.split(" ")
        val = int(val)
        dom = dom.split(".")
        for i in range(len(dom)):
            temp = ".".join(dom[i:])
            hashMap[temp] = hashMap.get(temp, 0) + val
        res = []
    return [f"{item[1]} {item[0]}" for item in hashMap.items()]


print(subdomainVisits(a))

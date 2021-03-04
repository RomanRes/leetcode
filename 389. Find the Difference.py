s = "abcd"
t = "abcde"

# hashmap solution
def findTheDifference(s: str, t: str) -> str:
    d = {}
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    for letter in t:
        d[letter] = d.get(letter, 0) - 1
    for key in d:
        if d[key] == -1:
            return key

#python solution

print(findTheDifference(s, t))

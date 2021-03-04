def minSteps(s: str, t: str) -> int:
    h1 = dict()
    h2 = dict()
    for letter in s:
        h1[letter] = h1.get(letter, 0) + 1
    for letter in t:
        h2[letter] = h2.get(letter, 0) + 1
    counter = 0
    for letter in h1:
        temp = h1[letter] - h2.get(letter, 0)
        if temp > 0:
            counter += h1[letter] - h2.get(letter, 0)
    return counter



minSteps("aba", "bab")

# python version

"leetcode"
"practice"

def minSteps(s: str, t: str) -> int:
    return sum([s.count(letter) - t.count(letter) for letter in set(s)
                if (s.count(letter) - t.count(letter)) > 0])



print(minSteps("leetcode", "practice"))

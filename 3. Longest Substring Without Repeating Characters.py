s = "dvdf"
def lengthOfLongestSubstring(s):
    temp = set()
    ans = 0
    for letter in s:
        if letter in temp:
            ans = max(ans, len(temp))
            temp = set(letter)
        else:
            temp.add(letter)
    return max(ans, len(temp))

print(lengthOfLongestSubstring(s))
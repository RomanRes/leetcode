s = ["h","e"]

print(len(s) // 2)

for i in range(len(s)):
    if i >= (len(s) // 2):
        break
    s[i], s[~i] = s[~i], s[i]

print(s)
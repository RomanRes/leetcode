s = "MerryChristmas"

def halvesAreAlike(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    h = int(len(s) / 2)
    counter = 0
    for i in s[:h]:
        if i in vowels:
            counter += 1
    for i in s[h:]:
        if i in vowels:
            counter -= 1
    if counter == 0:
        return True
    return False

print(halvesAreAlike(s))
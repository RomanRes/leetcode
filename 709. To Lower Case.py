# lower solution

def toLowerCase(str: str) -> str:
        return str.lower()

print(toLowerCase("AAA"))


def toLowerCase(str: str) -> str:
    temp = []
    for letter in str:
        t_lett = ord(letter)
        if 64 < t_lett < 91:
            temp.append(chr(t_lett + 32))
        else:
            temp.append(letter)


    return ''.join(temp)

print(toLowerCase("AABBCC"))

#ASKii
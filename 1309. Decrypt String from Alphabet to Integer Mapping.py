'''
to slow....

'''

def freqAlphabets(s: str) -> str:
    jzCharacters = {'10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm',
                    '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q',
                    '18#': 'r', '19#': 's', '20#': 't', '21#': 'u',
                    '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y',
                    '26#': 'z'}
    aiCharacters = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
                    '6': 'f', '7': 'g', '8': 'h', '9': 'i'}

    for char in jzCharacters:
        s = s.replace(char, jzCharacters[char])
    for char in aiCharacters:
        s = s.replace(char, aiCharacters[char])
    return s

def freqAlphabets(s: str) -> str:
    jzCharacters = {str(num - 96) + '#': chr(num) for num in range(106, 123)}
    aiCharacters = {str(num - 96): chr(num) for num in range(97, 106)}
    k = 0
    ans = []
    while k < len(s):
        if s[k:k+3].isdigit():
            ans.append(aiCharacters[s[k]])
            k +=1
        else:
            ans.append(jzCharacters[s[k:k+3]])
            k += 3
    return ''.join(ans)


s = "10#11#12"
print(freqAlphabets(s))



jzCharacters = {str(num - 96) + '#': chr(num) for num in range(106, 123)}
aiCharacters = {str(num - 96): chr(num) for num in range(97, 106)}
print(aiCharacters)
print(ord('j'))

print(ord('z'))
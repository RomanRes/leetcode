words = ["gin", "zen", "gig", "msg"]

def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
             ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--","-..-","-.--","--.."]
    result = set()
    for word in set(words):
        temp = []
        for letter in word:
            temp.append(morse[ord(letter) - 97])
        result.add(''.join(temp))
    print(result)

def uniqueMorseRepresentations(words):
    morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    result = set()
    for word in set(words):
        temp = []
        for letter in word:
            temp.append(morse[letter])
        result.add(''.join(temp))
    return result

def uniqueMorseRepresentations(words):
    morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
             'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
             'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
             'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
             'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
    ans = {"".join(morse[letter] for letter in word) for word in words}
    return len(ans)



uniqueMorseRepresentations(words)
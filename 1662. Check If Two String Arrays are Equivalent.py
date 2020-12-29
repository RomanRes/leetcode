word1 = ["ab", "c"]
word2 = ["a", "bc"]
def arrayStringsAreEqual(word1, word2):
    first = ''.join(word1)
    second = ''.join(word2)
    if first == second:
        return True
    return False
print(arrayStringsAreEqual(word1, word2))

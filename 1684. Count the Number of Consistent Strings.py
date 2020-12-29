allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]


def countConsistentStrings(allowed, words):
    allowed =set(allowed)
    counter = 0
    for word in words:
        if set(word) <= allowed:
            counter += 1
    return counter

countConsistentStrings(allowed, words)



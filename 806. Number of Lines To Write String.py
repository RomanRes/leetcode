widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"


def numberOfLines(widths, s):
    counter = 0
    row = 0
    for val in s:
        row += widths[ord(val) - 97]
        if row > 100:
            row = widths[ord(val) - 97]
            counter += 1
    return [counter + 1, row]


print(numberOfLines(widths, s))



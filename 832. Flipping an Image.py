a = [[1, 1, 1, 0]]

def flipAndInvertImage( A):
    for row in A:
        for i in range(int((len(row) + 1) / 2)):
            row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
    return A

print(flipAndInvertImage(a))
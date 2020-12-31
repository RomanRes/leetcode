n = 2
m = 3
indices = [[0,1],[1,1]]

def oddCells(n, m, indices):
    row = [0] * n
    col = [0] * m
    for i,j  in indices:
        row[i] += 1
        col[j] += 1

    ans = 0
    for i in row:
        for j in col:
            temp = i + j
            if temp % 2 == 1:
                ans += 1

    return ans

print(oddCells(n, m, indices))



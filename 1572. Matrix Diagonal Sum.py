mat = [[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]

def diagonalSum(mat):
    leng = len(mat)
    ans = 0
    for row in range(leng):
        print(row)
        ans += mat[row][row] + mat[row][-row - 1]
        print(mat[row][row], mat[row][-row - 1])
    if leng % 2 == 1:
        ans -= mat[int(leng/2)][int(leng/2)]
    return ans

def diagonalSum(mat):
    import numpy
    a = numpy.array(mat)
    ans = a.diagonal().sum() + numpy.fliplr(a).diagonal().sum()
    leng = len(mat)
    if leng % 2 == 1:
        ans -= mat[int(leng/2)][int(leng/2)]
    return ans

print(diagonalSum(mat))
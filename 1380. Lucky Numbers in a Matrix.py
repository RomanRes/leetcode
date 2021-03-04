matrix = [[3,7,8],[9,11,13],[15,16,17]]



def luckyNumbers(matrix):
    row = [min(r) for r in matrix]
    col = []
    for c in range(len(matrix[0])):
        temp = []
        for r in range(len(matrix)):
            temp.append(matrix[r][c])
        col.append(max(temp))
    return [num for num in row if num in col]

def luckyNumbers(matrix):

    return list({min(r) for r in matrix} & {max(c) for c in zip(*matrix)})


print(luckyNumbers(matrix))
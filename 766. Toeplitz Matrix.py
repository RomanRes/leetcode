matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]


def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    diagonal = dict()
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if r - c not in diagonal:
                diagonal[r - c] = val
            elif diagonal[r - c] != val:
                return False
    return True
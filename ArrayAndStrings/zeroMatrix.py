# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0

# 1. Better space
# O(n*m) & O(m+n)

def zeroMatrix_better(mat):
    rows = len(mat)  # n
    cols = len(mat[0])  # m

    rowsToTransform = set()
    colsToTransform = set()

    # Find all zero positions and record its row and col
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                rowsToTransform.add(i)
                colsToTransform.add(j)

    # Iterate over rows and cols that need to be set to 0
    for i in rowsToTransform:
        for j in range(cols):
            mat[i][j] = 0

    for j in colsToTransform:
        for i in range(rows):
            mat[i][j] = 0

    return mat

# 2. No extra space
# O(n*m) & O(1)
# Note: Idea -> Use the first row and first column as flags for whether the corresponding column or corresponding row has a 0


def zeroMatrix_best(mat):
    firstRowHasZero = False
    firstColHasZero = False

    # Record whether the first row or column has a real 0
    for num in mat[0]:
        if num == 0:
            firstRowHasZero = True
    for arr in mat:
        if arr[0] == 0:
            firstColHasZero = True

    # Iterate over rest of matrix.
    # Set 0 to the first row/column if a column/row has a 0
    for i in range(1, len(mat[0])):
        for j in range(1, len(mat)):
            if mat[i][j] == 0:
                mat[0][j] = 0  # Set first row
                mat[i][0] = 0  # Set first column

    # Iterate over first row and first column and set 0's to rest of matrix
    for j in range(1, len(mat[0])):
        if mat[0][j] == 0:
            for i in range(len(mat)):
                mat[i][j] = 0
    for i in range(1, len(mat)):
        if mat[i][0] == 0:
            for j in range(len(mat[0])):
                mat[i][j] = 0

    # Check if the first column and first row has real 0's
    if firstRowHasZero:
        for j in range(len(mat[0])):
            mat[0][j] = 0
    if firstColHasZero:
        for i in range(len(mat)):
            mat[i][0] = 0

    return mat


matrix = [[1, 2, 3, 0], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 16]]
print(zeroMatrix_best(matrix))

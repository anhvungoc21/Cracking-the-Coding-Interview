# Given an image represented by an N by N matrix, where each pixel in the image is represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place?

# 1. Out-of-place -- Create new matrix.
# Same as in-place but using extra space
# O(n^2) & O(n^2)
# Write rows to columns

def rotateMatrix_naive(mat):
    n = len(mat)
    newMat = [[None for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            # 90 degrees clockwise
            newMat[col][n-1-row] = mat[row][col]

            # Cool: Transposition would be:
            # newMat[col][row] = mat[row][col]
    return newMat

# 2. In-place with no extra memory
# O(n^2) & O(1)
# Note: Idea -> Swap by LAYERS. Outermost -> Innermost layers of matrix.
# * A layer consists of 4 arrays (top, right, bottom, left). We save one layer (top), and do swaps in the reverse order of the rotation.

def rotateMatrix_inPlace(mat):
    n = len(mat)
    # If odd, the innermost layer is always 1-element. No rotation needed.
    layers = n // 2

    for layer in range(layers):
        # Define boundaries of layers as we move outside in
        first = layer
        last = n - 1 - layer

        # Iterate over each position pos for all 4 layers simultaneously
        # Note: Only do until the second-to-last position for each layer. The last position is the first position of the next layer.
        for pos in range(first, last):
            # Save top
            top = mat[first][pos]

            # Left -> Top:
            mat[first][pos] = mat[last-pos][first]

            # Bottom -> Left:
            mat[last-pos][first] = mat[last][last-pos]

            # Right -> Bottom:
            mat[last][last-pos] = mat[pos][last]

            # Top -> Right:
            mat[pos][last] = top

    return mat


testMat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(rotateMatrix_inPlace(testMat))

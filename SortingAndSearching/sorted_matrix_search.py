# Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.

# 20 35 80 95
# 30 55 95 105
# 40 80 100 120

# ? Approach 1: 2D binary search by cleverly enforcing direction
def solution(mat, target):
    row, col = 0, len(mat[0]) - 1

    while row < len(mat) and col >= 0:
        if mat[row][col] == target:
            return (row, col)
        
        # Move to left (smaller) col if target is smaller
        elif mat[row][col] > target:
            col -= 1
        # Move to down (larger) row if target is larger 
        else:
            row += 1

    return (-1, -1)

# ? Approach 2: Partition and Search
# This uses the diagonal to divide the search space into 4 quadrants, 2 of which need to be searched
def solution(mat, target):
    pass





# ======================================== #

# ! Read the prompt wrong.
# This is a solution when the elements are laid out in ascending order throughout each row and each column.
# Observations:
# - Can find row which is smaller than the element but the next row is larger with BS
# - Once a row is found, BS in that row.

def solution(mat, target):
    # Invalid
    if mat[0][0] > target: return (-1, -1)

    row = 0
    while mat[row][0] <= target:
        row += 1

    # Return if first element is target
    if mat[row - 1][0] == target:
        return (row, 0)
    
    # Here, row is after the target
    col = binary_search(mat[row - 1], target)
    return (row, col) if col != -1 else (-1, -1)

def binary_search(row, target):
    low, high = 0, len(row)

    while low <= high:
        mid = low + ((high - low) // 2)

        if row[mid] == target:
            return mid
        elif row[mid] < target:
            low = mid + 1
        else:
            high =  mid - 1

    return -1

mat = [[1, 3, 5, 7], [9, 10, 14, 16], [20, 28, 30, 35]]
print(solution(mat, 9))
# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.

from copy import deepcopy

def solution():
    results = []
    eight_queens(0, [0] * 8, results)
    return results

def eight_queens(row, columns, results):
    # Placed all 8 queens!
    if row == 8: results.append(columns.copy())

    # Explore all possible ways of placing a queen on this row
    for col in range(8):
        if can_place(row, col, columns):
            # Place queen
            columns[row] = col

            # Recurse
            eight_queens(row + 1, columns, results)

def can_place(row1, col1, columns):
    # Note: Optimizations
    # - Don't have to check row because we're placing 1 queen on 1 row
    # - Don't have to check later rows because we haven't placed them
    # - Clever diagonal checking

    for row2 in range(row1):
        col2 = columns[row2]

        # Check if this column is blocked
        if col2 == col1: return False

        # Check if diagonals are blocked
        if abs(col1 - col2) == abs(row1 - row2): return False
    
    return True
        

boards = solution()
for board in boards:
    for row in board:
        row_str = ["O"] * 8
        row_str[row] = "X"
        print(" ".join(row_str))
    print("\n")
print(len(boards))
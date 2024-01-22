# Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.

# DP
# Time: O(r * c)
# Space: O(r * c)
def solution(grid):
    r = len(grid)
    c = len(grid[0])
    # Encoding: Right = 1, Down = 2

    # Fill in base cases
    # First row can only be accessed by going right
    for i in range(c):
        if grid[0][i] == -1: break
        grid[0][i] = 1

    # First column can only be visited by going down
    for i in range(r):
        if grid[i][0] == -1: break
        grid[i][0] = 2

    # Build
    for j in range(1, c):
        for i in range(1, r):
            # Invalid
            if grid[i][j] == -1: continue

            # Access from either way if previous is accessible
            if i > 0 and grid[i][j - 1] > 0: # From left
                grid[i][j] = 1
            if j > 0 and grid[i - 1][j] > 0 : # From top
                grid[i][j] = 2

    # Verify that destination is reached
    r, c = r - 1, c - 1
    if grid[r][c] == 0: return ["NO PATH"]

    # Trace back path
    path = []
    while r > 0 or c > 0:
        # Get step
        went_right = (grid[r][c] == 1)
        path.append("right" if went_right else "down")
    
        # Update
        if went_right:
            c -= 1
        else:
            r -= 1

    return path[::-1]
        

# Test
rows = 4
cols = 6
grid = [[0 for _ in range(cols)] for _ in range(rows)]
grid[0][1] = -1
grid[rows - 2][cols - 1] = -1
grid[rows - 2][cols - 2] = -1
grid[rows - 2][cols - 3] = -1
grid[rows - 2][cols - 4] = -1
# grid[rows - 2][cols - 5] = -1
grid[rows - 2][cols - 6] = -1

[print(row) for row in grid]
print(solution(grid))
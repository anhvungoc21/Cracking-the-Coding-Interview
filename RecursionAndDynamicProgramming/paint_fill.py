# Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, fill the surrounding area until the color changes from the original color.

from collections import deque
def solution(screen, r, c, fill):
    rows, cols = len(screen), len(screen[0])

    queue = deque([(r, c)])
    color = screen[r][c]

    # Directions: top, right, bottom, left
    dirs_row = [-1, 0, 1, 0]
    dirs_col = [0, 1, 0, -1]

    while queue:
        r, c = queue.popleft()

        # Fill
        screen[r][c] = fill

        # Recurse
        for i in range(4):
            nr, nc = r + dirs_row[i], c + dirs_col[i]
            if valid(nr, nc, rows, cols) and  screen[nr][nc] == color:
                queue.append((nr, nc))

    return screen

def valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


screen = [[1, 0, 1], [0, 0, 0], [1, 0, 0], [0, 0, 1]]
for row in screen: print(row)
print()
for row in solution(screen, 1, 1, 2): print(row)
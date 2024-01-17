# A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, not byte will be split across rows). The height of the screen, of course, can be derived from the length of the array and the width. Implement a function that draws a horizontal line from (x1, y) to (x2, y).


# ? Brute force
# Find row y
# Set all bits from x1 to x2

# ? Clever
# Only starting and ending byte are not full of "1"'s
# The bytes in between can be set to "111111"s (0xFF)

def solution(screen, width, x1, x2, y):
    for i in range(x1, x2 + 1):
            #  ----- Row ------   -- Byte --   --- Position in byte ---
        screen[(width // 8) * y + (i // 8)] |= (1 << (8 - (i % 8) - 1))

    return screen


# Verify
width = 3
height = 5
screen = [0] * (width * height)

i = 0
for byte in solution(screen, width * 8, 0, 6, 0):
    print(bin(byte)[2:].zfill(8), end = "")
    if i == width - 1:
        print()
    i = (i + 1) if i < width - 1 else 0

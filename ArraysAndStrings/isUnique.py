# Determine if a string has all unique characters. What if you cannot use additional data structures?

# 1. Hashing
# O(n) & O(n)
def isUnique_hash(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        else:
            visited.add(char)

    return True

# 2. Sorting
# O(n log n) & O(1)


def isUnique_sort(s):
    s_sorted = sorted(s)
    lastSeen = ''
    for char in s_sorted:
        if char == lastSeen:
            return False
        lastSeen = char

    return True


# 3. Tuple mimicking Bit Vector
# Only works if know the number of possible characters
# O(n) & O(1)
NUM_CHARS = 26


def isUnique_tuple(s):
    visited = (0 for _ in range(26))
    for char in s:
        pos = ord(char) % NUM_CHARS
        if visited[pos] == 1:
            return False
        else:
            visited[pos] = 1

    return True


# 4. Bit Vector
# Only works if know the number of possible characters
# O(n) & O(1)
# Note: Python 3 apparently uses a variable number of bits to represent integers. 
# The actual number of bits used depends on the magnitude of the integer being represented. Python automatically adjusts the number of bits used to accommodate larger or smaller numbers as needed. This is known as arbitrary-precision arithmetic.
NUM_CHARS = 128 # ASCII
def isUnique_bit(s):
    visited = 0
    for char in s:
        pos = ord(char) % NUM_CHARS
        if (visited >> pos) & 1:
            return False
        else:
            visited |= 1 << pos

    return True


print(isUnique_bit("abcdefghijklmnopqrstuvwxyz123456789"))
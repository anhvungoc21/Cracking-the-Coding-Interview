# You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fit between bit 3 and bit 2

# Example:
# N = 10000000000
# M = 10011
# i = 2
# j = 6
# => Output: N = 10001001100


def solution(M, N, i, j):
    # Clear bits j to i in N
    # 1. Create mask of j - i 1's
    mask = ~(~0 << (j - i + 1))
    # 2. Shift mask to correct position
    mask = mask << i
    # 3. Flip mask to clear bits
    mask = ~mask
    # 4. Clear bits in N
    N &= mask

    # Shift N to correct position
    M = M << i

    # Set M bits in N
    N |= M
    return bin(N)

N = int("10000000000", 2)
M = int("10011", 2)

print(solution(M, N, 2, 6))
# Given a string, check if it is a permutation of a palindrome.

# 1. Hashing
# Idea: If palindrome, there must be no more than 1 character who has an odd number of occurences
# O(n) & O(n) <If limit characters, O(1) space>

def isPalindromePermutation_hash(s: str):
    visited = set()
    for char in s.lower():
        if not char.isalpha():
            continue
        if char in visited:
            visited.remove(char)
        else:
            visited.add(char)

    return len(visited) <= 1


# print(isPalindromePermutation_hash("Tact Coa"))


# 2. Bit Vector
# Idea: Same as hashing, but flip bits accordingly. If final results > 1, not a palindrome.
# O(n) & O(1)
NUM_CHARS = 26  # Letters only - Specified in prompt


def isPalindromePermutation_bit(s: str):
    visited = 0
    for char in s.lower():
        if not char.isalpha():
            continue

        pos = ord(char) % NUM_CHARS

        # Toggle bit at pos
        visited ^= 1 << pos

    # Check if all bits are 0 except one bit or fewer
    # NOTE: Idea -> If less than 1 bit is 1, must be a power of 2 or 0. There's a nice trick to test this:
    # Explanation: Subtracting 1 from a power of 2 results in flipping all the bits (e.g. 1000 -> 0111)
    return (visited & (visited - 1)) == 0


print(isPalindromePermutation_bit("Tact Ca"))

# Write a recursive function to multiply two positive integers without using the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

# Observations:
# - Multiply a by b: a + ... + a (b times) => Brute easy
# a added b times
# -> b/2 times
# -> b/4 times

# Improvement: O(smaller) instead of O(b) time

def solution(a, b):
    return recursive_multiply(max(a, b), min(a, b))

def recursive_multiply(num, times):
    if times == 0: return 0
    if times == 1: return num

    # b is even -> half * 2
    # b is odd -> half * 2 + a
    half = solution(num, times // 2)
    result = half + half + (0 if (times % 2 == 0) else num)
    return result

print(solution(12, 4))

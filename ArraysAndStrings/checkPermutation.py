# Given two strings, write a method to decide if one is a permutation of the other.

# 1. Hashing
# O(n) & O(k)
# `n` is the number of characters in the longer string
# `k` is the number of unique characters in both strings. If working with limited alphabet, this may arguably be O(1)
from collections import Counter
def checkPermutation_hash(s1, s2):
    s1_dict = Counter(s1)
    for char in s2:
        if char not in s1_dict:
            return False
        s1_dict.subtract(char)

    return s1_dict.total() == 0


# 2. Sorting
# O(n log n) & O(1)
def checkPermutation_sort(s1, s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    for i, char in enumerate(s1_sorted):
        if char != s2_sorted[i]:
            return False
    return True

print(checkPermutation_sort("awwsd", "wadsw"))
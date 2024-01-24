# You are given an array-like data structure Listy which lacks a size method. It does, however, have an elementAt(i) method that returns the element at the index i in O(1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data structure only supports positive integers.) Given a Listy which contains sorted, positve integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.

# Observations
# We likely want to identify the length of the array through binary search. Like the "Search in Rotated Array" problem, we can perform multiple binary searches for different purposes.
#
# Search 1: Find length of array by searching a numeric array
# Say we have lengths 1, 2, 4, 8, 16, ...
# => The actual length must be in between 2 values -> The first elementAt(i) == 1 gets us that bound
# => Perform binary search using elementAt to get end of array
#
# Search 2: Find element -> Normal binary search

# ? 1. Solution 1: Good, but naive and unnecessarily long
def solution(arr, target):
    # Empty array
    if arr.elementAt(0) == -1: 
        return -1

    # Singleton array
    if arr.elementAt(1) == -1: 
        return 0 if arr.elementAt(0) == target else -1

    # Find length (last index) of array
    low = high = 1
    while arr.elementAt(high) == -1:
        low = high
        high = high * 2
    last_index = find_last_index(arr, low, high)

    # Find element
    low, high = 0, last_index
    while low <= high:
        mid = low + ((high - low) // 2)
        
        if arr.elementAt(mid) == target:
            return mid
        elif arr.elementAt(mid) > target:
            low = mid - 1
        else:
            high = mid + 1

    return -1

def find_last_index(arr, low, high):
    while low <= high:
        mid = low + ((high - low) // 2)

        # Found last index
        if (arr.elementAt(mid) != -1) and (arr.elementAt(mid) == -1):
            return mid
        
        elif arr.elementAt(mid) == -1:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# ? Solution 2: Same idea, more concise
# We don't have to necessarily find the exact length.
# If we know the bounds, we can modify our binary search guards to search the correct half

def solution(arr, target):
    index = 1

    # First check: Find larger bound of length
    # Second check: Index is larger than index of actual target, yet smaller than actual length
    while (arr.elementAt(index) != -1) and (arr.elementAt(index) < target):
        index *= 2

    # Here we know that the element must be between index/2 and index
    return binary_search(arr, target, index // 2, index)

def binary_search(arr, target, low, high):
    while low <= high:
        mid = low + ((high - low) // 2)
        
        if arr[mid] == target:
            return mid

        # Also search lower when mid exceeds array length
        elif arr.elementAt(mid) == -1 or arr.elementAt(mid) > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1
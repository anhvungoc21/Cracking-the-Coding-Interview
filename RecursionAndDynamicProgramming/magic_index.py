# A magic index in an array A[0 ... n -1] is defined to be an index such that A[i] = i. Given a sorted array of distict integers, write a method to find a magic index, if one exists, in array A.

# Observation:
# Each index, the number can only grow by 1 to match
# => We can get rid of half of the array if we find an invalid index
#   + Too big: Search smaller half
#   + Too small: Search bigger half

# Recursion and Iterative have the same structure
def solution(arr):
    return magic_index(arr, 0, len(arr) - 1)

def magic_index(arr, low, high):
    if low > high: return -1

    mid = low + ((high - low) // 2)
    if arr[mid] == mid: 
        return mid
    elif arr[mid] > mid:
        return magic_index(arr, low, mid - 1)
    else:
        return magic_index(arr, mid + 1, high)

arr = [-3, 0, 2, 5, 7, 8, 10]  
print(solution(arr))

# * Follow-up: What if the values are not distinct?
# This invalidates our first observation
# We can no longer discard one half. We need to search both halves, but we can cut some of the search space
# e.g. arr[5] = 3 -> We only need to search arr[0]->arr[3]

def solution(arr):
    return magic_index(arr, 0, len(arr) - 1)

def magic_index(arr, start, end):
    if start > end: return -1

    mid = start + (end - start) // 2

    # Found
    if arr[mid] == mid: return mid

    # Search left
    left = min(mid - 1, arr[mid])
    left_index = magic_index(arr, start, left)
    if left_index >= 0: return left

    # Search right
    right = max(mid + 1, arr[mid])
    right_index = magic_index(arr, right, end)
    return right

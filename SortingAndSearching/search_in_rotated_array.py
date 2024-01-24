# Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.

# ! This doesn't work when there are repeated elements
# Observations
# 1 2 3 4 5 6 7 8 9
# 7 8 9 1 2 3 4 5 6
# => Two portions basically
#
# If we can find the split point through binary search, 
# we can perform binary search on the half that we know the element will be in. 
#   + Larger half: arr[0] -> split
#   + Smaller half: split -> arr[len]
# => Normal binary search with a different starting point
# 
# To find split point, we find the element i that is smaller than the i-1
# - To decide which half to recurse on, we can compare to the first element
#   + If larger: search upper half
#   + If smaller: search smaller half
# => Slight variation of normal binary search

# Return index of smallest element of array, aka the split
def find_split(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        
        # Array is in sorted order
        if mid == 0: return 0

        # Found split
        if arr[mid] < arr[mid - 1]: 
            return mid
        elif arr[mid] > arr[0]:
            low = mid + 1
        else:
            high = mid - 1

    return -1
    

def solution(arr, target):
    split = find_split(arr)
    if split == -1: return "Error"

    # Determine which half to search
    low, high = -1, -1
    if target > arr[0]:
        low, high = 0, split
    else:
        low, high = split, len(arr) -1

    # Normal binary search
    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == target: 
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1 # Not found

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(solution(arr, 5))
arr = [70, 75, 17, 18, 30, 31, 35, 50, 60]
print(solution(arr, 18))
arr = [24, 25, 26, 27, 30, 31, 13, 18, 23]
print(solution(arr, 18))
arr = [30, 30, 30, 30, 24, 25, 26, 27]
print(solution(arr, 26))
arr = [40, 41, 42, 43, 30, 30, 30, 30]
print(solution(arr, 42))


# ==================================================

# This solution is more general and works with any rotation direction of the array
def solution(arr, target):
    return binary_search(arr, 0, len(arr) - 1, target)

def binary_search(arr, left, right, target):
    # Invalid
    if left > right: return -1

    # Found
    mid = left + ((right - left) // 2)
    if arr[mid] == target: return mid

    # Left half is normally ordered
    if arr[left] < arr[mid]:
        
        # ? Left half is normally ordered. So if it is in this range, we recurse with "normal" binary search on it
        # ? Otherwise, we recurse on right half since this function takes care of the "un-normal" half too.
        # Target is within left range. Search left
        if arr[left] <= target < arr[mid]:
            return binary_search(arr, left, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, right, target)
    
    # Right half is normally ordered
    elif arr[mid] < arr[right]:

        # Target is within right range. Search right
        if arr[mid] <= target < arr[right]:
            return binary_search(arr, mid + 1, right, target)
        else:
            return binary_search(arr, left, mid - 1, target)
    
    # Ambiguous. Search both halves
    else:
        result = -1

        # Left half are duplicates. Search right
        if arr[left] == arr[mid]:
            location = binary_search(arr, mid + 1, right, target)
        
        # Right half are duplicates. Search left
        if result == -1 and arr[mid] == arr[right]:
            location = binary_search(arr, left, mid - 1, target)

        return location

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10 ,14]
print(solution(arr, 5)) 
# In an array of integers, a "peak" is an element which is greater than or equal to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers. For example, in the array [5, 8, 6, 2, 3, 4, 6], {8, 6} are peaks and {5, 2} are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

# ? Ideas:
# - If we maintain peaks, we are also maintaining valleys
# - We deal with 3-element windows. Examining all possible permutations tell us that we can always swap the middle element with the largest of the three to CREATE a peak.
#   => We are concerned with messing up previous peaks. We won't because creating a peak means swapping an even smaller element outside. This maintains the valley.

def solution(arr):
    # Start at first peak (2nd element)
    for i in range(1, len(arr), 2):
        max_idx = get_max_index(arr, i - 1, i, i + 1)
        if i != max_idx:
            swap(arr, i, max_idx)

    return arr

def swap(arr, origin, dest):
    temp = arr[origin]
    arr[origin] = arr[dest]
    arr[dest] = temp

def get_max_index(arr, a, b, c):
    a_val = arr[a] if valid(a, len(arr)) else -float("inf")
    b_val = arr[b] if valid(b, len(arr)) else -float("inf")
    c_val = arr[c] if valid(c, len(arr)) else -float("inf")

    largest = max(a_val, b_val, c_val)
    if largest == a_val: return a
    elif largest == b_val: return b
    else: return c

def valid(idx, n):
    return 0 <= idx < n

print(solution([15, 0, 1, 14, 8, 9, 11, 7, 4]))
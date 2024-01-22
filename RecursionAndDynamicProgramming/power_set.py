# Write a method to return all subsets of a set

# Observations:
# - Subset: 0 -> n elements

# Approach: Base case and Build
# n = 0 => {}
# n = 1 => {}, {a1}
# n = 2 => {}, {a1}, {a2}, {a1, a2}
# n = 3 => {}, {a1}, {a2}, {a1, a2},
#          {a3}, {a1, a3}, {a2, a3}, {a1, a2, a3}
# * => P(n) is just P(n - 1) duplicated, and then with the new element added to it

def solution(arr):
    return subsets(arr, len(arr))

def subsets(arr, count):
    # Base case
    if count == 0: return [[]]
    
    # Recurse
    all_subsets = subsets(arr, count - 1)
    result = all_subsets.copy()

    # Add elements to previous call
    for subset in all_subsets:
        new_subset = subset.copy()
        new_subset.append(arr[count - 1])
        result.append(new_subset)

    return result

print(solution([1, 2, 3]))
    
# Given two sorted arrays, find the number of elements in common. The arrays are the same length and each has all distinct elements

# Note: If given unsorted, use a hash table to optimize for time, or sort to optimize for space.

def findCommonElements(arr1, arr2):
    p1 = 0
    p2 = 0

    common = set()
    while p2 < len(arr2):
        # Skip all smaller elements
        while p1 < len(arr1) and arr1[p1] < arr2[p2]:
            p1 += 1
        if not p1 < len(arr1): break

        # Check if landed on equality
        if arr1[p1] == arr2[p2]:
            common.add(arr1[p1])

        # Always increment p2 (the goal post)
        p2 += 1

    return len(common)


print(findCommonElements([13, 27, 35, 40, 49, 55, 59],
                         [17, 35, 39, 40, 55, 58, 60]))

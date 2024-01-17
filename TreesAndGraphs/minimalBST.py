# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a inary search tree with minimal height

# * Idea -> Perform binary search to find the middle element. Then, divide and conquer to create left and right sub-trees!

from _Tree import Node

def solution(arr):
    # start and end are both valid indicies
    return minimal_tree(arr, 0, len(arr) - 1)


def minimal_tree(arr, start, end):
    # Invalid
    if start > end:
        return None

    # ? Which index to take when 2-element window
    mid = start + ((end - start) // 2)

    # Recurse
    left = minimal_tree(arr, start, mid - 1)
    right = minimal_tree(arr, mid + 1, end)

    # Assemble tree
    root = Node(mid)
    if left:
        root.left = left
    if right:
        root.right = right

    return root



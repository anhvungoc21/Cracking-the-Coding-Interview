# Implement a function to check if a binary tree is a binary search tree

# * Idea -> Depending on the branch, we worry about a constraint being violated:
#         * Left branch: A node is a larger than the current allowable max (root)
#         * Right branch: A node is smaller than the current allowable min (root)
#         ? => Keep track of the most extreme min, max constraints for each node

import math

def solution(root):
    return is_valid(root, math.inf, -math.inf)

def is_valid(root, cur_min, cur_max):
    # Check root validity
    if not root: return True
    if root.data < cur_min or root.data > cur_max: return False

    # Recurse
    left_valid = is_valid(root.left, cur_min, root.data)
    right_valid = is_valid(root.right, root.data, cur_max)

    return right_valid and left_valid

# ? Note: We don't need to wait for left and right sub-tree results!
def is_valid(root):
    stack = [(root, math.inf, -math.inf)]

    while stack:
        node, cur_min, cur_max = stack.pop()

        # Check for node invalidty
        if node.data < cur_min or node.data > cur_max: return False

        # Visit its children first
        stack.append((node, cur_min, cur_max))
        if node.left: stack.append((node.left, cur_min, node.data))
        if node.right: stack.append((node.right, node.data, cur_max))

    return True

# ? Morris traversal to avoid memory costs (gets rid of both stack and recursion)

# Write an algorithm to find the "next" node (i.e. in-order successor) of a given node in a BST. You may assume that each node has a link to its parent.

# * Idea -> When we find our node, there are 2 scenarios:
# * - There is a right child: The next node is the first node of the left branch
# * - There is no right child: We have to return to the root whom this branch is a left sub-tree. 

# Successor is always larger
# Has right: -> Return left-most node of right branch.
# No right: Either
#   1. Moves back up (D, F) to the first parent bigger than itself
#   2. Or, end of tree (no parent found)

def solution(given):
    # Found right node. Return its left-most
    if given.right:
        to_ret = given.right
        while to_ret.left:
            to_ret = to_ret.left
        return to_ret

    # No right node. Return to first parent who is larger 
    #   (given is on left branch of that parent)
    root = given.parent
    while root and root.data < given.data:
        root = root.parent
    return root

    # # Alternative: Search upwards for parent whose left path contains target
    # while root.parent and root != root.parent.left:
    #     root = root.parent
    # return root.parent # is None if bubbled up to actual root
    

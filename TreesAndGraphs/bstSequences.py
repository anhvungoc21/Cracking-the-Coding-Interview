# A binary search tree was created by traversing through an array from left to right and inserting each element. 
# Given a BST with distinct elements, print all possible arrays that could have led to this tree

# Observations:
# Root is always fixed
# Other than that, we can insert nodes 


# For each tree, its root must always come first
# => Prepend the root to all possible weavings of 2 sub-trees recursively
# Note: We weave because we need to preserve the relative order of each sub-array

def solution(root):
    # Base case
    if not root: return [[]]

    # Recurse
    left_weaves = solution(root.left)
    right_weaves = solution(root.right)
    
    # Weave and prepend
    weaves = []
    for left in left_weaves:
        for right in right_weaves:
            weaves.extend(make_weaves(left, right, [root.data]))

    return weaves

def make_weaves(first, second, prefix):
    # Base cases: One list is empty. Append the rest
    if not first: return [prefix.copy() + second.copy()]
    if not second: return [prefix.copy() + first.copy()]

    # 2 options
    first_weaves = make_weaves(first[1:], second.copy(), prefix.copy() + [first[0]])
    second_weaves = make_weaves(first.copy(), second[1:], prefix.copy() + [second[0]])

    return first_weaves + second_weaves

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

root = Node(50,
            Node(20, 
                 Node(10,
                      Node(5, None, None),
                      Node(15, None, None)),
                Node(25, None, None)),
            Node(60,
                 None,
                 Node(70,
                      Node(65, None, None),
                      Node(80, None, None))))

print(len(solution(root)))

root = Node(2, Node(1, None, None), Node(3, None, None))
print(solution(root))
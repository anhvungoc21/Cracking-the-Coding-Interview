# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth

# * Idea -> Level-order traversal

def solution(tree):
    level = [tree.root]
    lists = []

    while level:
        # Create list
        lists.append(create_linked_list(level))

        # Next level
        next_level = []
        for node in level:
            next_level.append(node.left)
            next_level.append(node.right)
        level = next_level

    return lists

def create_linked_list(arr):
    next_node = None
    for data in arr[::-1]:
        cur_node = Node(data)
        cur_node.next = next_node
        next_node = cur_node

    return next_node
        
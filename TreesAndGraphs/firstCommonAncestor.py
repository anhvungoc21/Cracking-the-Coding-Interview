# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.

# Version 1: With pointers to parents
# Approach 1: Counting depth. O(d)
def solution(p, q):
    count_p = count_q = 0

    # Traverse all the way to top to get height
    temp_p = p
    temp_q = q
    while temp_p.parent:
        temp_p = temp_p.parent
        count_p += 1
    while temp_q.parent:
        temp_q = temp_q.parent
        count_q += 1

    # Traverse difference
    _, high = (p, q) if count_p < count_q else (q, p)
    for _ in range(abs(count_p - count_q)):
        high = high.parent
    
    # Get potential common ancestor
    while p != q:
        p = p.parent
        q = q.parent

    return p

# Version 1: With links to parents
# Approach 2: Check each sibling sub-tree. O(t) -> O(n)
def solution(p, q):
    # Checks if node is covered by (is a descendant of) root
    def covers(root, node):
        if not root: return False
        if root == node: return True
        return covers(root.left, node) or covers(root.right, node)
    
    # One node covers another
    if covers(p, q): return p
    if covers(q, p): return q

    # On two different sides
    # Missing null checks here but who cares :D
    parent = p.parent
    sibling = parent.left if p == parent.right else parent.right
    while not covers(sibling, q):
        parent = parent.parent
        sibling = parent.left if p == parent.right else parent.right
    return parent

# Version 2: Without links to parents
# ? Optimized recursive solution which visits each node once
# Brute force would be to naively check every sub-tree for p and q
def solution(root, p, q):
    ancestor, found_ancestor = find_ancestor(root, p, q)
    return ancestor if found_ancestor else None

def find_ancestor(root, p, q):
    # Invalid node. Found nothing
    if not root: return None, False

    # Found both p and q here!
    if root == p and root == q: return p, True

    # Recurse. Bubble up result if found on sub-tree
    right_root, right_found = find_ancestor(root.right, p, q)
    if right_found: return right_root, True
    left_root, left_found = find_ancestor(root.left, p, q)
    if left_found: return left_root, True

    # ? Found something on both sub-trees. Must be p and q. Current root is the ancestor!
    if right_root and left_root:
        return root, True
    # ? Current root is p or q. If sub-tree also has sth, then it must be the other one. Current root is ancestor!
    elif root == p or root == q:
        return root, right_root or left_root
    # Bubble up any potentially non-null root. Haven't found ancestor yet.
    else:
        return right_root if right_root else left_root, False
    

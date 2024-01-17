# T1 and T2 are two very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1

# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. 
# That is, if you cut off the tree at node n, the two trees would be identical

# Takes care of t2 empty
def solution(t1, t2):
    # Empty tree to find
    if not t2: return True
    return is_sub_tree(t1, t2)

# Husk. Finds same root. 
# Then, call kernel to verify entire tree.
def is_sub_tree(t1, t2):
    # End of t1
    if not t1: 
        return True
    # Found same root. Verify whole tree
    elif t1.data == t2.data:
        return match_tree(t1, t2)
    # Didn't find. Continue searching for same root
    else:
        return (is_sub_tree(t1.left, t2) or
               is_sub_tree(t1.right, t2))

# Recusively matches an entire tree
def match_tree(t1, t2):
    # Both empty
    if not t1 and not t2: 
        return True
    # One is empty, other isn't
    elif not t1 or not t2:
        return False
    # Non-matching root
    elif t1.data != t2.data:
        return False
    # Root matches. Recurse
    else:
        return (match_tree(t1.left, t2.left) and
                match_tree(t1.right, t2.right))
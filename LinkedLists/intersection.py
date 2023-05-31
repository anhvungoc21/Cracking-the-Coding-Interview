# Given two singly linked lists, determine if two lists intersect. Return the intersecting node. Note that intersection is defined based on reference, not value.

from _Class import LinkedList, Node

def intersection(l1: LinkedList, l2: LinkedList) -> Node:
    if not l1.head or not l2.head: return None

    # Calculate length of both lists
    cur1 = l1.head
    cur2 = l2.head
    len1 = len2 = 0 # Is actually real_length - 1 since we're not moving till null
    while cur1.next:
        len1 += 1
        cur1 = cur1.next
    while cur2.next:
        len2 += 1
        cur2 = cur2.next

    # If ending nodes are not the same, they do not intersect
    if cur1 != cur2:
        return None

    # Increment the longer list by the difference. If same length, ignore.
    cur1 = l1.head
    cur2 = l2.head
    diff = len1 - len2
    if diff < 0:
        for _ in range(diff):
            cur2 = cur2.next
    elif diff > 0:
        for _ in range(diff):
            cur1 = cur1.next

    # Move both pointers simultaneously and find intersecting node
    while cur1 != cur2: # Here, they MUST have an intersection
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1



l1 = LinkedList(None)
l2 = LinkedList(None)

# --- No intersection ---
l1.fromList([1, 2, 3, 4, 6])
l2.fromList([6, 7, 8])
print(intersection(l1, l2))

l1.fromList([])
l2.fromList([])
print(intersection(l1, l2))


# --- Has intersection ---
na = Node('a')
nb = Node('b')
nc = Node('c')
nx = Node('x')
ny = Node('y')
nI_1 = Node(1)
nI_2 = Node(2)
nIntersect = Node("I")

# 1. Different length
# a -> b -> c -> |
#                I -> 1 -> 2
#      x -> y -> |
na.next = nb
nb.next = nc
nc.next = nIntersect
nx.next = ny
ny.next = nIntersect
nIntersect.next = nI_1
nI_1.next = nI_2

l1 = LinkedList(na)
l2 = LinkedList(nx)
print(intersection(l1, l2)) # found!

# 2. Same length
# a -> b -> |
#           I -> 1 -> 2
# x -> y -> |
na.next = nb
nb.next = nIntersect
nx.next = ny
ny.next = nIntersect
nIntersect.next = nI_1
nI_1.next = nI_2

l1 = LinkedList(na)
l2 = LinkedList(nx)
print(intersection(l1, l2)) # found!

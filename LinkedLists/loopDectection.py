# Given a linked list which might contain a loop. Implement an algorithm that returns the node at the beginning of the loop (if one exists)

from _Class import LinkedList, Node

#? Floyd's Turtoise and Hare algorithm:
def loopDetection(ll: LinkedList) -> Node:
    if not ll.head: return None

    slow = fast = ll.head
    while fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    # Hit null. Must not have a loop
    return False

# -- No loop --
ll = LinkedList(None)
ll.fromList(['a', 'b', 'c', 'd', 'e'])
print(loopDetection(ll))

# -- Has loop -- 
# Loop from another node
na = Node('a')
nb = Node('b')
nc = Node('c')
nd = Node('d')
ne = Node('e')
na.next = nb
nb.next = nc
nc.next = nd
nd.next = ne
ne.next = nc
ll = LinkedList(na)
print(loopDetection(ll))

# Loop from self
na.next = nb
nb.next = nc
nc.next = nc
ll = LinkedList(na)
print(loopDetection(ll))
# Given a linked list which might contain a loop. Implement an algorithm that returns the node at the beginning of the loop (if one exists)

from _Class import LinkedList, Node

#? Floyd's Turtoise and Hare algorithm:
# * Proof that putting a node at the beginning once `fast` meets `slow`, then increment them both again, can help detect start of cycle:
# Define: 
# x: number of nodes before cycle
# y: number of nodes `slow` travels in the cycle before meeting `fast`
# z: number of nodes in the cycle - y
# We know:
# dist_slow = x + y
# dist_fast = x + y + z + y
# dist_fast = 2 * dist_slow
# => Easily show that x = z
def loopDetection(ll: LinkedList) -> Node:
    if not ll.head: return None

    slow = fast = ll.head
    while fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Loop detected. Find cycle's start by putting another pointer at the beginning of linked list.
            slow = ll.head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    # Hit null. Must not have a loop
    return None

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
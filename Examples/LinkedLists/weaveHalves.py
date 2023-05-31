# Given a linked list a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn. Rearrange the linked list into a1 -> b1 -> a2 -> b2 -> ... -> an -> bn.
# If number of nodes is odd, ignore odd node at the end

from _Class import LinkedList, Node


def weaveHalves(ll: LinkedList):
    slow = ll.head
    fast = ll.head
    numNodes = 0

    # Move fast to end of linked list so that slow is in the middle
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        numNodes += 1

    # Count number of nodes. If fast has reached None, then even. Else, odd
    # Counting nodes is unnecessary if number of nodes is even. 
    numNodes *= 2
    if fast:
        numNodes += 1

    # Base case: Singleton
    if numNodes == 1:
        return

    # Weave
    p2 = slow
    p1 = ll.head
    nextP2 = None

    # Stop when p2 hits the final element
    while p2.next:
        # Special case: Ignore last node when odd
        if numNodes % 2 == 1 and not p2.next.next:
            p1.next = p2
            return

        # Insert p2 next to p1
        nextP2 = p2.next
        p2.next = p1.next
        p1.next = p2

        # Increment
        p2 = nextP2
        p1 = p1.next.next

    p1.next = p2
    return


ll = LinkedList(Node(0))
ll.fromList([1, 2, 3, 4, 5])
weaveHalves(ll)
print(ll)
ll.fromList([1, 2, 3, 4, 5, 6])
weaveHalves(ll)
print(ll)

# [1, 2, 3] => [1, 2, 3] is correct.

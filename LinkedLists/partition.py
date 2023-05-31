# Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. Nodes with value x does not necessarily need to appear in between the "small" and "large" partition.

from _Class import LinkedList, Node

# 1. Actually partition with two heads
# O(n) & O(1)
def partition(ll: LinkedList, pivot: int):
    if not ll.head or not ll.head.next: return

    headSmall = small = Node('small')
    headLarge = large = Node('large')
    cur = ll.head
    
    while cur:
        nextNode = cur.next
        if cur.data < pivot:
            small.next = cur
            small = small.next
        else:
            large.next = cur
            large = large.next
        cur = nextNode

    small.next = headLarge.next
    ll.head = headSmall.next
    return


#? 2. Partition smaller nodes -- GREAT
# O(n) & O(1)
# Idea: Only remove a node if it is smaller and move it to a separate head

def partition(ll: LinkedList, pivot: int):
    if not ll.head or not ll.head.next: return

    dummy = cur = Node('dummy')
    dummySmall = small = Node('small')
    cur.next = ll.head

    while cur.next:
        if cur.next.data < pivot:
            # Append node to small LinkedList
            small.next = cur.next
            small = small.next
            
            # Remove node from current LinkedList
            cur.next = cur.next.next
        cur = cur.next

    small.next = dummy.next
    ll.head = dummySmall.next
    return

#? 3. Two pointers & No extra nodes -- GREAT
# ! Does NOT preserve the order in which nodes appear
# O(n) & O(1)
# Two pointers start at the same node.
# + For any smaller node, point that node to the small pointer.
# + For any larger node, point the larger pointer TO that node.
def partition(ll: LinkedList, pivot: int):
    if not ll.head or not ll.head.next: return
    
    cur = small = large = ll.head
    while cur:
        nextNode = cur.next
        if cur.data < pivot:
            cur.next = small # * Left of small is always open
            small = cur
        else:
            large.next = cur # * Right of large is always open
            large = cur

        cur = nextNode

    # Unlink large & Set head to small
    large.next = None
    ll.head = small
    return

ll = LinkedList(None)
ll.fromList([1, 4, 2, 5, 3, 2, 6, 8])
partition(ll, 5)
print(ll)
# Same as sumBackwardsList but numbers are encoded in linked lists in their natural order instead of reversed
# O(2n) & O(n) <recursive>
# Steps:
# - Calculate length with 1 traversal
# - Traverse longer list until both pointers at the same position. Keep a `prev` pointer that points to the last position before this same position.
# - Recurse on both lists simultaneously. During stack-popping, calculate sum and return carryOver. Update both lists.
# - Formulate answer:
#   + If same length: Append a node at the beginning if still has carry over. Return an arbitrary list.
#   + If different length: Add carryOver to `prev` if necessary. Return the longer list.

from _Class import LinkedList, Node

def sumForwardLists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    p1 = l1.head
    p2 = l2.head
    if not p1 or not p2: return None

    # Calculate length
    len1 = len2 = 0
    while p1:
        len1 += 1
        p1 = p1.next
    while p2:
        len2 += 1
        p2 = p2.next

    # Traverse longer list till same position
    p1 = l1.head
    p2 = l2.head
    prev = None # Keeps the node immediately before where p1 and p2 recurse to add potential carryover
    if len1 > len2:
        for _ in range(len1 - len2):
            prev = p1
            p1 = p1.next
    elif len2 > len1:
        for _ in range(len2 - len1):
            prev = p2
            p2 = p2.next

    # Recurse on both lists simultaneously
    def rec(n1, n2):
        # End of both lists. No carry over
        if not n1:
            return 0
        
        # Recurse 
        carryOver = rec(n1.next, n2.next)
        
        # -- Post-order behavior --
        # Calculate sum
        mySum = n1.data + n2.data + carryOver
        carryOver = 1 if mySum >= 10 else 0
        
        # Assign digit
        digit = mySum % 10
        n1.data = digit
        n2.data = digit

        return carryOver
    
    carryOver = rec(p1, p2)
    
    # If same length and has carry over, append new node at start
    if len1 == len2:
        if carryOver != 0:
          newHead = Node(carryOver)
          newHead.next = l1.head
          l1.head = newHead
        return l1
    
    # Different length
    prev.data += carryOver
    if len1 > len2:
        return l1
    else:
        return l2


l1 = LinkedList(None)
l2 = LinkedList(None)

#! MISSED THIS: All 9s. Carry over at all steps => Need to pad the shorter list with 0s and then recurse through both lists simultaneously.
l1.fromList([9, 9, 9, 9, 9, 9, 9]) # 9999999
l2.fromList([9, 9, 9, 9]) # 9999
print(sumForwardLists(l1, l2)) # 89990001 - correct!

# Testing carry over to all meaningful positions
l1.fromList([1, 2, 8, 3]) # 1283
l2.fromList([9, 5, 4]) # 954
print(sumForwardLists(l1, l2)) # 2237 - correct!

# Same length, with carry over at last position
l1.fromList([2, 8, 3]) # 283
l2.fromList([9, 5, 4]) # 954
print(sumForwardLists(l1, l2)) # 1237 - correct!

# Same length, no carry over at last position
l1.fromList([1, 2, 3]) # 123
l2.fromList([4, 5, 7]) # 457
print(sumForwardLists(l1, l2)) # 580  - correct!

# Both singleton, with carry over
l1.fromList([5]) # 5
l2.fromList([5]) # 5
print(sumForwardLists(l1, l2)) # 10  - correct!

# Both singleton, no carry over
l1.fromList([5]) # 5
l2.fromList([4]) # 4
print(sumForwardLists(l1, l2)) # 9 - correct!

# Both empty. 
l1.fromList([]) # None
l2.fromList([]) # None
print(sumForwardLists(l1, l2)) # None  - correct!

# One empty. This is a ill-formed input.
# => Could have an initial check to return None
l1.fromList([5]) # 5
l2.fromList([]) # None
print(sumForwardLists(l1, l2)) # None - correct!
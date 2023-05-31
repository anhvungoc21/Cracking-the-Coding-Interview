# Two numbers are represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, that is the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

from _Class import LinkedList, Node

def sumBackwardsLists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    p1 = l1.head
    p2 = l2.head
    if not p1 or not p2: return None

    prev = None
    carryOver = 0
    while p1 and p2:
        # Compute sum and reset carry-over
        mySum = p1.data + p2.data + carryOver
        carryOver = 0

        # Check sum
        if mySum >= 10:
            carryOver = 1
            mySum = mySum % 10

        # Store result in both lists
        p1.data = mySum
        p2.data = mySum
        prev = p1 # Keep the last node of a list in case both lists run out and need to add carry over
        p1 = p1.next
        p2 = p2.next

    # Equal lengths. Check if need to add carry-over node
    if not p1 and not p2: 
        if carryOver:
            prev.next = Node(carryOver)
        return l1

    # Add carry-over if needed and return the remaining list.
    # The rest of the list needs no adjustments!
    if not p1:
        p2.data += carryOver
        return l2
    else:
        p1.data += carryOver
        return l1

l1 = LinkedList(None)
l2 = LinkedList(None)

# Testing carry over to all meaningful positions
l1.fromList([3, 8, 2 ,1]) # 1283
l2.fromList([4, 5, 9]) # 954
print(sumBackwardsLists(l1, l2)) # 2237 - correct!

# Same length, with carry over at last position
l1.fromList([3, 8, 2]) # 283
l2.fromList([4, 5, 9]) # 954
print(sumBackwardsLists(l1, l2)) # 1237 - correct!

# Same length, no carry over at last position
l1.fromList([3, 2, 1]) # 123
l2.fromList([7, 5, 4]) # 457
print(sumBackwardsLists(l1, l2)) # 580  - correct!

# Both singleton, with carry over
l1.fromList([5]) # 5
l2.fromList([5]) # 5
print(sumBackwardsLists(l1, l2)) # 10  - correct!

# Both singleton, no carry over
l1.fromList([5]) # 5
l2.fromList([4]) # 4
print(sumBackwardsLists(l1, l2)) # 9 - correct!

# Both empty. 
l1.fromList([]) # None
l2.fromList([]) # None
print(sumBackwardsLists(l1, l2)) # None  - correct!

# One empty. This is a ill-formed input.
# => Could have an initial check to return None
l1.fromList([5]) # 5
l2.fromList([]) # None
print(sumBackwardsLists(l1, l2)) # None - correct!
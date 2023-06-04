# Two numbers are represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, that is the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

from _Class import LinkedList, Node
def total(v1: int, v2: int, carryOver):
    total = v1 + v2 + carryOver
    digit = total % 10
    carryOver = total // 10
    return digit, carryOver

def sumBackwardsLists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    cur1 = l1.head
    cur2 = l2.head
    if not cur1 or not cur2: return None

    prev = None
    carryOver = 0

    # Iterate over same length
    while cur1 and cur2:
        digit, carryOver = total(cur1.data, cur2.data, carryOver)

        # Set both linkedlists in case we return either
        cur1.data = digit
        cur2.data = digit
        
        prev = cur1
        cur1 = cur1.next
        cur2 = cur2.next

    # When cur1 == cur2 == None, return l1 since prev is set to cur1
    toRet = l2 if cur2 else l1

    # Add the rest
    cur = cur2 if cur2 else cur1
    while cur:
        digit, carryOver = total(cur.data, 0, carryOver)
        cur.data = digit
        prev = cur
        cur = cur.next

    # Check if still has carryOver. Create extra node for 1
    if carryOver != 0:
        prev.next = Node(carryOver)

    return toRet

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

#! MISSED THIS: All 9s. Carry over at all steps
l1.fromList([9, 9, 9, 9, 9, 9, 9]) # 9999999
l2.fromList([9, 9, 9, 9]) # 9999
print(sumBackwardsLists(l1, l2)) # 89990001 - correct!

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
from _Class import LinkedList, Node
# Implement an algorithm to find the kth to last element of a singly linked list

# 1. 2 passes, no extra space
# O(2n) & O(1)
# Count length and traverse (length - k) again
def returnKthToLast(ll: LinkedList, k: int):
    length = 0
    cur = ll.head

    # Count length
    while cur:
        length += 1
        cur = cur.next

    # Traverse
    if k > length:
        return None  # Invalid k

    cur = ll.head
    for _ in range(length - k):
        cur = cur.next

    return cur.data

# 2. 1 pass, extra space for last seen numbers
# O(n) & O(n)
def returnKthToLast(ll: LinkedList, k: int):
    values = []

    # Traverse
    cur = ll.head
    while cur:
        values.append(cur.data)
        cur = cur.next

    # Find value in array
    if k > len(values):
        return None
    return values[-k]

# 3. 1 pass, Create doubly linked list
# O(n) & O(1)
def returnKthToLast(ll: LinkedList, k: int):
    if not ll.head:
        return None

    prev = dummy = Node('dummy')
    dummy.next = ll.head
    cur = ll.head

    # Traverse and create previous pointers
    while cur:
        cur.prev = prev
        prev = cur
        cur = cur.next

    # Undo any invalid mutations
    ll.head.prev = None
    dummy.next = None

    # Now prev is at last node. Go back
    for _ in range(k - 1):
        prev = prev.prev

        if not prev:
            return None

    return prev.data

# ? 4. Two pointers k distance away -- BEST APPROACH!!!
# O(n) & O(1)
def returnKthToLast(ll: LinkedList, k: int):
    if not ll.head:
        return None

    left = right = ll.head
    # Traverse second pointer
    for _ in range(k - 1):
        if not right.next:
            return None
        right = right.next

    # Move both pointers simultaneously
    while right.next:
        left = left.next
        right = right.next

    return left.data

# ? 5. Recursion -- INTERESTING!!!
# O(n) & O(n)
class Solution:
  def __init__(self):
      self.i = 0

  def returnKthToLast(self, ll: LinkedList, k: int):
      def rec(node: Node):
          # Base case: End of linked list
          if not node:
              return None

          # Recurse until end without doing anything.
          # Note: Only take action when popping off the stack!
          data = rec(node.next)

          # Note: The lines after the recursive call is when the calls are popped off the stack
          self.i += 1 # Increment i
          # Found position k. Return node's data
          if self.i == k:
              return node.data
          
          # Return whatever was returned by the last call popped from the stack
          return data
      
      self.i = 0
      return rec(ll.head)

s = Solution()
ll = LinkedList(None)
ll.fromList([1, 2, 3, 4, 5])
print(s.returnKthToLast(ll, 2))
print(s.returnKthToLast(ll, 6))
ll.fromList([1])
print(s.returnKthToLast(ll, 1))
print(s.returnKthToLast(ll, 2))
ll.fromList([])
print(s.returnKthToLast(ll, 1))

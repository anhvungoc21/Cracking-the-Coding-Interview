class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def __str__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(str(cur.data))
            cur = cur.next
        return " -> ".join(nodes)

    # Utilities
    def fromList(self, arr):
        self.head = Node("dummy") # Remove all nodes
        cur = self.head
        for data in arr:
            cur.next = Node(data)
            cur = cur.next

        self.head = self.head.next
        return

    def appendToTail(self, newData):
        cur = self.head
        while cur.next:
          cur = cur.next
        cur.next = Node(newData)
        return
  
# Tests
# ll = LinkedList(Node(0))
# ll.fromList([1, 2, 3, 4, 5])
# print(ll)
# print(ll.head)
# ll.fromList([])
# print(ll)
# print(ll.head)
  
      
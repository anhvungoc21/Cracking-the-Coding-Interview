# Given only access to a node in the middle (i.e. a node that is not the first or the last node, not necessarily the exact middle) of a singly linked list, delete that node.

# Note: IDEA -> Make it LOOK LIKE this node is deleted
# - We don't have access to any incoming pointer
# * => We make sure every pointer going OUT of this node is altered, aka pointed to the next node's pointers
# * => This way, if anyone access `data` or `next`, it's always going to be correct

from _Class import Node, LinkedList

def deleteMiddleNode(node: Node):
    node.data = node.next.data
    node.next = node.next.next
    return

# Example
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
ll = LinkedList(node1)

node1.next = node2
node2.next = node3
node3.next = node4
deleteMiddleNode(node3)
print(ll)
from _Class import LinkedList
# Remove duplicates from an UNSORTED linked list

# 1. Hash
# O(n) and O(n)
# Keep hash table of found elements
def removeDups(ll: LinkedList):
    prev = ll.head
    found = set()

    while prev:
        found.add(prev.data)
        while prev.next and prev.next.data in found:
            prev.next = prev.next.next
        prev = prev.next

    return ll.head

# 2. No extra space
# O(n^2) and O(1)
# Use `cur` pointer to search for each `prev` value
def removeDups(ll: LinkedList):
    if not ll.head or not ll.head.next:
        return

    prev = ll.head
    cur = prev.next
    while prev:
        while cur:
            if cur.data == prev.data:
                prev.next = cur.next
            cur = cur.next
        prev = prev.next

    return


ll = LinkedList(None)
ll.fromList([1, 2, 3, 4, 5])
removeDups(ll)
print(ll)
ll.fromList([1, 1, 2, 3, 1, 2])
removeDups(ll)
print(ll)
ll.fromList([1, 1, 1, 1, 1])
removeDups(ll)
print(ll)
ll.fromList([1])
removeDups(ll)
print(ll)
ll.fromList([])
removeDups(ll)
print(ll)

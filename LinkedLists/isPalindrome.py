# Implement a function to check if a linked list is a palindrome

# Recursion
# Recursively traverse until end of list. Start another pointer at first node when at last node.

from _Class import LinkedList, Node
def isPalindrome(ll: LinkedList) -> bool:
    def rec(rightNode: Node, head: Node):
        if not rightNode: return True, head

        # Recurse
        isPalindrome, leftNode = rec(rightNode.next, head)

        # Check for invalid palindrome found already
        if not isPalindrome or leftNode.data != rightNode.data:
            return False, None
        
        # Still valid palindrome
        return isPalindrome, leftNode.next
    
    result, _ = rec(ll.head, ll.head)
    return result


ll = LinkedList(None)
ll.fromList([])
print(isPalindrome(ll))

ll.fromList([""])
print(isPalindrome(ll))

ll.fromList(["a"])
print(isPalindrome(ll))

ll.fromList(["a", "a"])
print(isPalindrome(ll))

ll.fromList(["a", "b", "a"])
print(isPalindrome(ll))

ll.fromList(["a", "b", "b", "a"])
print(isPalindrome(ll))

ll.fromList(["a", "b", "c", "a"])
print(isPalindrome(ll))

ll.fromList(["a", "b"])
print(isPalindrome(ll))

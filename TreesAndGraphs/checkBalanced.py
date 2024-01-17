# Implement a function to check if a binary tree is balanced. 
# For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one

# * Idea -> At each root, check for balanced-ness by calculating height of left and right sub-trees
# ? Brute Force: Implementing a separate function for calculating height -> O(2^n) due to repeated calls

def solution(root):
   balanced, _ = is_balanced(root)
   return balanced

def is_balanced(root):
   # Base case
   if not root.left and not root.right:
      return True, 1
   
   # Recurse
   left_balanced, left_height = is_balanced(root.left)
   right_balanced, right_height = is_balanced(root.right)

   # Found imbalance at children. Bubble up result
   if not left_balanced or not right_balanced: return False, -1

   # Found imbalance at current root.
   if abs(left_height - right_height) > 1: return False, -1

   return True, max(left_height, right_height)
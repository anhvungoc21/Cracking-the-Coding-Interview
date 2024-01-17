# You are implementing a BST class from scratch which, in addition to insert, find, delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.

# Observations
# ? n nodes -> Each node must have 1/n chance of being picked
# ? Each node has to be aware of how many nodes in the subtree which it is the node
# ? To choose which branch to follow, we also take into account how many nodes there are in that branch

# ? IDEA: The probability of picking a sub-tree to move to must be the sum of each node's probability. k nodes -> k/n

# Mathematical rationale:
# Say we have n nodes in total, x nodes on the left branch, and y nodes on the right branch
# * => Possibility of going left branch is x/n
# *    Then, the possibility of staying at that left node is 1/x
# *    => The accum possibility of choosing that left node is x/n * 1/x = 1/n!!!

import random

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.num_nodes = 1

class RandomBST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        # Special: first node
        if not self.root:
            self.root = new_node
            return
        
        # Find empty space
        cur = self.root
        took_left = True
        while cur:
            # Increment number of nodes
            cur.num_nodes += 1

            prev = cur
            if data < cur.data:
                cur = cur.left
                took_left = True
            else:
                cur = cur.right
                took_left = False

        # Insert 
        if took_left:
            prev.left = new_node
        else:
            prev.right = new_node

    def find(self, data):
        if not self.root: return None

        cur = self.root
        while True:
            if not cur or data == cur.data: return cur
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right

    def random_node(self):
        if not self.root: return None

        cur = self.root
        while True:
            # Get random number in range (0, n-1)
            rand = random.randint(0, cur.num_nodes - 1)

            # Threshold
            left_size = cur.left.num_nodes if cur.left else 0
            
            # Stay
            if rand == left_size: # 1/n
                return cur
            elif rand < left_size: # left_size/n
                cur = cur.left
            else: # right_size/n
                cur = cur.right

    def delete_node_rec(self, root, data):
        if not root: return None

        # Find in left tree
        if data < root.data:
            root.left = self.delete_node_rec(root.left, data)
        # Find in right tree
        elif data > root.data:
            root.right = self.delete_node_rec(root.right, data)
        else:
            # Found node to delete
            # Case 1: Leaf. Simple. Delete
            if not root.left and not root.right: return None

            # Case 2: One child. Simple. Link child to parent node.
            if not root.left: return root.right
            if not root.right: return root.left
            
            # Case 3: Two children
            #   - Identify in-order successor of node
            #     ? Node with smallest key in right sub-tree of node
            #     ?  (left-most descendant)
            #   - Replace the key of given node with successor
            #   - Delete successor
            # ? => This works because there are no keys between the removed node and its successor node
            else:
                replacement = self.find_min(root.right)
                root.data = replacement.data
                root.right = self.delete_min(root.right)

        root.num_nodes -= 1
        return root
    
    # Find left-most node of a branch whose root is `root`
    def find_min(self, root):
        while root.left:
            root = root.left
        return root
    
    # Delete the left-most node of a branch
    def delete_min(self, root):
        if not root: return None

        # Found min. Replace root with root.right
        if not root.left:
            return root.right

        root.left = self.delete_min(root.left)
        return root
          
    def delete(self, data):
        self.delete_node_rec(self.root, data)

    def print_level(self):
        level = [self.root]

        while level:
            next_level = []
            found_data = False
            for node in level:
                if node: 
                    found_data = True
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    next_level.extend([None, None])

            # Found a level with all Nones
            if not found_data:
                return
            
            # Print before moving on
            print([(node.data, node.num_nodes) if node else None for node in level])
            level = next_level

tree = RandomBST()
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(6)
tree.insert(8)

tree.print_level()
tree.delete(7)
tree.print_level()

from collections import defaultdict
found = defaultdict(int)
for _ in range(100000):
    rand = tree.random_node().data
    found[rand] += 1
for item in found.items():
    print(item)
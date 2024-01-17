# You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (travelling only from parent nodes to child nodes).

# Ideas:
# Same as prefix sum problem, just with multiple paths to consider
# ? Idea: DFS with changing prefixSum array updated for each path

from collections import defaultdict

def solution(node, target):
    return paths_with_sum(node, 0, defaultdict(int), target)

def paths_with_sum(node, accum, sums, target):
    if not node:
        return 0

    count = 0

    # Current sum from root to this node
    cur_sum = node.data + accum
    if cur_sum == target:
        count += + 1

    # Find inner subarrays
    if cur_sum - target in sums:
        count += sums[cur_sum - target]

    # Add current sum to count
    sums[cur_sum] += 1
        
    # Recurse
    # Note: Instead of creating copies. Could wait for left/right to return then -= 1 the left/right sum
    sums_left = sums.copy()
    sums_right = sums.copy()

    return (count +
            paths_with_sum(node.left, cur_sum, sums_left, target) +
            paths_with_sum(node.right, cur_sum, sums_right, target))


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

root = Node(10,
            Node(5,
                 Node(3,
                      Node(3, None, None),
                      Node(-2, None, None)),
                 Node(2,
                      None,
                      Node(1, None, None))),
            Node(-3, 
                 None, 
                 Node(11, None, None)))

print(solution(root, 8))
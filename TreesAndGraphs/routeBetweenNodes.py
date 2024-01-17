# Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.

# Graph
# .nodes

# Node
# .neighbors


from collections import deque

def solution(graph, start, end):
    # Initialization
    for node in graph:
        node.visited = False

    queue = deque([start])
    start.visited = True

    while queue:
        node = queue.popleft()

        # What is that route? Might be a good follow-up
        if node == end:
            return True
        
        # Explore paths
        for neighbor in node.neighbors:
            if neighbor.visited: continue
            queue.append(neighbor)
            neighbor.visited = True

    return False

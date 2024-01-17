# You are given a list of projects and a list of dependencies which is a list of pairs of projects, where the second project is dependent on the first project.
# All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built.
# If there is no valid build, return an error.

# ? => Idea: Post-order DFS to build all dependencies before depender


from collections import defaultdict, deque

# Approach 1: Topological sorting
# Each incoming edge a->b represents: "a comes before b"
def solution(projects, dependencies):
    order = []

    # Build incoming edges and dependencies count
    edges = {}
    incoming = {}
    for project in projects:
        edges[project] = set()
        incoming[project] = 0
    for first, second in dependencies:
        edges[first].add(second)
        incoming[second] += 1

    # Process and build projects with no dependencies
    queue = deque([])
    for project in projects:
        if incoming[project] == 0:
            queue.append(project)
            order.append(project)

    # Build projects with no dependencies iteratively
    while queue:
        cur = queue.popleft()

        # Remove current. Means remove edge to child
        # This decrements the child's incoming
        for child in edges[cur]:
            incoming[child] -= 1

            # Process child if 0 incoming
            if incoming[child] == 0:
                order.append(child)
                queue.append(child)

    # If can't build any project (queue is empty) and haven't built all, invalid!
    return order if len(order) == len(projects) else "Error"

# Approach 2: Post-order DFS
# ? Projects at the end of the DFS chain are built last
# ? Once we return from a DFS call, we can safely build a project LAST
def solution(projects, dependencies):
    visited = set()
    visiting = set()
    order = []

    # Initialize graph
    edges = {}
    for project in projects:
        edges[project] = set()
    for first, second in dependencies:
        edges[first].add(second)
    
    # Exhaustive DFS
    for project in projects:
        if not dfs(project, visited, visiting, edges, order): 
            return "Error"

    return order[::-1]

def dfs(project, visited, visiting, edges, order):
    # Don't rebuild projects
    if project in visited: return True
    
    # DFS from this project
    stack = [project]

    while stack:
        node = stack.pop()
        if node in visited: continue

        # First seen. Process children first
        if node not in visiting:
            stack.append(node)
            visiting.add(node)
            for child in edges[node]:
                if child in visiting: 
                    return False
                stack.append(child)

        # Second seen. Safely build node
        else:
            visiting.remove(node)
            visited.add(node)
            order.append(node)
    
    return True

# Approach 3: Post-order DFS but the other way around
# ? Edge means "depends on"
# ? Once we return from a DFS call, we can safely build a project FIRST because its children have been built
def solution(projects, dependencies):
    visited = set()
    visiting = set()
    order = []

    # Initialize graph
    edges = {}
    for project in projects:
        edges[project] = set()
    for first, second in dependencies:
        edges[second].add(first)

    # Exhaustive DFS
    for project in projects:
        if not dfs(project, visited, visiting, edges, order): 
            return "Error"

    return order

def dfs(project, visited, visiting, edges, order):
    # Don't rebuild projects
    if project in visited: return True
    
    # DFS from this project
    stack = [project]

    while stack:
        node = stack.pop()
        if node in visited: continue

        # First seen. Process children first
        if node not in visiting:
            stack.append(node)
            visiting.add(node)
            for child in edges[node]:
                if child in visiting: 
                    return False
                stack.append(child)

        # Second seen. Safely build node
        else:
            visiting.remove(node)
            visited.add(node)
            order.append(node)
    
    return True

print(solution(["a", "b", "c", "d", "e", "f"],
               [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]))

print(solution(["f", "c", "b", "a", "e", "d", "g"],
               [("f", "c"), ("f", "b"), ("f", "a"), ("c", "a"), ("b", "a"), ("a", "e"), ("b", "e"), ("d", "g")]))

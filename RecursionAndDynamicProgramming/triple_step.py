# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs

# * 1. Naive
# Time: Each node spawns 3 children => 3^steps
# Space (Recursion): O(steps)
def solution(steps):
    # Invalid
    if steps < 0:
        return 0
    
    # Reached
    if steps == 0:
        return 1
    
    # Take all choices
    return solution(steps - 1) + solution(steps - 2) + solution(steps - 3)

# * 2. Memoization (top-down)
# Time: O(steps)
# Space: O(steps) for recursion & O(steps) for memo 
def solution(steps):
    memo = [0] * (steps + 1)

    # Base cases
    memo[0] = 0
    memo[1] = 1
    memo[2] = 2
    return rec(steps, memo)

def rec(steps, memo):
    if steps < 0: return 0

    # Calculated before
    if memo[steps] > 0: return memo[steps]

    # Calculate and store result
    result = rec(steps - 1, memo) + rec(steps - 2, memo) + rec(steps - 3, memo)
    memo[steps] = result
    return result

# * 3. DP (bottom-up)
# Time: O(steps)
# Space: O(steps)
def solution(steps):
    table = [0] * (steps + 1)

    # Fill in base cases
    table[0] = 0
    table[1] = 1
    table[2] = 2

    # Build
    for i in range(3, steps + 1):
        table[i] = table[i - 1] + table[i - 2] + table[i - 3]

    return table[steps]


print(solution(5))

# 1 -> 2 -> 1
# 1 -> 3
# 1 -> 1 -> 1 -> 1
# 1 -> 1 -> 2
# 2 -> 1 -> 1
# 2 -> 2
# 3 -> 1
# Write a method to compute all permutations of a string of unique characters

# Base case and Build

# n = 0: ""
# n = 1: a1
# n = 2: a1a2, 
#        a2a1
# n = 3: a1a2a3, a1a3a2, a3a1a2,
#        a2a1a3, a2a3a1, a3a2a1
# * => P(n) is inserting new character at every possible location of each permutation in P(n - 1)

# Build P(n) from first P(n - 1) by inserting char-n
def solution(s):
    return permutations(s, 0, len(s))

# Time: O(n!) leaf nodes * O(n) nodes on each path * O(n) work on each node => O((n + 2!)
# Space: O(n!) for result because for each level of the tree, there's an additional branch
def permutations(s, start, end):
    if start == end: return [""]

    # Recurse
    perms = permutations(s, start, end - 1)

    results = []
    char = s[end - 1]
    # Insert character
    for perm in perms:
        for i in range(len(perm) + 1): # + 1 because append to end
            left = perm[:i]
            right = perm[i:]
            results.append(left + char + right)
    
    return results

print(solution("abc"))

# Alternate Approach
# Build P(n) from all P(n - 1)s by prepending char-i
def solution(s):
    result = []
    permutations("", s, result)
    return result

def permutations(prefix, remainder, result):
    # Chain of prefix is result
    if len(remainder) == 0: result.append(prefix)

    # Use each character as prepend
    for i in range(len(remainder)):
        before = remainder[:i]
        after = remainder[i+1:]
        char = remainder[i]
        
        permutations(prefix + char, before + after, result)
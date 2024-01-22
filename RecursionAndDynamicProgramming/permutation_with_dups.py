# Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates.

# Approach
# - Instead of operating character by character, we operate by their count
# => Choose a starting character. Then, prepend that to all permutations of the remaining characters

from collections import Counter
def solution(s):
    result = []
    letters = Counter(s)
    permutations(letters, "", len(s), result)
    return result

def permutations(letters, prefix, remaining, result):
    # Reached end of chain. Add result
    if remaining == 0:
        result.append(prefix)
        return
    
    # Pick a character to prepend
    for char in letters.keys():
        if letters[char] == 0: continue

        # "Use" char
        letters[char] -= 1
        permutations(letters, prefix + char, remaining - 1, result)

        # "Unuse" char for next for-loop iteration
        letters[char] += 1
    

print(solution("aabc"))
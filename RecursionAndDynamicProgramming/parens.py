# Implement an algorithm to print all valid (i.e. properly opened and closed) combinations of n pairs of parentheses.

# Base case and build

# 0 -> ""
# 1 -> ()
# 2 -> (()), # 2 insertions
#      ()()
# 3 -> ()(()), (()()), ((())),
#      ()()(), (())(), ()(())
# * => Observation: Can insert a pair after an opening paren. But this creates duplicates that we can't quite check for

# * Approach: Build string from scratch
# At any step, we can insert either a left or right paren
# - Can always insert a left paren as long as there is space left
# - Can insert a right paren when there are left parents to be closed
# => Keep track of the number of left and right parens to be inserted

def solution(n):
    result = []
    parens(n, n, [], result)
    return result

def parens(left, right, prefix, result):
    # Invalid
    if left < 0 or right < left: return

    # Out of parens to add. Save result
    if left == 0 and right == 0: 
        result.append("".join(prefix))
        return 
    
    # Recurse left
    prefix.append("(")
    parens(left - 1, right, prefix, result)
    prefix.pop()

    # Recurse right
    prefix.append(")")
    parens(left, right - 1, prefix, result)
    prefix.pop()

print(solution(3))




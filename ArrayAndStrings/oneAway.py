
# There are 3 types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Given 2 strings, write a function to check if they are one (or zero) edit away from being the same

# 1. Iterate and check
# O(n) & O(1)
def oneAway(s1, s2):
    p1 = len(s1) - 1
    p2 = len(s2) - 1

    # Traverse until find difference
    while p1 >= 0 and p2 >= 0 and s1[p1] == s2[p2]:
        p1 -= 1
        p2 -= 1

    # Check for equality (no edits):
    if p1 == p2 == 0:
        return True

    # Consider 3 choices -- Compare the rest of the string AFTER making a change
    replace = s1[:p1-1] == s2[:p2-1]
    remove = s1[:p1-1] == s2[:p2]
    insert = s1[:p1] == s2[:p2-1]

    return replace or remove or insert


print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))

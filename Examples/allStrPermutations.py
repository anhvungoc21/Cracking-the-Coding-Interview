# Design an algorithm to print all permutations of a string. For simplicity, assume all characters are unique.

def insertCharInStr(s, char):
    perms = []
    for pos in range(len(s) + 1):
        left = s[:pos]
        right = s[pos:]
        perms.append(left + char + right)

    return perms

def insertCharInStrs(strs, char):
    perms = []
    for s in strs:
        perms.extend(insertCharInStr(s, char))
    return perms


def getPermutations(s):
    # Base case:
    if len(s) <= 1:
        return s

    # Recurse
    char = s[-1]
    lastPerms = getPermutations(s[:-1])
    perms = insertCharInStrs(lastPerms, char)

    return perms


def printPermutations(s):
    print(getPermutations(s))
    return


print(getPermutations("ab"))

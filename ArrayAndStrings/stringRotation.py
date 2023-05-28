# Assume you had a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring. e.g. "waterbottle" is a rotation of "erbottlewat"

# Helper - Tests if s1 is a substring of s2
def isSubstring(s1: str, s2: str):

    pos = 0
    for pos in range(len(s2) - len(s1)):
        if (s1[0] == s2[pos]) and (s2[pos:pos+len(s1)] == s1):
            return True
    return False

# Clever
# Note: Idea -> When a rotation of a string is concatenated to itself, the original string is formed somewhere inside
# Note: There is a "cutting" point somewhere that separates the original string into 2 halves. These can be re-joined as stated above.
# O(n) & O(n)]

def isStringRotation(s1: str, s2: str):
    # Prior checks
    if len(s1) != len(s2):
        return False

    s = s2 + s2
    return isSubstring(s1, s)


print(isStringRotation("waterbottle", "erbottlewat"))

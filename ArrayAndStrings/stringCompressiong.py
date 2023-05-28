# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).

# 1. StringBuilder
# O(n) & O(k)
# k is the number of unique letters. This is always < 26, so maybe O(1)?
def stringCompression_naive(s):
    compressed = []

    curChar = s[0]
    curCount = 1
    for char in s[1:]:
        if char == curChar:
            curCount += 1
        else:
            compressed.append(curChar)
            compressed.append(str(curCount))
            curChar = char
            curCount = 1

    # Add the final group of characters
    compressed.append(curChar)
    compressed.append(str(curCount))

    return "".join(compressed) if len(compressed) < len(s) else s


print(stringCompression_naive("aabcccccaaa"))
print(stringCompression_naive("abcdefgh"))

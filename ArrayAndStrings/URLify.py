# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

# 1. Create new string
# O(n) & O(n)
def URLify_naive(s):
    url = []
    for char in s:
        if char == " ":
            url.append('%20')
        else:
            url.append(char)

    return "".join(url)

# print(URLify_naive("Mr John Smith"))


# 2. Modify in-place
# O(n) & O(1)
def URLify_inplace(s):
    s = list(s)  # Python does not support mutating strings

    # Iterate over each character of the "real" length
    last = len(s) - 1
    lastSpace = last

    # Skip through all end spaces.
    while s[last] == ' ':
        last -= 1

    # Swap and replace
    for i in range(last, -1, -1):
        # Note: Unnecessary -- If a swap just occured, move pointer i to next non-space character
        # * Because whenever i is at a space, it's a REAL space. The next iteration moves on to a non-space character.

        # Swap non-space character to end
        if s[i] != ' ':
            temp = s[i]
            s[i] = s[lastSpace]
            s[lastSpace] = temp
            lastSpace -= 1

        # Replace space with `%20`. Update pointer to lastSpace.
        else:
            s[lastSpace] = '0'
            s[lastSpace - 1] = '2'
            s[lastSpace - 2] = '%'
            lastSpace -= 3

        i -= 1

    return "".join(s)


print(URLify_inplace("Mr John Smith    "))

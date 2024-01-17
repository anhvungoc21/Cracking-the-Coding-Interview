# Write a function to determine the number of bits you would need to flip to convert integer A to integer B

# * Idea: Number of bits to flip = Number of 1s in XOR

def solution(A, B):
    xor = A ^ B

    count = 0
    while xor > 0:

        # Note: This clever trick clears the right-most "1"
        # e.g. 100100 (x)
        #      100011 (x - 1)
        #  & = 100000   
        xor = xor & (xor - 1)
        count += 1

        # Otherwise, could just check and shift right by 1 every time
        # count += xor & 1
        # xor >>= 1

    return count
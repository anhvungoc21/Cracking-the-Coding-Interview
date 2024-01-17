# You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.

def solution(num):
    cur_length = 0
    prev_length = 0
    max_length = 0

    # Check each bit from right to left
    # This direction because it's more convenient to check least-significant bit
    while num > 0:
        # Check for right-most 1
        if ((num & 1) == 1):
            cur_length += 1

        # Found 0. Check another bit
        else:
            # If second bit is 1. Then we can bridge prev_length and cur_length
            # prev_length is now the first sequence of 1s
            # cur_length is now the second sequence of 1s
            prev_length = 0 if ((num & 2) == 0) else cur_length # Note: Careful about this check! Reversing the ternary is not trivial.
            cur_length = 0

        # Update
        max_length = max(max_length, prev_length + cur_length + 1)

        # Check next bit
        num >>= 1

    return max_length

print(solution(int("1111100111111", 2)))
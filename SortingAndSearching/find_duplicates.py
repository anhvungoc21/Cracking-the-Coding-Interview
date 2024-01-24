# You have an array with all numbers from 1 to N, where N is at most 32,000. The array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory available, how would you print all duplicate elements in the array?

# Observations:
# - N is at most 32,000 => ~ <2^15 bits needed to represent
# - We have 4 * 8 (bits/byte) * 2^10(1024) > 2^15
# => We can represent each integer with one bit. When there's a set bit, just print the corresponding number

def solution(arr):
    bs = BitSet(32000)
    for num in arr:
        num0 = num - 1 # Numbers 1-n but bits start at 0 

        if bs.get(num0):
            print(num)
        else:
            bs.set(num0)


class BitSet:
    def __init__(self, size):
        self.bitset = [0 for _ in range(size // 32 + 1)]

    def get(self, pos):
        # word * 32 + bit = pos
        word_idx = pos // 32
        bit_idx = pos % 32

        # Check set bit
        return (self.bitset[word_idx] & (1 << bit_idx)) != 0

    def set(self, pos):
        word_idx = pos // 32
        bit_idx = pos % 32
        self.bitset[word_idx] |= (1 << bit_idx)



# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e. each disk sits on top of an even larger one). You have the following constraints:
# (1) Only one disk can be moved at a time
# (2) A disk is slid off the top of one tower onto another tower
# (3) A disk cannot be placed on top of a smaller disk
# Write a program to move the disks from the first tower to the last using Stacks.

# 1 disk - base case
# [_] [] []
# [] [] [_]

# 2 disks
# [_-] [] []
# [_] [-] []
# [] [-] [_]
# [] [] [- _]

# * >= 2 disks => Move largest disk, then move n - 1

def solution(n):
    tower = [k for k in range(1, n + 1)]
    buffer = []
    dest = []

    tower_of_hanoi(n, tower, buffer, dest)
    return tower, buffer, dest

def tower_of_hanoi(num_disks, tower, buffer, dest):    
    # Base case:
    if num_disks <= 0: return

    # Move n - 1 disks to buffer
    tower_of_hanoi(num_disks - 1, tower, dest, buffer)

    # Move largest disk to dest
    dest.append(tower.pop())

    # Move n - 1 disks from buffer to dest
    tower_of_hanoi(num_disks - 1, buffer, tower, dest)

print(solution(5))
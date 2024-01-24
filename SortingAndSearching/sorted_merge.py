# You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

# Observations:
# A: [1 3 7 _ _]
# B: [2 5]
# -> [1 3 _ _ 7] -> [1 3 _ 5 7] -> [1 _ 3 5 7] -> [1 2 3 5 7]
# => Inserting in an ascending order is a bad idea due to shifting
# => Descending order!

def solution(A, B, countA):
    p_B = len(B) - 1
    p_A = countA - 1
    p_buffer = len(A) - 1

    while p_B >= 0:
        # Compare A and B
        if A[p_A] > B[p_B]:
            A[p_buffer] = A[p_A]
            A[p_A] = None
            
            p_A -= 1
        
        else:
            A[p_buffer] = B[p_B]
            B[p_B] = None

            p_B -= 1

        p_buffer -= 1

A = [None for _ in range(5)]
A[0] = 1
A[1] = 3
A[2] = 7
B = [2, 5]

solution(A, B, 3)
print(A, B)



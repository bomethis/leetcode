class Solution:
    def flipAndInvertImage(A):
        i = 0
        j = 0
        B = []
        C = []
        for i in range(len(A)):
            for j in range(len(A[i])):
                P = A[i].pop()       # reverse order by .pop() method into list B
                if P == 0:           # Invering 0s and 1s within for loop
                    P = 1
                else:
                    P = 0
                B.append(P)
                j += 1
            C.append(B)             # insert list B containing the reversed and inverted values into list C
            i += 1
            j = 0
            B = []
        return C

#Test
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print(Solution.flipAndInvertImage(A))


# Runtime: 44 ms, faster than 94.83% of Python3 online submissions for Flipping an Image.
# Memory Usage: 13.1 MB, less than 75.51% of Python3 online submissions for Flipping an Image.

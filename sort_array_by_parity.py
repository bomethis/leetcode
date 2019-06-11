class Solution:
    def sortArrayByParity(A):
        j = 0
        for i in range(len(A)):  # Sort/swap in place
            while A[i] % 2 != 0:
                A.append(A.pop(i))
                j += 1
                if j >= len(A):
                    return A
            else:
                i += 1
                j += 1

#test
A = [9,7,5,3,1,4]
print(Solution.sortArrayByParity(A))


# Success
# Details
# Runtime: 76 ms, faster than 36.33% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 13.7 MB, less than 63.05% of Python3 online submissions for Sort Array By Parity.

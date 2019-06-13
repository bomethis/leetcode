class Solution:
    def sortedSquares(A):
        for i in range(len(A)):  # sorting in place the square of each num
            in_place = 0
            num = A.pop(in_place)
            squared_num = num**2
            A.append(squared_num)

        return sorted(A)



A = [-7,-3,2,3,11]
print(Solution.sortedSquares(A))

#
# Runtime: 316 ms, faster than 5.33% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 14.6 MB, less than 97.65% of Python3 online submissions for Squares of a Sorted Array.

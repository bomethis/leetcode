class Solution:
    def repeatedNTimes(A):
        unique_nums = len(set(A))
        N = unique_nums - 1
        sorted_list = sorted(A)
        unique = 0
        for i in range(unique_nums):
            if sorted_list[unique] == sorted_list[unique + N]:
                return sorted_list[i]
            else:
                unique += N


A = [5,1,5,2,5,3,5,4]
print(Solution.repeatedNTimes(A))

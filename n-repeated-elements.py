class Solution:
    def repeatedNTimes(A):
        unique_nums = len(set(A))
        N = unique_nums - 1
        sorted_list = sorted(A)

        for i in range(len(N)):
            count = 1
            while sorted_list[i] == sorted_list[i+1]:
                count += 1
                if count == N:
                    return sorted_list[i]


A = [5,1,5,2,5,3,5,4]
print(Solution.repeatedNTimes(A))

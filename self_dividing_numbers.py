class Solution:
    def selfDividingNumbers(left, right):
        self_divs = []
        for i in range(left, right+1):
            j_count = 0
            length_i = len(str(i))
            for j in str(i):
                if int(j) == 0:
                    break
                if int(i) % int(j) == 0:
                    j_count += 1
                else:
                    break
            if j_count == length_i:
                self_divs.append(i)

        return self_divs

print(Solution.selfDividingNumbers(1, 22))


# Success
# Details
# Runtime: 68 ms, faster than 45.30% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.3 MB, less than 25.36% of Python3 online submissions for Self Dividing Numbers.

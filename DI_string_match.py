class Solution:
    def diStringMatch(S):
        len_s = len(S)
        sorted_li = list(range(len_s+1))
        out_li = []
        # return sorted_li
        for i in range(len_s):
            if S[i] == "D":
                out_li.append(sorted_li.pop())
            else:
                out_li.append(sorted_li.pop(0))

        out_li.append(sorted_li.pop())

        return out_li


S = "DDI"
print(Solution.diStringMatch(S))


# Success
# Details
# Runtime: 100 ms, faster than 31.94% of Python3 online submissions for DI String Match.
# Memory Usage: 14.2 MB, less than 69.01% of Python3 online submissions for DI String Match.

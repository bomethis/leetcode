class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # using list comprehension // Love Python
        li = [aS for aS in S if aS in J]

        return len(li)

#run test
s = Solution()
print(s.numJewelsInStones("aJSiI", "ajId"))


# My Leetcode submissions Summary
# Success
# Details
# Runtime: 20 ms, faster than 87.07% of Python online submissions for Jewels and Stones.
# Memory Usage: 11.7 MB, less than 81.18% of Python online submissions for Jewels and Stones.

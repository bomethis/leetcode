class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """


# using recursion
        def depth_first_search(root):
            if root is None:
                return
            if L <= root.val <= R:
                self.sum += root.val
            if L < root.val:
                depth_first_search(root.left)
            if root.val < R:
                depth_first_search(root.right)

        self.sum = 0
        depth_first_search(root)
        return self.sum






#         Success
# Details
# Runtime: 280 ms, faster than 59.53% of Python online submissions for Range Sum of BST.
# Memory Usage: 28.2 MB, less than 30.06% of Python online submissions for Range Sum of BST.

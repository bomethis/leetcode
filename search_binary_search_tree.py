class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        rNode = [None]
        def dfs(Node):
            if Node is None:
                return
            if Node.val == val:
                rNode[0] = Node
            dfs(Node.left)
            dfs(Node.right)
        dfs(root)    
        return rNode[0]

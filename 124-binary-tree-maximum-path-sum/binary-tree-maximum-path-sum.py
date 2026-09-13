# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.max_sum = float('-inf')


        def dfs(root):

            if root is None:
                return 0

            s_left  = max(dfs(root.left), 0)
            s_right = max(dfs(root.right), 0)
            
            self.max_sum  = max(self.max_sum , root.val + s_left+s_right)
            return root.val + max(s_left, s_right)

        dfs(root)

        return self.max_sum








        
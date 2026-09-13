# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        self.ans = 0



        def dfs(root,curr_max):

            if root is None:
                return

            if root.val>=curr_max:
                self.ans += 1

            dfs(root.left,max(root.val,curr_max))
            dfs(root.right,max(root.val,curr_max))

        dfs(root, float('-inf'))

        return self.ans

                

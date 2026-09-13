# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        self.flag = True


        def dfs(root,min_val,max_val):

            if self.flag == False or root is None:
                return


            if not (min_val < root.val < max_val):
                self.flag = False
                return

            dfs(root.left,min_val, root.val)
            dfs(root.right,root.val, max_val)

        dfs(root,-float('infinity'),float('infinity'))


        return self.flag











        # self.flag = True

        # def dfs(root):
        #     if root is None:
        #         return

        #     if root.left:

        #         if root.left.val>root.val or root.left.val==root.val:
        #             self.flag = False

        #     if root.right:

        #         if root.right.val<root.val or root.right.val==root.val:
        #             self.flag = False
            

        #     dfs(root.left)
        #     dfs(root.right)

        # dfs(root)
        # return self.flag
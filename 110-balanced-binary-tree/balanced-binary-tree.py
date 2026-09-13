# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        self.balanced_flag = True



        def height(root):
            if root is None:
                return 0

            h_l = height(root.left)
            h_r = height(root.right)

            # print(abs(h_l-h_r))

            if abs(h_l-h_r)>1:
                self.balanced_flag = False


            return 1+max(h_l,h_r)


        height(root)
        return self.balanced_flag
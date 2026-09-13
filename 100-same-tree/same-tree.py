# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        self.flag = True


        def check_same(p,q):
            if p is None and q is None:
                return

            elif (p is None and q is not None) or (p is not None and q is None):
                self.flag = False
                return

            elif p.val!=q.val:
                self.flag = False
                return

            check_same(p.left,q.left)
            check_same(p.right,q.right)

        check_same(p,q)
        return self.flag




                


        
        
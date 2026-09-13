# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        # Check whether same

        def same_tree(p,q):

            if p is None and q is None:
                return True
            
            elif (p is None and q is not None) or (p is not None and q is None):
                return False

            elif p.val!=q.val:
                return False

            f_l = same_tree(p.left,q.left)
            f_r = same_tree(p.right,q.right)

            return f_l and f_r


        if root is None:
            if subRoot is None:
                return True
            else:
                return False

        if same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        






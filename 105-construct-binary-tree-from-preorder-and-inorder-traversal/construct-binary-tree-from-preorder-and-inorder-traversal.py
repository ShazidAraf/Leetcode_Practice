# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        self.p = 0

        pos = {v:i for i,v in enumerate(inorder)}
        # print(pos)

        def build(low,high):

            if low>high:
                return None

            val = preorder[self.p]
            self.p+=1
            root = TreeNode(val)
            root.left = build(low,pos[val]-1)
            root.right = build(pos[val]+1,high)
            return root

        return build(0,len(preorder)-1)
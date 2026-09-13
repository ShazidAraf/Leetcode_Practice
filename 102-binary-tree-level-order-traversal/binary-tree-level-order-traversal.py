# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        H = defaultdict(list)

        def dfs(root,level):

            if root is None:
                return 

            H[level].append(root.val)

            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root,0)


        return list(H.values())

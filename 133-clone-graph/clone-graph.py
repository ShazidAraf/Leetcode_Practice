"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """


        if node is None:
            return None



        H = {}


        def dfs(node):

            if node in H:
                return H[node]

            copy_ = Node(node.val)
            H[node] = copy_

            for nei in node.neighbors:
                copy_.neighbors.append(dfs(nei))

            return copy_

        
        copy_ = dfs(node)

        return copy_
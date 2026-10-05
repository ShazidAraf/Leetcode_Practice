class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        n = len(edges)
        graph = {i:[] for i in range(1,n+1)}

        visiting = set()
        visited = set()


        def dfs(node,parent):

            visiting.add(node)

            for nei in graph[node]:

                if nei==parent:
                    continue

                if nei in visiting:
                    return True

                if dfs(nei,node):
                    return True

            visiting.remove(node)

            return False




        for a,b in edges:

            graph[a].append(b)
            graph[b].append(a)

            if dfs(a,-1):
                return [a,b]
        
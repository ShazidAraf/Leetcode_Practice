class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        graph = {i: [] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visiting = set()
        visited = set()

        # print(graph)

        def dfs(node,parent):

            if node in visited:
                return False

            visiting.add(node)

            for nei in graph[node]:

                if nei==parent:
                    continue

                if nei in visiting:
                    return True
                if dfs(nei,node):
                    return True

            visiting.remove(node)
            visited.add(node)

            return False


        flag = dfs(0,-1)

        # print(visited)

        if flag or len(visited)<n:
            return False
        else:
            return True






        
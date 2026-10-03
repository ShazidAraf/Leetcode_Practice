class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """


        graph = {i:[] for i in range(n)}

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)


        visit = [False]*n

        def dfs(node):

            visit[node] = True

            for nei in graph[node]:

                if not visit[nei]:
                    dfs(nei)

        count = 0


        for i in range(n):

            if not visit[i]:
                dfs(i)
                count+=1


        return count






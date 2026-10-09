class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        H1 = collections.defaultdict(list)
        for u, v, w in times:
            H1[u].append((v, w))              # forward edges

        cost = {}                             # plain dict
        def dfs(node, d):                     # d = time to reach node on this path
            if node in cost and cost[node] <= d:
                return                        # already reached faster
            cost[node] = d
            for nei, w in H1[node]:
                dfs(nei, d + w)

        dfs(k, 0)                             # actually call it
        return -1 if len(cost) < n else max(cost.values())


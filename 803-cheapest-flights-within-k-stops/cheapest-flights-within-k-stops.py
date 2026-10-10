class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """


        cost = [float('inf') for i in range(n)]
        cost[src] = 0

        tmp = cost[:]


        for i in range(k+1):
            cost = tmp[:]
            for u,v,w in flights:
                if cost[u] + w < tmp[v]:
                    tmp[v] = cost[u] + w

        cost = tmp[:]

        if cost[dst]==float('inf'):
            return -1
        else:
            return cost[dst]




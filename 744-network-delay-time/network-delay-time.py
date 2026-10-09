class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        Graph = collections.defaultdict(list)


        for u,v,w in times:
            Graph[u].append([v,w])


        minheap = [[0,k]]
        visit = set()
        t = 0



        while minheap:

            path_cost,node = heapq.heappop(minheap)

            if node in visit:
                continue

            visit.add(node)
            t = max(t,path_cost)

            for nei,cost in Graph[node]:

                if nei in visit:
                    continue
                heapq.heappush(minheap, [path_cost + cost, nei])

        if len(visit)<n:
            return -1
        else:
            return t

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        graph = {i:[] for i in range(n)}

        for i in range(n):
            for j in range(i+1,n):

                d = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                graph[i].append([d,j])
                graph[j].append([d,i])

        # print(graph)

        minheap = [[0,0]]
        visit = set()
        res = 0

        while len(visit)<n:

            cost,node = heapq.heappop(minheap)

            if node in visit:
                continue

            visit.add(node)
            res += cost

            for cost_ , nei in graph[node]:

                if nei in visit:
                    continue
                heapq.heappush(minheap,[cost_ , nei])
                

        return res

        